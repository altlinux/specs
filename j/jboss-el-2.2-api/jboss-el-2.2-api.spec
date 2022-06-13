Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.5
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:         jboss-el-2.2-api
Version:      1.0.5
Release:      alt1_1jpp11
Summary:      Expression Language 2.2 API
License:      CDDL or GPLv2 with exceptions

URL:          https://github.com/jboss/jboss-el-api_spec
Source0:      %{url}/archive/jboss-el-api_2.2_spec-%{namedversion}.tar.gz
Source1:      cddl.txt

BuildArch:    noarch

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
Source44: import.info

%description
Expression Language 2.2 API classes.

%package javadoc
Group: Development/Java
Summary: Javadocs for %{name}
BuildArch: noarch

%description javadoc	
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-el-api_spec-jboss-el-api_2.2_spec-%{namedversion}

%pom_remove_plugin :maven-source-plugin

cp %{SOURCE1} .

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference cddl.txt LICENSE
%doc README

%files javadoc -f .mfiles-javadoc
%doc --no-dereference cddl.txt LICENSE

%changelog
* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 1.0.5-alt1_1jpp11
- java11 build

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_1jpp8
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_10jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_9jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_6jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_5jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_4jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_0.6.20120212git2fabd8jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_0.4.20120212git2fabd8jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_0.4.20120212git2fabd8jpp7
- new version

