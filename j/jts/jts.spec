BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jts
Version:       1.15.0
Release:       alt1_4jpp11
Group:         Development/Java
Summary:       Java Topology Suite
License:       EPL-1.0 or BSD
URL:           https://projects.eclipse.org/projects/locationtech.jts
Source0:       https://github.com/locationtech/jts/archive/jts-%{version}/jts-jts-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.googlecode.json-simple:json-simple)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.jdom:jdom2)

BuildArch:     noarch
Source44: import.info

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

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n jts-jts-%{version}

# Uneeded plugins for RPM builds
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin

# Remove this test because junit.swingui is unavailable
rm modules/core/src/test/java/test/jts/junit/SimpleTest.java
sed -i -e '/SimpleTest\.class/d' modules/core/src/test/java/test/jts/junit/MasterTester.java

# Don't bundle deps
%pom_remove_plugin :maven-assembly-plugin modules/tests modules/app

# Backward compatibility aliases
%mvn_alias org.locationtech.jts:jts-core com.vividsolutions:jts-core com.vividsolutions:jts
%mvn_alias org.locationtech.jts.io:jts-io-common com.vividsolutions:jts-io

%mvn_package ":jts-io*" jts-io
%mvn_package ":jts{,-modules}" jts-parent
%mvn_package ":jts-tests" jts-app

%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles-%{name}-core
%doc README.md USING.md MIGRATION.md
%doc --no-dereference LICENSE*

%files app -f .mfiles-%{name}-app
%files example -f .mfiles-%{name}-example
%files io -f .mfiles-%{name}-io

%files parent -f .mfiles-%{name}-parent
%doc --no-dereference LICENSE*

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE*



%changelog
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

