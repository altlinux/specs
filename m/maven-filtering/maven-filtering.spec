Name:           maven-filtering
Version:        3.4.0
Release:        alt1.1

Summary:        Apache Maven Filtering
License:        Apache-2.0
Group:          Development/Java
URL:            https://maven.apache.org/shared/maven-filtering/
VCS:            https://github.com/apache/maven-filtering

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.codehaus.plexus:plexus-testing)

BuildArch:      noarch

%description
These Plexus components have been built from the filtering process/code in
Maven Resources Plugin. The goal is to provide a shared component for all
plugins that needs to filter resources.

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

* Wed Feb 18 2026 Evgeniy Serov <scala@altlinux.org> 3.4.0-alt1
- Updated to 3.4.0.

* Fri Jun 10 2022 Igor Vlasenko <viy@altlinux.org> 3.2.0-alt1_3jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 3.2.0-alt1_1jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_9jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_7jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_3jpp8
- new jpp release

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_2jpp8
- new version

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_2jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_2jpp8
- new version

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_1jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_9jpp7
- rebuild with maven-local

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_9jpp7
- new release

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_8jpp7
- full build

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

