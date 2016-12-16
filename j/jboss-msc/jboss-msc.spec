Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-msc
%define version 1.2.6
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-msc
Version:          1.2.6
Release:          alt1_1jpp8
Summary:          JBoss Modular Service Container
# Not available license file https://issues.jboss.org/browse/MSC-153
License:          LGPLv2+
URL:              https://github.com/jbossas/jboss-msc
Source0:          https://github.com/jbossas/jboss-msc/archive/%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(jdepend:jdepend)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.javassist:javassist)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss:jboss-vfs)
BuildRequires:    mvn(org.jboss.apiviz:apiviz)
BuildRequires:    mvn(org.jboss.byteman:byteman)
BuildRequires:    mvn(org.jboss.byteman:byteman-bmunit)
BuildRequires:    mvn(org.jboss.byteman:byteman-install)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:    mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires:    mvn(org.jboss.maven.plugins:maven-injection-plugin)
BuildRequires:    mvn(org.jboss.modules:jboss-modules)
BuildRequires:    mvn(org.jboss.threads:jboss-threads)
Source44: import.info

%description
This package contains the JBoss Modular Service Container.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-msc-%{namedversion}

%build
# Some failed tests, most probably because network limitations on Koji
%mvn_build -f

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.6-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_4jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_0.3.Beta1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3jpp7
- new version

