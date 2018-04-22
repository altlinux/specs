Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.1.4
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          jboss-ejb-client
Version:       2.1.4
Release:       alt1_4jpp8
Summary:       JBoss EJB client
# https://issues.jboss.org/browse/EJBCLIENT-160
License:       LGPLv2+
URL:           http://www.jboss.org/
Source0:       https://github.com/jbossas/jboss-ejb-client/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

Patch0:        jboss-ejb-client-2.1.4-remove-ambiguous-reference-to-debugf.patch

BuildRequires: maven-local
BuildRequires: mvn(java_cup:java_cup)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.byteman:byteman)
BuildRequires: mvn(org.jboss.byteman:byteman-bmunit)
BuildRequires: mvn(org.jboss.byteman:byteman-install)
BuildRequires: mvn(org.jboss.byteman:byteman-submit)
BuildRequires: mvn(org.jboss.logging:jboss-logging) >= 3.1.4.GA
BuildRequires: mvn(org.jboss.logging:jboss-logging-processor:1)
BuildRequires: mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires: mvn(org.jboss.marshalling:jboss-marshalling)
BuildRequires: mvn(org.jboss.marshalling:jboss-marshalling-river)
BuildRequires: mvn(org.jboss.remoting:jboss-remoting)
BuildRequires: mvn(org.jboss.sasl:jboss-sasl)
BuildRequires: mvn(org.jboss.spec.javax.ejb:jboss-ejb-api_3.1_spec)
BuildRequires: mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.1_spec)
BuildRequires: mvn(org.jboss.xnio:xnio-api)
BuildRequires: mvn(org.jboss.xnio:xnio-nio)

BuildArch:     noarch
Source44: import.info

%description
Client library for EJB applications working against Wildfly.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1

%pom_xpath_set pom:properties/pom:version.org.jboss.logging.jboss-logging-processor 1

# Dont work properly
%pom_remove_plugin :maven-checkstyle-plugin

%build

# NoClassDefFoundError: Could not initialize class org.jboss.remoting3.remote.RemoteLogger
%mvn_build -f

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.4-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.4-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.4-alt1_2jpp8
- new jpp release

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

