%define _unpackaged_files_terminate_build 1

Name: apicatalog-titanium-jcs
Version: 1.1.1
Release: alt1

Summary: Titanium JCS is a Java implementation of the RFC 8785 JSON Canonicalization Scheme
License: Apache-2.0
Group: Development/Java
Url: https://apicatalog.com
Vcs: https://github.com/filip26/titanium-jcs.git
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

%package javadoc
Group: Development/Java
Summary: Javadoc for %name

%description
The JSON Canonicalization Scheme (JCS) defines a deterministic way to serialize
JSON so that the same JSON data model always produces the same byte sequence.

This is critical for use cases such as digital signatures, hashing, and data
integrity verification, where even small differences in whitespace, member
ordering, or number formatting would otherwise break validation.

By normalizing JSON into a canonical form, JCS ensures interoperability across
systems and guarantees stable, repeatable representations of data.

Titanium JCS is a Java implementation of the RFC 8785 JSON Canonicalization
Scheme (JCS).

%description javadoc
This package contains javadoc for %name.

%prep
%setup
%pom_remove_plugin :maven-javadoc-plugin

%pom_add_dep org.apiguardian:apiguardian-api:test

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Nov 08 2025 Ivan Khanas <xeno@altlinux.org> 1.1.1-alt1
- First build for ALT.
