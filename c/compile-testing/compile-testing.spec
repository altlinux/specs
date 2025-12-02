%define _unpackaged_files_terminate_build 1

Name: compile-testing
Version: 0.23.0
Release: alt1

Summary: Testing tools for javac and annotation processors
License: Apache-2.0
Group: Development/Java
Url: https://github.com/google/compile-testing
Vcs: https://github.com/google/compile-testing.git
ExclusiveArch: %java_arches
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: jspecify
BuildRequires: guava
BuildRequires: truth
BuildRequires: google-error-prone-annotations
BuildRequires: junit
BuildRequires: auto-common
BuildRequires: auto-value
BuildRequires: auto-value-annotations
BuildRequires: maven-surefire-plugin
BuildRequires: maven-source-plugin

%description
A library for testing javac compilation with or without annotation processors.

%prep
%setup
%autopatch -p1

%pom_remove_plugin -r :maven-gpg-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%changelog
* Wed Nov 26 2025 Ivan Khanas <xeno@altlinux.org> 0.23.0-alt1
- First build for ALT.
