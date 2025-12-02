%define _unpackaged_files_terminate_build 1

Name: google-java-format
Version: 1.32.0
Release: alt1

Summary: Reformats Java source code to comply with Google Java Style
License: Apache-2.0
Group: Development/Java
Url: https://github.com/google/google-java-format
Vcs: https://github.com/google/google-java-format.git
ExclusiveArch: %java_arches
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: maven-local
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-source-plugin
BuildRequires: replacer
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-shade-plugin
BuildRequires: jspecify
BuildRequires: auto-value-annotations
BuildRequires: auto-value
BuildRequires: auto-service
BuildRequires: google-error-prone-annotations
BuildRequires: google-error-prone-core
BuildRequires: compile-testing
BuildRequires: guava-testlib
BuildRequires: truth

%description
Google's Java code formatter that parses Java source code and reformats it to
the Google Java Style Guide specification.  Supports command-line usage, Maven,
Gradle, and IDE integrations.

%prep
%setup
%autopatch -p1

%pom_disable_module eclipse_plugin

%pom_remove_plugin -r :maven-javadoc-plugin

%pom_remove_dep -r com.google.auto.service:auto-service-annotations

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles

%changelog
* Mon Dec 1 2025 Ivan Khanas <xeno@altlinux.org> 1.32.0-alt1
- First build for ALT.
