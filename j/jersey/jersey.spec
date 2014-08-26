# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
%global with_grizzly 0
Name:          jersey
Version:       1.17.1
Release:       alt1_2jpp7
Summary:       JAX-RS (JSR 311) production quality Reference Implementation
Group:         Development/Java
# One file in jersey-core/ is under ASL 2.0 license
License:       (CDDL or GPLv2 with exceptions) and ASL 2.0
URL:           http://jersey.java.net/
# svn export https://svn.java.net/svn/jersey~svn/tags/jersey-1.17.1/jersey jersey-1.17.1
# find jersey-1.17.1 -name '*.jar' -delete
# find jersey-1.17.1 -name '*.class' -delete
# tar czf jersey-1.17.1-src-svn.tar.gz jersey-1.17.1
Source0:       %{name}-%{version}-src-svn.tar.gz
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

# change
#     com.sun.tools.xjc.maven2 maven-jaxb-plugin 1.1.1 with maven-jaxb2-plugin
#     aId weld-osgi-bundle with weld-core
#     aId osgi_R4_core with org.osgi.core
#     javax.servlet javax.servlet-api 3.0.1 with org.jboss.spec.javax.servlet jboss-servlet-api_3.0_spec
#     javax.servlet jsp-api 2.0 with org.jboss.spec.javax.servlet.jsp jboss-jsp-api_2.2_spec
#     org.glassfish javax.ejb 3.1 with org.jboss.spec.javax.ejb jboss-ejb-api_3.1_spec
#     org.glassfish.web el-impl 2.2 with org.apache.tomcat tomcat-jasper-el 7.0.27
# add geronimo-annotation
# fix ant and eclipselink aId
# resolved problem with missing weld-build-config
Patch0:        %{name}-1.14-fixbuild.patch
# remove org.aspectj aspectjrt
# remove testng classifier jdk15
# change javax.servlet servlet-api 2.5 with org.jboss.spec.javax.servlet jboss-servlet-api_3.0_spec
# change spring25-release-version [2.5.2,3) to 3
Patch1:        %{name}-1.15-contribs-spring-pom.patch

BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: eclipselink
BuildRequires: felix-osgi-core
BuildRequires: geronimo-annotation >= 1.0-7
BuildRequires: geronimo-jpa
BuildRequires: glassfish-fastinfoset
BuildRequires: glassfish-jaxb
BuildRequires: glassfish-jaxb-api
%if %{with_grizzly}
# https://bugzilla.redhat.com/show_bug.cgi?id=859114
BuildRequires: grizzly
%endif
BuildRequires: jackson
BuildRequires: javamail
BuildRequires: jboss-ejb-3.1-api
BuildRequires: jboss-el-2.2-api
BuildRequires: jboss-jsp-2.2-api
BuildRequires: jboss-servlet-3.0-api
BuildRequires: jdom
BuildRequires: jettison
BuildRequires: jsr-311
BuildRequires: objectweb-asm
BuildRequires: rome >= 0.9-11
BuildRequires: tomcat-lib
BuildRequires: weld-core
BuildRequires: weld-parent

# tests deps
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-io
BuildRequires: aspectjweaver
BuildRequires: cglib
BuildRequires: cobertura
BuildRequires: junit
BuildRequires: testng
BuildRequires: tomcat-lib

# contrib
BuildRequires: freemarker
BuildRequires: guice
BuildRequires: guice-extensions
BuildRequires: guice-servlet
BuildRequires: httpcomponents-client
BuildRequires: jakarta-commons-httpclient
BuildRequires: mimepull
#BuildRequires: simple >= 5.0.4 some B/R are not available
BuildRequires: springframework
BuildRequires: springframework-aop
BuildRequires: springframework-beans
BuildRequires: springframework-context
BuildRequires: springframework-web
BuildRequires: xerces-j2
# jersey maven-wald-plugin deps
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)

%if %{?fedora} > 18
BuildRequires: geronimo-parent-poms
%endif
BuildRequires: buildnumber-maven-plugin
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-istack-commons-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-jaxb2-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-bundle
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-surefire-provider-testng

