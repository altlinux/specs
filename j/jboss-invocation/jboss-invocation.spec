Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-invocation
%define version 1.2.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-invocation
Version:          1.2.1
Release:          alt1_3jpp8
Summary:          JBoss Invocation API 
License:          LGPLv2+
URL:              https://github.com/jbossas/jboss-invocation
Source0:          https://github.com/jbossas/jboss-invocation/archive/%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    junit
BuildRequires:    jboss-parent
BuildRequires:    jboss-logging
BuildRequires:    jboss-marshalling
BuildRequires:    jboss-logging-tools
BuildRequires:    jboss-classfilewriter
BuildRequires:    jboss-interceptors-1.2-api
BuildRequires:    wildfly-security-manager
Source44: import.info

%description
This package contains JBoss Invocation API

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-invocation-%{namedversion}

%pom_remove_plugin "org.jboss.seven2six:seven2six"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_3jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_2jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_4jpp7
- new version

