Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-ejb-3.1-api
%define version 1.0.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-ejb-3.1-api
Version:          1.0.2
Release:          alt2_14jpp8
Summary:          EJB 3.1 API
Group:            Development/Other
License:          CDDL or GPLv2 with exceptions
Url:              http://www.jboss.org
Source0:          https://github.com/jboss/jboss-ejb-api_spec/archive/jboss-ejb-api_3.1_spec-%{namedversion}.tar.gz

BuildRequires:    jboss-transaction-1.1-api
BuildRequires:    jboss-jaxrpc-1.1-api
BuildRequires:    jboss-specs-parent
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin

BuildArch:        noarch
Source44: import.info

%description
The Java EJB 3.1 API classes.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-ejb-api_spec-jboss-ejb-api_3.1_spec-%{namedversion}

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
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_14jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_13jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_3jpp7
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt1_4jpp6
- new version

