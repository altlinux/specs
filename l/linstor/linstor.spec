%define GRADLE_TASKS installdist
%define GRADLE_FLAGS --offline --gradle-user-home /tmp --no-daemon -Pjava11=true --exclude-task generateJava
%define LS_PREFIX %_datadir/linstor-server
%define FIREWALLD_SERVICES %_usr/lib/firewalld/services
%define NAME_VERS %name-server-%version

# Prevent brp-java-repack-jars from being run.
%define __jar_repack %nil

Name: linstor
Version: 1.29.1
Release: alt1
Summary: DRBD replicated volume manager
Group: System/Servers
License: GPLv2+
Url: https://github.com/LINBIT/linstor-server
Source0: http://www.linbit.com/downloads/linstor/linstor-server-%version.tar.gz
Source1: gradle-8.2.1-bin.zip
# Source1: gradle-6.7-bin.zip
BuildArch: noarch

BuildRequires(pre): /proc rpm-build-java jpackage-utils
BuildRequires: java-11-openjdk-devel
BuildRequires: python3
BuildRequires: unzip
#BuildRequires: gradle

%description
LINSTOR developed by LINBIT, is a software that manages replicated volumes across a group of machines.
With native integration to Kubernetes, LINSTOR makes building, running, and controlling block storage simple.
LINSTOR is open-source software designed to manage block storage devices for large Linux server clusters.
It's used to provide persistent Linux block storage for cloudnative and hypervisor environments.

%prep
%setup -n %NAME_VERS -a1

%build
# export PATH=$PWD/gradle-6.7/bin:$PATH
export PATH=$PWD/gradle-8.2.1/bin:$PATH
gradle %GRADLE_TASKS %GRADLE_FLAGS
#for p in server satellite controller; do echo "%%LS_PREFIX/.$p" >> "%%_builddir/%%NAME_VERS/$p/jar.deps"; done

