%define _unpackaged_files_terminate_build 1

Name: modulemaker-maven-plugin
Version: 1.9
Release: alt1

Summary: A Maven plugin for creating a module-info.class
License: Apache-2.0
Group: Development/Java
Url: https://github.com/raphw/modulemaker-maven-plugin
Vcs: https://github.com/raphw/modulemaker-maven-plugin.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: maven-local
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: objectweb-asm
BuildRequires: maven-plugin-annotations
BuildRequires: maven-lib
BuildRequires: maven-source-plugin
BuildRequires: maven-plugin-plugin

%description
This plugin allows the creation of a module-info.class for projects on Java 6
to Java 8 where a module-info.java file cannot be compiled.

%prep
%setup

%build
%mvn_build -s -f -j -- -Dmaven.compiler.source=1.8 \
  -Dmaven.compiler.target=1.8 \
  -Dmaven.javadoc.source=1.8 \
  -Dmaven.compiler.release=9 \
  #

%install
%mvn_install

%files -f .mfiles-modulemaker-maven-plugin

%changelog
* Thu Nov 13 2025 Ivan Khanas <xeno@altlinux.org> 1.9-alt1
- Fist build for ALT.
