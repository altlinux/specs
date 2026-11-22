%define _unpackaged_files_terminate_build 1
%global xmvn_install_repo jetty-install

Name: jetty
Version: 12.1.15
Release: alt1

Summary: Java Webserver and Servlet Container
License: Apache-2.0 or EPL-2.0
Group: Networking/WWW
URL: https://jetty.org/
VCS: https://github.com/jetty/jetty.project.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: prepare-core-stage.py
Source2: version-text-repositories.xml
Patch0: system-jetty.patch
Patch1: 0001-Reuse-an-already-opened-ZIP-file-system-in-EE-tests.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: git-core
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires: mvn(com.fasterxml.jackson:jackson-bom:pom:)
BuildRequires: mvn(io.netty:netty-bom:pom:)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-commons)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.junit.platform:junit-platform-commons)
BuildRequires: mvn(org.junit.platform:junit-platform-engine)
BuildRequires: mvn(org.eclipse.jetty.toolchain:jetty-test-helper)
BuildRequires: mvn(org.slf4j:slf4j-api:2)
BuildRequires: mvn(org.eclipse.jetty.toolchain:jetty-version-maven-plugin)
BuildRequires: mvn(com.google.jimfs:jimfs)
BuildRequires: mvn(org.awaitility:awaitility)
BuildRequires: mvn(org.bouncycastle:bcpkix-jdk18on)
BuildRequires: mvn(org.eclipse.jetty.toolchain:jetty-perf-helper)
BuildRequires: mvn(org.eclipse.jetty.toolchain:jetty-assembly-descriptors)
BuildRequires: mvn(org.eclipse.jetty.toolchain:jetty-modify-sources-maven-plugin)
BuildRequires: mvn(org.reactivestreams:reactive-streams-tck-flow)
BuildRequires: mvn(org.testng:testng)
BuildRequires: mvn(org.apache.maven.surefire:surefire-junit-platform)
BuildRequires: mvn(org.apache.maven.surefire:surefire-testng)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(org.openjdk.jmh:jmh-core)
BuildRequires: mvn(org.openjdk.jmh:jmh-generator-annprocess)
# The generic Servlet capability can also select Tomcat's API package.
BuildRequires: mvn(jakarta.servlet:jakarta.servlet-api:5.0.0)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(jakarta.servlet:jakarta.servlet-api:6.0.0)
BuildRequires: mvn(jakarta.platform:jakarta.jakartaee-bom:pom:10.0.0)
BuildRequires: mvn(org.codehaus.mojo:flatten-maven-plugin)
BuildRequires: mvn(org.mortbay.jasper:jasper-jsp:pom:)
BuildRequires: mvn(org.mortbay.jasper:mortbay-apache-jsp)
BuildRequires: mvn(jakarta.servlet.jsp.jstl:jakarta.servlet.jsp.jstl-api:1.2.7)
BuildRequires: mvn(org.glassfish.web:jakarta.servlet.jsp.jstl:1.2.6)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-tools-annotations)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-tools-api)
BuildRequires: ant
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.eclipse.jetty.toolchain:jetty-test-policy)
BuildRequires: mvn(net.minidev:json-smart)
BuildRequires: mvn(com.github.luben:zstd-jni)
BuildRequires: mvn(com.googlecode.json-simple:json-simple)
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(org.codehaus.plexus:plexus-xml)
BuildRequires: mvn(jakarta.enterprise:jakarta.enterprise.cdi-api:4.1.0)
BuildRequires: mvn(jakarta.enterprise:jakarta.enterprise.lang-model:4.1.0)
BuildRequires: mvn(jakarta.websocket:jakarta.websocket-api)
BuildRequires: mvn(jakarta.websocket:jakarta.websocket-client-api)
BuildRequires: mvn(jakarta.annotation:jakarta.annotation-api)
BuildRequires: mvn(jakarta.inject:jakarta.inject-api)
BuildRequires: mvn(jakarta.interceptor:jakarta.interceptor-api)
BuildRequires: mvn(jakarta.transaction:jakarta.transaction-api)
BuildRequires: mvn(net.java.dev.jna:jna)
BuildRequires: libquiche0

%description
Jetty provides HTTP clients, servers, servlet engines and JSP support.
This package includes the HTTP/3 and QUIC modules and a JNA binding
for system Quiche.

%package core
Summary: Jetty core parent POM
Group: Development/Java

%description core
Parent POM of the Jetty core modules.

%package build
Summary: Jetty build parent POM
Group: Development/Java

%description build
Parent POM of the Jetty build resources.

%package build-resources
Summary: Jetty shared build resources
Group: Development/Java

%description build-resources
Genuine upstream license and build resources used by Jetty modules.

%package slf4j-impl
Summary: Jetty SLF4J implementation
Group: Development/Java

%description slf4j-impl
Jetty logging implementation for SLF4J.

%package util
Summary: Jetty utilities
Group: Development/Java

%description util
General utility classes used by the Jetty HTTP server and client modules.

%package jmx
Summary: Jetty JMX integration
Group: Development/Java

%description jmx
Jetty managed beans and JMX connector support.

%package io
Summary: Jetty asynchronous IO
Group: Development/Java

%description io
Jetty byte buffers, endpoints, selectors and asynchronous content transport.

%package http
Summary: Jetty HTTP protocol
Group: Development/Java

%description http
Jetty HTTP parsers, generators, fields and multipart protocol support.

%package test-parent
Summary: Jetty test tools parent POM
Group: Development/Java

%description test-parent
Genuine upstream parent POM for the Jetty test tool modules.

