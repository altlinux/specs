Group: Networking/WWW
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 25
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jetty
%define version 9.4.0
# Copyright (c) 2000-2007, JPackage Project
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

%global jtuid       110
%global username    %{name}
%global confdir     %{_sysconfdir}/%{name}
%global logdir      %{_var}/log/%{name}
%global apphomedir     %{_datadir}/%{name}
%global jettycachedir %{_var}/cache/%{name}
%global tempdir     %{jettycachedir}/temp
%global rundir      %{_var}/run/%{name}
%global jettylibdir %{_var}/lib/%{name}
%global appdir      %{jettylibdir}/webapps


%global addver M0

# Conditionals to help breaking eclipse <-> jetty dependency cycle
# when bootstrapping for new architectures
%if 0%{?fedora}
%bcond_without nosql
%bcond_without osgi
%bcond_without spring
# package without service files
%bcond_without service
%endif

Name:           jetty
Version:        9.4.0
Release:        alt1_0.2.M0jpp8
Summary:        Java Webserver and Servlet Container

# Jetty is dual licensed under both ASL 2.0 and EPL 1.0, see NOTICE.txt
License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        https://github.com/eclipse/%{name}.project/archive/%{name}-%{version}.%{addver}.tar.gz
Source1:        jetty.sh
Source3:        jetty.logrotate
Source5:        %{name}.service
# MIT license text taken from Utf8Appendable.java
Source6:        LICENSE-MIT

Patch1:         0001-Fedora-jetty.home.patch

BuildRequires:  geronimo-annotation
BuildRequires:  geronimo-jaspic-spec
BuildRequires:  jboss-transaction-1.2-api
BuildRequires:  jboss-websocket-1.0-api
BuildRequires:  glassfish-annotation-api
BuildRequires:  geronimo-parent-poms
BuildRequires:  glassfish-servlet-api
BuildRequires:  glassfish-el
BuildRequires:  glassfish-el-api
BuildRequires:  glassfish-jsp
BuildRequires:  glassfish-jsp-api
BuildRequires:  tomcat-taglibs-standard
BuildRequires:  tomcat-lib
BuildRequires:  java-devel >= 1.7.0
BuildRequires:  jpackage-utils
BuildRequires:  maven-local >= 0.7.0
BuildRequires:  jvnet-parent
BuildRequires:  ant
BuildRequires:  maven-local
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-war-plugin
BuildRequires:  exec-maven-plugin
BuildRequires:  objectweb-asm
BuildRequires:  slf4j
BuildRequires:  ecj
BuildRequires:  geronimo-parent-poms
BuildRequires:  maven-plugin-build-helper
BuildRequires:  weld-core
BuildRequires:  infinispan
BuildRequires:  jnr-unixsocket

%if %{with osgi}
BuildRequires:  eclipse-platform
%endif
%if %{with nosql}
BuildRequires:  mongo-java-driver >= 2.6.5
%endif
%if %{with spring}
BuildRequires:  springframework-beans
%endif

BuildRequires:  javamail
BuildRequires:  jetty-parent
BuildRequires:  jetty-distribution-remote-resources
BuildRequires:  jetty-build-support
BuildRequires:  jetty-version-maven-plugin
BuildRequires:  jetty-toolchain
BuildRequires:  jetty-assembly-descriptors
BuildRequires:  jetty-test-policy
BuildRequires:  jetty-artifact-remote-resources
BuildRequires:  jetty-schemas
BuildRequires:  jetty-alpn-api

BuildArch:      noarch


