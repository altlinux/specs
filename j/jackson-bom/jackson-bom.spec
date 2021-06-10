Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jackson-bom
Version:        2.11.4
Release:        alt1_2jpp11
Summary:        Bill of materials POM for Jackson projects
License:        ASL 2.0

URL:            https://github.com/FasterXML/jackson-bom
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson:jackson-parent:pom:) >= 2.11

BuildArch:      noarch
Source44: import.info

%description
A "bill of materials" POM for Jackson dependencies.

%prep
%setup -q -n %{name}-%{name}-%{version}

# Disable plugins not needed during RPM builds
%pom_remove_plugin ":maven-enforcer-plugin" base
%pom_remove_plugin ":nexus-staging-maven-plugin" base

# New EE coords
%pom_change_dep "javax.activation:javax.activation-api" "jakarta.activation:jakarta.activation-api" base

%build
%mvn_build -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 2.11.4-alt1_2jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.11.2-alt1_1jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 2.10.2-alt1_2jpp8
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 2.9.9-alt1_1jpp8
- new version

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.8-alt1_1jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_3jpp8
- fc29 update

* Wed May 16 2018 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_2jpp8
- java update

