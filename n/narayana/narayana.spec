Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name narayana
%define version 5.0.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:       narayana
Version:    5.0.0
Release:    alt1_5jpp8
Summary:    Distributed Transaction Manager
License:    LGPLv2+
URL:        http://www.jboss.org/narayana/
Source0:    https://github.com/jbosstm/narayana/archive/%{namedversion}.tar.gz

BuildArch: noarch

BuildRequires: aether
BuildRequires: junit
BuildRequires: antlr-tool
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: ant-contrib
BuildRequires: apache-commons-codec
BuildRequires: avalon-logkit
BuildRequires: cdi-api
BuildRequires: hibernate-jpa-2.0-api
BuildRequires: dom4j
BuildRequires: byteman
BuildRequires: ironjacamar
BuildRequires: jacorb
BuildRequires: jakarta-commons-httpclient
BuildRequires: jboss-logging
BuildRequires: jboss-logging-tools
BuildRequires: jboss-transaction-1.2-api
BuildRequires: jboss-transaction-spi
BuildRequires: jboss-interceptors-1.2-api
BuildRequires: jboss-servlet-3.0-api
BuildRequires: jboss-ejb-3.1-api
BuildRequires: jboss-annotations-1.1-api
BuildRequires: jbossws-api >= 1.0.2
BuildRequires: jboss-integration
BuildRequires: h2
BuildRequires: hornetq
BuildRequires: mvn(org.hornetq:hornetq-journal)
BuildRequires: jfreechart
BuildRequires: java-service-wrapper
BuildRequires: slf4j
BuildRequires: maven-local
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-shade-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: maven-war-plugin
BuildRequires: idlj-maven-plugin
BuildRequires: glassfish-annotation-api
BuildRequires: jvnet-parent
BuildRequires: jbossws-parent
BuildRequires: resteasy
BuildRequires: weld-core

# This package replaced jboss-jts
# Below you can find appropriate obsoletes/provides
Provides: jboss-jts = %{version}-%{release}
Obsoletes: jboss-jts < 4.16.6-12
Source44: import.info

%description
A set of JBoss modules that fully supports ACID transactions
spread across multiple resource managers and application servers.
It implements a Distributed Transaction Manager (DTM) with support
for two-phase commit (2PC) across XA resource managers, JBoss
server instances, and CORBA OTS resources.

JBossJTS implements the Java Transaction Service (JTS) and CORBA
Transaction Service (OTS) specifications.

%package javadoc
Group: Development/Java
Summary: Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
# Extract the source:
%setup -q -n narayana-%{namedversion}

find . -name "*.jar" -type f -delete
find . -name "*.class" -type f -delete

%pom_remove_dep "orson:orson" ArjunaCore/arjuna/pom.xml
%pom_remove_plugin "org.codehaus.mojo:findbugs-maven-plugin"

# Remove the hardcoded path to emma.jar
sed -i "s|<systemPath*systemPath>||" pom.xml

# Fix the gid of jfreechart
%pom_remove_dep "jfree:jfreechart" ArjunaCore/arjuna/pom.xml
%pom_add_dep "org.jfree:jfreechart" ArjunaCore/arjuna/pom.xml

# Remove JConsole dep
%pom_remove_dep "sun.jdk:jconsole" ArjunaCore/arjuna/pom.xml

%pom_remove_dep "org.jboss.arquillian.junit:arquillian-junit-container" ArjunaJTA/cdi/pom.xml
%pom_remove_dep "org.jboss.arquillian.junit:arquillian-junit-container" txframework/pom.xml

%pom_disable_module localjunit XTS

# No org.jboss.spec:jboss-javaee-6.0:pom:3.0.1.Final
%pom_remove_dep "org.jboss.spec:jboss-javaee-6.0" txbridge/pom.xml
%pom_remove_plugin ":maven-dependency-plugin" txbridge/pom.xml
%pom_remove_plugin "org.jboss.byteman:byteman-rulecheck-maven-plugin"

# Because of removed modules
%pom_disable_module narayana-full

# Remove war deps
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:type = 'war']" XTS/sar/pom.xml
%pom_disable_module webservice rts/at/pom.xml
%pom_remove_dep "org.jboss.narayana.rts:restat-web" narayana-full/pom.xml

%pom_remove_dep "org.jboss.arquillian.junit:" ArjunaJTA/spi/pom.xml

%build
%mvn_package :::api: __default
# Some missing deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc README.md
%doc copyright.txt
%doc common/copyright.txt

%files javadoc -f .mfiles-javadoc
%doc copyright.txt
%doc common/copyright.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_5jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_4jpp8
- unbootstrap build

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

