Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%global with_grizzly 1
# Use jetty 9.1.1.v20140108.
#def_with jetty
%bcond_with jetty
Name:          jersey
Version:       2.18
Release:       alt1_3jpp8
Summary:       JAX-RS (JSR 311) production quality Reference Implementation
# One file in jersey-core/ is under ASL 2.0 license
# https://java.net/jira/browse/JERSEY-2870
License:       (CDDL or GPLv2 with exceptions) and ASL 2.0
URL:           http://jersey.java.net/
Source0:       https://github.com/jersey/jersey/archive/%{version}.tar.gz
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt
# Remove repackaged dependencies: guava, atinject
Patch0:        jersey-2.18-use-system-libraries.patch
# Support fo servlet 3.1 apis
Patch1:        jersey-2.17-mvc-jsp-servlet31.patch
# Update istack plugin reference
Patch2:        jersey-2.17-new-istack-plugin.patch

BuildRequires: maven-local
BuildRequires: mvn(com.esotericsoftware:kryo)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-base)
BuildRequires: mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider)
BuildRequires: mvn(com.github.spullara.mustache.java:compiler)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.sun.istack:istack-commons-maven-plugin)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(io.reactivex:rxjava)
BuildRequires: mvn(javax.annotation:javax.annotation-api)
BuildRequires: mvn(javax.el:javax.el-api)
BuildRequires: mvn(javax.enterprise:cdi-api) >= 1.1
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(javax.json:javax.json-api)
BuildRequires: mvn(javax.persistence:persistence-api)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(javax.servlet.jsp:jsp-api)
BuildRequires: mvn(javax.validation:validation-api)
BuildRequires: mvn(javax.ws.rs:javax.ws.rs-api)
BuildRequires: mvn(javax.xml.bind:jaxb-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.java:jvnet-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.aspectj:aspectjrt)
BuildRequires: mvn(org.aspectj:aspectjweaver)
BuildRequires: mvn(org.codehaus.jackson:jackson-core-asl)
BuildRequires: mvn(org.codehaus.jackson:jackson-jaxrs)
BuildRequires: mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires: mvn(org.codehaus.jackson:jackson-xc)
BuildRequires: mvn(org.codehaus.jettison:jettison)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
%if %{with jetty}
BuildRequires: mvn(org.eclipse.jetty:jetty-client)
BuildRequires: mvn(org.eclipse.jetty:jetty-continuation)
BuildRequires: mvn(org.eclipse.jetty:jetty-server)
BuildRequires: mvn(org.eclipse.jetty:jetty-util)
BuildRequires: mvn(org.eclipse.jetty:jetty-webapp)
%endif
BuildRequires: mvn(org.freemarker:freemarker)
BuildRequires: mvn(org.glassfish:javax.json)
BuildRequires: mvn(org.glassfish:jsonp-jaxrs)
BuildRequires: mvn(org.glassfish.grizzly:grizzly-http-servlet)
BuildRequires: mvn(org.glassfish.hk2:hk2)
BuildRequires: mvn(org.glassfish.hk2:hk2-api)
BuildRequires: mvn(org.glassfish.hk2:hk2-bom:pom:)
BuildRequires: mvn(org.glassfish.hk2:hk2-locator)
BuildRequires: mvn(org.glassfish.hk2:osgi-resource-locator)
BuildRequires: mvn(org.glassfish.hk2:spring-bridge)
BuildRequires: mvn(org.glassfish.web:javax.el)
BuildRequires: mvn(org.hamcrest:hamcrest-library)
BuildRequires: mvn(org.hibernate:hibernate-validator)
BuildRequires: mvn(org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec)
BuildRequires: mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.2_spec)
BuildRequires: mvn(org.jboss:jboss-vfs)
BuildRequires: mvn(org.jboss.weld.se:weld-se-core)
BuildRequires: mvn(org.jvnet.jaxb2.maven2:maven-jaxb22-plugin)
# mimepull >= 1.9.5 https://bugzilla.redhat.com/show_bug.cgi?id=1189216
BuildRequires: mvn(org.jvnet.mimepull:mimepull)
BuildRequires: mvn(org.osgi:org.osgi.core)
BuildRequires: mvn(org.ow2.asm:asm-all)
BuildRequires: mvn(org.springframework:spring-aop)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.springframework:spring-web)
BuildRequires: mvn(org.testng:testng)
BuildRequires: mvn(xerces:xercesImpl)

