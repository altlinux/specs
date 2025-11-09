%define _unpackaged_files_terminate_build 1

Name: apicatalog-titanium-rdf-api
Version: 1.0.0
Release: alt1

Summary: Collection of straightforward micro-interfaces for processing RDF statements
License: Apache-2.0
Group: Development/Java
Url: https://apicatalog.com
Vcs: https://github.com/filip26/titanium-rdf-api.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-11-compat
BuildRequires: maven-local
BuildRequires: jakarta-json-impl
BuildRequires: maven-source-plugin
BuildRequires: junit5

%package javadoc
Group: Development/Java
Summary: Javadoc for %name

%description
A collection of straightforward micro-interfaces for processing RDF statements
and facilitating seamless interoperability and data exchange across various
libraries.

%description javadoc
This package contains javadoc for %name.

%prep
%setup
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Nov 06 2025 Ivan Khanas <xeno@altlinux.org> 1.0.0-alt1
- First build for ALT.
