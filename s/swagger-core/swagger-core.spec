Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.5.10
%global namedreltag %nil
%global namedversion %{version}%{?namedreltag}
Name:          swagger-core
Version:       1.5.10
Release:       alt1_3jpp8
Summary:       Java implementation of Swagger
# Source files without license headers https://github.com/swagger-api/swagger-core/issues/1882
License:       ASL 2.0
URL:           http://swagger.io/
Source0:       https://github.com/swagger-api/swagger-core/archive/v%{namedversion}/%{name}-%{namedversion}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(asm:asm)
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(ch.qos.logback:logback-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires: mvn(com.fasterxml.jackson.datatype:jackson-datatype-guava)
BuildRequires: mvn(com.fasterxml.jackson.datatype:jackson-datatype-joda)
BuildRequires: mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.sun.jersey:jersey-client:1)
BuildRequires: mvn(com.sun.jersey:jersey-core:1)
BuildRequires: mvn(com.sun.jersey:jersey-server:1)
BuildRequires: mvn(com.sun.jersey:jersey-servlet:1)
BuildRequires: mvn(com.sun.jersey.contribs:jersey-multipart:1)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(javax.validation:validation-api)
BuildRequires: mvn(javax.ws.rs:jsr311-api)
BuildRequires: mvn(joda-time:joda-time)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires: mvn(org.glassfish.jersey.containers:jersey-container-servlet-core)
BuildRequires: mvn(org.glassfish.jersey.media:jersey-media-multipart)
BuildRequires: mvn(org.hibernate:hibernate-validator)
BuildRequires: mvn(org.joda:joda-convert)
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.powermock:powermock-api-mockito)
BuildRequires: mvn(org.reflections:reflections)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(org.testng:testng)

BuildArch:     noarch
Source44: import.info

%description
The goal of Swagger is to define a standard, language-agnostic interface
to REST APIs which allows both humans and computers to discover and
understand the capabilities of the service without access to source code,
documentation, or through network traffic inspection. When properly defined
via Swagger, a consumer can understand and interact with the remote service
with a minimal amount of implementation logic. Similar to what interfaces
have done for lower level programming, Swagger removes the guesswork
in calling the service.

%package annotations
Group: Development/Java
Summary:       Swagger Annotations

%description annotations
Swagger Annotations that configures definition level metadata.

%package hibernate-validations
Group: Development/Java
Summary:       Swagger Hibernate Validations

%description hibernate-validations
Swagger Hibernate Validations support.

%package jaxrs
Group: Development/Java
Summary:       Swagger JAXRS

%description jaxrs
Swagger *JAX-RS* support.

%package jersey-jaxrs
Group: Development/Java
Summary:       Swagger Models

%description jersey-jaxrs
Swagger Jersey 1.x *JAX-RS* support.

%package jersey2-jaxrs
Group: Development/Java
Summary:       Swagger Models

%description jersey2-jaxrs
Swagger Jersey 2.x *JAX-RS* support.

%package models
Group: Development/Java
Summary:       Swagger Models

%description models
Swagger Models module.

%package mule
Group: Development/Java
Summary:       Swagger Mule

%description mule
Swagger Mule.

%package project
Group: Development/Java
Summary:       Swagger Parent POM

%description project
Swagger Parent POM.

%package servlet
Group: Development/Java
Summary:       Swagger Servlet

%description servlet
Swagger Servlet.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

# Dependency convergence error
%pom_remove_plugin :maven-enforcer-plugin

# Unwanted plugins
%pom_xpath_remove "pom:build/pom:extensions"
%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin -r :jetty-maven-plugin

# Unwanted task
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-javadoc-plugin']/pom:executions"

%pom_change_dep -r org.glassfish.hk2.external:javax.inject javax.inject:javax.inject:1

%pom_xpath_set "pom:properties/pom:jersey-version" 1

# Force glassfish-servlet-api use
%pom_xpath_set "pom:properties/pom:servlet-api-version" 3.1.0
%pom_change_dep -r javax.servlet:servlet-api javax.servlet:javax.servlet-api:'${servlet-api-version}'

# Unavailable Test deps
# com.openpojo:openpojo:0.8.0
%pom_remove_dep com.openpojo:openpojo modules/swagger-models
rm modules/swagger-models/src/test/java/io/swagger/PojosTest.java
# org.powermock:powermock-module-testng:1.6.4
%pom_remove_dep org.powermock:powermock-module-testng modules/swagger-models
rm modules/swagger-models/src/test/java/io/swagger/models/ArrayModelTest.java \
 modules/swagger-models/src/test/java/io/swagger/models/ModelImplTest.java

#java.lang.AssertionError: expected [4] but found [2]
rm modules/swagger-core/src/test/java/io/swagger/ModelConverterTest.java
#java.lang.AssertionError: Serialized object:
#{"in":"query","required":false,"type":"integer","default":1234,"format":"1nt64"}
#does not equal to expected serialized string:
#{"in":"query","required":false,"type":"integer","default":1234,"format":"1nt64"}
rm modules/swagger-core/src/test/java/io/swagger/parameter/ParameterSerializationTest.java

# com.jayway.restassured:rest-assured:2.8.0
%pom_remove_dep -r com.jayway.restassured:rest-assured
rm modules/swagger-jaxrs/src/test/java/io/swagger/functional/test/ApiListingResourceIT.java

%build
# Disable (temporarily) test suite. Until rhbz#1369224, 1369232 are not fixed
%mvn_build -sf

%install
%mvn_install

%files -f .mfiles-swagger-core
%doc README.md

%files annotations -f .mfiles-swagger-annotations
%doc LICENSE

%files hibernate-validations -f .mfiles-swagger-hibernate-validations
%files jaxrs -f .mfiles-swagger-jaxrs
%files jersey-jaxrs -f .mfiles-swagger-jersey-jaxrs
%files jersey2-jaxrs -f .mfiles-swagger-jersey2-jaxrs
%files models -f .mfiles-swagger-models
%files mule -f .mfiles-swagger-mule
%files project -f .mfiles-swagger-project
%doc LICENSE

%files servlet -f .mfiles-swagger-servlet

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.10-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.10-alt1_2jpp8
- new jpp release

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.8-alt1_2jpp8
- new version

