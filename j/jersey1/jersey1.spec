Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          jersey1
Version:       1.19
Release:       alt1_7jpp8
Summary:       JAX-RS (JSR 311) production quality Reference Implementation
# One file in jersey-core/ is under ASL 2.0 license
# License file with incorrect fsf address https://java.net/jira/browse/JERSEY-2870
License:       (CDDL or GPLv2 with exceptions) and ASL 2.0
URL:           http://jersey.java.net/
Source0:       https://github.com/jersey/jersey-1.x/archive/%{version}.tar.gz
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt
# remove org.aspectj aspectjrt
# remove testng classifier jdk15
# change javax.servlet servlet-api 2.5 with org.jboss.spec.javax.servlet jboss-servlet-api_3.0_spec
# change spring25-release-version [2.5.2,3) to 3
Patch0:        jersey-1.19-contribs-spring-pom.patch
# Fix for rhbz#1019234
Patch1:        jersey-1.19-remove-tools-scope-system.patch
Patch2:        jersey-1.18.3-grizzly23.patch
Patch3:        jersey-1.19-system-asm.patch
# Disable the EclipseLink MOXy support
Patch4:        jersey-1.19-disable-eclipselink-support.patch

BuildRequires: maven-local
BuildRequires: mvn(cglib:cglib)
BuildRequires: mvn(com.google.inject:guice)
BuildRequires: mvn(com.google.inject.extensions:extensions-parent:pom:)
BuildRequires: mvn(com.google.inject.extensions:guice-servlet)
BuildRequires: mvn(com.sun.xml.fastinfoset:FastInfoset)
BuildRequires: mvn(com.sun.istack:istack-commons-maven-plugin)
BuildRequires: mvn(com.sun:tools)
BuildRequires: mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(commons-httpclient:commons-httpclient)
# geronimo-annotation
BuildRequires: mvn(javax.annotation:jsr250-api)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(javax.mail:mail)
# geronimo-jpa
BuildRequires: mvn(javax.persistence:persistence-api)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(javax.ws.rs:jsr311-api)
BuildRequires: mvn(javax.xml.bind:jaxb-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.java:jvnet-parent:pom:)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-launcher)
BuildRequires: mvn(org.apache.ant:ant-testutil)
BuildRequires: mvn(org.apache.commons:commons-io)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-interceptor_3.0_spec)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jcdi_1.0_spec)
BuildRequires: mvn(org.apache.geronimo.specs:specs-parent:pom:)
BuildRequires: mvn(org.apache.tomcat:tomcat-jasper-el)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.surefire:surefire-testng)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(org.aspectj:aspectjweaver)
BuildRequires: mvn(org.codehaus.jackson:jackson-core-asl)
BuildRequires: mvn(org.codehaus.jackson:jackson-jaxrs)
BuildRequires: mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires: mvn(org.codehaus.jackson:jackson-xc)
BuildRequires: mvn(org.codehaus.jettison:jettison)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.freemarker:freemarker)
BuildRequires: mvn(org.glassfish.grizzly:grizzly-http)
BuildRequires: mvn(org.glassfish.grizzly:grizzly-http-server)
BuildRequires: mvn(org.jboss.spec.javax.el:jboss-el-api_2.2_spec)
BuildRequires: mvn(org.jboss.spec.javax.ejb:jboss-ejb-api_3.1_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet.jsp:jboss-jsp-api_2.2_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec)
BuildRequires: mvn(org.jvnet.jaxb2.maven2:maven-jaxb22-plugin)
BuildRequires: mvn(org.jvnet.mimepull:mimepull)
BuildRequires: mvn(org.hamcrest:hamcrest-all)
BuildRequires: mvn(org.osgi:org.osgi.core)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.springframework:spring-aop)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.springframework:spring-web)
BuildRequires: mvn(org.testng:testng)
BuildRequires: mvn(xerces:xercesImpl)

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

%package contribs
Group: Development/Java
Summary:       Contributions to Jersey

%description contribs
Projects that provide additional functionality to jersey,
like integration with other projects/frameworks.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jersey-1.x-%{version}
find . -name "*.jar" -print -delete
find . -name "*.class" -print -delete

%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
rm -rf jersey-server/src/main/java/jersey/repackaged
%patch4 -p1
rm -rf jersey-json/src/main/java/com/sun/jersey/json/impl/MoxyXmlStructure.java
%pom_remove_dep org.eclipse.persistence: jersey-json
rm jersey-json/src/test/java/com/sun/jersey/json/impl/ExceptionFromWriterTest.java \
 jersey-json/src/test/java/com/sun/jersey/json/impl/writer/DefaultXmlStreamWriterTest.java
%pom_disable_module jersey-moxy contribs
%pom_remove_dep org.eclipse.persistence:

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

