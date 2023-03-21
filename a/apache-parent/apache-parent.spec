Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
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

Name:           apache-parent
Version:        26
Release:        alt1_3jpp11
Summary:        Parent POM file for Apache projects
License:        ASL 2.0
URL:            http://apache.org/
Source0:        https://repo1.maven.org/maven2/org/apache/apache/%{version}/apache-%{version}-source-release.zip
BuildArch:      noarch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
%endif

# Not generated automatically
%if %{without bootstrap}
BuildRequires:  mvn(org.apache:apache-jar-resource-bundle)
%endif
Requires:       mvn(org.apache:apache-jar-resource-bundle)
Source44: import.info

%description
This package contains the parent pom file for apache projects.

%prep
%setup -q -n apache-%{version}

%pom_remove_plugin :maven-site-plugin

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 26-alt1_3jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 23-alt1_6jpp11
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 23-alt1_3jpp8
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 19-alt1_4jpp8
- new version

* Fri May 18 2018 Igor Vlasenko <viy@altlinux.ru> 19-alt1_2jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 18-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 18-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 18-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 17-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 17-alt1_2jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 17-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 10-alt2_13jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 10-alt2_10jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 10-alt2_7jpp7
- rebuild with new apache-resource-bundles

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 10-alt1_7jpp7
- fc update

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 10-alt1_5jpp7
- new release

