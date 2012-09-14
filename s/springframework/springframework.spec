BuildRequires: bouncycastle-mail bouncycastle-tsp xpp3-minimal
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: springframework
Summary: Spring Java Application Framework
Version: 3.1.1
Release: alt1_10jpp7
Epoch: 0
License: ASL 2.0
Group: Development/Java
URL: http://www.springframework.org
BuildArch: noarch

# curl https://nodeload.github.com/SpringSource/spring-framework/tarball/v3.1.1.RELEASE > spring-framework-3.1.1.tar.gz
Source0: %{name}-%{version}.tar.gz
Source1: spring-framework-%{version}-pom.xml
# force use tomcat 7.x apis
Source2: spring-framework-%{version}-depmap

# Use the group id of Jetty 8, it has to be org.eclipse.jetty instead of
# org.mortbay.jetty:
Patch1: %{name}-update-jetty-gid.patch

# Remove the dependency on jaxws-api as this is part of the JDK:
Patch2: %{name}-remove-jaxws-api-dependency.patch

# Update the cglib group id (it should be net.sf.cglib instead of cglib) and
# the artifact id (it should be cglib instead of cglib-nodep):
Patch3: %{name}-update-cglib-gid-and-aid.patch

# Don't rename the asm package:
Patch4: %{name}-dont-rebundle-asm.patch

# Don't use the AWS extension:
Patch5: %{name}-dont-use-aws-extension.patch

# The groovy package that we have in the distribution at the
# moment provides the "groovy" artifact, but not the "groovy-all"
# artifact, required by spring. We are patching spring to use
# "groovy" instead of "groovy-all", but this should probably be
# reviewed in the groovy package:
Patch6: %{name}-downgrade-groovy-aid.patch

# Remove the dependency on JRuby (sources using it are also removed before
# building):
Patch7: %{name}-remove-jruby-dependency.patch

# Use the correct hibernate validator artifact id:
Patch9: %{name}-fix-hibernate-validator-aid.patch

# Remove the dependency on jsr-166 as this is part of the JDK:
Patch10: %{name}-remove-jsr166-dependency.patch

# Remove the dependency on WebSphere UOW as it is not open source and we will
# never be able to build it:
Patch11: %{name}-remove-websphere-uow-dependency.patch

# Use the the standard EJB API (currently provided by geronimo-ejb) instead of
# a spring specific one:
Patch12: %{name}-use-javax-ejb.patch

# Use the JCA API provided by JBoss:
Patch13: %{name}-use-jboss-jca-api.patch

# Use the correct Derby artifact id:
Patch14: %{name}-fix-derby-aid.patch

# Fix the tomcat catalina artifact id to use the one in Tomcat 7 as Tomcat 6
# has no POMs:
Patch15: %{name}-fix-tomcat-catalina-aid.patch
# change
# com.bea.commonj com.springsource.commonj org.apache.geronimo.specs geronimo-commonj_1.1_spec
# opensymphony with org.quartz-scheduler
# remove javax.activation
# fix jasperreports gId
Patch17: springframework-3.1.1-context_support-pom.patch
# fix build with velocity 1.7
Patch18: springframework-3.1.1-velocity.patch
# unavailable deps castor-xml
Patch19: springframework-3.1.1-oxm-remove-castor-xml.patch
# use jboss-connector-api_1.6_spec instead of geronimo-j2ee-connector_1.5_spec
Patch20: springframework-3.1.1-jms-connector-api.patch
# fix openjpa deps
Patch21: springframework-3.1.1-orm-pom.patch
# jpa-2.0-api support
Patch22: springframework-3.1.1-orm-jpa_api.patch
# add tiles-el
Patch23: springframework-3.1.1-web_servlet-pom.patch
# fix struts deps
Patch24: springframework-3.1.1-struts-pom.patch
# Build with Quartz 2.x only
Patch25: springframework-3.1.1-no-quartz1.patch

Patch33: springframework-3.1.1-alt-jcommon-0.17.patch

