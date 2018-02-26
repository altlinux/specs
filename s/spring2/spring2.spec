ExclusiveArch: x86_64
BuildRequires: avalon-framework
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
%define version 2.5.6.SEC03
%define name spring2
# Copyright (c) 2000-2012, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%if 0
FIXME: (dwalluck): Need to link offline:
  [javadoc] javadoc: warning - Error fetching URL: http://java.sun.com/javase/6/docs/api/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://java.sun.com/j2ee/1.4/docs/api/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://aopalliance.sourceforge.net/doc/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://cglib.sourceforge.net/apidocs/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://ehcache.sourceforge.net/apidocs/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://freemarker.sourceforge.net/docs/api/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://www.hibernate.org/hib_docs/v3/api/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://jakarta.apache.org/commons/collections/apidocs-COLLECTIONS_3_0/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://jakarta.apache.org/commons/dbcp/apidocs/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://jakarta.apache.org/commons/fileupload/apidocs/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://jakarta.apache.org/commons/httpclient/apidocs/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://jakarta.apache.org/commons/logging/apidocs/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://jakarta.apache.org/commons/pool/apidocs/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://junit.sourceforge.net/javadoc_40/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://logging.apache.org/log4j/docs/api/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://jakarta.apache.org/regexp/apidocs/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://jakarta.apache.org/poi/apidocs/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://portals.apache.org/pluto/multiproject/portlet-api/apidocs/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://www.opensymphony.com/quartz/api/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://struts.apache.org/struts-doc-1.2.9/api/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://java.sun.com/javase/6/docs/jre/api/net/httpserver/spec/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://tiles.apache.org/framework/apidocs/package-list
  [javadoc] javadoc: warning - Error fetching URL: http://velocity.apache.org/engine/devel/apidocs/package-list
%endif

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with gcj_support
%bcond_with gcj_support
#def_with nodeps
%bcond_with nodeps
%bcond_without repolib
#def_with xmlgraphics
%bcond_with xmlgraphics
#def_with zips
%bcond_with zips

