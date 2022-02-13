Group: Networking/WWW
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jetty
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
%global logdir      %{_localstatedir}/log/%{name}
%global apphomedir     %{_datadir}/%{name}
%global jettycachedir %{_localstatedir}/cache/%{name}
%global tempdir     %{jettycachedir}/temp
%global rundir      %{_localstatedir}/run/%{name}
%global jettylibdir %{_localstatedir}/lib/%{name}
%global appdir      %{jettylibdir}/webapps


%global addver  .v20210413

# minimal version required to build eclipse and thermostat
# eclipse needs: util, server, http, continuation, io, security, servlet
# thermostat needs: server, jaas, webapp
# above modules need: jmx, xml
%bcond_without  jp_minimal

Name:           jetty
Version:        9.4.40
Release:        alt1_2jpp11
Summary:        Java Webserver and Servlet Container

# Jetty is dual licensed under both ASL 2.0 and EPL 1.0, see NOTICE.txt
License:        ASL 2.0 or EPL-1.0
URL:            http://www.eclipse.org/jetty/
Source0:        https://github.com/eclipse/%{name}.project/archive/%{name}-%{version}%{addver}.tar.gz
Source1:        jetty.sh
Source3:        jetty.logrotate
Source5:        %{name}.service
# MIT license text taken from Utf8Appendable.java
Source6:        LICENSE-MIT

Patch1:         0001-Distro-jetty.home.patch
Patch2:         0002-Port-to-servlet-api-4-5.patch

BuildRequires:  maven-local
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)

%if %{without jp_minimal}
BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jnr-unixsocket)
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(javax.enterprise:cdi-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(javax.servlet.jsp:javax.servlet.jsp-api)
BuildRequires:  mvn(javax.servlet:jstl)
BuildRequires:  mvn(javax.transaction:javax.transaction-api)
BuildRequires:  mvn(javax.websocket:javax.websocket-api)
BuildRequires:  mvn(javax.websocket:javax.websocket-client-api)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-launcher)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-war-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-tools-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  mvn(org.apache.taglibs:taglibs-standard-impl)
BuildRequires:  mvn(org.apache.taglibs:taglibs-standard-spec)
BuildRequires:  mvn(org.apache.tomcat:tomcat-jasper)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty.alpn:alpn-api)
BuildRequires:  mvn(org.eclipse.jetty.orbit:javax.mail.glassfish)
BuildRequires:  mvn(org.eclipse.jetty.orbit:javax.security.auth.message)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-assembly-descriptors)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-schemas)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-test-helper)
BuildRequires:  mvn(org.jboss.weld.servlet:weld-servlet-core)
BuildRequires:  mvn(org.mongodb:mongo-java-driver)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.slf4j:slf4j-api)

BuildRequires:  mvn(org.mortbay.jetty.alpn:alpn-boot)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-artifact-remote-resources)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-distribution-remote-resources)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-test-policy)
#BuildRequires:  mvn(org.eclipse.jetty.toolchain.setuid:jetty-setuid-java)
BuildRequires:  maven-javadoc-plugin
BuildRequires:  glassfish-el
BuildRequires:  libsystemd-devel libudev-devel systemd systemd-analyze systemd-homed systemd-networkd systemd-portable systemd-sysvinit
BuildRequires:  junit5

# duplicate providers, choose one
BuildRequires:  jboss-websocket-1.0-api
Requires:       jboss-websocket-1.0-api
%endif

BuildArch:      noarch

