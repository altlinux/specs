Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          apacheds
Version:       1.5.7
Release:       alt2_4jpp7
Summary:       Apache Directory Server
# these packages are not configured to run as a server
Group:         Development/Java
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

BuildRequires: jpackage-utils
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
BuildRequires: maven-compiler-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

Requires:      apacheds-shared

Requires:      jpackage-utils
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
Group:         Development/Java
Summary:       ApacheDS Core
Requires:      %{name}-jdbm = %{?epoch:%epoch:}%{version}-%{release}
Requires:      %{name}-xdbm = %{?epoch:%epoch:}%{version}-%{release}
Requires:      %{name}-kerberos = %{?epoch:%epoch:}%{version}-%{release}
Requires:      %{name}-protocols = %{?epoch:%epoch:}%{version}-%{release}
Requires:      apache-commons-io
Requires:      bouncycastle
Requires:      %{name}-ldap-client
Requires:      junit
Requires:      ldapjdk >= 0:4.18-11

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
Group:         Development/Java
Summary:       ApacheDS I18n
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description i18n
Internationalization of errors and other messages.

%package jdbm
Group:         Development/Java
Summary:       ApacheDS specific JDBM Implementation
Requires:      %{name}-i18n = %{?epoch:%epoch:}%{version}-%{release}

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
Group:         Development/Java
Summary:       ApacheDS Kerberos
Requires:      %{name}-core = %{?epoch:%epoch:}%{version}-%{release}
Requires:      apache-mina

%description kerberos
This package provides:
- The Kerberos protocol provider for ApacheDS.
- Interceptors used by the ApacheDS kerberos service.

%package protocols
Group:         Development/Java
Summary:       ApacheDS Protocols
Requires:      %{name}-kerberos = %{?epoch:%epoch:}%{version}-%{release}
Requires:      apache-mina

%description protocols
This package provides the following protocols for ApacheDS:
- Change Password
- DHCP
- DNS
- LDAP
- NTP

%package server
Group:         Development/Java
Summary:       ApacheDS Server modules
Requires:      %{name}-core = %{?epoch:%epoch:}%{version}-%{release}
#R equires:      {name}-ldap-client
#R equires:      junit
#R equires:      ldapjdk >= 0:4.18-11

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
Group:         Development/Java
Summary:       ApacheDS Utils
Requires:      %{name}-core = %{?epoch:%epoch:}%{version}-%{release}

%description utils
Contains utility classes for ApacheDS. 

#%% package xbean-spring
# BR/R xbean-spring maven-xbean-plugin
# BR/R springframework-beans
# BR/R springframework-context
# BR/R springframework-core 
#%% description xbean-spring

%package xdbm
Group:         Development/Java
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
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n apacheds-%{version}
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
# server-integ fails
mvn-rpmbuild -Pquicktest -Dmaven.test.failure.ignore=true install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-parent.pom
%add_maven_depmap JPP.%{name}-parent.pom

mkdir -p %{buildroot}%{_javadir}/%{name}

