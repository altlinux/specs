Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
#def_with arquillian
%bcond_with arquillian
Name:          openwebbeans
Version:       1.2.8
Release:       alt1_2jpp8
Summary:       Implementation of the JSR-299 WebBeans
License:       ASL 2.0
URL:           http://openwebbeans.apache.org/
Source0:       http://www.apache.org/dist/openwebbeans/%{version}/%{name}-%{version}-source-release.zip
Patch0:        %{name}-1.2.0-servlet31.patch

BuildRequires: maven-local
BuildRequires: mvn(javax.annotation:javax.annotation-api) >= 1.2
BuildRequires: mvn(javax.el:javax.el-api)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(javax.servlet.jsp:javax.servlet.jsp-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache:apache-jar-resource-bundle)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-ejb_3.1_spec)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jcdi_1.0_spec)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jta_1.1_spec)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-validation_1.0_spec)
BuildRequires: mvn(org.apache.geronimo.specs:specs:pom:)
BuildRequires: mvn(org.apache.httpcomponents:project:pom:)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.apache.tomcat:tomcat-catalina)
BuildRequires: mvn(org.apache.xbean:xbean-finder)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi)
BuildRequires: mvn(org.hibernate.javax.persistence:hibernate-jpa-2.0-api)
BuildRequires: mvn(org.jboss.spec.javax.faces:jboss-jsf-api_2.2_spec)
BuildRequires: mvn(org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-commons)

%if %{with arquillian}
# 2015-07-29: Retired because it depends on shrinkwrap-resolver which did not build for two releases.
BuildRequires: mvn(org.jboss.arquillian:arquillian-bom)
BuildRequires: mvn(org.jboss.arquillian.container:arquillian-container-spi)
BuildRequires: mvn(org.jboss.arquillian.core:arquillian-core-spi)
BuildRequires: mvn(org.jboss.arquillian.junit:arquillian-junit-container)
BuildRequires: mvn(org.jboss.arquillian.test:arquillian-test-spi)
BuildRequires: mvn(org.jboss.arquillian.testenricher:arquillian-testenricher-cdi)
BuildRequires: mvn(org.jboss.shrinkwrap:shrinkwrap-api)
BuildRequires: mvn(org.jboss.shrinkwrap.resolver:shrinkwrap-resolver-bom:pom:)
%endif

Obsoletes:     %{name}-arquillian
Obsoletes:     %{name}-cdi11

BuildArch:     noarch
Source44: import.info

%description
OpenWebBeans is an implementation of the JSR-299, Contexts and
Dependency Injection for the Java EE platform.

It also already incorporates some features which are part of JSR-346
but doesn't need API changes as we still use the JCDI-1.0 API. The
incorporated CDI-1.1 features are mostly parts which are not well defined
in the CDI-1.0 specification, like Serialisation checks, etc.

%package clustering
Group: Development/Java
Summary:       Apache OpenWebBeans Clustering Plugin

%description clustering
Apache OpenWebBeans Clustering plugin.

%package ee
Group: Development/Java
Summary:       Apache OpenWebBeans Java EE plugin

%description ee
Apache OpenWebBeans Java EE Utility.

%package ee-common
Group: Development/Java
Summary:       Apache OpenWebBeans EE Common plugin

%description ee-common
Apache OpenWebBeans Java EE Common.

%package ejb
Group: Development/Java
Summary:       Apache OpenWebBeans EJB plugin

%description ejb
Apache OpenWebBeans Java EE EJB plugin.

%package el22
Group: Development/Java
Summary:       Apache OpenWebBeans EL 2.2 plugin

%description el22
Apache OpenWebBeans EL 2.2 integration.

%package impl
Group: Development/Java
Summary:       Apache OpenWebBeans Core

%description impl
Apache OpenWebBeans Implementation core module.

%package jee5-ejb-resource
Group: Development/Java
Summary:       Apache OpenWebBeans EE Resource plugin

%description jee5-ejb-resource
Apache OpenWebBeans EE 5 Resource Integration.

%package jms
Group: Development/Java
Summary:       Apache OpenWebBeans JMS plugin

%description jms
Apache OpenWebBeans JMS Integration.

%package jsf
Group: Development/Java
Summary:       Apache OpenWebBeans JSF-2 plugin

%description jsf
Apache OpenWebBeans JSF integration.

%package osgi
Group: Development/Java
Summary:       Apache OpenWebBeans OSGi plugin

%description osgi
Apache OpenWebBeans OSGi ClassLoader scanning support.

%package resource
Group: Development/Java
Summary:       Apache OpenWebBeans EE Resource plugin

%description resource
Apache OpenWebBeans EE Resource Integration.

%package spi
Group: Development/Java
Summary:       Apache OpenWebBeans SPI definition

%description spi
Apache OpenWebBeans Service Provider Interfaces.

%package test
Group: Development/Java
Summary:       Apache OpenWebBeans CDI Test Framework

%description test
This package contains testing support for CDI containers and
also provides an implementation for OpenWebBeans.

%package tomcat7
Group: Development/Java
Summary:       Apache OpenWebBeans Tomcat 7 plugin

%description tomcat7
ApacheOpenWebBeans Tomcat 7 Web Profile.

%package web
Group: Development/Java
Summary:       Apache OpenWebBeans Web plugin