%package test-multipart
Summary: Jetty multipart test tools
Group: Development/Java

%description test-multipart
Genuine upstream multipart capture data and assertions used by Jetty tests.

%package util-ajax
Summary: Jetty JSON utilities
Group: Development/Java

%description util-ajax
Jetty JSON parsing and conversion utilities.

%package xml
Summary: Jetty XML configuration
Group: Development/Java

%description xml
Jetty XML configuration and DTD resources.

%package http-tools
Summary: Jetty HTTP test and utility tools
Group: Development/Java

%description http-tools
Jetty HTTP request and response testing utilities.

%package server
Summary: Jetty HTTP server
Group: Development/Java

%description server
Jetty HTTP connectors, handlers and server lifecycle support.

%package session
Summary: Jetty HTTP session management
Group: Development/Java

%description session
Jetty session caches, persistence stores and session lifecycle support.

%package security
Summary: Jetty server authentication and authorization
Group: Development/Java

%description security
Jetty authentication, authorization, JAAS and login service implementations.


%package ee9
Summary: Jetty Jakarta EE9 parent POM
Group: Development/Java

%description ee9
Parent POM of the Jetty Jakarta EE9 modules.

%package ee9-nested
Summary: Jetty EE9 nested server adapter
Group: Development/Java

%description ee9-nested
Jetty nested HTTP server adapter for the Jakarta Servlet 5 API.

%package ee9-security
Summary: Jetty EE9 servlet security
Group: Development/Java

%description ee9-security
Security handlers for Jetty applications using Jakarta Servlet 5.

%package servlet
Summary: Jetty EE9 servlet container
Group: Development/Java

%description servlet
Jetty servlet container for Jakarta Servlet 5 applications.

%package ee8
Summary: Jetty EE8 parent POM
Group: Development/Java

%description ee8
Genuine upstream parent POM and source conversion configuration for Jetty EE8.

%package ee8-nested
Summary: Jetty EE8 nested handlers
Group: Development/Java

%description ee8-nested
Jetty handlers adapted to the legacy Servlet 4 request and response API.

%package ee8-security
Summary: Jetty EE8 servlet security
Group: Development/Java

%description ee8-security
Authentication and authorization for Jetty handlers using Servlet 4.

%package alpn
Summary: Jetty ALPN parent POM
Group: Development/Java

%description alpn
Jetty ALPN parent POM.

%package alpn-client
Summary: Jetty ALPN client API
Group: Development/Java

%description alpn-client
Jetty ALPN client API.

%package compression
Summary: Jetty compression parent POM
Group: Development/Java

%description compression
Jetty compression parent POM.

%package compression-common
Summary: Jetty compression interfaces and codecs
Group: Development/Java

%description compression-common
Jetty compression interfaces and codecs.

%package compression-gzip
Summary: Jetty Gzip support
Group: Development/Java

%description compression-gzip
Jetty Gzip support.

%package compression-server
Summary: Jetty HTTP server compression handler
Group: Development/Java

%description compression-server
Jetty HTTP server compression handler.

%package compression-zstandard
Summary: Jetty Zstandard support
Group: Development/Java

%description compression-zstandard
Jetty Zstandard support.

%package client
Summary: Jetty HTTP client and HTTP/1.1 transport
Group: Development/Java

%description client
Jetty HTTP client and HTTP/1.1 transport.

%package ee8-servlet
Summary: Jetty Servlet 4 container
Group: Development/Java

%description ee8-servlet
Jetty Servlet 4 container.

%package ee8-apache-jsp
Summary: Apache Jasper integration for Jetty EE8
Group: Development/Java

%description ee8-apache-jsp
Jetty EE8 integration with Apache Jasper, including the no-logging variant.

%package ee8-glassfish-jstl
Summary: GlassFish JSTL integration for Jetty EE8
Group: Development/Java

%description ee8-glassfish-jstl
GlassFish JSTL dependencies and resources for the Jetty EE8 environment.

%package ee8-jspc-maven-plugin
Summary: Jetty EE8 JSP compiler Maven plugin
Group: Development/Java

%description ee8-jspc-maven-plugin
The Maven plugin for precompiling JSP pages in the Jetty EE8 environment.

%package alpn-server
Summary: JEP 244 ALPN server support
Group: Networking/WWW

%description alpn-server
JEP 244 ALPN server support.

%package alpn-java-client
Summary: JDK ALPN client provider
Group: Networking/WWW

%description alpn-java-client
JDK ALPN client provider.

%package alpn-java-server
Summary: JDK ALPN server provider
Group: Networking/WWW

%description alpn-java-server
JDK ALPN server provider.

%package proxy
Summary: Jetty HTTP proxy
Group: Networking/WWW

%description proxy
Jetty HTTP proxy.

%package http2
Summary: Jetty HTTP/2 parent POM
Group: Networking/WWW

%description http2
Jetty HTTP/2 parent POM.

%package http2-client
Summary: Jetty HTTP/2 client
Group: Networking/WWW

%description http2-client
Jetty HTTP/2 client.

%package http2-client-transport
Summary: HTTP/2 transport for the Jetty client
Group: Networking/WWW

%description http2-client-transport
HTTP/2 transport for the Jetty client.

%package http2-common
Summary: Common Jetty HTTP/2 implementation
Group: Networking/WWW

%description http2-common
Common Jetty HTTP/2 implementation.

%package http2-hpack
Summary: Jetty HPACK header compression
Group: Networking/WWW

%description http2-hpack
Jetty HPACK header compression.

