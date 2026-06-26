Name: jheaps
Version: 0.14
Release: alt1

Summary: Java library that provides various heap implementations
License: Apache-2.0
Group: Development/Java
Url: https://www.jheaps.org
Vcs: https://github.com/d-michail/jheaps
BuildArch: noarch

Source0: https://github.com/d-michail/jheaps/archive/%name-%version.tar.gz

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default

BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

%description
JHeaps is a free library that provides
various heap implementations written in Java.

%javadoc_package

%prep
%setup

%pom_remove_plugin :jacoco-maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Fri Jun 26 2026 Anton Meleshnikov <alton@altlinux.org> 0.14-alt1
- Initial build for Sisyphus.
