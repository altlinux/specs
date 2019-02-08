Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 28
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Conditionals to help breaking org.apache.felix.scr.generator <-> org.apache.felix.scr.annotations dependency cycle
%if 0%{?fedora}
%bcond_with annotations
%endif

%global bundle    org.apache.felix.scr.generator

Name:          felix-scr-generator
Version:       1.18.0
Release:       alt1_2jpp8
Summary:       Descriptor Generator Implementation
License:       ASL 2.0
URL:           http://felix.apache.org/documentation/subprojects/apache-felix-service-component-runtime.html
Source0:       http://archive.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
%if %{without annotations}
BuildRequires:  mvn(org.apache.felix:org.apache.felix.scr.annotations)
%endif
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.ow2.asm:asm-all)
Source44: import.info

%description
Provides the implementation to generate Declarative Services and Metatype
Service descriptors from Java 5 Annotations and/or JavaDoc tags.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%mvn_file : felix/%{bundle}

%pom_change_dep org.osgi:org.osgi.core org.osgi:osgi.core
%pom_change_dep org.osgi:org.osgi.compendium org.osgi:osgi.cmpn

%build
# tests skipped for circular dependency with org.apache.felix.scr.annotations
%mvn_build \
%if %{with annotations}
 -f \
%endif
 -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc changelog.txt
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.18.0-alt1_2jpp8
- fc29 update

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 1.18.0-alt1_1jpp8
- java update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.16.0-alt1_3jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.16.0-alt1_2jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.16.0-alt1_1jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.13.0-alt1_3jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.13.0-alt1_2jpp8
- java 8 mass update

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt1_1jpp7
- new release

