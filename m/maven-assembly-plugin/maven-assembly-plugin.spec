Name:           maven-assembly-plugin
Version:        3.7.1
Release:        alt1.1

Summary:        Maven Assembly Plugin
License:        Apache-2.0
Group:          Development/Java
URL:            https://maven.apache.org/plugins/maven-assembly-plugin/
VCS:            https://github.com/apache/maven-assembly-plugin

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.jdom:jdom2)
BuildRequires:  mvn(jaxen:jaxen)

BuildArch:      noarch

%description
A Maven plugin to create archives of your project's sources, classes,
dependencies etc. from flexible assembly descriptors.

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
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 3.7.1-alt1.1
- Cosmetic fixes.

* Wed Feb 18 2026 Evgeniy Serov <scala@altlinux.org> 3.7.1-alt1
- Updated to 3.7.1.

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 3.3.0-alt1_6jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 3.3.0-alt1_3jpp11
- new version

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 3.2.0-alt1_2jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_1jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_5jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_3jpp8
- java update

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_1jpp8
- new version

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_8jpp8
- new fc release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_6jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.5-alt1_3jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_7jpp7
- new release

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_5jpp7
- added BR: for xmvn

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_5jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.3-alt2_2jpp7
- fixed build

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_2jpp7
- new release

* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt2_4jpp7
- maven2 compatibility: added
  maven-assembly-plugin-2.2.2-alt-allow-empty-assembly-id.patch

* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt1_4jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

