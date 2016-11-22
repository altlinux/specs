Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbossws-spi
%define version 2.3.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-spi
Version:          2.3.1
Release:          alt1_4jpp8
Summary:          JBossWS SPI
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws

# svn export http://anonsvn.jboss.org/repos/jbossws/spi/tags/jbossws-spi-2.3.1.Final/
# tar cafJ jbossws-spi-2.3.1.Final.tar.xz jbossws-spi-2.3.1.Final
Source0:          jbossws-spi-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:    mvn(org.jboss.spec.javax.jms:jboss-jms-api_1.1_spec)
BuildRequires:    mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec)
BuildRequires:    mvn(org.jboss.ws:jbossws-api) >= 1.0.1
BuildRequires:    mvn(org.jboss.ws:jbossws-parent:pom:)
Source44: import.info

%description
JBoss WS SPI classes

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jbossws-spi-%{namedversion}
# Disable java8doc doclint, using own javadoc setting
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_4jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_3jpp8
- java8 mass update

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt1_4jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt1_1jpp7
- update

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.3-alt1_3jpp7
- new version

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_2jpp5
- new jpp release

