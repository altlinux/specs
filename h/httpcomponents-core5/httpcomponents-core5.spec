%define _unpackaged_files_terminate_build 1

Name: httpcomponents-core5
Version: 5.4.4
Release: alt1

Summary: Apache HttpComponents Core 5 transport foundation
License: Apache-2.0
Group: Development/Java
URL: https://hc.apache.org/httpcomponents-core-5.4.x/
VCS: https://github.com/apache/httpcomponents-core.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.apache.httpcomponents:httpcomponents-parent:pom:)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.conscrypt:conscrypt-openjdk)
BuildRequires: mvn(org.reactivestreams:reactive-streams)

%description
HTTP/1.1 protocol and transport foundation for Apache HttpComponents 5.
The same source builds the HTTP/2 and Reactive Streams extensions.

%package h2
Summary: HTTP/2 transport for Apache HttpComponents Core 5
Group: Development/Java

%description h2
HTTP/2 protocol support and TLS integration for HttpComponents Core 5.

%package reactive
Summary: Reactive Streams bindings for Apache HttpComponents Core 5
Group: Development/Java

%description reactive
Reactive Streams producers and consumers for HttpComponents Core 5.

%package javadoc
Summary: API documentation for Apache HttpComponents Core 5
Group: Development/Documentation

%description javadoc
API documentation for Apache HttpComponents Core 5.

%prep
%setup
# The separate integration-test/benchmark harness is not a runtime module.
%pom_disable_module httpcore5-testing
# Development checks require separate tooling and comparison artifacts.
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :japicmp-maven-plugin
# Preserve the optional Conscrypt API with the genuine system artifact.
%pom_change_dep org.conscrypt:conscrypt-openjdk-uber \
    org.conscrypt:conscrypt-openjdk
%pom_change_dep org.conscrypt:conscrypt-openjdk-uber \
    org.conscrypt:conscrypt-openjdk httpcore5-h2
%mvn_package :*::sources: __noinstall
%mvn_package :httpcore5-h2 h2
%mvn_package :httpcore5-reactive reactive
%mvn_file :httpcore5 httpcomponents5/httpcore5
%mvn_file :httpcore5-h2 httpcomponents5/httpcore5-h2
%mvn_file :httpcore5-reactive httpcomponents5/httpcore5-reactive

%build
# Full tests require the unavailable Testcontainers artifacts.
%mvn_build -f -- -Dmaven.compiler.release=

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files h2 -f .mfiles-h2

%files reactive -f .mfiles-reactive

%files javadoc
%_javadocdir/%name

%changelog
* Wed Nov 11 2026 Ivan Khanas <xeno@altlinux.org> 5.4.4-alt1
- Initial build for ALT.
