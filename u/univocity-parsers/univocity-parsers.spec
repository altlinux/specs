Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           univocity-parsers
Version:        2.8.3
Release:        alt1_2jpp11
Summary:        Collection of parsers for Java
License:        ASL 2.0

URL:            https://github.com/uniVocity/univocity-parsers
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.univocity:univocity-output-tester)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.hsqldb:hsqldb)
BuildRequires:  mvn(org.testng:testng)
Source44: import.info

%description
uniVocity-parsers is a suite of extremely fast and reliable parsers
for Java.  It provides a consistent interface for handling different
file formats, and a solid framework for the development of new
parsers.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -- -Dmaven.compile.source=1.8 -Dmaven.compile.target=1.8 -Dmaven.javadoc.source=1.8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE-2.0.html

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE-2.0.html

%changelog
* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 2.8.3-alt1_2jpp11
- new version

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 2.5.5-alt1_5jpp8
- fc update & java 8 build

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 2.5.5-alt1_2jpp8
- new version

