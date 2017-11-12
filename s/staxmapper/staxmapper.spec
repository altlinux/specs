Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.2.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             staxmapper
Version:          1.2.0
Release:          alt1_3jpp8
Summary:          StAX Mapper
License:          LGPLv2+
URL:              https://github.com/jbossas/staxmapper
Source0:          https://github.com/jbossas/staxmapper/archive/%{namedversion}.tar.gz
BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
Source44: import.info

%description
This package contains the StAX Mapper.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%build
%mvn_build

%install
%mvn_install

# Not available license file reported @ https://issues.jboss.org/browse/STXM-14
%files -f .mfiles
%files javadoc -f .mfiles-javadoc

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1jpp8
- new version

* Sun Feb 14 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_13jpp8
- updated gradle support

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_4jpp7
- new version

