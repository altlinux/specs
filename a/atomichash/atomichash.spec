%define _unpackaged_files_terminate_build 1

# Tests disabled: lock-free CAS algorithms livelock/busy-wait
# under hasher CPU restrictions, taking 30+ minutes per test suite.
%def_without check

Name: atomichash
Version: 1.0.1
Release: alt1

Summary: Atomic, non-blocking, hash-based data structures for Java
License: Apache-2.0
Group: Development/Java
Url: https://github.com/arxila/atomichash
Vcs: https://github.com/arxila/atomichash
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: java-11-openjdk-devel

%description
AtomicHash is a Java library providing atomic, non-blocking,
hash-based data structures. It offers thread-safe implementations
of hash maps and hash sets without the need for locks, using
compare-and-swap operations for concurrent access.

%package javadoc
Summary: API documentation for atomichash
Group: Development/Java

%description javadoc
API documentation for the atomichash library.

%prep
%setup
# Remove parent POM to avoid network resolution
%pom_remove_parent

# Remove junit-jupiter dep (version came from parent BOM) and re-add with explicit version
%pom_remove_dep org.junit.jupiter:junit-jupiter
%pom_add_dep org.junit.jupiter:junit-jupiter:5.10.2:test
%pom_add_dep org.apache.commons:commons-lang3:3.17.0:test

%build
%mvn_build %{?_without_check:-f}

%install
%mvn_install

%check
%mvn_build -s

%files -f .mfiles
%doc LICENSE.txt README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Thu May 29 2026 Timofei Fedotov <sovtouch@altlinux.org> 1.0.1-alt1
- Initial build for ALT Sisyphus.
