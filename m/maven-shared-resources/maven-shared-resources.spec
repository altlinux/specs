Name:          maven-shared-resources
Version:       6
Release:       alt1

Summary:       Apache Maven Shared Resources
License:       Apache-2.0
Group:         Development/Java
URL:           http://maven.apache.org/shared/maven-shared-resources/
VCS:           https://github.com/apache/maven-shared-resources

Source0:       %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires: mvn(org.apache.maven.shared:maven-shared-components:pom:)

BuildArch:     noarch

%description
This is a collection of templates that are specific to the Maven project.
They are probably not of interest to projects other than Apache Maven.

%prep
%setup

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Fri Mar 20 2026 Evgeniy Serov <scala@altlinux.org> 6-alt1
- Updated to 6.

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 2-alt1_8jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 2-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2-alt1_3jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 2-alt1_2jpp8
- new version

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1-alt1_1jpp7
- update

* Sun Aug 24 2014 Igor Vlasenko <viy@altlinux.ru> 1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

