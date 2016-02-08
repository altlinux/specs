Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: jdepend
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-msc
%define version 1.2.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-msc
Version:          1.2.2
Release:          alt1_2jpp8
Summary:          JBoss Modular Service Container
License:          LGPLv2+
URL:              https://github.com/jbossas/jboss-msc
Source0:          https://github.com/jbossas/jboss-msc/archive/%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    javassist
BuildRequires:    jboss-parent
BuildRequires:    junit
BuildRequires:    byteman
BuildRequires:    jboss-logging
BuildRequires:    jboss-vfs
BuildRequires:    jboss-threads
BuildRequires:    jboss-logging-tools
BuildRequires:    maven-injection-plugin
BuildRequires:    jboss-modules
BuildRequires:    apiviz
Source44: import.info

%description
This package contains the JBoss Modular Service Container.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
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
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
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

