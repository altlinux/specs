Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name hibernate-validator
%define version 5.2.4
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global majorversion 5
Name:          hibernate-validator
Version:       5.2.4
Release:       alt1_1jpp8
Summary:       Bean Validation 1.1 (JSR 349) Reference Implementation
License:       ASL 2.0
URL:           http://www.hibernate.org/subprojects/validator.html
Source0:       https://github.com/hibernate/hibernate-validator/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz
# JAXB2 and JDK7+ problems see https://hibernate.atlassian.net/browse/HV-528
Patch0:        %{name}-5.2.4.Final-jaxb.patch

BuildRequires: maven-local
BuildRequires: mvn(com.fasterxml:classmate)
BuildRequires: mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires: mvn(com.thoughtworks.paranamer:paranamer)
BuildRequires: mvn(javax.annotation:javax.annotation-api)
BuildRequires: mvn(javax.el:javax.el-api)
BuildRequires: mvn(javax.enterprise:cdi-api)
BuildRequires: mvn(javax.validation:validation-api)
BuildRequires: mvn(javax.xml.bind:jaxb-api)
BuildRequires: mvn(joda-time:joda-time)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.codehaus.mojo:jaxb2-maven-plugin)
BuildRequires: mvn(org.glassfish.web:javax.el)
BuildRequires: mvn(org.hibernate.javax.persistence:hibernate-jpa-2.1-api)
BuildRequires: mvn(org.jboss.arquillian:arquillian-bom:pom:)
BuildRequires: mvn(org.jboss.maven.plugins:maven-injection-plugin)
BuildRequires: mvn(org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec)
BuildRequires: mvn(org.jboss.logging:jboss-logging) >= 3.1.1
BuildRequires: mvn(org.jboss.logging:jboss-logging-processor:1)
BuildRequires: mvn(org.jboss.maven.plugins:maven-injection-plugin)
BuildRequires: mvn(org.jboss.shrinkwrap:shrinkwrap-bom:pom:)
BuildRequires: mvn(org.jboss.shrinkwrap.descriptors:shrinkwrap-descriptors-bom:pom:)
BuildRequires: mvn(org.jboss.shrinkwrap.resolver:shrinkwrap-resolver-bom:pom:)
BuildRequires: mvn(org.jsoup:jsoup)
BuildRequires: mvn(org.testng:testng)

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

%package parent
Group: Development/Java
Summary:       Hibernate Validator Parent POM

%description parent
Aggregator of the Hibernate Validator modules.

%package performance
Group: Development/Java
Summary:       Hibernate Validator Performance Tests

%description performance
Hibernate Validator performance tests.

%package test-utils
Group: Development/Java
Summary:       Hibernate Validator Test Utils

%description test-utils
Hibernate Validator Test Utils.

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

%patch0 -p1

%pom_disable_module distribution
%pom_disable_module documentation
%pom_disable_module engine-jdk8-tests
%pom_disable_module integration
%pom_disable_module osgi
%pom_disable_module tck-runner

# https://hibernate.atlassian.net/browse/HV-1069
%pom_remove_dep :fest-assert test-utils
rm -r test-utils/src/main/java/org/hibernate/validator/testutil/ConstraintViolationAssert.java \
 test-utils/src/main/java/org/hibernate/validator/testutil/DescriptorAssert.java \
 test-utils/src/main/java/org/hibernate/validator/testutil/MessageLoggedAssertionLogger.java

# documentation plugins
%pom_remove_plugin :maven-jdocbook-plugin
%pom_remove_plugin org.zanata:zanata-maven-plugin
# tck-runner and documentation plugins
%pom_remove_plugin -r org.codehaus.gmaven:gmaven-plugin
%pom_remove_plugin -r org.codehaus.mojo:clirr-maven-plugin
%pom_remove_plugin -r org.codehaus.mojo:chronos-jmeter-maven-plugin
%pom_remove_plugin org.codehaus.mojo:chronos-report-maven-plugin performance

%pom_xpath_remove "pom:build/pom:extensions"

%pom_remove_plugin -r :maven-dependency-plugin
%pom_remove_plugin -r :maven-surefire-report-plugin
%pom_remove_plugin -r :animal-sniffer-maven-plugin

%pom_xpath_inject "pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration" " <excludePackageNames>*.internal.*</excludePackageNames>"

%pom_xpath_set "pom:maven.javadoc.skip" false

# https://bugs.openjdk.java.net/browse/JDK-8067747
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration" \
 "<useIncrementalCompilation>false</useIncrementalCompilation>"

%pom_xpath_set "pom:properties/pom:jboss.logging.processor.version" 1
%pom_change_dep :jboss-logging-processor ::'${jboss.logging.processor.version}' engine

# Unavailable deps JavaFX
rm engine/src/main/java/org/hibernate/validator/internal/engine/valuehandling/JavaFXPropertyValueUnwrapper.java

%build

# Running tests requires hibernate proper (and require weld-core >= 2.0.0 groovy >= 2.1.0), so skip for now:
%mvn_build -f -s -- -Pdist

%install
%mvn_install

%files -f .mfiles-%{name}
%doc CONTRIBUTING.md README.md changelog.txt
%doc copyright.txt license.txt

%files annotation-processor -f .mfiles-%{name}-annotation-processor
%doc copyright.txt license.txt

%files cdi -f .mfiles-%{name}-cdi
%files parent -f .mfiles-%{name}-parent
%doc copyright.txt license.txt

%files performance -f .mfiles-%{name}-performance
%doc copyright.txt license.txt

%files test-utils -f .mfiles-%{name}-test-utils
%doc copyright.txt license.txt

%files javadoc -f .mfiles-javadoc
%doc copyright.txt license.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 5.2.4-alt1_1jpp8
- new version

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