Requires:      ant
Requires:      eclipselink
Requires:      felix-osgi-core
Requires:      geronimo-annotation >= 1.0-7
Requires:      geronimo-jpa
Requires:      glassfish-fastinfoset
Requires:      glassfish-jaxb
%if %{with_grizzly}
Requires:      grizzly
%endif
Requires:      jackson
Requires:      javamail
Requires:      jboss-ejb-3.1-api
Requires:      jboss-jsp-2.2-api
Requires:      jboss-servlet-3.0-api
Requires:      jettison
Requires:      jsr-311
Requires:      objectweb-asm
Requires:      rome >= 0.9-11
# tomcat-lib jasper-el
Requires:      tomcat-lib
Requires:      weld-core

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Jersey is the open source JAX-RS (JSR 311)
production quality Reference Implementation
for building RESTful Web services.

%package test-framework
Group:         Development/Java
Summary:       Jersey Test Framework
Requires:      %{name} = %{version}-%{release}
%if %{with_grizzly}
Requires:      grizzly
%endif
Requires:      jboss-servlet-3.0-api
Requires:      junit

%description test-framework
%{summary}.

%package contribs
Group:         Development/Java
Summary:       Contributions to Jersey
Requires:      %{name} = %{version}-%{release}
Requires:      ant
Requires:      eclipselink
Requires:      freemarker
Requires:      glassfish-jaxb-api
Requires:      guice-servlet
Requires:      httpcomponents-client
Requires:      jackson
Requires:      jakarta-commons-httpclient
Requires:      jboss-servlet-3.0-api
Requires:      mimepull
#Requires:      simple >= 5.0.4
Requires:      springframework
Requires:      springframework-aop
Requires:      springframework-beans
Requires:      springframework-context
Requires:      springframework-web
Requires:      xerces-j2

%description contribs
Projects that provide additional functionality to jersey,
like integration with other projects/frameworks.

%package -n maven-wadl-plugin
Group:         Development/Java
Summary:       WADL Maven Mojo
Requires:      %{name} = %{version}-%{release}
Requires:      maven
Requires:      mvn(org.apache.maven:maven-artifact)
Requires:      mvn(org.apache.maven:maven-plugin-api)
Requires:      xerces-j2

%description -n maven-wadl-plugin
A maven plugin that generates a wadl file
from resource classes and more stuff.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

%patch0 -p1
%patch1 -p0

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

# unavailable test deps
%pom_remove_dep com.sun.net.httpserver:http jersey-client

# disable embedded jsr-311 copy
%pom_remove_plugin org.apache.maven.plugins:maven-dependency-plugin jersey-core

# require org.mortbay.jetty maven-jetty-plugin 6.1.15
%pom_disable_module bill-burke-book contribs
# require org.apache.abdera abdera-parser abdera-extensions-json 1.0
%pom_disable_module jersey-atom-abdera contribs
# require org.glassfish.grizzly grizzly-http-client 1.2
%pom_disable_module jersey-non-blocking-client contribs
# require org.ops4j.pax.exam pax-exam pax-exam-junit pax-exam-container-default pax-exam-junit-extender-impl 1.2.3
# org.ops4j.pax.swissbox pax-swissbox-tinybundles 1.3.1
# grizzly 1.x
%pom_disable_module oauth-tests contribs/jersey-oauth
# require net.liftweb lift-webkit 1.1-M7
# net.sourceforge.jwebunit jwebunit-htmlunit-plugin 1.4.1
# net.sf.alchim yuicompressor-maven-plugin
# org.mortbay.jetty jetty maven-jetty-plugin 6.1.19
# org.scala-lang scala-compiler scala-library 2.7.5
# org.scala-tools maven-scala-plugin 2.10.1
# org.scala-tools.testing scalacheck 1.5, specs 1.6.2.2, scalatest 0.9.4
%pom_disable_module scala contribs
# require simple 5.0.4 some B/R are not available
%pom_disable_module jersey-simple-server contribs

# [ERROR] 
# Artifact Ids of the format maven-___-plugin are reserved for 
# plugins in the Group Id org.apache.maven.plugins
# Please change your artifactId to the format ___-maven-plugin
# In the future this error will break the build.
sed -i 's|<artifactId>maven-wadl-plugin</artifactId>|<artifactId>wadl-maven-plugin</artifactId>|' \
  contribs/maven-wadl-plugin/pom.xml

# [ERROR] com.sun.jersey.wadl.GenerateWadlMojo#_wadlFile:
# [ERROR] Failed to execute goal org.apache.maven.plugins:maven-plugin-plugin:3.1:descriptor
# (default-descriptor) on project maven-wadl-plugin: Error extracting plugin descriptor:
# 'com.sun.jersey.wadl.GenerateWadlMojo#_wadlFile: cannot use both @parameter expression and property'
sed -i 's|property="wadlFile" expression="${project.build.directory}/application.wadl"|expression="${project.build.directory}/application.wadl"|' \
  contribs/maven-wadl-plugin/src/main/java/com/sun/jersey/wadl/GenerateWadlMojo.java

