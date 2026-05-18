Name:             jboss-marshalling
Version:          2.3.0
Release:          alt1

Summary:          JBoss Marshalling
License:          Apache-2.0
Group:            Development/Java
URL:              http://jbossmarshalling.jboss.org/
VCS:              https://github.com/jboss-remoting/jboss-marshalling

Source0:          %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildRequires:  mvn(org.jboss.modules:jboss-modules)
BuildRequires:  mvn(org.testng:testng)

BuildArch:      noarch

%description
JBoss Marshalling is an alternative serialization API used by WildFly project
addressing many problems of JDK serialization API while remaining fully
compatible with "java.io.Serializable".

%javadoc_package

%prep
%setup

%pom_disable_module tests

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt *.md

%changelog
* Tue Apr 07 2026 Evgeniy Serov <scala@altlinux.org> 2.3.0-alt1
- Updated to 2.3.0.
- Returned to Sisyphus.

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 1.4.11-alt1_8jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.11-alt1_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.11-alt1_5jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.4.11-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.11-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.11-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.11-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.6-alt1_4jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.6-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.13-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.13-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.13-alt1_3jpp7
- new version

