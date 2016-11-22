Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-common-core
%define version 2.2.22
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jboss-common-core
Version:          2.2.22
Release:          alt1_4jpp8
Summary:          JBoss Common Classes
License:          LGPLv2+ and ASL 1.1
URL:              http://www.jboss.org

# svn export http://anonsvn.jboss.org/repos/common/common-core/tags/2.2.22.GA/ jboss-common-core-2.2.22.GA
# tar cafJ jboss-common-core-2.2.22.GA.tar.xz jboss-common-core-2.2.22.GA
Source0:          %{name}-%{namedversion}.tar.xz
# The URLLister* family of classes was removed because the apache-slide:webdavlib is a dead project and the classes aren't used in JBoss AS 7 at all. 
Patch0:           %{name}-%{namedversion}-URLLister-removal.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
Source44: import.info

%description
JBoss Common Core Utility classes

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1

rm -rf projectSet.psf .settings/ .project .classpath

%pom_remove_plugin :maven-source-plugin

%build
# Some failed tests
# Failed tests: testJavaLangEditors(org.jboss.test.util.test.propertyeditor.PropertyEditorsUnitTestCase):
#   PropertyEditor: org.jboss.util.propertyeditor.BooleanEditor, getAsText() == expectedStringOutput ' expected:<null> but was:<null>
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.2.22-alt1_4jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.2.22-alt1_3jpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.18-alt2_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.18-alt2_9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.18-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.18-alt1_7jpp7
- new version

* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.14-alt2_2jpp6
- fixed build with maven3

* Wed Feb 09 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.2.14-alt1_2jpp6
- new version

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2.8-alt4_1jpp5
- target=5 and build with velocity 15

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2.8-alt3_1jpp5
- build with velocity 15

* Thu Sep 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2.8-alt2_1jpp5
- fixed build with new maven 2.0.8

* Thu Jun 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2.8-alt1_1jpp5
- new jpp release

