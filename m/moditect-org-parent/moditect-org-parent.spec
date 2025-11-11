%define _unpackaged_files_terminate_build 1

Name: moditect-org-parent
Version: 1.4.0
Release: alt1

Summary: Parent POM for all Maven based ModiTect projects
License: Apache-2.0
Group: Development/Java
Url: https://github.com/moditect/moditect-org-parent
Vcs: https://github.com/moditect/moditect-org-parent.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local

%description
%summary.

%prep
%setup
%pom_remove_plugin :license-maven-plugin
%pom_remove_plugin :git-commit-id-plugin
%pom_remove_plugin :formatter-maven-plugin
%pom_remove_plugin :impsort-maven-plugin
%pom_remove_plugin :versions-maven-plugin

%build
%mvn_build -f -j -- -Dmaven.compiler.source=1.8 \
  -Dmaven.compiler.target=1.8 \
  -Dmaven.javadoc.source=1.8 \
  -Dmaven.compiler.release=8 \
  #

%install
%mvn_install

%files -f .mfiles

%changelog
* Mon Nov 10 2025 Ivan Khanas <xeno@altlinux.org> 1.4.0-alt1
- First build for ALT.