%package http2-server
Summary: Jetty HTTP/2 server
Group: Networking/WWW

%description http2-server
Jetty HTTP/2 server.

%package websocket
Summary: Jetty WebSocket parent POM
Group: Development/Java

%description websocket
Jetty WebSocket parent POM.

%package websocket-core-client
Summary: Jetty WebSocket protocol client
Group: Development/Java

%description websocket-core-client
Jetty WebSocket protocol client.

%package websocket-core-common
Summary: Jetty Shared WebSocket protocol implementation
Group: Development/Java

%description websocket-core-common
Jetty Shared WebSocket protocol implementation.

%package websocket-core-server
Summary: Jetty WebSocket protocol server
Group: Development/Java

%description websocket-core-server
Jetty WebSocket protocol server.

%package websocket-jetty-api
Summary: Jetty Jetty WebSocket API
Group: Development/Java

%description websocket-jetty-api
Jetty Jetty WebSocket API.

%package websocket-jetty-client
Summary: Jetty Jetty WebSocket client
Group: Development/Java

%description websocket-jetty-client
Jetty Jetty WebSocket client.

%package websocket-jetty-common
Summary: Jetty Shared Jetty WebSocket implementation
Group: Development/Java

%description websocket-jetty-common
Jetty Shared Jetty WebSocket implementation.

%package websocket-jetty-server
Summary: Jetty Jetty WebSocket server
Group: Development/Java

%description websocket-jetty-server
Jetty Jetty WebSocket server.

%package ee
Summary: Jetty Shared EE parent POM
Group: Development/Java

%description ee
Jetty Shared EE parent POM.

%package ee-webapp
Summary: Jetty Shared EE web application support
Group: Development/Java

%description ee-webapp
Jetty Shared EE web application support.

%package ee-test-resources
Summary: Jetty Shared EE test resources
Group: Development/Java

%description ee-test-resources
Jetty Shared EE test resources.

%package ee10
Summary: Jetty EE10 parent POM
Group: Development/Java

%description ee10
Jetty EE10 parent POM.

%package ee10-bom
Summary: Jetty EE10 dependency management BOM
Group: Development/Java

%description ee10-bom
Jetty EE10 dependency management BOM.

%package ee10-servlet
Summary: Jetty EE10 Servlet implementation
Group: Development/Java

%description ee10-servlet
Jetty EE10 Servlet implementation.

%package ee10-webapp
Summary: Jetty EE10 web application implementation
Group: Development/Java

%description ee10-webapp
Jetty EE10 web application implementation.

%package ee10-servlets
Summary: Jetty EE10 Servlet utilities
Group: Development/Java

%description ee10-servlets
Jetty EE10 Servlet utilities.


%package jndi
Summary: Jetty JNDI services
Group: Development/Java

%description jndi
Jetty JNDI services.

%package plus
Summary: Jetty enterprise services
Group: Development/Java

%description plus
Jetty enterprise services.

%package annotations
Summary: Jetty annotation scanning
Group: Development/Java

%description annotations
Jetty annotation scanning.

%package ee10-plus
Summary: Jetty EE10 enterprise services
Group: Development/Java

%description ee10-plus
Jetty EE10 enterprise services.

%package ee10-annotations
Summary: Jetty EE10 annotation processing
Group: Development/Java

%description ee10-annotations
Jetty EE10 annotation processing.

%package ee10-websocket
Summary: Jetty EE10 WebSocket parent POM
Group: Development/Java

%description ee10-websocket
Jetty EE10 WebSocket parent POM.

%package ee10-websocket-jakarta-common
Summary: Jetty EE10 Jakarta WebSocket common implementation
Group: Development/Java

%description ee10-websocket-jakarta-common
Jetty EE10 Jakarta WebSocket common implementation.

%package ee10-websocket-jakarta-client
Summary: Jetty EE10 Jakarta WebSocket client
Group: Development/Java

%description ee10-websocket-jakarta-client
Jetty EE10 Jakarta WebSocket client.

%package ee10-websocket-servlet
Summary: Jetty EE10 WebSocket servlet integration
Group: Development/Java

%description ee10-websocket-servlet
Jetty EE10 WebSocket servlet integration.

%package ee10-websocket-jakarta-server
Summary: Jetty EE10 Jakarta WebSocket server
Group: Development/Java

%description ee10-websocket-jakarta-server
Jetty EE10 Jakarta WebSocket server.

%package http3
Summary: Jetty HTTP/3 parent POM
Group: Development/Java

%description http3
Parent POM of the Jetty HTTP/3 modules.

%package http3-client
Summary: Jetty HTTP/3 client
Group: Development/Java

%description http3-client
Low-level client API for HTTP/3 sessions and streams.

%package http3-client-transport
Summary: Jetty HTTP/3 client transport
Group: Development/Java

%description http3-client-transport
HTTP/3 transport for the Jetty HTTP client.

%package http3-common
Summary: Jetty HTTP/3 protocol
Group: Development/Java

%description http3-common
Shared HTTP/3 frames and session implementation.

%package http3-qpack
Summary: Jetty HTTP/3 QPACK
Group: Development/Java

%description http3-qpack
QPACK header compression and decompression.

%package http3-server
Summary: Jetty HTTP/3 server
Group: Development/Java

%description http3-server
HTTP/3 protocol support for the Jetty server.

%package quic
Summary: Jetty QUIC parent POM
Group: Development/Java

%description quic
Parent POM of the Jetty QUIC modules.

%package quic-api
Summary: Jetty QUIC API
Group: Development/Java

