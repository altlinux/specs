%define _unpackaged_files_terminate_build 1

Name: ktor
Version: 3.6.1
Release: alt1

Summary: Kotlin framework for asynchronous HTTP clients and servers
License: Apache-2.0
Group: Development/Java
BuildArch: noarch
URL: https://ktor.io
VCS: https://github.com/ktorio/ktor.git

Source: %name-%version.tar
Patch: system-jvm.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(com.auth0:java-jwt)
BuildRequires: mvn(com.auth0:jwks-rsa)
BuildRequires: mvn(com.charleskorn.kaml:kaml-jvm)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-smile)
BuildRequires: mvn(com.fasterxml.jackson.module:jackson-module-kotlin)
BuildRequires: mvn(com.github.luben:zstd-jni)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(com.squareup.okhttp3:okhttp)
BuildRequires: mvn(com.squareup.okio:okio)
BuildRequires: mvn(com.typesafe:config)
BuildRequires: mvn(io.github.pdvrieze.xmlutil:serialization-jvm)
BuildRequires: mvn(io.netty:netty-codec)
BuildRequires: mvn(io.netty:netty-codec-http2)
BuildRequires: mvn(io.netty:netty-codec-http3)
BuildRequires: mvn(io.netty:netty-handler)
BuildRequires: mvn(io.netty:netty-tcnative)
BuildRequires: mvn(io.netty:netty-transport-native-epoll)
BuildRequires: mvn(io.netty:netty-transport-classes-kqueue)
BuildRequires: mvn(jakarta.servlet:jakarta.servlet-api:6.0.0)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(net.mamoe.yamlkt:yamlkt-jvm)
BuildRequires: mvn(org.apache.httpcomponents.client5:httpclient5)
BuildRequires: mvn(org.apache.httpcomponents:httpasyncclient)
BuildRequires: mvn(org.eclipse.jetty.alpn:alpn-api)
BuildRequires: mvn(org.eclipse.jetty.ee10.websocket:jetty-ee10-websocket-jakarta-server)
BuildRequires: mvn(org.eclipse.jetty.ee10:jetty-ee10-servlet)
BuildRequires: mvn(org.eclipse.jetty.ee10:jetty-ee10-servlets)
BuildRequires: mvn(org.eclipse.jetty.http2:http2-client:9.4)
BuildRequires: mvn(org.eclipse.jetty.http2:http2-server:9.4)
BuildRequires: mvn(org.eclipse.jetty.http2:jetty-http2-client)
BuildRequires: mvn(org.eclipse.jetty.http2:jetty-http2-server)
BuildRequires: mvn(org.eclipse.jetty:jetty-alpn-java-client)
BuildRequires: mvn(org.eclipse.jetty:jetty-alpn-java-client:9.4)
BuildRequires: mvn(org.eclipse.jetty:jetty-alpn-java-server)
BuildRequires: mvn(org.eclipse.jetty:jetty-alpn-java-server:9.4)
BuildRequires: mvn(org.eclipse.jetty:jetty-alpn-openjdk8-client:9.4)
BuildRequires: mvn(org.eclipse.jetty:jetty-alpn-openjdk8-server:9.4)
BuildRequires: mvn(org.eclipse.jetty:jetty-alpn-server)
BuildRequires: mvn(org.eclipse.jetty:jetty-alpn-server:9.4)
BuildRequires: mvn(org.eclipse.jetty:jetty-server)
BuildRequires: mvn(org.eclipse.jetty:jetty-server:9.4)
BuildRequires: mvn(org.eclipse.jetty:jetty-servlet:9.4)
BuildRequires: mvn(org.eclipse.jetty:jetty-servlets:9.4)
BuildRequires: mvn(org.freemarker:freemarker)
BuildRequires: mvn(org.fusesource.jansi:jansi)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-gradle-plugin)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-reflect)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-serialization)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit5)
BuildRequires: mvn(org.jetbrains.kotlinx:atomicfu-gradle-plugin)
# Both the Gradle copy and kotlinx-coroutines expose the same Maven name.
BuildRequires: kotlinx-coroutines
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-coroutines-debug-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-coroutines-slf4j-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-coroutines-test-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-datetime-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-html-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-io-core-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-cbor-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-core-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-json-io-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-json-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-protobuf-jvm)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-simple)
BuildRequires: mvn(tools.jackson.core:jackson-databind)
BuildRequires: mvn(tools.jackson.dataformat:jackson-dataformat-smile)
BuildRequires: mvn(tools.jackson.module:jackson-module-kotlin)

# Use the Tomcat 9.0 compatibility capability for the javax engine.
BuildRequires: mvn(org.apache.tomcat.embed:tomcat-embed-core:9.0)
# Embed Jakarta pulls the matching server libraries and APIs.
BuildRequires: mvn(org.apache.tomcat.embed:tomcat-embed-core)

%description
Ktor provides asynchronous HTTP clients and servers for Kotlin. This package
contains separate JVM modules for its client and server engines, networking,
serialization and plugins. Complete multiplatform sources are retained.

