Epoch: 0
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.3.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-parent
Version:          1.3.0
Release:          alt1_4jpp8
Summary:          JBossWS Parent
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws
Source0:          https://github.com/jbossws/jbossws-parent/archive/%{name}-%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-source-plugin)
Source44: import.info

%description
This package contains the JBossWS Parent.

%prep
%setup -q -n %{name}-%{name}-%{namedversion}

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_1jpp8
- new version

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

