Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             stax2-api
Version:          4.2.1
Release:          alt1_4jpp11
Summary:          Experimental API extending basic StAX implementation
License:          BSD

URL:              https://github.com/FasterXML/stax2-api
Source0:          %{url}/archive/%{name}-%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(com.fasterxml:oss-parent:pom:)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
Source44: import.info

%description
StAX2 is an experimental API that is intended to extend
basic StAX specifications in a way that allows implementations
to experiment with features before they end up in the actual
StAX specification (if they do). As such, it is intended
to be freely implementable by all StAX implementations same way
as StAX, but without going through a formal JCP process.

%package          javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description      javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}


%pom_xpath_remove pom:Import-Package

# javadoc generation fails due to strict doclint in JDK 8
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :moditect-maven-plugin

%build
%mvn_file :%{name} %{name}
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 4.2.1-alt1_4jpp11
- new version

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 4.2-alt1_2jpp11
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1_6jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt1_4jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_4jpp7
- new version