# jp_minimal doesn't have main package
%if %{without jp_minimal}
# Explicit requires for javapackages-tools since jetty.sh script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Requires:       %{name}-annotations = %{version}-%{release}
Requires:       %{name}-ant = %{version}-%{release}
Requires:       %{name}-client = %{version}-%{release}
Requires:       %{name}-continuation = %{version}-%{release}
Requires:       %{name}-deploy = %{version}-%{release}
Requires:       %{name}-fcgi-client = %{version}-%{release}
Requires:       %{name}-fcgi-server = %{version}-%{release}
Requires:       %{name}-http = %{version}-%{release}
Requires:       %{name}-http-spi = %{version}-%{release}
Requires:       %{name}-io = %{version}-%{release}
Requires:       %{name}-jaas = %{version}-%{release}
Requires:       %{name}-jaspi = %{version}-%{release}
Requires:       %{name}-jmx = %{version}-%{release}
Requires:       %{name}-jndi = %{version}-%{release}
Requires:       %{name}-jsp = %{version}-%{release}
Requires:       %{name}-jspc-maven-plugin = %{version}-%{release}
Requires:       %{name}-maven-plugin = %{version}-%{release}
Requires:       %{name}-plus = %{version}-%{release}
Requires:       %{name}-proxy = %{version}-%{release}
Requires:       %{name}-rewrite = %{version}-%{release}
Requires:       %{name}-security = %{version}-%{release}
Requires:       %{name}-server = %{version}-%{release}
Requires:       %{name}-servlet = %{version}-%{release}
Requires:       %{name}-servlets = %{version}-%{release}
Requires:       %{name}-start = %{version}-%{release}
Requires:       %{name}-unixsocket = %{version}-%{release}
Requires:       %{name}-util = %{version}-%{release}
Requires:       %{name}-util-ajax = %{version}-%{release}
Requires:       %{name}-webapp = %{version}-%{release}
Requires:       %{name}-xml = %{version}-%{release}
Requires:       %{name}-cdi = %{version}-%{release}
Requires:       %{name}-websocket-api = %{version}-%{release}
Requires:       %{name}-websocket-client = %{version}-%{release}
Requires:       %{name}-websocket-common = %{version}-%{release}
Requires:       %{name}-websocket-server = %{version}-%{release}
Requires:       %{name}-websocket-servlet = %{version}-%{release}
Requires:       %{name}-javax-websocket-client-impl = %{version}-%{release}
Requires:       %{name}-javax-websocket-server-impl = %{version}-%{release}
Requires:       %{name}-nosql = %{version}-%{release}
Requires:       %{name}-quickstart = %{version}-%{release}
Requires:       %{name}-jstl = %{version}-%{release}
Requires:       %{name}-alpn-client = %{version}-%{release}
Requires:       %{name}-alpn-server = %{version}-%{release}
Requires:       %{name}-http2-client = %{version}-%{release}
Requires:       %{name}-http2-common = %{version}-%{release}
Requires:       %{name}-http2-hpack = %{version}-%{release}
Requires:       %{name}-http2-http-client-transport = %{version}-%{release}
Requires:       %{name}-http2-server = %{version}-%{release}

Requires(pre):    shadow-change shadow-check shadow-convert shadow-edit shadow-groups shadow-log shadow-submap shadow-utils
%{?systemd_ordering}


Provides:       group(%username) = %jtuid
Provides:       user(%username) = %jtuid
%endif

# Hazelcast in Fedora is too old for jetty to build against (Added in F29)
Obsoletes:      %{name}-hazelcast < 9.4.18-1
# Infinispan in Fedora is too old for jetty to build against (Added in F31)
Obsoletes:      %{name}-infinispan < 9.4.18-1
# Eclipse no longer available (Added in F31)
Obsoletes:      %{name}-osgi-alpn < 9.4.18-1
Obsoletes:      %{name}-osgi-boot < 9.4.18-1
Obsoletes:      %{name}-osgi-boot-jsp < 9.4.18-1
Obsoletes:      %{name}-osgi-boot-warurl < 9.4.18-1
# Spring framework removed from Fedora (Added in F32)
Obsoletes:      %{name}-spring < 9.4.24-1

