%define _unpackaged_files_terminate_build 1

Name: mockito-errorprone
Epoch: 1
Version: 5.20.0
Release: alt1

Summary: Error Prone integration for Mockito framework
License: MIT
Group: Development/Java
Url: https://site.mockito.org
Vcs: https://github.com/mockito/mockito.git
ExclusiveArch: %java_arches
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: java-21-openjdk-devel
BuildRequires: xgradle
BuildRequires: biz-aQute-bnd-gradle-plugins
BuildRequires: mockito-core
BuildRequires: junit
BuildRequires: google-error-prone-core
BuildRequires: byte-buddy
BuildRequires: byte-buddy-agent
BuildRequires: maven-plugin-bundle
BuildRequires: apiguardian
BuildRequires: assertj-core
BuildRequires: hamcrest
BuildRequires: junit5
BuildRequires: objenesis
BuildRequires: opentest4j
BuildRequires: objectweb-asm
BuildRequires: guava
BuildRequires: auto-common
BuildRequires: auto-service

%description
Error Prone integration module for Mockito testing framework.

This package provides Error Prone compiler checks specific to Mockito, helping
to detect common mistakes and anti-patterns in Mockito usage at compile time.
It includes annotations and error checks that improve code quality and test
reliability by catching potential issues early in the development process.

The module integrates with Google's Error Prone static analysis tool to provide
additional compile-time verification for Mockito-based tests.

%prep
%setup
%autopatch -p1

# Remove unwanted directory for RPM build(requires kotlin-dsl).
rm -rf buildSrc

%build
%gradle_publish

%install
%gradle_register --artifacts=%name

%gradle_install

%files -f .mfiles

%changelog
* Tue Dec 02 2025 Ivan Khanas <xeno@altlinux.org> 1:5.20.0-alt1
- First build for ALT.
