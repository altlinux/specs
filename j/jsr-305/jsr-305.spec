Epoch: 1
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           jsr-305
Version:        3.0.2
Release:        alt1_3jpp11
Summary:        Correctness annotations for Java code

# The majority of code is BSD-licensed, but some Java sources
# are licensed under CC-BY license, see: $ grep -r Creative .
License:        BSD and CC-BY
URL:            https://code.google.com/p/jsr-305
BuildArch:      noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
# File containing URL to CC-BY license text
Source1:        NOTICE-CC-BY.txt

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%endif
Source44: import.info

%description
This package contains reference implementations, test cases, and other
documents for Java Specification Request 305: Annotations for Software Defect
Detection.

%{?javadoc_package}

%prep
%setup -q
cp %{SOURCE1} NOTICE-CC-BY

%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/*" 1.6

sed -i 's|<groupId>com\.google\.code\.findbugs</groupId>|<groupId>org.jsr-305</groupId>|' ri/pom.xml
sed -i 's|<artifactId>jsr305</artifactId>|<artifactId>ri</artifactId>|' ri/pom.xml

%mvn_file :ri %{name}
%mvn_alias :ri com.google.code.findbugs:jsr305
%mvn_package ":{proposedAnnotations,tcl}" __noinstall

# do not build sampleUses module - it causes Javadoc generation to fail
%pom_disable_module sampleUses

%pom_remove_parent ri
%pom_add_parent org.jsr-305:jsr-305:0.1-SNAPSHOT ri

%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin ri
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin ri
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin ri
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin ri

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference ri/LICENSE NOTICE-CC-BY
%doc sampleUses

%changelog
* Wed Aug 18 2021 Igor Vlasenko <viy@altlinux.org> 1:3.0.2-alt1_3jpp11
- new version

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 1:0-alt4_0.30.20130910svnjpp11
- new version

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1:0-alt4_0.27.20130910svnjpp11
- update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1:0-alt4_0.24.20130910svnjpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1:0-alt4_0.22.20130910svnjpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:0-alt4_0.21.20130910svnjpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:0-alt4_0.20.20130910svnjpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:0-alt4_0.19.20130910svnjpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1:0-alt4_0.18.20130910svnjpp8
- new version

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 1:0-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:0-alt2_0.16.20130910svnjpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:0-alt2_0.13.20090319svnjpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:0-alt2_0.10.20090319svnjpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1:0-alt1_0.10.20090319svnjpp7
- new version

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_3jpp6
- jpp 6 release

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_2jpp5
- new jpp release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_1jpp5
- converted from JPackage by jppimport script

