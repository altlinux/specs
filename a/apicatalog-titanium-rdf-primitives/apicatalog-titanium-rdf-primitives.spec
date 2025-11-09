%define _unpackaged_files_terminate_build 1

Name: apicatalog-titanium-rdf-primitives
Version: 1.0.3
Release: alt1

Summary: Formerly part of Titanium JSON-LD
License: Apache-2.0
Group: Development/Java
Url: https://apicatalog.com
Vcs: https://github.com/filip26/titanium-rdf-primitives.git
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
%summary

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
* Sat Nov 08 2025 Ivan Khanas <xeno@altlinux.org> 1.0.3-alt1
- First build for ALT.