# unavailable deps
%pom_disable_module archetypes
%pom_disable_module archive
%pom_disable_module experimental
%pom_disable_module glassfish
%pom_disable_module jersey-bundle
%pom_disable_module jersey-documentation
%pom_disable_module jersey-grizzly
%pom_disable_module jersey-tests
%pom_disable_module osgi
%pom_disable_module ri
%pom_disable_module samples
%pom_disable_module tests
%pom_disable_module jersey-test-framework-grizzly jersey-test-framework
%pom_disable_module jersey-test-framework-embedded-glassfish jersey-test-framework
%pom_disable_module bill-burke-book contribs
%pom_disable_module jersey-atom-abdera contribs
%pom_disable_module jersey-non-blocking-client contribs
%pom_disable_module oauth-tests contribs/jersey-oauth
%pom_disable_module scala contribs
%pom_disable_module jersey-simple-server contribs
%pom_disable_module maven-wadl-plugin contribs
# Conflicts with jdom and jdom2 packages
%pom_disable_module jersey-atom

%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :cobertura-maven-plugin jersey-json
%pom_remove_plugin :cobertura-maven-plugin samples

# unavailable test deps
%pom_remove_dep com.sun.net.httpserver:http jersey-client

%pom_remove_plugin :maven-surefire-plugin jersey-core
%pom_remove_plugin :maven-surefire-plugin jersey-server

# Prepare offline setting for generate java source code
cat > jersey-server/etc/bindings.cat << EOF
PUBLIC "-//W3C//DTD XMLSchema 200102//EN" "XMLSchema.dtd"
PUBLIC "XMLSchema.dtd" "XMLSchema.dtd"
SYSTEM "XMLSchema.dtd" "XMLSchema.dtd"

PUBLIC "datatypes" "datatypes.dtd"
SYSTEM "datatypes.dtd" "datatypes.dtd"

SYSTEM "xml.xsd" "xml.xsd"
EOF

rm -r jersey-server/etc/catalog.xml
sed -i 's|schemaLocation="http://www.w3.org/2001/xml.xsd"|schemaLocation="./xml.xsd"|' jersey-server/etc/wadl.xsd
# update plugin references
%pom_remove_plugin com.sun.tools.xjc.maven2: jersey-server
%pom_add_plugin "org.jvnet.jaxb2.maven2:maven-jaxb22-plugin:0.12.3" jersey-server '
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

# fix aId for new istack-commons maven plugin
for p in atom core bundle json; do
%pom_xpath_set "pom:plugin[pom:groupId = 'com.sun.istack' ]/pom:artifactId" istack-commons-maven-plugin jersey-${p}
done

%pom_change_dep org.osgi: :org.osgi.core jersey-client
%pom_change_dep org.osgi: :org.osgi.core jersey-server
%pom_change_dep org.osgi: :org.osgi.core jersey-servlet

%pom_change_dep :ant org.apache.ant: jersey-servlet

# Replace the weld-osgi-bundle dependency with the required JEE APIs
%pom_change_dep org.jboss.weld:weld-osgi-bundle org.apache.geronimo.specs:geronimo-jcdi_1.0_spec:1.0 jersey-servlet
%pom_add_dep javax.annotation:jsr250-api:1.0:provided jersey-servlet
%pom_add_dep org.apache.geronimo.specs:geronimo-interceptor_3.0_spec:1.0.1:provided jersey-servlet
%pom_add_dep javax.inject:javax.inject:1:provided jersey-servlet

%pom_change_dep org.glassfish:javax.ejb org.jboss.spec.javax.ejb:jboss-ejb-api_3.1_spec jersey-servlet
%pom_change_dep javax.servlet:javax.servlet-api org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec jersey-servlet
%pom_change_dep javax.servlet:jsp-api org.jboss.spec.javax.servlet.jsp:jboss-jsp-api_2.2_spec jersey-servlet
%pom_change_dep org.glassfish.web:el-impl org.apache.tomcat:tomcat-jasper-el jersey-server-linking
%pom_change_dep javax.servlet:servlet-api org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec contribs/jersey-guice

%pom_add_dep commons-codec:commons-codec::test contribs/jersey-apache-client
%pom_add_dep commons-codec:commons-codec::test contribs/jersey-multipart

# disable spring contribs tests. fails for various reasons
sed -i 's,<skip>${maven.test.skip}</skip>,<skip>true</skip>,' contribs/spring/pom.xml

# disable embedded jsr-311 copy
sed -i "s|<Export-Package>javax.ws.rs.*;-split-package:=merge-first,com.sun.jersey|<Export-Package>com.sun.jersey|" \
 jersey-core/pom.xml
sed -i "s|<Import-Package>!javax.ws.rs.*,javax.mail|<Import-Package>javax.ws.rs.*,javax.mail|" \
 jersey-core/pom.xml
#  contribs/jersey-moxy
for p in jersey-atom jersey-client jersey-core jersey-fastinfoset \
 jersey-grizzly2 jersey-grizzly2-servlet jersey-json jersey-server \
 jersey-servlet; do
%pom_xpath_set "pom:plugin[pom:artifactId = 'maven-bundle-plugin' ]/pom:configuration/pom:unpackBundle" false ${p}
done
#  contribs/jersey-moxy
for p in jersey-atom jersey-client jersey-fastinfoset jersey-json jersey-server ;do
%pom_add_dep javax.ws.rs:jsr311-api ${p}
done
for p in contribs/jersey-oauth/oauth-signature ;do
%pom_add_dep javax.ws.rs:jsr311-api::test ${p}
done

