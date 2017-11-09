Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 3.2.18
%global namedreltag .RELEASE
%global namedversion %{version}%{?namedreltag}

Name:          springframework
Version:       3.2.18
Release:       alt1_3jpp8
Summary:       Spring Java Application Framework
Epoch:         0
License:       ASL 2.0
URL:           http://projects.spring.io/spring-framework/

Source0:       https://github.com/spring-projects/spring-framework/archive/v%{namedversion}/%{name}-%{namedversion}.tar.gz

Source101:     springframework-%{namedversion}.pom
Source102:     http://repo1.maven.org/maven2/org/%{name}/spring-core/%{namedversion}/spring-core-%{namedversion}.pom
Source103:     http://repo1.maven.org/maven2/org/%{name}/spring-expression/%{namedversion}/spring-expression-%{namedversion}.pom
Source104:     http://repo1.maven.org/maven2/org/%{name}/spring-context/%{namedversion}/spring-context-%{namedversion}.pom
Source105:     http://repo1.maven.org/maven2/org/%{name}/spring-aop/%{namedversion}/spring-aop-%{namedversion}.pom
Source106:     http://repo1.maven.org/maven2/org/%{name}/spring-instrument/%{namedversion}/spring-instrument-%{namedversion}.pom
Source107:     http://repo1.maven.org/maven2/org/%{name}/spring-beans/%{namedversion}/spring-beans-%{namedversion}.pom
Source108:     http://repo1.maven.org/maven2/org/%{name}/spring-orm/%{namedversion}/spring-orm-%{namedversion}.pom
Source109:     http://repo1.maven.org/maven2/org/%{name}/spring-test/%{namedversion}/spring-test-%{namedversion}.pom
Source110:     http://repo1.maven.org/maven2/org/%{name}/spring-context-support/%{namedversion}/spring-context-support-%{namedversion}.pom
Source111:     http://repo1.maven.org/maven2/org/%{name}/spring-instrument-tomcat/%{namedversion}/spring-instrument-tomcat-%{namedversion}.pom
Source112:     http://repo1.maven.org/maven2/org/%{name}/spring-jdbc/%{namedversion}/spring-jdbc-%{namedversion}.pom
Source113:     http://repo1.maven.org/maven2/org/%{name}/spring-jms/%{namedversion}/spring-jms-%{namedversion}.pom
Source114:     http://repo1.maven.org/maven2/org/%{name}/spring-tx/%{namedversion}/spring-tx-%{namedversion}.pom
Source115:     http://repo1.maven.org/maven2/org/%{name}/spring-web/%{namedversion}/spring-web-%{namedversion}.pom
Source116:     http://repo1.maven.org/maven2/org/%{name}/spring-oxm/%{namedversion}/spring-oxm-%{namedversion}.pom
Source117:     http://repo1.maven.org/maven2/org/%{name}/spring-struts/%{namedversion}/spring-struts-%{namedversion}.pom
Source118:     http://repo1.maven.org/maven2/org/%{name}/spring-webmvc/%{namedversion}/spring-webmvc-%{namedversion}.pom
Source119:     http://repo1.maven.org/maven2/org/%{name}/spring-webmvc-portlet/%{namedversion}/spring-webmvc-portlet-%{namedversion}.pom
# Customized pom file
# Some project use these classes.
Source120:     spring-test-mvc-%{namedversion}.pom
Source121:     spring-orm-hibernate4-template.pom

Patch0:        springframework-3.2.6-java.io.IOException-is-never-thrown.patch
Patch1:        springframework-3.2.6-port-spring-jms-to-javax.resources-1.7.patch
Patch2:        springframework-3.2.6-port-spring-orm-to-javax.persistence-2.0.patch
Patch3:        springframework-3.2.6-port-spring-test-to-servlet-3.1.patch
Patch4:        springframework-3.2.6-port-spring-tx-to-javax.resources-1.7.patch
Patch5:        springframework-3.2.6-port-to-hibernate-validator-5.patch
# Derby 10.6+ support
Patch6:        springframework-3.2.13-derby.patch
# jopt-simple 4.6 support
Patch7:        springframework-3.2.14-jopt-simple.patch
Patch8:        springframework-3.2.14-build-with-tomcat8.patch
# Hibernate 4.3+ and for JTA 1.1 support
Patch9:        springframework-3.2.18-hibernate4.3.patch