%package call-id
BuildArch: noarch
Group: Development/Java
Summary: Ktor call-id module

%description call-id
The ktor-call-id library module for Ktor.

%package client
BuildArch: noarch
Group: Development/Java
Summary: Ktor client module

%description client
The ktor-client library module for Ktor.

%package client-android
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-android module

%description client-android
The ktor-client-android library module for Ktor.

%package client-apache
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-apache module

%description client-apache
The ktor-client-apache library module for Ktor.

%package client-apache5
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-apache5 module

%description client-apache5
The ktor-client-apache5 library module for Ktor.

%package client-auth
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-auth module

%description client-auth
The ktor-client-auth library module for Ktor.

%package client-bom-remover
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-bom-remover module

%description client-bom-remover
The ktor-client-bom-remover library module for Ktor.

%package client-call-id
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-call-id module

%description client-call-id
The ktor-client-call-id library module for Ktor.

%package client-cio
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-cio module

%description client-cio
The ktor-client-cio library module for Ktor.

%package client-content-negotiation
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-content-negotiation module

%description client-content-negotiation
The ktor-client-content-negotiation library module for Ktor.

%package client-core
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-core module

%description client-core
The ktor-client-core library module for Ktor.

%package client-encoding
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-encoding module

%description client-encoding
The ktor-client-encoding library module for Ktor.

%package client-engine-defaults
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-engine-defaults module

%description client-engine-defaults
The ktor-client-engine-defaults library module for Ktor.

%package client-gson
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-gson module

%description client-gson
The ktor-client-gson library module for Ktor.

%package client-jackson
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-jackson module

%description client-jackson
The ktor-client-jackson library module for Ktor.

%package client-java
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-java module

%description client-java
The ktor-client-java library module for Ktor.

%package client-jetty
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-jetty module

%description client-jetty
The ktor-client-jetty library module for Ktor.

%package client-jetty-jakarta
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-jetty-jakarta module

%description client-jetty-jakarta
The ktor-client-jetty-jakarta library module for Ktor.

%package client-json
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-json module

%description client-json
The ktor-client-json library module for Ktor.

%package client-logging
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-logging module

%description client-logging
The ktor-client-logging library module for Ktor.

%package client-mock
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-mock module

%description client-mock
The ktor-client-mock library module for Ktor.

%package client-okhttp
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-okhttp module

%description client-okhttp
The ktor-client-okhttp library module for Ktor.

%package client-resources
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-resources module

%description client-resources
The ktor-client-resources library module for Ktor.

%package client-serialization
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-serialization module

%description client-serialization
The ktor-client-serialization library module for Ktor.

%package client-websockets
BuildArch: noarch
Group: Development/Java
Summary: Ktor client-websockets module

%description client-websockets
The ktor-client-websockets library module for Ktor.

%package encoding-zstd
BuildArch: noarch
Group: Development/Java
Summary: Ktor encoding-zstd module

%description encoding-zstd
The ktor-encoding-zstd library module for Ktor.

%package events
BuildArch: noarch
Group: Development/Java
Summary: Ktor events module

%description events
The ktor-events library module for Ktor.

%package htmx
BuildArch: noarch
Group: Development/Java
Summary: Ktor htmx module

%description htmx
The ktor-htmx library module for Ktor.

%package htmx-html
BuildArch: noarch
Group: Development/Java
Summary: Ktor htmx-html module

%description htmx-html
The ktor-htmx-html library module for Ktor.

%package http
BuildArch: noarch
Group: Development/Java
Summary: Ktor http module

%description http
The ktor-http library module for Ktor.

%package http-cio
BuildArch: noarch
Group: Development/Java
Summary: Ktor http-cio module

%description http-cio
The ktor-http-cio library module for Ktor.

%package io
BuildArch: noarch
Group: Development/Java
Summary: Ktor io module

%description io
The ktor-io library module for Ktor.

%package network
BuildArch: noarch
Group: Development/Java
Summary: Ktor network module

%description network
The ktor-network library module for Ktor.

%package network-tls
BuildArch: noarch
Group: Development/Java
Summary: Ktor network-tls module

%description network-tls
The ktor-network-tls library module for Ktor.

%package network-tls-certificates
BuildArch: noarch
Group: Development/Java
Summary: Ktor network-tls-certificates module

%description network-tls-certificates
The ktor-network-tls-certificates library module for Ktor.

%package openapi-schema
BuildArch: noarch
Group: Development/Java
Summary: Ktor openapi-schema module

%description openapi-schema
The ktor-openapi-schema library module for Ktor.

%package openapi-schema-reflect
BuildArch: noarch
Group: Development/Java
Summary: Ktor openapi-schema-reflect module

%description openapi-schema-reflect
The ktor-openapi-schema-reflect library module for Ktor.

%package resources
BuildArch: noarch
Group: Development/Java
Summary: Ktor resources module

%description resources
The ktor-resources library module for Ktor.

%package serialization
BuildArch: noarch
Group: Development/Java
Summary: Ktor serialization module

%description serialization
The ktor-serialization library module for Ktor.