Requires:       %{name}-annotations = %{version}
Requires:       %{name}-ant = %{version}
Requires:       %{name}-cdi = %{version}
Requires:       %{name}-client = %{version}
Requires:       %{name}-continuation = %{version}
Requires:       %{name}-deploy = %{version}
Requires:       %{name}-fcgi-client = %{version}
Requires:       %{name}-fcgi-server = %{version}
Requires:       %{name}-http = %{version}
Requires:       %{name}-http-spi = %{version}
Requires:       %{name}-io = %{version}
Requires:       %{name}-infinispan = %{version}
Requires:       %{name}-jaas = %{version}
Requires:       %{name}-jaspi = %{version}
Requires:       %{name}-jmx = %{version}
Requires:       %{name}-jndi = %{version}
Requires:       %{name}-jsp = %{version}
Requires:       %{name}-jspc-maven-plugin = %{version}
Requires:       %{name}-maven-plugin = %{version}
Requires:       %{name}-monitor = %{version}
Requires:       %{name}-plus = %{version}
Requires:       %{name}-proxy = %{version}
Requires:       %{name}-rewrite = %{version}
Requires:       %{name}-security = %{version}
Requires:       %{name}-server = %{version}
Requires:       %{name}-servlet = %{version}
Requires:       %{name}-servlets = %{version}
Requires:       %{name}-spring = %{version}
Requires:       %{name}-start = %{version}
Requires:       %{name}-unixsocket = %{version}
Requires:       %{name}-util = %{version}
Requires:       %{name}-util-ajax = %{version}
Requires:       %{name}-webapp = %{version}
Requires:       %{name}-xml = %{version}
Requires:       %{name}-websocket-api = %{version}
Requires:       %{name}-websocket-client = %{version}
Requires:       %{name}-websocket-common = %{version}
Requires:       %{name}-websocket-server = %{version}
Requires:       %{name}-websocket-servlet = %{version}
Requires:       %{name}-javax-websocket-client-impl = %{version}
Requires:       %{name}-javax-websocket-server-impl = %{version}
Requires:       %{name}-nosql = %{version}
Requires:       %{name}-httpservice = %{version}
Requires:       %{name}-osgi-boot = %{version}
Requires:       %{name}-osgi-boot-warurl = %{version}
Requires:       %{name}-osgi-project = %{version}
Requires:       %{name}-osgi-boot-jsp = %{version}
Requires:       %{name}-quickstart = %{version}
Requires:       %{name}-alpn-client = %{version}
Requires:       %{name}-alpn-server = %{version}
Requires:       %{name}-osgi-alpn = %{version}
Requires:       %{name}-jstl = %{version}
Requires:       %{name}-http2-client = %{version}
Requires:       %{name}-http2-common = %{version}
Requires:       %{name}-http2-hpack = %{version}
Requires:       %{name}-http2-http-client-transport = %{version}
Requires:       %{name}-http2-server = %{version}

Requires(pre): shadow-change shadow-check shadow-convert shadow-edit shadow-groups shadow-log shadow-submap shadow-utils


Provides:       group(%username) = %jtuid
Provides:       user(%username) = %jtuid

Obsoletes: %{name}-manual < %{version}-%{release}

Obsoletes: %{name}-ajp < %{version}-%{release}
Obsoletes: %{name}-http-spi < %{version}-%{release}
Obsoletes: %{name}-nested < %{version}-%{release}
Obsoletes: %{name}-overlay-deployer < %{version}-%{release}
Obsoletes: %{name}-policy < %{version}-%{release}
Obsoletes: %{name}-websocket-mux-extension < %{version}-%{release}
Obsoletes: %{name}-runner < %{version}-%{release}
Obsoletes: %{name}-osgi-npn < %{version}-%{release}
Source44: import.info
Source45: jetty.init

%description
%global desc \
Jetty is a 100% Java HTTP Server and Servlet Container. This means that you\
do not need to configure and run a separate web server (like Apache) in order\
to use Java, servlets and JSPs to generate dynamic content. Jetty is a fully\
featured web server for static and dynamic content. Unlike separate\
server/container solutions, this means that your web server and web\
application run in the same process, without interconnection overheads\
and complications. Furthermore, as a pure java component, Jetty can be simply\
included in your application for demonstration, distribution or deployment.\
Jetty is available on all Java supported platforms.
%{desc}
%global extdesc %{desc}\
\
This package contains

%package        project
Group: Development/Java
Summary:        POM files for Jetty

%description    project
%{extdesc} %{summary}.

%package        annotations
Group: Networking/WWW
Summary:        annotations module for Jetty

%description    annotations
%{extdesc} %{summary}.

%package        ant
Group: Networking/WWW
Summary:        ant module for Jetty

%description    ant
%{extdesc} %{summary}.

%package cdi
Group: Networking/WWW
Summary:        Jetty CDI Configuration

%description cdi
%{extdesc} %{summary}.

%package        client
Group: Networking/WWW
Summary:        client module for Jetty

%description    client
%{extdesc} %{summary}.

%package        continuation
Group: Networking/WWW
Summary:        continuation module for Jetty

%description    continuation
%{extdesc} %{summary}.

%package        deploy
Group: Networking/WWW
Summary:        deploy module for Jetty

%description    deploy
%{extdesc} %{summary}.

%package fcgi-client
Group: Networking/WWW
Summary:        FastCGI client module for Jetty

%description fcgi-client
%{extdesc} %{summary}.

