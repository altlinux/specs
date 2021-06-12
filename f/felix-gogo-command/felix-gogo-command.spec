Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global bundle  org.apache.felix.gogo.command

%bcond_without tests

Name:           felix-gogo-command
Version:        1.1.2
Release:        alt1_1jpp11
Summary:        Apache Felix Gogo command line shell for OSGi
License:        ASL 2.0
URL:            https://felix.apache.org/documentation/subprojects/apache-felix-gogo.html
BuildArch:      noarch

Source0:        http://archive.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:gogo-parent:pom:) >= 5
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.gogo.runtime)
BuildRequires:  mvn(org.osgi:osgi.annotation)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
%if %{with tests}
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.mockito:mockito-core)
%endif
Source44: import.info

%description
Apache Felix Gogo is a subproject of Apache Felix implementing a command
line shell for OSGi. It is used in many OSGi runtimes and servers.

This package implements a set of basic commands.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%mvn_file : felix/%{bundle}

# Use compendium dep
%pom_remove_dep :org.osgi.service.log
%pom_xpath_inject "pom:dependencies" "
<dependency>
<groupId>org.osgi</groupId>
<artifactId>osgi.cmpn</artifactId>
</dependency>"

%build
%if %{with tests}
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8
%else
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8
%endif

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.1.2-alt1_1jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.0.2-alt1_12jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_9jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_7jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_4jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_4jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_3jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.14.0-alt1_5jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt2_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt1_4jpp7
- new release