%if %{with jp_minimal}
# Remove left-over packages that would have broken deps when built in minimal mode
Obsoletes:      %{name}-project < 9.4.20-1
Obsoletes:      %{name}-annotations < 9.4.20-1
Obsoletes:      %{name}-ant < 9.4.20-1
Obsoletes:      %{name}-cdi < 9.4.20-1
Obsoletes:      %{name}-deploy < 9.4.20-1
Obsoletes:      %{name}-fcgi-client < 9.4.20-1
Obsoletes:      %{name}-fcgi-server < 9.4.20-1
Obsoletes:      %{name}-http-spi < 9.4.20-1
Obsoletes:      %{name}-jaspi < 9.4.20-1
Obsoletes:      %{name}-jndi < 9.4.20-1
Obsoletes:      %{name}-jsp < 9.4.20-1
Obsoletes:      %{name}-jstl < 9.4.20-1
Obsoletes:      %{name}-jspc-maven-plugin < 9.4.20-1
Obsoletes:      %{name}-maven-plugin < 9.4.20-1
Obsoletes:      %{name}-plus < 9.4.20-1
Obsoletes:      %{name}-proxy < 9.4.20-1
Obsoletes:      %{name}-quickstart < 9.4.20-1
Obsoletes:      %{name}-rewrite < 9.4.20-1
Obsoletes:      %{name}-servlets < 9.4.20-1
Obsoletes:      %{name}-start < 9.4.20-1
Obsoletes:      %{name}-unixsocket < 9.4.20-1
Obsoletes:      %{name}-websocket-api < 9.4.20-1
Obsoletes:      %{name}-websocket-client < 9.4.20-1
Obsoletes:      %{name}-websocket-common < 9.4.20-1
Obsoletes:      %{name}-websocket-server < 9.4.20-1
Obsoletes:      %{name}-websocket-servlet < 9.4.20-1
Obsoletes:      %{name}-javax-websocket-client-impl < 9.4.20-1
Obsoletes:      %{name}-javax-websocket-server-impl < 9.4.20-1
Obsoletes:      %{name}-alpn-client < 9.4.20-1
Obsoletes:      %{name}-alpn-server < 9.4.20-1
Obsoletes:      %{name}-http2-client < 9.4.20-1
Obsoletes:      %{name}-http2-common < 9.4.20-1
Obsoletes:      %{name}-http2-hpack < 9.4.20-1
Obsoletes:      %{name}-http2-http-client-transport < 9.4.20-1
Obsoletes:      %{name}-http2-server < 9.4.20-1
Obsoletes:      %{name}-nosql < 9.4.20-1
%endif
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

# packages in jp_minimal set
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

%description    io
%{extdesc} %{summary}.

%package        jaas
Group: Networking/WWW
Summary:        jaas module for Jetty

%description    jaas
%{extdesc} %{summary}.

%package        jsp
Group: Networking/WWW
Summary:        jsp module for Jetty
Requires:       glassfish-el

%description    jsp
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
# Eclipse no longer available (Added in F31)
Obsoletes:      %{name}-httpservice < 9.4.18-1

%description    servlet
%{extdesc} %{summary}.

%package        util
Group: Networking/WWW
Summary:        util module for Jetty
# Utf8Appendable.java is additionally under MIT license
License:        (ASL 2.0 or EPL-1.0) and MIT

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

%package        jmx
Group: Networking/WWW
Summary:        jmx module for Jetty

%description    jmx
%{extdesc} %{summary}.

%package        xml
Group: Networking/WWW
Summary:        xml module for Jetty

%description    xml
%{extdesc} %{summary}.



%if %{without jp_minimal}
%package        project
Group: Development/Java
Summary:        POM files for Jetty
Obsoletes:      %{name}-websocket-parent < 9.4.0-0.4
Provides:       %{name}-websocket-parent = %{version}-%{release}
Obsoletes:      %{name}-osgi-project < 9.4.0-0.4
Provides:       %{name}-osgi-project = %{version}-%{release}

%description    project
%{extdesc} %{summary}.

%package        deploy
Group: Networking/WWW
Summary:        deploy module for Jetty

%description    deploy
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

%package        fcgi-client
Group: Networking/WWW
Summary:        FastCGI client module for Jetty

%description    fcgi-client
%{extdesc} %{summary}.

%package        fcgi-server
Group: Networking/WWW
Summary:        FastCGI client module for Jetty

%description    fcgi-server
%{extdesc} %{summary}.

%package        jaspi
Group: Networking/WWW
Summary:        jaspi module for Jetty

%description    jaspi
%{extdesc} %{summary}.

%package        jndi
Group: Networking/WWW
Summary:        jndi module for Jetty

%description    jndi
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

%package        servlets
Group: Networking/WWW
Summary:        servlets module for Jetty

%description    servlets
%{extdesc} %{summary}.

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

%package        nosql
Group: Networking/WWW
Summary:        nosql module for Jetty

%description    nosql
%{extdesc} %{summary}.

%package        quickstart
Group: Networking/WWW
Summary:        quickstart module for Jetty

