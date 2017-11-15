Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          aesh
Version:       0.66.8
Release:       alt1_4jpp8
Summary:       Another Extendable SHell
License:       ASL 2.0
URL:           http://aeshell.github.io/
Source0:       https://github.com/aeshell/aesh/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.fusesource.jansi:jansi)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
A.sh is a Java library for handling console input with the goal to support most
GNU Readline features.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc	
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}
# Cleanup
rm -r *gradle*

%pom_xpath_set pom:addClasspath false
# This test @ random fails (koji only)
# ComparisonFailure: expected:<[]foo> but was:<[$<2>]foo>
rm src/test/java/org/jboss/aesh/parser/ParserTest.java

%build
# Disable test failure on ARM builder only
%mvn_build -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc README.asciidoc
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.66.8-alt1_4jpp8
- fc update

* Mon Oct 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.66.8-alt1_3jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.33.7-alt1_4jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.33.7-alt1_3jpp8
- java 8 mass update

