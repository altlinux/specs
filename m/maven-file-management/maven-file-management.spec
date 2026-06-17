Name:           maven-file-management
Epoch:          1
Version:        3.2.0
Release:        alt1

Summary:        Apache Maven File Management API
License:        Apache-2.0
Group:          Development/Java
URL:            https://maven.apache.org/shared/file-management/
VCS:            https://github.com/apache/maven-file-management

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)

BuildArch:      noarch

%description
Provides a component for plugins to easily resolve project dependencies.

%javadoc_package

%prep
%setup

%pom_add_dep org.apiguardian:apiguardian-api:1.1.2:test

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Tue Jun 16 2026 Evgeniy Serov <scala@altlinux.org> 1:3.2.0-alt1
- Updated to 3.2.0.

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1:3.0.0-alt1_17jpp11
- update

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1:3.0.0-alt1_14jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1:3.0.0-alt1_9jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.0.0-alt1_7jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.0.0-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.0.0-alt1_3jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.0.0-alt1_2jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt3_12jpp8
- new version

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt1_6jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt1_0jpp7
- new release