%description    quickstart
%{extdesc} %{summary}.

%package        alpn-client
Group: Networking/WWW
Summary:        alpn-client module for Jetty

%description    alpn-client
%{extdesc} %{summary}.

%package        alpn-server
Group: Networking/WWW
Summary:        alpn-server module for Jetty

%description    alpn-server
%{extdesc} %{summary}.

%package        http2-client
Group: Networking/WWW
Summary:        http2-client module for Jetty

%description    http2-client
%{extdesc} %{summary}.

%package        http2-common
Group: Networking/WWW
Summary:        http2-common module for Jetty

%description    http2-common
%{extdesc} %{summary}.

%package        http2-hpack
Group: Networking/WWW
Summary:        http2-hpack module for Jetty

%description    http2-hpack
%{extdesc} %{summary}.

%package        http2-http-client-transport
Group: Networking/WWW
Summary:        http2-http-client-transport module for Jetty

%description    http2-http-client-transport
%{extdesc} %{summary}.

%package        http2-server
Group: Networking/WWW
Summary:        http2-server module for Jetty

%description    http2-server
%{extdesc} %{summary}.

%package        jstl
Group: Networking/WWW
Summary:        jstl module for Jetty

%description    jstl
%{extdesc} %{summary}.

%endif

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
# some MIT-licensed code (from Utf8Appendable) is used to generate javadoc
License:        (ASL 2.0 or EPL-1.0) and MIT
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}.project-%{name}-%{version}%{addver}

%patch1 -p1
%patch2 -p1

find . -name "*.?ar" -exec rm {} \;
find . -name "*.class" -exec rm {} \;

# Plugins irrelevant or harmful to building the package
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :spotbugs-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-eclipse-plugin
%pom_remove_plugin -r :license-maven-plugin
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-deploy-plugin
%pom_remove_plugin -r :jacoco-maven-plugin
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :h2spec-maven-plugin

# Unnecessary pom flattening can be skipped
%pom_remove_plugin -r :flatten-maven-plugin jetty-bom

%pom_disable_module aggregates/jetty-all

# Reflective use of classes that might not be present in the JDK should be optional OSGi-wise
%pom_xpath_inject "pom:configuration/pom:instructions" \
"<Import-Package>sun.misc;resolution:=optional,com.sun.nio.file;resolution:=optional,*</Import-Package>"

%pom_remove_dep "com.sun.net.httpserver:http" jetty-http-spi

%pom_change_dep -r org.mortbay.jasper:apache-jsp org.apache.tomcat:tomcat-jasper

%pom_add_dep 'org.junit.jupiter:junit-jupiter-engine:${junit.version}' tests/test-sessions/test-sessions-common

# provided by glassfish-jsp-api that has newer version
%pom_change_dep -r javax.servlet.jsp:jsp-api javax.servlet.jsp:javax.servlet.jsp-api

# txt artifact - not installable
%pom_remove_plugin ":jetty-version-maven-plugin"
%pom_xpath_remove "pom:artifactItem[pom:classifier='version']" jetty-home

# Disable building source release
%pom_xpath_remove 'pom:execution[pom:id="sources"]' jetty-home

# Unwanted JS in javadoc
sed -i '/^\s*\*.*<script>/d' jetty-util/src/main/java/org/eclipse/jetty/util/resource/Resource.java

# only used for integration tests
%pom_remove_plugin :maven-invoker-plugin jetty-jspc-maven-plugin

# These bundles have a dep on Eclipse that is not available on every arch
%pom_disable_module jetty-osgi

# We don't have asciidoctor-maven-plugin
%pom_disable_module jetty-documentation
%pom_remove_dep -r :jetty-documentation
%pom_xpath_remove 'pom:execution[pom:id="unpack-documentation"]' jetty-distribution

%pom_xpath_remove 'pom:artifactItem[pom:artifactId="libsetuid-osx"]' jetty-home/pom.xml

# TODO remove when jetty-setuid is packaged
%pom_xpath_remove "pom:execution[pom:id[text()='copy-setuid-deps']]" jetty-home/pom.xml

# We don't have gcloud-java-datastore in Fedora
%pom_disable_module jetty-gcloud
%pom_disable_module test-gcloud-sessions tests/test-sessions
%pom_remove_dep :jetty-gcloud-session-manager jetty-home

