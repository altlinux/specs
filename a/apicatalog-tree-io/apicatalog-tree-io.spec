%define _unpackaged_files_terminate_build 1

Name: apicatalog-tree-io
Version: 0.8.0
Release: alt2

Summary: Uniform API to read/write heterogeneous tree data models
License: Apache-2.0
Group: Development/Java
Url: https://apicatalog.com
Vcs: https://github.com/filip26/tree-io.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: jpackage-default
BuildRequires: maven-local

BuildRequires: maven-source-plugin
BuildRequires: jakarta-json2
BuildRequires: jackson-databind
BuildRequires: apiguardian

%description
Tree-io (pronounced tri-yo) provides a consistent and lightweight abstraction
for working with heterogeneous hierarchical data structures. It is
format-agnostic (JSON, YAML, CBOR) and library-agnostic (Jackson, Gson,
Jakarta), allowing you to read, manipulate, and write trees uniformly
without depending on a specific parser or serializer.

%javadoc_package

%prep
%setup
%pom_remove_plugin -r :maven-javadoc-plugin

# Add apiguardian as a test dependency to avoid warnings by junit.
%pom_add_dep -r org.apiguardian:apiguardian-api:test

%pom_disable_module cbor-adapter

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Mon Aug 31 2026 Evgeniy Serov <scala@altlinux.org> 0.8.0-alt2
- Build with jpackage-default.
- Switch to macro-based javadoc packaging.

* Fri Nov 08 2025 Ivan Khanas <xeno@altlinux.org> 0.8.0-alt1
- First build for ALT.
