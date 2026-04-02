Name:           maven-archiver
Version:        3.6.2
Release:        alt1.1

Summary:        Apache Maven Archiver
License:        Apache-2.0
Group:          Development/Java
URL:            http://maven.apache.org/shared/maven-archiver/
VCS:            https://github.com/apache/maven-archiver

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.mockito:mockito-core)

BuildArch:      noarch

%description
The Maven Archiver is used by other Maven plugins
to handle packaging.

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
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 3.6.2-alt1.1
- Cosmetic fixes.

* Tue Feb 24 2026 Evgeniy Serov <scala@altlinux.org> 3.6.2-alt1
- Updated to 3.6.2.

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:3.5.2-alt1_2jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:3.5.1-alt1_3jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:3.5.1-alt1_1jpp11
- new version

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 0:3.5.0-alt1_2jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.4.0-alt1_1jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_4jpp8
- new version

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_1jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.1.1-alt1_3jpp8
- fc27 update

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.1.1-alt1_2jpp8
- new version

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.0-alt1_2jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt2_8jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt2_7jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt2_3jpp7
- rebuild with maven-local

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_3jpp7
- new fc release

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_2jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