%package serialization-gson
BuildArch: noarch
Group: Development/Java
Summary: Ktor serialization-gson module

%description serialization-gson
The ktor-serialization-gson library module for Ktor.

%package serialization-jackson
BuildArch: noarch
Group: Development/Java
Summary: Ktor serialization-jackson module

%description serialization-jackson
The ktor-serialization-jackson library module for Ktor.

%package serialization-jackson3
BuildArch: noarch
Group: Development/Java
Summary: Ktor serialization-jackson3 module

%description serialization-jackson3
The ktor-serialization-jackson3 library module for Ktor.

%package serialization-kotlinx
BuildArch: noarch
Group: Development/Java
Summary: Ktor serialization-kotlinx module

%description serialization-kotlinx
The ktor-serialization-kotlinx library module for Ktor.

%package serialization-kotlinx-cbor
BuildArch: noarch
Group: Development/Java
Summary: Ktor serialization-kotlinx-cbor module

%description serialization-kotlinx-cbor
The ktor-serialization-kotlinx-cbor library module for Ktor.

%package serialization-kotlinx-json
BuildArch: noarch
Group: Development/Java
Summary: Ktor serialization-kotlinx-json module

%description serialization-kotlinx-json
The ktor-serialization-kotlinx-json library module for Ktor.

%package serialization-kotlinx-protobuf
BuildArch: noarch
Group: Development/Java
Summary: Ktor serialization-kotlinx-protobuf module

%description serialization-kotlinx-protobuf
The ktor-serialization-kotlinx-protobuf library module for Ktor.

%package serialization-kotlinx-xml
BuildArch: noarch
Group: Development/Java
Summary: Ktor serialization-kotlinx-xml module

%description serialization-kotlinx-xml
The ktor-serialization-kotlinx-xml library module for Ktor.

%package server
BuildArch: noarch
Group: Development/Java
Summary: Ktor server module

%description server
The ktor-server library module for Ktor.

%package server-auth
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-auth module

%description server-auth
The ktor-server-auth library module for Ktor.

%package server-auth-api-key
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-auth-api-key module

%description server-auth-api-key
The ktor-server-auth-api-key library module for Ktor.

%package server-auth-jwt
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-auth-jwt module

%description server-auth-jwt
The ktor-server-auth-jwt library module for Ktor.

%package server-auth-ldap
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-auth-ldap module

%description server-auth-ldap
The ktor-server-auth-ldap library module for Ktor.

%package server-auto-head-response
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-auto-head-response module

%description server-auto-head-response
The ktor-server-auto-head-response library module for Ktor.

%package server-body-limit
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-body-limit module

%description server-body-limit
The ktor-server-body-limit library module for Ktor.

%package server-caching-headers
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-caching-headers module

%description server-caching-headers
The ktor-server-caching-headers library module for Ktor.

%package server-call-id
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-call-id module

%description server-call-id
The ktor-server-call-id library module for Ktor.

%package server-call-logging
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-call-logging module

%description server-call-logging
The ktor-server-call-logging library module for Ktor.

%package server-cio
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-cio module

%description server-cio
The ktor-server-cio library module for Ktor.

%package server-compression
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-compression module

%description server-compression
The ktor-server-compression library module for Ktor.

%package server-compression-zstd
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-compression-zstd module

%description server-compression-zstd
The ktor-server-compression-zstd library module for Ktor.

%package server-conditional-headers
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-conditional-headers module

%description server-conditional-headers
The ktor-server-conditional-headers library module for Ktor.

%package server-config-yaml
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-config-yaml module

%description server-config-yaml
The ktor-server-config-yaml library module for Ktor.

%package server-content-negotiation
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-content-negotiation module

%description server-content-negotiation
The ktor-server-content-negotiation library module for Ktor.

%package server-core
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-core module

%description server-core
The ktor-server-core library module for Ktor.

%package server-cors
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-cors module

%description server-cors
The ktor-server-cors library module for Ktor.

%package server-csrf
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-csrf module

%description server-csrf
The ktor-server-csrf library module for Ktor.

%package server-data-conversion
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-data-conversion module

%description server-data-conversion
The ktor-server-data-conversion library module for Ktor.

%package server-default-headers
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-default-headers module

%description server-default-headers
The ktor-server-default-headers library module for Ktor.

%package server-di
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-di module

%description server-di
The ktor-server-di library module for Ktor.

%package server-double-receive
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-double-receive module

%description server-double-receive
The ktor-server-double-receive library module for Ktor.

%package server-forwarded-header
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-forwarded-header module

%description server-forwarded-header
The ktor-server-forwarded-header library module for Ktor.

%package server-freemarker
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-freemarker module

%description server-freemarker
The ktor-server-freemarker library module for Ktor.

%package server-host-common
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-host-common module

%description server-host-common
The ktor-server-host-common library module for Ktor.

%package server-hsts
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-hsts module

%description server-hsts
The ktor-server-hsts library module for Ktor.

%package server-html-builder
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-html-builder module

%description server-html-builder
The ktor-server-html-builder library module for Ktor.

%package server-htmx
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-htmx module

