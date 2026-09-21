%define dbeaver_common_commit d11df22413e9c48278ee22afbfa9f00f0d54e776
%define equinox_commit 12022c26e62ce76e376f6f9b22001b9aa0f969a7
%define datadam_api_commit 3a5981e58e130909df93aa9b0c8b3e406d46812b

%ifarch x86_64
%define jna_arch linux-x86-64
%endif
%ifarch aarch64
%define jna_arch linux-aarch64
%endif

Name: dbeaver
Version: 26.2.1
Release: alt1

Summary: Universal Database Manager
Summary(ru_RU.UTF-8): Универсальный менеджер баз данных
License: Apache-2.0
Group: Databases

URL: https://%name.io/
Vcs: https://github.com/%name/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

ExcludeArch: %ix86

# https://github.com/%name/%name/archive/%version/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: %name.desktop
Source2: maven-local-repository.tar
# https://github.com/dbeaver/dbeaver-common/archive/%dbeaver_common_commit/dbeaver-common-%dbeaver_common_commit.tar.gz
Source3: dbeaver-common-%dbeaver_common_commit.tar
# https://github.com/eclipse-equinox/equinox/archive/%equinox_commit/equinox-%equinox_commit.tar.gz
Source4: equinox-%equinox_commit.tar
# https://github.com/dbeaver/datadam-api/archive/%datadam_api_commit/datadam-api-%datadam_api_commit.tar.gz
Source5: datadam-api-%datadam_api_commit.tar

Patch0: %name-alt-autoupdate.patch

BuildRequires: /proc rpm-build-java maven
BuildRequires: java-25-openjdk-devel
BuildRequires: gcc glibc-devel pkg-config
BuildRequires: libgtk+3-devel

Requires: java-25-openjdk-headless

%description
DBeaver is free and open source universal database tool for developers and database administrators.

*  Usability is the main goal of this project, program UI is carefully designed and implemented.
*  It is free and open-source (ASL).
*  It is multiplatform.
*  It is based on opensource framework and allows writing of various extensions (plugins).
*  It supports any database having a JDBC driver.
*  It may handle any external datasource which may or may not have a JDBC driver.
*  There is a set of plugins for different databases and different database management utilities (e.g. ERD, data transfer, compare, data export/import, mock data generation, etc).
*  It has a great number of features.

%prep
%setup -b 2 -b 3 -b 4 -b 5
%patch0 -p1

%__mv -Tf ../dbeaver-common-%dbeaver_common_commit ../dbeaver-common
%__mv -Tf ../datadam-api-%datadam_api_commit ../datadam-api

%__rm -rf ~/.m2
%__mv -Tf ../.m2 ~/.m2

%build
export JAVA_HOME="$(dirname "$(dirname "$(readlink -f "$(command -v javac)")")")"
cd %_builddir/equinox-%equinox_commit/features/org.eclipse.equinox.executable.feature/library/gtk
BINARIES_DIR=%_builddir/eqbin sh build.sh -java "$JAVA_HOME" -os linux -ws gtk -arch %_arch

