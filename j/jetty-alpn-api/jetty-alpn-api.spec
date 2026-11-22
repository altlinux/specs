%define _unpackaged_files_terminate_build 1

Name: jetty-alpn-api
Version: 1.1.3
Release: alt3

Summary: Application Layer Protocol Negotiation API for Jetty
License: Apache-2.0 or EPL-1.0
Group: Development/Java
URL: https://eclipse.googlesource.com/jetty/org.eclipse.jetty.alpn/
VCS: https://eclipse.googlesource.com/jetty/org.eclipse.jetty.alpn

Source0: %name-%version.tar
Source1: LICENSE-APACHE-2.0
Source2: LICENSE-EPL-1.0.html
Patch0: system-jetty-parent.patch

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.eclipse.jetty:jetty-parent:pom:)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)

%description
Standalone Application Layer Protocol Negotiation API, including client and
server provider interfaces and registration for SSL engines and sockets.

%package javadoc
Summary: API documentation for %name
Group: Development/Java

%description javadoc
API documentation for the standalone Jetty ALPN API.

%prep
%setup
%autopatch -p1
cp -p %SOURCE1 %SOURCE2 .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-APACHE-2.0 LICENSE-EPL-1.0.html

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Nov 21 2026 Ivan Khanas <xeno@altlinux.org> 1.1.3-alt3
- Initial build for ALT.