# we don't have com.googlecode.xmemcached:xmemcached yet
%pom_disable_module jetty-memcached
%pom_disable_module test-memcached-sessions tests/test-sessions
%pom_remove_dep :jetty-memcached-sessions jetty-home

# Hazelcast in Fedora is too old to build against
%pom_disable_module jetty-hazelcast
%pom_disable_module test-hazelcast-sessions tests/test-sessions
%pom_remove_dep :jetty-hazelcast jetty-home

# Infinispan in Fedora is too old to build against
%pom_disable_module jetty-infinispan
%pom_disable_module test-infinispan-sessions tests/test-sessions
%pom_remove_dep :infinispan-embedded jetty-home
%pom_remove_dep :infinispan-embedded-query jetty-home
%pom_remove_dep :infinispan-remote jetty-home
%pom_remove_dep :infinispan-remote-query jetty-home
%pom_xpath_remove "pom:execution[pom:id='unpack-infinispan-config']" jetty-home

# Springframework not available in Fedora
%pom_disable_module jetty-spring

# Not currently able to build tests, so can't build benchmarks
%pom_disable_module jetty-jmh

# Distribution tests require internet access, so disable
%pom_disable_module test-distribution tests

# missing conscrypt
%pom_disable_module jetty-alpn-conscrypt-server jetty-alpn
%pom_disable_module jetty-alpn-conscrypt-client jetty-alpn
%pom_remove_dep -r :jetty-alpn-conscrypt-server
%pom_remove_dep -r :jetty-alpn-conscrypt-client
rm -fr examples/embedded/src/main/java/org/eclipse/jetty/embedded/ManyConnectors.java

cp %{SOURCE6} .

# the default location is not allowed by SELinux
sed -i '/<SystemProperty name="jetty.state"/d' \
    jetty-home/src/main/resources/etc/jetty-started.xml

%if %{with jp_minimal}
# remote-resources only copies about.html
%pom_remove_plugin :maven-remote-resources-plugin
# packages module configs, we don't need those in minimal
%pom_remove_plugin :maven-assembly-plugin
# only useful when tests are enabled (copies test deps)
%pom_remove_plugin :maven-dependency-plugin jetty-client

%pom_disable_module jetty-ant
%pom_disable_module jetty-http2
%pom_disable_module jetty-fcgi
%pom_disable_module jetty-websocket
%pom_disable_module jetty-servlets
%pom_disable_module apache-jsp
%pom_disable_module apache-jstl
%pom_disable_module jetty-maven-plugin
%pom_disable_module jetty-jspc-maven-plugin
%pom_disable_module jetty-deploy
%pom_disable_module jetty-start
%pom_disable_module jetty-plus
%pom_disable_module jetty-annotations
%pom_disable_module jetty-jndi
%pom_disable_module jetty-cdi
%pom_disable_module jetty-proxy
%pom_disable_module jetty-jaspi
%pom_disable_module jetty-rewrite
%pom_disable_module jetty-nosql
%pom_disable_module jetty-unixsocket
%pom_disable_module tests
%pom_disable_module examples
%pom_disable_module jetty-quickstart
%pom_disable_module jetty-distribution
%pom_disable_module jetty-runner
%pom_disable_module jetty-http-spi
%pom_disable_module jetty-alpn
%pom_disable_module jetty-home
%pom_disable_module jetty-openid

%endif

%build
%mvn_package :jetty-home __noinstall
%mvn_package :jetty-distribution __noinstall
%mvn_package :build-resources __noinstall

# Separate package for POMs
%if %{without jp_minimal}
%mvn_package ':*-project' project
%mvn_package ':*-parent' project
%mvn_package ':*-bom' project
%else
%mvn_package ':*-project' __noinstall
%mvn_package ':*-parent' __noinstall
%mvn_package ':*-bom' __noinstall
%endif

# artifact used by demo
%mvn_package :test-mock-resources

%mvn_package ':test-*' __noinstall
%mvn_package ':*-tests' __noinstall
%mvn_package ':*-it' __noinstall
%mvn_package ':example-*' __noinstall
%mvn_package org.eclipse.jetty.tests: __noinstall
%mvn_package ::war: __noinstall
%mvn_package :jetty-runner __noinstall