%define repodir %{_javadir}/repository.jboss.com/org/springframework/%{upstream_version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define bname   spring

%define upstream_tag .SEC03
%define upstream_version %{version}%{?upstream_tag}

Name:           spring2
Summary:        Spring J2EE Framework
Version:        2.5.6.SEC03
Release:        alt4_5jpp6
Epoch:          0
License:        ASL 2.0
Group:          Development/Java
URL:            http://www.springframework.org/
# svn -q export https://src.springframework.org/svn/spring-maintenance/tags/release-2-5-6-SEC03/ spring2-2.5.6.SEC03 && tar cjf spring2-2.5.6.SEC03.tar.bz2 spring2-2.5.6.SEC03
Source0:        %{name}-%{version}.tar.bz2
Source1:        http://static.springframework.org/spring/files/docbook-reference-libs.zip
Source2:        spring2-component-info.xml
Patch0:         spring-2.5.1-WorkManagerTaskExecutor.patch
Patch1:         spring-2.5.5-SqlMapClientFactoryBean.patch
Patch2:         spring-2.5.1-HibernateJpaDialect.patch
Patch3:         spring-2.5.1-DefaultContextLoadTimeWeaver.patch
Patch4:         spring-2.5.6-build.patch
Patch5:         spring-2.5.1-PathMatchingResourcePatternResolverTests.patch
Patch6:         spring-2.5.1-TopLinkTransactionManager.patch
Patch8:         spring-2.5.1-JRubyScriptUtils.patch
Patch9:         spring-2.5.5-quartz-1.6.0-SchedulerFactoryBean.patch
Patch10:        spring-2.5.5-HibernateJpaVendorAdapter.patch
Patch11:        spring-2.5.5-TilesViewTests.patch
Patch12:        spring-2.5.6-doc-pdf.patch
Patch13:        spring2-2.5.6-xmlgraphics-fop.patch
Patch14:        spring2-2.5.6-build-no-link.patch
Patch15:        spring2-2.5.6-asm.patch
Patch16:        spring2-2.5.6-LocalVariableTableParameterNameDiscoverer.patch
Patch17:        spring2-BshScriptUtils.patch
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  ant-trax >= 0:1.6.5
BuildRequires:  ant-junit >= 0:1.6.5
BuildRequires:  ant-nodeps >= 0:1.6.5
BuildRequires:  junit
BuildRequires:  junit-addons
BuildRequires:  junit44 >= 0:4.4
BuildRequires:  antlr
BuildRequires:  excalibur-avalon-framework
BuildRequires:  saxon
BuildRequires:  spring-build-aws-ant

#BuildRequires:  activemq3
BuildRequires:  annotation_1_0_api
BuildRequires:  aopalliance
BuildRequires:  apache-ibatis2-sqlmap
BuildRequires:  apache-jdo-2.0-api
BuildRequires:  openjpa >= 0:1.0.1
#BuildRequires:  aqute-bndlib
BuildRequires:  asm
BuildRequires:  asm2
BuildRequires:  aspectj >= 0:1.5.3
BuildRequires:  axis
BuildRequires:  backport-util-concurrent >= 0:3.1
BuildRequires:  bsh2
BuildRequires:  burlap >= 0:3.0.8
BuildRequires:  c3p0 >= 0:0.9.0
BuildRequires:  cglib21
BuildRequires:  commonj_1_1_apis
BuildRequires:  dom4j
BuildRequires:  easymock
BuildRequires:  easymock-classextension
BuildRequires:  ecj3
BuildRequires:  ehcache >= 0:1.3.0
BuildRequires:  ejb_3_0_api
BuildRequires:  el_1_0_api
%if %with xmlgraphics
BuildRequires:  xmlgraphics-fop
%endif
BuildRequires:  freemarker
BuildRequires:  geronimo-interceptor-3.0-api
BuildRequires:  glassfish-jstl
BuildRequires:  glassfish-persistence-impl
BuildRequires:  groovy15
BuildRequires:  hessian-nodep
BuildRequires:  hibernate3 >= 0:3.3.2
BuildRequires:  hibernate3-annotations
BuildRequires:  hibernate3-commons-annotations
BuildRequires:  hibernate3-entitymanager
BuildRequires:  hsqldb
BuildRequires:  httpunit
BuildRequires:  itext
BuildRequires:  j2ee_connector_1_5_api
BuildRequires:  jaf_1_1_api
BuildRequires:  jakarta-cactus
BuildRequires:  apache-commons-attributes
BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-dbcp
BuildRequires:  apache-commons-digester
BuildRequires:  apache-commons-discovery
BuildRequires:  apache-commons-fileupload
BuildRequires:  apache-commons-httpclient
BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-lang
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-pool
BuildRequires:  apache-commons-validator
BuildRequires:  jakarta-taglibs-standard
BuildRequires:  jamonapi
BuildRequires:  jarjar
BuildRequires:  jasperreports2 >= 0:2.0.4
BuildRequires:  jta_1_1_api
BuildRequires:  glassfish-javamail >= 0:1.4.0
BuildRequires:  jaxb_2_1_api
BuildRequires:  jaxen
BuildRequires:  jaxrpc_1_1_api
BuildRequires:  jaxws_2_1_api
BuildRequires:  jboss4-common
BuildRequires:  jdom
BuildRequires:  jets3t
BuildRequires:  jexcelapi
BuildRequires:  jmock
BuildRequires:  jms_1_1_api
BuildRequires:  jotm
BuildRequires:  jpa_3_0_api
BuildRequires:  jruby >= 0:1.1.1
BuildRequires:  jruby-bytelist
BuildRequires:  jsp_2_0_api
BuildRequires:  jta_1_0_1B_api
BuildRequires:  apache-poi >= 0:2.5.1
BuildRequires:  log4j
BuildRequires:  jsf_1_2_api
BuildRequires:  mx4j >= 0:3.0.1-2jpp
BuildRequires:  ognl
BuildRequires:  portlet-1.0-api
#BuildRequires:  qdox15 >= 0:1.5
BuildRequires:  quartz16
BuildRequires:  saaj_1_3_api
BuildRequires:  serp
BuildRequires:  servlet_2_4_api
BuildRequires:  slf4j
BuildRequires:  struts >= 0:1.3.8
BuildRequires:  struts-tiles >= 0:1.3.8
BuildRequires:  testng
BuildRequires:  objenesis
BuildRequires:  jcommander
BuildRequires:  jtidy
BuildRequires:  tiles
BuildRequires:  tomcat5
BuildRequires:  unzip
# XXX: (dwalluck): brew is 1.4;  upstream is velocity-1.5
BuildRequires:  velocity >= 0:1.5
# XXX: (dwalluck): brew is 1.2; upstream is velocity-tools-view-1.4
BuildRequires:  velocity-tools
BuildRequires:  ws_metadata_2_0_api
BuildRequires:  wsdl4j16
BuildRequires:  xapool
BuildRequires:  xjavadoc
BuildRequires:  xerces-j2


Requires(post):    jpackage-utils >= 0:1.7.3
Requires(postun):  jpackage-utils >= 0:1.7.3
%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
%endif

%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info

%description
Spring is a layered Java/J2EE application framework, 
based on code published in Expert One-on-One J2EE 
Design and Development by Rod Johnson (Wrox, 2002). 

%package core
Summary:        Spring core
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
%if %without nodeps
Requires:       asm2
Requires:       backport-util-concurrent >= 0:3.0
Requires:       apache-commons-collections
Requires:       apache-commons-logging
Requires:       log4j
%endif

%description core
Spring bean container, core utilities
Optionals: log4j

%package aspects
Summary:        Spring aspects
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-beans = %{epoch}:%{version}-%{release}
Requires:       %{name}-tx = %{epoch}:%{version}-%{release}
%if %without nodeps
Requires:       aspectj >= 0:1.2.1
Requires:       apache-commons-logging
%endif

%description aspects
Spring AOP aspects, source level metadata support
Optionals: cglib21, apache-commons-attributes

%package aop
Summary:        Spring aop
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-beans = %{epoch}:%{version}-%{release}
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
%if %without nodeps
Requires:       aopalliance
Requires:       aspectj >= 0:1.5.3
Requires:       cglib21
Requires:       apache-commons-attributes
Requires:       apache-commons-pool
Requires:       jamonapi
Requires:       apache-commons-logging
%endif

%description aop
Spring AOP framework, source level metadata support
Optionals: cglib21, apache-commons-attributes

%package agent
Summary:        Spring aop
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
%if %without nodeps
Requires:       aopalliance
%endif

%description agent
Spring AOP agent, source level metadata support
Optionals: cglib21, apache-commons-attributes


%package beans
Summary:        Spring beans
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
%if %without nodeps
Requires:       cglib21
Requires:       apache-commons-logging
%endif

%description beans
%{summary}.

%package context
Summary:        Spring context
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-agent = %{epoch}:%{version}-%{release}
Requires:       %{name}-aop = %{epoch}:%{version}-%{release}
Requires:       %{name}-beans = %{epoch}:%{version}-%{release}
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
%if %without nodeps
Requires:       aopalliance
%if 0
Requires:       backport-util-concurrent
%endif
Requires:       apache-commons-logging
Requires:       commonj_1_1_apis
Requires:       ejb_3_0_api
Requires:       jms_1_1_api
%if 0
Requires:       jaxrpc_1_1_api
%endif
%endif

%description context
Spring application context, validation, UI support, mail,
JNDI, JMS, EJB, remoting, scheduling, caching
Optionals: velocity, freemarker, javamail, jms, ejb, axis,
hessian, burlap, quartz, ehcache

%package context-support
Summary:        Spring context-support
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-aop = %{epoch}:%{version}-%{release}
Requires:       %{name}-beans = %{epoch}:%{version}-%{release}
Requires:       %{name}-context = %{epoch}:%{version}-%{release}
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-jdbc = %{epoch}:%{version}-%{release}
Requires:       %{name}-tx = %{epoch}:%{version}-%{release}
%if %without nodeps
Requires:       aopalliance
Requires:       bsh2
Requires:       cglib21
Requires:       commonj_1_1_apis
Requires:       freemarker
Requires:       ehcache >= 0:1.3.0
Requires:       groovy15
Requires:       jaf_1_1_api
Requires:       apache-commons-collections
Requires:       apache-commons-logging
Requires:       jasperreports2 >= 0:2.0.4
Requires:       javamail_1_4_api
Requires:       jruby >= 0:1.1.1
Requires:       quartz16
Requires:       velocity
Requires:       velocity-tools
%endif

%description context-support
Spring context support, transaction infrastructure, JDBC support
Optionals: spring-aop, jta

%package jms
Summary:        Spring jms
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-beans = %{epoch}:%{version}-%{release}
Requires:       %{name}-context = %{epoch}:%{version}-%{release}
Requires:       %{name}-context-support = %{epoch}:%{version}-%{release}
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-tx = %{epoch}:%{version}-%{release}
%if %without nodeps
Requires:       apache-commons-logging
Requires:       apache-commons-pool
Requires:       jms_1_1_api
%endif

%description jms
%{summary}.

%package jdbc
Summary:        Spring jdbc
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-beans = %{epoch}:%{version}-%{release}
Requires:       %{name}-context = %{epoch}:%{version}-%{release}
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-tx = %{epoch}:%{version}-%{release}
%if %without nodeps
Requires:       c3p0
Requires:       apache-commons-dbcp
Requires:       apache-commons-logging
Requires:       jotm
%endif

%description jdbc
%{summary}.

%package orm
Summary:        Spring orm
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-aop = %{epoch}:%{version}-%{release}
Requires:       %{name}-beans = %{epoch}:%{version}-%{release}
Requires:       %{name}-context = %{epoch}:%{version}-%{release}
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-jdbc = %{epoch}:%{version}-%{release}
Requires:       %{name}-tx = %{epoch}:%{version}-%{release}
Requires:       %{name}-web = %{epoch}:%{version}-%{release}
%if %without nodeps
Requires:       aopalliance
Requires:       apache-jdo-2.0-api
Requires:       apache-ibatis2-sqlmap
Requires:       jpa_3_0_api
Requires:       hibernate3
Requires:       hibernate3-entitymanager
Requires:       jpa_3_0_api
Requires:       apache-commons-logging
%endif

%description orm
Spring Hibernate support, JDO support, Apache OJB, iBATIS SQL Maps
Optionals: hibernate, hibernate3, hibernate-annotations, 
apache-jdo-2.0-api, db-ojb, ibatis, j2ee-connector

%package test
Summary:        Spring test
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-beans = %{epoch}:%{version}-%{release}
Requires:       %{name}-context = %{epoch}:%{version}-%{release}
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-jdbc = %{epoch}:%{version}-%{release}
Requires:       %{name}-orm = %{epoch}:%{version}-%{release}
Requires:       %{name}-tx = %{epoch}:%{version}-%{release}
Requires:       %{name}-webmvc = %{epoch}:%{version}-%{release}
%if %without nodeps
Requires:       aspectj >= 0:1.5.3
Requires:       jpa_3_0_api
Requires:       jsp_2_0_api
Requires:       junit
Requires:       servlet_2_4_api
Requires:       apache-commons-logging
Requires:       jakarta-taglibs-standard
Requires:       portlet-1.0-api
%endif

%description test
%{summary}.

%package tomcat-weaver
Summary:        Spring tomcat weaver
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-context = %{epoch}:%{version}-%{release}
%if %without nodeps
# for tomcat5/naming-resources
Requires:       tomcat5-common-lib
# for tomcat5/catalina
Requires:       tomcat5-server-lib
%endif

%description tomcat-weaver
%{summary}.

%package tx
Summary:        Spring tx
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-aop = %{epoch}:%{version}-%{release}
Requires:       %{name}-beans = %{epoch}:%{version}-%{release}
Requires:       %{name}-context = %{epoch}:%{version}-%{release}
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
%if %without nodeps
Requires:       aopalliance
Requires:       j2ee_connector_1_5_api
Requires:       jta_1_1_api
Requires:       apache-commons-logging
Requires:       jotm
Requires:       xapool
%endif

%description tx
%{summary}.

%package web
Summary:        Spring web
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-beans = %{epoch}:%{version}-%{release}
Requires:       %{name}-context = %{epoch}:%{version}-%{release}
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
%if %without nodeps
Requires:       axis
Requires:       hessian-nodep
Requires:       apache-commons-beanutils
Requires:       apache-commons-fileupload
Requires:       apache-commons-logging
Requires:       jakarta-taglibs-standard
Requires:       apache-commons-httpclient
Requires:       jsp_2_0_api
Requires:       servlet_2_4_api
Requires:       log4j
Requires:       jsf_1_1_api
Requires:       struts >= 0:1.3.8
Requires:       struts-tiles >= 0:1.3.8
%endif

%description web
Spring web application support, multipart resolver, struts support,
web utilities
Optionals: jspapi, jakarta-taglibs-standard, apache-commons-fileupload,
struts

%package webmvc
Summary:        Spring webmvc
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-beans = %{epoch}:%{version}-%{release}
Requires:       %{name}-context = %{epoch}:%{version}-%{release}
Requires:       %{name}-context-support = %{epoch}:%{version}-%{release}
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-web = %{epoch}:%{version}-%{release}
%if %without nodeps
Requires:       freemarker
Requires:       itext
Requires:       apache-commons-attributes
Requires:       apache-poi
Requires:       apache-commons-logging
Requires:       jakarta-taglibs-standard
Requires:       jasperreports2 >= 0:2.0.2
Requires:       jexcelapi
Requires:       jsp_2_0_api
Requires:       servlet_2_4_api
Requires:       tiles
Requires:       velocity
Requires:       velocity-tools
%endif

%description webmvc
Spring framework servlets, web MVC framework, web controllers, web views
Optionals: tiles, itext, poi

%package webmvc-portlet
Summary:        Spring webmvc-portlet
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-beans = %{epoch}:%{version}-%{release}
Requires:       %{name}-context = %{epoch}:%{version}-%{release}
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-web = %{epoch}:%{version}-%{release}
Requires:       %{name}-webmvc = %{epoch}:%{version}-%{release}
%if %without nodeps
Requires:       apache-commons-fileupload
Requires:       apache-commons-logging
Requires:       jsp_2_0_api
Requires:       portlet-1.0-api
%endif

%description webmvc-portlet
Spring framework portlet support
Optionals: tiles, itext, poi

%package webmvc-struts
Summary:        Spring webmvc-struts
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-beans = %{epoch}:%{version}-%{release}
Requires:       %{name}-context = %{epoch}:%{version}-%{release}
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-web = %{epoch}:%{version}-%{release}
Requires:       %{name}-webmvc = %{epoch}:%{version}-%{release}
%if %without nodeps
Requires:       apache-commons-logging
Requires:       jakarta-taglibs-standard
Requires:       jsp_2_0_api
Requires:       servlet_2_4_api
Requires:       tiles
Requires:       struts >= 0:1.3.8
%endif

%description webmvc-struts
Spring framework struts support
Optionals: tiles, itext, poi

%package all
Summary:        Spring all except mocks
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
%if %without nodeps
Requires:       aopalliance
# XXX: (dwalluck): We are building against but not shipping these two
Requires:       apache-ibatis2-sqlmap
Requires:       apache-jdo-2.0-api
Requires:       asm2
Requires:       aspectj >= 0:1.5.3
Requires:       axis
Requires:       backport-util-concurrent >= 0:3.0
Requires:       bsh2
Requires:       c3p0
Requires:       cglib21
Requires:       commonj_1_1_apis
Requires:       ehcache >= 0:1.3.0
Requires:       ejb_3_0_api
Requires:       freemarker
Requires:       jpa_3_0_api
Requires:       groovy15
Requires:       hessian-nodep
Requires:       hibernate3
Requires:       hibernate3-entitymanager
Requires:       itext
Requires:       j2ee_connector_1_5_api
Requires:       apache-commons-attributes
Requires:       apache-commons-dbcp
Requires:       apache-commons-httpclient
Requires:       apache-commons-pool
Requires:       jakarta-oro
Requires:       apache-poi
Requires:       jamonapi
Requires:       jaf_1_1_api
Requires:       apache-commons-beanutils
Requires:       apache-commons-collections
Requires:       apache-commons-fileupload
Requires:       apache-commons-logging
Requires:       jakarta-taglibs-standard
Requires:       javamail_1_4_api
Requires:       jaxrpc_1_1_api
Requires:       jexcelapi
Requires:       jpa_3_0_api
Requires:       jms_1_1_api
Requires:       jotm
Requires:       jruby >= 0:1.1.1
Requires:       jsp_2_0_api
Requires:       jta_1_1_api
Requires:       junit
Requires:       quartz16
Requires:       servlet_2_4_api
Requires:       tiles
Requires:       tomcat5
Requires:       velocity
Requires:       velocity-tools
Requires:       jsf_1_1_api
Requires:       log4j
Requires:       portlet-1.0-api
Requires:       struts >= 0:1.3.8
Requires:       xapool
%endif

%description all
Spring everything except mocks
Optionals: log4j, cglib21, apache-commons-attributes
velocity, freemarker, javamail, jms, ejb, axis, hessian, 
burlap, quartz, ehcache, jta, hibernate, hibernate3, 
hibernate-annotations, apache-jdo-2.0-api, ojb, ibatis,
jspapi, jakarta-taglibs-standard, apache-commons-fileupload,
tiles, itest, poi

#%package mock
#Summary:        Spring mock
#Group:          Development/Libraries/Application Frameworks
#Requires:       %{name} = %{epoch}:%{version}-%{release}
#Requires:       %{name}-core = %{epoch}:%{version}-%{release}
#
#%description mock
#Spring JNDI mocks, Servlet API mocks

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
Requires:       %{name}-javadoc = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description manual
%{summary}.

%package demo
Summary:        Samples for %{name}
Group:          Development/Documentation
Requires:       %{name} = %{epoch}:%{version}-%{release}
%if %without nodeps
Requires:       antlr
Requires:       axis
Requires:       dom4j
Requires:       jaxen
Requires:       hsqldb
Requires:       ehcache
%endif

%description demo
%{summary}.
Optionals: antlr, axis, dom4j, jaxen, ehcache, hsqldb

%package devel
Summary:        Source jars for %{name}
Group:          Development/Java

%description devel
%{summary}.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%if %with zips
%package zip
Summary:     Container for the zipped distribution of %{name}
Group:       Development/Java

%description zip
Container for the zipped distribution of %{name}.
%endif

%prep
%setup -q 
pushd docs/reference
unzip -qq %{SOURCE1}
popd
chmod -R go=u-w *
#find . -name "*.jar" -exec rm {} \;
for f in $(find . -name "*.jar"); do
    mv $f $f.no
done

for j in $(find test/org/springframework/orm/toplink -name "*.java"); do
    sed -i -e 's/oracle\.toplink\./oracle.toplink.essentials./g' $j
done
for j in $(find src/org/springframework/orm/toplink -name "*.java"); do
    sed -i -e 's/oracle\.toplink\./oracle.toplink.essentials./g' $j
done
for j in $(find src/org/springframework/orm/toplink -name "*.java"); do
    sed -i -e 's/oracle\.toplink\.essentials\.sessions\.SessionLog/oracle.toplink.essentials.logging.SessionLog/' $j
    sed -i -e 's/oracle\.toplink\.essentials\.sessions\.DefaultSessionLog/oracle.toplink.essentials.logging.DefaultSessionLog/' $j
    sed -i -e 's/oracle\.toplink\.essentials\.publicinterface\.Session/oracle.toplink.essentials.sessions.Session/' $j
done
## SessionBroker not available in glassfish-persistence
rm src/org/springframework/orm/toplink/SessionBrokerSessionFactory.java
## sessions.xml support not available in glassfish-persistence ?
rm src/org/springframework/orm/toplink/LocalSessionFactory.java
rm src/org/springframework/orm/toplink/LocalSessionFactoryBean.java
## no specific 904 available
rm src/org/springframework/orm/toplink/support/CommonsLoggingSessionLog904.java
# cannot test unavailables
rm test/org/springframework/orm/toplink/SessionBrokerFactoryTests.java

# the following are test input files
mv tiger/test/order-supplemental.jar.no tiger/test/order-supplemental.jar
mv tiger/test/order.jar.no tiger/test/order.jar
mv tiger/test/org/springframework/orm/jpa/jpa-archive.jar.no tiger/test/org/springframework/orm/jpa/jpa-archive.jar

rm -rf tiger/src/org/springframework/instrument/classloading/oc4j/
rm -rf tiger/src/org/springframework/instrument/classloading/glassfish/
rm -f src/org/springframework/transaction/jta/WebSphereUowTransactionManager.java
rm -f test/org/springframework/transaction/jta/WebSphereUowTransactionManagerTests.java
rm -f test/org/springframework/transaction/jta/MockUOWManager.java

# tests with non free requires
rm tiger/test/org/springframework/instrument/classloading/glassfish/GlassFishLoadTimeWeaverTests.java
rm tiger/test/org/springframework/instrument/classloading/oc4j/OC4JClassPreprocessorAdapterTests.java
rm tiger/test/org/springframework/instrument/classloading/oc4j/OC4JLoadTimeWeaverTests.java

# requires bsh2 -> asm1 <--> asm2
rm test/org/springframework/scripting/bsh/BshScriptFactoryTests.java

# temp rm wait for newer hibernate3
rm tiger/test/org/springframework/orm/jpa/hibernate/HibernateMultiEntityManagerFactoryIntegrationTests.java

# temp rm wait for either openjpa or aspectj fix
####rm tiger/test/org/springframework/orm/jpa/openjpa/OpenJpaEntityManagerFactoryWithAspectJWeavingIntegrationTests.java

## !?! No tests found in org.springframework.test.context.SpringRunnerContextCacheTests ?!?
#rm tiger/test/org/springframework/test/context/SpringRunnerContextCacheTests.java
## see spring-2.5.1-SpringJUnit4SuiteTests.patch

## !?! No tests found in org.springframework.test.context.TestContextManagerTests ?!?
#rm tiger/test/org/springframework/test/context/TestContextManagerTests.java

## !?! No tests found in org.springframework.test.context.TestExecutionListenersTests ?!?
#rm tiger/test/org/springframework/test/context/TestExecutionListenersTests.java


%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5
%patch6 -b .sav6
%patch8 -b .sav8
#%%patch9 -b .sav9
%patch10 -b .sav10
%patch11 -b .sav11
%patch12 -b .sav12
%if %with xmlgraphics
%patch13 -b .sav13
%endif
%patch14 -b .sav14
%patch15 -b .sav15
%patch16 -b .sav16
%patch17 -b .sav17

rm tiger/src/org/springframework/orm/jpa/vendor/Eclipse*.java
rm tiger/test/org/springframework/orm/jpa/eclipselink/EclipseLinkEntityManagerFactoryIntegrationTests.java

# BUILD/spring/autobuilds/apps/jpetstore/lib/ibatis-common.jar.no
ln -sf $(build-classpath apache-ibatis2-common) autobuilds/apps/jpetstore/lib/ibatis-common.jar
# BUILD/spring/autobuilds/lib/ant-addons/path-to-fileset.jar.no

# BUILD/spring/autobuilds/lib/aspectj/aspectjrt-1.2.1.jar.no
ln -sf $(build-classpath aspectjrt) autobuilds/lib/aspectj/aspectjrt-1.2.1.jar
# BUILD/spring/autobuilds/lib/cactus/cactus-1.7.1.jar.no
ln -sf $(build-classpath cactus-14/cactus) autobuilds/lib/cactus/cactus-1.7.1.jar
# BUILD/spring/autobuilds/lib/cactus/cactus-ant-1.7.1.jar.no
ln -sf $(build-classpath cactus-14/cactus-ant) autobuilds/lib/cactus/cactus-ant-1.7.1.jar
# BUILD/spring/autobuilds/lib/cargo/cargo-0.6.jar.no

# BUILD/spring/autobuilds/lib/apache-commons/commons-httpclient-2.0.jar.no
ln -sf $(build-classpath commons-httpclient) autobuilds/lib/jakarta-commons/commons-httpclient-2.0.jar
# BUILD/spring/autobuilds/lib/junit-addons/junit-addons-1.4.jar.no
ln -sf $(build-classpath junit-addons) autobuilds/lib/junit-addons/junit-addons-1.4.jar
# BUILD/spring/docs/reference/lib/avalon-framework-cvs-20020806.jar.no
ln -sf $(build-classpath excalibur/avalon-framework) docs/reference/lib/avalon-framework-cvs-20020806.jar
# BUILD/spring/docs/reference/lib/batik.jar.no
%if %with xmlgraphics
ln -sf $(build-classpath batik-all) docs/reference/lib/batik.jar
%else
cp -p docs/reference/lib/batik.jar.no docs/reference/lib/batik.jar
%endif
# BUILD/spring/docs/reference/lib/fop.jar.no
%if %with xmlgraphics
ln -sf $(build-classpath xmlgraphics-fop) docs/reference/lib/fop.jar
%else
cp -p docs/reference/lib/fop.jar.no docs/reference/lib/fop.jar
# BUILD/spring/docs/reference/lib/jai_codec.jar.no
cp -p docs/reference/lib/jai_codec.jar.no docs/reference/lib/jai_codec.jar
# BUILD/spring/docs/reference/lib/jai_core.jar.no
cp -p docs/reference/lib/jai_core.jar.no docs/reference/lib/jai_core.jar
# BUILD/spring/docs/reference/lib/saxon-dbxsl-extensions.jar.no
cp -p docs/reference/lib/saxon-dbxsl-extensions.jar.no docs/reference/lib/saxon-dbxsl-extensions.jar
%endif
# BUILD/spring/docs/reference/lib/saxon.jar.no
ln -sf $(build-classpath saxon) docs/reference/lib/saxon.jar
# BUILD/spring/lib/activemq/activemq-1.1.jar.no
##ln -sf $(build-classpath activemq3) lib/activemq/activemq-1.1.jar
cp -p lib/activemq/activemq-1.1.jar.no lib/activemq/activemq-1.1.jar
# BUILD/spring/lib/ant/ant.jar.no
ln -sf $(build-classpath ant) lib/ant/ant.jar
# BUILD/spring/lib/ant/ant-junit.jar.no
ln -sf $(build-classpath ant/ant-junit) lib/ant/ant-junit.jar
# BUILD/spring/lib/ant/ant-launcher.jar.no
ln -sf $(build-classpath ant-launcher) lib/ant/ant-launcher.jar
# BUILD/spring/lib/ant/ant-trax.jar.no
ln -sf $(build-classpath ant/ant-trax) lib/ant/ant-trax.jar
# BUILD/spring/lib/antlr/antlr-2.7.6.jar.no
ln -sf $(build-classpath antlr) lib/antlr/antlr-2.7.6.jar
# BUILD/spring/lib/aopalliance/aopalliance.jar.no
ln -sf $(build-classpath aopalliance) lib/aopalliance/aopalliance.jar
# BUILD/spring/lib/asm/asm-2.2.3.jar.no
ln -sf $(build-classpath asm2/asm2) lib/asm/asm-2.2.3.jar
# BUILD/spring/lib/asm/asm-commons-2.2.3.jar.no
ln -sf $(build-classpath asm2/asm2-commons) lib/asm/asm-commons-2.2.3.jar
# BUILD/spring/lib/asm/asm-util-2.2.3.jar.no
ln -sf $(build-classpath asm2/asm2-util) lib/asm/asm-util-2.2.3.jar
# BUILD/spring/lib/aspectj/aspectjrt.jar.no
ln -sf $(build-classpath aspectjrt) lib/aspectj/aspectjrt.jar
# BUILD/spring/lib/aspectj/aspectjtools.jar.no
ln -sf $(build-classpath aspectjtools) lib/aspectj/aspectjtools.jar
# BUILD/spring/lib/aspectj/aspectjweaver.jar.no
ln -sf $(build-classpath aspectjweaver) lib/aspectj/aspectjweaver.jar
# BUILD/spring/lib/aws/spring-aws-ant.jar.no
ln -sf $(build-classpath spring-build/org.springframework.build.aws.ant) lib/aws/spring-aws-ant.jar
# BUILD/spring/lib/axis/axis.jar.no
ln -sf $(build-classpath axis/axis) lib/axis/axis.jar
# BUILD/spring/lib/axis/wsdl4j.jar.no
ln -sf $(build-classpath wsdl4j/wsdl4j16) lib/axis/wsdl4j.jar
# BUILD/spring/lib/bsh/bsh-2.0b4.jar.no
ln -sf $(build-classpath bsh2/bsh-core) lib/bsh/bsh-2.0b4.jar
## BUILD/spring/lib/bundlor/com.springsource.bundlor-1.0.0.M1.jar.no
## BUILD/spring/lib/bundlor/com.springsource.bundlor.ant-1.0.0.M1.jar.no
## BUILD/spring/lib/bundlor/com.springsource.org.antlr-3.0.1.jar.no
## BUILD/spring/lib/bundlor/com.springsource.org.apache.commons.cli-1.1.0.jar.no
## BUILD/spring/lib/bundlor/com.springsource.org.apache.commons.logging-1.1.1.jar.no
## BUILD/spring/lib/bundlor/com.springsource.org.apache.ws.commons.schema-1.3.2.jar.no
## BUILD/spring/lib/bundlor/com.springsource.org.objectweb.asm-3.1.0.jar.no
## BUILD/spring/lib/bundlor/com.springsource.org.objectweb.asm.commons-3.1.0.jar.no
## BUILD/spring/lib/bundlor/com.springsource.org.objectweb.asm.tree-3.1.0.jar.no
## BUILD/spring/lib/bundlor/com.springsource.server.osgi.manifest-1.0.0.BUILD-20080905115514.jar.no
## BUILD/spring/lib/bundlor/com.springsource.server.serviceability.ffdc-1.0.0.BUILD-20080905115514.jar.no
## BUILD/spring/lib/bundlor/com.springsource.server.serviceability.output-1.0.0.BUILD-20080905115514.jar.no
## BUILD/spring/lib/bundlor/com.springsource.server.serviceability.tracing-1.0.0.BUILD-20080905115514.jar.no
## BUILD/spring/lib/bundlor/com.springsource.slf4j.api-1.5.0.jar.no
## BUILD/spring/lib/bundlor/com.springsource.slf4j.org.apache.commons.logging-1.5.0.jar.no
## BUILD/spring/lib/bundlor/com.springsource.slf4j.org.apache.log4j-1.5.0.jar.no
## BUILD/spring/lib/bundlor/org.eclipse.osgi-3.4.0.v20080605-1900.jar.no
## BUILD/spring/lib/bundlor/org.springframework.beans-2.5.5.A.jar.no
## BUILD/spring/lib/bundlor/org.springframework.core-2.5.5.A.jar.no
## BUILD/spring/lib/bundlor/org.springframework.xml-1.5.2.A.jar.no
#mv lib/bundlor lib/bundlor-not-yet-available
for j in  lib/bundlor/*.jar.no; do
    on=$(echo $j | sed -e 's/\.no$//');
    mv $j $on
done

# BUILD/spring/lib/c3p0/c3p0-0.9.1.2.jar.no
ln -sf $(build-classpath c3p0) lib/c3p0/c3p0-0.9.1.2.jar
# BUILD/spring/lib/caucho/hessian-3.1.3.jar.no
ln -sf $(build-classpath hessian-nodep) lib/caucho/hessian-3.1.3.jar
ln -sf $(build-classpath burlap) lib/caucho/burlap.jar
# BUILD/spring/lib/cglib/cglib-nodep-2.1_3.jar.no
ln -sf $(build-classpath cglib21) lib/cglib/cglib-nodep-2.1_3.jar
# BUILD/spring/lib/clover/clover.jar.no

#BUILD/spring/lib/commonj/commonj-twm.jar.no
ln -sf $(build-classpath commonj_1_1_apis) lib/commonj/commonj-twm.jar
# BUILD/spring/lib/concurrent/backport-util-concurrent.jar.no
ln -sf $(build-classpath backport-util-concurrent) lib/concurrent/backport-util-concurrent.jar
# BUILD/spring/lib/dom4j/dom4j-1.6.1.jar.no
ln -sf $(build-classpath dom4j) lib/dom4j/dom4j-1.6.1.jar
# BUILD/spring/lib/dom4j/jaxen-1.1-beta-7.jar.no
ln -sf $(build-classpath jaxen) lib/dom4j/jaxen-1.1-beta-7.jar
# BUILD/spring/lib/easymock/easymockclassextension.jar.no
ln -sf $(build-classpath easymock-classextension) lib/easymock/easymockclassextension.jar
# BUILD/spring/lib/easymock/easymock.jar.no
ln -sf $(build-classpath easymock) lib/easymock/easymock.jar
# BUILD/spring/lib/eclipselink/eclipselink.jar.no

# BUILD/spring/lib/ehcache/ehcache-1.5.0.jar.no
ln -sf $(build-classpath ehcache) lib/ehcache/ehcache-1.5.0.jar
%if %with xmlgraphics
# BUILD/spring/lib/fop/fop.jar.no
ln -sf $(build-classpath xmlgraphics-fop) lib/fop/fop.jar
%else
cp -p lib/fop/fop.jar.no lib/fop/fop.jar
%endif
# BUILD/spring/lib/freemarker/freemarker.jar.no
ln -sf $(build-classpath freemarker) lib/freemarker/freemarker.jar
# BUILD/spring/lib/glassfish/glassfish-clapi.jar.no

# BUILD/spring/lib/groovy/groovy-1.5.6.jar.no
ln -sf $(build-classpath groovy15-all) lib/groovy/groovy-1.5.6.jar
# BUILD/spring/lib/hibernate/hibernate3.jar.no
ln -sf $(build-classpath hibernate3-core) lib/hibernate/hibernate3.jar
# BUILD/spring/lib/hibernate/hibernate-annotations.jar.no
ln -sf $(build-classpath hibernate3-annotations) lib/hibernate/hibernate-annotations.jar
# BUILD/spring/lib/hibernate/hibernate-commons-annotations.jar.no
ln -sf $(build-classpath hibernate3-commons-annotations) lib/hibernate/hibernate-commons-annotations.jar
# BUILD/spring/lib/hibernate/hibernate-entitymanager.jar.no
ln -sf $(build-classpath hibernate3-entitymanager) lib/hibernate/hibernate-entitymanager.jar
# BUILD/spring/lib/hsqldb/hsqldb.jar.no
ln -sf $(build-classpath hsqldb) lib/hsqldb/hsqldb.jar
# BUILD/spring/lib/httpclient/commons-httpclient-3.0.jar.no
ln -sf $(build-classpath commons-httpclient) lib/httpclient/commons-httpclient-3.0.jar
# BUILD/spring/lib/httpunit/httpunit.jar.no
ln -sf $(build-classpath httpunit) lib/httpunit/httpunit.jar
# BUILD/spring/lib/httpunit/Tidy.jar.no
ln -sf $(build-classpath jtidy) lib/httpunit/Tidy.jar
# BUILD/spring/lib/ibatis/ibatis-2.3.4.726.jar.no
ln -sf $(build-classpath apache-ibatis2) lib/ibatis/ibatis-2.3.4.726.jar
# BUILD/spring/lib/innovation/HTTPClient-0.3-3.jar.no

# BUILD/spring/lib/itext/iText-2.1.3.jar.no
ln -sf $(build-classpath itext) lib/itext/iText-2.1.3.jar
# BUILD/spring/lib/j2ee/activation.jar.no
ln -sf $(build-classpath jaf_1_1_api) lib/j2ee/activation.jar
# BUILD/spring/lib/j2ee/common-annotations.jar.no
ln -sf $(build-classpath annotation_1_0_api) lib/j2ee/common-annotations.jar
# BUILD/spring/lib/j2ee/connector.jar.no
ln -sf $(build-classpath j2ee_connector_1_5_api) lib/j2ee/connector.jar
# BUILD/spring/lib/j2ee/ejb-api.jar.no
ln -sf $(build-classpath ejb_3_0_api) lib/j2ee/ejb-api.jar
ln -s $(build-classpath interceptor_api) lib/j2ee/interceptor_api.jar
# BUILD/spring/lib/j2ee/el-api.jar.no
ln -sf $(build-classpath el_1_0_api) lib/j2ee/el-api.jar
# BUILD/spring/lib/j2ee/jaxrpc.jar.no
ln -sf $(build-classpath jaxrpc_1_1_api) lib/j2ee/jaxrpc.jar
# BUILD/spring/lib/j2ee/jms.jar.no
ln -sf $(build-classpath jms_1_1_api) lib/j2ee/jms.jar
# BUILD/spring/lib/j2ee/jsf-api.jar.no
ln -sf $(build-classpath jsf_1_2_api) lib/j2ee/jsf-api.jar
# BUILD/spring/lib/j2ee/jsp-api.jar.no
ln -sf $(build-classpath jsp_2_0_api) lib/j2ee/jsp-api.jar
# BUILD/spring/lib/j2ee/jstl.jar.no
ln -sf $(build-classpath jstl) lib/j2ee/jstl.jar
# BUILD/spring/lib/j2ee/jta.jar.no
ln -sf $(build-classpath jta_1_1_api) lib/j2ee/jta.jar
# BUILD/spring/lib/j2ee/mail.jar.no
ln -sf $(build-classpath javamail_1_4_api) lib/j2ee/mail.jar
# BUILD/spring/lib/j2ee/persistence.jar.no
ln -sf $(build-classpath jpa_1_0B_api) lib/j2ee/persistence.jar
# BUILD/spring/lib/j2ee/rowset.jar.no

# BUILD/spring/lib/j2ee/servlet-api.jar.no
ln -sf $(build-classpath tomcat5-servlet-2.4-api) lib/j2ee/servlet-api.jar
# BUILD/spring/lib/apache-commons/commons-attributes-api.jar.no
ln -sf $(build-classpath commons-attributes-api) lib/jakarta-commons/commons-attributes-api.jar
# BUILD/spring/lib/jakarta-commons/commons-attributes-compiler.jar.no
ln -sf $(build-classpath commons-attributes-compiler) lib/jakarta-commons/commons-attributes-compiler.jar
# BUILD/spring/lib/jakarta-commons/commons-beanutils.jar.no
ln -sf $(build-classpath commons-beanutils) lib/jakarta-commons/commons-beanutils.jar
# BUILD/spring/lib/jakarta-commons/commons-codec.jar.no
ln -sf $(build-classpath commons-codec) lib/jakarta-commons/commons-codec.jar
# BUILD/spring/lib/jakarta-commons/commons-collections.jar.no
ln -sf $(build-classpath commons-collections) lib/jakarta-commons/commons-collections.jar
# BUILD/spring/lib/jakarta-commons/commons-dbcp.jar.no
ln -sf $(build-classpath commons-dbcp) lib/jakarta-commons/commons-dbcp.jar
# BUILD/spring/lib/jakarta-commons/commons-digester.jar.no
ln -sf $(build-classpath commons-digester) lib/jakarta-commons/commons-digester.jar
# BUILD/spring/lib/jakarta-commons/commons-discovery.jar.no
ln -sf $(build-classpath commons-discovery) lib/jakarta-commons/commons-discovery.jar
# BUILD/spring/lib/jakarta-commons/commons-fileupload.jar.no
ln -sf $(build-classpath commons-fileupload) lib/jakarta-commons/commons-fileupload.jar
# BUILD/spring/lib/jakarta-commons/commons-httpclient.jar.no
ln -sf $(build-classpath commons-httpclient) lib/jakarta-commons/commons-httpclient.jar
# BUILD/spring/lib/jakarta-commons/commons-io.jar.no
ln -sf $(build-classpath commons-io) lib/jakarta-commons/commons-io.jar
# BUILD/spring/lib/jakarta-commons/commons-lang.jar.no
ln -sf $(build-classpath commons-lang) lib/jakarta-commons/commons-lang.jar
# BUILD/spring/lib/jakarta-commons/commons-logging.jar.no
ln -sf $(build-classpath commons-logging) lib/jakarta-commons/commons-logging.jar
# BUILD/spring/lib/jakarta-commons/commons-pool.jar.no
ln -sf $(build-classpath commons-pool) lib/jakarta-commons/commons-pool.jar
# BUILD/spring/lib/jakarta-commons/commons-validator.jar.no
ln -sf $(build-classpath commons-validator) lib/jakarta-commons/commons-validator.jar
# BUILD/spring/lib/jakarta-taglibs/standard.jar.no
ln -sf $(build-classpath taglibs-standard) lib/jakarta-taglibs/standard.jar
# BUILD/spring/lib/jamon/jamon-2.7.jar.no
ln -sf $(build-classpath jamonapi) lib/jamon/jamon-2.7.jar
# BUILD/spring/lib/jarjar/jarjar.jar.no
ln -sf $(build-classpath jarjar) lib/jarjar/jarjar.jar
# BUILD/spring/lib/jasperreports/jasperreports-2.0.5.jar.no
ln -sf $(build-classpath jasperreports2) lib/jasperreports/jasperreports-2.0.5.jar
# BUILD/spring/lib/javassist/javassist-3.4.GA.jar.no
ln -sf $(build-classpath javassist) lib/javassist/javassist-3.4.GA.jar
# BUILD/spring/lib/jaxws/jaxb-api.jar.no
ln -sf $(build-classpath glassfish-jaxb/jaxb-api) lib/jaxws/jaxb-api.jar
# BUILD/spring/lib/jaxws/jaxws-api.jar.no
ln -sf $(build-classpath jaxws_2_1_api) lib/jaxws/jaxws-api.jar
# BUILD/spring/lib/jaxws/jws-api.jar.no
ln -sf $(build-classpath ws_metadata_2_0_api) lib/jaxws/jws-api.jar
# BUILD/spring/lib/jaxws/saaj-api.jar.no
ln -sf $(build-classpath saaj_1_3_api) lib/jaxws/saaj-api.jar
# BUILD/spring/lib/jdo/jdo2-api.jar.no
ln -sf $(build-classpath apache-jdo-2.0-api) lib/jdo/jdo2-api.jar
# BUILD/spring/lib/jdom/jdom.jar.no
ln -sf $(build-classpath jdom) lib/jdom/jdom.jar
# BUILD/spring/lib/jdt/jdt-compiler-3.1.1.jar.no
ln -sf $(build-classpath ecj3) lib/jdt/jdt-compiler-3.1.1.jar
# BUILD/spring/lib/jets3t/jets3t.jar.no
ln -sf $(build-classpath jets3t/jets3t) lib/jdt/jdt-compiler-3.1.1.jar
# BUILD/spring/lib/jexcelapi/jxl.jar.no
ln -sf $(build-classpath jexcelapi/jxl) lib/jexcelapi/jxl.jar
# BUILD/spring/lib/jmock/jmock-cglib.jar.no
ln -sf $(build-classpath jmock-cglib) lib/jmock/jmock-cglib.jar
# BUILD/spring/lib/jmock/jmock.jar.no
ln -sf $(build-classpath jmock) lib/jmock/jmock.jar
# BUILD/spring/lib/jmx/jmxremote.jar.no

# BUILD/spring/lib/jmx/jmxremote_optional.jar.no

# BUILD/spring/lib/jmx/jmxri.jar.no

# BUILD/spring/lib/jotm/jotm.jar.no
ln -sf $(build-classpath jotm/jotm) lib/jotm/jotm.jar
# BUILD/spring/lib/jotm/xapool.jar.no
ln -sf $(build-classpath xapool) lib/jotm/xapool.jar
# BUILD/spring/lib/jruby/jruby.jar.no
ln -sf $(build-classpath jruby) lib/jruby/jruby.jar
ln -sf $(build-classpath jruby-bytelist) lib/jruby/jruby-bytelist.jar
# BUILD/spring/lib/junit/junit-3.8.2.jar.no
ln -sf $(build-classpath junit) lib/junit/junit-3.8.2.jar
# BUILD/spring/lib/junit/junit-4.4.jar.no
ln -sf $(build-classpath junit44) lib/junit/junit-4.4.jar
# BUILD/spring/lib/log4j/log4j-1.2.15.jar.no
ln -sf $(build-classpath log4j) lib/log4j/log4j-1.2.15.jar
# BUILD/spring/lib/maven/maven-ant-tasks.jar.no

# BUILD/spring/lib/oc4j/oc4j-clapi.jar.no

# BUILD/spring/lib/ognl/ognl.jar.no
ln -sf $(build-classpath ognl) lib/ognl/ognl.jar
# BUILD/spring/lib/openjpa/openjpa-1.1.0.jar.no
ln -sf $(build-classpath openjpa/all) lib/openjpa/openjpa-1.1.0.jar
# BUILD/spring/lib/osgi/org.eclipse.osgi_3.1.1.jar.no

# BUILD/spring/lib/poi/poi-3.0.1.jar.no
ln -sf $(build-classpath poi/poi) lib/poi/poi-3.0.1.jar
# BUILD/spring/lib/portlet/portlet-api.jar.no
ln -sf $(build-classpath portlet-1.0-api) lib/portlet/portlet-api.jar
# BUILD/spring/lib/qdox/qdox-1.5.jar.no
##ln -sf $(build-classpath qdox) lib/qdox/qdox-1.5.jar
cp -p lib/qdox/qdox-1.5.jar.no lib/qdox/qdox-1.5.jar
# BUILD/spring/lib/quartz/quartz-all-1.6.1.jar.no
ln -sf $(build-classpath quartz16-all) lib/quartz/quartz-all-1.6.1.jar
# BUILD/spring/lib/serp/serp-1.13.1.jar.no
ln -sf $(build-classpath serp) lib/serp/serp-1.13.1.jar
# BUILD/spring/lib/slf4j/slf4j-api-1.5.0.jar.no
ln -sf $(build-classpath slf4j/slf4j-api) lib/slf4j/slf4j-api-1.5.0.jar
# BUILD/spring/lib/slf4j/slf4j-log4j12-1.5.0.jar.no
ln -sf $(build-classpath slf4j/slf4j-log4j12) lib/slf4j/slf4j-log4j12-1.5.0.jar
# BUILD/spring/lib/struts/struts.jar.no
ln -sf $(build-classpath struts) lib/struts/struts.jar
ln -sf $(build-classpath struts-tiles) lib/struts/struts-tiles.jar
ln -sf $(build-classpath struts-extras) lib/struts/struts-extras.jar
# BUILD/spring/lib/testng/testng-5.8-jdk15.jar.no
ln -sf $(build-classpath testng) lib/testng/testng-5.8-jdk15.jar
ln -sf $(build-classpath jcommander) lib/testng/jcommander.jar
ln -sf $(build-classpath objenesis) lib/testng/objenesis.jar
# BUILD/spring/lib/tiles/tiles-api-2.0.6.jar.no
ln -sf $(build-classpath tiles/api) lib/tiles/api-2.0.6.jar
# BUILD/spring/lib/tiles/tiles-core-2.0.6.jar.no
ln -sf $(build-classpath tiles/core) lib/tiles/core-2.0.6.jar
# BUILD/spring/lib/tiles/tiles-jsp-2.0.6.jar.no
ln -sf $(build-classpath tiles/jsp) lib/tiles/jsp-2.0.6.jar
#
#ln -sf $(build-classpath tiles/servlet) lib/tiles/tiles-servlet-2.0.6.jar
# BUILD/spring/lib/tomcat/catalina.jar.no
ln -sf $(build-classpath tomcat5/catalina) lib/tomcat/catalina.jar
# BUILD/spring/lib/tomcat/naming-resources.jar.no
ln -sf $(build-classpath tomcat5/naming-resources) lib/tomcat/naming-resources.jar
#BUILD/spring-framework-2.5.1/lib/toplink/toplink-api.jar.no
ln -sf $(build-classpath glassfish-persistence-1.0b-api) lib/toplink/toplink-api.jar
#mv lib/toplink/toplink-api.jar.no lib/toplink/toplink-api.jar
#BUILD/spring-framework-2.5.1/lib/toplink/toplink-essentials.jar.no
ln -sf $(build-classpath glassfish/toplink-essentials) lib/toplink/toplink-essentials.jar
#mv lib/toplink/toplink-essentials.jar.no lib/toplink/toplink-essentials.jar

# BUILD/spring/lib/velocity/velocity-1.5.jar.no
ln -sf $(build-classpath velocity) lib/velocity/velocity-1.5.jar
# BUILD/spring/lib/velocity/velocity-tools-view-1.4.jar.no
ln -sf $(build-classpath velocity-tools) lib/velocity/velocity-tools-view-1.4.jar
# BUILD/spring/lib/websphere/websphere_uow_api.jar.no

# BUILD/spring/lib/xdoclet/xjavadoc-1.1.jar.no
ln -sf $(build-classpath xjavadoc) lib/xdoclet/xjavadoc-1.1.jar
# BUILD/spring/lib/xerces/xercesImpl.jar.no
ln -sf $(build-classpath xerces-j2) lib/xerces/xercesImpl.jar
# BUILD/spring/samples/jca-1.0/dist/spring-jca-sample.jar.no

# BUILD/spring/samples/jca-1.0/lib/spring-cciblackbox-tx.jar.no

##################################################################
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
echo The following jars are symlinked:
%{_bindir}/find -type l -name "*.jar" -print
echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
echo ##################################################################
echo WARNING: The following jars are NOT symlinked:
%{_bindir}/find -not -type l -name "*.jar" -print
echo ##################################################################

%build
export CLASSPATH=
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/trax`
OPT_JAR_LIST="$OPT_JAR_LIST ant/ant-junit junit"
#export ANT_OPTS="-Xmx512m -XX:-UseGCOverheadLimit"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first -Djava.awt.headless=true build 
rm lib/cglib/cglib-nodep-2.1_3.jar
ln -sf $(build-classpath cglib21-nodep) lib/cglib/cglib-nodep-2.1_3.jar
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first -Djava.awt.headless=true tests 
rm lib/cglib/cglib-nodep-2.1_3.jar
ln -sf $(build-classpath cglib21) lib/cglib/cglib-nodep-2.1_3.jar
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first -Djava.awt.headless=true release

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

install -p -m 644 dist/%{bname}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -p -m 644 dist/weaving/%{bname}-agent.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/agent-%{version}.jar
install -p -m 644 dist/modules/%{bname}-aop.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/aop-%{version}.jar
install -p -m 644 dist/weaving/%{bname}-aspects.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/aspects-%{version}.jar
install -p -m 644 dist/modules/%{bname}-beans.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/beans-%{version}.jar
install -p -m 644 dist/modules/%{bname}-context.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/context-%{version}.jar
install -p -m 644 dist/modules/%{bname}-context-support.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/context-support-%{version}.jar
install -p -m 644 dist/modules/%{bname}-core.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-%{version}.jar
install -p -m 644 dist/modules/%{bname}-jdbc.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jdbc-%{version}.jar
install -p -m 644 dist/modules/%{bname}-jms.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jms-%{version}.jar
install -p -m 644 dist/modules/%{bname}-orm.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/orm-%{version}.jar
install -p -m 644 dist/modules/%{bname}-test.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/test-%{version}.jar
install -p -m 644 dist/weaving/%{bname}-tomcat-weaver.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/tomcat-weaver-%{version}.jar
install -p -m 644 dist/modules/%{bname}-tx.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/tx-%{version}.jar
install -p -m 644 dist/modules/%{bname}-web.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/web-%{version}.jar
install -p -m 644 dist/modules/%{bname}-webmvc.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/webmvc-%{version}.jar
install -p -m 644 dist/modules/%{bname}-webmvc-portlet.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/webmvc-portlet-%{version}.jar
install -p -m 644 dist/modules/%{bname}-webmvc-struts.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/webmvc-struts-%{version}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}-sources
install -p -m 644 dist/weaving-sources/spring-agent-sources.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-sources/agent-sources-%{version}.jar
install -p -m 644 dist/module-sources/spring-aop-sources.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-sources/aop-sources-%{version}.jar
install -p -m 644 dist/weaving-sources/spring-aspects-sources.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-sources/aspects-sources-%{version}.jar
install -p -m 644 dist/module-sources/spring-beans-sources.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-sources/beans-sources-%{version}.jar
install -p -m 644 dist/module-sources/spring-context-sources.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-sources/context-sources-%{version}.jar
install -p -m 644 dist/module-sources/spring-context-support-sources.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-sources/context-support-sources-%{version}.jar
install -p -m 644 dist/module-sources/spring-core-sources.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-sources/core-sources-%{version}.jar
install -p -m 644 dist/module-sources/spring-jdbc-sources.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-sources/jdbc-sources-%{version}.jar
install -p -m 644 dist/module-sources/spring-jms-sources.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-sources/jms-sources-%{version}.jar
install -p -m 644 dist/module-sources/spring-orm-sources.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-sources/orm-sources-%{version}.jar
install -p -m 644 dist/module-sources/spring-test-sources.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-sources/test-sources-%{version}.jar
install -p -m 644 dist/weaving-sources/spring-tomcat-weaver-sources.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-sources/tomcat-weaver-sources-%{version}.jar
install -p -m 644 dist/module-sources/spring-tx-sources.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-sources/tx-sources-%{version}.jar
install -p -m 644 dist/module-sources/spring-webmvc-sources.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-sources/webmvc-sources-%{version}.jar
install -p -m 644 dist/module-sources/spring-webmvc-portlet-sources.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-sources/webmvc-portlet-sources-%{version}.jar
install -p -m 644 dist/module-sources/spring-webmvc-struts-sources.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-sources/webmvc-struts-sources-%{version}.jar
install -p -m 644 dist/module-sources/spring-web-sources.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-sources/web-sources-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name}-sources && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

%add_to_maven_depmap org.springframework %{bname}-agent %{version} JPP/%{name} agent
%add_to_maven_depmap org.springframework %{bname}-aop %{version} JPP/%{name} aop
%add_to_maven_depmap org.springframework %{bname}-aspects %{version} JPP/%{name} aspects
%add_to_maven_depmap org.springframework %{bname}-beans %{version} JPP/%{name} beans
%add_to_maven_depmap org.springframework %{bname}-context %{version} JPP/%{name} context
%add_to_maven_depmap org.springframework %{bname}-context-support %{version} JPP/%{name} context-support
%add_to_maven_depmap org.springframework %{bname}-core %{version} JPP/%{name} core
%add_to_maven_depmap org.springframework %{bname}-jdbc %{version} JPP/%{name} jdbc
%add_to_maven_depmap org.springframework %{bname}-jms %{version} JPP/%{name} jms
%add_to_maven_depmap org.springframework %{bname}-orm %{version} JPP/%{name} orm
%add_to_maven_depmap org.springframework %{bname} %{version} JPP %{name}
%add_to_maven_depmap org.springframework %{bname}-test %{version} JPP/%{name} test
%add_to_maven_depmap org.springframework %{bname}-tomcat-weaver %{version} JPP/%{name} tomcat-weaver
%add_to_maven_depmap org.springframework %{bname}-tx %{version} JPP/%{name} tx
%add_to_maven_depmap org.springframework %{bname}-webmvc %{version} JPP/%{name} webmvc
%add_to_maven_depmap org.springframework %{bname}-webmvc-portlet %{version} JPP/%{name} webmvc-portlet
%add_to_maven_depmap org.springframework %{bname}-webmvc-struts %{version} JPP/%{name} webmvc-struts
%add_to_maven_depmap org.springframework %{bname}-web %{version} JPP/%{name} web

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m 644 dist/maven/spring-agent.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-agent.pom
install -p -m 644 dist/maven/spring-aop.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-aop.pom
install -p -m 644 dist/maven/spring-aspects.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-aspects.pom
install -p -m 644 dist/maven/spring-beans.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-beans.pom
install -p -m 644 dist/maven/spring-context.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-context.pom
install -p -m 644 dist/maven/spring-context-support.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-context-support.pom
install -p -m 644 dist/maven/spring-core.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-core.pom
install -p -m 644 dist/maven/spring-jdbc.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jdbc.pom
install -p -m 644 dist/maven/spring-jms.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jms.pom
install -p -m 644 dist/maven/spring-orm.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-orm.pom
install -p -m 644 dist/maven/spring.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
install -p -m 644 dist/maven/spring-test.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-test.pom
install -p -m 644 dist/maven/spring-tomcat-weaver.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-tomcat-weaver.pom
install -p -m 644 dist/maven/spring-tx.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-tx.pom
install -p -m 644 dist/maven/spring-web.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-web.pom
install -p -m 644 dist/maven/spring-webmvc.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-webmvc.pom
install -p -m 644 dist/maven/spring-webmvc-portlet.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-webmvc-portlet.pom
install -p -m 644 dist/maven/spring-webmvc-struts.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-webmvc-struts.pom

# resources
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc
install -p -m 644 dist/resources/spring-aop-2.0.xsd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-aop-2.0.xsd
install -p -m 644 dist/resources/spring-aop-2.5.xsd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-aop-2.5.xsd
install -p -m 644 dist/resources/spring-beans-2.0.dtd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-beans-2.0.dtd
install -p -m 644 dist/resources/spring-beans-2.0.xsd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-beans-2.0.xsd
install -p -m 644 dist/resources/spring-beans-2.5.xsd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-beans-2.5.xsd
install -p -m 644 dist/resources/spring-beans.dtd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-beans.dtd
install -p -m 644 dist/resources/spring-context-2.5.xsd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-context-2.5.xsd
install -p -m 644 dist/resources/spring-form.tld $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-form.tld
install -p -m 644 dist/resources/spring.ftl $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}.ftl
install -p -m 644 dist/resources/spring-jee-2.0.xsd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-jee-2.0.xsd
install -p -m 644 dist/resources/spring-jee-2.5.xsd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-jee-2.5.xsd
install -p -m 644 dist/resources/spring-jms-2.5.xsd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-jms-2.5.xsd
install -p -m 644 dist/resources/spring-lang-2.0.xsd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-lang-2.0.xsd
install -p -m 644 dist/resources/spring-lang-2.5.xsd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-lang-2.5.xsd
install -p -m 644 dist/resources/spring.tld $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}.tld
install -p -m 644 dist/resources/spring-tool-2.0.xsd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-tool-2.0.xsd
install -p -m 644 dist/resources/spring-tool-2.5.xsd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-tool-2.5.xsd
install -p -m 644 dist/resources/spring-tx-2.0.xsd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-tx-2.0.xsd
install -p -m 644 dist/resources/spring-tx-2.5.xsd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-tx-2.5.xsd
install -p -m 644 dist/resources/spring-util-2.0.xsd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-util-2.0.xsd
install -p -m 644 dist/resources/spring-util-2.5.xsd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}-util-2.5.xsd
install -p -m 644 dist/resources/spring.vm $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{bname}.vm

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

### manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/
cp -pr changelog.txt license.txt notice.txt readme.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/
ln -s %{_javadocdir}/%{name} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/api
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/taglib/
cp -pr docs/taglib/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/taglib/
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/reference/
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/reference/html_single/
cp -pr docs/reference/html_single/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/reference/html_single/
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/reference/images/admons/
cp -p docs/reference/images/admons/*.png docs/reference/images/admons/*.gif docs/reference/images/admons/*.tif $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/reference/images/admons/
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/reference/pdf/
cp -p docs/reference/pdf/*.pdf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/reference/pdf/
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/reference/styles/
cp -p docs/reference/styles/html.css $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/reference/styles/
cp -p docs/reference/readme.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/reference/
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/MVC-step-by-step/
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/MVC-step-by-step/html_single/
cp -pr docs/MVC-step-by-step/html_single/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/MVC-step-by-step/html_single/
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/MVC-step-by-step/images/admons/
cp -p docs/MVC-step-by-step/images/admons/*.png docs/MVC-step-by-step/images/admons/*.gif docs/MVC-step-by-step/images/admons/*.tif $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/MVC-step-by-step/images/admons/
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/MVC-step-by-step/pdf/
cp -p docs/MVC-step-by-step/pdf/*.pdf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/MVC-step-by-step/pdf/
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/MVC-step-by-step/styles/
cp -p docs/MVC-step-by-step/styles/html.css $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/MVC-step-by-step/styles/
###

# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/samples
for d in imagedb jpetstore petclinic petportal; do
    cp -pr samples/${d}/ $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/samples/
done

# FIXME: (dwalluck): hack for Recognition of file failed
rm $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/samples/jpetstore/war/images/*.gif

## osgi
#install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/osgi/bnd
#cp -pr osgi/bnd/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/osgi/bnd

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{upstream_version}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH2} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH3} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH4} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH5} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH6} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH8} $RPM_BUILD_ROOT%{repodirsrc}
#install -p -m 644 %{PATCH9} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH10} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH11} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH12} $RPM_BUILD_ROOT%{repodirsrc}
#install -p -m 644 %{PATCH13} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH14} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH15} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/spring.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/agent-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/spring-agent.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/aop-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/spring-aop.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/aspects-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/spring-aspects.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/beans-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/spring-beans.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/context-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/spring-context.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/context-support-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/spring-context-support.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/core-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/spring-core.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jdbc-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/spring-jdbc.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jms-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/spring-jms.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/orm-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/spring-orm.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/test-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/spring-test.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/tomcat-weaver-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/spring-tomcat-weaver.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/tx-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/spring-tx.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/web-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/spring-web.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/webmvc-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/spring-webmvc.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/webmvc-portlet-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/spring-webmvc-portlet.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/webmvc-struts-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/spring-webmvc-struts.jar
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom $RPM_BUILD_ROOT%{repodirlib}/spring.pom
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-agent.pom $RPM_BUILD_ROOT%{repodirlib}/spring-agent.pom
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-aop.pom $RPM_BUILD_ROOT%{repodirlib}/spring-aop.pom
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-aspects.pom $RPM_BUILD_ROOT%{repodirlib}/spring-aspects.pom
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-beans.pom $RPM_BUILD_ROOT%{repodirlib}/spring-beans.pom
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-context.pom $RPM_BUILD_ROOT%{repodirlib}/spring-context.pom
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-context-support.pom $RPM_BUILD_ROOT%{repodirlib}/spring-context-support.pom
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-core.pom $RPM_BUILD_ROOT%{repodirlib}/spring-core.pom
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jdbc.pom $RPM_BUILD_ROOT%{repodirlib}/spring-jdbc.pom
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jms.pom $RPM_BUILD_ROOT%{repodirlib}/spring-jms.pom
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-orm.pom $RPM_BUILD_ROOT%{repodirlib}/spring-orm.pom
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-test.pom $RPM_BUILD_ROOT%{repodirlib}/spring-test.pom
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-tomcat-weaver.pom $RPM_BUILD_ROOT%{repodirlib}/spring-tomcat-weaver.pom
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-tx.pom $RPM_BUILD_ROOT%{repodirlib}/spring-tx.pom
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-web.pom $RPM_BUILD_ROOT%{repodirlib}/spring-web.pom
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-webmvc.pom $RPM_BUILD_ROOT%{repodirlib}/spring-webmvc.pom
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-webmvc-portlet.pom $RPM_BUILD_ROOT%{repodirlib}/spring-webmvc-portlet.pom
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-webmvc-struts.pom $RPM_BUILD_ROOT%{repodirlib}/spring-webmvc-struts.pom
%endif

%if %with zips
%{__mkdir_p} %{buildroot}%{_javadir}/jbossas-fordev
%{__cp} -p target/release/spring-framework-%{upstream_version}-with-dependencies.zip %{buildroot}%{_javadir}/jbossas-fordev/spring-framework-%{upstream_version}-with-dependencies.zip
%{__cp} -p target/release/spring-framework-%{upstream_version}.zip %{buildroot}%{_javadir}/jbossas-fordev/spring-framework-%{upstream_version}.zip
%{__cp} -p target/release/spring-framework-%{upstream_version}-with-docs.zip %{buildroot}%{_javadir}/jbossas-fordev/spring-framework-%{upstream_version}-with-docs.zip
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

%files
%doc %dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/changelog.txt
%doc %{_docdir}/%{name}-%{version}/license.txt
%doc %{_docdir}/%{name}-%{version}/notice.txt
%doc %{_docdir}/%{name}-%{version}/readme.txt
%dir %{_javadir}/%{name}
%dir %{_datadir}/%{name}-%{version}
%dir %{_datadir}/%{name}-%{version}/etc
%{_datadir}/%{name}-%{version}/etc/*
#%dir %{_datadir}/%{name}-%{version}/osgi
#%dir %{_datadir}/%{name}-%{version}/osgi/bnd
#%{_datadir}/%{name}-%{version}/osgi/bnd/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-*%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files core
%{_javadir}/%{name}/core*.jar

%files agent
%{_javadir}/%{name}/agent*.jar

%files aop
%{_javadir}/%{name}/aop*.jar

%files aspects
%{_javadir}/%{name}/aspects*.jar

%files beans
%{_javadir}/%{name}/beans*.jar

%files context
%{_javadir}/%{name}/context.jar
%{_javadir}/%{name}/context-%{version}.jar

%files context-support
%{_javadir}/%{name}/context-support*.jar

%files jms
%{_javadir}/%{name}/jms*.jar

%files jdbc
%{_javadir}/%{name}/jdbc*.jar

%files orm
%{_javadir}/%{name}/orm*.jar

%files test
%{_javadir}/%{name}/test*.jar

%files tomcat-weaver
%{_javadir}/%{name}/tomcat-weaver*.jar

%files tx
%{_javadir}/%{name}/tx*.jar

%files web
%{_javadir}/%{name}/web-*.jar
%{_javadir}/%{name}/web.jar

%files webmvc
%{_javadir}/%{name}/webmvc.jar
%{_javadir}/%{name}/webmvc-%{version}.jar

%files webmvc-portlet
%{_javadir}/%{name}/webmvc-portlet*.jar

%files webmvc-struts
%{_javadir}/%{name}/webmvc-struts*.jar

%files all
%{_javadir}/%{name}*.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/*
%exclude %doc %{_docdir}/%{name}-%{version}/changelog.txt
%exclude %doc %{_docdir}/%{name}-%{version}/license.txt
%exclude %doc %{_docdir}/%{name}-%{version}/notice.txt
%exclude %doc %{_docdir}/%{name}-%{version}/readme.txt
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files demo
%{_datadir}/%{name}-%{version}/samples

%files devel
%dir %{_javadir}/%{name}-sources
%{_javadir}/%{name}-sources/aop-sources-%{version}.jar
%{_javadir}/%{name}-sources/aop-sources.jar
%{_javadir}/%{name}-sources/agent-sources-%{version}.jar
%{_javadir}/%{name}-sources/agent-sources.jar
%{_javadir}/%{name}-sources/aspects-sources-%{version}.jar
%{_javadir}/%{name}-sources/aspects-sources.jar
%{_javadir}/%{name}-sources/beans-sources-%{version}.jar
%{_javadir}/%{name}-sources/beans-sources.jar
%{_javadir}/%{name}-sources/context-sources-%{version}.jar
%{_javadir}/%{name}-sources/context-sources.jar
%{_javadir}/%{name}-sources/context-support-sources-%{version}.jar
%{_javadir}/%{name}-sources/context-support-sources.jar
%{_javadir}/%{name}-sources/core-sources-%{version}.jar
%{_javadir}/%{name}-sources/core-sources.jar
%{_javadir}/%{name}-sources/jdbc-sources-%{version}.jar
%{_javadir}/%{name}-sources/jdbc-sources.jar
%{_javadir}/%{name}-sources/jms-sources-%{version}.jar
%{_javadir}/%{name}-sources/jms-sources.jar
%{_javadir}/%{name}-sources/orm-sources-%{version}.jar
%{_javadir}/%{name}-sources/orm-sources.jar
%{_javadir}/%{name}-sources/tomcat-weaver-sources-%{version}.jar
%{_javadir}/%{name}-sources/tomcat-weaver-sources.jar
%{_javadir}/%{name}-sources/test-sources-%{version}.jar
%{_javadir}/%{name}-sources/test-sources.jar
%{_javadir}/%{name}-sources/tx-sources-%{version}.jar
%{_javadir}/%{name}-sources/tx-sources.jar
%{_javadir}/%{name}-sources/web-sources-%{version}.jar
%{_javadir}/%{name}-sources/web-sources.jar
%{_javadir}/%{name}-sources/webmvc-portlet-sources-%{version}.jar
%{_javadir}/%{name}-sources/webmvc-portlet-sources.jar
%{_javadir}/%{name}-sources/webmvc-sources-%{version}.jar
%{_javadir}/%{name}-sources/webmvc-sources.jar
%{_javadir}/%{name}-sources/webmvc-struts-sources-%{version}.jar
%{_javadir}/%{name}-sources/webmvc-struts-sources.jar

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%if %with zips
# FIXME: (dwalluck): This could be split.
%files zip
%defattr(0644,jboss,jboss,0755)
%dir %{_javadir}/jbossas-fordev
%{_javadir}/jbossas-fordev/spring-framework-%{upstream_version}-with-dependencies.zip
%{_javadir}/jbossas-fordev/spring-framework-%{upstream_version}.zip
%{_javadir}/jbossas-fordev/spring-framework-%{upstream_version}-with-docs.zip
%endif

%changelog
* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5.6.SEC03-alt4_5jpp6
- fixed build

* Fri Jun 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5.6.SEC03-alt3_5jpp6
- fixed build

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5.6.SEC03-alt2_5jpp6
- built with java 6 due to abstract getParentLogger

* Wed Jan 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5.6.SEC03-alt1_5jpp6
- SEC03 release

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.5.6-alt3_6.SEC02jpp6
- fixed build with slf4j

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.5.6-alt2_6.SEC02jpp6
- new bugfix release SEC02 (closes: #23690)

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.5.6-alt2_6.SEC01jpp6
- new bugfix release SEC01

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.5.6-alt2_1jpp5
- selected java5 compiler explicitly

* Fri Jun 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.5.6-alt1_1jpp5
- fixed build

* Fri Mar 20 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.5.5-alt2_1jpp6
- fixed build
- INFO:	junit 4.5 is incompatible with this build. use junit 4.4.

* Wed Mar 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.5.5-alt1_1jpp6
- first build