%description quic-api
Interfaces for QUIC connections, streams and sessions.

%package quic-client
Summary: Jetty QUIC client
Group: Development/Java

%description quic-client
Shared QUIC transport support for Jetty clients.

%package quic-common
Summary: Jetty QUIC protocol
Group: Development/Java

%description quic-common
Shared QUIC frame and connection implementation.

%package quic-server
Summary: Jetty QUIC server
Group: Development/Java

%description quic-server
Shared QUIC transport support for Jetty servers.

%package quic-util
Summary: Jetty QUIC utilities
Group: Development/Java

%description quic-util
Utilities for working with the QUIC wire format.

%package quic-quiche
Summary: Jetty Quiche parent POM
Group: Development/Java

%description quic-quiche
Parent POM of the Jetty Quiche modules.

%package quic-quiche-common
Summary: Jetty Quiche protocol
Group: Development/Java

%description quic-quiche-common
Shared Jetty integration with the Quiche library.

%package quic-quiche-client
Summary: Jetty Quiche client
Group: Development/Java

%description quic-quiche-client
Quiche transport implementation for Jetty clients.

%package quic-quiche-server
Summary: Jetty Quiche server
Group: Development/Java

%description quic-quiche-server
Quiche transport implementation for Jetty servers.

%package quic-quiche-jna
Summary: Jetty Quiche JNA binding
Group: Development/Java
# The JNA binding loads libquiche.so.0 at runtime.
Requires: libquiche0

%description quic-quiche-jna
JNA binding to the system Quiche library.

%prep
%setup -q
%autopatch -p1
rm -f .mvn/maven.config
python3 %SOURCE1

# The selected EE9 modules use the Servlet 5 API from the distribution.
%pom_remove_dep jakarta.platform:jakarta.jakartaee-bom jetty-ee9
%pom_remove_dep org.eclipse.jetty.toolchain:jetty-jakarta-servlet-api \
    jetty-ee9/jetty-ee9-nested
%pom_add_dep jakarta.servlet:jakarta.servlet-api:5.0.0 jetty-ee9/jetty-ee9-nested
sed -i 's/requires transitive jetty.servlet.api;/requires transitive jakarta.servlet;/' \
    jetty-ee9/jetty-ee9-nested/src/main/java/module-info.java

# Gear records the upstream revision in Git's tar PAX header.
# Keep SCM metadata generation usable without a live Git working copy.
scm_revision="$(git get-tar-commit-id < %SOURCE0)"
case "$scm_revision" in
  *[!0-9a-f]*|"") exit 1 ;;
esac
test "${#scm_revision}" -eq 40
%pom_xpath_inject pom:properties \
  "<nonCanonicalRevision>$scm_revision</nonCanonicalRevision>"
%pom_xpath_set \
  "//pom:execution[pom:id='create-git-sha']/pom:configuration/pom:revisionOnScmFailure" \
  '${nonCanonicalRevision}'

# Select the real versioned SLF4J 2 compatibility publication in ALT.
%pom_xpath_set pom:properties/pom:slf4j.version 2

surefire_plugin="pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']"
surefire_config="$surefire_plugin/pom:configuration"

# Preserve test compilation and independent tests; these upstream-tagged
# methods require external networking or expensive/unreliable concurrency.
%pom_xpath_inject "$surefire_config" \
  '<excludedGroups>external,stress,flaky</excludedGroups>' \
  jetty-core/jetty-util/pom.xml

# Keep IO test compilation and ordinary tests. These exact upstream tags
# mark expensive stress and unreliable repeated thread-rejection checks.
%pom_xpath_inject "$surefire_config" \
  '<excludedGroups>stress,Unstable</excludedGroups>' jetty-core/jetty-io

# OpenPojo is absent from the target repository; retain the independent JMX
# tests and narrow test compilation only to the one dependent class.
%pom_remove_dep com.openpojo:openpojo jetty-core/jetty-jmx
%pom_xpath_inject pom:build/pom:plugins \
  "<plugin><artifactId>maven-compiler-plugin</artifactId><configuration> \
    <testExcludes><testExclude>**/PojoTest.java</testExclude></testExcludes> \
    </configuration></plugin>" \
  jetty-core/jetty-jmx

# Only the seven XHTML validation tests require the unavailable schema tool.
# Preserve the other server test classes and ordinary JMH source compilation.
%pom_remove_dep org.eclipse.jetty.toolchain:jetty-xhtml-schemas jetty-core/jetty-server
%pom_xpath_inject pom:build/pom:plugins \
  "<plugin><artifactId>maven-compiler-plugin</artifactId><configuration> \
    <testExcludes><testExclude>**/ResourceListingTest.java</testExclude></testExcludes> \
    </configuration></plugin>" \
  jetty-core/jetty-server
%pom_xpath_inject "$surefire_config" \
  '<excludedGroups>slow</excludedGroups>' jetty-core/jetty-server

# Only the unused JDBC test helper initializes an external MariaDB container.
# Keep all independent session tests and the genuine nonempty tests classifier.
%pom_remove_dep org.testcontainers:testcontainers jetty-core/jetty-session
%pom_remove_dep org.testcontainers:testcontainers-mariadb jetty-core/jetty-session
%pom_xpath_inject pom:build/pom:plugins \
  "<plugin><artifactId>maven-compiler-plugin</artifactId><configuration> \
    <testExcludes><testExclude>**/JdbcTestHelper.java</testExclude></testExcludes> \
    </configuration></plugin>" \
  jetty-core/jetty-session

