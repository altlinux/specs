Group: Development/Other
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

Name:           maven-shared-incremental
Version:        1.1
Release:        alt1_23jpp11
Summary:        Maven Incremental Build support utilities
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-shared-incremental/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
%endif
Source44: import.info

%description
Various utility classes and plexus components for supporting
incremental build functionality in maven plugins.

%package javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -q
%pom_remove_dep :plexus-component-api

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1.1-alt1_23jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_18jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_16jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_13jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_12jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_11jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_10jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_9jpp8
- new version

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_2jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.2jpp
- rebuild to add provides

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

