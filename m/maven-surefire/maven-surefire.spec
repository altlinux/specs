Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without  junit5

Name:           maven-surefire
Epoch:          0
Version:        3.0.0_M4
Release:        alt1_1jpp11
Summary:        Test framework project
License:        ASL 2.0 and CPL

%global upstream_version %(echo '%{version}' | tr '_' '-')

URL:            http://maven.apache.org/surefire/

# ./generate-tarball.sh 3.0.0-M4
Source0:        %{name}-%{upstream_version}.tar.gz
# Remove bundled binaries which cannot be easily verified for licensing
Source1:        generate-tarball.sh
Source2:        http://junit.sourceforge.net/cpl-v10.html

Patch1:         0001-Port-to-TestNG-6.11.patch
Patch2:         0002-Port-to-current-maven-shared-utils.patch
Patch3:         0003-Fix-broken-Javadocs.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-decoration-model)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-toolchain)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-java)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.testng:testng)
BuildRequires:  mvn(org.testng:testng::jdk15:)

%if %{with junit5}
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher)
%endif

# PpidChecker relies on /usr/bin/ps to check process uptime
Requires:       libprocps procps
Source44: import.info

%description
Surefire is a test framework project.

%package plugin
Group: Development/Java
Summary:        Surefire plugin for maven
Requires:       %{name}-provider-junit = %{epoch}:%{version}-%{release}
Requires:       %{name}-provider-testng = %{epoch}:%{version}-%{release}
%if %{with junit5}
Requires:       %{name}-provider-junit5 = %{epoch}:%{version}-%{release}
%endif

%description plugin
Maven surefire plugin for running tests via the surefire framework.

%package report-plugin
Group: Development/Java
Summary:        Surefire reports plugin for maven

%description report-plugin
Plugin for generating reports from surefire test runs.

%package provider-junit
Group: Development/Java
Summary:        JUnit provider for Maven Surefire

%description provider-junit
JUnit provider for Maven Surefire.

%if %{with junit5}
%package provider-junit5
Group: Development/Java
Summary:        JUnit 5 provider for Maven Surefire

%description provider-junit5
JUnit 5 provider for Maven Surefire.
%endif

%package provider-testng
Group: Development/Java
Summary:        TestNG provider for Maven Surefire

%description provider-testng
TestNG provider for Maven Surefire.

%package report-parser
Group: Development/Java
Summary:        Parses report output files from surefire

%description report-parser
Plugin for parsing report output files from surefire.

%package -n maven-failsafe-plugin
Group: Development/Java
Summary:        Maven plugin for running integration tests

%description -n maven-failsafe-plugin
The Failsafe Plugin is designed to run integration tests while the
Surefire Plugins is designed to run unit. The name (failsafe) was
chosen both because it is a synonym of surefire and because it implies
that when it fails, it does so in a safe way.

If you use the Surefire Plugin for running tests, then when you have a
test failure, the build will stop at the integration-test phase and
your integration test environment will not have been torn down
correctly.

The Failsafe Plugin is used during the integration-test and verify
phases of the build lifecycle to execute the integration tests of an
application. The Failsafe Plugin will not fail the build during the
integration-test phase thus enabling the post-integration-test phase
to execute.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n surefire-%{upstream_version}
cp -p %{SOURCE2} .

%patch1 -p1
%patch2 -p1
%patch3 -p1

# Disable strict doclint
sed -i /-Xdoclint:all/d pom.xml

%pom_disable_module surefire-shadefire

%if %{without junit5}
%pom_disable_module surefire-junit-platform surefire-providers
%endif

%pom_remove_dep -r org.apache.maven.surefire:surefire-shadefire

# Help plugin is needed only to evaluate effective Maven settings.
# For building RPM package default settings will suffice.
%pom_remove_plugin :maven-help-plugin surefire-its

# QA plugin useful only for upstream
%pom_remove_plugin -r :jacoco-maven-plugin

# Not in Fedora
%pom_remove_plugin -r :animal-sniffer-maven-plugin

# Complains
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

# We don't need site-source
%pom_remove_plugin :maven-assembly-plugin maven-surefire-plugin
%pom_remove_dep -r ::::site-source

# This package needs maven compat for ArtifactResolver class
%pom_add_dep org.apache.maven:maven-compat maven-surefire-common

%mvn_package ":*{surefire-plugin,report-plugin}*" @1
%mvn_package ":*junit-platform*" junit5
%mvn_package ":*{junit,testng,failsafe-plugin,report-parser}*"  @1
%mvn_package ":*tests*" __noinstall

%build
# tests are disabled because of unpackaged dependencies (fest-assert, etc.)
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE NOTICE cpl-v10.html

%files plugin -f .mfiles-surefire-plugin
%files report-plugin -f .mfiles-report-plugin
%files report-parser -f .mfiles-report-parser
%files provider-junit -f .mfiles-junit
%files provider-testng -f .mfiles-testng
%files -n maven-failsafe-plugin -f .mfiles-failsafe-plugin
%if %{with junit5}
%files provider-junit5 -f .mfiles-junit5
%endif

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE cpl-v10.html

%changelog
* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:3.0.0_M4-alt1_1jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:2.22.0-alt1_9jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.22.0-alt1_6jpp8
- fc update

* Wed Jun 19 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.22.0-alt1_4jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.21.0-alt1_1jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.20.1-alt1_3jpp8
- new version

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.19.1-alt1_8jpp8
- new release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.19.1-alt1_2jpp8
- new version

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.18.1-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.18.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.16-alt1_1jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.14-alt1_2jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.12.4-alt2_2jpp7
- rebuild with maven-local

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.12.4-alt1_2jpp7
- update

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.12-alt2_5jpp7
- fixed build

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.12-alt1_5jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