%description server-htmx
The ktor-server-htmx library module for Ktor.

%package server-http-redirect
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-http-redirect module

%description server-http-redirect
The ktor-server-http-redirect library module for Ktor.

%package server-i18n
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-i18n module

%description server-i18n
The ktor-server-i18n library module for Ktor.

%package server-jetty
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-jetty module

%description server-jetty
The ktor-server-jetty library module for Ktor.

%package server-jetty-jakarta
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-jetty-jakarta module

%description server-jetty-jakarta
The ktor-server-jetty-jakarta library module for Ktor.

%package server-method-override
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-method-override module

%description server-method-override
The ktor-server-method-override library module for Ktor.

%package server-netty
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-netty module

%description server-netty
The ktor-server-netty library module for Ktor.

%package server-partial-content
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-partial-content module

%description server-partial-content
The ktor-server-partial-content library module for Ktor.

%package server-rate-limit
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-rate-limit module

%description server-rate-limit
The ktor-server-rate-limit library module for Ktor.

%package server-request-validation
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-request-validation module

%description server-request-validation
The ktor-server-request-validation library module for Ktor.

%package server-resources
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-resources module

%description server-resources
The ktor-server-resources library module for Ktor.

%package server-routing-openapi
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-routing-openapi module

%description server-routing-openapi
The ktor-server-routing-openapi library module for Ktor.

%package server-servlet
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-servlet module

%description server-servlet
The ktor-server-servlet library module for Ktor.

%package server-servlet-jakarta
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-servlet-jakarta module

%description server-servlet-jakarta
The ktor-server-servlet-jakarta library module for Ktor.

%package server-sessions
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-sessions module

%description server-sessions
The ktor-server-sessions library module for Ktor.

%package server-sse
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-sse module

%description server-sse
The ktor-server-sse library module for Ktor.

%package server-status-pages
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-status-pages module

%description server-status-pages
The ktor-server-status-pages library module for Ktor.

%package server-test-host
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-test-host module

%description server-test-host
The ktor-server-test-host library module for Ktor.

%package server-tomcat
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-tomcat module

%description server-tomcat
The ktor-server-tomcat library module for Ktor.

%package server-tomcat-jakarta
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-tomcat-jakarta module

%description server-tomcat-jakarta
The ktor-server-tomcat-jakarta library module for Ktor.

%package server-websockets
BuildArch: noarch
Group: Development/Java
Summary: Ktor server-websockets module

%description server-websockets
The ktor-server-websockets library module for Ktor.

%package sse
BuildArch: noarch
Group: Development/Java
Summary: Ktor sse module

%description sse
The ktor-sse library module for Ktor.

%package test-dispatcher
BuildArch: noarch
Group: Development/Java
Summary: Ktor test-dispatcher module

%description test-dispatcher
The ktor-test-dispatcher library module for Ktor.

%package utils
BuildArch: noarch
Group: Development/Java
Summary: Ktor utils module

%description utils
The ktor-utils library module for Ktor.

%package websocket-serialization
BuildArch: noarch
Group: Development/Java
Summary: Ktor websocket-serialization module

%description websocket-serialization
The ktor-websocket-serialization library module for Ktor.

%package websockets
BuildArch: noarch
Group: Development/Java
Summary: Ktor websockets module

%description websockets
The ktor-websockets library module for Ktor.

%prep
%setup
%autopatch -p1

# The 32-bit Gradle JVM cannot reserve the upstream 6 GiB heap.
if [ "$(getconf LONG_BIT)" = 32 ]; then
    sed -i '/^org\.gradle\.jvmargs=/s/-Xms2g -Xmx6g -XX:MaxMetaspaceSize=1g/-Xms256m -Xmx1536m -XX:MaxMetaspaceSize=384m/' gradle.properties
fi

%build
%gradle_publish

