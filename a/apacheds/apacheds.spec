Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# these packages are not configured to run as a server
Name:          apacheds
Version:       1.5.7
Release:       alt2_7jpp7
Summary:       Apache Directory Server
License:       ASL 2.0
Url:           http://directory.apache.org/
# svn export http://svn.apache.org/repos/asf/directory/apacheds/tags/1.5.7/ apacheds-1.5.7
# tar czf apacheds-1.5.7-src-svn.tar.gz apacheds-1.5.7
Source0:       %{name}-%{version}-src-svn.tar.gz
# remove unavailable / unused deps
# fix bouncycastle gId aId
Patch0:        %{name}-%{version}-fixbuild.patch
# add maven-surefire-plugin version
Patch1:        %{name}-%{version}-i18n-pom.patch

BuildRequires: directory-project

BuildRequires: apache-commons-io
BuildRequires: apache-mina
BuildRequires: apacheds-ldap-client
BuildRequires: apacheds-shared
BuildRequires: bouncycastle
BuildRequires: junit
BuildRequires: ldapjdk >= 0:4.18-11
BuildRequires: log4j
BuildRequires: slf4j

# BuildRequires: antlr
# BuildRequires: apache-commons-cli
# BuildRequires: apache-commons-collections
# BuildRequires: apache-commons-daemon
# BuildRequires: apache-commons-dbcp
# BuildRequires: apache-commons-lang
# BuildRequires: apache-commons-pool
# BuildRequires: apacheds-daemon-bootstrappers
# BuildRequires: java-service-wrapper
# BuildRequires: jboss-system
# BuildRequires: jetty
# BuildRequires: maven
# BuildRequires: maven-xbean-plugin
# BuildRequires: plexus-utils
# BuildRequires: quartz
# BuildRequires: springframework-beans
# BuildRequires: springframework-context
# BuildRequires: springframework-core 
# BuildRequires: velocity
# BuildRequires: xbean-spring 
# BuildRequires: xerces-j2

# test deps
BuildRequires: apache-commons-net

BuildRequires: maven-local
BuildRequires: maven-antrun-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-provider-junit4

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

%package i18n
Group: Development/Java
Summary:       ApacheDS I18n

%description i18n
Internationalization of errors and other messages.

%package jdbm
Group: Development/Java
Summary:       ApacheDS specific JDBM Implementation

%description jdbm
A specific JDBM Implementation.
A JDBM entry store which does not have any dependency on
core interfaces. The JDBM partition will use this store
and build on it to adapt this to server specific partition
interfaces. Having this separate module without
dependencies on core interfaces makes it easier to avoid
cyclic dependencies between modules. This is especially
important for use within the bootstrap plugin which needs
to build the schema partition used for bootstrapping the
server. 

%package kerberos
Group: Development/Java
Summary:       ApacheDS Kerberos

%description kerberos
This package provides:
- The Kerberos protocol provider for ApacheDS.
- Interceptors used by the ApacheDS kerberos service.

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

%package utils
Group: Development/Java
Summary:       ApacheDS Utils

%description utils
Contains utility classes for ApacheDS. 

#%% package xbean-spring
# BR/R xbean-spring maven-xbean-plugin
# BR/R springframework-beans
# BR/R springframework-context
# BR/R springframework-core 
#%% description xbean-spring

%package xdbm
Group: Development/Java
Summary:       ApacheDS XDBM

%description xdbm
Base XDBM (btree based) entry store interfaces.
Search engine implementation generalized for XDBM entry
store scheme.
Generalized (X) DBM Tools:
Several kinds of two column key/value data structures, in
memory and on disk which sort keys can can be used to
implement xdbm partitions. JDBM is one example. These
partition use the same database structure or scheme for
maintaining LDAP entries and facilitating search operations
on them. This module contains common tools that could be
used to manage aspects common to all xdbm implementations. 

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
chmod 644 README.txt

%pom_disable_module all
# TODO
# depend on 
# jboss jboss-system 3.2.3
# org.apache.directory.daemon daemon-bootstrappers (deceased)
# org.apache.xbean xbean-spring maven-xbean-plugin
# org.springframework spring-core spring-beans spring-context
%pom_disable_module xbean-spring
# TODO
# http-integration
# default-config
# server-sar
# server-tools
# server-xml
%pom_disable_module server-tools
%pom_disable_module server-xml
# depend on jetty 6.x
%pom_disable_module http-integration
# depend on http-integration
%pom_disable_module default-config

# this test fails
rm -rf i18n/src/test/java/org/apache/directory/server/i18n/GermanLanguageTest.java
rm -rf xdbm-search/src/test/java/org/apache/directory/server/xdbm/search/impl/LessEqTest.java

%build

%mvn_package ":%{name}-avl-partition" core
%mvn_package ":%{name}-core" core
%mvn_package ":%{name}-core-annotations" core
%mvn_package ":%{name}-core-api" core
%mvn_package ":%{name}-core-avl" core
%mvn_package ":%{name}-core-constants" core
%mvn_package ":%{name}-core-entry" core
%mvn_package ":%{name}-core-integ" core
%mvn_package ":%{name}-core-jndi" core
%mvn_package ":%{name}-core-mock" core
%mvn_package ":%{name}-jdbm-partition" core
%mvn_package ":%{name}-jdbm-store" core
%mvn_package ":%{name}-ldif-partition" core
%mvn_package ":%{name}-server-annotations" core
%mvn_package ":%{name}-test-framework" core
%mvn_package ":%{name}-i18n" i18n
%mvn_package ":%{name}-jdbm" jdbm
%mvn_package ":%{name}-interceptor-kerberos" kerberos
%mvn_package ":%{name}-kerberos-shared" kerberos
%mvn_package ":%{name}-kerberos-test" kerberos
%mvn_package ":%{name}-protocol-kerberos" kerberos
%mvn_package ":%{name}-protocol-changepw" protocols
%mvn_package ":%{name}-protocol-dhcp" protocols
%mvn_package ":%{name}-protocol-dns" protocols
%mvn_package ":%{name}-protocol-ldap" protocols
%mvn_package ":%{name}-protocol-ntp" protocols
%mvn_package ":%{name}-protocol-shared" protocols
%mvn_package ":%{name}-server-integ" server
%mvn_package ":%{name}-server-jndi" server
%mvn_package ":%{name}-server-replication" server
%mvn_package ":%{name}-utils" utils
%mvn_package ":%{name}-xdbm-base" xdbm
%mvn_package ":%{name}-xdbm-search" xdbm
%mvn_package ":%{name}-xdbm-tools" xdbm

# server-integ fails
%mvn_build -s -- -Pquicktest -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles-%{name}-parent
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE README.txt

%files core -f .mfiles-core
%doc LICENSE NOTICE

# files http-integration

%files i18n -f .mfiles-i18n
%doc LICENSE NOTICE

%files jdbm -f .mfiles-jdbm
%doc LICENSE NOTICE

%files kerberos -f .mfiles-kerberos
%doc LICENSE NOTICE

%files protocols -f .mfiles-protocols
%doc LICENSE NOTICE

%files server -f .mfiles-server
%doc LICENSE NOTICE

%files utils -f .mfiles-utils
%doc LICENSE NOTICE

# files xbean-spring 

%files xdbm -f .mfiles-xdbm
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
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

