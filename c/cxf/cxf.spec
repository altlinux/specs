Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name cxf
%define version 2.7.11
# vim: set ts=4 sw=4 sts=4 et:
%global tarname apache-%{name}-%{version}-src

Name:          cxf
Epoch:         1
Version:       2.7.11
Release:       alt1_4jpp8
Summary:       Apache CXF
License:       ASL 2.0
URL:           http://cxf.apache.org/

Source0:       http://archive.apache.org/dist/%{name}/%{version}/%{tarname}.tar.gz

Patch0:        0001-JDK-8-support.patch

# Add missing method available in apache-mina 2.0.9
Patch1:        cxf-2.7.11-mina-core2.0.9-support.patch


BuildArch:     noarch

BuildRequires: jandex
BuildRequires: jra
BuildRequires: maven-local
BuildRequires: mvn(asm:asm)
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires: mvn(com.sun.xml.bind:jaxb-xjc)
BuildRequires: mvn(com.sun.xml.fastinfoset:FastInfoset)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(javax.mail:mail)
BuildRequires: mvn(jdom:jdom)
BuildRequires: mvn(log4j:log4j:12)
BuildRequires: mvn(net.sf.cglib:cglib)
BuildRequires: mvn(net.sf.ehcache:ehcache-core)
BuildRequires: mvn(net.shibboleth:parent:pom:)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.aries.blueprint:org.apache.aries.blueprint.core)
BuildRequires: mvn(org.apache.cxf:cxf-xjc-plugin) >= 2.6.2
BuildRequires: mvn(org.apache.cxf.build-utils:cxf-xml2fastinfoset-plugin) >= 2.6.0
BuildRequires: mvn(org.apache.cxf.xjcplugins:cxf-xjc-dv)
BuildRequires: mvn(org.apache.cxf.xjcplugins:cxf-xjc-pl)
BuildRequires: mvn(org.apache.cxf.xjcplugins:cxf-xjc-wsdlextension)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-project)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.shared:maven-artifact-resolver)
BuildRequires: mvn(org.apache.maven.wagon:wagon-ssh)
BuildRequires: mvn(org.apache.mina:mina-core)
BuildRequires: mvn(org.apache.neethi:neethi)
BuildRequires: mvn(org.apache.velocity:velocity)
BuildRequires: mvn(org.apache.ws.security:wss4j) >= 1.6.10
BuildRequires: mvn(org.apache.ws.xmlschema:xmlschema-core)
BuildRequires: mvn(org.apache.xmlbeans:xmlbeans)
BuildRequires: mvn(org.apache.xmlgraphics:batik-ext)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk16)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires: mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires: mvn(org.eclipse.tycho:tycho-packaging-plugin)
BuildRequires: mvn(org.jboss.spec.javax.resource:jboss-connector-api_1.6_spec) >= 1.0.1
BuildRequires: mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec)
BuildRequires: mvn(org.jboss.spec.javax.xml.ws:jboss-jaxws-api_2.2_spec)
BuildRequires: mvn(org.jibx:jibx-bind)
BuildRequires: mvn(org.jibx:jibx-run)
BuildRequires: mvn(org.jibx:jibx-schema)
BuildRequires: mvn(org.jibx:jibx-tools)
BuildRequires: mvn(org.opensaml:opensaml)
BuildRequires: mvn(org.osgi:org.osgi.compendium)
BuildRequires: mvn(org.osgi:org.osgi.core)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.sonatype.plexus:plexus-build-api)
BuildRequires: mvn(org.springframework:spring-aop)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-core) >= 3.1.1
BuildRequires: mvn(org.springframework:spring-jms)
BuildRequires: mvn(org.springframework:spring-tx)
BuildRequires: mvn(org.springframework:spring-web)
BuildRequires: mvn(org.springframework:spring-webmvc)
BuildRequires: mvn(rhino:js)
BuildRequires: mvn(wsdl4j:wsdl4j)
BuildRequires: mvn(xml-resolver:xml-resolver)
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