# Build requirements (alphabetical):
BuildRequires: aopalliance
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-logging
BuildRequires: aspectjweaver
BuildRequires: atinject
BuildRequires: backport-util-concurrent
BuildRequires: bsh
BuildRequires: c3p0
BuildRequires: cglib
BuildRequires: derby
BuildRequires: ehcache-core
BuildRequires: geronimo-annotation
BuildRequires: geronimo-ejb
BuildRequires: geronimo-interceptor
BuildRequires: geronimo-jpa
BuildRequires: geronimo-jta
BuildRequires: geronimo-validation
BuildRequires: groovy
BuildRequires: h2
BuildRequires: hamcrest
BuildRequires: hibernate3
BuildRequires: hibernate3-entitymanager
BuildRequires: hibernate-jpa-2.0-api
BuildRequires: hibernate-validator
BuildRequires: hsqldb
BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: jamonapi >= 2.73-5
BuildRequires: jboss-connector-1.6-api
BuildRequires: jboss-el-2.2-api >= 1.0.1-0.2
BuildRequires: jboss-jstl-1.2-api
BuildRequires: jetty
BuildRequires: joda-time
BuildRequires: jopt-simple
BuildRequires: jpackage-utils
BuildRequires: junit
BuildRequires: log4j
BuildRequires: objectweb-asm
BuildRequires: tomcat-el-2.2-api
BuildRequires: tomcat-lib >= 7.0.27-2

BuildRequires: apache-poi
BuildRequires: apache-commons-fileupload >= 1.2.2-5
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-pool
BuildRequires: axis
BuildRequires: eclipselink
BuildRequires: eclipse-jdt
BuildRequires: freemarker >= 2.3.19
BuildRequires: geronimo-commonj
BuildRequires: geronimo-jaxrpc
BuildRequires: geronimo-jms
BuildRequires: geronimo-saaj
BuildRequires: glassfish-jaxb
BuildRequires: glassfish-toplink-essentials
BuildRequires: hessian
BuildRequires: httpcomponents-client
BuildRequires: itext
BuildRequires: jackson
BuildRequires: jakarta-commons-httpclient
BuildRequires: jakarta-taglibs-standard
BuildRequires: jasperreports
BuildRequires: jboss-jsf-2.1-api
BuildRequires: jboss-jsp-2.2-api
BuildRequires: jdo2-api
BuildRequires: jexcelapi
BuildRequires: jfreechart
BuildRequires: jibx >= 1.2.4-3
BuildRequires: openjpa
BuildRequires: portlet-2.0-api
BuildRequires: quartz
BuildRequires: rome >= 0.9-11
BuildRequires: struts
BuildRequires: tiles
BuildRequires: tomcat-servlet-3.0-api
BuildRequires: velocity
BuildRequires: velocity-tools
BuildRequires: xmlbeans
BuildRequires: xstream

# Runtime requirements (only for the main package, other requirements go in the
# subpackages):
Requires: apache-commons-collections
Requires: apache-commons-logging
Requires: aspectjweaver
Requires: objectweb-asm
Requires: log4j
Requires: jopt-simple
Requires: jpackage-utils
Source44: import.info


%description
Spring is a layered Java/J2EE application framework, based on code published in
Expert One-on-One J2EE Design and Development by Rod Johnson (Wrox, 2002). 


%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.


%package aop
Summary: Spring Aspect Oriented Framework
Group: Development/Java
Requires: %{name}-beans = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Requires: apache-commons-logging
Requires: apache-commons-pool
Requires: aopalliance
Requires: aspectjweaver
Requires: cglib
Requires: jamonapi
Requires: objectweb-asm

%description aop
Spring AOP is an enabling technology that allows the implementation of custom
aspects and provides declarative transaction management without EJB.


%package beans
Summary: Spring Bean Factory
Group: Development/Java
Requires: %{name} = %{version}-%{release}
Requires: atinject
Requires: cglib
Requires: tomcat-el-2.2-api

%description beans
The Spring Bean Factory provides an advanced configuration mechanism capable of
managing beans of any nature, using potentially any kind of storage facility.


