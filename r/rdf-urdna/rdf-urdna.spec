%define _unpackaged_files_terminate_build 1
%def_with check

Name: rdf-urdna
Version: 1.4
Release: alt1

Summary: This is an implementation of the Universal RDF Dataset Normalization Algorithm for Java 1.8
License: Apache-2.0
Group: Development/Java
Url: https://github.com/setl/rdf-urdna
Vcs: https://github.com/setl/rdf-urdna.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: 0001-Adapt-to-gradle-8-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: jpackage-11-compat
BuildRequires: apicatalog-titanium-json-ld
%if_with check
BuildRequires: junit
BuildRequires: jakarta-json2
BuildRequires: hamcrest
%endif

%package javadoc
Group: Development/Java
Summary: Javadoc for %name

%description
A Java implementation of the RDF Dataset Canonicalization algorithm (URDNA
2015). This library transforms RDF datasets into a canonical form, enabling
deterministic digital signatures and easy comparison of RDF data.

%description javadoc
This package contains javadoc for %name.

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register
%gradle_register_javadoc

%gradle_install

%check
%gradle_check

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Nov 09 2025 Ivan Khanas <xeno@altlinux.org> 1.4-alt1
- First build for ALT.
