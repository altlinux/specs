Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# Conditionals to help breaking org.apache.felix.scr.generator <-> org.apache.felix.scr.annotations dependency cycle
%if 0%{?fedora}
#def_with annotations
%bcond_with annotations
%endif

%global project   felix
%global bundle    org.apache.felix.scr.generator

Name:          felix-scr-generator
Version:       1.13.0
Release:       alt1_3jpp8
Summary:       Descriptor Generator Implementation
License:       ASL 2.0
URL:           http://felix.apache.org/
Source0:       http://www.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:felix-parent:pom:)
%if %{without annotations}
BuildRequires: mvn(org.apache.felix:org.apache.felix.scr.annotations)
%endif
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-site-plugin)
BuildRequires: mvn(org.easymock:easymock)
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(org.osgi:org.osgi.compendium)
BuildRequires: mvn(org.osgi:org.osgi.core)
BuildRequires: mvn(org.ow2.asm:asm-all)

BuildArch:     noarch
Source44: import.info

%description
Provides the implementation to generate Declarative Services and Metatype
Service descriptors from Java 5 Annotations and/or JavaDoc tags.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%mvn_file :%{bundle} %{project}/%{bundle}

%build

%mvn_build \
%if %{with annotations}
# tests skipped for circular dependency with org.apache.felix.scr.annotations
 -f \
%endif
 -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc changelog.txt
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.13.0-alt1_3jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.13.0-alt1_2jpp8
- java 8 mass update

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt1_1jpp7
- new release

