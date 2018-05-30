Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
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
# %%name and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name cxf
%define version 3.1.6
%global tarname apache-%{name}-%{version}-src

%bcond_with jetty

Name:          cxf
Epoch:         1
Version:       3.1.6
Release:       alt2_7jpp8
Summary:       Apache CXF
License:       ASL 2.0
URL:           http://cxf.apache.org/
Source0:       http://www.apache.org/dist/cxf/%{version}/%{tarname}.tar.gz

Patch0:        cxf-3.1.4-port-to-servlet-3.1.patch
Patch1:        cxf-3.1.4-port-to-ehcache-core-2.6.patch
Patch2:        cxf-3.1.4-osgi-Dictionary.patch

Patch3:        cxf-3.1.6-CVE-2016-6812.patch
Patch4:        cxf-3.1.6-CVE-2016-8739.patch
Patch5:        cxf-3.1.6-CVE-2017-3156.patch

BuildRequires: maven-local
BuildRequires: mvn(antlr:antlr)
BuildRequires: mvn(cglib:cglib)
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(com.sun.mail:javax.mail)
BuildRequires: mvn(com.sun.xml.fastinfoset:FastInfoset)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(io.dropwizard.metrics:metrics-core)
BuildRequires: mvn(io.netty:netty-all)
BuildRequires: mvn(io.swagger:swagger-jaxrs) >= 1.5.8
BuildRequires: mvn(javax.annotation:javax.annotation-api)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(javax.validation:validation-api)
BuildRequires: mvn(javax.ws.rs:javax.ws.rs-api)
BuildRequires: mvn(jdom:jdom)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(net.java.dev.msv:msv-core)
BuildRequires: mvn(net.oauth.core:oauth-provider)
BuildRequires: mvn(net.sf.cglib:cglib)
# ehcache:2.9.0
BuildRequires: mvn(net.sf.ehcache:ehcache-core)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.aries.blueprint:blueprint-parser) >= 1.3.1
BuildRequires: mvn(org.apache.aries.blueprint:org.apache.aries.blueprint.api) >= 1.0.0
BuildRequires: mvn(org.apache.aries.blueprint:org.apache.aries.blueprint.core) >= 1.0.0
BuildRequires: mvn(org.apache.commons:commons-jexl)
BuildRequires: mvn(org.apache.cxf:cxf-xjc-plugin)
BuildRequires: mvn(org.apache.cxf.build-utils:cxf-buildtools)
BuildRequires: mvn(org.apache.cxf.build-utils:cxf-xml2fastinfoset-plugin)
BuildRequires: mvn(org.apache.cxf.xjcplugins:cxf-xjc-dv)
BuildRequires: mvn(org.apache.cxf.xjcplugins:cxf-xjc-javadoc)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jcache_1.0_spec)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jta_1.1_spec)
BuildRequires: mvn(org.apache.httpcomponents:httpcore-nio)
BuildRequires: mvn(org.apache.httpcomponents:httpasyncclient)
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.shared:maven-artifact-resolver)
BuildRequires: mvn(org.apache.mina:mina-core)
BuildRequires: mvn(org.apache.neethi:neethi)
BuildRequires: mvn(org.apache.velocity:velocity)
BuildRequires: mvn(org.apache.ws.xmlschema:xmlschema-core) >= 2.2.1
BuildRequires: mvn(org.apache.wss4j:wss4j-policy) >= 2.1.5
BuildRequires: mvn(org.apache.wss4j:wss4j-ws-security-common) >= 2.1.5
BuildRequires: mvn(org.apache.wss4j:wss4j-ws-security-dom) >= 2.1.5
BuildRequires: mvn(org.apache.wss4j:wss4j-ws-security-policy-stax) >= 2.1.5
BuildRequires: mvn(org.apache.wss4j:wss4j-ws-security-stax) >= 2.1.5
BuildRequires: mvn(org.apache.xmlbeans:xmlbeans)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires: mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires: mvn(org.eclipse.gemini.blueprint:gemini-blueprint-core)
BuildRequires: mvn(org.eclipse.gemini.blueprint:gemini-blueprint-io)
%if %{with jetty}
BuildRequires: mvn(org.eclipse.jetty:jetty-continuation)
BuildRequires: mvn(org.eclipse.jetty:jetty-http)
BuildRequires: mvn(org.eclipse.jetty:jetty-io)
BuildRequires: mvn(org.eclipse.jetty:jetty-jmx)
BuildRequires: mvn(org.eclipse.jetty:jetty-security)
BuildRequires: mvn(org.eclipse.jetty:jetty-server)
BuildRequires: mvn(org.eclipse.jetty:jetty-util)
%endif
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi.services)
BuildRequires: mvn(org.eclipse.tycho:tycho-packaging-plugin)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-core)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-runtime)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-xjc)
BuildRequires: mvn(org.glassfish.jaxb:txw2)
BuildRequires: mvn(org.jboss:jandex)
BuildRequires: mvn(org.jboss.jandex:jandex-maven-plugin)
BuildRequires: mvn(org.jboss.spec.javax.resource:jboss-connector-api_1.6_spec)
BuildRequires: mvn(org.jibx:jibx-bind)
BuildRequires: mvn(org.jibx:jibx-run)
BuildRequires: mvn(org.jibx:jibx-schema)
BuildRequires: mvn(org.jibx:jibx-tools)
BuildRequires: mvn(org.jvnet.jaxb2_commons:jaxb2-basics)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.sonatype.plexus:plexus-build-api)
# springframework:4.1.9.RELEASE https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=1363923
BuildRequires: mvn(org.springframework:spring-aop)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.springframework:spring-web)
BuildRequires: mvn(org.springframework:spring-webmvc)
BuildRequires: mvn(org.springframework.ldap:spring-ldap-core)
BuildRequires: mvn(rhino:js)
BuildRequires: mvn(wsdl4j:wsdl4j)
BuildRequires: mvn(xerces:xercesImpl)
BuildRequires: mvn(xml-resolver:xml-resolver)
BuildRequires: mvn(org.apache:apache-jar-resource-bundle)
# No more available
Obsoletes:     %{name}-api < %{version}-%{release}