Obsoletes:     maven-wadl-plugin
Provides:      %{name}-contribs
Obsoletes:     %{name}-contribs < 2.17-1

BuildArch:     noarch
Source44: import.info

%description
Jersey is the open source JAX-RS (JSR 311)
production quality Reference Implementation
for building RESTful Web services.

%package test-framework
Group: Development/Java
Summary:       Jersey Test Framework

%description test-framework
%{summary}.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
find . -name "*.jar" -print -delete
find . -name "*.class" -print -delete

%patch0 -p1
%patch1 -p1
%patch2 -p1

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

%pom_xpath_remove pom:build/pom:extensions

%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :buildnumber-maven-plugin core-common
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-source-plugin ext/wadl-doclet
%pom_remove_plugin :maven-source-plugin incubator/declarative-linking
%pom_remove_plugin :maven-jflex-plugin media/moxy
%pom_remove_plugin :maven-jflex-plugin media/jaxb
%pom_remove_plugin :maven-shade-plugin core-server

%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-javadoc-plugin' ]/pom:executions"
%pom_remove_plugin :maven-checkstyle-plugin

%pom_disable_module archetypes
%pom_disable_module bundles
%pom_remove_dep org.glassfish.jersey.bundles: bom
%pom_remove_dep org.glassfish.jersey.bundles.repackaged: bom
%pom_disable_module jersey-guava bundles/repackaged
%pom_disable_module examples
%pom_disable_module examples/java8-webapp
%pom_disable_module examples/rx-client-java8-webapp
%pom_disable_module gae-integration incubator
%pom_disable_module html-json incubator

# Use jersey-jsr166e bundle of Doug Lea's JCP JSR-166 APIS
%pom_disable_module rx-client-jsr166e ext/rx
%pom_remove_dep :jersey-rx-client-jsr166e bom
# org.glassfish.grizzly:grizzly-http-client:1.8
%pom_disable_module grizzly-connector connectors
%pom_remove_dep :jersey-grizzly-connector bom
# Use com.sun.jersey:jersey-servlet:1.17
%pom_disable_module servlet-portability ext
%pom_remove_dep :jersey-servlet-portability bom
%pom_disable_module tests
%pom_disable_module glassfish containers
%pom_remove_dep :jersey-gf-ejb bom

%if %{without jetty}
# Add support for jetty 9.3.0.M2
%pom_disable_module jetty-connector connectors
%pom_disable_module jetty-http containers
%pom_disable_module jetty-servlet containers
%pom_disable_module jetty test-framework/providers
%pom_remove_dep :jersey-container-jetty-http bom
%pom_remove_dep :jersey-container-jetty-servlet bom
%pom_remove_dep :jersey-jetty-connector bom
%pom_remove_dep :jersey-jetty-connector media/multipart
%pom_remove_dep :jersey-test-framework-provider-jetty bom
%pom_remove_dep :jersey-test-framework-provider-jetty test-framework/providers/bundle
%endif

# simple:5.1.4
%pom_disable_module simple-http containers
%pom_disable_module simple test-framework/providers
%pom_remove_dep :jersey-container-simple-http bom
%pom_remove_dep :jersey-test-framework-provider-simple bom
%pom_remove_dep :jersey-test-framework-provider-simple test-framework/providers/bundle
# eclipselink:2.6.0
%pom_disable_module moxy media
%pom_remove_dep :jersey-media-moxy bom

# Force servlet 3.1 apis
%pom_remove_dep org.mortbay.jetty:servlet-api-2.5
%pom_remove_dep org.mortbay.jetty:servlet-api-2.5 tests/osgi/functional
sed -i "s|<artifactId>servlet-api|<artifactId>javax.servlet-api|" $(find . -name "pom.xml")

# Fix asm aId (asm-debug-all)
%pom_xpath_set "pom:dependency[pom:groupId = 'org.ow2.asm']/pom:artifactId" asm-all
%pom_xpath_set "pom:dependency[pom:groupId = 'org.ow2.asm']/pom:artifactId" asm-all core-server
%pom_xpath_set "pom:dependency[pom:groupId = 'org.ow2.asm']/pom:artifactId" asm-all test-framework