BuildRequires:  maven-local
BuildRequires:  mvn(aopalliance:aopalliance)
BuildRequires:  mvn(c3p0:c3p0)
BuildRequires:  mvn(com.caucho:hessian)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.h2database:h2)
BuildRequires:  mvn(com.jamonapi:jamon)
BuildRequires:  mvn(com.lowagie:itext)
BuildRequires:  mvn(com.rometools:rome)
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(commons-fileupload:commons-fileupload)
BuildRequires:  mvn(commons-httpclient:commons-httpclient)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(commons-pool:commons-pool)
BuildRequires:  mvn(com.thoughtworks.xstream:xstream)
BuildRequires:  mvn(hsqldb:hsqldb:1)
BuildRequires:  mvn(jasperreports:jasperreports)
BuildRequires:  mvn(javax.ejb:ejb-api)
BuildRequires:  mvn(javax.faces:jsf-api)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(javax.jdo:jdo-api)
BuildRequires:  mvn(javax.mail:mail)
BuildRequires:  mvn(javax.portlet:portlet-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(javax.servlet.jsp:jsp-api)
BuildRequires:  mvn(javax.servlet:jstl)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(javax.xml:jaxrpc-api)
BuildRequires:  mvn(javax.xml.soap:saaj-api)
BuildRequires:  mvn(joda-time:joda-time)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(net.sf.cglib:cglib)
BuildRequires:  mvn(net.sf.ehcache:ehcache-core)
BuildRequires:  mvn(net.sourceforge.jexcelapi:jxl)
BuildRequires:  mvn(org.apache.derby:derby)
BuildRequires:  mvn(org.apache.derby:derbyclient)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-interceptor_3.0_spec)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-jta_1.1_spec)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-validation_1.0_spec)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.openjpa:openjpa-lib)
BuildRequires:  mvn(org.apache.openjpa:openjpa-persistence)
BuildRequires:  mvn(org.apache.poi:poi)
BuildRequires:  mvn(org.apache.struts:struts-core)
BuildRequires:  mvn(org.apache.struts:struts-extras)
BuildRequires:  mvn(org.apache.struts:struts-tiles)
BuildRequires:  mvn(org.apache.tiles:tiles-api)
BuildRequires:  mvn(org.apache.tiles:tiles-core)
BuildRequires:  mvn(org.apache.tiles:tiles-el)
BuildRequires:  mvn(org.apache.tiles:tiles-jsp)
BuildRequires:  mvn(org.apache.tiles:tiles-servlet)
BuildRequires:  mvn(org.apache.tomcat:tomcat-catalina)
BuildRequires:  mvn(org.apache.tomcat:tomcat-el-api)
BuildRequires:  mvn(org.apache.tomcat:tomcat-jsp-api)
BuildRequires:  mvn(org.apache.tomcat:tomcat-servlet-api)
BuildRequires:  mvn(org.apache.xmlbeans:xmlbeans)
BuildRequires:  mvn(org.aspectj:aspectjweaver)
BuildRequires:  mvn(org.beanshell:bsh)
BuildRequires:  mvn(org.codehaus.castor:castor-xml)
BuildRequires:  mvn(org.codehaus.groovy:groovy)
BuildRequires:  mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires:  mvn(org.eclipse.persistence:org.eclipse.persistence.core)
BuildRequires:  mvn(org.eclipse.persistence:org.eclipse.persistence.jpa)
BuildRequires:  mvn(org.freemarker:freemarker)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.hibernate:hibernate-core:4)
BuildRequires:  mvn(org.hibernate:hibernate-core:3)
BuildRequires:  mvn(org.hibernate:hibernate-entitymanager:4)
BuildRequires:  mvn(org.hibernate:hibernate-entitymanager:3)
BuildRequires:  mvn(org.hibernate:hibernate-validator)
BuildRequires:  mvn(org.hibernate.javax.persistence:hibernate-jpa-2.0-api)
BuildRequires:  mvn(org.hibernate.javax.persistence:hibernate-jpa-2.1-api)
BuildRequires:  mvn(org.jboss.spec.javax.resource:jboss-connector-api_1.7_spec)
BuildRequires:  mvn(org.jibx:jibx-run)
BuildRequires:  mvn(org.jruby.extras:bytelist)
BuildRequires:  mvn(org.jruby:jruby)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.quartz-scheduler:quartz)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.testng:testng)
BuildRequires:  mvn(toplink.essentials:toplink-essentials)
BuildRequires:  mvn(velocity-tools:velocity-tools-view)
BuildRequires:  mvn(velocity:velocity)
BuildRequires:  mvn(xmlunit:xmlunit)
BuildRequires:  mvn(org.apache.taglibs:taglibs-standard-jstlel)
BuildRequires:  mvn(javax.servlet:jstl)
BuildRequires:  mvn(org.apache.taglibs:taglibs-standard-spec)
BuildRequires:  mvn(com.jayway.jsonpath:json-path)
BuildRequires:  mvn(net.sf.jopt-simple:jopt-simple)
BuildRequires:  xmvn

