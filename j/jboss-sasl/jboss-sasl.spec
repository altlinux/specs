Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-sasl
%define version 1.0.5
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-sasl
Version:          1.0.5
Release:          alt1_1jpp8
Summary:          SASL Provider for J2SE
License:          LGPLv2+
URL:              https://github.com/wildfly-security/jboss-sasl
Source0:          https://github.com/wildfly-security/jboss-sasl/archive/%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:    mvn(org.jboss.maven.plugins:maven-injection-plugin)
Source44: import.info

%description
This package contains SASL Provider for J2SE

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_13jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_12jpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp7
- new version

