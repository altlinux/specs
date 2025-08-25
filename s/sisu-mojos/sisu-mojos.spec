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

Name:           sisu-mojos
Version:        0.9.0.M2
Release:        alt1
Summary:        Sisu plugin for Apache Maven
License:        EPL-1.0
URL:            https://www.eclipse.org/sisu
BuildArch:      noarch

Source0:        https://github.com/eclipse/sisu.mojos/archive/refs/tags/releases/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         sisu-mojos-remove-enforceBytecodeVersion.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
#BuildRequires:  mvn(org.codehaus.mojo:extra-enforcer-rules)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.slf4j:slf4j-nop)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
%endif

%description
The Sisu Plugin for Maven provides mojos to generate
META-INF/sisu/javax.inject.Named index files for the Sisu container.

%javadoc_package

%prep
%setup -n sisu.mojos-releases-%{version}
%patch0 -p2

%mvn_alias : org.sonatype.plugins:
%pom_remove_dep :extra-enforcer-rules

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Sun Aug 24 2025 Andrey Cherepanov <cas@altlinux.org> 0.9.0.M2-alt1
- new version

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0.3.5-alt1_2jpp11
- new version

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0.3.4-alt1_11jpp11
- update

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0.3.4-alt1_8jpp11
- update

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 0.3.4-alt1_3jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt1_2jpp8
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_9jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_5jpp8
- fc27 update

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_2jpp8
- new version

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

