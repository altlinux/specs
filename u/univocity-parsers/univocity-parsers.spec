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

Name:           univocity-parsers
Version:        2.9.1
Release:        alt1_3jpp11
Summary:        Collection of parsers for Java
License:        ASL 2.0
URL:            https://github.com/uniVocity/univocity-parsers
BuildArch:      noarch

Source0:        https://github.com/uniVocity/univocity-parsers/archive/v%{version}.tar.gz

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
%endif
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
# Tests require univocity-output-tester, which is not packaged yet.
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE-2.0.html

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE-2.0.html

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 2.9.1-alt1_3jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 2.9.1-alt1_1jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.9.0-alt1_1jpp11
- new version

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 2.8.3-alt1_2jpp11
- new version

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 2.5.5-alt1_5jpp8
- fc update & java 8 build

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 2.5.5-alt1_2jpp8
- new version

