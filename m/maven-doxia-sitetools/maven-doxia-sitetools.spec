Name:           maven-doxia-sitetools
Version:        2.0.0
Release:        alt1

Summary:        Apache Maven Doxia Sitetools
License:        Apache-2.0
Group:          Development/Java
URL:            https://maven.apache.org/doxia/doxia-sitetools/

Source0:        %name-%version.tar

Patch0:         0001-remove-dependency-velocity-tools.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-i18n)
BuildRequires:  mvn(org.codehaus.plexus:plexus-testing)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-apt)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-xdoc)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-xhtml5)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-fml)
BuildRequires:  mvn(org.codehaus.plexus:plexus-velocity)

BuildRequires:  mvn(org.mockito:mockito-core)

BuildArch:      noarch

%description
Doxia is a content generation framework which aims to provide its
users with powerful techniques for generating static and dynamic
content. Doxia can be used to generate static sites in addition to
being incorporated into dynamic content generation systems like blogs,
wikis and content management systems.

%javadoc_package

%prep
%setup
%autopatch -p1

%pom_add_dep org.apiguardian:apiguardian-api:1.1.2:test
%pom_add_dep org.codehaus.plexus:plexus-utils doxia-skin-model

%pom_remove_dep org.htmlunit:htmlunit doxia-site-renderer
%pom_remove_dep org.apache.velocity.tools:velocity-tools-generic doxia-site-renderer

# requires internet connection
rm doxia-integration-tools/src/test/java/org/apache/maven/doxia/tools/SiteToolTest.java

%build
# tests are disabled cause missing htmlunit
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Mon Apr 06 2026 Evgeniy Serov <scala@altlinux.org> 2.0.0-alt1
- Updated to 2.0.0.

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:1.11.1-alt1_3jpp11
- new version

* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 0:1.9.2-alt1_7jpp11
- java11 build

* Thu Jun 03 2021 Igor Vlasenko <viy@altlinux.org> 0:1.9.2-alt1_3jpp8
- new version, use jvm8

* Fri May 14 2021 Igor Vlasenko <viy@altlinux.org> 0:1.9.1-alt1_3jpp8
- non-bootstrap build

* Thu May 13 2021 Igor Vlasenko <viy@altlinux.org> 0:1.9.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.7.5-alt1_4jpp8
- new version

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7.5-alt1_1jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7.4-alt1_4jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7.4-alt1_3jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_3jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_2jpp8
- java 8 mass update

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_5jpp7
- rebuild with maven-local

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_5jpp7
- fixed maven1 dependency

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_5jpp7
- fc update

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp7
- new release

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