# Exclude only the ApacheDS-backed LDAP integration class from compilation.
# Independent authentication/authorization/JAAS tests remain enabled.
%pom_xpath_inject pom:build/pom:plugins \
  "<plugin><artifactId>maven-compiler-plugin</artifactId><configuration> \
    <testExcludes><testExclude>**/JAASLdapLoginServiceTest.java</testExclude></testExcludes> \
    </configuration></plugin>" \
  jetty-core/jetty-security

# XMvn resolves target dependencies from the system Java repository.
# Preserve TypeUtilTest's upstream assertion with the actual fixture root.
%pom_xpath_set "$surefire_config/pom:systemPropertyVariables/pom:mavenRepoPath" \
  %_javadir jetty-core/jetty-util/pom.xml

# The target toolchain config descriptor consumes target/config.
# Feed it the genuine filtered output from the upstream resource generator.
config_plugins="//pom:profile[pom:id='config']/pom:build/pom:plugins"
resources_plugin="$config_plugins/pom:plugin[pom:artifactId='maven-resources-plugin']"
copy_resources="$resources_plugin/pom:executions/pom:execution[pom:id='copy-resources']"
%pom_xpath_set "$copy_resources/pom:configuration/pom:outputDirectory" \
  '${project.build.directory}/config'

# Keep the genuine upstream typed version publication in its own layout.
%mvn_config repositories "$(cat %SOURCE2)"
%mvn_file org.eclipse.jetty:jetty-project:txt:version jetty-project-version

%mvn_package :jetty-project:*:*
%mvn_package org.eclipse.jetty:jetty-alpn-server:*:* alpn-server
%mvn_package org.eclipse.jetty:jetty-alpn-java-client:*:* alpn-java-client
%mvn_package org.eclipse.jetty:jetty-alpn-java-server:*:* alpn-java-server
%mvn_package org.eclipse.jetty:jetty-proxy:*:* proxy
%mvn_package org.eclipse.jetty.http2:jetty-http2:*:* http2
%mvn_package org.eclipse.jetty.http2:jetty-http2-client:*:* http2-client
%mvn_package org.eclipse.jetty.http2:jetty-http2-client-transport:*:* http2-client-transport
%mvn_package org.eclipse.jetty.http2:jetty-http2-common:*:* http2-common
%mvn_package org.eclipse.jetty.http2:jetty-http2-hpack:*:* http2-hpack
%mvn_package org.eclipse.jetty.http2:jetty-http2-server:*:* http2-server
%mvn_package org.eclipse.jetty.http2:jetty-http2-tests __noinstall
%mvn_package :jetty-core:*:* core
%mvn_package :build:*:* build
%mvn_package :build-resources:*:* build-resources
%mvn_package :jetty-slf4j-impl:*:* slf4j-impl
%mvn_package :jetty-util:*:* util
%mvn_package :jetty-jmx:*:* jmx
%mvn_package :jetty-io:*:* io
%mvn_package :jetty-http:*:* http
%mvn_package :jetty-util-ajax:*:* util-ajax
%mvn_package :jetty-xml:*:* xml
%mvn_package :jetty-http-tools:*:* http-tools
%mvn_package :jetty-server:*:* server
%mvn_package :jetty-session:*:* session
%mvn_package :jetty-security:*:* security
%mvn_package org.eclipse.jetty.ee9:jetty-ee9:pom:* ee9
%mvn_package org.eclipse.jetty.ee9:jetty-ee9-nested:*:* ee9-nested
%mvn_package org.eclipse.jetty.ee9:jetty-ee9-security:*:* ee9-security
%mvn_package org.eclipse.jetty.ee9:jetty-ee9-servlet:*:* servlet
%mvn_alias org.eclipse.jetty.ee9:jetty-ee9-servlet org.eclipse.jetty:jetty-servlet
%mvn_package org.eclipse.jetty.ee8:jetty-ee8:pom:* ee8
%mvn_package org.eclipse.jetty.ee8:jetty-ee8-nested:*:* ee8-nested
%mvn_package org.eclipse.jetty.ee8:jetty-ee8-security:*:* ee8-security
%mvn_package org.eclipse.jetty.tests:tests:pom:* test-parent
%mvn_package org.eclipse.jetty.tests:jetty-test-multipart:*:* test-multipart
%mvn_package org.eclipse.jetty:jetty-alpn:*:* alpn
%mvn_package org.eclipse.jetty:jetty-alpn-client:*:* alpn-client
%mvn_package org.eclipse.jetty.compression:jetty-compression:*:* compression
%mvn_package org.eclipse.jetty.compression:jetty-compression-common:*:* compression-common
%mvn_package org.eclipse.jetty.compression:jetty-compression-gzip:*:* compression-gzip
%mvn_package org.eclipse.jetty.compression:jetty-compression-server:*:* compression-server
%mvn_package org.eclipse.jetty.compression:jetty-compression-zstandard:*:* compression-zstandard
%mvn_package org.eclipse.jetty:jetty-client:*:* client
%mvn_package org.eclipse.jetty.ee8:jetty-ee8-servlet:*:* ee8-servlet
%mvn_package org.eclipse.jetty.ee8:jetty-ee8-apache-jsp:*:* ee8-apache-jsp
%mvn_package org.eclipse.jetty.ee8:jetty-ee8-glassfish-jstl:*:* ee8-glassfish-jstl
%mvn_package org.eclipse.jetty.ee8:jetty-ee8-jspc-maven-plugin:*:* ee8-jspc-maven-plugin

