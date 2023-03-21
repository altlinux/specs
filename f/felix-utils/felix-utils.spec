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

%global bundle org.apache.felix.utils

Name:           felix-utils
Version:        1.11.8
Release:        alt1_2jpp11
Summary:        Utility classes for OSGi
License:        ASL 2.0
URL:            https://felix.apache.org
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/felix/%{bundle}/%{version}/%{bundle}-%{version}-source-release.tar.gz

# The module org.osgi.cmpn requires implementing methods which were not
# implemented in previous versions where org.osgi.compendium was used
Patch0:         0000-Port-to-osgi-cmpn.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
%endif
Source44: import.info

%description
Utility classes for OSGi

%package javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}
%patch0 -p1

%pom_remove_parent
%pom_xpath_inject pom:project "<groupId>org.apache.felix</groupId>"
%pom_remove_plugin :apache-rat-plugin

%mvn_file :%{bundle} "felix/%{bundle}"

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE
%doc DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1.11.8-alt1_2jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1.11.6-alt1_3jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.11.6-alt1_1jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.11.4-alt1_3jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.11.2-alt1_1jpp8
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.10.4-alt1_4jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.10.4-alt1_3jpp8
- fc29 update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.10.4-alt1_2jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt1_1jpp8
- new version

* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_2jpp8
- new version

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.6-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt1_3jpp8
- new fc release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt1_2jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_3jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_5jpp7
- new release