%install
%mvn_package io.ktor:ktor-call-id call-id
%mvn_package io.ktor:ktor-call-id-jvm call-id
%mvn_package io.ktor:ktor-client client
%mvn_package io.ktor:ktor-client-jvm client
%mvn_package io.ktor:ktor-client-android client-android
%mvn_package io.ktor:ktor-client-android-jvm client-android
%mvn_package io.ktor:ktor-client-apache client-apache
%mvn_package io.ktor:ktor-client-apache-jvm client-apache
%mvn_package io.ktor:ktor-client-apache5 client-apache5
%mvn_package io.ktor:ktor-client-apache5-jvm client-apache5
%mvn_package io.ktor:ktor-client-auth client-auth
%mvn_package io.ktor:ktor-client-auth-jvm client-auth
%mvn_package io.ktor:ktor-client-bom-remover client-bom-remover
%mvn_package io.ktor:ktor-client-bom-remover-jvm client-bom-remover
%mvn_package io.ktor:ktor-client-call-id client-call-id
%mvn_package io.ktor:ktor-client-call-id-jvm client-call-id
%mvn_package io.ktor:ktor-client-cio client-cio
%mvn_package io.ktor:ktor-client-cio-jvm client-cio
%mvn_package io.ktor:ktor-client-content-negotiation client-content-negotiation
%mvn_package io.ktor:ktor-client-content-negotiation-jvm client-content-negotiation
%mvn_package io.ktor:ktor-client-core client-core
%mvn_package io.ktor:ktor-client-core-jvm client-core
%mvn_package io.ktor:ktor-client-encoding client-encoding
%mvn_package io.ktor:ktor-client-encoding-jvm client-encoding
%mvn_package io.ktor:ktor-client-engine-defaults client-engine-defaults
%mvn_package io.ktor:ktor-client-engine-defaults-jvm client-engine-defaults
%mvn_package io.ktor:ktor-client-gson client-gson
%mvn_package io.ktor:ktor-client-gson-jvm client-gson
%mvn_package io.ktor:ktor-client-jackson client-jackson
%mvn_package io.ktor:ktor-client-jackson-jvm client-jackson
%mvn_package io.ktor:ktor-client-java client-java
%mvn_package io.ktor:ktor-client-java-jvm client-java
%mvn_package io.ktor:ktor-client-jetty client-jetty
%mvn_package io.ktor:ktor-client-jetty-jvm client-jetty
%mvn_package io.ktor:ktor-client-jetty-jakarta client-jetty-jakarta
%mvn_package io.ktor:ktor-client-jetty-jakarta-jvm client-jetty-jakarta
%mvn_package io.ktor:ktor-client-json client-json
%mvn_package io.ktor:ktor-client-json-jvm client-json
%mvn_package io.ktor:ktor-client-logging client-logging
%mvn_package io.ktor:ktor-client-logging-jvm client-logging
%mvn_package io.ktor:ktor-client-mock client-mock
%mvn_package io.ktor:ktor-client-mock-jvm client-mock
%mvn_package io.ktor:ktor-client-okhttp client-okhttp
%mvn_package io.ktor:ktor-client-okhttp-jvm client-okhttp
%mvn_package io.ktor:ktor-client-resources client-resources
%mvn_package io.ktor:ktor-client-resources-jvm client-resources
%mvn_package io.ktor:ktor-client-serialization client-serialization
%mvn_package io.ktor:ktor-client-serialization-jvm client-serialization
%mvn_package io.ktor:ktor-client-websockets client-websockets
%mvn_package io.ktor:ktor-client-websockets-jvm client-websockets
%mvn_package io.ktor:ktor-encoding-zstd encoding-zstd
%mvn_package io.ktor:ktor-encoding-zstd-jvm encoding-zstd
%mvn_package io.ktor:ktor-events events
%mvn_package io.ktor:ktor-events-jvm events
%mvn_package io.ktor:ktor-htmx htmx
%mvn_package io.ktor:ktor-htmx-jvm htmx
%mvn_package io.ktor:ktor-htmx-html htmx-html
%mvn_package io.ktor:ktor-htmx-html-jvm htmx-html
%mvn_package io.ktor:ktor-http http
%mvn_package io.ktor:ktor-http-jvm http
%mvn_package io.ktor:ktor-http-cio http-cio
%mvn_package io.ktor:ktor-http-cio-jvm http-cio
%mvn_package io.ktor:ktor-io io
%mvn_package io.ktor:ktor-io-jvm io
%mvn_package io.ktor:ktor-network network
%mvn_package io.ktor:ktor-network-jvm network
%mvn_package io.ktor:ktor-network-tls network-tls
%mvn_package io.ktor:ktor-network-tls-jvm network-tls
%mvn_package io.ktor:ktor-network-tls-certificates network-tls-certificates
%mvn_package io.ktor:ktor-network-tls-certificates-jvm network-tls-certificates
%mvn_package io.ktor:ktor-openapi-schema openapi-schema
%mvn_package io.ktor:ktor-openapi-schema-jvm openapi-schema
%mvn_package io.ktor:ktor-openapi-schema-reflect openapi-schema-reflect
%mvn_package io.ktor:ktor-openapi-schema-reflect-jvm openapi-schema-reflect
%mvn_package io.ktor:ktor-resources resources
%mvn_package io.ktor:ktor-resources-jvm resources
%mvn_package io.ktor:ktor-serialization serialization
%mvn_package io.ktor:ktor-serialization-jvm serialization
%mvn_package io.ktor:ktor-serialization-gson serialization-gson
%mvn_package io.ktor:ktor-serialization-gson-jvm serialization-gson
%mvn_package io.ktor:ktor-serialization-jackson serialization-jackson
%mvn_package io.ktor:ktor-serialization-jackson-jvm serialization-jackson
%mvn_package io.ktor:ktor-serialization-jackson3 serialization-jackson3
%mvn_package io.ktor:ktor-serialization-jackson3-jvm serialization-jackson3
%mvn_package io.ktor:ktor-serialization-kotlinx serialization-kotlinx
%mvn_package io.ktor:ktor-serialization-kotlinx-jvm serialization-kotlinx
%mvn_package io.ktor:ktor-serialization-kotlinx-cbor serialization-kotlinx-cbor
%mvn_package io.ktor:ktor-serialization-kotlinx-cbor-jvm serialization-kotlinx-cbor
%mvn_package io.ktor:ktor-serialization-kotlinx-json serialization-kotlinx-json
%mvn_package io.ktor:ktor-serialization-kotlinx-json-jvm serialization-kotlinx-json
%mvn_package io.ktor:ktor-serialization-kotlinx-protobuf serialization-kotlinx-protobuf
%mvn_package io.ktor:ktor-serialization-kotlinx-protobuf-jvm serialization-kotlinx-protobuf
%mvn_package io.ktor:ktor-serialization-kotlinx-xml serialization-kotlinx-xml
%mvn_package io.ktor:ktor-serialization-kotlinx-xml-jvm serialization-kotlinx-xml
%mvn_package io.ktor:ktor-server server
%mvn_package io.ktor:ktor-server-jvm server
%mvn_package io.ktor:ktor-server-auth server-auth
%mvn_package io.ktor:ktor-server-auth-jvm server-auth
%mvn_package io.ktor:ktor-server-auth-api-key server-auth-api-key
%mvn_package io.ktor:ktor-server-auth-api-key-jvm server-auth-api-key
%mvn_package io.ktor:ktor-server-auth-jwt server-auth-jwt
%mvn_package io.ktor:ktor-server-auth-jwt-jvm server-auth-jwt
%mvn_package io.ktor:ktor-server-auth-ldap server-auth-ldap
%mvn_package io.ktor:ktor-server-auth-ldap-jvm server-auth-ldap
%mvn_package io.ktor:ktor-server-auto-head-response server-auto-head-response
%mvn_package io.ktor:ktor-server-auto-head-response-jvm server-auto-head-response
%mvn_package io.ktor:ktor-server-body-limit server-body-limit
%mvn_package io.ktor:ktor-server-body-limit-jvm server-body-limit
%mvn_package io.ktor:ktor-server-caching-headers server-caching-headers
%mvn_package io.ktor:ktor-server-caching-headers-jvm server-caching-headers
%mvn_package io.ktor:ktor-server-call-id server-call-id
%mvn_package io.ktor:ktor-server-call-id-jvm server-call-id
%mvn_package io.ktor:ktor-server-call-logging server-call-logging
%mvn_package io.ktor:ktor-server-call-logging-jvm server-call-logging
%mvn_package io.ktor:ktor-server-cio server-cio
%mvn_package io.ktor:ktor-server-cio-jvm server-cio
%mvn_package io.ktor:ktor-server-compression server-compression
%mvn_package io.ktor:ktor-server-compression-jvm server-compression
%mvn_package io.ktor:ktor-server-compression-zstd server-compression-zstd
%mvn_package io.ktor:ktor-server-compression-zstd-jvm server-compression-zstd
%mvn_package io.ktor:ktor-server-conditional-headers server-conditional-headers
%mvn_package io.ktor:ktor-server-conditional-headers-jvm server-conditional-headers
%mvn_package io.ktor:ktor-server-config-yaml server-config-yaml
%mvn_package io.ktor:ktor-server-config-yaml-jvm server-config-yaml
%mvn_package io.ktor:ktor-server-content-negotiation server-content-negotiation
%mvn_package io.ktor:ktor-server-content-negotiation-jvm server-content-negotiation
%mvn_package io.ktor:ktor-server-core server-core
%mvn_package io.ktor:ktor-server-core-jvm server-core
%mvn_package io.ktor:ktor-server-cors server-cors
%mvn_package io.ktor:ktor-server-cors-jvm server-cors
%mvn_package io.ktor:ktor-server-csrf server-csrf
%mvn_package io.ktor:ktor-server-csrf-jvm server-csrf
%mvn_package io.ktor:ktor-server-data-conversion server-data-conversion
%mvn_package io.ktor:ktor-server-data-conversion-jvm server-data-conversion
%mvn_package io.ktor:ktor-server-default-headers server-default-headers
%mvn_package io.ktor:ktor-server-default-headers-jvm server-default-headers
%mvn_package io.ktor:ktor-server-di server-di
%mvn_package io.ktor:ktor-server-di-jvm server-di
%mvn_package io.ktor:ktor-server-double-receive server-double-receive
%mvn_package io.ktor:ktor-server-double-receive-jvm server-double-receive
%mvn_package io.ktor:ktor-server-forwarded-header server-forwarded-header
%mvn_package io.ktor:ktor-server-forwarded-header-jvm server-forwarded-header
%mvn_package io.ktor:ktor-server-freemarker server-freemarker
%mvn_package io.ktor:ktor-server-freemarker-jvm server-freemarker
%mvn_package io.ktor:ktor-server-host-common server-host-common
%mvn_package io.ktor:ktor-server-host-common-jvm server-host-common
%mvn_package io.ktor:ktor-server-hsts server-hsts
%mvn_package io.ktor:ktor-server-hsts-jvm server-hsts
%mvn_package io.ktor:ktor-server-html-builder server-html-builder
%mvn_package io.ktor:ktor-server-html-builder-jvm server-html-builder
%mvn_package io.ktor:ktor-server-htmx server-htmx
%mvn_package io.ktor:ktor-server-htmx-jvm server-htmx
%mvn_package io.ktor:ktor-server-http-redirect server-http-redirect
%mvn_package io.ktor:ktor-server-http-redirect-jvm server-http-redirect
%mvn_package io.ktor:ktor-server-i18n server-i18n
%mvn_package io.ktor:ktor-server-i18n-jvm server-i18n
%mvn_package io.ktor:ktor-server-jetty server-jetty
%mvn_package io.ktor:ktor-server-jetty-jvm server-jetty
%mvn_package io.ktor:ktor-server-jetty-jakarta server-jetty-jakarta
%mvn_package io.ktor:ktor-server-jetty-jakarta-jvm server-jetty-jakarta
%mvn_package io.ktor:ktor-server-method-override server-method-override
%mvn_package io.ktor:ktor-server-method-override-jvm server-method-override
%mvn_package io.ktor:ktor-server-netty server-netty
%mvn_package io.ktor:ktor-server-netty-jvm server-netty
%mvn_package io.ktor:ktor-server-partial-content server-partial-content
%mvn_package io.ktor:ktor-server-partial-content-jvm server-partial-content
%mvn_package io.ktor:ktor-server-rate-limit server-rate-limit
%mvn_package io.ktor:ktor-server-rate-limit-jvm server-rate-limit
%mvn_package io.ktor:ktor-server-request-validation server-request-validation
%mvn_package io.ktor:ktor-server-request-validation-jvm server-request-validation
%mvn_package io.ktor:ktor-server-resources server-resources
%mvn_package io.ktor:ktor-server-resources-jvm server-resources
%mvn_package io.ktor:ktor-server-routing-openapi server-routing-openapi
%mvn_package io.ktor:ktor-server-routing-openapi-jvm server-routing-openapi
%mvn_package io.ktor:ktor-server-servlet server-servlet
%mvn_package io.ktor:ktor-server-servlet-jvm server-servlet
%mvn_package io.ktor:ktor-server-servlet-jakarta server-servlet-jakarta
%mvn_package io.ktor:ktor-server-servlet-jakarta-jvm server-servlet-jakarta
%mvn_package io.ktor:ktor-server-sessions server-sessions
%mvn_package io.ktor:ktor-server-sessions-jvm server-sessions
%mvn_package io.ktor:ktor-server-sse server-sse
%mvn_package io.ktor:ktor-server-sse-jvm server-sse
%mvn_package io.ktor:ktor-server-status-pages server-status-pages
%mvn_package io.ktor:ktor-server-status-pages-jvm server-status-pages
%mvn_package io.ktor:ktor-server-test-host server-test-host
%mvn_package io.ktor:ktor-server-test-host-jvm server-test-host
%mvn_package io.ktor:ktor-server-tomcat server-tomcat
%mvn_package io.ktor:ktor-server-tomcat-jvm server-tomcat
%mvn_package io.ktor:ktor-server-tomcat-jakarta server-tomcat-jakarta
%mvn_package io.ktor:ktor-server-tomcat-jakarta-jvm server-tomcat-jakarta
%mvn_package io.ktor:ktor-server-websockets server-websockets
%mvn_package io.ktor:ktor-server-websockets-jvm server-websockets
%mvn_package io.ktor:ktor-sse sse
%mvn_package io.ktor:ktor-sse-jvm sse
%mvn_package io.ktor:ktor-test-dispatcher test-dispatcher
%mvn_package io.ktor:ktor-test-dispatcher-jvm test-dispatcher
%mvn_package io.ktor:ktor-utils utils
%mvn_package io.ktor:ktor-utils-jvm utils
%mvn_package io.ktor:ktor-websocket-serialization websocket-serialization
%mvn_package io.ktor:ktor-websocket-serialization-jvm websocket-serialization
%mvn_package io.ktor:ktor-websockets websockets
%mvn_package io.ktor:ktor-websockets-jvm websockets
%gradle_register --artifacts=ktor-
%gradle_install

