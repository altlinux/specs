Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.3
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-api
Version:          1.0.3
Release:          alt1_4jpp8
Summary:          JBossWS API
# https://issues.jboss.org/browse/JBWS-4001
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws
Source0:          https://github.com/jbossws/jbossws-api/archive/%{name}-%{namedversion}.tar.gz
BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-annotations:1)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor:1)
BuildRequires:    mvn(org.jboss.ws:jbossws-parent:pom:)
Source44: import.info

%description
JBoss WS public API.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{namedversion}

# Disable java8doc doclint, using own javadoc setting
%pom_remove_plugin :maven-javadoc-plugin

%pom_xpath_set pom:properties/pom:jboss-logging-annotations.version 1
%pom_xpath_set pom:properties/pom:jboss-logging-processor.version 1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_0.7.CR1jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_0.6.CR1jpp8
- java8 mass update

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1jpp7
- update

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp7
- new version