%package api
Group: Development/Java
Summary:       Apache CXF API

%description api
Apache CXF API classes.

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

find . -name "*.jar" -delete
find . -name "*.class" -delete

%patch0 -p1
%patch1 -p1

iconv -f macintosh -t utf8 < licenses/cdd1-1.0.txt > cdd.txt
mv -f cdd.txt licenses/cdd1-1.0.txt

# Replace cglib-nodep with cglib
find . -name "pom.xml" -print | xargs sed -i "s|>cglib<|>net.sf.cglib<|"
find . -name "pom.xml" -print | xargs sed -i "s|cglib-nodep|cglib|"

# Replace bcprov-jdk15 with bcprov-jdk16
find . -name "pom.xml" -print | xargs sed -i "s|bcprov-jdk15|bcprov-jdk16|;s|bcprov-jdk16on|bcprov-jdk16|"

# Not necessary for javadoc generation
%pom_remove_plugin "org.apache.maven.plugins:maven-dependency-plugin" distribution/pom.xml

sed -i "s|<cxf.servlet-api.group>org.apache.geronimo.specs</cxf.servlet-api.group>|<cxf.servlet-api.group>org.jboss.spec.javax.servlet</cxf.servlet-api.group>|" parent/pom.xml
sed -i "s|<cxf.servlet-api.artifact>geronimo-servlet_3.0_spec</cxf.servlet-api.artifact>|<cxf.servlet-api.artifact>jboss-servlet-api_3.0_spec</cxf.servlet-api.artifact>|" parent/pom.xml

# Replace selected Geronimo APIs with other implementations
while read gid aid newgid newaid version
do

for f in $(grep "<artifactId>${aid}</artifactId>" --include "pom.xml" --exclude-dir "*samples*" -r | awk -F: '{ print $1 }' | uniq)
do

%pom_remove_dep "${gid}:${aid}" ${f}
%pom_xpath_inject "pom:dependencies" "<dependency><groupId>${newgid}</groupId><artifactId>${newaid}</artifactId></dependency>" ${f}

done


# Make sure we add the version requirements for just added APIs in parent pom.xml
%pom_xpath_inject "pom:dependencyManagement/pom:dependencies/pom:dependency[pom:artifactId='${newaid}']" "<version>${version}</version>" parent/pom.xml

done <<EOF
org.apache.geronimo.specs geronimo-j2ee-connector_1.5_spec org.jboss.spec.javax.resource jboss-connector-api_1.6_spec 1.0.1.Final
org.apache.geronimo.specs geronimo-jaxws_2.2_spec org.jboss.spec.javax.xml.ws jboss-jaxws-api_2.2_spec 2.0.2.Final
org.apache.geronimo.specs geronimo-javamail_1.4_spec javax.mail mail 1.4.3
EOF

# Disable main modules
# No ant-trax
%pom_disable_module "testutils"
%pom_disable_module "integration"
%pom_disable_module "osgi/karaf"
%pom_disable_module "osgi/bundle"
%pom_disable_module "systests"

# Disable common submodules
%pom_disable_module wstx-msv-validation common/pom.xml
%pom_disable_module xerces-xsd-validation common/pom.xml

# Disable Maven plugins submodules
# Requires jsr-339, jaxrs 2.0
%pom_disable_module "java2wadl-plugin" maven-plugins/pom.xml
%pom_disable_module "wadl2java-plugin" maven-plugins/pom.xml
%pom_disable_module "wsdl-validator-plugin" maven-plugins/pom.xml
%pom_disable_module "corba" maven-plugins/pom.xml
%pom_disable_module "archetypes" maven-plugins/pom.xml

# Disable rt submodules
%pom_disable_module "corba" rt/bindings/pom.xml
%pom_disable_module "databinding/xmlbeans" rt/pom.xml
%pom_disable_module "databinding/sdo" rt/pom.xml