Obsoletes:     %{name}-instrument-tomcat

BuildArch:     noarch
Source44: import.info

%description
Spring is a layered Java/J2EE application framework, based on code published in
Expert One-on-One J2EE Design and Development by Rod Johnson (Wrox, 2002). 

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%package aop
Group: Development/Java
Summary:       Spring Aspect Oriented Framework

%description aop
Spring AOP is an enabling technology that allows the implementation of custom
aspects and provides declarative transaction management without EJB.

%package beans
Group: Development/Java
Summary:       Spring Bean Factory

%description beans
The Spring Bean Factory provides an advanced configuration mechanism capable of
managing beans of any nature, using potentially any kind of storage facility.

%package context
Group: Development/Java
Summary:       Spring Application Context

%description context
The Spring Application Context is a complete superset of a bean factory, and
adds enhanced capabilities to it, some of them more J2EE and
enterprise-centric.

%package context-support
Group: Development/Java
Summary:       Spring Context Support

%description context-support
This package provide Quartz/CommonJ scheduling,
UI templating, mail and caching.

%package expression
Group: Development/Java
Summary:       Spring Expression Language (SpEL)

%description expression
The Spring Expression Language (SpEL for short) is a powerful expression
language that supports querying and manipulating an object graph at runtime.

%package instrument
Group: Development/Java
Summary:       Spring Instrumentation

%description instrument
The Spring Instrumentation Framework exposes performance and
resource utilization metrics for the Spring container and
gives you runtime control of the container.

#%%package instrument-tomcat
#Summary:       Spring Instrument Tomcat Weaver

#%%description instrument-tomcat
#Extension of Tomcat's default class loader which
#adds instrumentation to loaded classes without the
#need to use a VM-wide agent.

%package jdbc
Group: Development/Java
Summary:       Spring JDBC

%description jdbc
Spring JDBC takes care of all the low-level details associated to the
development with JDBC.

%package jms
Group: Development/Java
Summary:       Spring jms

%description jms
This package provide Java Message Service 1.0.2/1.1 support.

%package orm
Group: Development/Java
Summary:       Spring ORM

%description orm
This package provide JDO support, JPA support, Hibernate
support, TopLink support.

%package orm-hibernate4
Group: Development/Java
Summary:       Spring ORM Hibernate 4 Support

%description orm-hibernate4
This package provide Hibernate 4 support.

%package oxm
Group: Development/Java
Summary:       Spring OXM

%description oxm
This package provide marshaling and unmarshalling
for XML with JAXB context and JiBX binding factories.

%package struts
Group: Development/Java
Summary:       Spring Web Struts

%description struts
This package provide integrate a Struts
application with Spring

%package test
Group: Development/Java
Summary:       Spring test context framework

%description test
Spring's test context framework. Also includes common Servlet and
Portlet API mocks.

%package test-mvc
Group: Development/Java
Summary:       Spring Test MVC Framework

%description test-mvc
Spring's test MVC framework.

%package tx
Group: Development/Java
Summary:       Spring Transaction Management

%description tx
Spring provides a consistent abstraction for transaction management that
provides a consistent programming model across different transaction APIs,
supports declarative transaction management, provides a simpler API for
programmatic transaction management and integrates with Spring's various data
access abstractions.

%package web
Group: Development/Java
Summary:       Spring Web

%description web
This package provide web application context, multipart
resolver, HTTP-based remoting support.

%package webmvc
Group: Development/Java
Summary:       Spring Web Servlet

%description webmvc
This package provide framework servlets, web MVC framework,
web controllers, web views for JSP, Velocity, Tiles,
iText and POI.

%package webmvc-portlet
Group: Development/Java
Summary:       Spring Web Portlet

%description webmvc-portlet
This package provide support development of Portlet
applications with Spring.

