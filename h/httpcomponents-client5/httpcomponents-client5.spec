%define _unpackaged_files_terminate_build 1

Name: httpcomponents-client5
Version: 5.6.5
Release: alt1

Summary: Apache HttpComponents Client 5 HTTP agent
License: Apache-2.0 and MPL-2.0
Group: Development/Java
URL: https://hc.apache.org/httpcomponents-client-5.6.x/
VCS: https://github.com/apache/httpcomponents-client.git

Source0: %name-%version.tar


BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.apache.httpcomponents:httpcomponents-parent:pom:)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.httpcomponents.core5:httpcore5)
BuildRequires: mvn(org.apache.httpcomponents.core5:httpcore5-h2)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.conscrypt:conscrypt-openjdk)
BuildRequires: mvn(org.apache.commons:commons-compress)
BuildRequires: mvn(com.github.luben:zstd-jni)
BuildRequires: mvn(com.aayushatharva.brotli4j:brotli4j)

BuildArch: noarch

%description
Apache HttpComponents Client provides HTTP/1.1 and HTTP/2 clients, connection
management, authentication, MIME entities and a fluent API.

%package fluent
Summary: Fluent API for Apache HttpClient 5
Group: Development/Java

%description fluent
Convenient fluent HTTP request and response APIs for Apache HttpClient 5.

%package javadoc
Summary: API documentation for Apache HttpClient 5
Group: Development/Documentation

%description javadoc
API documentation for Apache HttpClient 5 and its runtime extensions.

%prep
%setup -n %name-%version
# The separate integration-test harness is not a runtime module.
%pom_disable_module httpclient5-testing
# MIME is included in main; retain the released main and fluent scope.
%pom_disable_module httpclient5-cache
%pom_disable_module httpclient5-observation
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :japicmp-maven-plugin
# Parent 15 inherits Surefire versions without hc.surefire.version.
%pom_remove_plugin :maven-surefire-plugin
# Build offline with the genuine upstream public suffix resource.
%pom_remove_plugin :download-maven-plugin httpclient5
# Imported BOMs are used only by tests and examples.
%pom_remove_dep org.junit:junit-bom
%pom_remove_dep io.opentelemetry:opentelemetry-bom
# Full tests require the unavailable Junixsocket 2 artifacts.
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:scope='test']" \
    httpclient5
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:scope='test']" \
    httpclient5-fluent
%pom_change_dep org.conscrypt:conscrypt-openjdk-uber \
    org.conscrypt:conscrypt-openjdk
%pom_change_dep org.conscrypt:conscrypt-openjdk-uber \
    org.conscrypt:conscrypt-openjdk httpclient5
%mvn_package :*::sources: __noinstall
%mvn_package :httpclient5-fluent fluent
%mvn_file :httpclient5 httpcomponents5/httpclient5
%mvn_file :httpclient5-fluent httpcomponents5/httpclient5-fluent

%build
%mvn_build -f -- -Dmaven.compiler.release=

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files fluent -f .mfiles-fluent

%files javadoc
%_javadocdir/%name

%changelog
* Wed Nov 11 2026 Ivan Khanas <xeno@altlinux.org> 5.6.5-alt1
- Initial build for ALT.
