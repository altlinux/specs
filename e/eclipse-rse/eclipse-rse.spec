# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: gcc-c++ perl(Shell.pm) unzip
# END SourceDeps(oneline)
BuildRequires: perl(Authen/PAM.pm)
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%if 0%{?rhel} >= 6
%global debug_package %{nil}
%endif
%global install_loc         %{_datadir}/eclipse/dropins
%global rseserver_install   %{_datadir}/eclipse-rse-server
%global rseserver_java      %{_datadir}/java/eclipse-rse-server
%global rseserver_config    %{_sysconfdir}/sysconfig/rseserver
%global rse_snapshot        org.eclipse.tm

Name: eclipse-rse
Summary: Eclipse Remote System Explorer
Version: 3.5
Release: alt2_0.4.rc3jpp7
License: EPL
URL: http://www.eclipse.org/dsdp/tm/

Source0: http://git.eclipse.org/c/tm/org.eclipse.tm.git/snapshot/S3_5RC3.tar.bz2
Source4: notice.html
Source5: epl-v10.html

# Use Authen::pam to authenticate clients
Patch1: eclipse-rse-server-auth-pl.patch
# Fix classpath in daemon and server scripts to point
# to install locations
Patch2: eclipse-rse-server-scripts.patch
# Patch to remove eclipse-parent pom reference and multiple environments
Patch3: eclipse-rse-top-pom.patch
# Patch to remove dependency on org.apache.commons.net.source
Patch4: eclipse-rse-commons-net-source.patch
# Patch to allow junit4 to be used for building tests
Patch5: eclipse-rse-junit.patch
# Patch to remove tests from tm repo
Patch6: eclipse-rse-tm-repo.patch



# All arches line up except i386 -> x86
%ifarch %{ix86}
%define eclipse_arch    x86
%else
%ifarch %{arm}
%define eclipse_arch    arm
%else
%define eclipse_arch   %{_arch}
%endif
%endif

%if 0%{?rhel} >= 6
ExclusiveArch: i686 x86_64
%else
BuildArch: noarch
%endif

BuildRequires: tycho
BuildRequires: tycho-extras
BuildRequires: maven-local maven >= 3.0.3
BuildRequires: junit

BuildRequires: eclipse-pde >= 1:3.8.0-0.21
BuildRequires: eclipse-emf >= 0:2.4.1
BuildRequires: apache-commons-net >= 0:1.4.1-5.4
Requires: eclipse-platform >= 1:3.8.0-0.21
Requires: eclipse-emf >= 0:2.4.1
Requires: apache-commons-net >= 0:2.0

Group: Development/Java
Source44: import.info

%description
Remote System Explorer (RSE) is a framework and toolkit in Eclipse Workbench
that allows you to connect and work with a variety of remote systems.

%package server
Summary: Eclipse Remote System Explorer Server
Group: Development/Java
Requires: perl
Requires: perl-Authen-PAM

%description server
The Remote System Explorer (RSE) framework server that can be used so clients can connect to this machine via RSE.

%prep
%setup -q -n S3_5RC3

%patch3 -b .orig
%patch4
%patch5
%patch6 -b .orig

sed -i -e 's/<arch>x86<\/arch>/<arch>%{eclipse_arch}<\/arch>/g' pom.xml

pushd rse/plugins/org.eclipse.rse.services.dstore
%patch1
%patch2
popd

%build

mvn-rpmbuild -DskipTychoVersionCheck -Dmaven.test.skip=true clean install

cp %{SOURCE4} .
cp %{SOURCE5} .

%install

install -d -m 755 %{buildroot}%{_datadir}/eclipse
install -d -m 755 %{buildroot}%{install_loc}/rse/eclipse
install -d -m 755 %{buildroot}%{rseserver_install}
install -d -m 755 %{buildroot}%{rseserver_java}
install -d -m 755 %{buildroot}%{rseserver_config}

cp -R releng/org.eclipse.tm.repo/target/repository/features \
   %{buildroot}%{install_loc}/rse/eclipse \

cp -R releng/org.eclipse.tm.repo/target/repository/plugins \
   %{buildroot}%{install_loc}/rse/eclipse \

pushd %{buildroot}%{install_loc}/rse/eclipse/plugins
rm org.apache.commons.net_*.jar
ln -s %{_javadir}/commons-net.jar org.apache.commons.net.jar
popd

pushd %{buildroot}%{install_loc}/rse/eclipse/plugins
unzip -q -o -d %{buildroot}%{rseserver_java} org.eclipse.rse.services.dstore_*.jar dstore_miners.jar
unzip -q -o -d %{buildroot}%{rseserver_java} org.eclipse.dstore.core_*.jar dstore_core.jar
unzip -q -o -d %{buildroot}%{rseserver_java} org.eclipse.dstore.extra_*.jar dstore_extra_server.jar
unzip -q -o -d %{buildroot}%{rseserver_java} org.eclipse.rse.services_*.jar clientserver.jar
# Remove server-specific jar files from plug-ins
jarname=`ls org.eclipse.rse.services.dstore_*.jar`
zip -d $jarname dstore_miners.jar
jarname=`ls org.eclipse.dstore.core_*.jar`
zip -d $jarname dstore_core.jar
jarname=`ls org.eclipse.dstore.extra_*.jar`
zip -d $jarname dstore_extra_server.jar
jarname=`ls org.eclipse.rse.services_*.jar`
zip -d $jarname clientserver.jar
popd

pushd rse/plugins/org.eclipse.rse.services.dstore
pushd serverruntime/scripts/linux
cp *.pl %{buildroot}%{rseserver_install}
popd
pushd serverruntime/data
cp *.properties %{buildroot}%{rseserver_config}
cp *.dat %{buildroot}%{rseserver_install}
popd

%files
%{install_loc}/rse
%doc rse/features/org.eclipse.rse.sdk-feature/epl-v10.html
%doc rse/features/org.eclipse.rse.sdk-feature/license.html

%files server
%{rseserver_install}
%{rseserver_java}
%dir %{rseserver_config}
%config(noreplace) %{rseserver_config}/ssl.properties
%config(noreplace) %{rseserver_config}/rsecomm.properties
%doc notice.html
%doc epl-v10.html

%changelog
* Fri Aug 08 2014 Igor Vlasenko <viy@altlinux.ru> 3.5-alt2_0.4.rc3jpp7
- rebuild with maven-local

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1_0.4.rc3jpp7
- new version

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 3.4-alt2_3jpp7
- commons-net 3.2 support

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 3.4-alt1_3jpp7
- new version

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1_3jpp6
- update to new release by jppimport

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1_1jpp6
- new version

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_3jpp6
- new version

* Thu Feb 04 2010 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_2jpp5
- first build; note: use embedded jakarta-commons-net 2.0