_eqdir=%_builddir/equinox-%equinox_commit/features/org.eclipse.equinox.executable.feature/library/gtk
_eqexe=$_eqdir/eclipse
_eqlib=$(echo $_eqdir/eclipse_*.so)
_featjar=$(echo ~/.m2/repository/p2/org/eclipse/update/feature/org.eclipse.equinox.executable/*/*.jar)
_fragjar=$(echo ~/.m2/repository/p2/osgi/bundle/org.eclipse.equinox.launcher.gtk.linux.%_arch/*/*.jar)
_rootjar=$(echo ~/.m2/repository/p2/binary/org.eclipse.equinox.executable_root.gtk.linux.%_arch/*/*.jar)
_tmp=$(mktemp -d)
%__mkdir_p $_tmp/feat/bin/gtk/linux/%_arch
%__cp -f $_eqexe $_tmp/feat/bin/gtk/linux/%_arch/launcher
%__cp -f $_eqexe $_tmp/launcher
%__cp -f $_eqlib $_tmp/
( cd $_tmp/feat && jar uf $_featjar bin/gtk/linux/%_arch/launcher )
( cd $_tmp && jar uf $_fragjar $(basename $_eqlib) )
( cd $_tmp && jar uf $_rootjar launcher )
%__rm -rf $_tmp

cd %_builddir/%name-%version
mvn -o -B -T1C clean install -Pproduct-dbeaver-ce -f product/aggregate

%install
# Create  directories
%__mkdir_p %buildroot%_bindir
%__mkdir_p %buildroot%_datadir/%name
%__mkdir_p %buildroot%_libexecdir
%__mkdir_p %buildroot%_pixmapsdir

# Install icons into /usr/share/icons/hicolor
for _size in 16 32 48 64 128 256 512
do
	%__install -Dp -m 0644 product/community/icons-sources/icon_${_size}x${_size}.png %buildroot%_iconsdir/hicolor/${_size}x${_size}/apps/%name.png
done

# Move into the target directory
%__cp -r product/community/target/products/org.jkiss.dbeaver.core.product/linux/gtk/%_arch/%name %buildroot%_libexecdir

# Keep only the native JNA library for the target architecture
find %buildroot%_libexecdir/%name/plugins/com.sun.jna_*/com/sun/jna \
	-name libjnidispatch.so ! -path '*/%jna_arch/*' -delete

# Move shared data to /usr/share/dbeaver
for _file in  .eclipseproduct artifacts.xml configuration dbeaver.ini licenses readme.txt
do
	%__mv %buildroot%_libexecdir/%name/${_file} %buildroot%_datadir/%name
	%__ln_s ../../..%_datadir/%name/${_file} %buildroot%_libexecdir/%name/
done

%ifarch x86_64
%__rm %buildroot%_libexecdir/%name/%name.png
%endif

# Install icons into /usr/share/pixmaps
%__mv %buildroot%_libexecdir/%name/icon.xpm %buildroot%_pixmapsdir/%name.xpm

# Install executable script into /usr/bin
%__ln_s ../..%_libexecdir/%name/%name %buildroot%_bindir/%name

# Install application launcher into /usr/share/applications
%__install -Dp -m 0755 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%config %_datadir/%name/%name.ini
%_iconsdir/hicolor/*/apps/%name.png
%_libexecdir/%name
%_pixmapsdir/%name.xpm

%changelog
* Mon Sep 21 2026 Nazarov Denis <nenderus@altlinux.org> 26.2.1-alt1
- Version 26.2.1
- Build Eclipse launcher from source, exclude precompiled binaries (Closes: #41062)

* Sat Jul 16 2022 Igor Vlasenko <viy@altlinux.org> 21.2.0-alt2
- build w/o maven-javadoc-plugin

* Sun Sep 05 2021 Nazarov Denis <nenderus@altlinux.org> 21.2.0-alt1
- Version 21.2.0

* Mon Aug 16 2021 Nazarov Denis <nenderus@altlinux.org> 21.1.5-alt1
- Version 21.1.5

* Wed Aug 04 2021 Nazarov Denis <nenderus@altlinux.org> 21.1.4-alt1
- Version 21.1.4

* Mon Jul 19 2021 Nazarov Denis <nenderus@altlinux.org> 21.1.3-alt1
- Version 21.1.3

* Wed Jul 14 2021 Nazarov Denis <nenderus@altlinux.org> 21.1.2-alt1
- Version 21.1.2

* Mon Jun 21 2021 Nazarov Denis <nenderus@altlinux.org> 21.1.1-alt1
- Version 21.1.1

* Mon May 31 2021 Nazarov Denis <nenderus@altlinux.org> 21.1.0-alt1
- Version 21.1.0

* Thu May 20 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.5-alt1
- Version 21.0.5

* Mon May 03 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.4-alt1
- Version 21.0.4

* Sun Apr 18 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.3-alt1
- Version 21.0.3

* Mon Apr 05 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.2-alt1
- Version 21.0.2

* Thu Mar 25 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.1-alt3
- Reduce maven local repository

* Mon Mar 22 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.1-alt2
- Improved build
- Disable auto update check by default

* Mon Mar 22 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.1-alt1
- Version 21.0.1

* Thu Mar 04 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.0-alt3
- Build on ppc64le

* Mon Mar 01 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.0-alt2
- Build on AArch64

* Sun Feb 28 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.0-alt1
- Version 21.0.0

* Fri Feb 26 2021 Nazarov Denis <nenderus@altlinux.org> 7.3.5-alt3
- Add requires on java-openjdk-headless

* Thu Feb 25 2021 Nazarov Denis <nenderus@altlinux.org> 7.3.5-alt2
- Build with maven

* Fri Feb 19 2021 Nazarov Denis <nenderus@altlinux.org> 7.3.5-alt1
- Initial build for ALT Linux
