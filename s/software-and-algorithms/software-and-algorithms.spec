%define _unpackaged_files_terminate_build 1

Name: software-and-algorithms
Version: 1.0.0
Release: alt1

Summary: Neat algorithm implementations in Java
License: Apache-2.0
Group: Development/Java
Url: https://github.com/KevinStern/software-and-algorithms
Vcs: https://github.com/KevinStern/software-and-algorithms.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: maven-local
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-source-plugin

%description
%summary.

%prep
%setup
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -j -- -Dmaven.compiler.source=1.8 \
  -Dmaven.compiler.target=1.8 \
  -Dmaven.javadoc.source=1.8 \
  -Dmaven.compiler.release=8 \
  #

%install
%mvn_install

%files -f .mfiles

%changelog
* Mon Nov 24 2025 Ivan Khanas <xeno@altlinux.org> 1.0.0-alt1
- Fist build for ALT.
