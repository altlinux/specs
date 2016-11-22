Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbossws-api
%define version 1.0.2
%global namedreltag .CR1
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-api
Version:          1.0.2
Release:          alt1_0.7.CR1jpp8
Summary:          JBossWS API
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws

# svn export http://anonsvn.jboss.org/repos/jbossws/api/tags/jbossws-api-1.0.2.CR1/ jbossws-api-1.0.2.CR1
# tar cafJ jbossws-api-1.0.2.CR1.tar.xz jbossws-api-1.0.2.CR1
Source0:          jbossws-api-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:    mvn(org.jboss.ws:jbossws-parent:pom:)
Source44: import.info

%description
JBoss WS public API

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jbossws-api-%{namedversion}

# Disable java8doc doclint, using own javadoc setting
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
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

