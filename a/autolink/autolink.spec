%define _unpackaged_files_terminate_build 1
%def_without check

Name: autolink
Version: 0.12.0
Release: alt1

Summary: Java library to extract links
Group: Development/Java
License: MIT
Url: https://github.com/robinst/autolink-java
Vcs: https://github.com/robinst/autolink-java
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: maven-jar-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-compiler-plugin
BuildRequires: maven-source-plugin
%if_with check
# Build with tests requires junit5-5.13.0
BuildRequires: junit5
%endif

%package javadoc
Summary: API documentation for autolink
Group: Development/Java

%description
Java library to extract links such as URLs and email addresses from plain text.
It's smart about where a link ends, such as with trailing punctuation.

%description javadoc
This package contains API documentation for autolink.

%prep
%setup

%pom_remove_plugin :japicmp-maven-plugin
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-gpg-plugin

%build
%if_with check
%mvn_build
%else
%mvn_build -f
%endif

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Mar 24 2026 Arseniy Kostevich <faux@altlinux.org> 0.12.0-alt1
- Initial build for ALT.