# Prepare offline setting for generate java source code
cat > core-server/etc/bindings.cat << EOF
PUBLIC "-//W3C//DTD XMLSchema 200102//EN" "XMLSchema.dtd"
PUBLIC "XMLSchema" "XMLSchema.dtd"
SYSTEM "XMLSchema.dtd" "XMLSchema.dtd"

PUBLIC "datatypes" "datatypes.dtd"
SYSTEM "datatypes.dtd" "datatypes.dtd"

SYSTEM "xml.xsd" "xml.xsd"
EOF
rm -r core-server/etc/catalog.xml core-server/src/main/java/com/sun/research/ws/wadl
sed -i 's|schemaLocation="http://www.w3.org/2001/xml.xsd"|schemaLocation="./xml.xsd"|' core-server/etc/wadl.xsd

# Update plugin references
%pom_remove_plugin com.sun.tools.xjc.maven2: core-server
%pom_add_plugin "org.jvnet.jaxb2.maven2:maven-jaxb22-plugin:0.12.3" core-server '
<executions>
  <execution>
    <id>bindings</id>
    <phase>generate-sources</phase>
    <goals>
      <goal>generate</goal>
    </goals>
    <configuration>
      <generatePackage>com.sun.research.ws.wadl</generatePackage>
      <catalog>${basedir}/etc/bindings.cat</catalog>
      <schemaDirectory>${basedir}/etc</schemaDirectory>
      <bindingDirectory>${basedir}</bindingDirectory>
      <bindingIncludes>
        <bindingInclude>wadl.xsd</bindingInclude>
      </bindingIncludes>
      <forceRegenerate>false</forceRegenerate>
      <episode>true</episode>
      <specVersion>2.1</specVersion>
      <extension>true</extension>
      <strict>false</strict>
    </configuration>
  </execution>
</executions>'

%pom_xpath_remove "pom:plugin[pom:artifactId ='maven-surefire-plugin']/pom:configuration/pom:argLine" core-common
%pom_xpath_remove "pom:plugin[pom:artifactId ='maven-surefire-plugin']/pom:configuration/pom:argLine" core-server

%pom_remove_dep :javaee-api ext/cdi/jersey-cdi1x-transaction
# package javax.enterprise.context javax.enterprise.event javax.enterprise.inject.spi does not exist
%pom_add_dep javax.enterprise:cdi-api:'${cdi.api.version}':provided ext/cdi/jersey-cdi1x-transaction
# package javax.interceptor does not exist
%pom_add_dep org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec:1.0.0.Alpha3:provided ext/cdi/jersey-cdi1x-transaction
# cannot find symbol javax.transaction.Transactional javax.transaction.TransactionalException
%pom_add_dep org.jboss.spec.javax.transaction:jboss-transaction-api_1.2_spec:1.0.0.Alpha3:provided ext/cdi/jersey-cdi1x-transaction

%pom_xpath_remove "pom:dependencies/pom:dependency[pom:artifactId = 'tools']/pom:scope" ext/wadl-doclet
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:artifactId = 'tools']/pom:systemPath" ext/wadl-doclet

# ClassNotFoundException: javax.json.JsonStructure
%pom_add_dep javax.json:javax.json-api:1.0 media/json-processing

# Change scope form test to ..., cause: package com.google.common.util.concurrent does not exist
%pom_xpath_set "pom:dependency[pom:artifactId = 'guava']/pom:scope" provided connectors/apache-connector
%pom_xpath_set "pom:dependency[pom:artifactId = 'guava']/pom:scope" provided containers/jdk-http

# NoClassDefFoundError: org/objectweb/asm/ClassVisitor
%pom_add_dep org.ow2.asm:asm-all:5.0.3:test containers/jdk-http
%pom_add_dep org.ow2.asm:asm-all:5.0.3:test media/json-processing

# Jersey core server unit tests should run with active security manager
rm -r core-common/src/test/java/org/glassfish/jersey/SecurityManagerConfiguredTest.java
rm -r core-server/src/test/java/org/glassfish/jersey/server/SecurityManagerConfiguredTest.java
# Fails for various reason (use org.jboss:jboss-vfs:jar:3.2.6.Final)
rm -r core-server/src/test/java/org/glassfish/jersey/server/SecurityContextTest.java \
 core-server/src/test/java/org/glassfish/jersey/server/internal/process/ProxyInjectablesTest.java \
 core-server/src/test/java/org/glassfish/jersey/server/internal/inject/JaxRsInjectablesTest.java \
 core-server/src/test/java/org/glassfish/jersey/server/internal/routing/ResourcePushingTest.java \
 core-server/src/test/java/org/glassfish/jersey/server/model/ResourceInfoTest.java
