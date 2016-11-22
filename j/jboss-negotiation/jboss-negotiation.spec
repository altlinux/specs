Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-negotiation
%define version 2.2.7
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-negotiation
Version:          2.2.7
Release:          alt1_5jpp8
Summary:          JBoss Negotiation
License:          LGPLv2+
URL:              http://www.jboss.org/picketlink/Negotiation
Source0:          https://github.com/wildfly-security/jboss-negotiation/archive/security-negotiation-%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec)
BuildRequires:    mvn(org.jboss.web:jbossweb)
BuildRequires:    mvn(org.picketbox:picketbox)
BuildRequires:    mvn(org.picketbox:picketbox-commons)
Source44: import.info


%description
Negotiation project provides SPNEGO/Kerberos support in JBoss

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-negotiation-security-negotiation-%{namedversion}

%pom_disable_module jboss-negotiation-toolkit

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt1_5jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt1_4jpp8
- added java requires

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2_10.SP1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2_9.SP1jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2_7.SP1jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_7.SP1jpp7
- new version

