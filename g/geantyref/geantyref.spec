%define _unpackaged_files_terminate_build 1

Name: geantyref
Version: 2.0.1
Release: alt1

Summary: Generic type reflection library with annotated type support
License: Apache-2.0
Group: Development/Java
URL: https://github.com/leangen/geantyref
VCS: https://github.com/leangen/geantyref.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: bnd-maven-plugin
BuildRequires: junit

%description
GeAnTyRef provides generic type reflection with support for AnnotatedType.
It resolves type parameters and supertypes, preserves type annotations, and
constructs parameterized and annotated types at runtime.

%package javadoc
Summary: API documentation for %name
Group: Development/Documentation

%description javadoc
API documentation for the GeAnTyRef generic type reflection library.

%prep
%setup

%build
# The test suite requires the declared JDK 17.
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%name
%doc LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 2.0.1-alt1
- Initial build for ALT.
