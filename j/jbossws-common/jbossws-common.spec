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
%define version 3.1.3
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-common
Version:          3.1.3
Release:          alt1_4jpp8
Summary:          JBossWS Common
License:          LGPLv2+
URL:              http://jbossws.jboss.org

Source0:          https://github.com/jbossws/jbossws-common/archive/%{name}-%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(jboss.jaxbintros:jboss-jaxb-intros)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor:1)
BuildRequires:    mvn(org.jboss.ws:jbossws-parent:pom:)
BuildRequires:    mvn(org.jboss.ws:jbossws-spi)
BuildRequires:    mvn(org.jboss.spec.javax.jms:jboss-jms-api_1.1_spec)
BuildRequires:    mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec)
BuildRequires:    mvn(org.jboss.spec.javax.xml.rpc:jboss-jaxrpc-api_1.1_spec)
BuildRequires:    mvn(org.jboss.spec.javax.xml.ws:jboss-jaxws-api_2.2_spec)
BuildRequires:    mvn(wsdl4j:wsdl4j)
Source44: import.info

%description
JBoss Web Services - Common.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{namedversion}

# Remove test where network connectivity is required
rm src/test/java/org/jboss/test/ws/common/management/AbstractServerConfigTestCase.java

%pom_xpath_set pom:properties/pom:jboss-logging-processor.version 1

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.1.3-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.1.3-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.1.3-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_3jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_2jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt1_3jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt1_1jpp7
- update

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_4jpp7
- new version

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt1_2jpp5
- full version

* Fri Mar 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt0.1jpp
- bootstrap for jbossas