# These generated container tests need the separate EE8 webapp and annotation
# modules. Preserve their upstream EE9 input.
%pom_remove_dep :jetty-ee8-annotations jetty-ee8/jetty-ee8-glassfish-jstl
%pom_remove_dep :jetty-ee8-webapp jetty-ee8/jetty-ee8-glassfish-jstl
%pom_xpath_inject pom:build/pom:plugins \
  "<plugin><artifactId>maven-compiler-plugin</artifactId><configuration> \
    <testExcludes><testExclude>**/jstl/*.java</testExclude></testExcludes> \
    </configuration></plugin>" \
  jetty-ee8/jetty-ee8-glassfish-jstl

# Kerby KDC is needed only by the offline-unavailable SPNEGO test fixture.
%pom_remove_dep org.apache.kerby:kerb-simplekdc jetty-core/jetty-client
%pom_xpath_inject pom:build/pom:plugins \
  "<plugin><artifactId>maven-compiler-plugin</artifactId><configuration> \
    <testExcludes><testExclude>**/SPNEGOAuthenticationTest.java</testExclude></testExcludes> \
    </configuration></plugin>" \
  jetty-core/jetty-client
%pom_xpath_set pom:properties/pom:jetty-test-policy.version 1.7

# Run the remaining proxy test classes sequentially.
%pom_xpath_inject pom:properties \
  '<junit.jupiter.execution.parallel.enabled>false</junit.jupiter.execution.parallel.enabled>' \
  jetty-core/jetty-proxy


# Preserve the proxy tests at testCompile and omit its intermittent tunnel test.
%pom_xpath_inject "$surefire_config" \
  '<excludedGroups>flaky</excludedGroups>' jetty-core/jetty-proxy
# The HTTP/2 integration tests open concurrent loopback fixtures internally.
# Run their JUnit classes sequentially and leave the internal concurrency intact.
%pom_xpath_inject pom:properties \
  '<junit.jupiter.execution.parallel.enabled>false</junit.jupiter.execution.parallel.enabled>' \
  jetty-core/jetty-http2/jetty-http2-tests
# The Hasher build is offline. Keep both upstream external tests compiled.
%pom_xpath_inject "$surefire_config" \
  '<excludedGroups>external</excludedGroups>' jetty-core/jetty-http2/jetty-http2-tests

%mvn_package org.eclipse.jetty.http3:jetty-http3:*:* http3
%mvn_package org.eclipse.jetty.http3:jetty-http3-client:*:* http3-client
%mvn_package org.eclipse.jetty.http3:jetty-http3-client-transport:*:* http3-client-transport
%mvn_package org.eclipse.jetty.http3:jetty-http3-common:*:* http3-common
%mvn_package org.eclipse.jetty.http3:jetty-http3-qpack:*:* http3-qpack
%mvn_package org.eclipse.jetty.http3:jetty-http3-server:*:* http3-server
%mvn_package org.eclipse.jetty.http3:jetty-http3-tests __noinstall
%mvn_package org.eclipse.jetty.quic:jetty-quic:*:* quic
%mvn_package org.eclipse.jetty.quic:jetty-quic-api:*:* quic-api
%mvn_package org.eclipse.jetty.quic:jetty-quic-client:*:* quic-client
%mvn_package org.eclipse.jetty.quic:jetty-quic-common:*:* quic-common
%mvn_package org.eclipse.jetty.quic:jetty-quic-server:*:* quic-server
%mvn_package org.eclipse.jetty.quic:jetty-quic-util:*:* quic-util
%mvn_package org.eclipse.jetty.quic:jetty-quic-quiche:*:* quic-quiche
%mvn_package org.eclipse.jetty.quic:jetty-quic-quiche-common:*:* quic-quiche-common
%mvn_package org.eclipse.jetty.quic:jetty-quic-quiche-client:*:* quic-quiche-client
%mvn_package org.eclipse.jetty.quic:jetty-quic-quiche-server:*:* quic-quiche-server
%mvn_package org.eclipse.jetty.quic:jetty-quic-quiche-jna:*:* quic-quiche-jna
%mvn_package org.eclipse.jetty.quic:jetty-quic-tests __noinstall

# Exclude the external HTTP/3 suite on JDK21 as well as in the FFM profile.
%pom_add_plugin 'org.apache.maven.plugins:maven-surefire-plugin:${maven.surefire.plugin.version}' \
  jetty-core/jetty-http3/jetty-http3-tests \
  '<configuration><excludedGroups>external</excludedGroups></configuration>'

%mvn_package org.eclipse.jetty.websocket:jetty-websocket:*:* websocket
%mvn_package org.eclipse.jetty.websocket:jetty-websocket-core-client:*:* websocket-core-client
%mvn_package org.eclipse.jetty.websocket:jetty-websocket-core-common:*:* websocket-core-common
%mvn_package org.eclipse.jetty.websocket:jetty-websocket-core-server:*:* websocket-core-server
%mvn_package org.eclipse.jetty.websocket:jetty-websocket-jetty-api:*:* websocket-jetty-api
%mvn_package org.eclipse.jetty.websocket:jetty-websocket-jetty-client:*:* websocket-jetty-client
%mvn_package org.eclipse.jetty.websocket:jetty-websocket-jetty-common:*:* websocket-jetty-common
%mvn_package org.eclipse.jetty.websocket:jetty-websocket-jetty-server:*:* websocket-jetty-server
%mvn_package org.eclipse.jetty.websocket:jetty-websocket-core-tests __noinstall
%mvn_package org.eclipse.jetty.websocket:jetty-websocket-jetty-tests __noinstall
%pom_remove_dep org.testcontainers:testcontainers \
  jetty-core/jetty-websocket/jetty-websocket-core-tests
