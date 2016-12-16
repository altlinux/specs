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
%define version 5.3.3
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          narayana
Version:       5.3.3
Release:       alt1_1jpp8
Summary:       Distributed Transaction Manager
License:       LGPLv2+
URL:           http://narayana.io/
Source0:       https://github.com/jbosstm/narayana/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(commons-httpclient:commons-httpclient)
BuildRequires: mvn(dom4j:dom4j)
BuildRequires: mvn(java_cup:java_cup)
BuildRequires: mvn(javax.annotation:javax.annotation-api)
BuildRequires: mvn(javax.enterprise:cdi-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.activemq:artemis-journal)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-war-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:idlj-maven-plugin)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi.services)
BuildRequires: mvn(org.jacoco:org.jacoco.ant)
BuildRequires: mvn(org.jacorb:jacorb)
BuildRequires: mvn(org.jacorb:jacorb-idl-compiler)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss:jboss-transaction-spi) >= 7.3.0
BuildRequires: mvn(org.jboss.byteman:byteman)
BuildRequires: mvn(org.jboss.byteman:byteman-dtest)
BuildRequires: mvn(org.jboss.byteman:byteman-submit)
BuildRequires: mvn(org.jboss.integration:jboss-corba-ots-spi)
BuildRequires: mvn(org.jboss.ironjacamar:ironjacamar-spec-api)
BuildRequires: mvn(org.jboss.jandex:jandex-maven-plugin)
BuildRequires: mvn(org.jboss.logging:jboss-logging)
BuildRequires: mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires: mvn(org.jboss.resteasy:resteasy-jaxb-provider)
BuildRequires: mvn(org.jboss.resteasy:resteasy-jaxrs)
BuildRequires: mvn(org.jboss.resteasy:resteasy-jettison-provider)
BuildRequires: mvn(org.jboss.resteasy:tjws)
BuildRequires: mvn(org.jboss.spec.javax.ejb:jboss-ejb-api_3.1_spec)
BuildRequires: mvn(org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec)
BuildRequires: mvn(org.jboss.spec.javax.jms:jboss-jms-api_1.1_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec)
BuildRequires: mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.2_spec)
BuildRequires: mvn(org.jboss.ws:jbossws-api)
BuildRequires: mvn(org.springframework:spring-tx)
BuildRequires: mvn(tanukisoft:wrapper)

BuildArch:     noarch
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
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
# Extract the source:
%setup -q -n %{name}-%{namedversion}

find . -name "*.jar" -type f -delete
find . -name "*.class" -type f -delete
find . -name "*.dll" -type f -delete
find . -name "*.exe" -type f -delete
find . -name "*.so" -type f -delete
rm -r ArjunaJTS/services/bin/*

%pom_disable_module localjunit XTS
%pom_disable_module narayana-full
%pom_disable_module webservice rts/at

%pom_remove_plugin -r "org.codehaus.mojo:findbugs-maven-plugin"
%pom_remove_plugin -r "org.sonatype.plugins:nexus-staging-maven-plugin"
%pom_remove_plugin -r "org.jboss.byteman:byteman-rulecheck-maven-plugin"

%pom_remove_plugin -r :nexus-staging-maven-plugin ArjunaJTS/narayana-jts-jacorb  ArjunaJTS/narayana-jts-idlj

# Remove JConsole dep
%pom_remove_dep "sun.jdk:jconsole" ArjunaCore/arjuna
%pom_remove_dep -r "orson:orson" ArjunaCore/arjuna ArjunaCore/arjunacore
%pom_change_dep -r "jfree:jfreechart" "org.jfree:jfreechart" ArjunaCore/arjuna ArjunaCore/arjunacore

%pom_remove_dep -r "org.jboss.arquillian.junit:arquillian-junit-container"

# org.jboss.openjdk-orb:openjdk-orb:8.0.4.Final
%pom_remove_dep -r "org.jboss.openjdk-orb:openjdk-orb"

%pom_remove_plugin ":maven-dependency-plugin" txbridge

# Disable copy of: jboss-transaction-spi and jboss-transaction-api_1.2_spec
%pom_xpath_remove pom:Embed-Dependency osgi/jta
%pom_xpath_remove pom:Export-Package osgi/jta
%pom_xpath_remove pom:Private-Package osgi/jta
# Invalid filter syntax in requirement
%pom_xpath_remove pom:Require-Capability osgi/jta

# org.jboss.osgi.metadata:jbosgi-metadata:4.0.0.CR1
%pom_remove_dep "org.jboss.osgi.metadata:jbosgi-metadata" osgi
%pom_remove_dep "org.jboss.osgi.metadata:jbosgi-metadata" osgi/jta

# package org.osgi.framework.wiring does not exist
%pom_change_dep "org.osgi:org.osgi.core" "org.eclipse.osgi:org.eclipse.osgi" osgi
%pom_change_dep "org.osgi:org.osgi.core" "org.eclipse.osgi:org.eclipse.osgi" osgi/jta
# package org.osgi.service.cm does not exist
%pom_change_dep "org.osgi:org.osgi.compendium" "org.eclipse.osgi:org.eclipse.osgi.services"  osgi
%pom_change_dep "org.osgi:org.osgi.compendium" "org.eclipse.osgi:org.eclipse.osgi.services"  osgi/jta

%pom_xpath_remove "pom:dependency[pom:type='war']" XTS/sar

# https://bugs.openjdk.java.net/browse/JDK-8067747
for mod in orbportability jts; do
   %pom_xpath_inject "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:executions/pom:execution/pom:configuration" \
  "<useIncrementalCompilation>false</useIncrementalCompilation>" ArjunaJTS/${mod}
done

# Disable default-jar execution of maven-jar-plugin, which is causing
# problems with version 3.0.0 of the plugin.
for mod in XTS/WS-C XTS/WS-T XTS/WSTX XTS/bridge; do
    %pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions" "
        <execution>
          <id>default-jar</id>
          <phase>skip</phase>
        </execution>" ${mod}
done

# [ERROR] 'dependencies.dependency.(groupId:artifactId:type:classifier)' must be unique duplicate declaration of version
%pom_remove_dep org.jboss.narayana:common ArjunaJTS/orbportability
%pom_add_dep org.jboss.narayana:common:'${project.version}' ArjunaJTS/orbportability

%pom_remove_dep -r org.jboss.resteasy:jaxrs-api rts/at/bridge rts/at/integration rts/at/tx rts/at/util

%mvn_package :::api: __default
%mvn_package :::war: __noinstall

%build

# Some missing deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc common/copyright.txt

%files javadoc -f .mfiles-javadoc
%doc common/copyright.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 5.3.3-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_5jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_4jpp8
- unbootstrap build

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

