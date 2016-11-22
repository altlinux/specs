Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-el-2.2-api
%define version 1.0.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:         jboss-el-2.2-api
Version:      1.0.2
Release:      alt1_4jpp8
Summary:      Expression Language 2.2 API
License:      CDDL or GPLv2 with exceptions
URL:          http://www.jboss.org

Source0:      https://github.com/jboss/jboss-el-api_spec/archive/%{namedversion}.tar.gz

BuildRequires: jboss-parent
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin

BuildArch: noarch
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
%setup -q -n jboss-el-api_spec-%{namedversion}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE
%doc README

%files javadoc -f .mfiles-javadoc
%doc LICENSE
%doc README

%changelog
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