%package context
Summary: Spring Application Context
Group: Development/Java
Requires: %{name} = %{version}-%{release}
Requires: %{name}-aop = %{version}-%{release}
Requires: %{name}-beans = %{version}-%{release}
Requires: %{name}-expression = %{version}-%{release}
Requires: %{name}-instrument = %{version}-%{release}
Requires: aspectjweaver
Requires: atinject
Requires: backport-util-concurrent
Requires: bsh
Requires: cglib
Requires: geronimo-annotation
Requires: geronimo-ejb
Requires: geronimo-interceptor
Requires: geronimo-jpa
Requires: geronimo-jta
Requires: geronimo-validation
Requires: groovy
Requires: hamcrest
Requires: hibernate-validator
Requires: joda-time
Requires: objectweb-asm

%description context
The Spring Application Context is a complete superset of a bean factory, and
adds enhanced capabilities to it, some of them more J2EE and
enterprise-centric.

%package context-support
Summary:  Spring Context Support
Group:    Development/Java
Requires: %{name} = %{version}-%{release}
Requires: %{name}-beans = %{version}-%{release}
Requires: %{name}-context = %{version}-%{release}
Requires: %{name}-jdbc = %{version}-%{release}
Requires: %{name}-tx = %{version}-%{release}
Requires: apache-commons-collections
Requires: freemarker >= 2.3.19
Requires: geronimo-commonj
Requires: jasperreports
Requires: javamail
Requires: velocity
# Should these be considered optional?
Requires: ehcache-core
Requires: quartz

%description context-support
Spring J2EE Framework.

This package provide Quartz/CommonJ scheduling,
UI templating, mail and caching.

%package expression
Summary: Spring Expression Language (SpEL)
Group: Development/Java
Requires: %{name} = %{version}-%{release}

%description expression
The Spring Expression Language (SpEL for short) is a powerful expression
language that supports querying and manipulating an object graph at runtime.


%package instrument
Summary: Spring Instrumentation
Group: Development/Java
Requires: %{name} = %{version}-%{release}

%description instrument
The Spring Instrumentation Framework exposes performance and resource utilization
metrics for the Spring container and gives you runtime control of the
container.


%package jdbc
Summary: Spring JDBC
Group: Development/Java
Requires: %{name} = %{version}-%{release}
Requires: %{name}-beans = %{version}-%{release}
Requires: %{name}-context = %{version}-%{release}
Requires: %{name}-tx = %{version}-%{release}
Requires: c3p0
Requires: geronimo-jta
Requires: h2
Requires: hsqldb
Requires: derby

%description jdbc
Spring JDBC takes care of all the low-level details associated to the
development with JDBC.

%package jms
Summary:  Spring jms
Group:    Development/Java
Requires: %{name} = %{version}-%{release}
Requires: %{name}-aop = %{version}-%{release}
Requires: %{name}-beans = %{version}-%{release}
Requires: %{name}-context = %{version}-%{release}
Requires: %{name}-oxm = %{version}-%{release}
Requires: %{name}-tx = %{version}-%{release}
Requires: aopalliance
Requires: apache-commons-pool
Requires: geronimo-jms
Requires: geronimo-jta
Requires: jackson
Requires: jboss-connector-1.6-api

%description jms
Spring J2EE Framework.
This package provide Java Message Service 1.0.2/1.1 support.

%package orm
Summary:  Spring ORM
Group:    Development/Java
Requires: %{name} = %{version}-%{release}
Requires: %{name}-aop = %{version}-%{release}
Requires: %{name}-beans = %{version}-%{release}
Requires: %{name}-context = %{version}-%{release}
Requires: %{name}-jdbc = %{version}-%{release}
Requires: %{name}-tx = %{version}-%{release}
Requires: %{name}-web = %{version}-%{release}
Requires: aopalliance
Requires: eclipselink
Requires: geronimo-jta
Requires: glassfish-toplink-essentials
Requires: hibernate3
Requires: hibernate-jpa-2.0-api
Requires: jdo2-api
Requires: openjpa
Requires: tomcat-servlet-3.0-api