%pom_remove_dep org.testcontainers:testcontainers-junit-jupiter \
  jetty-core/jetty-websocket/jetty-websocket-core-tests
%pom_xpath_inject pom:build/pom:plugins \
  "<plugin><artifactId>maven-compiler-plugin</artifactId><configuration> \
    <testExcludes><testExclude>**/AutobahnTests.java</testExclude></testExcludes> \
    </configuration></plugin>" \
  jetty-core/jetty-websocket/jetty-websocket-core-tests

# PathMatchers is unavailable in the packaged Jetty test helper.
%pom_xpath_inject pom:build/pom:plugins \
  "<plugin><artifactId>maven-compiler-plugin</artifactId><configuration> \
    <testExcludes><testExclude>**/TempDirTest.java</testExclude></testExcludes> \
    </configuration></plugin>" \
  jetty-ee10/jetty-ee10-webapp

# MavenPaths is unavailable in the packaged Jetty test helper.
%pom_xpath_inject pom:build/pom:plugins \
  "<plugin><artifactId>maven-compiler-plugin</artifactId><configuration> \
    <testExcludes><testExclude>**/TestAnnotationConfiguration.java</testExclude></testExcludes> \
    </configuration></plugin>" \
  jetty-ee10/jetty-ee10-annotations

%mvn_package org.eclipse.jetty.ee:jetty-ee:*:* ee
%mvn_package org.eclipse.jetty.ee:jetty-ee-webapp:*:* ee-webapp
%mvn_package org.eclipse.jetty.ee:jetty-ee-test-resources:*:* ee-test-resources
%mvn_package org.eclipse.jetty.ee10:jetty-ee10:*:* ee10
%mvn_package org.eclipse.jetty.ee10:jetty-ee10-bom:*:* ee10-bom
%mvn_package org.eclipse.jetty.ee10:jetty-ee10-servlet:*:* ee10-servlet
%mvn_package org.eclipse.jetty.ee10:jetty-ee10-webapp:*:* ee10-webapp
%mvn_package org.eclipse.jetty.ee10:jetty-ee10-servlets:*:* ee10-servlets

%mvn_package org.eclipse.jetty:jetty-jndi:*:* jndi
%mvn_package org.eclipse.jetty:jetty-plus:*:* plus
%mvn_package org.eclipse.jetty:jetty-annotations:*:* annotations
%mvn_package org.eclipse.jetty.ee10:jetty-ee10-plus:*:* ee10-plus
%mvn_package org.eclipse.jetty.ee10:jetty-ee10-annotations:*:* ee10-annotations
%mvn_package org.eclipse.jetty.ee10.websocket:jetty-ee10-websocket:*:* ee10-websocket
%mvn_package org.eclipse.jetty.ee10.websocket:jetty-ee10-websocket-jakarta-common:*:* \
  ee10-websocket-jakarta-common
%mvn_package org.eclipse.jetty.ee10.websocket:jetty-ee10-websocket-jakarta-client:*:* \
  ee10-websocket-jakarta-client
%mvn_package org.eclipse.jetty.ee10.websocket:jetty-ee10-websocket-servlet:*:* \
  ee10-websocket-servlet
%mvn_package org.eclipse.jetty.ee10.websocket:jetty-ee10-websocket-jakarta-server:*:* \
  ee10-websocket-jakarta-server

%pom_xpath_set pom:properties/pom:ee10.jakarta.websocket.api.version 2.2.0 jetty-ee10

# Override the imported EE10 BOM for the installed CDI 4.1 APIs.
%pom_xpath_set pom:properties/pom:ee10.jakarta.enterprise.cdi.api.version 4.1.0 jetty-ee10
%pom_xpath_inject pom:dependencyManagement/pom:dependencies \
  "<dependency><groupId>jakarta.enterprise</groupId> \
    <artifactId>jakarta.enterprise.cdi-api</artifactId> \
    <version>\${ee10.jakarta.enterprise.cdi.api.version}</version> \
    </dependency>" \
  jetty-ee10
%pom_xpath_inject pom:dependencyManagement/pom:dependencies \
  "<dependency><groupId>jakarta.enterprise</groupId> \
    <artifactId>jakarta.enterprise.lang-model</artifactId> \
    <version>\${ee10.jakarta.enterprise.cdi.api.version}</version> \
    </dependency>" \
  jetty-ee10

%pom_xpath_set pom:properties/pom:flatten.maven.plugin.version 1.9.0

%build
set --
java=%_jvmdir/java-21-openjdk/bin/java
# Detect the build JVM because the RPM itself is noarch.
if "$java" -XshowSettings:properties -version 2>&1 | \
    grep -Eq 'os\.arch = (x86|i[3-6]86)$'; then
    set -- -DskipTests
fi
%mvn_build -s -j -- "$@"

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE.txt

%files core -f .mfiles-core
%files build -f .mfiles-build
%files build-resources -f .mfiles-build-resources
%files slf4j-impl -f .mfiles-slf4j-impl
%files util -f .mfiles-util
%files jmx -f .mfiles-jmx
%files io -f .mfiles-io
%files http -f .mfiles-http
%files util-ajax -f .mfiles-util-ajax
%files xml -f .mfiles-xml
%files http-tools -f .mfiles-http-tools
%files server -f .mfiles-server
%files session -f .mfiles-session
%files security -f .mfiles-security
%files ee8 -f .mfiles-ee8
%files ee9 -f .mfiles-ee9

