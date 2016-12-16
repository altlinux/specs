Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name apacheds
%define version 2.0.0
%global namedreltag -M21
%global namedversion %{version}%{?namedreltag}

%global jetty_version 8.1.17.v20150415

Name:          apacheds
Version:       2.0.0
Release:       alt1_0.3.M21jpp8
Summary:       Apache Directory Server
License:       ASL 2.0
Url:           http://directory.apache.org/
Source0:       http://www.apache.org/dist/directory/apacheds/dist/%{namedversion}/%{name}-parent-%{namedversion}-source-release.zip

Patch0:        apacheds-2.0.0-M21-jetty8.patch

BuildRequires: maven-local
BuildRequires: mvn(com.google.code.findbugs:annotations)
BuildRequires: mvn(commons-collections:commons-collections)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(ldapsdk:ldapsdk)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(net.sf.ehcache:ehcache-core)
BuildRequires: mvn(org.apache.directory.api:api-asn1-api)
BuildRequires: mvn(org.apache.directory.api:api-dsml-engine)
BuildRequires: mvn(org.apache.directory.api:api-i18n)
BuildRequires: mvn(org.apache.directory.api:api-ldap-client-api)
BuildRequires: mvn(org.apache.directory.api:api-ldap-codec-core)
BuildRequires: mvn(org.apache.directory.api:api-ldap-codec-standalone)
BuildRequires: mvn(org.apache.directory.api:api-ldap-extras-aci)
BuildRequires: mvn(org.apache.directory.api:api-ldap-extras-sp)
BuildRequires: mvn(org.apache.directory.api:api-ldap-extras-trigger)
BuildRequires: mvn(org.apache.directory.api:api-ldap-extras-util)
BuildRequires: mvn(org.apache.directory.api:api-ldap-model)
BuildRequires: mvn(org.apache.directory.api:api-ldap-schema-data)
BuildRequires: mvn(org.apache.directory.api:api-util)
BuildRequires: mvn(org.apache.directory.jdbm:apacheds-jdbm1)
BuildRequires: mvn(org.apache.directory.mavibot:mavibot)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.mina:mina-core)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires: mvn(org.eclipse.jetty:jetty-server:%jetty_version)
BuildRequires: mvn(org.eclipse.jetty:jetty-util:%jetty_version)
BuildRequires: mvn(org.eclipse.jetty:jetty-webapp:%jetty_version)
BuildRequires: mvn(org.eclipse.jetty:jetty-xml:%jetty_version)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
BuildRequires: mvn(tanukisoft:wrapper)

Obsoletes:     %{name}-jdbm < %{version}
Obsoletes:     %{name}-utils
Obsoletes:     %{name}-xdbm

BuildArch:     noarch
Source44: import.info

%description
ApacheDS is an extensible and embeddable directory server
entirely written in Java, which has been certified LDAPv3
compatible by the Open Group. Besides LDAP it supports
Kerberos 5 and the Change Password Protocol. It has been
designed to introduce triggers, stored procedures, queues and
views to the world of LDAP which has lacked these rich
constructs.

%package core
Group: Development/Java
Summary:       ApacheDS Core

%description core
Server's core contains the JNDI provider, interceptors,
schema, and database subsystems. The core is the heart
of the server without protocols enabled.
- A linked in memory AVL tree implementation with Cursor.
- Contains classes that store interfaces with various
constants in ApacheDS.
Cursor interfaces used by the server core.
Server side LDAP entry classes.
Integration testing framework for Apache Directory Server.
Contains a JNDI provider implementation which wraps the
core so existing applications based on JNDI can use the
server embedded transparently. Remote and local run-time
operations will appear and feel exactly the same with a
performance boost when local. All operations via this
JNDI provider bypass the LDAP stack to perform operations
directly on the ApacheDS core.
A collection of tools as plugins to manage various tasks
associated with the directory server.
Shared classes between the core plugin and the core to
prevent cyclic dependencies since the core uses the core
plugin.
A linked in memory splay tree implementation with Cursor.
Core unit tests. 

%package http-integration
Group: Development/Java
Summary:       ApacheDS Jetty HTTP Server Integration

%description http-integration
This package provides Jetty HTTP Server Integration.

%package i18n
Group: Development/Java
Summary:       ApacheDS I18n

%description i18n
Internationalization of errors and other messages.

%package kerberos
Group: Development/Java
Summary:       ApacheDS Kerberos

%description kerberos
This package provides:
- The Kerberos protocol provider for ApacheDS.
- Interceptors used by the ApacheDS kerberos service.

%package osgi
Group: Development/Java
Summary:       ApacheDS OSGi Integration

%description osgi
This package provides:
- ApacheDS OSGi Integration Tests.

%package protocols
Group: Development/Java
Summary:       ApacheDS Protocols

%description protocols
This package provides the following protocols for ApacheDS:
- Change Password
- DHCP
- DNS
- LDAP
- NTP

%package server
Group: Development/Java
Summary:       ApacheDS Server modules