%package fcgi-server
Group: Networking/WWW
Summary:        FastCGI client module for Jetty

%description fcgi-server
%{extdesc} %{summary}.

%package        http
Group: Networking/WWW
Summary:        http module for Jetty

%description    http
%{extdesc} %{summary}.

%package        http-spi
Group: Networking/WWW
Summary:        http-spi module for Jetty

%description    http-spi
%{extdesc} %{summary}.

%package        io
Group: Networking/WWW
Summary:        io module for Jetty
Obsoletes:      %{name}-websocket < %{version}-%{release}

%description    io
%{extdesc} %{summary}.

%package        infinispan
Group: Networking/WWW
Summary:        infinispan module for Jetty

%description    infinispan
%{extdesc} %{summary}.

%package        jaas
Group: Networking/WWW
Summary:        jaas module for Jetty

%description    jaas
%{extdesc} %{summary}.

%package        jaspi
Group: Networking/WWW
Summary:        jaspi module for Jetty

%description    jaspi
%{extdesc} %{summary}.

%package        jmx
Group: Networking/WWW
Summary:        jmx module for Jetty

%description    jmx
%{extdesc} %{summary}.

%package        jndi
Group: Networking/WWW
Summary:        jndi module for Jetty

%description    jndi
%{extdesc} %{summary}.

%package        jsp
Group: Networking/WWW
Summary:        jsp module for Jetty

%description    jsp
%{extdesc} %{summary}.

%package        jspc-maven-plugin
Group: Networking/WWW
Summary:        jspc-maven-plugin module for Jetty

%description    jspc-maven-plugin
%{extdesc} %{summary}.

%package        maven-plugin
Group: Networking/WWW
Summary:        maven-plugin module for Jetty

%description    maven-plugin
%{extdesc} %{summary}.

%package        monitor
Group: Networking/WWW
Summary:        monitor module for Jetty

%description    monitor
%{extdesc} %{summary}.

%package        plus
Group: Networking/WWW
Summary:        plus module for Jetty

%description    plus
%{extdesc} %{summary}.

%package        proxy
Group: Networking/WWW
Summary:        proxy module for Jetty

%description    proxy
%{extdesc} %{summary}.

%package        rewrite
Group: Networking/WWW
Summary:        rewrite module for Jetty

%description    rewrite
%{extdesc} %{summary}.

%package        security
Group: Networking/WWW
Summary:        security module for Jetty

%description    security
%{extdesc} %{summary}.

%package        server
Group: Networking/WWW
Summary:        server module for Jetty

%description    server
%{extdesc} %{summary}.

%package        servlet
Group: Networking/WWW
Summary:        servlet module for Jetty

%description    servlet
%{extdesc} %{summary}.

%package        servlets
Group: Networking/WWW
Summary:        servlets module for Jetty

%description    servlets
%{extdesc} %{summary}.

%if %{with spring}
%package        spring
Group: Networking/WWW
Summary:        spring module for Jetty

%description    spring
%{extdesc} %{summary}.
%endif

%package        start
Group: Networking/WWW
Summary:        start module for Jetty

%description    start
%{extdesc} %{summary}.

%package        unixsocket
Group: Networking/WWW
Summary:        unixsocket module for Jetty

%description    unixsocket
%{extdesc} %{summary}.

%package        util
Group: Networking/WWW
Summary:        util module for Jetty
# Utf8Appendable.java is additionally under MIT license
License:        (ASL 2.0 or EPL) and MIT

%description    util
%{extdesc} %{summary}.

%package        util-ajax
Group: Networking/WWW
Summary:        util-ajax module for Jetty

%description    util-ajax
%{extdesc} %{summary}.

%package        webapp
Group: Networking/WWW
Summary:        webapp module for Jetty

%description    webapp
%{extdesc} %{summary}.

%package        xml
Group: Networking/WWW
Summary:        xml module for Jetty

%description    xml
%{extdesc} %{summary}.

%package        websocket-api
Group: Networking/WWW
Summary:        websocket-api module for Jetty

%description    websocket-api
%{extdesc} %{summary}.

%package        websocket-client
Group: Networking/WWW
Summary:        websocket-client module for Jetty

%description    websocket-client
%{extdesc} %{summary}.

%package        websocket-common
Group: Networking/WWW
Summary:        websocket-common module for Jetty

%description    websocket-common
%{extdesc} %{summary}.

%package        websocket-parent
Group: Networking/WWW
Summary:        POM file for jetty-websocket

%description    websocket-parent
%{extdesc} %{summary}.

