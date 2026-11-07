%define _unpackaged_files_terminate_build 1

Name: jwks-rsa-java
Version: 0.24.2
Release: alt1

Summary: JSON Web Key Set client for Java
License: MIT
Group: Development/Java
URL: https://github.com/auth0/jwks-rsa-java
VCS: https://github.com/auth0/jwks-rsa-java.git
BuildArch: noarch

Source: %name-%version.tar
Patch: system-gradle.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: java-17-openjdk-devel
BuildRequires: jackson-databind
BuildRequires: guava
BuildRequires: junit
BuildRequires: mockito-core
BuildRequires: hamcrest

%description
Retrieves and caches JSON Web Keys, parses RSA and EC public keys, and
provides configurable retrieval limits and HTTP clients.

%package javadoc
Summary: API documentation for the JSON Web Key Set client
Group: Development/Java

%description javadoc
API documentation for the JSON Web Key Set client.

%prep
%setup
%autopatch -p1


%build
%gradle_publish --no-daemon

%install
%gradle_register --artifacts=jwks-rsa
%gradle_register_javadoc --artifacts=jwks-rsa
%gradle_install

%check
%gradle_check --no-daemon

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 0.24.2-alt1
- Initial build for ALT.
