%define _unpackaged_files_terminate_build 1

Name: dmlloyd-module-info
Version: 2.2
Release: alt1

Summary: Module-info.class generator and Maven plugin
License: LGPL-2.1-or-later
Group: Development/Java
Url: https://github.com/dmlloyd/module-info
Vcs: https://github.com/dmlloyd/module-info.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: maven-plugin-plugin
BuildRequires: maven-plugin-tools
BuildRequires: maven-shade-plugin
BuildRequires: maven-filtering
BuildRequires: objectweb-asm
BuildRequires: beust-jcommander
BuildRequires: snakeyaml
BuildRequires: plexus-utils

%description
Module Info Generator creates module-info.class files from YAML definitions
and can be used as a Maven plugin.

%prep
%setup

%pom_remove_parent
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_dep org.apache.maven:maven-project

%build
%mvn_build -j -- -Dbootstrap

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference README.adoc

%changelog
* Fri Mar 27 2026 Ivan Khanas <xeno@altlinux.org> 2.2-alt1
- First build for ALT.