%package        websocket-server
Group: Networking/WWW
Summary:        websocket-server module for Jetty

%description    websocket-server
%{extdesc} %{summary}.

%package        websocket-servlet
Group: Networking/WWW
Summary:        websocket-servlet module for Jetty

%description    websocket-servlet
%{extdesc} %{summary}.

%package        javax-websocket-client-impl
Group: Networking/WWW
Summary:        javax-websocket-client-impl module for Jetty

%description    javax-websocket-client-impl
%{extdesc} %{summary}.

%package        javax-websocket-server-impl
Group: Networking/WWW
Summary:        javax-websocket-server-impl module for Jetty

%description    javax-websocket-server-impl
%{extdesc} %{summary}.

%if %{with nosql}
%package        nosql
Group: Networking/WWW
Summary:        nosql module for Jetty

%description    nosql
%{extdesc} %{summary}.
%endif

%if %{with osgi}
%package        httpservice
Group: Networking/WWW
Summary:        httpservice module for Jetty

%description    httpservice
%{extdesc} %{summary}.

%package        osgi-boot
Group: Networking/WWW
Summary:        osgi-boot module for Jetty

%description    osgi-boot
%{extdesc} %{summary}.

%package        osgi-boot-warurl
Group: Networking/WWW
Summary:        osgi-boot-warurl module for Jetty

%description    osgi-boot-warurl
%{extdesc} %{summary}.

%package        osgi-project
Group: Networking/WWW
Summary:        osgi-project module for Jetty

%description    osgi-project
%{extdesc} %{summary}.

%package        osgi-boot-jsp
Group: Networking/WWW
Summary:        osgi-boot-jsp module for Jetty

%description    osgi-boot-jsp
%{extdesc} %{summary}.

%endif # with osgi

%package quickstart
Group: Networking/WWW
Summary:        quickstart module for Jetty

%description quickstart
%{extdesc} %{summary}.

%package alpn-client
Group: Networking/WWW
Summary:        alpn-client module for Jetty

%description alpn-client
%{extdesc} %{summary}.

%package alpn-server
Group: Networking/WWW
Summary:        alpn-server module for Jetty

%description alpn-server
%{extdesc} %{summary}.

%package osgi-alpn
Group: Networking/WWW
Summary:        osgi-alpn module for Jetty

%description osgi-alpn
%{extdesc} %{summary}.

%package jstl
Group: Networking/WWW
Summary:        jstl module for Jetty

%description jstl
%{extdesc} %{summary}.

%package http2-client
Group: Networking/WWW
Summary:        http2-client module for Jetty

%description http2-client
%{extdesc} %{summary}.

%package http2-common
Group: Networking/WWW
Summary:        http2-common module for Jetty

%description http2-common
%{extdesc} %{summary}.

%package http2-hpack
Group: Networking/WWW
Summary:        http2-hpack module for Jetty

%description http2-hpack
%{extdesc} %{summary}.

%package http2-http-client-transport
Group: Networking/WWW
Summary:        http2-http-client-transport module for Jetty

%description http2-http-client-transport
%{extdesc} %{summary}.

%package http2-server
Group: Networking/WWW
Summary:        http2-server module for Jetty

%description http2-server
%{extdesc} %{summary}.


%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
# some MIT-licensed code (from Utf8Appendable) is used to generate javadoc
License:        (ASL 2.0 or EPL) and MIT
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}.project-%{name}-%{version}.%{addver}

%patch1 -p1

find . -name "*.?ar" -exec rm {} \;
find . -name "*.class" -exec rm {} \;

# Use proper groupId for apache ant
%pom_xpath_replace "pom:groupId[text()='ant']" "<groupId>org.apache.ant</groupId>" jetty-ant/pom.xml

%pom_change_dep -r "javax.transaction:javax.transaction-api" "org.jboss.spec.javax.transaction:jboss-transaction-api_1.2_spec"
%pom_remove_dep "com.sun.net.httpserver:http" jetty-http-spi

# glassfish-jstl has licensing issues
%pom_change_dep -r "org.glassfish.web:javax.servlet.jsp.jstl" "javax.servlet:jstl"

%pom_change_dep -r org.mortbay.jasper:apache-jsp org.apache.tomcat:tomcat-jasper

%pom_remove_plugin ":clirr-maven-plugin" jetty-websocket
%pom_remove_plugin ":maven-eclipse-plugin" jetty-osgi

# it tries to execute start.jar, but can't find its config that wasn't
# installed yet
%pom_remove_plugin ":exec-maven-plugin" jetty-distribution

