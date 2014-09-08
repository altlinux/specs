Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-surefire
Version:        2.16
Release:        alt1_1jpp7
Epoch:          0
Summary:        Test framework project
License:        ASL 2.0 and CPL
URL:            http://maven.apache.org/surefire/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/surefire/surefire/%{version}/surefire-%{version}-source-release.zip
Source2:        http://junit.sourceforge.net/cpl-v10.html
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-decoration-model)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven.shared:maven-verifier)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-plugin-descriptor)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven:maven-toolchain)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.testng:testng)

BuildRequires:  maven-invoker-plugin
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-shared-utils
BuildRequires:  maven-shared-verifier
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-failsafe-plugin
BuildRequires:  maven-surefire-plugin >= 0:2.12-1
BuildRequires:  maven-toolchain
BuildRequires:  maven-project
BuildRequires:  maven-shared-common-artifact-filters
BuildRequires:  modello
BuildRequires:  plexus-containers-component-api >= 1.0-0.a34
BuildRequires:  maven-plugin-testing-harness
BuildRequires:  javacc-maven-plugin

Obsoletes:      maven-surefire-booter <= 0:1.5.3
Provides:       maven-surefire-booter = %{epoch}:%{version}-%{release}
Source44: import.info

%description
Surefire is a test framework project.

%package plugin
Group: Development/Java
Summary:                Surefire plugin for maven
Obsoletes:              maven2-plugin-surefire <= 0:2.0.4
Provides:               maven2-plugin-surefire = %{epoch}:%{version}-%{release}
Obsoletes:              maven-surefire-maven-plugin < 0:2.6
Provides:               maven-surefire-maven-plugin = %{epoch}:%{version}-%{release}

%description plugin
Maven surefire plugin for running tests via the surefire framework.

%package report-plugin
Group: Development/Java
Summary:                Surefire reports plugin for maven
Obsoletes:              maven2-plugin-surefire-report <= 0:2.0.4
Provides:               maven2-plugin-surefire-report = %{epoch}:%{version}-%{release}
Obsoletes:              maven-surefire-report-maven-plugin < 0:2.6
Provides:               maven-surefire-report-maven-plugin = %{epoch}:%{version}-%{release}

%description report-plugin
Plugin for generating reports from surefire test runs.


%package provider-junit
Group: Development/Java
Summary:                JUnit provider for Maven Surefire
Obsoletes:              maven2-plugin-surefire-report <= 0:2.0.4O
Provides:               maven2-plugin-surefire-report = %{epoch}:%{version}-%{release}
Obsoletes:              %{name}-provider-junit4 < %{epoch}:%{version}-%{release}
Provides:               %{name}-provider-junit4 = %{epoch}:%{version}-%{release}

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
%pom_add_dep org.apache.maven:maven-compat maven-surefire-common
%pom_disable_module surefire-shadefire

for module in maven-failsafe-plugin maven-surefire-common \
        maven-surefire-plugin surefire-api surefire-booter \
        surefire-grouper surefire-providers \
        surefire-setup-integration-tests \
        surefire-report-parser; do
    %pom_remove_dep org.apache.maven.surefire:surefire-shadefire $module
done

# Help plugin is needed only to evaluate effective Maven settings.
# For building RPM package default settings will suffice.
%pom_remove_plugin :maven-help-plugin surefire-setup-integration-tests

%build
%mvn_package ":*{surefire-plugin,report-plugin}*" @1
%mvn_package ":*{junit,testng,failsafe-plugin,report-parser}*"  @1
%mvn_package ":*tests*" __noinstall
# tests turned off because they need jmock
%mvn_build -f

%install
%mvn_install


%files -f .mfiles
%doc README.TXT
%doc LICENSE NOTICE cpl-v10.html
%dir %{_javadir}/maven-surefire

%files plugin -f .mfiles-surefire-plugin
%files report-plugin -f .mfiles-report-plugin
%files report-parser -f .mfiles-report-parser
%files provider-junit -f .mfiles-junit
%files provider-testng -f .mfiles-testng
%files -n maven-failsafe-plugin -f .mfiles-failsafe-plugin

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE cpl-v10.html

%changelog
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