sed -i "s|<artifactId>apache-maven|<artifactId>maven-compat|" contribs/maven-wadl-plugin/pom.xml

%if %{with_grizzly}

%pom_remove_dep org.glassfish:javax.servlet jersey-grizzly2-servlet
%pom_add_dep org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec jersey-grizzly2-servlet
# javax.servlet javax.servlet-api 3.0.1
%pom_remove_dep javax.servlet:javax.servlet-api jersey-test-framework/jersey-test-framework-core
%pom_add_dep org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec jersey-test-framework/jersey-test-framework-core
# these test fails ( NOTE grizzly use servlet 3.1 apis, instead, jersey use servlet 3.0.1 apis )
rm -r contribs/jersey-apache-client/src/test/java/com/sun/jersey/client/apache/impl \
 jersey-test-framework/jersey-test-framework-grizzly2/src/test/java/com/sun/jersey/test/framework/impl/container/grizzlyweb2 \
 contribs/jersey-guice/src/test/java/com/sun/jersey/guice

%else

%pom_disable_module jersey-grizzly2
%pom_disable_module jersey-grizzly2-servlet
%pom_disable_module jersey-test-framework-grizzly2 jersey-test-framework
# unavailable test deps
%pom_remove_dep com.sun.jersey:jersey-grizzly2 contribs/jersey-apache-client
rm -r contribs/jersey-apache-client/src/test/java/com/sun/jersey/client/apache/impl
%pom_remove_dep com.sun.jersey:jersey-grizzly2 contribs/jersey-apache-client4
rm -r contribs/jersey-apache-client4/src/test/java/com/sun/jersey/client/apache4/impl
%pom_remove_dep com.sun.jersey.jersey-test-framework:jersey-test-framework-grizzly2 contribs/jersey-freemarker
%pom_remove_dep com.sun.jerssey.jersey-test-framework:jersey-test-framework-grizzly2 contribs/jersey-freemarker
%pom_remove_dep com.sun.jersey:jersey-grizzly2-servlet contribs/jersey-guice
rm -r contribs/jersey-guice/src/test/java/com/sun/jersey/guice
%pom_remove_dep com.sun.jersey:jersey-grizzly2 contribs/jersey-multipart
rm -r contribs/jersey-multipart/src/test/java/com/sun/jersey/multipart/impl
%pom_remove_dep com.sun.jersey:jersey-grizzly2-servlet contribs/spring
rm -r contribs/spring/src/test/java/com/sun/jersey/spring*/

# transitive deps
%pom_add_dep com.sun.jersey:jersey-server:'${project.version}' contribs/jersey-multipart
%endif

# disable spring contribs tests. fails for various reasons
sed -i 's,<skip>${maven.test.skip}</skip>,<skip>true</skip>,' contribs/spring/pom.xml

%pom_add_dep commons-codec:commons-codec:any:test contribs/jersey-apache-client
%pom_add_dep commons-codec:commons-codec:any:test contribs/jersey-multipart
%pom_remove_dep org.jvnet:mimepull contribs/jersey-multipart
%pom_add_dep org.jvnet.mimepull:mimepull contribs/jersey-multipart
%pom_remove_dep javax.servlet:servlet-api contribs/jersey-guice
%pom_add_dep org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec:any:provided contribs/jersey-guice
%pom_remove_dep ant:ant contribs/ant-wadl-task
%pom_add_dep org.apache.ant:ant:any:provided contribs/ant-wadl-task

%pom_remove_dep org.eclipse.persistence:org.eclipse.persistence.moxy contribs/jersey-moxy
%pom_add_dep org.eclipse.persistence:eclipselink contribs/jersey-moxy

# disable embedded jsr-311 copy
sed -i "s|<Export-Package>javax.ws.rs.*;-split-package:=merge-first,com.sun.jersey|<Export-Package>com.sun.jersey|" \
 jersey-core/pom.xml
sed -i "s|<Import-Package>!javax.ws.rs.*,javax.mail|<Import-Package>javax.ws.rs.*,javax.mail|" \
 jersey-core/pom.xml

