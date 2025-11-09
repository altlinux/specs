%define _unpackaged_files_terminate_build 1

Name: apicatalog-titanium-rdf-n-quads
Version: 1.0.2
Release: alt1

Summary: Java implementation of a streaming RDF N-Quads reader and writer
License: Apache-2.0
Group: Development/Java
Url: https://apicatalog.com
Vcs: https://github.com/filip26/titanium-rdf-n-quads.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-11-compat
BuildRequires: maven-local
BuildRequires: apicatalog-tree-io
BuildRequires: junit5
BuildRequires: maven-source-plugin
BuildRequires: jakarta-json2
BuildRequires: apicatalog-titanium-rdf-api

%package javadoc
Group: Development/Java
Summary: Javadoc for %name

%description
A Java implementation of a streaming RDF N-Quads reader and writer, optimized
for efficient parsing, serialization, and handling of large RDF datasets. It
enables scalable processing of RDF statements in a memory-efficient, streaming
fashion.

%description javadoc
This package contains javadoc for %name.

%prep
%setup
%pom_remove_plugin :maven-javadoc-plugin

%pom_add_dep -r org.apiguardian:apiguardian-api:test

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Nov 08 2025 Ivan Khanas <xeno@altlinux.org> 1.0.2-alt1
- First build for ALT.
