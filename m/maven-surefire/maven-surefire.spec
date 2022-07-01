Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           maven-surefire
Version:        3.0.0_M4
Release:        alt1_3jpp11
Summary:        Test framework project
License:        ASL 2.0 and CPL
URL:            https://maven.apache.org/surefire/
BuildArch:      noarch

%global upstream_version %(echo '%{version}' | tr '_' '-')
%global source_version %(echo '%{version}' | tr '_' '~')

# ./generate-tarball.sh
Source0:        %{name}-%{source_version}.tar.gz
# Remove bundled binaries which cannot be easily verified for licensing
Source1:        generate-tarball.sh
Source2:        https://junit.sourceforge.net/cpl-v10.html

Patch1:         0001-Port-to-TestNG-6.11.patch
Patch2:         0002-Disable-JUnit-4.8-test-grouping.patch
Patch3:         0003-Port-to-maven-shared-utils-3.3.3.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-java)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher)
BuildRequires:  mvn(org.testng:testng)
BuildRequires:  mvn(org.testng:testng::jdk15:)
%endif


# PpidChecker relies on /usr/bin/ps to check process uptime
Requires:       libprocps procps
Source44: import.info

%description
Surefire is a test framework project.

%package plugin
Group: Development/Java
Summary:        Surefire plugin for maven
Requires:       %{name}-provider-junit = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-provider-junit5 = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-provider-testng = %{?epoch:%epoch:}%{version}-%{release}

%description plugin
Maven surefire plugin for running tests via the surefire framework.

%package provider-junit
Group: Development/Java
Summary:        JUnit provider for Maven Surefire

%description provider-junit
JUnit provider for Maven Surefire.

%package provider-junit5
Group: Development/Java
Summary:        JUnit 5 provider for Maven Surefire

%description provider-junit5
JUnit 5 provider for Maven Surefire.

%package provider-testng
Group: Development/Java
Summary:        TestNG provider for Maven Surefire

%description provider-testng
TestNG provider for Maven Surefire.

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

%pom_disable_module maven-surefire-report-plugin
%pom_disable_module surefire-report-parser
%pom_disable_module surefire-shadefire

%pom_remove_dep :maven-toolchain maven-surefire-common

%pom_disable_module surefire-grouper
%pom_remove_dep :surefire-grouper surefire-providers/common-junit48
%pom_remove_dep :surefire-grouper surefire-providers/surefire-testng-utils
rm surefire-providers/common-junit48/src/main/java/org/apache/maven/surefire/common/junit48/{FilterFactory,GroupMatcherCategoryFilter}.java
rm surefire-providers/surefire-testng-utils/src/main/java/org/apache/maven/surefire/testng/utils/GroupMatcherMethodSelector.java

%pom_remove_dep -r org.apache.maven.surefire:surefire-shadefire

# Help plugin is needed only to evaluate effective Maven settings.
# For building RPM package default settings will suffice.
%pom_remove_plugin :maven-help-plugin surefire-its

# QA plugin useful only for upstream
%pom_remove_plugin -r :jacoco-maven-plugin
# Not wanted
%pom_remove_plugin -r :maven-shade-plugin
# Not in Fedora
%pom_remove_plugin -r :animal-sniffer-maven-plugin
# Complains
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
# We don't need site-source
%pom_remove_plugin :maven-assembly-plugin maven-surefire-plugin
%pom_remove_dep -r ::::site-source

%build
%mvn_package ":*{surefire-plugin}*" @1
%mvn_package ":*junit-platform*" junit5
%mvn_package ":*{junit,testng,failsafe-plugin}*"  @1
%mvn_package ":*tests*" __noinstall
# tests turned off because they need jmock
%mvn_build -f -- -DcommonsIoVersion=2.8.0 -DcommonsLang3Version=3.11

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE NOTICE cpl-v10.html

%files plugin -f .mfiles-surefire-plugin
%files provider-junit -f .mfiles-junit
%files provider-junit5 -f .mfiles-junit5
%files provider-testng -f .mfiles-testng
%files -n maven-failsafe-plugin -f .mfiles-failsafe-plugin

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE cpl-v10.html

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:3.0.0_M4-alt1_3jpp11
- fixed build with maven-shared-utils

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

