Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jsr-305
Version:        0
Release:        alt4_0.22.20130910svnjpp8
Summary:        Correctness annotations for Java code

# The majority of code is BSD-licensed, but some Java sources
# are licensed under CC-BY license, see: $ grep -r Creative .
License:        BSD and CC-BY
URL:            http://jsr-305.googlecode.com/
BuildArch:      noarch

# There has been no official release yet.  This is a snapshot of the Subversion
# repository as of 10 Sep 2013.  Use the following commands to generate the
# tarball:
#   svn export -r 51 http://jsr-305.googlecode.com/svn/trunk jsr-305
#   tar -czvf jsr-305-20130910svn.tgz jsr-305
Source0:        jsr-305-20130910svn.tgz
# File containing URL to CC-BY license text
Source1:        NOTICE-CC-BY.txt

BuildRequires:  maven-local
Source44: import.info

%package javadoc
Group: Development/Java
Summary:        Javadoc documentation for %{name}
BuildArch: noarch

%description
This package contains reference implementations, test cases, and other
documents for Java Specification Request 305: Annotations for Software Defect
Detection.

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}
cp %{SOURCE1} NOTICE-CC-BY

%mvn_file :ri %{name}
%mvn_alias :ri com.google.code.findbugs:jsr305
%mvn_package ":{proposedAnnotations,tcl}" __noinstall

# do not build sampleUses module - it causes Javadoc generation to fail
%pom_disable_module sampleUses

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc ri/LICENSE NOTICE-CC-BY sampleUses

%files javadoc -f .mfiles-javadoc
%doc ri/LICENSE NOTICE-CC-BY

%changelog
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

