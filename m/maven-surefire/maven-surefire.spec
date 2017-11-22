Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-surefire
Version:        2.20.1
Release:        alt1_3jpp8
Epoch:          0
Summary:        Test framework project
License:        ASL 2.0 and CPL
URL:            http://maven.apache.org/surefire/
BuildArch:      noarch

Source0:        http://repo2.maven.org/maven2/org/apache/maven/surefire/surefire/%{version}/surefire-%{version}-source-release.tar
Source2:        http://junit.sourceforge.net/cpl-v10.html

Patch0:         0001-Maven-3.patch
Patch1:         0002-Fix-test-with-doxia-1.7.patch
Patch2:         0003-Port-to-TestNG-6.11.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven.shared:maven-verifier)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit47)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.testng:testng)
BuildRequires:  mvn(org.testng:testng::jdk15:)

# PpidChecker relies on /usr/bin/ps to check process uptime
Requires:       procps sysvinit-utils
Source44: import.info

%description
Surefire is a test framework project.

%package plugin
Group: Development/Java
Summary:                Surefire plugin for maven

%description plugin
Maven surefire plugin for running tests via the surefire framework.

%package report-plugin
Group: Development/Java
Summary:                Surefire reports plugin for maven

%description report-plugin
Plugin for generating reports from surefire test runs.

%package provider-junit
Group: Development/Java
Summary:                JUnit provider for Maven Surefire

%description provider-junit
JUnit provider for Maven Surefire.

%package provider-testng
Group: Development/Java
Summary:                TestNG provider for Maven Surefire

%description provider-testng
TestNG provider for Maven Surefire.

%package report-parser
Group: Development/Java
Summary:                Parses report output files from surefire

%description report-parser
Plugin for parsing report output files from surefire.

%package -n maven-failsafe-plugin
Group: Development/Java
Summary:                Maven plugin for running integration tests

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
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n surefire-%{version}
cp -p %{SOURCE2} .

%patch0 -p1
%patch1 -p1
%patch2 -p1

# Disable strict doclint
sed -i /-Xdoclint:all/d pom.xml

%pom_disable_module surefire-shadefire

%pom_remove_dep -r org.apache.maven.surefire:surefire-shadefire

# Help plugin is needed only to evaluate effective Maven settings.
# For building RPM package default settings will suffice.
%pom_remove_plugin :maven-help-plugin surefire-setup-integration-tests

# Not in Fedora
%pom_remove_plugin :animal-sniffer-maven-plugin
# Complains
%pom_remove_plugin :apache-rat-plugin
# We don't need site-source
%pom_remove_plugin :maven-assembly-plugin maven-surefire-plugin
%pom_remove_dep -r ::::site-source

%pom_xpath_set pom:mavenVersion 3.3.3
%pom_remove_dep :maven-project maven-surefire-report-plugin
%pom_remove_dep :maven-project maven-surefire-common
%pom_remove_dep :maven-plugin-descriptor maven-surefire-common
%pom_remove_dep :maven-toolchain maven-surefire-common

%pom_xpath_remove -r "pom:execution[pom:id='shared-logging-generated-sources']"

%pom_add_dep com.google.code.findbugs:jsr305 surefire-api

%build
%mvn_package ":*{surefire-plugin,report-plugin}*" @1
%mvn_package ":*{junit,testng,failsafe-plugin,report-parser}*"  @1
%mvn_package ":*tests*" __noinstall
# tests turned off because they need jmock
# use xmvn-javadoc because maven-javadoc-plugin crashes JVM
%mvn_build -f -j -G org.fedoraproject.xmvn:xmvn-mojo:javadoc

%install
%mvn_install


%files -f .mfiles
%doc README.md
%doc LICENSE NOTICE cpl-v10.html

%files plugin -f .mfiles-surefire-plugin
%files report-plugin -f .mfiles-report-plugin
%files report-parser -f .mfiles-report-parser
%files provider-junit -f .mfiles-junit
%files provider-testng -f .mfiles-testng
%files -n maven-failsafe-plugin -f .mfiles-failsafe-plugin

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE cpl-v10.html

%changelog
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