%description orm
Spring J2EE Framework.

This package provide JDO support, JPA support, Hibernate
support, TopLink support, iBATIS support.

%package oxm
Summary:  Spring OXM
Group:    Development/Java
Requires: %{name} = %{version}-%{release}
Requires: %{name}-beans = %{version}-%{release}
Requires: %{name}-context = %{version}-%{release}
Requires: aopalliance
Requires: apache-commons-lang
Requires: glassfish-jaxb
Requires: jibx >= 1.2.4-3
Requires: xmlbeans
Requires: xstream

%description oxm
Spring J2EE Framework.

This package provide marshaling and unmarshalling
for XML with JAXB context and JiBX binding factories.

%package struts
Summary:  Spring Web Struts
Group:    Development/Java
Requires: %{name} = %{version}-%{release}
Requires: %{name}-beans = %{version}-%{release}
Requires: %{name}-context = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-web = %{version}-%{release}
Requires: %{name}-webmvc = %{version}-%{release}
Requires: apache-commons-beanutils
Requires: jakarta-taglibs-standard
Requires: jboss-jsp-2.2-api
Requires: tomcat-servlet-3.0-api
Requires: struts

%description struts
Spring J2EE Framework.

This package provide integrate a Struts
application with Spring

%package tx
Summary: Spring Transaction Management
Group: Development/Java
Requires: %{name} = %{version}-%{release}

%description tx
Spring provides a consistent abstraction for transaction management that
provides a consistent programming model across different transaction APIs,
supports declarative transaction management, provides a simpler API for
programmatic transaction management and integrates with Spring's various data
access abstractions.

%package web
Summary:  Spring Web
Group:    Development/Java
Requires: %{name} = %{version}-%{release}
Requires: %{name}-aop = %{version}-%{release}
Requires: %{name}-beans = %{version}-%{release}
Requires: %{name}-context = %{version}-%{release}
Requires: %{name}-oxm = %{version}-%{release}
Requires: aopalliance
Requires: apache-commons-fileupload >= 1.2.2-5
Requires: axis
Requires: hessian
Requires: httpcomponents-client
Requires: jakarta-commons-httpclient
Requires: jackson
Requires: log4j
Requires: portlet-2.0-api
Requires: rome >= 0.9-11
Requires: tomcat-servlet-3.0-api
Requires: jboss-el-2.2-api
Requires: jboss-jsf-2.1-api
Requires: jboss-jsp-2.2-api
Requires: geronimo-jaxrpc
Requires: geronimo-saaj

%description web
Spring J2EE Framework.

This package provide web application context, multipart
resolver, HTTP-based remoting support.

%package webmvc
Summary:  Spring Web Servlet
Group:    Development/Java
Requires: %{name} = %{version}-%{release}
Requires: %{name}-beans = %{version}-%{release}
Requires: %{name}-context = %{version}-%{release}
Requires: %{name}-context-support = %{version}-%{release}
Requires: %{name}-expression = %{version}-%{release}
Requires: %{name}-orm = %{version}-%{release}
Requires: %{name}-oxm = %{version}-%{release}
Requires: %{name}-web = %{version}-%{release}
Requires: apache-poi
Requires: freemarker
Requires: geronimo-jta
Requires: geronimo-validation
Requires: itext
Requires: jackson
Requires: jakarta-taglibs-standard
Requires: jasperreports
Requires: jboss-el-2.2-api
Requires: jboss-jsp-2.2-api
Requires: jexcelapi
Requires: objectweb-asm
Requires: rome >= 0.9-11
Requires: tiles
Requires: tomcat-servlet-3.0-api
Requires: velocity
Requires: velocity-tools

%description webmvc
Spring J2EE Framework.

This package provide framework servlets, web MVC framework,
web controllers, web views for JSP, Velocity, Tiles,
iText and POI.