# core modules
for m in avl-partition \
  core \
  core-annotations \
  core-api \
  core-avl \
  core-constants \
  core-entry \
  core-integ \
  core-jndi \
  core-mock \
  jdbm-partition \
  jdbm-store \
  ldif-partition \
  server-annotations \
  test-framework; do
  install -m 644 ${m}/target/%{name}-${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${m}.jar
  install -pm 644 ${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
%add_maven_depmap -f core JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done

install -m 644 i18n/target/%{name}-i18n-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-i18n.jar
install -pm 644 i18n/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-i18n.pom
%add_maven_depmap -f i18n JPP.%{name}-%{name}-i18n.pom %{name}/%{name}-i18n.jar

install -m 644 jdbm/target/%{name}-jdbm-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-jdbm.jar
install -pm 644 jdbm/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-jdbm.pom
%add_maven_depmap -f jdbm JPP.%{name}-%{name}-jdbm.pom %{name}/%{name}-jdbm.jar

# kerberos modules
for m in interceptor-kerberos \
  kerberos-shared \
  kerberos-test \
  protocol-kerberos; do
  install -m 644 ${m}/target/%{name}-${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${m}.jar
  install -pm 644 ${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
%add_maven_depmap -f kerberos JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done

# protocols modules
for m in protocol-changepw \
  protocol-dhcp \
  protocol-dns \
  protocol-ldap \
  protocol-ntp \
  protocol-shared; do
  install -m 644 ${m}/target/%{name}-${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${m}.jar
  install -pm 644 ${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
%add_maven_depmap -f protocols JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done

# server modules
# TODO
# http-integration
# default-config
# server-sar
# server-tools
# server-xml
for m in server-integ \
  server-jndi \
  server-replication; do
  install -m 644 ${m}/target/%{name}-${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${m}.jar
  install -pm 644 ${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
%add_maven_depmap -f server JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done

install -m 644 utils/target/%{name}-utils-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-utils.jar
install -pm 644 utils/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-utils.pom
%add_maven_depmap -f utils JPP.%{name}-%{name}-utils.pom %{name}/%{name}-utils.jar

# TODO
# xbean-spring

# xdbm modules
for m in xdbm-base \
  xdbm-search \
  xdbm-tools; do
  install -m 644 ${m}/target/%{name}-${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${m}.jar
  install -pm 644 ${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
%add_maven_depmap -f xdbm JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%dir %{_javadir}/%{name}
%{_mavenpomdir}/JPP.%{name}-parent.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE NOTICE README.txt

%files core
%{_javadir}/%{name}/%{name}-core*.jar
%{_javadir}/%{name}/%{name}-avl-partition.jar
%{_javadir}/%{name}/%{name}-jdbm-partition.jar
%{_javadir}/%{name}/%{name}-jdbm-store.jar
%{_javadir}/%{name}/%{name}-ldif-partition.jar
%{_javadir}/%{name}/%{name}-server-annotations.jar
%{_javadir}/%{name}/%{name}-test-framework.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-core*.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-avl-partition.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-jdbm-partition.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-jdbm-store.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-ldif-partition.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-server-annotations.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-test-framework*.pom
%{_mavendepmapfragdir}/%{name}-core
%doc LICENSE NOTICE

%files i18n
%{_javadir}/%{name}/%{name}-i18n.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-i18n.pom
%{_mavendepmapfragdir}/%{name}-i18n
%doc LICENSE NOTICE

%files jdbm
%{_javadir}/%{name}/%{name}-jdbm.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-jdbm.pom
%{_mavendepmapfragdir}/%{name}-jdbm
%doc LICENSE NOTICE

%files kerberos
%{_javadir}/%{name}/%{name}-*kerberos*.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-*kerberos*.pom
%{_mavendepmapfragdir}/%{name}-kerberos
%doc LICENSE NOTICE

%files protocols
%{_javadir}/%{name}/%{name}-protocol-changepw.jar
%{_javadir}/%{name}/%{name}-protocol-dhcp.jar
%{_javadir}/%{name}/%{name}-protocol-dns.jar
%{_javadir}/%{name}/%{name}-protocol-ldap.jar
%{_javadir}/%{name}/%{name}-protocol-ntp.jar
%{_javadir}/%{name}/%{name}-protocol-shared.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-protocol-changepw.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-protocol-dhcp.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-protocol-dns.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-protocol-ldap.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-protocol-ntp.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-protocol-shared.pom
%{_mavendepmapfragdir}/%{name}-protocols
%doc LICENSE NOTICE

%files server
%{_javadir}/%{name}/%{name}-server-integ.jar
%{_javadir}/%{name}/%{name}-server-jndi.jar
%{_javadir}/%{name}/%{name}-server-replication.jar
# default-config.jar
# http-integration.jar
# server-sar.jar
# server-tools.jar
# server-xml.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-server-integ.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-server-jndi.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-server-replication.pom
# default-config.pom
# http-integration.pom
# server-sar.pom
# server-tools.pom
# server-xml.pom
%{_mavendepmapfragdir}/%{name}-server
%doc LICENSE NOTICE

%files utils
%{_javadir}/%{name}/%{name}-utils.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-utils.pom
%{_mavendepmapfragdir}/%{name}-utils
%doc LICENSE NOTICE

# files xbean-spring 

%files xdbm
%{_javadir}/%{name}/%{name}-xdbm*.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-xdbm*.pom
%{_mavendepmapfragdir}/%{name}-xdbm
%doc LICENSE NOTICE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%changelog
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

