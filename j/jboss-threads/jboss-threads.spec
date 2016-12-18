Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-threads
%define version 2.2.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-threads
Version:          2.2.1
Release:          alt1_2jpp8
Summary:          JBoss Threads
# Not available license file https://issues.jboss.org/browse/JBTHR-36
License:          LGPLv2+
URL:              https://github.com/jbossas/jboss-threads
Source0:          https://github.com/jbossas/jboss-threads/archive/%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(jdepend:jdepend)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.apiviz:apiviz)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
Source44: import.info

%description
This package contains JBoss Threads

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_remove_plugin :maven-source-plugin

%build

# Disable test failure @ random fails:
# junit.framework.AssertionFailedError at org.jboss.threads.DeferredInterruptTestCase.testDeferral(DeferredInterruptTestCase.java:63)
%mvn_build -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt1_6jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt1_4jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt1_2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt2_8jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt2_6jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt1_6jpp7
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_2jpp6
- new version