%prep
%setup -q -n spring-framework-%{namedversion}
find -name "*.class" -delete
find -name "*.jar" -print -delete

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

cp %{SOURCE101} pom.xml
cp %{SOURCE102} spring-core/pom.xml
cp %{SOURCE103} spring-expression/pom.xml
cp %{SOURCE104} spring-context/pom.xml
cp %{SOURCE105} spring-aop/pom.xml
cp %{SOURCE106} spring-instrument/pom.xml
cp %{SOURCE107} spring-beans/pom.xml
cp %{SOURCE108} spring-orm/pom.xml
cp %{SOURCE109} spring-test/pom.xml
cp %{SOURCE110} spring-context-support/pom.xml

%pom_disable_module spring-instrument-tomcat
#cp %%{SOURCE111} spring-instrument-tomcat/pom.xml

cp %{SOURCE112} spring-jdbc/pom.xml
cp %{SOURCE113} spring-jms/pom.xml
cp %{SOURCE114} spring-tx/pom.xml
cp %{SOURCE115} spring-web/pom.xml
cp %{SOURCE116} spring-oxm/pom.xml
cp %{SOURCE117} spring-struts/pom.xml
cp %{SOURCE118} spring-webmvc/pom.xml
cp %{SOURCE119} spring-webmvc-portlet/pom.xml
cp %{SOURCE120} spring-test-mvc/pom.xml
cp %{SOURCE121} spring-orm-hibernate4/pom.xml
sed -i "s|@VERSION@|%{namedversion}|" spring-orm-hibernate4/pom.xml
%pom_xpath_inject pom:modules "<module>spring-orm-hibernate4</module>"
%pom_change_dep -r org.hibernate: ::4 spring-orm-hibernate4

# do not generate R on hiberante4, we use version 3
%pom_remove_dep :hibernate-entitymanager spring-orm
%pom_add_dep org.hibernate:hibernate-entitymanager:3 spring-orm
%pom_remove_dep :hibernate-core spring-orm
%pom_add_dep org.hibernate:hibernate-core:3 spring-orm

%pom_remove_dep struts:struts spring-struts
%pom_add_dep org.apache.struts:struts-core spring-struts
%pom_add_dep org.apache.struts:struts-extras spring-struts
%pom_add_dep org.apache.struts:struts-tiles spring-struts

# remove optional/missing deps
%pom_remove_dep org.apache.tiles:tiles-extras spring-webmvc
%pom_change_dep :tiles-el ::2.1.2 spring-webmvc
%pom_remove_dep ::3.0.4 spring-webmvc

# build against connector-api 1.7 instead of 1.5
%pom_remove_dep javax.resource:connector-api spring-tx
%pom_add_dep org.jboss.spec.javax.resource:jboss-connector-api_1.7_spec spring-tx

# Remove the dependency on WebSphere UOW as it is not open source and we will
# never be able to build it:
%pom_remove_dep com.ibm.websphere:uow spring-tx
rm spring-tx/src/main/java/org/springframework/transaction/jta/WebSphereUowTransactionManager.java \
 spring-tx/src/test/java/org/springframework/transaction/jta/WebSphereUowTransactionManagerTests.java

# hiberante3 is a compat package
%pom_remove_dep :hibernate-annotations spring-orm
%pom_remove_dep :hibernate-core spring-orm
%pom_add_dep org.hibernate:hibernate-core:3 spring-orm

