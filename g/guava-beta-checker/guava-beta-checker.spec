%define _unpackaged_files_terminate_build 1

Name: guava-beta-checker
Version: 1.0
Release: alt1

Summary: An Error Prone plugin that checks for usages of Guava APIs
License: Apache-2.0
Group: Development/Java
Url: https://github.com/google/guava-beta-checker
Vcs: https://github.com/google/guava-beta-checker.git
ExclusiveArch: %java_arches
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: sonatype-oss-parent
BuildRequires: guava
BuildRequires: junit
BuildRequires: google-error-prone-core
BuildRequires: auto-service
BuildRequires: compile-testing

%description
An Error Prone plugin that checks for usages of Guava APIs that are annotated
with the @Beta annotation. Such APIs should never be used in library code that
other projects may depend on; using the Beta Checker can help library projects
ensure that they don't use them.

%prep
%setup
%autopatch -p1

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles

%changelog
* Wed Nov 26 2025 Ivan Khanas <xeno@altlinux.org> 1.0-alt1
- First build for ALT.
