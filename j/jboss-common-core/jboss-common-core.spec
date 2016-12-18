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
%define version 2.5.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-common-core
Version:          2.5.0
Release:          alt1_1jpp8
Summary:          JBoss Common Classes
# Under Public Domain license src/main/java/org/jboss/util/Base64.java
License:          ASL 2.0 and Public Domain
URL:              http://www.jboss.org
Source0:          https://github.com/jboss/jboss-common-core/archive/%{name}-%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
Provides:         bundled(java-base64) = 2.1
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
%setup -q -n %{name}-%{name}-%{namedversion}

# The URLLister* family of classes was removed because the
# apache-slide:webdavlib is a dead project and
# the classes aren't used in JBoss AS 7 at all
rm src/main/java/org/jboss/net/protocol/URLLister.java \
 src/main/java/org/jboss/net/protocol/URLListerBase.java \
 src/main/java/org/jboss/net/protocol/URLListerFactory.java \
 src/main/java/org/jboss/net/protocol/file/FileURLLister.java

%pom_change_dep org.jboss.logging:jboss-logging-spi org.jboss.logging:jboss-logging

# AssertionFailedError: expected:<333> but was:<324>
rm src/test/java/org/jboss/test/util/test/xml/resolver/JBossEntityResolverUnitTestCase.java

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.5.0-alt1_1jpp8
- new version

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

