Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbossws-parent
%define version 1.1.0
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-parent
Version:          1.1.0
Release:          alt1_11jpp8
Summary:          JBossWS Parent
Group:            Development/Other
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws
Source0:          https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/jboss/ws/jbossws-parent/%{namedversion}/jbossws-parent-%{namedversion}.pom

BuildArch:        noarch

BuildRequires:    maven-local
Source44: import.info

%description
This package contains the JBossWS Parent

%prep
%setup -c -T
cp %{SOURCE0} pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_11jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_9jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_3jpp7
- new release

* Thu Oct 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_1jpp7
- new release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_4jpp6
- use maven-plugin-build-helper

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_4jpp6
- new jpp release

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_3jpp6
- new jpp release

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_1jpp5
- new jpp release