# missing dep ibatis
rm -rf spring-orm/src/main/java/org/springframework/orm/ibatis/*
%pom_remove_dep :ibatis-sqlmap spring-orm

%pom_remove_dep :openjpa spring-orm
%pom_add_dep org.apache.openjpa:openjpa-lib spring-orm

%pom_add_dep org.apache.openjpa:openjpa-persistence spring-orm

# build against connector-api 1.7 instead of 1.5
%pom_remove_dep javax.resource:connector-api spring-jms
%pom_add_dep org.jboss.spec.javax.resource:jboss-connector-api_1.7_spec spring-jms

# hsqldb1 is a compat package, fix version
%pom_remove_dep hsqldb:hsqldb spring-jdbc
%pom_add_dep hsqldb:hsqldb:1 spring-jdbc

# use tomcat 7 lib
#%% pom_remove_dep org.apache.tomcat:catalina spring-instrument-tomcat
#%% pom_add_dep org.apache.tomcat:tomcat-catalina spring-instrument-tomcat

# missing dep jcache TODO use geronimo-jcache
rm -Rf spring-context-support/src/main/java/org/springframework/cache/jcache/
%pom_remove_dep javax.cache:cache-api spring-context-support

# missing dep commonj
rm -Rf spring-context-support/src/main/java/org/springframework/scheduling/
%pom_remove_dep org.codehaus.fabric3.api:commonj spring-context-support

# replace javax deps
for p in beans \
 web \
 webmvc; do
  %pom_remove_dep :el-api spring-${p}
  %pom_add_dep org.apache.tomcat:tomcat-el-api spring-${p}
done

%pom_remove_dep :persistence-api spring-context
%pom_add_dep org.hibernate.javax.persistence:hibernate-jpa-2.0-api spring-context
%pom_remove_dep :validation-api spring-context
%pom_add_dep org.apache.geronimo.specs:geronimo-validation_1.0_spec spring-context

%pom_add_dep org.apache.geronimo.specs:geronimo-interceptor_3.0_spec spring-context
%pom_add_dep org.jruby.extras:bytelist spring-context

%pom_remove_dep :persistence-api spring-orm
%pom_add_dep org.hibernate.javax.persistence:hibernate-jpa-2.0-api spring-orm
%pom_remove_dep javax.servlet:servlet-api spring-orm
%pom_add_dep org.apache.tomcat:tomcat-servlet-api spring-context

%pom_remove_dep :persistence-api spring-test
%pom_add_dep org.apache.tomcat:tomcat-el-api spring-test
%pom_remove_dep javax.servlet.jsp:jsp-api spring-test
%pom_add_dep org.apache.tomcat:tomcat-jsp-api spring-test

%pom_remove_dep -r javax.activation:activation

%pom_add_dep org.apache.taglibs:taglibs-standard-jstlel spring-test '<optional>true</optional>'

%pom_add_dep javax.servlet:jstl spring-web '<optional>true</optional>'
%pom_remove_dep taglibs:standard spring-web

%pom_add_dep org.apache.taglibs:taglibs-standard-spec spring-webmvc '<optional>true</optional>'

# ERROR: XThis is not public in Bsh
rm spring-context/src/main/java/org/springframework/scripting/bsh/BshScriptFactory.java
rm spring-context/src/main/java/org/springframework/scripting/bsh/BshScriptUtils.java

# Don't depend on backport-util-concurrent (upstream dropped this dep in 4.x)
%pom_remove_dep :backport-util-concurrent spring-context

# TODO: missing deps in upstream poms?
%pom_add_dep org.ow2.asm:asm spring-core
%pom_add_dep net.sf.cglib:cglib:4.2 spring-core

%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'org.codehaus.groovy']/pom:artifactId" groovy spring-context

find ./ -name "*.java" -exec sed -i "s/org.springframework.asm/org.objectweb.asm/g" {} +
find ./ -name "*.java" -exec sed -i "s/org.springframework.cglib/net.sf.cglib/g" {} +
find ./ -name "*.java" -exec sed -i "/edu.emory.mathcs.backport/d" {} +

%pom_change_dep -r :rome com.rometools: spring-test-mvc spring-web spring-webmvc
find ./spring-test-mvc -name "*.java" -exec sed -i "s/com.sun.syndication/com.rometools.rome/g" {} + 
find ./spring-web -name "*.java" -exec sed -i "s/com.sun.syndication/com.rometools.rome/g" {} +
find ./spring-webmvc -name "*.java" -exec sed -i "s/com.sun.syndication/com.rometools.rome/g" {} +


rm spring-context/src/main/java/org/springframework/scheduling/backportconcurrent/*

# copy license and notice file
cp -p src/dist/* .

# Copy resources in non standard directory. Several projects (also test suite) use these resources
mkdir -p spring-context/src/main/resources/org/springframework/remoting/rmi
cp -p spring-context/src/main/java/org/springframework/remoting/rmi/RmiInvocationWrapperRTD.xml \
 spring-context/src/main/resources/org/springframework/remoting/rmi/
mkdir -p spring-context-support/src/main/resources/org/springframework/mail/javamail
cp -p spring-context-support/src/main/java/org/springframework/mail/javamail/mime.types \
 spring-context-support/src/main/resources/org/springframework/mail/javamail/
mkdir -p spring-web/src/main/resources/org/springframework/web/context
cp -p spring-web/src/main/java/org/springframework/web/context/ContextLoader.properties \
 spring-web/src/main/resources/org/springframework/web/context/
mkdir -p spring-webmvc/src/main/resources/org/springframework/web/servlet/view/velocity
cp -p spring-webmvc/src/main/java/org/springframework/web/servlet/DispatcherServlet.properties \
 spring-webmvc/src/main/resources/org/springframework/web/servlet/
cp -p spring-webmvc/src/main/java/org/springframework/web/servlet/view/velocity/spring.vm \
 spring-webmvc/src/main/resources/org/springframework/web/servlet/view/velocity
mkdir -p spring-webmvc/src/main/resources/org/springframework/web/servlet/view/freemarker
cp -p spring-webmvc/src/main/java/org/springframework/web/servlet/view/freemarker/spring.ftl \
 spring-webmvc/src/main/resources/org/springframework/web/servlet/view/freemarker/
mkdir -p spring-webmvc-portlet/src/main/resources/org/springframework/web/portlet
cp -p spring-webmvc-portlet/src/main/java/org/springframework/web/portlet/DispatcherPortlet.properties \
 spring-webmvc-portlet/src/main/resources/org/springframework/web/portlet/

#  instrument-tomcat
for p in aop \
 beans \
 context \
 context-support \
 core \
 expression \
 instrument \
 jdbc \
 jms \
 orm \
 oxm \
 struts \
 test \
 test-mvc \
 tx \
 web \
 webmvc \
 webmvc-portlet; do
 %pom_xpath_inject "pom:project" "<packaging>bundle</packaging>" spring-${p}
 %pom_add_plugin org.apache.felix:maven-bundle-plugin:2.5.4 spring-${p} "
 <extensions>true</extensions>
 <configuration>
   <instructions>
     <Bundle-SymbolicName>\${project.groupId}.${p}</Bundle-SymbolicName>
     <Bundle-Name>\${project.name}</Bundle-Name>
     <Bundle-Version>\${project.version}</Bundle-Version>
   </instructions>
 </configuration>
 <executions>
   <execution>
     <id>bundle-manifest</id>
     <phase>process-classes</phase>
     <goals>
       <goal>manifest</goal>
     </goals>
   </execution>
 </executions>"
done

%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>" spring-orm-hibernate4
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.5.4 spring-orm-hibernate4 "
<extensions>true</extensions>
 <configuration>
  <instructions>
    <Bundle-SymbolicName>\${project.groupId}.orm.hibernate4</Bundle-SymbolicName>
    <Bundle-Name>\${project.name}</Bundle-Name>
    <Bundle-Version>\${project.version}</Bundle-Version>
  </instructions>
 </configuration>
 <executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>"

%mvn_package ":spring-core" %{name}
%mvn_package :spring-project __noinstall

%build
# Build without the tests, as they bring a lot of dependecies that are not
# available in the distribution at the moment:
%mvn_build -X -f -s -- -Dproject.build.sourceEncoding=ISO-8859-1

%install
%mvn_install

%files -f .mfiles-%{name}
%doc README.md
%doc license.txt  notice.txt
%files javadoc -f .mfiles-javadoc
%doc license.txt  notice.txt
%files aop -f .mfiles-spring-aop
%files beans -f .mfiles-spring-beans
%files context -f .mfiles-spring-context
%files context-support -f .mfiles-spring-context-support
%files expression -f .mfiles-spring-expression
%files instrument -f .mfiles-spring-instrument
%doc license.txt  notice.txt
#%%files instrument-tomcat -f .mfiles-spring-instrument-tomcat
#%%license license.txt  notice.txt
%files jdbc -f .mfiles-spring-jdbc
%files jms -f .mfiles-spring-jms
%files orm -f .mfiles-spring-orm
%files orm-hibernate4 -f .mfiles-spring-orm-hibernate4
%files oxm -f .mfiles-spring-oxm
%files struts -f .mfiles-spring-struts
%files test -f .mfiles-spring-test
%files test-mvc -f .mfiles-spring-test-mvc
%files tx -f .mfiles-spring-tx
%files web -f .mfiles-spring-web
%files webmvc -f .mfiles-spring-webmvc
%files webmvc-portlet -f .mfiles-spring-webmvc-portlet


%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.2.18-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.2.18-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.2.15-alt1_3jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.2.15-alt1_2jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.2.14-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0:3.1.1-alt1_10jpp7.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for springframework

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1.1-alt1_10jpp7
- first build
