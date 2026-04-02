Name:           easymock
Version:        5.6.0
Release:        alt1.1

Summary:        Easy mock objects
License:        Apache-2.0
Group:          Development/Java
URL:            http://www.easymock.org
VCS:            https://github.com/easymock/easymock

Source0:        %name-%version.tar

Patch1:         0001-Disable-android-support.patch
Patch2:         0002-Migrate-from-deprecated-Hamcrest-is-to-isA.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.apache:apache-jar-resource-bundle)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.testng:testng)
BuildRequires:  mvn(junit:junit)

BuildArch:      noarch

%description
EasyMock provides Mock Objects for interfaces in JUnit tests by generating
them on the fly using Java's proxy mechanism. Due to EasyMock's unique style
of recording expectations, most refactorings will not affect the Mock Objects.
So EasyMock is a perfect fit for Test-Driven Development.

%javadoc_package

%prep
%setup
%autopatch -p1

%pom_xpath_remove pom:extensions

%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin :license-maven-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_dep -r :dexmaker core

rm core/src/main/java/org/easymock/internal/Android*.java
rm core/src/test/java/org/easymock/tests2/ClassExtensionHelperTest.java
%pom_disable_module test-android

%pom_disable_module test-integration
%pom_disable_module test-osgi

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc *.md 
%doc core/LICENSE.txt

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 5.6.0-alt1.1
- Cosmetic fixes.

* Sat Dec 27 2025 Evgeniy Serov <scala@altlinux.org> 5.6.0-alt1
- fixed FTBFS
- new version 5.6.0
- removed deprecated patches
- added a new patch migrating from Hamcrest is to isA matcher
- removed import.info

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:4.2-alt1_7jpp11
- update

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:4.2-alt1_4jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:4.2-alt1_1jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.6-alt1_5jpp8
- fc update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.6-alt1_3jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.5-alt1_2jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.5-alt1_1jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt1_4jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt1_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt1_3jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_20jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_18jpp7
- fc update

* Sat Jan 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_8jpp6
- jpp 6 release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_3jpp5
- new jpackage release

* Wed May 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

