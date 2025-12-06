%define _unpackaged_files_terminate_build 1

Name: system-lambda
Version: 1.2.1
Release: alt1

Summary: System Lambda is a collection of functions for testing code that uses java.lang.System
License: MIT
Group: Development/Java
Url: https://github.com/stefanbirkner/system-lambda
Vcs: https://github.com/stefanbirkner/system-lambda.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: fishbowl
BuildRequires: junit
BuildRequires: assertj-core

%description
System Lambda is a collection of functions for testing code which uses java.lang.System.
System Lambda is published under the MIT license. It requires at least Java 8.
For JUnit 4 there is an alternative to System Lambda. Its name is System Rules.

%prep
%setup
%autopatch -p1

%pom_remove_parent

%build
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Wed Dec 03 2025 Ivan Khanas <xeno@altlinux.org> 1.2.1-alt1
- First build for ALT.
