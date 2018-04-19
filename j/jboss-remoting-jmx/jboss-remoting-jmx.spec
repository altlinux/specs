Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          jboss-remoting-jmx
Version:       2.0.1
Release:       alt1_4jpp8
Summary:       JMX via JBoss Remoting
License:       LGPLv2+
URL:           http://www.jboss.org/
Source0:       https://github.com/jbossas/remoting-jmx/archive/%{namedversion}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.logging:jboss-logging)
BuildRequires: mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires: mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires: mvn(org.jboss.marshalling:jboss-marshalling)
BuildRequires: mvn(org.jboss.marshalling:jboss-marshalling-river)
BuildRequires: mvn(org.jboss.maven.plugins:maven-injection-plugin)
BuildRequires: mvn(org.jboss.remoting:jboss-remoting) >= 3.2.2
BuildRequires: mvn(org.jboss.sasl:jboss-sasl)
BuildRequires: mvn(org.jboss.xnio:xnio-api)
BuildRequires: mvn(org.jboss.xnio:xnio-nio)

BuildArch:     noarch
Source44: import.info

%description
Library for making JMX accessible using Remoting.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n remoting-jmx-%{namedversion}

%build
# Disable temporarily the test suite. Build fails: Timeout(86400)
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README
%doc --no-dereference COPYING.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference COPYING.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_4jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_3jpp8
- new version

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_4jpp7
- fixed build

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_4jpp7
- new version

