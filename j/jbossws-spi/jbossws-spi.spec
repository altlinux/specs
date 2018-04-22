Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 3.1.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-spi
Version:          3.1.2
Release:          alt1_4jpp8
Summary:          JBossWS SPI
# https://issues.jboss.org/browse/JBWS-4002
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws

Source0:          https://github.com/jbossws/jbossws-spi/archive/%{name}-%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:    mvn(org.jboss.spec.javax.jms:jboss-jms-api_1.1_spec)
BuildRequires:    mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec)
BuildRequires:    mvn(org.jboss.ws:jbossws-api) >= 1.0.1
BuildRequires:    mvn(org.jboss.ws:jbossws-parent:pom:)
Source44: import.info

%description
JBoss WS SPI classes.

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

# java.lang.ExceptionInInitializerError
#Caused by: java.lang.IllegalArgumentException: Invalid logger interface org.jboss.wsf.spi.Loggers (implementation not found in sun.misc.Launcher$AppClassLoader@75b84c92)
#	at org.jboss.logging.Logger$1.run(Logger.java:2556)
#	at java.security.AccessController.doPrivileged(Native Method)
#	at org.jboss.logging.Logger.getMessageLogger(Logger.java:2529)
#	at org.jboss.logging.Logger.getMessageLogger(Logger.java:2516)
#	at org.jboss.wsf.spi.Loggers.<clinit>(Loggers.java:47)
#	... 29 more
rm src/test/java/org/jboss/test/wsf/spi/metadata/config/ConfigMDParserTestCase.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.1.2-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.1.2-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.1.2-alt1_2jpp8
- new jpp release

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

