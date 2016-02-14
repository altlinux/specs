Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jms-1.1-api
%define version 1.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          jboss-jms-1.1-api
Version:       1.0.1
Release:       alt2_12jpp8
Summary:       JBoss JMS API 1.1 Spec
License:       CDDL or GPLv2 with exceptions
URL:           http://www.jboss.org

# git clone git://github.com/jboss/jboss-jms-api_spec.git jboss-jms-1.1-api
# cd jboss-jms-1.1-api/ && git archive --format=tar --prefix=jboss-jms-1.1-api/ jboss-jms-api_1.1_spec-1.0.1.Final | xz > jboss-jms-1.1-api-1.0.1.Final.tar.xz
Source0:       %{name}-%{namedversion}.tar.xz

BuildRequires: maven-local
BuildRequires: mvn(org.jboss:jboss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
The Java Messaging Service 1.1 API classes

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jms-1.1-api
# Unneeded plugin
%pom_remove_plugin :maven-source-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc README
%doc LICENSE

%changelog
* Sun Feb 14 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_12jpp8
- updated gradle support

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_9jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt1_3jpp7
- new version

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt4_2jpp6
- fixed build with moved maven1

* Sun Dec 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt3_2jpp6
- jpp 6.0 build

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt3_1jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt2_1jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_1jpp5
- converted from JPackage by jppimport script

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_2jpp1.7
- updated to new jpackage release

* Tue Jul 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

