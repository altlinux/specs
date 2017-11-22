Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# XMvn uses OSGi environment provided by Tycho, it shouldn't require
# any additional bundles.


# Integration tests are disabled by default, but you can run them by
# adding "--with its" to rpmbuild or mock invocation.
%bcond_with its

%bcond_without gradle

Name:           xmvn
Version:        3.0.0
Release:        alt1_6jpp8
Summary:        Local Extensions for Apache Maven
License:        ASL 2.0
URL:            https://fedora-java.github.io/xmvn/
BuildArch:      noarch

Source0:        https://github.com/fedora-java/xmvn/releases/download/%{version}/xmvn-%{version}.tar.xz

Patch0:         0001-Fix-installer-plugin-loading.patch

BuildRequires:  maven >= 3.5.0
BuildRequires:  maven-local
BuildRequires:  beust-jcommander
BuildRequires:  cglib
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-plugin-build-helper
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  objectweb-asm
BuildRequires:  modello
BuildRequires:  xmlunit
BuildRequires:  apache-ivy
BuildRequires:  junit
BuildRequires:  easymock
BuildRequires:  maven-invoker
BuildRequires:  plexus-containers-container-default
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-containers-component-metadata
%if %{with gradle}
BuildRequires:  gradle >= 2.5
%endif

Requires:       %{name}-minimal = %{version}-%{release}
Requires:       maven >= 3.4.0
Source44: import.info
%filter_from_requires /^osgi\\($/d

%description
This package provides extensions for Apache Maven that can be used to
manage system artifact repository and use it to resolve Maven
artifacts in offline mode, as well as Maven plugins to help with
creating RPM packages containing Maven artifacts.

%package        minimal
Group: Development/Java
Summary:        Dependency-reduced version of XMvn
Requires:       maven-lib >= 3.4.0
Requires:       %{name}-api = %{version}-%{release}
Requires:       %{name}-connector-aether = %{version}-%{release}
Requires:       %{name}-core = %{version}-%{release}
Requires:       apache-commons-cli
Requires:       apache-commons-lang3
Requires:       atinject
Requires:       google-guice
Requires:       guava
Requires:       maven-lib
Requires:       maven-resolver-api
Requires:       maven-resolver-impl
Requires:       maven-resolver-spi
Requires:       maven-resolver-util
Requires:       maven-wagon-provider-api
Requires:       plexus-cipher
Requires:       plexus-classworlds
Requires:       plexus-containers-component-annotations
Requires:       plexus-interpolation
Requires:       plexus-sec-dispatcher
Requires:       plexus-utils
Requires:       sisu-inject
Requires:       sisu-plexus
Requires:       slf4j

%description    minimal
This package provides minimal version of XMvn, incapable of using
remote repositories.

%package        parent-pom
Group: Development/Java
Summary:        XMvn Parent POM

%description    parent-pom
This package provides XMvn parent POM.

%package        api
Group: Development/Java
Summary:        XMvn API
Obsoletes:      %{name}-launcher < 3.0.0

%description    api
This package provides XMvn API module which contains public interface
for functionality implemented by XMvn Core.

%package        core
Group: Development/Java
Summary:        XMvn Core

%description    core
This package provides XMvn Core module, which implements the essential
functionality of XMvn such as resolution of artifacts from system
repository.

%package        connector-aether
Group: Development/Java
Summary:        XMvn Connector for Maven Resolver

%description    connector-aether
This package provides XMvn Connector for Maven Resolver, which
provides integration of Maven Resolver with XMvn.  It provides an
adapter which allows XMvn resolver to be used as Maven workspace
reader.

%if %{with gradle}
%package        connector-gradle
Group: Development/Java
Summary:        XMvn Connector for Gradle

%description    connector-gradle
This package provides XMvn Connector for Gradle, which provides
integration of Gradle with XMvn.  It provides an adapter which allows
XMvn resolver to be used as Gradle resolver.
%endif

%package        connector-ivy
Group: Development/Java
Summary:        XMvn Connector for Apache Ivy

%description    connector-ivy
This package provides XMvn Connector for Apache Ivy, which provides
integration of Apache Ivy with XMvn.  It provides an adapter which
allows XMvn resolver to be used as Ivy resolver.

%package        mojo
Group: Development/Java
Summary:        XMvn MOJO

%description    mojo
This package provides XMvn MOJO, which is a Maven plugin that consists
of several MOJOs.  Some goals of these MOJOs are intended to be
attached to default Maven lifecycle when building packages, others can
be called directly from Maven command line.

%package        tools-pom
Group: Development/Java
Summary:        XMvn Tools POM

%description    tools-pom
This package provides XMvn Tools parent POM.

%package        resolve
Group: Development/Java
Summary:        XMvn Resolver

%description    resolve
This package provides XMvn Resolver, which is a very simple
commald-line tool to resolve Maven artifacts from system repositories.
Basically it's just an interface to artifact resolution mechanism
implemented by XMvn Core.  The primary intended use case of XMvn
Resolver is debugging local artifact repositories.

%package        bisect
Group: Development/Java
Summary:        XMvn Bisect

%description    bisect
This package provides XMvn Bisect, which is a debugging tool that can
diagnose build failures by using bisection method.

%package        subst
Group: Development/Java
Summary:        XMvn Subst

%description    subst
This package provides XMvn Subst, which is a tool that can substitute
Maven artifact files with symbolic links to corresponding files in
artifact repository.

%package        install
Group: Development/Java
Summary:        XMvn Install

%description    install
This package provides XMvn Install, which is a command-line interface
to XMvn installer.  The installer reads reactor metadata and performs
artifact installation according to specified configuration.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package provides %{summary}.

%prep
%setup -q
%patch0 -p1

# Bisect IT has no chances of working in local, offline mode, without
# network access - it needs to access remote repositories.
find -name BisectIntegrationTest.java -delete

# Resolver IT won't work either - it tries to execute JAR file, which
# relies on Class-Path in manifest, which is forbidden in Fedora...
find -name ResolverIntegrationTest.java -delete

%pom_remove_plugin -r :maven-site-plugin

%mvn_package ":xmvn{,-it}" __noinstall

%if %{without gradle}
%pom_disable_module xmvn-connector-gradle
%endif

# Upstream code quality checks, not relevant when building RPMs
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :jacoco-maven-plugin
# FIXME pom macros don't seem to support submodules in profile
%pom_remove_plugin :jacoco-maven-plugin xmvn-it

# remove dependency plugin maven-binaries execution
# we provide apache-maven by symlink
%pom_xpath_remove "pom:executions/pom:execution[pom:id[text()='maven-binaries']]"

# Don't put Class-Path attributes in manifests
%pom_remove_plugin :maven-jar-plugin xmvn-tools

# get mavenVersion that is expected
maven_home=$(readlink -f $(dirname $(readlink $(which mvn)))/..)
mver=$(sed -n '/<mavenVersion>/{s/.*>\(.*\)<.*/\1/;p}' \
           xmvn-parent/pom.xml)
mkdir -p target/dependency/
cp -aL ${maven_home} target/dependency/apache-maven-$mver

%build
%if %{with its}
%mvn_build -s -j -- -Prun-its
%else
%mvn_build -s -j
%endif

tar --delay-directory-restore -xvf target/*tar.bz2
chmod -R +rwX %{name}-%{version}*
# These are installed as doc
rm -f %{name}-%{version}*/{AUTHORS-XMVN,README-XMVN.md,LICENSE,NOTICE,NOTICE-XMVN}
# Not needed - we use JPackage launcher scripts
rm -Rf %{name}-%{version}*/lib/{installer,resolver,subst,bisect}/
# Irrelevant Maven launcher scripts
rm -f %{name}-%{version}*/bin/{mvn.cmd,mvnDebug.cmd,mvn-script}


%install
%mvn_install

maven_home=$(readlink -f $(dirname $(readlink $(which mvn)))/..)

install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -r %{name}-%{version}*/* %{buildroot}%{_datadir}/%{name}/

for cmd in mvn mvnDebug mvnyjp; do
    cat <<EOF >%{buildroot}%{_datadir}/%{name}/bin/$cmd
#!/bin/sh -e
export _FEDORA_MAVEN_HOME="%{_datadir}/%{name}"
exec ${maven_home}/bin/$cmd "\${@}"
EOF
    chmod 755 %{buildroot}%{_datadir}/%{name}/bin/$cmd
done

# helper scripts
%jpackage_script org.fedoraproject.xmvn.tools.bisect.BisectCli "" "-Dxmvn.home=%{_datadir}/%{name}" xmvn/xmvn-bisect:beust-jcommander:maven-invoker:plexus/utils xmvn-bisect
%jpackage_script org.fedoraproject.xmvn.tools.install.cli.InstallerCli "" "" xmvn/xmvn-install:xmvn/xmvn-api:xmvn/xmvn-core:beust-jcommander:slf4j/api:slf4j/simple:objectweb-asm/asm xmvn-install
%jpackage_script org.fedoraproject.xmvn.tools.resolve.ResolverCli "" "" xmvn/xmvn-resolve:xmvn/xmvn-api:xmvn/xmvn-core:beust-jcommander xmvn-resolve
%jpackage_script org.fedoraproject.xmvn.tools.subst.SubstCli "" "" xmvn/xmvn-subst:xmvn/xmvn-api:xmvn/xmvn-core:beust-jcommander xmvn-subst

# copy over maven lib directory
cp -r ${maven_home}/lib/* %{buildroot}%{_datadir}/%{name}/lib/

# possibly recreate symlinks that can be automated with xmvn-subst
%{name}-subst -s -R %{buildroot} %{buildroot}%{_datadir}/%{name}/

# /usr/bin/xmvn
ln -s %{_datadir}/%{name}/bin/mvn %{buildroot}%{_bindir}/%{name}

# mvn-local symlink
ln -s %{name} %{buildroot}%{_bindir}/mvn-local

# make sure our conf is identical to maven so yum won't freak out
install -d -m 755 %{buildroot}%{_datadir}/%{name}/conf/
cp -P ${maven_home}/conf/settings.xml %{buildroot}%{_datadir}/%{name}/conf/
cp -P ${maven_home}/bin/m2.conf %{buildroot}%{_datadir}/%{name}/bin/

%files
%{_bindir}/mvn-local

%files minimal
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
%{_datadir}/%{name}/bin/mvnyjp
%{_datadir}/%{name}/boot
%{_datadir}/%{name}/conf

%files parent-pom -f .mfiles-xmvn-parent
%doc LICENSE NOTICE

%files core -f .mfiles-xmvn-core

%files api -f .mfiles-xmvn-api
%doc LICENSE NOTICE
%doc AUTHORS README.md

%files connector-aether -f .mfiles-xmvn-connector-aether

%if %{with gradle}
%files connector-gradle -f .mfiles-xmvn-connector-gradle
%endif

%files connector-ivy -f .mfiles-xmvn-connector-ivy

%files mojo -f .mfiles-xmvn-mojo

%files tools-pom -f .mfiles-xmvn-tools

%files resolve -f .mfiles-xmvn-resolve
%{_bindir}/%{name}-resolve

%files bisect -f .mfiles-xmvn-bisect
%{_bindir}/%{name}-bisect

%files subst -f .mfiles-xmvn-subst
%{_bindir}/%{name}-subst

%files install -f .mfiles-xmvn-install
%{_bindir}/%{name}-install

%files javadoc
%doc LICENSE NOTICE

%changelog
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

