%define _unpackaged_files_terminate_build 1

Name: jimfs
Version: 1.3.1
Release: alt1

Summary: An in-memory file system for Java 8+
License: Apache-2.0
Group: Development/Java
Url: https://github.com/google/jimfs
Vcs: https://github.com/google/jimfs.git
ExclusiveArch: %java_arches
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: jsr-305
BuildRequires: jspecify
BuildRequires: guava-testlib
BuildRequires: truth
BuildRequires: icu4j
BuildRequires: junit
BuildRequires: google-error-prone-annotations
BuildRequires: google-error-prone-core
BuildRequires: auto-common
BuildRequires: auto-service
BuildRequires: compile-testing
BuildRequires: maven-plugin-bundle
BuildRequires: guava-beta-checker

%description
Jimfs is an in-memory file system for Java 8 and above, implementing the
java.nio.file abstract file system APIs.

%{?javadoc_package}

%prep
%setup
%autopatch -p1

%pom_remove_plugin -r :maven-javadoc-plugin

%pom_remove_dep -r com.google.auto.service:auto-service-annotations
%pom_add_dep com.google.errorprone:error_prone_annotations jimfs

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%changelog
* Tue Dec 2 2025 Ivan Khanas <xeno@altlinux.org> 1.3.1-alt1
- First build for ALT.
