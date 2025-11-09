%define _unpackaged_files_terminate_build 1

Name: apicatalog-titanium-rdfc
Version: 2.0.0
Release: alt1

Summary: An implementation of the W3C Standard RDF Dataset Canonicalization Algorithm in Java
License: Apache-2.0
Group: Development/Java
Url: https://apicatalog.com
Vcs: https://github.com/filip26/titanium-rdf-canon.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-11-compat
BuildRequires: maven-local
BuildRequires: junit5
BuildRequires: maven-source-plugin
BuildRequires: jakarta-json2
BuildRequires: apicatalog-titanium-rdf-api
BuildRequires: apicatalog-titanium-rdf-n-quads

%package javadoc
Group: Development/Java
Summary: Javadoc for %name

%description
%summary.

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
* Sat Nov 08 2025 Ivan Khanas <xeno@altlinux.org> 2.0.0-alt1
- First build for ALT.
