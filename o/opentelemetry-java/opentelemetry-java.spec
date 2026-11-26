%define _unpackaged_files_terminate_build 1

Name: opentelemetry-java
Version: 1.68.0
Release: alt1

Summary: OpenTelemetry Java API and SDK
License: Apache-2.0
Group: Development/Java
URL: https://github.com/open-telemetry/opentelemetry-java
VCS: https://github.com/open-telemetry/opentelemetry-java.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: opentelemetry-proto.tar
Patch0: 0001-Generate-OTLP-wire-constants-from-protobuf-descripto.patch
Patch1: 0002-Build-SDK-and-IDEA-exporters-with-Gradle-offline.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: protobuf-compiler
BuildRequires: python3-module-protobuf
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.google.auto.value:auto-value)
BuildRequires: mvn(com.google.auto.value:auto-value-annotations)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.errorprone:error_prone_annotations)
BuildRequires: mvn(com.squareup.okhttp3:okhttp-jvm)
BuildRequires: mvn(io.grpc:grpc-api)
BuildRequires: mvn(javax.annotation:javax.annotation-api)
BuildRequires: mvn(org.codehaus.mojo:animal-sniffer-annotations)
BuildRequires: mvn(org.gradle.kotlin:gradle-kotlin-dsl-plugins)
BuildRequires: mvn(org.jctools:jctools-core)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-gradle-plugin)
BuildRequires: kotlinx-coroutines
BuildRequires: mvn(org.jspecify:jspecify)
BuildRequires: mvn(org.snakeyaml:snakeyaml-engine)

%description
OpenTelemetry Java APIs, SDK, exporters and extensions for traces, metrics
and logs.

%package api
Summary: OpenTelemetry Java api module
Group: Development/Java

%description api
The opentelemetry-api Maven module.

%package api-incubator
Summary: OpenTelemetry Java api-incubator module
Group: Development/Java

%description api-incubator
The opentelemetry-api-incubator Maven module.

%package common
Summary: OpenTelemetry Java common module
Group: Development/Java

%description common
The opentelemetry-common Maven module.

%package context
Summary: OpenTelemetry Java context module
Group: Development/Java

%description context
The opentelemetry-context Maven module.

%package exporter-common
Summary: OpenTelemetry Java exporter-common module
Group: Development/Java

%description exporter-common
The opentelemetry-exporter-common Maven module.

%package exporter-logging
Summary: OpenTelemetry Java exporter-logging module
Group: Development/Java

%description exporter-logging
The opentelemetry-exporter-logging Maven module.

%package exporter-logging-otlp
Summary: OpenTelemetry Java exporter-logging-otlp module
Group: Development/Java

%description exporter-logging-otlp
The opentelemetry-exporter-logging-otlp Maven module.

%package exporter-otlp
Summary: OpenTelemetry Java exporter-otlp module
Group: Development/Java

%description exporter-otlp
The opentelemetry-exporter-otlp Maven module.

%package exporter-otlp-common
Summary: OpenTelemetry Java exporter-otlp-common module
Group: Development/Java

%description exporter-otlp-common
The opentelemetry-exporter-otlp-common Maven module.

%package exporter-otlp-profiles
Summary: OpenTelemetry Java exporter-otlp-profiles module
Group: Development/Java

%description exporter-otlp-profiles
The opentelemetry-exporter-otlp-profiles Maven module.

%package exporter-sender-jdk
Summary: OpenTelemetry Java exporter-sender-jdk module
Group: Development/Java

%description exporter-sender-jdk
The opentelemetry-exporter-sender-jdk Maven module.

%package exporter-sender-okhttp
Summary: OpenTelemetry Java exporter-sender-okhttp module
Group: Development/Java

%description exporter-sender-okhttp
The opentelemetry-exporter-sender-okhttp Maven module.

%package extension-kotlin
Summary: OpenTelemetry Java extension-kotlin module
Group: Development/Java

%description extension-kotlin
The opentelemetry-extension-kotlin Maven module.

%package extension-trace-propagators
Summary: OpenTelemetry Java extension-trace-propagators module
Group: Development/Java

%description extension-trace-propagators
The opentelemetry-extension-trace-propagators Maven module.

%package sdk
Summary: OpenTelemetry Java sdk module
Group: Development/Java

%description sdk
The opentelemetry-sdk Maven module.

%package sdk-common
Summary: OpenTelemetry Java sdk-common module
Group: Development/Java

%description sdk-common
The opentelemetry-sdk-common Maven module.

%package sdk-logs
Summary: OpenTelemetry Java sdk-logs module
Group: Development/Java

%description sdk-logs
The opentelemetry-sdk-logs Maven module.

%package sdk-metrics
Summary: OpenTelemetry Java sdk-metrics module
Group: Development/Java

%description sdk-metrics
The opentelemetry-sdk-metrics Maven module.

%package sdk-profiles
Summary: OpenTelemetry Java sdk-profiles module
Group: Development/Java

