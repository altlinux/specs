Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-ejb-client
%define version 2.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          jboss-ejb-client
Version:       2.0.1
Release:       alt1_4jpp8
Summary:       JBoss EJB client
License:       LGPLv2+
URL:           http://www.jboss.org/

Source0:       https://github.com/jbossas/jboss-ejb-client/archive/%{namedversion}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.logging:jboss-logging)
BuildRequires: mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires: mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires: mvn(org.jboss.marshalling:jboss-marshalling)
BuildRequires: mvn(org.jboss.marshalling:jboss-marshalling-river)
BuildRequires: mvn(org.jboss.maven.plugins:maven-injection-plugin)
BuildRequires: mvn(org.jboss.remoting:jboss-remoting)
BuildRequires: mvn(org.jboss.sasl:jboss-sasl)
BuildRequires: mvn(org.jboss.spec.javax.ejb:jboss-ejb-api_3.1_spec)
BuildRequires: mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.1_spec)
BuildRequires: mvn(org.jboss.xnio:xnio-api)
BuildRequires: mvn(org.jboss.xnio:xnio-nio)

BuildArch:     noarch
Source44: import.info

%description
Client library for EJB applications working against JBoss AS

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

# Dont work properly
%pom_remove_plugin :maven-checkstyle-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_4jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_3jpp8
- java8 mass update

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_3jpp7
- new version

