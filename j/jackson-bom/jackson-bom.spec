Name:           jackson-bom
Version:        2.22.1
Release:        alt1

Summary:        Bill of materials POM for Jackson projects
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/FasterXML/jackson-bom
VCS:            https://github.com/FasterXML/jackson-bom

Source0:        %name-%version.tar

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(com.fasterxml.jackson:jackson-parent:pom:)

BuildArch:      noarch

%description
A "bill of materials" POM for Jackson dependencies.

%prep
%setup

%pom_remove_plugin :maven-enforcer-plugin base
%pom_remove_plugin :central-publishing-maven-plugin base

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc *.md LICENSE

%changelog
* Fri Aug 07 2026 Evgeniy Serov <scala@altlinux.org> 2.22.1-alt1
- Updated to 2.22.1.

* Thu Apr 02 2026 Anton Meleshnikov <alton@altlinux.org> 2.20.1-alt1
- new version

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