%description sdk-profiles
The opentelemetry-sdk-profiles Maven module.

%package sdk-trace
Summary: OpenTelemetry Java sdk-trace module
Group: Development/Java

%description sdk-trace
The opentelemetry-sdk-trace Maven module.

%package sdk-extension-autoconfigure
Summary: OpenTelemetry Java sdk-extension-autoconfigure module
Group: Development/Java

%description sdk-extension-autoconfigure
The opentelemetry-sdk-extension-autoconfigure Maven module.

%package sdk-extension-autoconfigure-spi
Summary: OpenTelemetry Java sdk-extension-autoconfigure-spi module
Group: Development/Java

%description sdk-extension-autoconfigure-spi
The opentelemetry-sdk-extension-autoconfigure-spi Maven module.

%package sdk-extension-declarative-config
Summary: OpenTelemetry Java sdk-extension-declarative-config module
Group: Development/Java

%description sdk-extension-declarative-config
The opentelemetry-sdk-extension-declarative-config Maven module.

%package sdk-extension-incubator
Summary: OpenTelemetry Java sdk-extension-incubator module
Group: Development/Java

%description sdk-extension-incubator
The opentelemetry-sdk-extension-incubator Maven module.

%prep
%setup -a1
%autopatch -p1

%mvn_package :opentelemetry-api api
%mvn_package :opentelemetry-api-incubator api-incubator
%mvn_package :opentelemetry-common common
%mvn_package :opentelemetry-context context
%mvn_package :opentelemetry-exporter-common exporter-common
%mvn_package :opentelemetry-exporter-logging exporter-logging
%mvn_package :opentelemetry-exporter-logging-otlp exporter-logging-otlp
%mvn_package :opentelemetry-exporter-otlp exporter-otlp
%mvn_package :opentelemetry-exporter-otlp-common exporter-otlp-common
%mvn_package :opentelemetry-exporter-otlp-profiles exporter-otlp-profiles
%mvn_package :opentelemetry-exporter-sender-jdk exporter-sender-jdk
%mvn_package :opentelemetry-exporter-sender-okhttp exporter-sender-okhttp
%mvn_package :opentelemetry-extension-kotlin extension-kotlin
%mvn_package :opentelemetry-extension-trace-propagators extension-trace-propagators
%mvn_package :opentelemetry-sdk sdk
%mvn_package :opentelemetry-sdk-common sdk-common
%mvn_package :opentelemetry-sdk-logs sdk-logs
%mvn_package :opentelemetry-sdk-metrics sdk-metrics
%mvn_package :opentelemetry-sdk-profiles sdk-profiles
%mvn_package :opentelemetry-sdk-trace sdk-trace
%mvn_package :opentelemetry-sdk-extension-autoconfigure sdk-extension-autoconfigure
%mvn_package :opentelemetry-sdk-extension-autoconfigure-spi sdk-extension-autoconfigure-spi
%mvn_package :opentelemetry-sdk-extension-declarative-config sdk-extension-declarative-config
%mvn_package :opentelemetry-sdk-extension-incubator sdk-extension-incubator

%build
%gradle_publish

%install
%gradle_register --artifacts=opentelemetry-
%gradle_install

%files api -f .mfiles-api

%files api-incubator -f .mfiles-api-incubator

%files common -f .mfiles-common
%doc LICENSE

%files context -f .mfiles-context

%files exporter-common -f .mfiles-exporter-common

%files exporter-logging -f .mfiles-exporter-logging

%files exporter-logging-otlp -f .mfiles-exporter-logging-otlp

%files exporter-otlp -f .mfiles-exporter-otlp

%files exporter-otlp-common -f .mfiles-exporter-otlp-common

%files exporter-otlp-profiles -f .mfiles-exporter-otlp-profiles

%files exporter-sender-jdk -f .mfiles-exporter-sender-jdk

%files exporter-sender-okhttp -f .mfiles-exporter-sender-okhttp

%files extension-kotlin -f .mfiles-extension-kotlin

%files extension-trace-propagators -f .mfiles-extension-trace-propagators

%files sdk -f .mfiles-sdk

%files sdk-common -f .mfiles-sdk-common

%files sdk-logs -f .mfiles-sdk-logs

%files sdk-metrics -f .mfiles-sdk-metrics

%files sdk-profiles -f .mfiles-sdk-profiles

%files sdk-trace -f .mfiles-sdk-trace

%files sdk-extension-autoconfigure -f .mfiles-sdk-extension-autoconfigure

%files sdk-extension-autoconfigure-spi -f .mfiles-sdk-extension-autoconfigure-spi

%files sdk-extension-declarative-config -f .mfiles-sdk-extension-declarative-config

%files sdk-extension-incubator -f .mfiles-sdk-extension-incubator

%changelog
* Thu Nov 26 2026 Ivan Khanas <xeno@altlinux.org> 1.68.0-alt1
- Initial build for ALT.