BuildArch:     noarch
Source44: import.info

%description
Apache CXF is an open-source services framework that aids in
the development of services using front-end programming APIs,
like JAX-WS and JAX-RS.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package maven-plugins
Group: Development/Java
Summary:       Apache CXF Maven Plugins

%description maven-plugins
Maven plugins required for building or testing Apache CXF.

%package rt
Group: Development/Java
Summary:       Apache CXF Runtime

%description rt
This package contains core feature set of Apache CXF;
web service standards support, frontends, and protocols
support.

%package services
Group: Development/Java
Summary:       Apache CXF Services

%description services
This package contains Apache CXF WSN services.

%package tools
Group: Development/Java
Summary:       Apache CXF Tools

%description tools
Apache CXF Command Line Tools.

%prep
%setup -q -n %{tarname}
find . -name "*.jar" -print -delete
find . -name "*.class" -print -delete

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# viy: maven-javadoc-plugin 3
%pom_disable_module "java2wadl-plugin" maven-plugins

# Disable main modules
# No ant-trax
%pom_disable_module "testutils"
%pom_disable_module "integration"

%pom_disable_module "osgi"
%pom_disable_module "bundle" osgi
%pom_disable_module "itests" osgi
%pom_disable_module "itests-felix" osgi
%pom_disable_module "karaf" osgi

%pom_disable_module "systests"
# Test dependency
%pom_disable_module "systests" services/sts
%pom_disable_module "test" tools/wsdlto
%pom_disable_module "javascript-tests" rt/javascript

# Unnecessary
%pom_disable_module "sts-war" services/sts
%pom_disable_module "xkms-war" services/xkms
%pom_disable_module "archetypes" maven-plugins
%pom_disable_module "xkms-features" services/xkms
%pom_disable_module "xkms-osgi" services/xkms
%pom_disable_module "xkms-itests" services/xkms

# org.atmosphere:atmosphere-runtime:2.3.5
# com.ning:async-http-client:1.9.8 2014-05-05: Retired
%pom_disable_module "websocket" rt/transports

# org.apache.tuscany.sdo:tuscany-sdo-impl,tuscany-sdo-tools:1.1.1 2016/05/28 - Apache Tuscany has been retired. 
%pom_disable_module "sdo" rt/databinding

# org.apache.abdera:abdera-core,abdera-parser,abdera-extensions-json:1.1.3
%pom_disable_module "extensions/providers" rt/rs

# org.apache.geronimo.specs:geronimo-jpa_2.0_spec:1.0
# org.apache.olingo:olingo-odata2-core:1.2.0
# org.apache.hbase:hbase-client:1.1.1 2015-10-13: Retired
%pom_disable_module "extensions/search" rt/rs

# com.google.gwt:gwt-servlet,gwt-user:2.7.0,com.google.gwt.inject:gin:2.1.2,org.codehaus.mojo:gwt-maven-plugin:2.7.0
%pom_disable_module "management-web" rt

