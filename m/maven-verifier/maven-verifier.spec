Name:           maven-verifier
Version:        2.0.0
Release:        alt0.m1

Summary:        Apache Maven Verifier
License:        Apache-2.0
Group:          Development/Java
URL:            https://maven.apache.org/shared/maven-verifier
VCS:            https://github.com/apache/maven-verifier

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)

BuildArch:  noarch

%description
Provides a test harness for Maven integration tests.

%javadoc_package

%prep
%setup

# requires internet connection
rm src/test/java/org/apache/maven/shared/verifier/Embedded3xLauncherTest.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Sun Apr 05 2026 Evgeniy Serov <scala@altlinux.org> 2.0.0-alt0.m1
- Updated to 2.0.0-M1.

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1.7.2-alt1_6jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.7.2-alt1_3jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_10jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_8jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_5jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_2jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_1jpp8
- new version

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_5jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

