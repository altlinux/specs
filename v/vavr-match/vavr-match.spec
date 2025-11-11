%define _unpackaged_files_terminate_build 1

Name: vavr-match
Version: 0.10.7
Release: alt1

Summary: Declarative Pattern Matching for Java
License: Apache-2.0
Group: Development/Java
Url: https://vavr.io
Vcs: https://github.com/vavr-io/vavr-match.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin
BuildRequires: moditect-maven-plugin

%description
Vavr Match is a powerful pattern matching component of the Vavr functional
library for Java. It enables declarative, expressive code by replacing complex
imperative conditionals with type-safe, functional pattern matching constructs.

%prep
%setup
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin

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
* Mon Nov 11 2025 Ivan Khanas <xeno@altlinux.org> 0.10.7-alt1
- First build for ALT.
