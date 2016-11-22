Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          jgoodies-animation
Version:       1.4.3
Release:       alt1_3jpp8
Summary:       Framework for time-based real-time animations in Java
License:       BSD
#Alt. URL:     http://java.net/projects/animation
URL:           http://www.jgoodies.com/freeware/animation/index.html

Source0:       http://www.jgoodies.com/download/libraries/animation/%{name}-%(tr "." "_" <<<%{version}).zip

BuildArch:     noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.jgoodies:jgoodies-common)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Source44: import.info


%description
The JGoodies Animation framework enables you to produce time-based real-time
animations in Java. It uses concepts and notions as described by the W3C
specification for the Synchronized Multimedia Integration Language (SMIL).

This animation framework has been designed for a seemless, flexible
and powerful integration with Java, ease-of-use and a small library size.
Unlike SMIL we use Java to describe the animations a.. not XML.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

mkdir -p src/main/java
(cd src/main/java && jar xf ../../../%{name}-%{version}-sources.jar)
mkdir -p src/test/java
(cd src/test/java && jar xf ../../../%{name}-%{version}-tests.jar)
find -name "*.jar" -delete

sed -i 's|\r||g' LICENSE.txt RELEASE-NOTES.txt

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt README.html RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_3jpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_2jpp7
- initial build

