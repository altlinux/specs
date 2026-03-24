%define _unpackaged_files_terminate_build 1

Name: jakarta-jsonb-api
Version: 3.0.1
Release: alt1

Summary: API of binding layer for converting Java objects
Group: Development/Java
License: EPL-2.0
Url: https://jakartaee.github.io/jsonb-api/
Vcs: https://github.com/jakartaee/jsonb-api
BuildArch: noarch

Source0: %name-%version.tar.gz

BuildRequires(pre): rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: ee4j-parent
BuildRequires: jakarta-json2
BuildRequires: junit
BuildRequires: maven-deploy-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: spec-version-maven-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-jar-plugin
BuildRequires: maven-source-plugin
BuildRequires: bnd-maven-plugin

%description
Jakarta JSON Binding is a standard binding layer for converting Java objects
to/from JSON documents.

%{?javadoc_package}

%prep
%setup
pushd api/
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :build-helper-maven-plugin
%pom_remove_plugin :spotbugs-maven-plugin
%pom_remove_plugin :maven-jxr-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :bnd-baseline-maven-plugin

%build
%mvn_build -- --file=api/pom.xml

%install
%mvn_install

%files -f .mfiles

%changelog
* Tue Mar 24 2026 Arseniy Kostevich <faux@altlinux.org> 3.0.1-alt1
- Initial build for ALT.
