Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without  memoryfilesystem

Name:           assertj-core
Version:        3.8.0
Release:        alt1_2jpp8
Summary:        Library of assertions similar to fest-assert
License:        ASL 2.0
URL:            http://joel-costigliola.github.io/assertj/
Source0:        https://github.com/joel-costigliola/assertj-core/archive/assertj-core-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(cglib:cglib-nodep)
%if %{with memoryfilesystem}
BuildRequires:  mvn(com.github.marschall:memoryfilesystem)
%endif
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.mockito:mockito-core)
Source44: import.info

%description
A rich and intuitive set of strongly-typed assertions to use for unit testing
(either with JUnit or TestNG).

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_parent
%pom_xpath_inject "pom:project" "<groupId>org.assertj</groupId>"

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin org.jacoco:jacoco-maven-plugin

# package org.mockito.internal.util.collections does not exist
rm -rf ./src/test/java/org/assertj/core/error/ShouldContainString_create_Test.java

%if %{without memoryfilesystem}
%pom_remove_dep :memoryfilesystem
rm -r src/test/java/org/assertj/core/internal/{Paths*.java,paths}
%endif

# test lib not in Fedora
%pom_remove_dep com.tngtech.java:junit-dataprovider

%build
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md CONTRIBUTING.md
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc CONTRIBUTING.md
%doc --no-dereference LICENSE.txt

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 3.8.0-alt1_2jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 3.8.0-alt1_1jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_3jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_2jpp8
- new fc release

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_1jpp8
- added osgi provides

