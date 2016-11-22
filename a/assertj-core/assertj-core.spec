Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           assertj-core
Version:        2.2.0
Release:        alt1_2jpp8
Summary:        Library of assertions similar to fest-assert
License:        ASL 2.0
URL:            http://joel-costigliola.github.io/assertj/
Source0:        https://github.com/joel-costigliola/%{name}/archive/%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(cglib:cglib-nodep)
BuildRequires:  mvn(com.github.marschall:memoryfilesystem)
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
%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin org.sonatype.plugins:jarjar-maven-plugin

%pom_xpath_inject "pom:project" "
    <properties>
        <maven.compiler.target>1.7</maven.compiler.target>
        <maven.compiler.source>1.7</maven.compiler.source>
    </properties>"

# package org.mockito.internal.util.collections does not exist
rm -rf ./src/test/java/org/assertj/core/error/ShouldContainString_create_Test.java

%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md CONTRIBUTING.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc CONTRIBUTING.md
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_2jpp8
- new fc release

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_1jpp8
- added osgi provides

