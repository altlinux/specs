# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-connector-1.6-api
%define version 1.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-connector-1.6-api
Version:          1.0.1
Release:          alt2_3jpp8
Summary:          Connector Architecture 1.6 API
Group:            Development/Other
License:          CDDL or GPLv2 with exceptions
URL:              http://www.jboss.org

Source0:          https://github.com/jboss/jboss-connector-api_spec/archive/jboss-connector-api_1.6_spec-%{namedversion}.tar.gz

BuildRequires:    jboss-specs-parent
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    jboss-transaction-1.1-api

BuildArch:        noarch
Source44: import.info

%description
Java EE Connector Architecture 1.6 API classes

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-connector-api_spec-jboss-connector-api_1.6_spec-%{namedversion}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc README LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_0.6.20120310git9dc9a5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_0.5.20120310git9dc9a5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_0.3.20120310git9dc9a5jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_0.3.20120310git9dc9a5jpp7
- new version