# txt artifact - not installable
%pom_remove_plugin ":jetty-version-maven-plugin"
%pom_xpath_remove "pom:artifactItem[pom:classifier='version']" jetty-distribution

# it doesn't like the trailing semicolon
sed -i 's#;</Export-Package>#</Export-Package>#' jetty-http2/http2-common/pom.xml

# Disable test and example artifacts
# they need more dependencies then we have time for right now :-)
# and also xmvn currently doesn't support .war
%pom_disable_module tests
%pom_disable_module examples
%pom_disable_module aggregates/jetty-all
%pom_disable_module test-jetty-osgi jetty-osgi/pom.xml
%pom_disable_module test-jetty-osgi-context jetty-osgi/pom.xml
%pom_disable_module test-jetty-osgi-webapp jetty-osgi/pom.xml
%pom_disable_module http2-alpn-tests jetty-http2/pom.xml
%pom_disable_module test-cdi-webapp jetty-cdi

# Since tests are disabled, we don't have some jars
%pom_remove_dep :test-jetty-webapp jetty-distribution/pom.xml
%pom_remove_dep :test-proxy-webapp jetty-distribution/pom.xml
%pom_remove_dep :example-async-rest-webapp jetty-distribution/pom.xml
%pom_xpath_remove "pom:artifactItem[pom:artifactId[text()='test-jetty-webapp']]" jetty-distribution/pom.xml
%pom_xpath_remove "pom:artifactItem[pom:artifactId[text()='test-proxy-webapp']]" jetty-distribution/pom.xml
%pom_xpath_remove "pom:artifactItem[pom:artifactId[text()='example-async-rest-webapp']]" jetty-distribution/pom.xml
%pom_xpath_remove "pom:artifactItem[pom:artifactId[text()='test-jaas-webapp']]" jetty-distribution/pom.xml
%pom_xpath_remove "pom:artifactItem[pom:artifactId[text()='test-jndi-webapp']]" jetty-distribution/pom.xml
%pom_xpath_remove "pom:artifactItem[pom:artifactId[text()='test-spec-webapp']]" jetty-distribution/pom.xml
%pom_remove_plugin :maven-dependency-plugin jetty-http2/http2-http-client-transport/pom.xml

# We don't have asciidoctor-maven-plugin
%pom_disable_module jetty-documentation

# Missing jars (jetty-setuid-java-1.0.0.jar,jetty-setuid-java-1.0.0-config.jar)
%pom_xpath_remove "pom:execution[pom:id[text()='copy-setuid-deps']]" jetty-distribution/pom.xml
# test-jaas-webapp artifact is disabled
%pom_xpath_remove "pom:execution[pom:id[text()='unpack-test-jaas-config']]" jetty-distribution/pom.xml
%pom_xpath_remove "pom:execution[pom:id[text()='unpack-test-jndi-config']]" jetty-distribution/pom.xml
%pom_xpath_remove "pom:execution[pom:id[text()='unpack-test-spec-config']]" jetty-distribution/pom.xml

# We don't have this plugin yet
%pom_remove_plugin :findbugs-maven-plugin jetty-websocket/pom.xml

# enforcer plugin constantly complains
%pom_remove_plugin :maven-enforcer-plugin

# Prevents problem with "Reporting mojo's can only be called from
# ReportDocumentRender". Investigate proper fix some other time?
%pom_remove_plugin :maven-pmd-plugin

# License plugin may be useful for upstream, but it has no use in
# Fedora.
%pom_remove_plugin :maven-license-plugin

# Remove unpack-config-deps from distribution
#
# This is needed because original code used classifiers to select subset
# of artifacts. Unfortunately there seems to be a weird bug affecting even
# upstream maven when this goes outside of reactor resolver. Or perhaps
# this is a weird feature.
#
# Our resolver obviously can't handle this so we have to unpack these
# manually before building distribution
%pom_xpath_remove "pom:execution[pom:id[text()='unpack-config-deps']]" jetty-distribution

# Disable default-jar executions of maven-jar-plugin in certain Jetty
# modules, which define their own executions of the plugin.  This
# avoids problems with version 3.0.0 of the plugin.
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions" "
      <execution>
        <id>default-jar</id>
        <phase>skip</phase>
      </execution>" \
    apache-jsp \
    jetty-infinispan \
    jetty-osgi/jetty-osgi-boot \
    jetty-osgi/jetty-osgi-boot-jsp \
    jetty-osgi/jetty-osgi-boot-warurl \
    jetty-osgi/jetty-osgi-httpservice \
    jetty-websocket/websocket-common \

