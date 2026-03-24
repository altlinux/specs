%define _unpackaged_files_terminate_build 1

Name: robtimus-build-helper-maven-plugin
Version: 2.0
Release: alt1

Summary: A Maven plugin that contains several utility goals
Group: Development/Java
License: Apache-2.0
Url: https://robtimus.github.io/build-helper-maven-plugin/
Vcs: https://github.com/robtimus/build-helper-maven-plugin
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-clean-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-deploy-plugin
BuildRequires: i18n-maven-plugin
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang3
BuildRequires: commonmark

%{?javadoc_package}

%description
A Maven plugin that contains several utility goals.

%prep
%setup
%pom_remove_parent
%pom_xpath_inject "pom:project" "<groupId>com.github.robtimus</groupId>"

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-surefire-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-project-info-reports-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles

%changelog
* Tue Mar 24 2026 Arseniy Kostevich <faux@altlinux.org> 2.0-alt1
- Initial build for ALT.