sed -i "s|<finalName>jersey-test-framework</finalName>||" \
jersey-test-framework/jersey-test-framework-core/pom.xml

# Cannot run program "svn"
%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin

%pom_xpath_remove "pom:profiles" contribs/wadl-resourcedoc-doclet
%pom_add_dep com.sun:tools contribs/wadl-resourcedoc-doclet
%pom_add_dep com.sun.jersey:jersey-server:'${project.version}' contribs/wadl-resourcedoc-doclet

%pom_change_dep javax.el:el-api org.jboss.spec.javax.el:jboss-el-api_2.2_spec jersey-server-linking

# these test fails ( NOTE grizzly use servlet 3.1 apis, instead, jersey use servlet 3.0.1 apis )
rm -r contribs/jersey-apache-client/src/test/java/com/sun/jersey/client/apache/impl \
 jersey-test-framework/jersey-test-framework-grizzly2/src/test/java/com/sun/jersey/test/framework/impl/container/grizzlyweb2 \
 contribs/jersey-guice/src/test/java/com/sun/jersey/guice

# these tests fail
rm -r jersey-json/src/test/java/com/sun/jersey/json/impl/NamespaceElementTest.java \
 jersey-json/src/test/java/com/sun/jersey/json/impl/NamespaceSupportIssue272Test.java \
 jersey-json/src/test/java/com/sun/jersey/json/impl/NamespaceAttributeTest.java

rm -r jersey-server/src/test/java/com/sun/jersey/server/impl/BuildIdTest.java

rm -r jersey-server-linking/src/test/java/com/sun/jersey/server/linking/el/LinkELContextTest.java
# java.lang.NoSuchMethodError: javax.el.ELContext.notifyBeforeEvaluation(Ljava/lang/String;)V
rm -r jersey-server-linking/src/test/java/com/sun/jersey/server/linking/impl/LinkProcessorTest.java \
 jersey-server-linking/src/test/java/com/sun/jersey/server/linking/impl/RefProcessorTest.java

# IllegalStateException: Unsupported cookie spec: default
rm -r contribs/jersey-apache-client4/src/test/java/com

rm -r jersey-core/src/test/java/com/sun/jersey/core/SecurityTest.java

%mvn_compat_version : %{version} 1

# Do not install source jars
#%%mvn_package ":::?*:" __noinstall
# Fix conflict with jersey-test-framework-core thanks to Mikolaj Izdebski
%mvn_file :jersey-test-framework %{name}/jersey-test-framework-pom
%mvn_file :jersey-test-framework-core %{name}/jersey-test-framework
%mvn_file :jersey-test-framework-core %{name}/jersey-test-framework-core
%mvn_package ":jersey-test-framework" test-framework
%mvn_package ":jersey-test-framework-core" test-framework 
%mvn_package ":jersey-test-framework-external" test-framework
%mvn_package ":jersey-test-framework-grizzly2" test-framework
%mvn_package ":jersey-test-framework-http" test-framework
%mvn_package ":jersey-test-framework-inmemory" test-framework
# contribs   jersey-simple-server
%mvn_package ":jersey-contribs" contribs
%mvn_package ":ant-wadl-task" contribs
%mvn_package ":jersey-apache-client" contribs
%mvn_package ":jersey-apache-client4" contribs
%mvn_package ":jersey-freemarker" contribs
%mvn_package ":jersey-guice" contribs
#%% mvn_package ":jersey-moxy" contribs
%mvn_package ":jersey-multipart" contribs
%mvn_package ":jersey-oauth" contribs
%mvn_package ":jersey-spring" contribs
%mvn_package ":jersey-wadl-json-schema" contribs
%mvn_package ":oauth-client" contribs
%mvn_package ":oauth-server" contribs
%mvn_package ":oauth-signature" contribs
%mvn_package ":wadl-resourcedoc-doclet" contribs

%build

%mvn_build

%install
%mvn_install

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "ant %{name}/jersey-server-%{version} jaxb-api" > ant-wadl-task
install -p -m 644 ant-wadl-task %{buildroot}%{_sysconfdir}/ant.d/ant-wadl-task

%files -f .mfiles
%doc dependencies.html getting-started.html 
%doc license.html legal/LICENSE.txt legal/maintenance/copyright.txt LICENSE-2.0.txt

%files test-framework -f .mfiles-test-framework
%doc license.html legal/LICENSE.txt legal/maintenance/copyright.txt

%files contribs -f .mfiles-contribs
%config(noreplace) %{_sysconfdir}/ant.d/ant-wadl-task
%doc license.html legal/LICENSE.txt legal/maintenance/copyright.txt

%files javadoc -f .mfiles-javadoc
%doc license.html legal/LICENSE.txt legal/maintenance/copyright.txt LICENSE-2.0.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1_7jpp8
- new fc release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1_6jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1_4jpp8
- new version

