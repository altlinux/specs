%define _unpackaged_files_terminate_build 1

Name: java-classmate
Version: 1.7.3
Release: alt2

Summary: Library for introspecting generic type information
License: Apache-2.0
Group: Development/Java
Url: http://fasterxml.com
Vcs: https://github.com/FasterXML/java-classmate.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-11-compat
BuildRequires: fasterxml-oss-parent
BuildRequires: mvn(org.moditect:moditect-maven-plugin)

%description
ClassMate is a zero-dependency Java library for accurately introspecting type
information, including reliable resolution of generic type declarations for
both classes ("types") and members (fields, methods and constructors).

%prep
%setup
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles

%changelog
* Thu May 21 2026 Ilfat Aminov <aminov@altlinux.org> 1.7.3-alt2
- fix moditect dependency

* Tue Mar 25 2026 Ivan Khanas <xeno@altlinux.org> 1.7.3-alt1
- First build for ALT.
