%define _unpackaged_files_terminate_build 1

Name: bridge-method-injector
Version: 1.32
Release: alt1

Summary: Preserve binary compatibility by generating Java bridge methods
License: MIT
Group: Development/Java
URL: https://github.com/jenkinsci/bridge-method-injector
VCS: https://github.com/jenkinsci/bridge-method-injector.git

Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: annotation-indexer
BuildRequires: mvn(com.github.spotbugs:spotbugs-annotations)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-commons)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(junit:junit)

%description
Annotations and Maven plugin that generate bridge methods, allowing Java
libraries to evolve while preserving compatibility with existing binaries.
Includes the complete annotation API and bytecode transformation engine.


%package annotation
Summary: Bridge method injection annotations
Group: Development/Java

%description annotation
Bridge method injection annotations.

%package javadoc
Summary: API documentation for %name
Group: Development/Java

%description javadoc
API documentation for the Bridge Method Injector and annotation library.

%prep
%setup
# Jenkins parent supplies release automation; use the system Maven lifecycle.
%pom_remove_parent
%mvn_package io.jenkins.tools:bridge-method-injector-parent
%mvn_package io.jenkins.tools:bridge-method-injector
%mvn_package io.jenkins.tools:bridge-method-annotation annotation

%build
%mvn_build -s -- -Dmaven.compiler.release=17 -Dmaven.compiler.proc=full \
    -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles

%files annotation -f .mfiles-annotation

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 16 2026 Ivan Khanas <xeno@altlinux.org> 1.32-alt1
- Initial build for ALT.
