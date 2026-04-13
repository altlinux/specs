%define _unpackaged_files_terminate_build 1

Name: nachocalendar
Version: 0.25
Release: alt1

Summary: Swing calendar components library
License: LGPL-3.0
Group: Development/Java
Url: https://github.com/Appendium/nachocalendar
Vcs: https://github.com/Appendium/nachocalendar.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-17-compat
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin
BuildRequires: junit
BuildRequires: lombok
BuildRequires: slf4j

%description
NachoCalendar is a Swing calendar/date chooser component library.
This package builds the core library module.

%package parent
Summary: Parent pom for %name
Group: Development/Java

%description parent
%summary.

%prep
%setup

%pom_remove_parent

%pom_disable_module nachocalendar-demo

%pom_remove_plugin -r :nexus-staging-maven-plugin
%pom_remove_plugin -r :maven-gpg-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :versions-maven-plugin
%pom_remove_plugin -r :maven-release-plugin

%build
%mvn_build -s -j

%install
%mvn_install

%files -f .mfiles-nachocalendar
%doc LICENSE README.md

%files parent -f .mfiles-nachocalendar-parent

%changelog
* Mon Apr 13 2026 Ivan Khanas <xeno@altlinux.org> 0.25-alt1
- First build for ALT.
