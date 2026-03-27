%define _unpackaged_files_terminate_build 1

Name: parsson
Version: 1.1.7
Release: alt1

Summary: Eclipse implementation of Jakarta JSON Processing specification
License: Apache-2.0
Group: Development/Java
Url: https://github.com/eclipse-ee4j/parsson
Vcs: https://github.com/eclipse-ee4j/parsson.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-17-compat
BuildRequires: ee4j-parent
BuildRequires: maven-assembly-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-bundle
BuildRequires: spec-version-maven-plugin
BuildRequires: jakarta-json-api
BuildRequires: jakarta-ws-rs
BuildRequires: jaxb-api

%description
Eclipse Parsson is an implementation of Jakarta JSON Processing specification.

%prep
%setup
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :buildnumber-maven-plugin
%pom_disable_module bundles
%pom_disable_module demos
%pom_disable_module providers

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles

%changelog
* Tue Mar 25 2026 Ivan Khanas <xeno@altlinux.org> 1.1.7-alt1
- First build for ALT.
