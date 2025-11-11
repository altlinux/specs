%define _unpackaged_files_terminate_build 1

Name: vavr
Version: 0.10.7
Release: alt1

Summary: Object-functional extension for Java that makes defensive programming easy
License: Apache-2.0
Group: Development/Java
Url: https://vavr.io
Vcs: https://github.com/vavr-io/vavr.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: vavr-match
BuildRequires: vavr-match-processor
BuildRequires: junit
BuildRequires: assertj-core
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin
BuildRequires: moditect-maven-plugin
BuildRequires: maven-clean-plugin
BuildRequires: maven-plugin-build-helper

%description
Vavr is an object-functional extension for Java that makes defensive
programming easy by leveraging immutability and functional control structures

%prep
%setup
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :scala-maven-plugin

%build

# Copy generated Tuple classes to standard Maven source directories for compilation.
cp -r vavr/src-gen/main/java/* vavr/src/main/java/
cp -r vavr/src-gen/test/java/* vavr/src/test/java/

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