# We don't have gcloud-java-datastore in Fedora
%pom_disable_module jetty-gcloud
%pom_remove_dep :jetty-gcloud-session-manager jetty-distribution

# we don't have com.googlecode.xmemcached:xmemcached yet
%pom_disable_module jetty-memcached

# Disable OSGi
%if %{without osgi}
%pom_disable_module jetty-osgi
%endif

# Disable NoSQL
%if %{without nosql}
%pom_disable_module jetty-nosql
%endif

# Disable Spring
%if %{without spring}
%pom_disable_module jetty-spring
%endif

cp %{SOURCE6} .

# the default location is not allowed by SELinux
sed -i '/<SystemProperty name="jetty.state"/d' \
    jetty-distribution/src/main/resources/etc/jetty-started.xml

# Looks like all CDDL licensed content in tarball has been replaced,
# we don't need to install this license
rm LICENSE-CONTRIBUTOR/CDDLv1.0.txt

%build
%mvn_package :jetty-distribution __noinstall
# Separate package for main POM file
%mvn_package :jetty-project project

%mvn_package :fcgi-parent __noinstall
%mvn_package :http2-parent __noinstall
%mvn_package :jetty-alpn-parent __noinstall
%mvn_package :jetty-runner __noinstall

%mvn_package org.eclipse.jetty.cdi: jetty-cdi

%mvn_package :apache-jsp jetty-jsp
%mvn_alias :apache-jsp :jetty-jsp

# we don't have all necessary dependencies to run tests
# missing test dep: org.eclipse.jetty.toolchain:jetty-test-helper
%mvn_build -f -s

pushd jetty-distribution
find .. -ipath '*target/*config.jar' | ( while read; do
  unzip $REPLY -x 'META-INF/*' -d target/distribution
done)

cd target/distribution

# Initialize config
java -Djetty.home=. -Djetty.base=. -jar start.jar \
    --add-to-start=deploy,websocket,ext,resources,jsp,jstl,http

ln -sf %{_javadir}/%{name}/%{name}-start.jar start.jar
popd

%install
%mvn_install

# Install jetty home
cp -pr jetty-distribution/target/distribution %{buildroot}%{apphomedir}

# dirs
%if %{with service}
install -dm 755 %{buildroot}%{_bindir}
install -dm 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -dm 755 %{buildroot}%{confdir}
install -dm 755 %{buildroot}%{apphomedir}/start.d
install -dm 755 %{buildroot}%{logdir}
install -dm 755 %{buildroot}%{rundir}
install -dm 755 %{buildroot}%{tempdir}
install -dm 755 %{buildroot}%{appdir}
install -dm 755 %{buildroot}%{_unitdir}

# systemd unit file
cp %{SOURCE5} %{buildroot}%{_unitdir}/

install -pm 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
echo '# Placeholder configuration file.  No default is provided.' > \
     %{buildroot}%{confdir}/jetty.conf

# add dependencies that are missing due to artifact coordinates changes
build-jar-repository %{buildroot}%{apphomedir}/lib/apache-jsp \
           tomcat/jasper tomcat/tomcat-juli \
           tomcat/tomcat-jsp-2.3-api tomcat/tomcat-api tomcat/tomcat-util \
           tomcat-taglibs-standard/taglibs-standard-compat \
           tomcat-taglibs-standard/taglibs-standard-impl \
           tomcat/tomcat-util-scan ecj glassfish-el-api glassfish-el

build-jar-repository %{buildroot}%{apphomedir}/lib/jndi/ jboss-transaction-1.2-api