%mvn_package org.eclipse.jetty.cdi: jetty-cdi

%mvn_package ':jetty-alpn*-client' jetty-alpn-client
%mvn_package ':jetty-alpn*-server' jetty-alpn-server


%mvn_package :apache-jsp jetty-jsp
%mvn_alias :apache-jsp :jetty-jsp

# we don't have all necessary dependencies to run tests
# missing test dep: org.eclipse.jetty.toolchain:jetty-perf-helper
%mvn_build -f -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install

# jp_minimal version doesn't contain main package
%if %{without jp_minimal}
# Install jetty home
cp -pr jetty-distribution/target/distribution %{buildroot}%{apphomedir}

# dirs
install -dm 755 %{buildroot}%{_bindir}
install -dm 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -dm 755 %{buildroot}%{confdir}
install -dm 755 %{buildroot}%{apphomedir}/start.d
install -dm 755 %{buildroot}%{logdir}
install -dm 755 %{buildroot}%{rundir}
install -dm 755 %{buildroot}%{tempdir}
install -dm 755 %{buildroot}%{jettylibdir}
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
           tomcat/tomcat-util-scan glassfish-el-api glassfish-el

# ecj doesn't have javapackages metadata in manifest, remove when fixed
ecj=`echo %{buildroot}%{apphomedir}/lib/apache-jsp/org.eclipse.jdt.ecj-*.jar`
rm $ecj

# substitute dependency jars (keep start.jar with shaded jetty util)
xmvn-subst -s -L -R %{buildroot} %{buildroot}%{apphomedir}/lib

# ecj doesn't have javapackages metadata in manifest, remove when fixed
ln -sf %{_javadir}/ecj.jar $ecj

# TODO uncomment when jetty-setuid is packaged
# test -e %{_jnidir}/jetty-setuid/libsetuid-linux.so
# ln -sf %{_jnidir}/jetty-setuid/libsetuid-linux.so %{buildroot}%{apphomedir}/lib/setuid/

( cat << EO_RC
JAVA_HOME=/usr/lib/jvm/java
JAVA_OPTIONS=
JETTY_HOME=%{apphomedir}
JETTY_CONSOLE=%{logdir}/jetty-console.log
JETTY_PORT=8080
JETTY_RUN=%{_localstatedir}/run/%{name}
JETTY_PID=\$JETTY_RUN/jetty.pid
EO_RC
) > %{buildroot}%{apphomedir}/.jettyrc

mkdir -p %{buildroot}%{_tmpfilesdir}
( cat << EOF
D %{rundir} 0755 %username %{username} -
EOF
) > %{buildroot}%{_tmpfilesdir}/%{name}.conf

rm -r %{buildroot}%{apphomedir}/logs
ln -s %{logdir} %{buildroot}%{apphomedir}/logs