%check
java=%_jvmdir/java-21-openjdk/bin/java
# The package is noarch, so check the build JVM's architecture.
if "$java" -XshowSettings:properties -version 2>&1 | \
    grep -Eq 'os\.arch = (x86|i[3-6]86)$'; then
    echo 'Skipping Ktor tests on i586.'
    exit 0
fi
%gradle_check --continue

%files call-id -f .mfiles-call-id

%files client -f .mfiles-client

%files client-android -f .mfiles-client-android

%files client-apache -f .mfiles-client-apache

%files client-apache5 -f .mfiles-client-apache5

%files client-auth -f .mfiles-client-auth

%files client-bom-remover -f .mfiles-client-bom-remover

%files client-call-id -f .mfiles-client-call-id

%files client-cio -f .mfiles-client-cio

%files client-content-negotiation -f .mfiles-client-content-negotiation

%files client-core -f .mfiles-client-core

%files client-encoding -f .mfiles-client-encoding

%files client-engine-defaults -f .mfiles-client-engine-defaults

%files client-gson -f .mfiles-client-gson

%files client-jackson -f .mfiles-client-jackson

%files client-java -f .mfiles-client-java

%files client-jetty -f .mfiles-client-jetty

%files client-jetty-jakarta -f .mfiles-client-jetty-jakarta