%package webmvc-portlet
Summary:  Spring Web Portlet
Group:    Development/Java
Requires: %{name} = %{version}-%{release}
Requires: %{name}-beans = %{version}-%{release}
Requires: %{name}-context = %{version}-%{release}
Requires: %{name}-web = %{version}-%{release}
Requires: %{name}-webmvc = %{version}-%{release}
Requires: apache-commons-fileupload >= 1.2.2-5
Requires: jboss-el-2.2-api
Requires: jboss-jsp-2.2-api
Requires: objectweb-asm
Requires: portlet-2.0-api
Requires: tomcat-servlet-3.0-api

%description webmvc-portlet
Spring J2EE Framework.

This package provide support development of Portlet
applications with Spring.

%prep
%setup -q -n SpringSource-spring-framework-79c9ca1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
# %patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

%patch17 -p0
%patch18 -p0
%patch19 -p0
%patch20 -p0
%patch21 -p0
%patch22 -p0
%patch23 -p0
%patch24 -p0
%patch25 -p1

%patch33 -p1

# ERROR: XThis is not public in Bsh
rm org.springframework.context/src/main/java/org/springframework/scripting/bsh/BshScriptFactory.java
rm org.springframework.context/src/main/java/org/springframework/scripting/bsh/BshScriptUtils.java

# ERROR: JRubyScriptUtils.java:[81,28] error: cannot access ByteList
rm org.springframework.context/src/main/java/org/springframework/scripting/jruby/JRubyScriptFactory.java
rm org.springframework.context/src/main/java/org/springframework/scripting/jruby/JRubyScriptUtils.java

# Remove classes which explicitly require Quartz 1.x (others are patched)
rm org.springframework.context.support/src/main/java/org/springframework/scheduling/quartz/JobDetailBean.java
rm org.springframework.context.support/src/main/java/org/springframework/scheduling/quartz/SimpleTriggerBean.java
rm org.springframework.context.support/src/main/java/org/springframework/scheduling/quartz/CronTriggerBean.java