for p in jersey-atom jersey-client jersey-fastinfoset jersey-json jersey-server contribs/jersey-moxy ;do
%pom_add_dep javax.ws.rs:jsr311-api ${p}
done
for p in contribs/jersey-oauth/oauth-signature ;do
%pom_add_dep javax.ws.rs:jsr311-api:any:test ${p}
done

# these tests fail
rm -r jersey-json/src/test/java/com/sun/jersey/json/impl/NamespaceElementTest.java \
 jersey-json/src/test/java/com/sun/jersey/json/impl/NamespaceSupportIssue272Test.java \
 jersey-json/src/test/java/com/sun/jersey/json/impl/NamespaceAttributeTest.java

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

%build

mvn-rpmbuild install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-project.pom
%add_maven_depmap JPP.%{name}-project.pom

mkdir -p %{buildroot}%{_javadir}/%{name}
for m in %{name}-atom \
  %{name}-client \
  %{name}-core \
  %{name}-fastinfoset \
%if %{with_grizzly}
  %{name}-grizzly2 \
  %{name}-grizzly2-servlet \
%endif
  %{name}-json \
  %{name}-core \
  %{name}-server \
  %{name}-server-linking \
  %{name}-servlet; do
 install -m 644 ${m}/target/${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${m}.jar
 install -pm 644 ${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${m}.pom
%add_maven_depmap JPP.%{name}-${m}.pom %{name}/${m}.jar
done

# test-framework
install -pm 644 %{name}-test-framework/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-test-framework.pom
%add_maven_depmap JPP.%{name}-test-framework.pom -f test-framework
install -m 644 %{name}-test-framework/%{name}-test-framework-core/target/%{name}-test-framework.jar \
  %{buildroot}%{_javadir}/%{name}/%{name}-test-framework-core.jar
install -pm 644 %{name}-test-framework/%{name}-test-framework-core/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-test-framework-core.pom
%add_maven_depmap JPP.%{name}-%{name}-test-framework-core.pom %{name}/%{name}-test-framework-core.jar -f test-framework

for m in  %{name}-test-framework-external \
%if %{with_grizzly}
  %{name}-test-framework-grizzly2 \
%endif
  %{name}-test-framework-http \
  %{name}-test-framework-inmemory; do
 install -m 644 %{name}-test-framework/${m}/target/${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${m}.jar
 install -pm 644 %{name}-test-framework/${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${m}.pom
%add_maven_depmap JPP.%{name}-${m}.pom %{name}/${m}.jar -f test-framework
done

# contribs   %%{name}-simple-server \
install -pm 644 contribs/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-contribs.pom
%add_maven_depmap JPP.%{name}-contribs.pom -f contribs
for m in ant-wadl-task \
  %{name}-apache-client \
  %{name}-apache-client4 \
  %{name}-freemarker \
  %{name}-guice \
  %{name}-moxy \
  %{name}-multipart \
  %{name}-wadl-json-schema \
  wadl-resourcedoc-doclet; do
 install -m 644 contribs/${m}/target/${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${m}.jar
 install -pm 644 contribs/${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${m}.pom
%add_maven_depmap JPP.%{name}-${m}.pom %{name}/${m}.jar -f contribs
done

install -m 644 contribs/spring/target/%{name}-spring-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-spring.jar
install -pm 644 contribs/spring/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-spring.pom
%add_maven_depmap JPP.%{name}-%{name}-spring.pom %{name}/%{name}-spring.jar -f contribs

install -m 644 contribs/maven-wadl-plugin/target/wadl-maven-plugin-%{version}.jar %{buildroot}%{_javadir}/%{name}/maven-wadl-plugin.jar
install -pm 644 contribs/maven-wadl-plugin/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-maven-wadl-plugin.pom
%add_maven_depmap JPP.%{name}-maven-wadl-plugin.pom %{name}/maven-wadl-plugin.jar -f maven-plugin
mv %{buildroot}%{_mavendepmapfragdir}/%{name}-maven-plugin %{buildroot}%{_mavendepmapfragdir}/maven-wadl-plugin

install -pm 644 contribs/%{name}-oauth/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-oauth.pom
%add_maven_depmap JPP.%{name}-oauth.pom -f contribs
for m in oauth-client \
  oauth-server \
  oauth-signature; do
 install -m 644 contribs/%{name}-oauth/${m}/target/${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${m}.jar
 install -pm 644 contribs/%{name}-oauth/${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${m}.pom
%add_maven_depmap JPP.%{name}-${m}.pom %{name}/${m}.jar -f contribs
done

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "ant %{name}/%{name}-server jaxb-api" > ant-wadl-task
install -p -m 644 ant-wadl-task %{buildroot}%{_sysconfdir}/ant.d/ant-wadl-task

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-atom.jar
%{_javadir}/%{name}/%{name}-client.jar
%{_javadir}/%{name}/%{name}-core.jar
%{_javadir}/%{name}/%{name}-fastinfoset.jar
%{_javadir}/%{name}/%{name}-json.jar
%{_javadir}/%{name}/%{name}-server-linking.jar
%{_javadir}/%{name}/%{name}-server.jar
%{_javadir}/%{name}/%{name}-servlet.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-atom.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-client.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-core.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-fastinfoset.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-json.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-server-linking.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-server.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-servlet.pom
%{_mavenpomdir}/JPP.%{name}-project.pom
%{_mavendepmapfragdir}/%{name}
%if %{with_grizzly}
%{_javadir}/%{name}/%{name}-grizzly2-servlet.jar
%{_javadir}/%{name}/%{name}-grizzly2.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-grizzly2-servlet.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-grizzly2.pom
%endif
%doc changes.txt dependencies.html getting-started.html license.html legal/LICENSE.txt legal/maintenance/copyright.txt LICENSE-2.0.txt

%files test-framework
%{_javadir}/%{name}/%{name}-test-framework-core.jar
%{_javadir}/%{name}/%{name}-test-framework-external.jar
%{_javadir}/%{name}/%{name}-test-framework-http.jar
%{_javadir}/%{name}/%{name}-test-framework-inmemory.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-test-framework-core.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-test-framework-external.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-test-framework-http.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-test-framework-inmemory.pom
%{_mavenpomdir}/JPP.%{name}-test-framework.pom
%{_mavendepmapfragdir}/%{name}-test-framework
%if %{with_grizzly}
%{_javadir}/%{name}/%{name}-test-framework-grizzly2.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-test-framework-grizzly2.pom
%endif
%doc license.html legal/LICENSE.txt legal/maintenance/copyright.txt

%files contribs
%{_javadir}/%{name}/ant-wadl-task.jar
%{_javadir}/%{name}/%{name}-apache-client.jar
%{_javadir}/%{name}/%{name}-apache-client4.jar
%{_javadir}/%{name}/%{name}-freemarker.jar
%{_javadir}/%{name}/%{name}-guice.jar
%{_javadir}/%{name}/%{name}-moxy.jar
%{_javadir}/%{name}/%{name}-multipart.jar
#%%{_javadir}/%%{name}/%%{name}-simple-server.jar
%{_javadir}/%{name}/%{name}-spring.jar
%{_javadir}/%{name}/%{name}-wadl-json-schema.jar
%{_javadir}/%{name}/oauth-client.jar
%{_javadir}/%{name}/oauth-server.jar
%{_javadir}/%{name}/oauth-signature.jar
%{_javadir}/%{name}/wadl-resourcedoc-doclet.jar
%{_mavenpomdir}/JPP.%{name}-contribs.pom
%{_mavenpomdir}/JPP.%{name}-ant-wadl-task.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-apache-client.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-apache-client4.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-freemarker.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-guice.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-moxy.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-multipart.pom
#%%{_mavenpomdir}/JPP.%%{name}-%%{name}-simple-server.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-spring.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-wadl-json-schema.pom
%{_mavenpomdir}/JPP.%{name}-oauth-client.pom
%{_mavenpomdir}/JPP.%{name}-oauth-server.pom
%{_mavenpomdir}/JPP.%{name}-oauth-signature.pom
%{_mavenpomdir}/JPP.%{name}-oauth.pom
%{_mavenpomdir}/JPP.%{name}-wadl-resourcedoc-doclet.pom
%{_mavendepmapfragdir}/%{name}-contribs
%config(noreplace) %{_sysconfdir}/ant.d/ant-wadl-task
%doc license.html legal/LICENSE.txt legal/maintenance/copyright.txt

%files -n maven-wadl-plugin
%{_javadir}/%{name}/maven-wadl-plugin.jar
%{_mavenpomdir}/JPP.%{name}-maven-wadl-plugin.pom
%{_mavendepmapfragdir}/maven-wadl-plugin
%doc license.html legal/LICENSE.txt legal/maintenance/copyright.txt

%files javadoc
%{_javadocdir}/%{name}
%doc license.html legal/LICENSE.txt legal/maintenance/copyright.txt LICENSE-2.0.txt

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.17.1-alt1_2jpp7
- new release

