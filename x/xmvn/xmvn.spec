Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

%if %{with bootstrap}
%global mbi 1
%endif

Name:           xmvn
Version:        4.0.0
Release:        alt1_0jpp11
Summary:        Local Extensions for Apache Maven
License:        ASL 2.0
URL:            https://fedora-java.github.io/xmvn/
BuildArch:      noarch

Source0:        https://github.com/fedora-java/xmvn/releases/download/%{version}/xmvn-%{version}.tar.xz

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-util)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-model-builder)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(org.xmlunit:xmlunit-assertj3)
# Maven home is used as template for XMvn home
BuildRequires:  maven
# Test dependency (for testing compatibility with Java 8)
BuildRequires:  java-1.8.0-openjdk-devel
%endif

Requires:       %{name}-minimal = %{version}-%{release}
Requires:       maven >= 3.6.1
Source44: import.info

%description
This package provides extensions for Apache Maven that can be used to
manage system artifact repository and use it to resolve Maven
artifacts in offline mode, as well as Maven plugins to help with
creating RPM packages containing Maven artifacts.

%package        minimal
Group: Development/Java
Summary:        Dependency-reduced version of XMvn
Requires:       %{name}-core = %{version}-%{release}
Requires:       apache-commons-cli
Requires:       apache-commons-lang3
Requires:       atinject
Requires:       google-guice
Requires:       guava
Requires:       maven-resolver-api maven-resolver-connector-basic maven-resolver-impl maven-resolver-spi maven-resolver-transport-wagon maven-resolver-util
Requires:       maven-wagon-file maven-wagon-http maven-wagon-http-shared maven-wagon-provider-api
Requires:       plexus-cipher
Requires:       plexus-classworlds
Requires:       plexus-containers-component-annotations
Requires:       plexus-interpolation
Requires:       plexus-sec-dispatcher
Requires:       plexus-utils
Requires:       sisu-inject sisu-plexus
Requires:       slf4j

Requires:       maven-lib >= 3.4.0
#Requires:       maven-jdk-binding
#Requires:       maven-openjdk11

Obsoletes:      xmvn-connector-aether < 4.0.0

%description    minimal
This package provides minimal version of XMvn, incapable of using
remote repositories.

%package        core
Group: Development/Java
Summary:        XMvn library
Obsoletes:      xmvn-parent-pom < 4.0.0
Obsoletes:      xmvn-api < 4.0.0

%description    core
This package provides XMvn API and XMvn Core modules, which implement
the essential functionality of XMvn such as resolution of artifacts
from system repository.

%package        mojo
Group: Development/Java
Summary:        XMvn MOJO

%description    mojo
This package provides XMvn MOJO, which is a Maven plugin that consists
of several MOJOs.  Some goals of these MOJOs are intended to be
attached to default Maven lifecycle when building packages, others can
be called directly from Maven command line.

%package        tools
Group: Development/Java
Summary:        XMvn tools
# Explicit javapackages-tools requires since scripts use
# /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Obsoletes:      xmvn-tools-pom < 4.0.0
Obsoletes:      xmvn-bisect < 4.0.0
Obsoletes:      xmvn-install < 4.0.0
Obsoletes:      xmvn-resolve < 4.0.0
Obsoletes:      xmvn-subst < 4.0.0

%description    tools
This package provides various XMvn tools:
* XMvn Install, which is a command-line interface to XMvn installer.
  The installer reads reactor metadata and performs artifact
  installation according to specified configuration.
* XMvn Resolver, which is a very simple commald-line tool to resolve
  Maven artifacts from system repositories.  Basically it's just an
  interface to artifact resolution mechanism implemented by XMvn Core.
  The primary intended use case of XMvn Resolver is debugging local
  artifact repositories.
* XMvn Subst, which is a tool that can substitute Maven artifact files
  with symbolic links to corresponding files in artifact repository.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package provides %{summary}.

%prep
%setup -q

%mvn_package ::tar.gz: __noinstall
%mvn_package ":{xmvn,xmvn-connector}" xmvn
%mvn_package ":xmvn-{api,core,parent}" core
%mvn_package ":xmvn-mojo" mojo
%mvn_package ":xmvn-{install,resolve,subst,tools}" tools

# Don't put Class-Path attributes in manifests
%pom_remove_plugin :maven-jar-plugin xmvn-tools

# Copy Maven home packaged as RPM instead of unpacking Maven binary
# tarball with maven-dependency-plugin
%pom_remove_plugin :maven-dependency-plugin
maven_home=$(realpath $(dirname $(realpath $(%{?jpb_env} which mvn)))/..)
mver=$(sed -n '/<mavenVersion>/{s/.*>\(.*\)<.*/\1/;p}' \
           xmvn-parent/pom.xml)
mkdir -p target/dependency/
cp -a "${maven_home}" target/dependency/apache-maven-$mver

%build
%mvn_build -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -P\\!quality

version=4.0.0
tar --delay-directory-restore -xvf target/xmvn-*-bin.tar.gz
chmod -R +rwX %{name}-${version}*
# These are installed as doc
rm -f %{name}-${version}*/{AUTHORS-XMVN,README-XMVN.md,LICENSE,NOTICE,NOTICE-XMVN}
# Not needed - we use JPackage launcher scripts
rm -Rf %{name}-${version}*/lib/{installer,resolver,subst}/
# Irrelevant Maven launcher scripts
rm -f %{name}-${version}*/bin/*


%install
%mvn_install

version=4.0.0
maven_home=$(realpath $(dirname $(realpath $(%{?jpb_env} which mvn)))/..)

install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -r%{?mbi:L} %{name}-${version}*/* %{buildroot}%{_datadir}/%{name}/

