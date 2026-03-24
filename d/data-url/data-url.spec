%define _unpackaged_files_terminate_build 1
%def_with check

Name: data-url
Version: 2.0.1
Release: alt1

Summary: Support for data URLs as specified in RFC 2397
Group: Development/Java
License: Apache-2.0
Url: https://robtimus.github.io/data-url/
Vcs: https://github.com/robtimus/data-url
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
BuildRequires: i18n-maven-plugin
BuildRequires: moditect-maven-plugin
BuildRequires: robtimus-build-helper-maven-plugin
BuildRequires: maven-assembly-plugin
BuildRequires: maven-clean-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-deploy-plugin
%if_with check
BuildRequires: junit5
BuildRequires: hamcrest
BuildRequires: mockito-core
BuildRequires: apache-commons-io
%endif

%{?javadoc_package}

%description
Java library that adds support for the data protocol as specified in RFC 2397.

%prep
%setup
%pom_remove_parent
%pom_xpath_inject "pom:project" "<groupId>com.github.robtimus</groupId>"
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-surefire-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-project-info-reports-plugin

%build
%if_with check
%mvn_build
%else
%mvn_build -f
%endif

%install
%mvn_install

%files -f .mfiles

%changelog
* Tue Mar 24 2026 Arseniy Kostevich <faux@altlinux.org> 2.0.1-alt1
- Initial build for ALT.
