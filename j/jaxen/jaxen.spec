Name:           jaxen
Version:        2.0.5
Release:        alt1

Summary:        An XPath engine written in Java
License:        BSD-2-Clause
Group:          Development/Java
URL:            https://jaxen-xpath.github.io/jaxen/
VCS:            https://github.com/jaxen-xpath/jaxen

Source0:        %name-%version.tar

Patch0:         jaxen-dom4j-test-localname.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(jdom:jdom)
BuildRequires:  mvn(xom:xom)

BuildArch:      noarch

%description
Jaxen is an open source XPath 1.0 library written in Java. It is adaptable to
many different object models, including DOM, XOM, dom4j, and JDOM. It is also
possible to write adapters that treat non-XML trees such as compiled Java byte
code or Java beans as XML, thus enabling you to query these trees with XPath
too.

%javadoc_package

%prep
%setup
%autopatch -p1

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-assembly-plugin . core
%pom_remove_plugin :japicmp-maven-plugin core

%pom_change_dep -r org.jdom:jdom-legacy jdom:jdom

%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt *.md

%changelog
* Thu Jun 04 2026 Evgeniy Serov <scala@altlinux.org> 2.0.5-alt1
- Updated to 2.0.5.

* Wed May 27 2026 Evgeniy Serov <scala@altlinux.org> 2.0.3-alt1
- Updated to 2.0.3.
- Enabled tests.

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:1.2.0-alt1_6jpp11
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_2jpp8
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_19jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_14jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_12jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_10jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_9jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_8jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_7jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt3_9jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt3_5jpp7
- fc update

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt3_1jpp6
- fixed build with moved maven1

* Tue Oct 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt2_1jpp6
- rebuild with target=5 (to avoid class poisoning)

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_1jpp6
- new version

* Mon Jun 15 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_3jpp5
- added repolib

* Fri Nov 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Mon Apr 30 2007 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.4beta2
- added JPackage compat stuff

* Fri Mar 24 2006 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt0.3beta2
- Fix typo in requires of javadoc package

* Wed Mar 22 2006 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt0.2beta2
- Fix build with j2se1.5

* Sat Apr 23 2005 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt0.1beta2
- Initial build for ALT Linux Sisyphus