for cmd in mvn mvnDebug; do
    cat <<EOF >%{buildroot}%{_datadir}/%{name}/bin/$cmd
#!/bin/sh -e
export _FEDORA_MAVEN_HOME="%{_datadir}/%{name}"
exec %{_datadir}/maven/bin/$cmd "\${@}"
EOF
    chmod 755 %{buildroot}%{_datadir}/%{name}/bin/$cmd
done

# helper scripts
%jpackage_script org.fedoraproject.xmvn.tools.install.cli.InstallerCli "" "" xmvn/xmvn-install:xmvn/xmvn-api:xmvn/xmvn-core:beust-jcommander:slf4j/api:slf4j/simple:objectweb-asm/asm:commons-compress xmvn-install
%jpackage_script org.fedoraproject.xmvn.tools.resolve.ResolverCli "" "" xmvn/xmvn-resolve:xmvn/xmvn-api:xmvn/xmvn-core:beust-jcommander xmvn-resolve
%jpackage_script org.fedoraproject.xmvn.tools.subst.SubstCli "" "" xmvn/xmvn-subst:xmvn/xmvn-api:xmvn/xmvn-core:beust-jcommander xmvn-subst

# copy over maven boot and lib directories
cp -r%{?mbi:L} ${maven_home}/boot/* %{buildroot}%{_datadir}/%{name}/boot/
cp -r%{?mbi:L} ${maven_home}/lib/* %{buildroot}%{_datadir}/%{name}/lib/

# possibly recreate symlinks that can be automated with xmvn-subst
%if !0%{?mbi}
%{name}-subst -s -R %{buildroot} %{buildroot}%{_datadir}/%{name}/
%endif

# /usr/bin/xmvn
ln -s %{_datadir}/%{name}/bin/mvn %{buildroot}%{_bindir}/%{name}

# mvn-local symlink
ln -s %{name} %{buildroot}%{_bindir}/mvn-local

# make sure our conf is identical to maven so yum won't freak out
install -d -m 755 %{buildroot}%{_datadir}/%{name}/conf/
cp -P ${maven_home}/conf/settings.xml %{buildroot}%{_datadir}/%{name}/conf/
cp -P ${maven_home}/bin/m2.conf %{buildroot}%{_datadir}/%{name}/bin/

# Make sure javapackages config is not bundled
rm -rf %{buildroot}%{_datadir}/%{name}/{configuration.xml,config.d/,conf/toolchains.xml,maven-metadata/}
for rpm404_ghost in %{_datadir}/%{name}/conf/logging.rpmmoved
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done

%if 0
pushd %buildroot%{_datadir}/%{name}/lib
[ -e jansi-linux.jar ] || exit 1
rm jansi-linux.jar
ln -s /usr/lib/java/jansi-native/jansi-linux.jar .
popd
%endif

%pre minimal
path = "/usr/share/xmvn/conf/logging"
if [ -d "$path" ]; then
  if [ -e "$path".rpmmoved ]; then
    mv "$path" "$path".rpmmoved.$$
  else
    mv "$path" "$path".rpmmoved
  fi
fi




# Workaround for rpm bug 447156 - rpm fails to change directory to symlink
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/
%files
%{_bindir}/mvn-local

%files minimal -f .mfiles-xmvn
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/*.jar
%{_datadir}/%{name}/lib/ext
%{_datadir}/%{name}/lib/jansi-native
%{_datadir}/%{name}/bin/m2.conf
%{_datadir}/%{name}/bin/mvn
%{_datadir}/%{name}/bin/mvnDebug
%{_datadir}/%{name}/boot
%{_datadir}/%{name}/conf
%ghost %{_datadir}/%{name}/conf/logging.rpmmoved

%files core -f .mfiles-core
%doc --no-dereference LICENSE NOTICE
%doc AUTHORS README.md

%files mojo -f .mfiles-mojo

%files tools -f .mfiles-tools
%{_bindir}/%{name}-install
%{_bindir}/%{name}-resolve
%{_bindir}/%{name}-subst

%files javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Wed Jun 29 2022 Igor Vlasenko <viy@altlinux.org> 4.0.0-alt1_0jpp11
- new version
- for use with older maven build

* Wed Jun 08 2022 Igor Vlasenko <viy@altlinux.org> 3.1.0-alt3_7jpp11
- nobootstrap

* Tue Jun 07 2022 Igor Vlasenko <viy@altlinux.org> 3.1.0-alt2_7jpp11
- bootstrap for guava update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 3.1.0-alt1_7jpp11
- update

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 3.1.0-alt1_2jpp11
- normal build

* Thu May 27 2021 Igor Vlasenko <viy@altlinux.org> 3.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu May 13 2021 Igor Vlasenko <viy@altlinux.org> 3.0.0-alt2_26jpp8
- build w/o gradle

* Sun May 09 2021 Igor Vlasenko <viy@altlinux.org> 3.0.0-alt1_26jpp8
- update

* Mon Jul 15 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_23jpp8
- build with new gradle

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_21jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_18jpp8
- java fc28+ update

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_14jpp8
- support for maven-javadoc-plugin-3.0.0

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_8jpp8
- support for gradle 4.3
- no support for maven-javadoc-plugin >= 3.0.0 yet

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_7jpp8
- rebuild with guava20

* Tue Nov 21 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_6jpp8
- new version (unbootstrap build)

* Tue Nov 21 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Oct 30 2017 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_21jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_11jpp8
- new fc release

* Fri Dec 09 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_6jpp8
- unbootstrup build

* Fri Dec 09 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_5jpp8
- unbootsrap build

* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt4_4jpp7
- rebuild to update symlinks

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt3_4jpp7
- fixed bin
- nobootstrap build

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_5jpp7
- nobootstrap build

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

