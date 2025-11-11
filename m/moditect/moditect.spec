%define _unpackaged_files_terminate_build 1

Name: moditect
Version: 1.3.0
Release: alt1

Summary: Tooling for the Java Module System 
License: Apache-2.0
Group: Development/Java
Url: https://github.com/moditect/moditect
Vcs: https://github.com/moditect/moditect.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: 0001-Fix-incompatibility-with-maven-archiever-3.5.2-alt-p.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: moditect-org-parent
BuildRequires: maven-shade-plugin
BuildRequires: javaparser
BuildRequires: maven-plugin-plugin

%description
Moditect is a comprehensive toolset for working with the Java Platform Module
System (JPMS).  It provides utilities and Maven integration for generating
module-info.java descriptors, enhancing existing JAR files with module
information, and creating modular runtime images.  This package includes the
core library, Maven plugin, and common configuration POM.

%package parent
Summary: Parent POM for Moditect project
Group: Development/Java
BuildArch: noarch

%description parent
Moditect is a tool for generating module descriptors (module-info.java) and
creating modular JARs for the Java Platform Module System (JPMS). This package
contains the parent POM that provides common configuration and dependency
management for all Moditect subprojects.

%package core
Summary: Core library for Moditect module system tooling
Group: Development/Java
BuildArch: noarch

%description core
Core library of Moditect that provides the fundamental functionality for
working with Java modules. It includes utilities for analyzing existing
JAR files, generating module-info.java descriptors, and creating modular
JARs compatible with Java Platform Module System (JPMS). This library is
used by the Maven plugin and other integration points.

%package aggregator
Summary: Aggregator POM for Moditect project
Group: Development/Java
BuildArch: noarch

%description aggregator
The aggregator POM for the Moditect project.  This module serves as the
top-level aggregator for building and managing all Moditect submodules (core
library, Maven plugin, and parent POM) as a unified project.  It defines common
build configuration, inter-module dependencies, and project-wide metadata,
ensuring consistent versioning and integration across the Moditect toolset.

%package maven-plugin
Summary: Maven plugin for Moditect module system tooling
Group: Development/Java
BuildArch: noarch

%description maven-plugin
Maven plugin for Moditect that integrates module system tooling into Maven
builds. It provides goals for generating module descriptors, enhancing
existing JAR files with module information, and creating runtime images.
This plugin enables seamless migration to Java Platform Module System (JPMS)
within Maven-based projects.

%prep
%setup
%autopatch -p1

%pom_disable_module integrationtest pom.xml

%pom_remove_plugin :license-maven-plugin parent/pom.xml

%build
%mvn_build -s -f -j -- -Dmaven.compiler.source=9 \
  -Dmaven.compiler.target=11 \
  -Dmaven.javadoc.source=11 \
  -Dmaven.compiler.release=11 \
  #

%install
%mvn_install

%files parent -f .mfiles-moditect-parent

%files core -f .mfiles-moditect

%files aggregator -f .mfiles-moditect-aggregator

%files maven-plugin -f .mfiles-moditect-maven-plugin

%changelog
* Mon Nov 10 2025 Ivan Khanas <xeno@altlinux.org> 1.3.0-alt1
- Fist build for ALT.