# org.apache.activemq:activemq-broker:5.12.0
# https://bugzilla.redhat.com/show_bug.cgi?id=998251
%pom_disable_module "wsn-core" services/wsn

%pom_disable_module "wsn-osgi" services/wsn

%if %{without jetty}
# Do not support jetty 9.4.0
%pom_disable_module "http-jetty" rt/transports
%endif

%pom_remove_plugin -r :maven-pmd-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
# com.googlecode.maven-download-plugin:download-maven-plugin:1.2.0 https://publicsuffix.org/list/effective_tld_names.dat
%pom_remove_plugin -r :download-maven-plugin

# used only for generate test stuff
%pom_remove_plugin -r org.codehaus.mojo:xmlbeans-maven-plugin

%pom_remove_dep -r :ant-nodeps

%pom_xpath_set pom:properties/pom:cxf.servlet-api.group javax.servlet parent
%pom_xpath_set pom:properties/pom:cxf.servlet-api.artifact javax.servlet-api parent
%pom_xpath_set pom:properties/pom:cxf.servlet-api-2.5.artifact javax.servlet-api parent

%pom_change_dep -r :geronimo-j2ee-connector_1.5_spec org.jboss.spec.javax.resource:jboss-connector-api_1.6_spec:1.0.1.Final
%pom_change_dep -r :geronimo-javamail_1.4_spec com.sun.mail:javax.mail:1.5.2

%pom_change_dep -r org.springframework.osgi:spring-osgi-io org.eclipse.gemini.blueprint:gemini-blueprint-io:1.0.2.RELEASE
%pom_change_dep -r org.springframework.osgi:spring-osgi-core org.eclipse.gemini.blueprint:gemini-blueprint-core:1.0.2.RELEASE
sed -i "s|org.springframework.osgi|org.eclipse.gemini.blueprint|" \
 core/src/main/java/org/apache/cxf/common/util/SpringOsgiUtil.java

# Remove deprecated httpclient annotations
sed -i '/ThreadSafe/d' \
 rt/transports/http-hc/src/main/java/org/apache/cxf/transport/http/asyncclient/SharedInputBuffer.java \
 rt/transports/http-hc/src/main/java/org/apache/cxf/transport/http/asyncclient/SharedOutputBuffer.java

%pom_change_dep -r :org.osgi.core  org.eclipse.osgi:org.eclipse.osgi:3.11.0.v20160714-1000
%pom_change_dep -r :org.osgi.compendium org.eclipse.osgi:org.eclipse.osgi.services:3.5.100.v20160714-1000

%pom_change_dep -r com.sun.xml.bind:jaxb-core org.glassfish.jaxb:jaxb-core:2.2.11
%pom_change_dep -r com.sun.xml.bind:jaxb-impl org.glassfish.jaxb:jaxb-runtime:2.2.11
%pom_change_dep -r com.sun.xml.bind:jaxb-xjc org.glassfish.jaxb:jaxb-xjc:2.2.11

%pom_change_dep -r :log4j :log4j:1.2.17
%pom_change_dep -r :cglib-nodep :cglib:3.1
%pom_change_dep -r javax.servlet:servlet-api :javax.servlet-api:3.1.0

%pom_change_dep io.netty:netty-codec-http io.netty:netty-all rt/transports/http-netty/netty-{client,server}

# NOTE: Maybe org.glassfish.jaxb:txw2 should be added as runtime deps in cxf-codegen-plugin pom file
for mod in rt/ws/policy tools/javato/ws services/wsn/wsn-api services/xkms/xkms-common ; do
# NoClassDefFoundError: com/sun/xml/txw2/output/XmlSerializer
%pom_xpath_inject "pom:plugin[pom:artifactId = 'cxf-codegen-plugin']" "
<dependencies>
  <dependency>
     <groupId>org.glassfish.jaxb</groupId>
     <artifactId>txw2</artifactId>
     <version>2.2.11</version>
  </dependency>
</dependencies>" ${mod}
done

%pom_xpath_inject "pom:plugin[pom:artifactId = 'cxf-codegen-plugin']/pom:dependencies" "
<dependency>
  <groupId>org.glassfish.jaxb</groupId>
  <artifactId>txw2</artifactId>
  <version>2.2.11</version>
</dependency>" services/ws-discovery/ws-discovery-api

# Disable old swagger support
%pom_remove_dep -r com.wordnik:swagger-jaxrs_2.10 rt/rs/description
rm rt/rs/description/src/main/java/org/apache/cxf/jaxrs/swagger/SwaggerFeature.java

