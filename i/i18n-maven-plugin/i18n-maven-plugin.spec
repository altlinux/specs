%define _unpackaged_files_terminate_build 1
%def_with check

Name: i18n-maven-plugin
Version: 3.1.2
Release: alt1

Summary: A Maven plugin for generating accessor classes for I18N resources
Group: Development/Java
License: Apache-2.0
Url: https://robtimus.github.io/i18n-maven-plugin/
Vcs: https://github.com/robtimus/i18n-maven-plugin
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
BuildRequires: maven-plugin-plugin
BuildRequires: maven-clean-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-deploy-plugin
BuildRequires: apache-commons-io
BuildRequires: freemarker
%if_with check
BuildRequires: junit5
BuildRequires: hamcrest
BuildRequires: mockito-core
%endif

%{?javadoc_package}

%description
The I18N Maven Plugin allows you to generate I18N classes from I18N resource
files. Such I18N classes provides easy and safe access to the keys in their
backing I18N resource files, without risking any MissingResourceExceptions
or getting the number of place holders wrong.

%prep
%setup
%pom_remove_parent
%pom_xpath_inject "pom:project" "<groupId>com.github.robtimus</groupId>"
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :build-helper-maven-plugin
%pom_remove_plugin :maven-surefire-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :central-publishing-maven-plugin
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
* Tue Mar 24 2026 Arseniy Kostevich <faux@altlinux.org> 3.1.2-alt1
- Initial build for ALT.
