%define _unpackaged_files_terminate_build 1

Name: jakarta-json2
Version: 2.0.1
Release: alt1

Summary: Jakarta JSON Processing provides portable APIs to parse, generate, transform, and query JSON documents
License: Apache-2.0
Group: Development/Java
Url: https://projects.eclipse.org/projects/ee4j.jsonp
Vcs: https://github.com/jakartaee/jsonp-api.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

Conflicts: jakarta-json

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: spec-version-maven-plugin
BuildRequires: buildnumber-maven-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-bundle
BuildRequires: maven-dependency-plugin

%description
Jakarta JSON Processing provides portable APIs to parse, generate, transform,
and query JSON documents. This project contains Jakarta JSON Processing
specification, API and TCK.

%prep
%setup
%autopatch -p1
sed -i 's/%version-SNAPSHOT/%version/g' api/pom.xml

%pom_remove_parent
%pom_remove_parent api/pom.xml

%pom_remove_plugin -r :directory-maven-plugin
%pom_remove_plugin -r :glassfish-copyright-maven-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_remove_plugin :maven-dependency-plugin impl/pom.xml

%pom_disable_module jaxrs
%pom_disable_module bundles

%build
%mvn_build --skip-javadoc

%install
%mvn_install

%files -f .mfiles

%changelog
* Fri Nov 08 2025 Ivan Khanas <xeno@altlinux.org> 2.0.1-alt1
- First build for ALT.
