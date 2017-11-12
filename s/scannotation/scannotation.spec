Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.3
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global alphatag r12

Name:          scannotation
Version:       1.0.3
Release:       alt2_0.15.r12jpp8
Summary:       A Java annotation scanner
License:       ASL 2.0
URL:           http://scannotation.sourceforge.net
# Also available here https://github.com/jharting/scannotation
# How we created tarball:
# svn export -r 12  https://scannotation.svn.sourceforge.net/svnroot/scannotation scannotation-1.0.3.Final
# tar -caJf scannotation-1.0.3.Final.tar.xz scannotation-1.0.3.Final
Source0:       %{name}-%{namedversion}.tar.xz
# Adding License file
Source1:       License.txt

BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: mvn(javassist:javassist)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(junit:junit)
Source44: import.info

%description
Scannotation is a Java library that creates an annotation database 
from a set of .class files.This database is really just a set of maps that index
what annotations are used and what classes are using them. Why do you need this? 
What if you are an annotation framework like an EJB 3.0 container and you want 
to automatically scan your classpath for EJB annotations so that you know what 
to deploy? Scannotation gives you apis that allow you to find archives in your 
classpath or WAR (web application) that you want to scan, then automatically 
scans them without loading each and every class within those archives

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_disable_module titan-test-jar
%pom_remove_dep :titan-cruise %{name}

# Force use servlet 3.1 apis
%pom_change_dep :servlet-api javax.servlet:javax.servlet-api:3.1.0 %{name}

cp -p %SOURCE1 .

%mvn_file org.%{name}:%{name} %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc License.txt

%files javadoc -f .mfiles-javadoc
%doc License.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_0.15.r12jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_0.14.r12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_0.13.r12jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_0.12.r12jpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_0.7.r12jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_0.6.r12jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_0.4.r12jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_0.4.r12jpp7
- new version

