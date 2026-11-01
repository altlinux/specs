%define _unpackaged_files_terminate_build 1

%if "%_host_cpu" == "x86_64" || "%_host_cpu" == "aarch64"
%define conscrypt_enabled true
%else
%define conscrypt_enabled false
%endif

Name: okhttp
Version: 5.5.1
Release: alt1

Summary: HTTP client for JVM applications
License: Apache-2.0
Group: Development/Java
Url: https://square.github.io/okhttp
VCS: https://github.com/square/okhttp.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-jvm.patch
# Conscrypt native libraries are currently packaged only for these two arches.
Patch1: okhttp-no-conscrypt.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: animal-sniffer
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlinx-coroutines
BuildRequires: xgradle
BuildRequires: mvn(com.squareup.okio:okio)
BuildRequires: mvn(com.squareup.okio:okio-jvm)
BuildRequires: mvn(com.squareup:kotlinpoet-jvm)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.bouncycastle:bctls-jdk18on)
BuildRequires: mvn(org.brotli:dec)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
%if "%_host_cpu" == "x86_64" || "%_host_cpu" == "aarch64"
BuildRequires: mvn(org.conscrypt:conscrypt-openjdk)
%endif
BuildRequires: mvn(org.openjsse:openjsse)

%description
OkHttp is an HTTP and HTTP/2 client with connection pooling, caching,
WebSockets and TLS verification. This JVM profile includes the core and BOM,
TLS helpers, logging, cookies, URLConnection, SSE, DNS-over-HTTPS, coroutines,
Brotli and MockWebServer libraries. JDK TLS and optional Bouncy Castle TLS are
supported, and the OpenJSSE adapter is included. Conscrypt is enabled on
x86_64 and aarch64, where its native provider is available. GraalVM
native-image integration is not compiled; its upstream sources are retained.

%prep
%setup
%patch0 -p1
%if "%_host_cpu" != "x86_64" && "%_host_cpu" != "aarch64"
%patch1 -p1
%endif

%build
rm -rf %_mavenrepolocal
%gradle_publish -Pconscrypt=%conscrypt_enabled

%install
%gradle_register
%gradle_register_bom
%gradle_install

# Upstream tests retained, but Burst/AssertK test dependencies are omitted
# by user request. Installed HTTP/HTTPS consumers are checked separately.

%files -f .mfiles
%doc LICENSE.txt README.md

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 5.5.1-alt1
- Initial build for ALT.