%files client-json -f .mfiles-client-json

%files client-logging -f .mfiles-client-logging

%files client-mock -f .mfiles-client-mock

%files client-okhttp -f .mfiles-client-okhttp

%files client-resources -f .mfiles-client-resources

%files client-serialization -f .mfiles-client-serialization

%files client-websockets -f .mfiles-client-websockets

%files encoding-zstd -f .mfiles-encoding-zstd

%files events -f .mfiles-events

%files htmx -f .mfiles-htmx

%files htmx-html -f .mfiles-htmx-html

%files http -f .mfiles-http

%files http-cio -f .mfiles-http-cio

%files io -f .mfiles-io

%files network -f .mfiles-network

%files network-tls -f .mfiles-network-tls

%files network-tls-certificates -f .mfiles-network-tls-certificates

%files openapi-schema -f .mfiles-openapi-schema

%files openapi-schema-reflect -f .mfiles-openapi-schema-reflect

%files resources -f .mfiles-resources

%files serialization -f .mfiles-serialization

%files serialization-gson -f .mfiles-serialization-gson

%files serialization-jackson -f .mfiles-serialization-jackson

%files serialization-jackson3 -f .mfiles-serialization-jackson3

%files serialization-kotlinx -f .mfiles-serialization-kotlinx

%files serialization-kotlinx-cbor -f .mfiles-serialization-kotlinx-cbor

