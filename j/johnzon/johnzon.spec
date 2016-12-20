Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          johnzon
Version:       0.9.4
Release:       alt1_1jpp8
Summary:       Implementation of JSR-353
License:       ASL 2.0
URL:           http://johnzon.apache.org/
Source0:       http://www.apache.org/dist/johnzon/%{name}-%{version}/apache-%{name}-%{version}-src.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.h2database:h2)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(javax.enterprise:cdi-api)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(javax.json:javax.json-api)
BuildRequires: mvn(javax.websocket:javax.websocket-api)
BuildRequires: mvn(javax.ws.rs:javax.ws.rs-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-interceptor_3.0_spec)
BuildRequires: mvn(org.apache.geronimo.specs:specs-parent:pom:)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.plugins:maven-checkstyle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.apache.openjpa:openjpa-jdbc)
BuildRequires: mvn(org.apache.openjpa:openjpa-lib)
BuildRequires: mvn(org.apache.openjpa:openjpa-persistence)
BuildRequires: mvn(org.apache.openjpa:openjpa-persistence-jdbc)
BuildRequires: mvn(org.apache.openwebbeans:openwebbeans-impl)
BuildRequires: mvn(org.apache.rat:apache-rat-plugin)
BuildRequires: mvn(org.apache.tomcat:tomcat-api)
BuildRequires: mvn(org.apache.tomcat:tomcat-servlet-api)
BuildRequires: mvn(org.jboss.arquillian.junit:arquillian-junit-container)
#BuildRequires: /usr/bin/asciidoctor

BuildArch:     noarch
Source44: import.info

%description
Apache Johnzon is a project providing an implementation of JsonProcessing and
a set of useful extension for this specification like an Object mapper,
some JAX-RS providers and a WebSocket module provides a basic integration with
Java WebSocket API (JSR 356).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%package jaxrs
Group: Development/Java
Summary:       Johnzon :: JAX-RS

%description jaxrs
Johnzon :: JAX-RS Implementation.

%package jsonb
Group: Development/Java
Summary:       Johnzon :: JSON-B

%description jsonb
Johnzon :: JSON-B Implementation.

%package jsonb-api
Group: Development/Java
Summary:       Johnzon :: JSON-B API

%description jsonb-api
Johnzon :: JSON-B API.

%package mapper
Group: Development/Java
Summary:       Johnzon :: Mapper

%description mapper
Johnzon :: Mapper.

%package maven-plugin
Group: Development/Java
Summary:       Johnzon :: Maven Plugin

%description maven-plugin
Johnzon :: Maven Plugin.

%package parent
Group: Development/Java
Summary:       Johnzon :: Parent POM

%description parent
Johnzon :: Parent POM.

%package websocket
Group: Development/Java
Summary:       Johnzon :: WebSocket

%description websocket
Johnzon :: WebSocket Implementation.

%prep
%setup -q -n apache-%{name}-%{version}-src

%pom_disable_module johnzon-distribution

# Unavailable plugin
%pom_remove_plugin -r :cobertura-maven-plugin
%pom_remove_plugin :cobertura-maven-plugin johnzon-websocket
%pom_remove_plugin -r :coveralls-maven-plugin

# Unneeded tasks
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-scm-publish-plugin
%pom_remove_plugin -r :maven-site-plugin
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"

# Use glassfish apis
%pom_change_dep -r :geronimo-json_1.0_spec javax.json:javax.json-api:1.0
%pom_change_dep org.apache.tomcat:tomcat-websocket-api javax.websocket:javax.websocket-api:1.1 johnzon-websocket

# Execution default-test of goal org.apache.maven.plugins:maven-surefire-plugin:2.19.1:test failed:
# The forked VM terminated without properly saying goodbye. VM crash or System.exit called?
sed -i "s|-Xms1024m -Xmx2048m|-Xms512m -Xmx512m|" pom.xml

%pom_change_dep org.apache.openjpa:openjpa org.apache.openjpa:openjpa-persistence johnzon-mapper
%pom_add_dep org.apache.openjpa:openjpa-lib:2.4.0:test johnzon-mapper
%pom_add_dep org.apache.openjpa:openjpa-jdbc:2.4.0:test johnzon-mapper
%pom_add_dep org.apache.openjpa:openjpa-persistence-jdbc:2.4.0:test johnzon-mapper

# Unavailable test deps
# com.github.stefanbirkner:system-rules:1.8.0
%pom_remove_dep com.github.stefanbirkner:system-rules johnzon-mapper
rm johnzon-mapper/src/test/java/org/apache/johnzon/mapper/NoWarningTest.java
# org.apache.tomee:arquillian-tomee-remote:7.0.1
%pom_remove_dep org.apache.tomee:arquillian-tomee-remote johnzon-websocket
rm johnzon-websocket/src/test/java/org/apache/johnzon/websocket/MapperCodecTest.java
# org.apache.tomee:apache-tomee:zip:7.0.1
%pom_remove_dep org.apache.tomee:apache-tomee johnzon-websocket
rm johnzon-websocket/src/test/java/org/apache/johnzon/websocket/JsrCodecTest.java
# org.apache.cxf:3.0.0
%pom_remove_dep -r org.apache.cxf:cxf-rt-rs-client johnzon-jaxrs johnzon-jsonb
%pom_remove_dep -r org.apache.cxf:cxf-rt-frontend-jaxrs johnzon-jaxrs johnzon-jsonb
%pom_remove_dep -r org.apache.cxf:cxf-rt-transports-local johnzon-jaxrs johnzon-jsonb
rm -r johnzon-jaxrs/src/test/java johnzon-jsonb/src/test/java/org/apache/johnzon/jsonb/jaxrs/JsonbJaxRsTest.java
# org.apache.tomcat:8.5.3
%pom_remove_dep org.apache.tomcat:tomcat-websocket johnzon-websocket

# Fix test deps
# package javax.ws.rs does not exist
%pom_add_dep javax.ws.rs:javax.ws.rs-api:2.0.1:test johnzon-websocket
%pom_change_dep :geronimo-jcdi_1.1_spec javax.enterprise:cdi-api johnzon-jsonb
%pom_change_dep :geronimo-atinject_1.0_spec javax.inject:javax.inject johnzon-jsonb
%pom_change_dep :geronimo-interceptor_1.2_spec :geronimo-interceptor_3.0_spec johnzon-jsonb

# openwebbeans:1.6.2
# javax.json.stream.JsonGenerationException: Invalid json
rm johnzon-jsonb/src/test/java/org/apache/johnzon/jsonb/CdiAdapterTest.java

%build

%mvn_build -s

# Re-generate documentation
#rm MATURITY.html
#asciidoctor MATURITY.adoc

%install
%mvn_install

%files -f .mfiles-johnzon-core
%doc MATURITY.html
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%files jaxrs -f .mfiles-johnzon-jaxrs
%files jsonb -f .mfiles-johnzon-jsonb
%files jsonb-api -f .mfiles-jsonb-api
%doc LICENSE NOTICE

%files mapper -f .mfiles-johnzon-mapper
%files maven-plugin -f .mfiles-johnzon-maven-plugin
%files parent -f .mfiles-johnzon
%doc LICENSE NOTICE

%files websocket -f .mfiles-johnzon-websocket

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1_1jpp8
- new version