# Exception: Unexpected exception, expected<java.security.AccessControlException> but was<java.lang.AssertionError>
rm -r core-common/src/test/java/org/glassfish/jersey/internal/util/ReflectionHelperTest.java
# Could not find javax.ws.rs-api.
rm -r core-server/src/test/java/org/glassfish/jersey/server/internal/scanning/JarFileScannerTest.java \
 core-server/src/test/java/org/glassfish/jersey/server/internal/scanning/PackageNamesScannerTest.java \
 core-server/src/test/java/org/glassfish/jersey/server/internal/scanning/VFSSchemeResourceFinderTest.java

rm -r test-framework/providers/grizzly2/src/test/java/org/glassfish/jersey/test/grizzly/web/GrizzlyWebInjectionTest.java

# NO test dep
%pom_remove_dep org.jmockit:jmockit ext/cdi/jersey-cdi1x
rm -r ext/cdi/jersey-cdi1x/src/test/java/org/glassfish/jersey/ext/cdi1x/internal/CdiUtilTest.java
rm -r ext/cdi/jersey-cdi1x/src/test/java/*
%pom_remove_dep org.glassfish.jersey.connectors:jersey-grizzly-connector media/multipart
%pom_remove_dep org.jmockit:jmockit media/multipart
rm -r media/multipart/src/test/java/org/glassfish/jersey/media/multipart/internal/MultiPartHeaderModificationTest.java \
 media/multipart/src/test/java/org/glassfish/jersey/media/multipart/internal/FormDataMultiPartReaderWriterTest.java \
 media/multipart/src/test/java/org/glassfish/jersey/media/multipart/MultipartMixedWithApacheClientTest.java \
 media/multipart/src/test/java/org/glassfish/jersey/media/multipart/internal/MultiPartReaderWriterTest.java \
 media/multipart/src/test/java/org/glassfish/jersey/media/multipart/internal/FormDataMultiPartBufferTest.java

# Add OSGi manifest required by docker-client
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 connectors/apache-connector '
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

%mvn_package "org.glassfish.jersey.test-framework:project" test-framework
%mvn_package "org.glassfish.jersey.test-framework.providers:project" test-framework
%mvn_package ":%{name}-test-framework-core" test-framework 
%mvn_package ":%{name}-test-framework-provider-bundle" test-framework
%mvn_package ":%{name}-test-framework-provider-external" test-framework
%mvn_package ":%{name}-test-framework-provider-grizzly2" test-framework
%mvn_package ":%{name}-test-framework-provider-inmemory" test-framework
%if %{with jetty}
%mvn_package ":%{name}-test-framework-provider-jetty" test-framework
%endif
%mvn_package ":%{name}-test-framework-provider-jdk-http" test-framework
%mvn_package ":%{name}-test-framework-util" test-framework
# Conflict with org.glassfish.jersey:project
%mvn_file "org.glassfish.jersey.test-framework:project" %{name}/test-framework-project
%mvn_file "org.glassfish.jersey.test-framework.providers:project" %{name}/test-framework-providers-project
%mvn_file "org.glassfish.jersey.connectors:project" %{name}/connectors-project
%mvn_file "org.glassfish.jersey.containers:project" %{name}/containers-project
%mvn_file "org.glassfish.jersey.ext:project" %{name}/ext-project
%mvn_file "org.glassfish.jersey.ext.cdi:project" %{name}/ext-cdi-project
%mvn_file "org.glassfish.jersey.ext.rx:project" %{name}/ext-rx-project
%mvn_file "org.glassfish.jersey.incubator:project" %{name}/incubator-project
%mvn_file "org.glassfish.jersey.media:project" %{name}/media-project
%mvn_file "org.glassfish.jersey.security:project" %{name}/security-project

%build

%mvn_build -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE.html LICENSE.txt LICENSE-2.0.txt etc/config/copyright.txt

%files test-framework -f .mfiles-test-framework
%doc LICENSE.html LICENSE.txt etc/config/copyright.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.html LICENSE.txt LICENSE-2.0.txt etc/config/copyright.txt

%changelog
* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 2.18-alt1_3jpp8
- new version