mv %{buildroot}%{apphomedir}/etc/* %{buildroot}/%{confdir}/
rm -r %{buildroot}%{apphomedir}/etc
ln -s %{confdir} %{buildroot}%{apphomedir}/etc

mv %{buildroot}%{apphomedir}/webapps %{buildroot}%{appdir}
ln -s %{appdir} %{buildroot}%{apphomedir}/webapps

rm %{buildroot}%{apphomedir}/*.txt  %{buildroot}%{apphomedir}/*.html

# Here jetty is going to put its runtime data.
# See: https://bugzilla.redhat.com/show_bug.cgi?id=845993
ln -sf %{rundir} %{buildroot}%{apphomedir}/work

# replace the startup script with ours
cp -p %{SOURCE1} %{buildroot}%{apphomedir}/bin/jetty.sh
for rpm404_ghost in %{rundir}
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done

mkdir -p $RPM_BUILD_ROOT`dirname /etc/default/jetty`
touch $RPM_BUILD_ROOT/etc/default/jetty
install -D -m 755 %{S:45} %buildroot%_initdir/%name


# NOTE: %if %{without jp_minimal} still in effect

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

%endif
%files client -f .mfiles-jetty-client
%files continuation -f .mfiles-jetty-continuation
%files jaas -f .mfiles-jetty-jaas
%files io -f .mfiles-jetty-io
%files server -f .mfiles-jetty-server
%files servlet -f .mfiles-jetty-servlet
%files util -f .mfiles-jetty-util
%doc --no-dereference LICENSE NOTICE.txt LICENSE-MIT
%files util-ajax -f .mfiles-jetty-util-ajax
%files webapp -f .mfiles-jetty-webapp
%files jmx -f .mfiles-jetty-jmx
%files xml -f .mfiles-jetty-xml
%files http -f .mfiles-jetty-http
%files security -f .mfiles-jetty-security

%if %{with jp_minimal}
%files
# Empty metapackage in minimal mode
%endif

%if %{without jp_minimal}
%files -f .mfiles
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
%_initdir/%name
%config(noreplace,missingok) /etc/default/jetty

%files project -f .mfiles-project
%doc README.md VERSION.txt
%doc --no-dereference LICENSE NOTICE.txt LICENSE-MIT

%files annotations -f .mfiles-jetty-annotations
%files ant -f .mfiles-jetty-ant
%files cdi -f .mfiles-jetty-cdi
%files deploy -f .mfiles-jetty-deploy
%files fcgi-client -f .mfiles-fcgi-client
%files fcgi-server -f .mfiles-fcgi-server
%files http-spi -f .mfiles-jetty-http-spi
%files jaspi -f .mfiles-jetty-jaspi
%files jndi -f .mfiles-jetty-jndi
%files jsp -f .mfiles-jetty-jsp
%files jstl -f .mfiles-apache-jstl
%files jspc-maven-plugin -f .mfiles-jetty-jspc-maven-plugin
%files maven-plugin -f .mfiles-jetty-maven-plugin
%files plus -f .mfiles-jetty-plus
%files proxy -f .mfiles-jetty-proxy
%files quickstart -f .mfiles-jetty-quickstart
%files rewrite -f .mfiles-jetty-rewrite
%files servlets -f .mfiles-jetty-servlets
%files start -f .mfiles-jetty-start
%files unixsocket -f .mfiles-jetty-unixsocket
%files websocket-api -f .mfiles-websocket-api
%files websocket-client -f .mfiles-websocket-client
%files websocket-common -f .mfiles-websocket-common
%files websocket-server -f .mfiles-websocket-server
%files websocket-servlet -f .mfiles-websocket-servlet
%files javax-websocket-client-impl -f .mfiles-javax-websocket-client-impl
%files javax-websocket-server-impl -f .mfiles-javax-websocket-server-impl
%files alpn-client -f .mfiles-jetty-alpn-client
%files alpn-server -f .mfiles-jetty-alpn-server
%files http2-client -f .mfiles-http2-client
%files http2-common -f .mfiles-http2-common
%files http2-hpack -f .mfiles-http2-hpack
%files http2-http-client-transport -f .mfiles-http2-http-client-transport
%files http2-server -f .mfiles-http2-server
%files nosql -f .mfiles-jetty-nosql
%endif

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE.txt LICENSE-MIT

%changelog
* Sun Feb 13 2022 Igor Vlasenko <viy@altlinux.org> 9.4.40-alt1_2jpp11
- do not package init script in minimal version (closes: 41882)

* Tue Jun 15 2021 Igor Vlasenko <viy@altlinux.org> 9.4.40-alt1_1jpp11
- fc update

* Sat Jun 12 2021 Igor Vlasenko <viy@altlinux.org> 9.4.38-alt1_1jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 9.4.31-alt1_3jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 9.4.24-alt1_3.v20191120jpp8
- fc update

* Mon Jul 15 2019 Igor Vlasenko <viy@altlinux.ru> 9.4.19-alt1_1.v20190610jpp8
- new version

* Thu Jun 20 2019 Igor Vlasenko <viy@altlinux.ru> 9.4.11-alt1_3.v20180605jpp8
- new version

* Wed May 30 2018 Igor Vlasenko <viy@altlinux.ru> 9.4.10-alt1_1.v20180503jpp8
- new version

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 9.4.7-alt1_1.v20170914jpp8
- new version

* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 9.4.6-alt2_2.v20170531jpp8
- fixed build with new tomcat

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 9.4.6-alt1_2.v20170531jpp8
- new version

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 9.4.3-alt1_3.v20170317jpp8
- new version

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

