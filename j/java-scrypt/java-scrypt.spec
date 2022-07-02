Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: java-scrypt
Version: 1.4.0
Release: alt1_17jpp11
Summary: Java implementation of scrypt

License: ASL 2.0
URL: https://github.com/wg/scrypt
Source0: https://github.com/wg/scrypt/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: no-jni.patch
BuildArch: noarch

BuildRequires: maven-local
Source44: import.info

%description
A pure Java implementation of the scrypt key derivation function.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n scrypt-%{version}
%patch0 -p1

%pom_remove_plugin :maven-compiler-plugin

find -name '*.so' -print -delete
find -name '*.dylib' -print -delete
find -name '*.jar' -print -delete

%build
#Disble tests, since many of them are releated to JNI
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc README
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1.4.0-alt1_17jpp11
- update

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.4.0-alt1_13jpp11
- new version

