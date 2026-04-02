Name:           plexus-languages
Version:        1.5.2
Release:        alt1.1

Summary:        Plexus Languages
License:        Apache-2.0
Group:          Development/Java
URL:            https://codehaus-plexus.github.io/plexus-languages/
VCS:            https://github.com/codehaus-plexus/plexus-languages

Source:         %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
# TODO: switch to mvn() prov, after fixing mockito bug
BuildRequires:  osgi(org.mockito.junit-jupiter)

BuildArch:      noarch

%description
Plexus Languages is a set of Plexus components that maintain shared
language features.

%javadoc_package

%prep
%setup

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc *.md

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 1.5.2-alt1.1
- Cosmetic fixes.

* Wed Feb 18 2026 Evgeniy Serov <scala@altlinux.org> 1.5.2-alt1
- Updated to 1.5.2.

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1.1.1-alt1_2jpp11
- new version

* Thu May 26 2022 Igor Vlasenko <viy@altlinux.org> 1.0.6-alt1_6jpp11
- fc update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.0.6-alt1_1jpp11
- new version

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 1.0.5-alt1_6jpp11
- new version

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 1.0.3-alt1_2jpp11
- new version

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_5jpp8
- fc update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_4jpp8
- new version

* Tue Jun 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt2_4jpp8
- fixed build with new objectweb-asm

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_4jpp8
- fc 28 update

