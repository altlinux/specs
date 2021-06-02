Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jboss-modules
Version:        1.5.2
Release:        alt2_12jpp11
Summary:        Modular Classloading System
# XPP3 License: src/main/java/org/jboss/modules/xml/MXParser.java
#  src/main/java/org/jboss/modules/xml/XmlPullParser.java
#  src/main/java/org/jboss/modules/xml/XmlPullParserException.java
License:        ASL 2.0 and xpp

%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

URL:            https://github.com/jbossas/jboss-modules
Source0:        %{url}/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.jboss.shrinkwrap:shrinkwrap-impl-base)
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
Source44: import.info

%description
Ths package contains A Modular Classloading System.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}-%{namedversion}

# do not build custom Javadocs with apiviz doclet
%pom_remove_plugin :maven-javadoc-plugin

# remove unnecessary maven plugins
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-source-plugin

# Tries to connect to remote host
rm src/test/java/org/jboss/modules/MavenResourceTest.java \
 src/test/java/org/jboss/modules/maven/MavenSettingsTest.java

# remove test that's not ready for Java 9 Modules
rm src/test/java/org/jboss/modules/JAXPModuleTest.java

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install


%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE.txt XPP3-LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt XPP3-LICENSE.txt


%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.5.2-alt2_12jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_8jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_5jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_3jpp8
- fc27 update

* Tue Oct 31 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_2jpp8
- new jpp release

* Mon Oct 30 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_2jpp8
- new jpp release
- removed javadoc due to non-identical noarch problem

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1_3jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1_2jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_0.1.Beta3jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_6jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_6jpp7
- new version

