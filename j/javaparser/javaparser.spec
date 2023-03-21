Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          javaparser
Version:       3.24.2
Release:       alt1_3jpp11
Summary:       Java 1 to 13 Parser and Abstract Syntax Tree for Java
License:       LGPLv3+ or ASL 2.0
URL:           http://javaparser.org
Source0:       https://github.com/javaparser/javaparser/archive/%{name}-parent-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires:  mvn(net.java.dev.javacc:javacc)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(junit:junit)

BuildArch:     noarch
Source44: import.info

%description
This package contains a Java 1 to 13 Parser with AST generation and
visitor support. The AST records the source code structure, javadoc
and comments. It is also possible to change the AST nodes or create new
ones to modify the source code.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-parent-%{version}

sed -i 's/\r//' readme.md

# Remove plugins unnecessary for RPM builds
%pom_remove_plugin -r :jacoco-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :coveralls-maven-plugin

# Compatibility alias
%mvn_alias :javaparser-core com.google.code.javaparser:javaparser

# Fix javacc plugin name
sed -i \
  -e 's/ph-javacc-maven-plugin/javacc-maven-plugin/' \
  -e 's/com.helger.maven/org.codehaus.mojo/' \
  javaparser-core/pom.xml

# This plugin is not in Fedora, so use maven-resources-plugin to accomplish the same thing
%pom_remove_plugin :templating-maven-plugin javaparser-core
%pom_xpath_inject "pom:build" "
<resources>
  <resource>
    <directory>src/main/java-templates</directory>
    <filtering>true</filtering>
    <targetPath>\${basedir}/src/main/java</targetPath>
  </resource>
</resources>" javaparser-core

# Missing dep on jbehave for testing
%pom_disable_module javaparser-core-testing
%pom_disable_module javaparser-core-testing-bdd

# Don't build the symbol solver
%pom_disable_module javaparser-symbol-solver-core
#%pom_disable_module javaparser-symbol-solver-logic
#%pom_disable_module javaparser-symbol-solver-model
%pom_disable_module javaparser-symbol-solver-testing

# Only need to ship the core module
%pom_disable_module javaparser-core-generators
%pom_disable_module javaparser-core-metamodel-generator
%pom_disable_module javaparser-core-serialization

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc readme.md changelog.md
%doc --no-dereference LICENSE LICENSE.APACHE LICENSE.GPL LICENSE.LGPL

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE LICENSE.APACHE LICENSE.GPL LICENSE.LGPL

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 3.24.2-alt1_3jpp11
- new version

* Sat Jul 09 2022 Igor Vlasenko <viy@altlinux.org> 3.22.0-alt1_3jpp11
- new version

* Sat May 28 2022 Igor Vlasenko <viy@altlinux.org> 3.14.16-alt1_4jpp11
- aqute-bnd5 support

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 3.14.16-alt1_1jpp11
- new version

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 3.3.5-alt1_3jpp8
- fc update

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 3.3.5-alt1_1jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.11-alt1_6jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.11-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.11-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.11-alt1_3jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.11-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_1jpp7
- new version

