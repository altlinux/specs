Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbossws-common
%define version 2.3.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-common
Version:          2.3.1
Release:          alt1_3jpp8
Summary:          JBossWS Common
License:          LGPLv2+
URL:              http://www.jboss.org/jbossws

# svn export http://anonsvn.jboss.org/repos/jbossws/common/tags/jbossws-common-2.3.1.Final/ jbossws-common-2.3.1.Final
# tar cafJ jbossws-common-2.3.1.Final.tar.xz jbossws-common-2.3.1.Final
Source0:          jbossws-common-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    jboss-common-core
BuildRequires:    jboss-ejb-3.1-api
BuildRequires:    jboss-jaxb-intros
BuildRequires:    jboss-jaxws-2.2-api
BuildRequires:    jboss-jaxrpc-1.1-api
BuildRequires:    jboss-jms-1.1-api
BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    jbossws-api
BuildRequires:    jbossws-spi
BuildRequires:    jbossws-parent
BuildRequires:    jboss-logging
BuildRequires:    jboss-logging-tools
BuildRequires:    wsdl4j
Source44: import.info

%description
JBoss Web Services - Common

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jbossws-common-%{namedversion}

# Remove test where network connectivity is required
rm src/test/java/org/jboss/test/ws/common/management/AbstractServerConfigTestCase.java

# Add jaxrpc dependency, since it's required
%pom_xpath_inject "pom:dependencies" "<dependency><groupId>org.jboss.spec.javax.xml.rpc</groupId><artifactId>jboss-jaxrpc-api_1.1_spec</artifactId><version>1.0.1.Final</version></dependency>"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
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

