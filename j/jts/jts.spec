%define _unpackaged_files_terminate_build 1

Name: jts
Version: 1.20.0
Release: alt1

Summary: Java Topology Suite
License: (EPL-2.0 or BSD-3-Clause) and BSD-3-Clause
Group: Development/Java
URL: https://projects.eclipse.org/projects/locationtech.jts
VCS: https://github.com/locationtech/jts.git

Source0: %name-%version.tar
Patch0: %name-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(com.googlecode.json-simple:json-simple)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.commons:commons-csv)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.jdom:jdom2)

%description
The LocationTech JTS Topology Suite (JTS) is an open source Java software
library that provides an object model for planar geometry together with a
set of fundamental geometric functions. JTS conforms to the Simple Features
Specification for SQL published by the Open GIS Consortium.  JTS is designed
to be used as a core component of vector-based geomatics software such as
geographical information systems. It can also be used as a general-purpose
library providing algorithms in computational geometry.

%package app
Group: Development/Java
Summary: JTS - Applications & tools

%description app
Applications & tools for working with JTS.

%package example
Group: Development/Java
Summary: JTS - Examples

%description example
Examples of working JTS code.

%package io
Group: Development/Java
Summary: JTS - IO

%description io
JTS Extension for to assist in read / write operations.

%package parent
Group: Development/Java
Summary: JTS - Parent POMs

%description parent
JTS - Parent POMs.

%package lab
Summary: JTS experimental algorithms
Group: Development/Java

%description lab
Experimental geometry algorithms from the JTS laboratory.

%package javadoc
Group: Development/Java
Summary: Javadoc for %name
BuildArch: noarch

%description javadoc
This package contains API documentation for %name.

%prep
%setup -q
%autopatch -p1

# XMvn generates the API documentation and installs Maven artifacts.
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin

# These reporting/lint plugins are not available in the build repository.
# All upstream Java test sources and their Surefire configuration are retained.
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-checkstyle-plugin

# Install unbundled applications using the system dependencies.
%pom_remove_plugin :maven-assembly-plugin modules/tests modules/app

# Preserve the existing Maven compatibility aliases.
%mvn_alias org.locationtech.jts:jts-core \
    com.vividsolutions:jts-core com.vividsolutions:jts
%mvn_alias org.locationtech.jts.io:jts-io-common com.vividsolutions:jts-io

%mvn_package ":jts-io*" jts-io
%mvn_package ":jts{,-modules}" jts-parent
%mvn_package ":build-tools" jts-parent
%mvn_package ":jts-tests" jts-app

%build
%mvn_build -s -- -Dmaven.compiler.release=8 -Dmaven.javadoc.source=8

%install
%mvn_install

%files -f .mfiles-%name-core
%doc USING.md MIGRATION.md
%doc LICENSE* OSGEO_LICENSE.txt

%files app -f .mfiles-%name-app
%files example -f .mfiles-%name-example
%files io -f .mfiles-%name-io
%files lab -f .mfiles-%name-lab

%files parent -f .mfiles-%name-parent

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 1.20.0-alt1
- New version.

* Thu Sep 14 2023 Igor Vlasenko <viy@altlinux.org> 1.15.0-alt1_4jpp11
- restored in Sisyphus

* Tue Jun 18 2019 Igor Vlasenko <viy@altlinux.ru> 1.15.0-alt1_3jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_6jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_4jpp8
- java 8 mass update