%description server
Integration testing framework for Apache Directory Server.
The JNDI provider which launches the core and associated
network services: Changepw, Kerberos, LDAP, and NTP if
all are configured. By default only LDAP is configured
to start-up.
A multi-master replication service for replicating
information across ApacheDS instances. This service is
modeled as an interceptor.
Various command-line utilities for apacheds.
Unit testing framework for ApacheDS Server JNDI Provider.
A single authoritative server.XML file. 

%package service
Group: Development/Java
Summary:       ApacheDS Services

%description service
This package provides ApacheDS Services. Used for reading the
configuration present in a Partition and instantiate the
necessary objects like DirectoryService, Interceptors etc.

%package wrapper
Group: Development/Java
Summary:       ApacheDS Wrapper

%description wrapper
A Tanuki Wrapper implementation for the ApacheDS service.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-parent-%{namedversion}
# cleanup
find . -name "*.bat" -delete
find . -name "*.class" -delete
find . -name "*.exe" -delete
find . -name "*.jar" -print -delete
rm -r installers-maven-plugin/src/main/resources/org/apache/directory/server/installers/*

chmod 644 README.txt

%patch0 -p1

%pom_xpath_set "pom:properties/pom:jetty.version" %jetty_version

%pom_remove_parent

%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-dependency-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin

%pom_disable_module all
%pom_disable_module installers
%pom_disable_module installers-maven-plugin

%pom_remove_dep -r :apacheds-installers
%pom_remove_dep -r :apacheds-installers-maven-plugin
%pom_remove_dep -r org.apache.directory.junit:junit-addons
# Remove the com.mycila.junit.concurrent annotations
sed -i '/Concurrency/d' $(find */src/test/java -name "*.java")
sed -i '/ConcurrentJunitRunner/d' $(find */src/test/java -name "*.java")

%pom_change_dep -r findbugs:annotations com.google.code.findbugs:annotations

%pom_xpath_remove -r "pom:dependency[pom:scope='test']"

%mvn_package :%{name}-core* core
%mvn_package :%{name}-interceptors* core
%mvn_package ":%{name}-http-directory-bridge" core
%mvn_package :%{name}-jdbm* core
%mvn_package ":%{name}-ldif-partition" core
%mvn_package ":%{name}-mavibot-partition" core
%mvn_package ":%{name}-server-annotations" core
%mvn_package ":%{name}-server-config" core
%mvn_package ":%{name}-test-framework" core
%mvn_package ":%{name}-xdbm-partition" core
%mvn_package ":%{name}-i18n" i18n
%mvn_package ":%{name}-interceptor-kerberos" kerberos
%mvn_package :%{name}-kerberos-* kerberos
%mvn_package ":kerberos-client" kerberos
%mvn_package ":%{name}-protocol-kerberos" kerberos
%mvn_package ":%{name}-protocol-changepw" protocols
%mvn_package ":%{name}-protocol-dhcp" protocols
%mvn_package ":%{name}-protocol-dns" protocols
%mvn_package ":%{name}-protocol-ldap" protocols
%mvn_package ":%{name}-protocol-ntp" protocols
%mvn_package ":%{name}-protocol-shared" protocols
%mvn_package ":ldap-client-test" protocols
%mvn_package ":%{name}-osgi-integ" osgi
%mvn_package ":%{name}-server-integ" server
%mvn_package ":%{name}-server-jndi" server
%mvn_package ":%{name}-server-replication" server
%mvn_package ":%{name}-service" service
%mvn_package ":%{name}-service-builder" service

%build

# No test dep org.apache.directory.junit:junit-addons:0.1
%mvn_build -s -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles-%{name}-parent
%doc README.txt
%doc LICENSE NOTICE

%files core -f .mfiles-core
%doc LICENSE NOTICE

%files http-integration -f .mfiles-%{name}-http-integration
%doc LICENSE NOTICE

%files i18n -f .mfiles-i18n
%doc LICENSE NOTICE

%files kerberos -f .mfiles-kerberos
%doc LICENSE NOTICE

%files osgi -f .mfiles-osgi
%doc LICENSE NOTICE

%files protocols -f .mfiles-protocols
%doc LICENSE NOTICE

%files server -f .mfiles-server
%doc LICENSE NOTICE

%files service -f .mfiles-service
%doc LICENSE NOTICE

%files wrapper -f .mfiles-%{name}-wrapper
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt1_0.3.M21jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt1_0.2.M21jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt1_0.1.M21jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.7-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.7-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.7-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.7-alt1_2jpp7
- fc release

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt10_1jpp6
- fixed build

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt9_1jpp6
- use qdox instead of qdox18

* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt8_1jpp6
- fixed build w/maven3

* Tue Mar 15 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt7_1jpp6
- fixed build

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt6_1jpp6
- fixed build

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt5_1jpp6
- fixed build

* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt4_1jpp6
- build with old commons-net 1.4 (for tests)

* Fri Oct 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt3_1jpp6
- fixed site build

* Sat Sep 25 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt2_1jpp6
- fixed build with new maven 2.0.8

* Thu Sep 16 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt1_1jpp6
- new version

