%define _unpackaged_files_terminate_build 1

Name: jhalterman-typetools
Version: 0.6.3
Release: alt1

Summary: Tools for working with generic types
License: Apache-2.0
Group: Development/Java
Url: https://github.com/jhalterman/typetools
Vcs: https://github.com/jhalterman/typetools.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: sonatype-oss-parent
BuildRequires: maven-plugin-bundle
BuildRequires: testng

%description
A simple, zero-dependency library for working with types.

%{?javadoc_package}

%prep
%setup
%pom_remove_plugin -r :maven-javadoc-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%changelog
* Tue Dec 02 2025 Ivan Khanas <xeno@altlinux.org> 0.6.3-alt1
- First build for ALT.