%pom_change_dep -r :geronimo-servlet_2.5_spec javax.servlet:javax.servlet-api:3.1.0 rt/transports/http-netty/netty-server

%pom_change_dep -r :ehcache :ehcache-core:2.6.11

%pom_change_dep -r org.bouncycastle:bcprov-ext-jdk15on :bcprov-jdk15on rt/rs/security/jose-parent/jose

# Use hazelcast:1.9.4
%pom_remove_dep -r com.hazelcast:hazelcast
rm services/sts/sts-core/src/main/java/org/apache/cxf/sts/cache/HazelCast*.java

# Create Jandex index file(s)
# Required by WildFly
%pom_add_plugin "org.jboss.jandex:jandex-maven-plugin:1.0.4" rt/ws/security "
<executions>
  <execution>
    <id>make-index</id>
    <goals>
      <goal>jandex</goal>
    </goals>
  </execution>
</executions>"

%pom_add_plugin "org.apache.felix:maven-bundle-plugin:3.0.1" rt/ws/security '
<configuration>
  <instructions>
    <Bundle-DocURL>http://cxf.apache.org</Bundle-DocURL>
    <Bundle-SymbolicName>${cxf.osgi.symbolic.name}</Bundle-SymbolicName>
    <Fragment-Host>${cxf.fragment.host}</Fragment-Host>
    <Implementation-Vendor>The Apache Software Foundation</Implementation-Vendor>
    <Implementation-Vendor-Id>org.apache</Implementation-Vendor-Id>
    <Implementation-Version>${cxf.osgi.version.clean}</Implementation-Version>
    <Specification-Vendor>The Apache Software Foundation</Specification-Vendor>
    <Specification-Version>${cxf.osgi.version.clean}</Specification-Version>
    <Import-Package>
        ${cxf.osgi.import},
        *
    </Import-Package>
    <Include-Resource>
        {maven-resources},
        /META-INF/jandex.idx=${project.build.outputDirectory}/META-INF/jandex.idx
    </Include-Resource>
  </instructions>
</configuration>'

%pom_xpath_remove "pom:dependency[pom:artifactId = 'tools']/pom:scope" maven-plugins/java2wadl-plugin
%pom_xpath_remove "pom:dependency[pom:artifactId = 'tools']/pom:systemPath" maven-plugins/java2wadl-plugin

%mvn_package ":cxf-tools*" tools
%mvn_package ":cxf-rt*" rt
%mvn_package ":cxf-maven-plugins*" maven-plugins
%mvn_package ":cxf-services*" services

%build

%mvn_build -f -j

# Create Jandex index file(s)
# Required by WildFly
java -cp $(build-classpath jandex) org.jboss.jandex.Main -j rt/security/target/cxf-rt-security-%{version}.jar
java -cp $(build-classpath jandex) org.jboss.jandex.Main -j rt/ws/security/target/cxf-rt-ws-security-%{version}.jar

%install
%mvn_install

install -pm 644 rt/security/target/cxf-rt-security-%{version}-jandex.jar %{buildroot}%{_javadir}/%{name}/cxf-rt-security-jandex.jar
install -pm 644 rt/ws/security/target/cxf-rt-ws-security-%{version}-jandex.jar %{buildroot}%{_javadir}/%{name}/cxf-rt-ws-security-jandex.jar

%files -f .mfiles
%doc README
%doc LICENSE NOTICE

%files tools -f .mfiles-tools
%doc LICENSE NOTICE

%files rt -f .mfiles-rt
%{_javadir}/%{name}/cxf-rt-security-jandex.jar
%{_javadir}/%{name}/cxf-rt-ws-security-jandex.jar
%doc LICENSE NOTICE

%files services -f .mfiles-services
%doc LICENSE NOTICE

%files maven-plugins -f .mfiles-maven-plugins
%doc LICENSE NOTICE

#%files javadoc -f .mfiles-javadoc
#%doc LICENSE NOTICE

%changelog
* Wed May 30 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.1.6-alt2_7jpp8
- fixed build with maven-javadoc-plugin 3

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.1.6-alt1_7jpp8
- fc27 update

* Fri Nov 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.1.6-alt1_5jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.7.11-alt1_4jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.7.11-alt1_3jpp8
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.6.9-alt2_1jpp7
- fixed build

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.6.9-alt1_1jpp7
- update

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.9-alt1_2jpp7
- new version

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.8-alt1_5jpp7
- new version

