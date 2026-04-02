Name:           maven-common-artifact-filters
Version:        3.4.0
Release:        alt1.1

Summary:        Apache Maven Common Artifact Filters
License:        Apache-2.0
Group:          Development/Java
URL:            https://maven.apache.org/shared/maven-common-artifact-filters/
VCS:            https://github.com/apache/maven-common-artifact-filters

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.openjdk.jmh:jmh-core)
BuildRequires:  mvn(org.openjdk.jmh:jmh-generator-annprocess)

BuildArch:      noarch

%description
A collection of ready-made filters to control inclusion/exclusion of artifacts
during dependency resolution.

%javadoc_package

%prep
%setup

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 3.4.0-alt1.1
- Cosmetic fixes.

* Tue Feb 24 2026 Evgeniy Serov <scala@altlinux.org> 3.4.0-alt1
- Updated to 3.4.0.

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 3.2.0-alt1_3jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 3.1.1-alt1_3jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 3.1.1-alt1_1jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 3.1.0-alt1_3jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_8jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_6jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_2jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_2jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt5_16jpp8
- new version

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_11jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_7jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_3jpp7
- rebuild with maven-local

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_3jpp7
- fixed maven1 dependency

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_3jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_2jpp7
- new version

