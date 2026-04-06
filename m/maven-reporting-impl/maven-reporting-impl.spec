Name:           maven-reporting-impl
Version:        4.0.0
Release:        alt1

Summary:        Apache Maven Reporting Implementation
License:        Apache-2.0
Group:          Development/Java
URL:            https://maven.apache.org/shared/maven-reporting-impl/
VCS:            https://github.com/apache/maven-reporting-impl

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-model)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-apt)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-xdoc)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)

BuildArch:      noarch

%description
Abstract classes to manage report generation, which can be run both:

* as part of a site generation (as a maven-reporting-api's MavenReport),
* or as a direct standalone invocation (as a maven-plugin-api's Mojo).

This is a replacement package for maven-shared-reporting-impl

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-invoker-plugin
%pom_add_dep org.apiguardian:apiguardian-api:1.1.2:test

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Fri Mar 20 2026 Evgeniy Serov <scala@altlinux.org> 4.0.0-alt1
- Udated to 4.0.0.

* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 3.0.0-alt1_7jpp11
- java11 build

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_7jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_5jpp8
- new version

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_1jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_3jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_2jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_2jpp8
- unbootsrap build

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_5jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_0jpp7
- new version