# require castor-xml
rm -rf org.springframework.oxm/src/main/java/org/springframework/oxm/castor/*
# fix hessian aId
sed -i "s|<artifactId>com.springsource.com.caucho|<artifactId>hessian|" org.springframework.web/pom.xml
# not available build desp
rm -rf org.springframework.orm/src/main/java/org/springframework/orm/hibernate4/*
rm -rf org.springframework.orm/src/main/java/org/springframework/orm/ibatis/*

# Put the dummy root POM in place:
cp %{SOURCE1} pom.xml


%build

# Build without the tests, as they bring a lot of dependecies that are not
# available in the distribution at the moment:
mvn-rpmbuild \
  -Dproject.build.sourceEncoding=ISO-8859-1 \
  -Dmaven.local.depmap.file="%{SOURCE2}" \
  -Dmaven.test.skip=true \
  install \
  javadoc:aggregate


%install

# Install jar and POM files:
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}
while read module_name artifact_id
do
  pom_file="${module_name}/pom.xml"
  jar_file="${module_name}/target/${artifact_id}-%{version}.RELEASE.jar"
  depmap_suffix=${artifact_id#spring-}
  install -p -m 644 ${pom_file} %{buildroot}%{_mavenpomdir}/JPP.%{name}-${artifact_id}.pom
  if [ -f "${jar_file}" ]
  then
    install -p -m 644 ${jar_file} %{buildroot}%{_javadir}/%{name}/${artifact_id}.jar
    %add_maven_depmap JPP.%{name}-${artifact_id}.pom %{name}/${artifact_id}.jar -f "${depmap_suffix}"
  else
    %add_maven_depmap JPP.%{name}-${artifact_id}.pom -f "${depmap_suffix}"
  fi
done <<'.'
org.springframework.spring-parent spring-parent
org.springframework.aop spring-aop
org.springframework.beans spring-beans
org.springframework.context spring-context
org.springframework.core spring-core
org.springframework.expression spring-expression
org.springframework.instrument spring-instrument
org.springframework.jdbc spring-jdbc
org.springframework.transaction spring-tx
org.springframework.context.support spring-context-support
org.springframework.oxm spring-oxm
org.springframework.web spring-web
org.springframework.jms spring-jms
org.springframework.orm spring-orm
org.springframework.web.servlet spring-webmvc
org.springframework.web.portlet spring-webmvc-portlet
org.springframework.web.struts spring-struts
.

# Install javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/.


%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/spring-core.jar
%{_mavendepmapfragdir}/%{name}-parent
%{_mavendepmapfragdir}/%{name}-core
%{_mavenpomdir}/JPP.%{name}-spring-parent.pom
%{_mavenpomdir}/JPP.%{name}-spring-core.pom
%doc build-spring-framework/resources/*


%files javadoc
%{_javadocdir}/%{name}
%doc build-spring-framework/resources/license.txt


%files aop
%{_mavendepmapfragdir}/%{name}-aop
%{_mavenpomdir}/JPP.%{name}-spring-aop.pom
%{_javadir}/%{name}/spring-aop.jar


%files beans
%{_mavendepmapfragdir}/%{name}-beans
%{_javadir}/%{name}/spring-beans.jar
%{_mavenpomdir}/JPP.%{name}-spring-beans.pom


%files context
%{_mavendepmapfragdir}/%{name}-context
%{_javadir}/%{name}/spring-context.jar
%{_mavenpomdir}/JPP.%{name}-spring-context.pom


%files context-support
%{_javadir}/%{name}/spring-context-support.jar
%{_mavenpomdir}/JPP.%{name}-spring-context-support.pom
%{_mavendepmapfragdir}/%{name}-context-support


%files expression
%{_mavendepmapfragdir}/%{name}-expression
%{_javadir}/%{name}/spring-expression.jar
%{_mavenpomdir}/JPP.%{name}-spring-expression.pom


%files instrument
%{_mavendepmapfragdir}/%{name}-instrument
%{_javadir}/%{name}/spring-instrument.jar
%{_mavenpomdir}/JPP.%{name}-spring-instrument.pom


%files jdbc
%{_mavendepmapfragdir}/%{name}-jdbc
%{_javadir}/%{name}/spring-jdbc.jar
%{_mavenpomdir}/JPP.%{name}-spring-jdbc.pom


%files jms
%{_javadir}/%{name}/spring-jms.jar
%{_mavenpomdir}/JPP.%{name}-spring-jms.pom
%{_mavendepmapfragdir}/%{name}-jms


%files orm
%{_javadir}/%{name}/spring-orm.jar
%{_mavenpomdir}/JPP.%{name}-spring-orm.pom
%{_mavendepmapfragdir}/%{name}-orm

%files oxm
%{_javadir}/%{name}/spring-oxm.jar
%{_mavenpomdir}/JPP.%{name}-spring-oxm.pom
%{_mavendepmapfragdir}/%{name}-oxm


%files struts
%{_javadir}/%{name}/spring-struts.jar
%{_mavenpomdir}/JPP.%{name}-spring-struts.pom
%{_mavendepmapfragdir}/%{name}-struts


%files tx
%{_mavendepmapfragdir}/%{name}-tx
%{_javadir}/%{name}/spring-tx.jar
%{_mavenpomdir}/JPP.%{name}-spring-tx.pom


%files web
%{_javadir}/%{name}/spring-web.jar
%{_mavenpomdir}/JPP.%{name}-spring-web.pom
%{_mavendepmapfragdir}/%{name}-web


%files webmvc
%{_javadir}/%{name}/spring-webmvc.jar
%{_mavenpomdir}/JPP.%{name}-spring-webmvc.pom
%{_mavendepmapfragdir}/%{name}-webmvc


%files webmvc-portlet
%{_javadir}/%{name}/spring-webmvc-portlet.jar
%{_mavenpomdir}/JPP.%{name}-spring-webmvc-portlet.pom
%{_mavendepmapfragdir}/%{name}-webmvc-portlet


%changelog
* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1.1-alt1_10jpp7
- first build