# Requires jsr-339, jaxrs 2.0
%pom_disable_module "frontend/jaxrs" rt/pom.xml
%pom_disable_module "transports/http-jetty" rt/pom.xml
%pom_disable_module "management-web" rt/pom.xml
%pom_disable_module "rs/extensions/providers" rt/pom.xml
%pom_disable_module "rs/extensions/search" rt/pom.xml

%pom_disable_module "rs/security/xml" rt/pom.xml
%pom_disable_module "rs/security/sso/saml" rt/pom.xml
%pom_disable_module "rs/security/oauth-parent" rt/pom.xml
%pom_disable_module "rs/security/cors" rt/pom.xml

%pom_disable_module xkms-itests services/xkms/pom.xml
%pom_disable_module xkms-features services/xkms/pom.xml
%pom_disable_module xkms-war services/xkms/pom.xml

# The repository system is offline but the artifact org.apache.httpcomponents:httpasyncclient:jar:4.0-beta3 is not available in the local repository
%pom_disable_module "transports/http-hc" rt/pom.xml

%pom_disable_module "javascript-tests" rt/javascript/pom.xml

%pom_disable_module wsn-core services/wsn/pom.xml
%pom_disable_module wsn-osgi services/wsn/pom.xml

%pom_remove_dep "com.wordnik:swagger-jaxrs_2.10" rt/frontend/jaxrs/pom.xml

# Disable tools submodules
# Requires frontend/jaxrs
%pom_disable_module "wadlto" tools/pom.xml
%pom_disable_module "corba" tools/pom.xml
# Requires jsr-339, jaxrs 2.0
#%pom_disable_module "frontend/javascript" tools/wsdlto/pom.xml
%pom_disable_module "test" tools/wsdlto/pom.xml
%pom_disable_module "misc" tools/wsdlto/pom.xml

# Test dependency
%pom_disable_module "systests" services/sts/pom.xml
# Unnecessary
%pom_disable_module "sts-war" services/sts/pom.xml

# No spring-ldap-core
%pom_remove_dep "org.springframework.ldap:spring-ldap-core" services/sts/sts-core/pom.xml
%pom_remove_dep "org.springframework.ldap:spring-ldap-core" services/sts/sts-war/pom.xml
rm -rf services/sts/sts-core/src/main/java/org/apache/cxf/sts/claims/Ldap*

# No hazelcast
%pom_remove_dep "com.hazelcast:hazelcast" services/sts/sts-core/pom.xml
%pom_remove_dep "com.hazelcast:hazelcast" services/sts/sts-war/pom.xml
rm -rf services/sts/sts-core/src/main/java/org/apache/cxf/sts/cache/HazelCast*

%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'log4j']/pom:version" 12 services/sts/sts-core/pom.xml

sed -i "s|@Override||" services/sts/sts-core/src/main/java/org/apache/cxf/sts/event/LoggerPatternLayoutLog4J.java

# Disable checkstyle plugin
%pom_remove_plugin "org.apache.maven.plugins:maven-checkstyle-plugin" parent/pom.xml

# Disable pmd plugin
%pom_remove_plugin "org.apache.maven.plugins:maven-pmd-plugin" parent/pom.xml

# Workaround for Woodstox 4.1 (4.2 is required, remove after upgrade)
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'cxf-codegen-plugin']/pom:executions/pom:execution/pom:configuration/pom:fork" rt/ws/policy/pom.xml
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'cxf-codegen-plugin']/pom:executions/pom:execution/pom:configuration/pom:fork" tools/javato/ws/pom.xml

# Disable remote-resources-plugin
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-remote-resources-plugin']" parent/pom.xml

