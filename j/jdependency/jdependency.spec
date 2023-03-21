Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jdependency
Version:        2.8.0
Release:        alt1_1jpp11
Summary:        This project provides an API to analyse class dependencies
License:        ASL 2.0
URL:            http://github.com/tcurdt/%{name}
BuildArch:      noarch

Source0:        http://github.com/tcurdt/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-analysis)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.ow2.asm:asm-tree)
BuildRequires:  mvn(org.ow2.asm:asm-util)
Source44: import.info

%description
%{name} is small library that helps you analyze class level
dependencies, clashes and missing classes.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%mvn_file : %{name}
# work-around for: https://bugzilla.redhat.com/show_bug.cgi?id=1981486
#%%pom_add_dep org.apache.commons:commons-lang3:3.12.0:test

# remove maven-compiler-plugin configuration that is broken with Java 11
#%%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

# remove a test case that is harmlessly broken on Java 11
#rm src/test/java/org/vafer/jdependency/DependencyUtilsTestCase.java

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:2.8.0-alt1_1jpp11
- new version

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:2.7.0-alt1_3jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:1.2-alt1_12jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:1.2-alt1_9jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_6jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_3jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_2jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_1jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt1_4jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt1_3jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_6jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_4jpp7
- new fc release

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_1jpp7
- fc version

* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt1_5jpp6
- new version