%files serialization-kotlinx-json -f .mfiles-serialization-kotlinx-json

%files serialization-kotlinx-protobuf -f .mfiles-serialization-kotlinx-protobuf

%files serialization-kotlinx-xml -f .mfiles-serialization-kotlinx-xml

%files server -f .mfiles-server

%files server-auth -f .mfiles-server-auth

%files server-auth-api-key -f .mfiles-server-auth-api-key

%files server-auth-jwt -f .mfiles-server-auth-jwt

%files server-auth-ldap -f .mfiles-server-auth-ldap

%files server-auto-head-response -f .mfiles-server-auto-head-response

%files server-body-limit -f .mfiles-server-body-limit

%files server-caching-headers -f .mfiles-server-caching-headers

%files server-call-id -f .mfiles-server-call-id

%files server-call-logging -f .mfiles-server-call-logging

%files server-cio -f .mfiles-server-cio

%files server-compression -f .mfiles-server-compression

%files server-compression-zstd -f .mfiles-server-compression-zstd

%files server-conditional-headers -f .mfiles-server-conditional-headers

%files server-config-yaml -f .mfiles-server-config-yaml

%files server-content-negotiation -f .mfiles-server-content-negotiation

%files server-core -f .mfiles-server-core

%files server-cors -f .mfiles-server-cors

%files server-csrf -f .mfiles-server-csrf

%files server-data-conversion -f .mfiles-server-data-conversion

%files server-default-headers -f .mfiles-server-default-headers

%files server-di -f .mfiles-server-di

%files server-double-receive -f .mfiles-server-double-receive

%files server-forwarded-header -f .mfiles-server-forwarded-header

%files server-freemarker -f .mfiles-server-freemarker

%files server-host-common -f .mfiles-server-host-common

%files server-hsts -f .mfiles-server-hsts

%files server-html-builder -f .mfiles-server-html-builder

%files server-htmx -f .mfiles-server-htmx

%files server-http-redirect -f .mfiles-server-http-redirect

%files server-i18n -f .mfiles-server-i18n

%files server-jetty -f .mfiles-server-jetty

%files server-jetty-jakarta -f .mfiles-server-jetty-jakarta

%files server-method-override -f .mfiles-server-method-override

%files server-netty -f .mfiles-server-netty

%files server-partial-content -f .mfiles-server-partial-content

%files server-rate-limit -f .mfiles-server-rate-limit

%files server-request-validation -f .mfiles-server-request-validation

%files server-resources -f .mfiles-server-resources

%files server-routing-openapi -f .mfiles-server-routing-openapi

%files server-servlet -f .mfiles-server-servlet

%files server-servlet-jakarta -f .mfiles-server-servlet-jakarta

%files server-sessions -f .mfiles-server-sessions

%files server-sse -f .mfiles-server-sse

%files server-status-pages -f .mfiles-server-status-pages

%files server-test-host -f .mfiles-server-test-host

%files server-tomcat -f .mfiles-server-tomcat

%files server-tomcat-jakarta -f .mfiles-server-tomcat-jakarta

%files server-websockets -f .mfiles-server-websockets

%files sse -f .mfiles-sse

%files test-dispatcher -f .mfiles-test-dispatcher

%files utils -f .mfiles-utils
%doc LICENSE

%files websocket-serialization -f .mfiles-websocket-serialization

%files websockets -f .mfiles-websockets

%changelog
* Sat Nov 21 2026 Ivan Khanas <xeno@altlinux.org> 3.6.1-alt1
- Initial build for ALT.
