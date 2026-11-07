%define _unpackaged_files_terminate_build 1

Name: java-jwt
Version: 4.6.2
Release: alt1

Summary: Java implementation of JSON Web Tokens
License: MIT
Group: Development/Java
URL: https://github.com/auth0/java-jwt
VCS: https://github.com/auth0/java-jwt.git
BuildArch: noarch

Source: %name-%version.tar
Patch: system-gradle.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: java-17-openjdk-devel
BuildRequires: jackson-core
BuildRequires: jackson-databind
BuildRequires: bouncycastle
BuildRequires: junit
BuildRequires: hamcrest
BuildRequires: mockito-core

%description
Java JWT creates, decodes and verifies JSON Web Tokens using HMAC, RSA
and ECDSA signatures, with configurable claim verification.

%package javadoc
Summary: API documentation for Java JWT
Group: Development/Java

%description javadoc
API documentation for Java JWT.

%prep
%setup
%autopatch -p1

%build
%gradle_publish --no-daemon

%install
%gradle_register --artifacts=java-jwt
%gradle_register_javadoc --artifacts=java-jwt
%gradle_install

%check
%gradle_check --no-daemon

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 4.6.2-alt1
- Initial build for ALT.