%install
mkdir -p %buildroot%LS_PREFIX
cp -r %_builddir/%NAME_VERS/build/install/linstor-server/lib %buildroot%LS_PREFIX
rm %buildroot/%LS_PREFIX/lib/%NAME_VERS.jar
chmod a-x %buildroot/%LS_PREFIX/lib/*.jar
mkdir -p %buildroot/%LS_PREFIX/lib/conf
cp %_builddir/%NAME_VERS/server/logback.xml %buildroot/%LS_PREFIX/lib/conf
mkdir -p %buildroot%LS_PREFIX/bin
cp -r %_builddir/%NAME_VERS/build/install/linstor-server/bin/Controller %buildroot%LS_PREFIX/bin
cp -r %_builddir/%NAME_VERS/build/install/linstor-server/bin/Satellite %buildroot%LS_PREFIX/bin
cp -r %_builddir/%NAME_VERS/build/install/linstor-server/bin/linstor-config %buildroot%LS_PREFIX/bin
cp -r %_builddir/%NAME_VERS/build/install/linstor-server/bin/linstor-database %buildroot/%LS_PREFIX/bin
cp -r %_builddir/%NAME_VERS/scripts/postinstall.sh %buildroot%LS_PREFIX/bin/controller.postinst.sh
mkdir -p %buildroot%_unitdir
sed -i '/\[Service\]/a Environment="JAVA_HOME=/usr/lib/jvm/jre-11-openjdk"' %_builddir/%NAME_VERS/scripts/linstor-*.service
cp -r %_builddir/%NAME_VERS/scripts/linstor-controller.service %buildroot%_unitdir
cp -r %_builddir/%NAME_VERS/scripts/linstor-satellite.service %buildroot%_unitdir
mkdir -p %buildroot%FIREWALLD_SERVICES
cp %_builddir/%NAME_VERS/scripts/firewalld/drbd.xml %buildroot%FIREWALLD_SERVICES
cp %_builddir/%NAME_VERS/scripts/firewalld/linstor-controller.xml %buildroot%FIREWALLD_SERVICES
cp %_builddir/%NAME_VERS/scripts/firewalld/linstor-satellite.xml %buildroot%FIREWALLD_SERVICES
mkdir -p %buildroot%_sysconfdir/drbd.d/
cp %_builddir/%NAME_VERS/scripts/linstor-resources.res %buildroot%_sysconfdir/drbd.d/
#touch %%buildroot%%LS_PREFIX/{.server,.satellite,.controller}
mkdir -p %buildroot%_sysconfdir/linstor
cp %_builddir/%NAME_VERS/docs/linstor.toml-example %buildroot%_sysconfdir/linstor/
touch %buildroot%_sysconfdir/linstor/linstor.toml
mkdir -p %buildroot/var/lib/linstor

### common
%package common
Summary: Common files shared between controller and satellite
Group: System/Servers
Requires: java-11-openjdk-headless

%description common
Linstor shared components between linstor-controller and linstor-satellite

%files common -f server/jar.deps
%dir %LS_PREFIX
%dir %LS_PREFIX/lib
%LS_PREFIX/lib/server-%version.jar
%LS_PREFIX/lib/jclcrypto-%version.jar
%dir %LS_PREFIX/lib/conf
%LS_PREFIX/lib/conf/logback.xml
%dir /var/lib/linstor
%dir %_sysconfdir/linstor

### controller
%package controller
Summary: Linstor controller specific files
Group: System/Servers
Requires: linstor-common = %EVR

%description controller
Linstor controller manages linstor satellites and persistant data storage.

%files controller -f controller/jar.deps
%dir %LS_PREFIX
%dir %LS_PREFIX/lib
%LS_PREFIX/lib/controller-%version.jar
%dir %LS_PREFIX/bin
%LS_PREFIX/bin/Controller
%LS_PREFIX/bin/linstor-config
%LS_PREFIX/bin/linstor-database
%LS_PREFIX/bin/controller.postinst.sh
%_unitdir/linstor-controller.service
%FIREWALLD_SERVICES/linstor-controller.xml
%_sysconfdir/linstor/linstor.toml-example
%ghost %config(noreplace) %_sysconfdir/linstor/linstor.toml


%post controller
%LS_PREFIX/bin/controller.postinst.sh
%post_service linstor-controller
#test -f %%_bindir/firewall-cmd && firewall-cmd --reload --quiet || :

%preun controller
%preun_service linstor-controller

### satellite
%package satellite
Summary: Linstor satellite specific files
Group: System/Servers
Requires: linstor-common = %EVR
Requires: lvm2 thin-provisioning-tools
Requires: drbd-utils >= 9.7.0

%description satellite
Linstor satellite, communicates with linstor-controller
and creates drbd resource files.

%files satellite -f satellite/jar.deps
%dir %LS_PREFIX
%dir %LS_PREFIX/lib
%LS_PREFIX/lib/satellite-%version.jar
%dir %LS_PREFIX/bin
%LS_PREFIX/bin/Satellite
%_unitdir/linstor-satellite.service
%FIREWALLD_SERVICES/linstor-satellite.xml
%FIREWALLD_SERVICES/drbd.xml
%config(noreplace) %_sysconfdir/drbd.d/linstor-resources.res

%post satellite
%post_service linstor-satellite
#test -f %%_bindir/firewall-cmd && firewall-cmd --reload --quiet || :

%preun satellite
%preun_service linstor-satellite

%changelog
* Wed Sep 25 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.29.1-alt1
- 1.29.1

* Wed Jul 31 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.29.0-alt1
- 1.29.0

* Thu Jul 11 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.28.0-alt1
- 1.28.0

* Thu Apr 25 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.27.1-alt1
- 1.27.1

* Thu Apr 04 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.27.0-alt1
- 1.27.0

* Mon Mar 04 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.26.2-alt1
- 1.26.2

* Thu Feb 22 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.26.1-alt1
- 1.26.1

* Mon Jan 29 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.26.0-alt1
- 1.26.0

* Fri Dec 01 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.25.1-alt1
- 1.25.1

* Wed Oct 25 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.25.0-alt1
- 1.25.0

* Thu Aug 31 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.24.2-alt1
- 1.24.2

* Mon Aug 14 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.24.1-alt1
- 1.24.1
- use gradle 8.2.1

* Tue May 23 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.23.0-alt1
- 1.23.0
- add JAVA_HOME for Java 11

* Wed May 10 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.22.1-alt1
- 1.22.1
- add Java 11 dependency, doesn't work with Java 17

* Wed Apr 19 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.22.0-alt1
- 1.22.0

* Tue Mar 14 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.21.0-alt1
- 1.21.0

* Thu Jan 26 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.20.3-alt1
- 1.20.3

* Thu Dec 15 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.20.2-alt1
- 1.20.2

* Tue Dec 13 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.20.1-alt1
- 1.20.1

* Mon Oct 31 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.20.0-alt1
- 1.20.0

* Thu Nov 11 2021 Alexey Shabalin <shaba@altlinux.org> 1.16.0-alt1
- 1.16.0

* Sun Nov 15 2020 Alexey Shabalin <shaba@altlinux.org> 1.10.0-alt2
- build as noarch again

* Sun Nov 15 2020 Alexey Shabalin <shaba@altlinux.org> 1.10.0-alt1
- 1.10.0

* Tue Jun 23 2020 Alexey Shabalin <shaba@altlinux.org> 1.7.1-alt1
- 1.7.1

* Thu Mar 05 2020 Alexey Shabalin <shaba@altlinux.org> 1.4.3-alt1
- Initial build
