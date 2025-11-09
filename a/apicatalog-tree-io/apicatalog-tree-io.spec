%define _unpackaged_files_terminate_build 1

Name: apicatalog-tree-io
Version: 0.8.0
Release: alt1

Summary: Uniform API to read/write heterogeneous tree data models
License: Apache-2.0
Group: Development/Java
Url: https://apicatalog.com
Vcs: https://github.com/filip26/tree-io.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-11-compat
BuildRequires: maven-local
BuildRequires: maven-source-plugin
BuildRequires: jakarta-json2
BuildRequires: jackson-databind
BuildRequires: apiguardian

%package javadoc
Group: Development/Java
Summary: Javadoc for %name

%description
Tree-io (pronounced tri-yo) provides a consistent and lightweight abstraction
for working with heterogeneous hierarchical data structures. It is
format-agnostic (JSON, YAML, CBOR) and library-agnostic (Jackson, Gson,
Jakarta), allowing you to read, manipulate, and write trees uniformly
without depending on a specific parser or serializer.

%description javadoc
This package contains javadoc for %name.

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

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Nov 08 2025 Ivan Khanas <xeno@altlinux.org> 0.8.0-alt1
- First build for ALT.