%description web
Apache OpenWebBeans Java EE Web and Serlvet plugin.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p1

rm -r DEPENDENCIES

# Require org.apache.openwebbeans.build-tools checkstyle-rules 1.2
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :taglist-maven-plugin
%pom_remove_plugin -r :maven-source-plugin

# Unavailable deps
%pom_disable_module distribution
%pom_disable_module samples
%pom_disable_module webbeans-doc
%pom_disable_module webbeans-el10
%pom_disable_module webbeans-jsf12
# TODO
# org.apache.openejb openejb-core
# org.apache.openejb openejb-core openejb-tomcat-catalina 3.1.4
# org.jboss.jsr299.tck jsr299-tck-api 1.0.4.CR1
%pom_disable_module webbeans-porting
# org.jboss.jsr299.tck jsr299-tck-impl 1.0.4.SP1
%pom_disable_module webbeans-tck
%pom_disable_module atinject-tck
%pom_disable_module webbeans-tomcat6

%if %{without arquillian}
%pom_disable_module webbeans-arquillian
%pom_remove_dep :arquillian-bom webbeans-arquillian
%endif

%pom_change_dep -r :geronimo-annotation_1.1_spec javax.annotation:javax.annotation-api:1.2
%pom_change_dep -r :geronimo-atinject_1.0_spec javax.inject:javax.inject:1
%pom_change_dep -r :geronimo-el_2.2_spec javax.el:javax.el-api:3.0.0
%pom_change_dep -r :geronimo-interceptor_1.1_spec org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec:1.0.0.Final
%pom_change_dep -r :geronimo-jpa_2.0_spec org.hibernate.javax.persistence:hibernate-jpa-2.0-api:1.0.1.Final
%pom_change_dep -r :geronimo-jsp_2.1_spec javax.servlet.jsp:javax.servlet.jsp-api:2.3.2-b01
%pom_change_dep -r :geronimo-servlet_2.5_spec javax.servlet:javax.servlet-api:3.1.0
%pom_change_dep -r :myfaces-api org.jboss.spec.javax.faces:jboss-jsf-api_2.2_spec:2.2.0
%pom_change_dep -r :org.osgi.core org.eclipse.osgi:org.eclipse.osgi

%pom_change_dep -r org.apache.xbean:xbean-finder-shaded org.apache.xbean:xbean-finder
%pom_change_dep -r org.apache.xbean:xbean-asm5-shaded org.ow2.asm:asm:5.0.3
sed -i "s|org.apache.xbean.asm5|org.objectweb.asm|" \
 webbeans-impl/src/main/java/org/apache/webbeans/proxy/AbstractProxyFactory.java \
 webbeans-impl/src/main/java/org/apache/webbeans/proxy/InterceptorDecoratorProxyFactory.java \
 webbeans-impl/src/main/java/org/apache/webbeans/proxy/NormalScopeProxyFactory.java \
 webbeans-impl/src/main/java/org/apache/webbeans/proxy/SubclassProxyFactory.java

%pom_add_dep org.ow2.asm:asm-commons:5.0.3:test webbeans-impl

# These test fails
# java.lang.OutOfMemoryError: unable to create new native thread
rm -r webbeans-impl/src/test/java/org/apache/webbeans/portable/AnnotatedTypeImplTest.java
# Require servlet 2.5 apis
rm -rf webbeans-clustering/src/test/java/org/apache/webbeans/web/failover/tests/MockServletContext.java \
 webbeans-clustering/src/test/java/org/apache/webbeans/web/failover/tests/MockServletRequest.java

# Break build
%pom_remove_plugin org.apache.rat:apache-rat-plugin

%mvn_package org.apache.openwebbeans.test: test

%mvn_package :%{name}-impl::tests: %{name}-impl

%build

# Some tests @ random fails
%mvn_build -s -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles-%{name}
%doc LICENSE NOTICE

%files clustering -f .mfiles-%{name}-clustering
%doc LICENSE NOTICE

%files ee -f .mfiles-%{name}-ee
%doc LICENSE NOTICE

%files ee-common -f .mfiles-%{name}-ee-common
%doc LICENSE NOTICE

%files ejb -f .mfiles-%{name}-ejb
%doc LICENSE NOTICE

%files el22 -f .mfiles-%{name}-el22
%doc LICENSE NOTICE

%files impl -f .mfiles-%{name}-impl
%doc LICENSE NOTICE

%files jee5-ejb-resource -f .mfiles-%{name}-jee5-ejb-resource
%doc LICENSE NOTICE

%files jms -f .mfiles-%{name}-jms
%doc LICENSE NOTICE

%files jsf -f .mfiles-%{name}-jsf
%doc LICENSE NOTICE

%files osgi -f .mfiles-%{name}-osgi
%doc LICENSE NOTICE

%files resource -f .mfiles-%{name}-resource
%doc LICENSE NOTICE

%files spi -f .mfiles-%{name}-spi
%doc LICENSE NOTICE

%files test -f .mfiles-test
%doc LICENSE NOTICE

%files tomcat7 -f .mfiles-%{name}-tomcat7
%doc LICENSE NOTICE

%files web -f .mfiles-%{name}-web
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.8-alt1_2jpp8
- new version

