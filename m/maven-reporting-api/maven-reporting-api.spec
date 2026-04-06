Name:           maven-reporting-api
Epoch:          1
Version:        4.0.0
Release:        alt1

Summary:        Apache Maven Reporting API
License:        Apache-2.0
Group:          Development/Java
URL:            http://maven.apache.org/shared/maven-reporting-api
VCS:            https://github.com/apache/maven-reporting-api

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)

BuildArch:      noarch

%description
API to manage report generation.

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
* Fri Mar 20 2026 Evgeniy Serov <scala@altlinux.org> 1:4.0.0-alt1
- Updated to 4.0.0.

* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 1:3.0-alt3_18jpp11
- java11 build

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1:3.0-alt3_18jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.0-alt3_16jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.0-alt3_13jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.0-alt3_11jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.0-alt3_10jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.0-alt3_9jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.0-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.0-alt1_3jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.0-alt1_0jpp7
- new version