for jar in %{buildroot}%{_javadir}/%{name}/*.jar; do
        mod=`basename -s .jar $jar`
        target="%{buildroot}%{apphomedir}/lib"
        case $mod in
            *cdi*) target="$target/$mod-%{version}.%{addver}.jar" ;;
            *websocket*) target="$target/websocket/$mod-%{version}.%{addver}.jar" ;;
            *spring*) target="$target/spring/$mod-%{version}.%{addver}.jar" ;;
            *http2*) target="$target/http2/$mod-%{version}.%{addver}.jar" ;;
            *fcgi*) target="$target/fcgi/$mod-%{version}.%{addver}.jar" ;;
            *apache-jsp*) target="$target/apache-jsp/org.eclipse.jetty.$mod-%{version}.%{addver}.jar" ;;
            *monitor*) target="$target/monitor/$mod-%{version}.%{addver}.jar" ;;
            *) target="$target/$mod-%{version}.%{addver}.jar" ;;
        esac
        ln -sf "${jar##%{buildroot}}" "$target"
done

# replace remaining deps
xmvn-subst "%{buildroot}%{apphomedir}/lib"

# ecj doesn't have javapackages metadata in manifest
ln -sf %{_javadir}/ecj.jar %{buildroot}%{apphomedir}/lib/apache-jsp/org.eclipse.jdt.core.compiler.ecj-*.jar

remaining=`find %{buildroot}%{apphomedir}/ -type f -name '*.jar'`
if [ -n "$remaining" ]; then echo "Unsymlinked jars in homedir: $remaining"; exit 1; fi

( cat << EO_RC
JAVA_HOME=/usr/lib/jvm/java
JAVA_OPTIONS=
JETTY_HOME=%{apphomedir}
JETTY_CONSOLE=%{logdir}/jetty-console.log
JETTY_PORT=8080
JETTY_RUN=%{_var}/run/%{name}
JETTY_PID=\$JETTY_RUN/jetty.pid
EO_RC
) > %{buildroot}%{apphomedir}/.jettyrc

mkdir -p %{buildroot}%{_tmpfilesdir}
( cat << EOF
D %{rundir} 0755 %username %{username} -
EOF
) > %{buildroot}%{_tmpfilesdir}/%{name}.conf

rm -fr %{buildroot}%{apphomedir}/logs
ln -s %{logdir} %{buildroot}%{apphomedir}/logs

mv %{buildroot}%{apphomedir}/etc/* %{buildroot}/%{confdir}
rm -fr %{buildroot}%{apphomedir}/etc
ln -s %{confdir} %{buildroot}%{apphomedir}/etc

mv %{buildroot}%{apphomedir}/webapps/* %{buildroot}/%{appdir}
rm -fr %{buildroot}%{apphomedir}/webapps
ln -s %{appdir} %{buildroot}%{apphomedir}/webapps

rm %{buildroot}%{apphomedir}/*.txt  %{buildroot}%{apphomedir}/*.html

# Here jetty is going to put its runtime data.
# See: https://bugzilla.redhat.com/show_bug.cgi?id=845993
ln -sf %{rundir} %{buildroot}%{apphomedir}/work

# replace the startup script with ours
cp -p %{SOURCE1} %{buildroot}%{apphomedir}/bin/jetty.sh

# touching all ghosts; hack for rpm 4.0.4
for rpm_404_ghost in %{rundir}
do
    mkdir -p %buildroot`dirname "$rpm_404_ghost"`
    touch %buildroot"$rpm_404_ghost"
done

mkdir -p $RPM_BUILD_ROOT`dirname /etc/default/jetty`
touch $RPM_BUILD_ROOT/etc/default/jetty
install -D -m 755 %{S:45} %buildroot%_initdir/%name


%pre
getent group %username >/dev/null || groupadd -f  -r %username
if ! getent passwd %username >/dev/null ; then
    if ! getent passwd %jtuid >/dev/null ; then
      useradd -r  -g %username -d %apphomedir -s /bin/sh \
      -c "Jetty web server" %username
    else
      useradd -r -g %username -d %apphomedir -s /bin/sh \
      -c "Jetty web server" %username
    fi
fi
exit 0

%post
%post_service jetty

%preun
%preun_service jetty

%endif # with service
%files
%if %{with service}
%{_tmpfilesdir}/%{name}.conf
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{confdir}
%dir %{jettylibdir}
%dir %{jettycachedir}
%{apphomedir}
%attr(744, jetty, jetty) %{apphomedir}/bin/jetty.sh
%attr(755, jetty, jetty) %{logdir}
%attr(755, jetty, jetty) %{tempdir}
%ghost %dir %attr(755, jetty, jetty) %{rundir}
%{appdir}
%{_unitdir}/%{name}.service
%endif # with service
%dir %{_javadir}/%{name}
%config(noreplace,missingok) /etc/default/jetty
%_initdir/%name

%files project -f .mfiles-project
%doc NOTICE.txt README.TXT VERSION.txt LICENSE-eplv10-aslv20.html LICENSE-CONTRIBUTOR

%files annotations -f .mfiles-jetty-annotations
%files ant -f .mfiles-jetty-ant
%files cdi -f .mfiles-jetty-cdi
%files client -f .mfiles-jetty-client
%files continuation -f .mfiles-jetty-continuation
%files deploy -f .mfiles-jetty-deploy
%files fcgi-client -f .mfiles-fcgi-client
%files fcgi-server -f .mfiles-fcgi-server
%files http -f .mfiles-jetty-http
%files http-spi -f .mfiles-jetty-http-spi
%files io -f .mfiles-jetty-io
%files infinispan -f .mfiles-jetty-infinispan
%files jaas -f .mfiles-jetty-jaas
%files jaspi -f .mfiles-jetty-jaspi
%files jmx -f .mfiles-jetty-jmx
%files jndi -f .mfiles-jetty-jndi
%files jsp -f .mfiles-jetty-jsp
%files jstl -f .mfiles-apache-jstl
%files jspc-maven-plugin -f .mfiles-jetty-jspc-maven-plugin
%files maven-plugin -f .mfiles-jetty-maven-plugin
%files monitor -f .mfiles-jetty-monitor
%files plus -f .mfiles-jetty-plus
%files proxy -f .mfiles-jetty-proxy
%files quickstart -f .mfiles-jetty-quickstart
%files rewrite -f .mfiles-jetty-rewrite
%files security -f .mfiles-jetty-security
%files server -f .mfiles-jetty-server
%files servlet -f .mfiles-jetty-servlet
%files servlets -f .mfiles-jetty-servlets
%files start -f .mfiles-jetty-start
%files unixsocket -f .mfiles-jetty-unixsocket
%files util -f .mfiles-jetty-util
%doc NOTICE.txt README.TXT VERSION.txt LICENSE-eplv10-aslv20.html LICENSE-CONTRIBUTOR
%doc LICENSE-MIT
%files util-ajax -f .mfiles-jetty-util-ajax
%files webapp -f .mfiles-jetty-webapp
%files xml -f .mfiles-jetty-xml
%files websocket-api -f .mfiles-websocket-api
%files websocket-client -f .mfiles-websocket-client
%files websocket-common -f .mfiles-websocket-common
%files websocket-parent -f .mfiles-websocket-parent
%files websocket-server -f .mfiles-websocket-server
%files websocket-servlet -f .mfiles-websocket-servlet
%files javax-websocket-client-impl -f .mfiles-javax-websocket-client-impl
%files javax-websocket-server-impl -f .mfiles-javax-websocket-server-impl
%files alpn-client -f .mfiles-jetty-alpn-client
%files alpn-server -f .mfiles-jetty-alpn-server
%files osgi-alpn -f .mfiles-jetty-osgi-alpn
%files http2-client -f .mfiles-http2-client
%files http2-common -f .mfiles-http2-common
%files http2-hpack -f .mfiles-http2-hpack
%files http2-http-client-transport -f .mfiles-http2-http-client-transport
%files http2-server -f .mfiles-http2-server

%if %{with nosql}
%files nosql -f .mfiles-jetty-nosql
%endif

%if %{with osgi}
%files httpservice -f .mfiles-jetty-httpservice
%files osgi-project -f .mfiles-jetty-osgi-project
%files osgi-boot -f .mfiles-jetty-osgi-boot
%files osgi-boot-warurl -f .mfiles-jetty-osgi-boot-warurl
%files osgi-boot-jsp -f .mfiles-jetty-osgi-boot-jsp
%endif

%if %{with spring}
%files spring -f .mfiles-jetty-spring
%endif

%files javadoc -f .mfiles-javadoc
%doc NOTICE.txt LICENSE*

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 9.4.0-alt1_0.2.M0jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 9.3.7-alt1_2.v20160115jpp8
- new version

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 9.3.0-alt1_6jpp8
- new version

* Wed Apr 24 2013 Repocop Q. A. Robot <repocop@altlinux.org> 8.1.5-alt4_6jpp7.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * systemd-files-in-etc for jetty

* Mon Mar 25 2013 Igor Vlasenko <viy@altlinux.ru> 8.1.5-alt4_6jpp7
- fixed init script

* Sun Mar 24 2013 Igor Vlasenko <viy@altlinux.ru> 8.1.5-alt3_6jpp7
- fixed scripts and provides

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 8.1.5-alt2_6jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 8.1.5-alt1_6jpp7
- fc update

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.5-alt1_5jpp7
- new version (closes: #27671)

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.5-alt1_2jpp7
- prebuild using manual depmap 

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.0-alt4_4jpp7
- fixed build

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.0-alt3_4jpp7
- rebuild

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.0-alt2_4jpp7
- fixed %pre

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.0-alt1_4jpp7
- full version