# Remove testutils
%pom_remove_dep "org.apache.cxf:cxf-testutils" rt/bindings/xml/pom.xml
%pom_remove_dep "org.apache.cxf:cxf-testutils" rt/frontend/simple/pom.xml
%pom_remove_dep "org.apache.cxf:cxf-testutils" rt/frontend/jaxws/pom.xml
%pom_remove_dep "org.apache.cxf:cxf-testutils" rt/databinding/aegis/pom.xml
%pom_remove_dep "org.apache.cxf:cxf-testutils" rt/databinding/jibx/pom.xml
%pom_remove_dep "org.apache.cxf:cxf-testutils" rt/bindings/object/pom.xml
%pom_remove_dep "org.apache.cxf:cxf-testutils" rt/bindings/coloc/pom.xml
%pom_remove_dep "org.apache.cxf:cxf-testutils" rt/management/pom.xml
%pom_remove_dep "org.apache.cxf:cxf-testutils" tools/javato/ws/pom.xml
%pom_remove_dep "org.apache.cxf:cxf-testutils" rt/transports/jms/pom.xml
%pom_remove_dep "org.apache.cxf:cxf-testutils" rt/ws/rm/pom.xml

# Remove jms transport test deps
%pom_remove_dep "org.apache.geronimo.specs:geronimo-j2ee-management_1.1_spec" rt/transports/jms/pom.xml
%pom_remove_dep "org.apache.xbean:xbean-spring" rt/transports/jms/pom.xml

# Remove aegis test deps
%pom_remove_dep "org.apache.cxf:cxf-wstx-msv-validation" rt/databinding/aegis/pom.xml

# Remove transports-http-jetty test dep
%pom_remove_dep "org.apache.cxf:cxf-rt-transports-http-jetty" tools/javato/ws/pom.xml
%pom_remove_dep "org.apache.cxf:cxf-rt-transports-http-jetty" rt/databinding/aegis/pom.xml
%pom_remove_dep "org.apache.cxf:cxf-rt-transports-http-jetty" rt/bindings/object/pom.xml
%pom_remove_dep "org.apache.cxf:cxf-rt-transports-http-jetty" rt/frontend/jaxrs/pom.xml

# Remove sprint-test dep
%pom_remove_dep "org.springframework:spring-test" rt/ws/policy/pom.xml

# Disable xsdvalidation
%pom_remove_dep "org.apache.cxf:cxf-xerces-xsd-validation" rt/frontend/simple/pom.xml

# Fix java.lang.NoClassDefFoundError: org/w3c/dom/ElementTraversal
%pom_xpath_inject "pom:dependencies" "<dependency><groupId>org.apache.xmlgraphics</groupId><artifactId>batik-ext</artifactId><version>1.8</version><scope>runtime</scope></dependency>" tools/common/pom.xml

# Fix javadoc doclint
%pom_remove_plugin -r :maven-javadoc-plugin
# Removed unused artifact
%pom_remove_dep -r org.apache.ant:ant-nodeps
# Use activemq >= 5.8.0 (activemq-core was splitted in several sub modules)
%pom_remove_dep -r org.apache.activemq:

%mvn_package ":cxf-tools*" tools
%mvn_package ":cxf-rt*" rt
%mvn_package ":cxf-maven-plugins*" maven-plugins
%mvn_package ":cxf-api*" api
%mvn_package ":cxf-services*" services

%build
%mvn_build -f

# Create Jandex index file(s)
# Required by WildFly
java -cp $(build-classpath jandex) org.jboss.jandex.Main -j rt/ws/security/target/cxf-rt-ws-security-%{version}.jar

%install
%mvn_install

install -pm 644 rt/ws/security/target/cxf-rt-ws-security-%{version}-jandex.jar %{buildroot}%{_javadir}/%{name}/cxf-rt-ws-security-jandex.jar

%files -f .mfiles
%doc README
%doc LICENSE NOTICE

%files tools -f .mfiles-tools
%doc LICENSE NOTICE

%files api -f .mfiles-api
%doc LICENSE NOTICE

%files rt -f .mfiles-rt
%{_javadir}/%{name}/cxf-rt-ws-security-jandex.jar
%doc LICENSE NOTICE

%files services -f .mfiles-services
%doc LICENSE NOTICE

%files maven-plugins -f .mfiles-maven-plugins
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
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

