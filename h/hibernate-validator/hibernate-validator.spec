Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name hibernate-validator
%define version 5.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global majorversion 5
Name:          hibernate-validator
Version:       5.0.1
Release:       alt1_6jpp8
Summary:       Bean Validation 1.1 (JSR 349) Reference Implementation
License:       ASL 2.0
URL:           http://www.hibernate.org/subprojects/validator.html
Source0:       https://github.com/hibernate/hibernate-validator/archive/%{namedversion}.tar.gz
# JAXB2 and JDK7 problems see https://hibernate.atlassian.net/browse/HV-528
Patch0:        %{name}-5.0.1.Final-jaxb.patch

BuildRequires: cdi-api
BuildRequires: bean-validation-api
BuildRequires: classmate
BuildRequires: glassfish-annotation-api
BuildRequires: glassfish-el
BuildRequires: glassfish-el-api
BuildRequires: glassfish-jaxb
BuildRequires: glassfish-jaxb-api
BuildRequires: hibernate-jpa-2.1-api
BuildRequires: jboss-interceptors-1.2-api
BuildRequires: jboss-logging >= 3.1.1
# 1.7.1
BuildRequires: jsoup
BuildRequires: joda-time
BuildRequires: junit

BuildRequires: jaxb2-maven-plugin
# 1.0.3.Final
BuildRequires: jboss-logging-tools
BuildRequires: maven-local
#BuildRequires: maven-dependency-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-injection-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-processor-plugin
%if 0
BuildRequires: beanvalidation-tck
BuildRequires: maven-failsafe-plugin
%endif

BuildArch:     noarch
Source44: import.info

%description
This is the reference implementation of JSR-349 - Bean Validation 1.1.
Bean Validation defines a meta-data model and API for JavaBean as well
as method validation. The default meta-data source are annotations,
with the ability to override and extend the meta-data through the
use of XML validation descriptors.

%package annotation-processor
Group: Development/Java
Summary:       Hibernate Validator Annotation Processor

%description annotation-processor
Hibernate Validator Annotation Processor.

%package cdi
Group: Development/Java
Summary:       Hibernate Validator Portable Extension

%description cdi
Hibernate Validator CDI Portable Extension.

%package performance
Group: Development/Java
Summary:       Hibernate Validator Performance Tests

%description performance
Hibernate Validator performance tests.

%if 0
%package integration
Group: Development/Java
Summary:       Hibernate Validator AS Integration Tests

%description integration
Hibernate Validator integration tests.

%package tck-runner
Group: Development/Java
Summary:       Hibernate Validator TCK Runner

%description tck-runner
Aggregates dependencies and runs the JSR-349 TCK.
%endif

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
find . -name "*.jar" -delete
# tck-runner/src/as7config/modules/org/jboss/as/ee/main/jboss-as-ee-7.1.1.Final.jar
%pom_disable_module distribution
%pom_disable_module documentation
# documentation plugins
%pom_remove_plugin :maven-jdocbook-plugin
%pom_remove_plugin org.zanata:zanata-maven-plugin
# tck-runner and documentation plugins
%pom_remove_plugin org.codehaus.gmaven:gmaven-plugin
%pom_remove_plugin org.codehaus.gmaven:gmaven-plugin integration
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin
%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-surefire-report-plugin
%pom_remove_plugin org.codehaus.mojo:chronos-jmeter-maven-plugin

%pom_remove_plugin org.apache.maven.plugins:maven-surefire-report-plugin engine
%pom_remove_plugin org.codehaus.mojo:chronos-jmeter-maven-plugin performance
%pom_remove_plugin org.codehaus.mojo:chronos-report-maven-plugin performance

%pom_xpath_remove "pom:build/pom:extensions"
# groovy 2.1.0
%pom_remove_dep org.codehaus.groovy:groovy-jsr223
# 2.0.0.CR2
%pom_remove_dep org.jboss.weld:weld-core
%pom_remove_dep org.jboss.as:jboss-as-arquillian-container-managed
%pom_remove_dep org.jboss.arquillian.container:arquillian-weld-se-embedded-1.1
%pom_remove_dep org.jboss.arquillian:arquillian-bom
%pom_remove_dep :fest-assert
%pom_remove_dep :easymock
%pom_remove_dep :log4j
%pom_remove_dep :slf4j-log4j12
%pom_remove_dep :testng

%pom_remove_plugin :maven-dependency-plugin tck-runner
%pom_remove_plugin :maven-surefire-report-plugin tck-runner
%pom_remove_plugin :maven-dependency-plugin annotation-processor

%pom_xpath_remove "pom:dependencies/pom:dependency[pom:scope ='test']" annotation-processor
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:scope ='test']" cdi
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:scope ='test']" engine
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:scope ='test']" integration
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:scope ='test']" tck-runner

%patch0 -p1

%pom_disable_module integration
%pom_disable_module tck-runner

%pom_xpath_inject "pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration" "
<excludePackageNames>*.internal.*</excludePackageNames>"

%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration" "
<excludePackageNames>*.internal.*</excludePackageNames>" engine

%build
%mvn_package ":%{name}-parent" %{name}
# Running tests requires hibernate proper (and require weld-core >= 2.0.0 groovy >= 2.1.0), so skip for now:
%mvn_build -f -s -- -Pdist

%install
%mvn_install

install -m 644 engine/target/hibernate-validator-%{namedversion}-testing.jar \
    %{buildroot}%{_javadir}/%{name}/%{name}-testing.jar

%files -f .mfiles-%{name}
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-testing.jar
%doc CONTRIBUTING.md README.md changelog.txt
%doc copyright.txt license.txt

%files annotation-processor -f .mfiles-%{name}-annotation-processor
%doc copyright.txt license.txt

%files cdi -f .mfiles-%{name}-cdi
%doc copyright.txt license.txt

%files performance -f .mfiles-%{name}-performance
%doc copyright.txt license.txt

%if 0
%files integration -f .mfiles-%{name}-integrationtest-as
%doc copyright.txt license.txt

%files tck-runner -f .mfiles-%{name}-tck-runner
%doc copyright.txt license.txt
%endif

%files javadoc -f .mfiles-javadoc
%doc copyright.txt license.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.1-alt1_6jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.1-alt1_5jpp8
- java 8 mass update

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt2_8jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1_5jpp7
- new version