%files ee9-nested -f .mfiles-ee9-nested

%files ee9-security -f .mfiles-ee9-security

%files servlet -f .mfiles-servlet

%files ee8-nested -f .mfiles-ee8-nested
%files ee8-security -f .mfiles-ee8-security
%files test-parent -f .mfiles-test-parent
%files test-multipart -f .mfiles-test-multipart
%files alpn -f .mfiles-alpn
%files alpn-client -f .mfiles-alpn-client
%files compression -f .mfiles-compression
%files compression-common -f .mfiles-compression-common
%files compression-gzip -f .mfiles-compression-gzip
%files compression-server -f .mfiles-compression-server
%files compression-zstandard -f .mfiles-compression-zstandard
%files client -f .mfiles-client
%files ee8-servlet -f .mfiles-ee8-servlet

%files ee8-apache-jsp -f .mfiles-ee8-apache-jsp

%files ee8-glassfish-jstl -f .mfiles-ee8-glassfish-jstl

%files ee8-jspc-maven-plugin -f .mfiles-ee8-jspc-maven-plugin

%files alpn-server -f .mfiles-alpn-server
%files alpn-java-client -f .mfiles-alpn-java-client
%files alpn-java-server -f .mfiles-alpn-java-server
%files proxy -f .mfiles-proxy
%files http2 -f .mfiles-http2
%files http2-client -f .mfiles-http2-client
%files http2-client-transport -f .mfiles-http2-client-transport
%files http2-common -f .mfiles-http2-common
%files http2-hpack -f .mfiles-http2-hpack
%files http2-server -f .mfiles-http2-server

%files websocket -f .mfiles-websocket
%files websocket-core-client -f .mfiles-websocket-core-client
%files websocket-core-common -f .mfiles-websocket-core-common
%files websocket-core-server -f .mfiles-websocket-core-server
%files websocket-jetty-api -f .mfiles-websocket-jetty-api
%files websocket-jetty-client -f .mfiles-websocket-jetty-client
%files websocket-jetty-common -f .mfiles-websocket-jetty-common
%files websocket-jetty-server -f .mfiles-websocket-jetty-server

%files ee -f .mfiles-ee
%files ee-webapp -f .mfiles-ee-webapp
%files ee-test-resources -f .mfiles-ee-test-resources
%files ee10 -f .mfiles-ee10
%files ee10-bom -f .mfiles-ee10-bom
%files ee10-servlet -f .mfiles-ee10-servlet
%files ee10-webapp -f .mfiles-ee10-webapp
%files ee10-servlets -f .mfiles-ee10-servlets

%files jndi -f .mfiles-jndi
%files plus -f .mfiles-plus
%files annotations -f .mfiles-annotations
%files ee10-plus -f .mfiles-ee10-plus
%files ee10-annotations -f .mfiles-ee10-annotations
%files ee10-websocket -f .mfiles-ee10-websocket
%files ee10-websocket-jakarta-common -f .mfiles-ee10-websocket-jakarta-common
%files ee10-websocket-jakarta-client -f .mfiles-ee10-websocket-jakarta-client
%files ee10-websocket-servlet -f .mfiles-ee10-websocket-servlet
%files ee10-websocket-jakarta-server -f .mfiles-ee10-websocket-jakarta-server

%files http3 -f .mfiles-http3
%files http3-client -f .mfiles-http3-client
%files http3-client-transport -f .mfiles-http3-client-transport
%files http3-common -f .mfiles-http3-common
%files http3-qpack -f .mfiles-http3-qpack
%files http3-server -f .mfiles-http3-server
%files quic -f .mfiles-quic
%files quic-api -f .mfiles-quic-api
%files quic-client -f .mfiles-quic-client
%files quic-common -f .mfiles-quic-common
%files quic-server -f .mfiles-quic-server
%files quic-util -f .mfiles-quic-util
%files quic-quiche -f .mfiles-quic-quiche
%files quic-quiche-common -f .mfiles-quic-quiche-common
%files quic-quiche-client -f .mfiles-quic-quiche-client
%files quic-quiche-server -f .mfiles-quic-quiche-server
%files quic-quiche-jna -f .mfiles-quic-quiche-jna

%changelog
* Sat Nov 21 2026 Ivan Khanas <xeno@altlinux.org> 12.1.15-alt1
- New version.
- Restore the Jakarta EE9 servlet modules.
- Fix concurrent access to ZIP resources in servlet tests.
- Skip running tests on i586.

* Mon Aug 24 2026 Ivan Khanas <xeno@altlinux.org> 12.1.12-alt1
- New version (fixes CVE-2026-10050).

* Wed Apr 01 2026 Ivan Khanas <xeno@altlinux.org> 12.1.8-alt1
- New version.

* Mon Feb 09 2026 Andrey Cherepanov <cas@altlinux.org> 9.4.58-alt1
- New version (fixes: CVE-2025-5115).

* Mon Mar 24 2025 Andrey Cherepanov <cas@altlinux.org> 9.4.57-alt1
- New version (fixes CVE-2024-6763)

* Thu Nov 21 2024 Andrey Cherepanov <cas@altlinux.org> 9.4.56-alt1
- New version.
- Change URL to https://jetty.org/
- Security fixes: CVE-2021-34429, CVE-2022-2047, CVE-2023-26048, CVE-2023-26049,
  CVE-2023-40167, CVE-2023-41900, CVE-2024-22201

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
