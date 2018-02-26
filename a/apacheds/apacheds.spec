BuildRequires: spring2-context spring2-beans
Packager: Igor Vlasenko <viy@altlinux.ru>
%define _with_java5 1
BuildRequires: maven-remote-resources-plugin
BuildRequires: /proc maven-surefire-provider-junit4 jakarta-commons-net14 nlog4j
BuildRequires: jpackage-compat
# Copyright (c) 2000-2009, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define gcj_support 0


Summary:        Embeddable LDAP server
Name:           apacheds
Version:        1.5.4
Release:        alt10_1jpp6
Epoch:          0
Group:          Development/Java
License:        Apache 2.0 License
URL:            http://directory.apache.org/apacheds/1.5/
Source0:        %{name}-%{version}.tar.gz
# svn export http://svn.apache.org/repos/asf/directory/apacheds/tags/1.5.4/ apacheds-1.5.4

Source1:        directory-project-12.tar.gz
# svn export http://svn.apache.org/repos/asf/directory/project/tags/12/ directory-project-12

Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-settings.xml
Source4:        apache-jar-resource-bundle-1.3.jar
Source5:        %{name}.init
Source6:        %{name}.sysconfig
Source7:        %{name}-bootstrapper.properties
Source8:        %{name}-log4j.properties
Source9:        %{name}-server.xml


Patch0:         directory-project-12-pom.patch
Patch1:         apacheds-pom.patch
Patch2:         apacheds-schema-bootstrap-pom.patch
Patch3:         apacheds-schema-registry-pom.patch
Patch4:         apacheds-core-plugin-pom.patch
Patch5:         apacheds-core-entry-pom.patch
Patch6:         apacheds-bootstrap-plugin-pom.patch
Patch7:         apacheds-core-pom.patch
Patch8:         apacheds-all-pom.patch
Patch9:         apacheds-schema-extras-pom.patch
Patch10:        apacheds-jdbm-store-pom.patch
Patch11:	apacheds-1.5.4-alt-pom-use-maven2-plugin-shade.patch
Patch33:	apacheds-1.5.4-alt-pom-slf4j16.patch

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: junit44
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-checkstyle
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-pmd
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-remote-resources
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven2-plugin-source
BuildRequires: maven2-plugin-stage
BuildRequires: maven2-default-skin
BuildRequires: maven-jxr
BuildRequires: maven-release
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-report-plugin
BuildRequires: geronimo-genesis
BuildRequires: mojo-maven2-plugin-build-helper
BuildRequires: mojo-maven2-plugin-cobertura
BuildRequires: mojo-maven2-plugin-rat
BuildRequires: maven2-plugin-shade
BuildRequires: mojo-maven2-plugin-taglist

BuildRequires: antlr
BuildRequires: apacheds-daemon-bootstrappers
BuildRequires: apacheds-shared-ldap
BuildRequires: apacheds-shared-asn1
BuildRequires: apacheds-shared-asn1-codec
BuildRequires: apacheds-shared-bouncycastle-reduced
BuildRequires: apacheds-shared-ldap
BuildRequires: derby
BuildRequires: dnsjava
BuildRequires: excalibur-avalon-logkit
BuildRequires: jakarta-commons-cli
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-io
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: jug
BuildRequires: ldapsdk
BuildRequires: mina11
BuildRequires: mina11-filter-ssl
BuildRequires: plexus-archiver
BuildRequires: plexus-utils
BuildRequires: qdox
BuildRequires: quartz16
BuildRequires: spring2-beans
BuildRequires: spring2-context
BuildRequires: spring2-core
BuildRequires: tanukiwrapper
BuildRequires: velocity
BuildRequires: xbean
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%description
The Apache Directory Server is an embeddable LDAP server implemented
in pure Java. It has several features that make it unique amoung 
LDAP servers. These features are described below:
* Designed as an LDAP and X.500 experimentation platform. Plugable
  components and subsystems make ApacheDS extremely modular and ideal
  for experiments with various aspects of the LDAP protocol.
* The server's frontend is completely separable from its backend 
  and vice-versa making it very flexible for implementing virtual
  directories, proxy servers and gateways to X.500.
* Several backends can be implemented and plugged into the server's
  partition nexus. The server supports a BTree based partition out of
  the box but any backing store can be used to implement a partition
  so long as it conforms to interfaces.
* The server exposes aspects of administration via a special system
  backend. LDAP can be used to manage these concerns through the 
  system naming context at ou=system.
* Java based triggers and stored procedures are being implemented.
* Both the backend subsystem and the frontend are separable and
  independently embeddable.
* The server contains a server side JNDI LDAP provider as the facade
  for the entire backend subsystem. JNDI operations are directly
  translated by this provider into operations against the nexus and
  the target partitions storing server entries.
* The server will use JNDI as the data access API for stored procedures.
  This will make stored procedures functional within and outside of
  the server without requiring recompilation.
* The server's networking code, MINA, Multipurpose Infrastructure for
  Network Applications was designed for pluggable protocol providers,
  of all sorts and not just LDAP. MINA gives ApacheDS the ability to
  handle large amounts of concurrency.
* The server uses the Snickers tools and APIs for ASN.1 BER encoding
  and decoding. These tools are designed for a very small encoding
  and decoding footprint as well as for use in non-blocking servers.


%package base
Group:          Development/Java
Summary:        ApacheDS install base
Obsoletes:      %{name}-sar-plugin < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-server-sar < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-server-ssl < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-testcase-archetype < %{epoch}:%{version}-%{release}

%description base
%{summary}.

%package all
Group:          Development/Java
Summary:        ApacheDS in one uberjar

%description all
%{summary}.

%package bootstrap
Group:          Development/Java
Summary:        ApacheDS Bootstrap Subsystem
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-jdbm = %{epoch}:%{version}-%{release}
Requires: %{name}-schema = %{epoch}:%{version}-%{release}
Requires: %{name}-utils = %{epoch}:%{version}-%{release}
Requires: antlr
Requires: maven2
Requires: slf4j

%description bootstrap
The apacheds-bootstrap-partition jar file that contains a 
pre-loaded partition with schema information.  This schema 
partition will mount off of the ou=schema namingContext. 
This artifact contains the db files for this partition. 
It must be used with the apacheds-bootstrap-extract jar 
which contains the classes to install these files.

The apacheds-bootstrap plugin pre-loads a set of schema 
objects into a special fixed schema partition within the 
server.  It uses the bootstrap schema objects to do this 
at build time.  The schema partition files created are 
then packaged using the jar plugin to become what is 
known as the bootstrap partition jar.




%package core
Group:          Development/Java
Summary:        ApacheDS Core Subsystem
Obsoletes:      %{name}-core-plugin < %{epoch}:%{version}-%{release}
Provides:       %{name}-core-plugin = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-core-shared < %{epoch}:%{version}-%{release}
Provides:       %{name}-core-shared = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-core-unit < %{epoch}:%{version}-%{release}
Provides:       %{name}-core-unit = %{epoch}:%{version}-%{release}
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-bootstrap = %{epoch}:%{version}-%{release}
Requires: %{name}-jdbm = %{epoch}:%{version}-%{release}
Requires: %{name}-schema = %{epoch}:%{version}-%{release}
Requires: %{name}-utils = %{epoch}:%{version}-%{release}
Requires: %{name}-xdbm = %{epoch}:%{version}-%{release}
Requires: antlr
Requires: apacheds-shared-bouncycastle-reduced
Requires: apacheds-shared-ldap
Requires: excalibur-avalon-logkit
Requires: jakarta-commons-collections
Requires: jakarta-commons-io
Requires: jakarta-commons-lang
Requires: junit44
Requires: maven2
Requires: velocity

%description core
- Server's core contains the JNDI provider, interceptors, 
  schema, and database subsystems.  The core is the heart 
  of the server without protocols enabled.
- A linked in memory AVL tree implementation with Cursor.
- Contains classes that store interfaces with various 
  constants in ApacheDS.
- Cursor interfaces used by the server core.
- Server side LDAP entry classes.
- Integration testing framework for Apache Directory Server.
- Contains a JNDI provider implementation which wraps the 
  core so existing applications based on JNDI can use the 
  server embedded transparently.  Remote and local runtime 
  operations will appear and feel exactly the same with a 
  performance boost when local.  All operations via this 
  JNDI provider bypass the LDAP stack to perform ooerations 
  directly on the ApacheDS core.
- A collection of tools as plugins to manage various tasks 
  associated with the directory server.
- Shared classes between the core plugin and the core to 
  prevent cyclic dependencies since the core uses the core 
  plugin.
- A linked in memory splay tree implementation with Cursor.
- Core unit tests.

%package kerberos
Group:          Development/Java
Summary:        ApacheDS Kerberos 
Obsoletes:      %{name}-kerberos-shared < %{epoch}:%{version}-%{release}
Provides:       %{name}-kerberos-shared = %{epoch}:%{version}-%{release}
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-bootstrap = %{epoch}:%{version}-%{release}
Requires: %{name}-protocol-shared = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: mina11

%description kerberos
- The Kerberos protocol provider for ApacheDS.
- Interceptors used by the ApacheDS kerberos service.

%package jdbm
Group:          Development/Java
Summary:        ApacheDS Jdbm
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-schema = %{epoch}:%{version}-%{release}
Requires: %{name}-xdbm = %{epoch}:%{version}-%{release}

%description jdbm
- A specific JDBM Implementation.
- A JDBM entry store which does not have any dependency on 
  core interfaces.  The JDBM partition will use this store 
  and build on it to adapt this to server specific partition
  interfaces.  Having this separate module without 
  dependencies on core interfaces makes it easier to avoid 
  cyclic dependencies between modules.  This is especially
  important for use within the bootstrap plugin which needs 
  to build the schema partition used for bootstrapping the 
  server.

%package mitosis
Group:          Development/Java
Summary:        ApacheDS Replication
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: derby
Requires: jakarta-commons-collections
Requires: jakarta-commons-dbcp
Requires: jakarta-commons-io
Requires: jakarta-commons-lang
Requires: jakarta-commons-pool
Requires: jug
Requires: mina11
Requires: quartz16

%description mitosis
Mitosis is the multi-master replications service included 
into Apache Directory Server.


%package protocol-changepw
Group:          Development/Java
Summary:        ApacheDS Protocol Change Password
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-kerberos = %{epoch}:%{version}-%{release}

%description protocol-changepw
The Change Password protocol provider for ApacheDS.

%package protocol-dhcp
Group:          Development/Java
Summary:        ApacheDS Protocol Dhcp
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-protocol-shared = %{epoch}:%{version}-%{release}
Requires: mina11

%description protocol-dhcp
The DHCP protocol provider for ApacheDS.

%package protocol-dns
Group:          Development/Java
Summary:        ApacheDS Protocol Dns
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-protocol-shared = %{epoch}:%{version}-%{release}

%description protocol-dns
The DNS protocol provider for ApacheDS.

%package protocol-kerberos
Group:          Development/Java
Summary:        ApacheDS Protocol Kerberos
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-kerberos = %{epoch}:%{version}-%{release}

%description protocol-kerberos
The Kerberos protocol provider for ApacheDS.

%package protocol-ldap
Group:          Development/Java
Summary:        ApacheDS Protocol Ldap
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-kerberos = %{epoch}:%{version}-%{release}
Requires: apacheds-shared-asn1-codec
Requires: apacheds-shared-ldap
Requires: mina11
Requires: mina11-filter-ssl

%description protocol-ldap
The LDAPv3 protocol provider for ApacheDS.

%package protocol-ntp
Group:          Development/Java
Summary:        ApacheDS Protocol Ntp
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-protocol-shared = %{epoch}:%{version}-%{release}
Requires: mina11

%description protocol-ntp
The NTP protocol provider for ApacheDS.

%package protocol-shared
Group:          Development/Java
Summary:        ApacheDS Protocol Shared
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: mina11

%description protocol-shared
Shared library that is used by all protocol providers 
in ApacheDS.

%package schema
Group:          Development/Java
Summary:        ApacheDS Schema Subsystem
Obsoletes:      %{name}-schema-archetype < %{epoch}:%{version}-%{release}
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-jdbm = %{epoch}:%{version}-%{release}
Requires: apacheds-shared-asn1
Requires: apacheds-shared-ldap
Requires: jakarta-commons-collections

%description schema
- The minimal set of schemas needed to bootstrap the 
  server's special schema partition which is used to 
  store all the schemas for the server.
- A set of additional bootstrap schemas beyond the 
  essential set.
- Interfaces for schema entity registries are contained 
  here.

%package server
Group:          Development/Java
Summary:        ApacheDS Server modules
Obsoletes:      %{name}-server-jndi < %{epoch}:%{version}-%{release}
Provides:       %{name}-server-jndi = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-server-main < %{epoch}:%{version}-%{release}
Provides:       %{name}-server-main = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-server-tools < %{epoch}:%{version}-%{release}
Provides:       %{name}-server-tools = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-server-unit < %{epoch}:%{version}-%{release}
Provides:       %{name}-server-unit = %{epoch}:%{version}-%{release}
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-bootstrap = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-kerberos = %{epoch}:%{version}-%{release}
Requires: %{name}-protocol-ldap = %{epoch}:%{version}-%{release}
Requires: %{name}-schema = %{epoch}:%{version}-%{release}
Requires: apacheds-daemon-bootstrappers
Requires: dnsjava
Requires: jakarta-commons-cli
Requires: jakarta-commons-io
Requires: jakarta-commons-lang
Requires: junit44
Requires: ldapsdk
Requires: slf4j
Requires: spring2-beans
Requires: spring2-context
Requires: spring2-core
Requires: tanukiwrapper
Requires: xbean

%description server
- Integration testing framework for Apache Directory Server.
- The JNDI provider which launches the core and associated
  network services: Changepw, Kerberos, LDAP, and NTP if
  all are configured. By default only LDAP is configured
  to startup.
- A multi-master replication service for replicating 
  information across ApacheDS instances.  This service is 
  modeled as an interceptor.
- Various commandline utilities for apacheds.
- Unit testing framework for ApacheDS Server JNDI Provider.
- A single authoritative server.xml file.

%package utils
Group:          Development/Java
Summary:        ApacheDS Utils
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}

%description utils
Contains utility classes for ApacheDS.

%package xbean-spring
Group:          Development/Java
Summary:        ApacheDS XBean Spring
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: xbean
Requires: qdox
Requires: spring2-beans
Requires: spring2-context
Requires: spring2-core

%description xbean-spring
%{summary}.

%package xdbm
Group:          Development/Java
Summary:        ApacheDS XDBM
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-schema = %{epoch}:%{version}-%{release}
Requires: jakarta-commons-io

%description xdbm
- Base XDBM (btree based) entry store interfaces.
- Search engine implementation generalized for XDBM entry 
  store scheme.
- Generalized (X) DBM Tools:
  Several kinds of two column key/value data structures, in
  memory and on  disk which sort keys can can be used to 
  implement xdbm partitions.  JDBM is one example.  These 
  partition use the same database structure or scheme for 
  maintaining LDAP entries and facilitating search operations 
  on them.  This module contains common tools that could be 
  used to manage aspects  common to all xdbm implementations.


%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Group:          Development/Documentation
Summary:        Documents for %{name}
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n %{name}-%{version}
gzip -dc %{SOURCE1} | tar xf -

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5
%patch6 -b .sav6
%patch7 -b .sav7
%patch8 -b .sav8
%patch9 -b .sav9
%patch10 -b .sav10
%patch11 -p1
%patch33 -p0

%build
cp %{SOURCE3} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP


export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository
export MAVEN_OPTS="-Xmx512m"

mkdir -p $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/
cp directory-project-12/pom.xml \
   $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/org.apache.directory.project-project.pom
cp bootstrap-plugin/pom.xml \
    $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/org.apache.directory.server-apacheds-bootstrap-plugin.pom

mkdir -p $MAVEN_REPO_LOCAL/org.apache/
cp %{SOURCE4} $MAVEN_REPO_LOCAL/org.apache/apache-jar-resource-bundle.jar

mkdir -p $MAVEN_REPO_LOCAL/org.apache.directory.server/
ln -sf $(pwd)/bootstrap-plugin/target/apacheds-bootstrap-plugin-%{version}.jar \
    $MAVEN_REPO_LOCAL/org.apache.directory.server/apacheds-bootstrap-plugin.jar 

# maven 2.0.8 hacks
install -Dm644 directory-project-12/pom.xml $MAVEN_REPO_LOCAL/org/apache/directory/project/project/12/project-12.pom
install -Dm644 %{SOURCE4} $MAVEN_REPO_LOCAL/org/apache/apache-jar-resource-bundle/1.4/apache-jar-resource-bundle-1.4.jar
install -Dm644 bootstrap-plugin/pom.xml $MAVEN_REPO_LOCAL/org/apache/directory/server/apacheds-bootstrap-plugin/2.0.8/apacheds-bootstrap-plugin-2.0.8.pom
mkdir -p $MAVEN_REPO_LOCAL/org/apache/directory/server/apacheds-bootstrap-plugin/2.0.8/
ln -sf $(pwd)/bootstrap-plugin/target/apacheds-bootstrap-plugin-%{version}.jar \
    $MAVEN_REPO_LOCAL/org/apache/directory/server/apacheds-bootstrap-plugin/2.0.8/apacheds-bootstrap-plugin-2.0.8.jar
# end maven 2.0.8 hooks

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $M2SETTINGS \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $M2SETTINGS \
        -Daggregate=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        javadoc:javadoc site ||:


%install

# system
install -d -m 0755 $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d
install -m 0755 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/%{name}
install -d -m 0755 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 0644 %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}

# home
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
ln -sf /usr/sbin/jsvc apacheds
ln -sf $(build-classpath apacheds-daemon-bootstrappers) bootstrapper.jar
ln -sf $(build-classpath nlog4j) logger.jar
ln -sf $(build-classpath commons-daemon) daemon.jar
popd
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}/conf
install -m 0755 %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/%{name}/conf/bootstrapper.properties
install -m 0755 %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/%{name}/conf/log4j.properties
install -m 0755 %{SOURCE9} $RPM_BUILD_ROOT%{_datadir}/%{name}/conf/server.xml

install -d -m 0755 $RPM_BUILD_ROOT%{_var}/lib/%{name}/lib/ext
build-jar-repository $RPM_BUILD_ROOT%{_var}/lib/%{name}/lib \
antlr \
apacheds-shared-asn1-codec \
apacheds-shared-asn1 \
apacheds-shared-bouncycastle-reduced \
apacheds-shared-ldap \
backport-util-concurrent \
commons-collections \
commons-logging \
mina11/core \
mina11/filter-ssl \
spring2/beans \
spring2/context \
spring2/core \

install -d -m 0755 $RPM_BUILD_ROOT%{_var}/lib/%{name}
ln -sf %{_var}/lib/%{name} $RPM_BUILD_ROOT%{_datadir}/%{name}/var
install -d -m 0755 $RPM_BUILD_ROOT%{_var}/log/%{name}
ln -sf %{_var}/log/%{name} $RPM_BUILD_ROOT%{_var}/lib/%{name}/log
install -d -m 0755 $RPM_BUILD_ROOT%{_var}/lib/%{name}/run
ln -sf %{_var}/tmp $RPM_BUILD_ROOT%{_var}/lib/%{name}/tmp
install -d -m 0755 $RPM_BUILD_ROOT%{_var}/lib/%{name}/partitions
ln -sf %{_var}/lib/%{name}/lib $RPM_BUILD_ROOT%{_datadir}/%{name}/lib


# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}


install -m 644 all/target/%{name}-all-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/all-%{version}.jar
install -m 644 bootstrap-extract/target/%{name}-bootstrap-extract-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/bootstrap-extract-%{version}.jar
install -m 644 bootstrap-partition/target/%{name}-bootstrap-partition-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/bootstrap-partition-%{version}.jar
install -m 644 bootstrap-plugin/target/%{name}-bootstrap-plugin-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/bootstrap-plugin-%{version}.jar

install -m 644 core-avl/target/%{name}-core-avl-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-avl-%{version}.jar
install -m 644 core-constants/target/%{name}-core-constants-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-constants-%{version}.jar
install -m 644 core-cursor/target/%{name}-core-cursor-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-cursor-%{version}.jar
install -m 644 core-entry/target/%{name}-core-entry-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-entry-%{version}.jar
install -m 644 core-integ/target/%{name}-core-integ-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-integ-%{version}.jar
install -m 644 core-jndi/target/%{name}-core-jndi-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-jndi-%{version}.jar
install -m 644 core-plugin/target/%{name}-core-plugin-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-plugin-%{version}.jar
install -m 644 core-shared/target/%{name}-core-shared-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-shared-%{version}.jar
install -m 644 core-splay/target/%{name}-core-splay-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-splay-%{version}.jar
install -m 644 core/target/%{name}-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-%{version}.jar
install -m 644 core-unit/target/%{name}-core-unit-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-unit-%{version}.jar

install -m 644 interceptor-kerberos/target/%{name}-interceptor-kerberos-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/interceptor-kerberos-%{version}.jar
install -m 644 jdbm-store/target/%{name}-jdbm-store-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jdbm-store-%{version}.jar
install -m 644 jdbm/target/%{name}-jdbm-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jdbm-%{version}.jar
install -m 644 kerberos-shared/target/%{name}-kerberos-shared-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/kerberos-shared-%{version}.jar
install -m 644 mitosis/target/mitosis-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/mitosis-%{version}.jar

install -m 644 protocol-changepw/target/%{name}-protocol-changepw-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/protocol-changepw-%{version}.jar
install -m 644 protocol-dhcp/target/%{name}-protocol-dhcp-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/protocol-dhcp-%{version}.jar
install -m 644 protocol-dns/target/%{name}-protocol-dns-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/protocol-dns-%{version}.jar
install -m 644 protocol-kerberos/target/%{name}-protocol-kerberos-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/protocol-kerberos-%{version}.jar
install -m 644 protocol-ldap/target/%{name}-protocol-ldap-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/protocol-ldap-%{version}.jar
install -m 644 protocol-ntp/target/%{name}-protocol-ntp-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/protocol-ntp-%{version}.jar
install -m 644 protocol-shared/target/%{name}-protocol-shared-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/protocol-shared-%{version}.jar

install -m 644 schema-bootstrap/target/%{name}-schema-bootstrap-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/schema-bootstrap-%{version}.jar
install -m 644 schema-extras/target/%{name}-schema-extras-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/schema-extras-%{version}.jar
install -m 644 schema-registries/target/%{name}-schema-registries-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/schema-registries-%{version}.jar

install -m 644 server-integ/target/%{name}-server-integ-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/server-integ-%{version}.jar
install -m 644 server-jndi/target/%{name}-server-jndi-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/server-jndi-%{version}.jar
install -m 644 server-replication/target/%{name}-server-replication-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/server-replication-%{version}.jar
install -m 644 server-tools/target/%{name}-server-tools-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/server-tools-%{version}.jar
install -m 644 server-unit/target/%{name}-server-unit-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/server-unit-%{version}.jar
install -m 644 server-xml/target/%{name}-server-xml-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/server-xml-%{version}.jar
install -m 644 utils/target/%{name}-utils-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/utils-%{version}.jar
install -m 644 xbean-spring/target/%{name}-xbean-spring-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xbean-spring-%{version}.jar

install -m 644 xdbm-base/target/%{name}-xdbm-base-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xdbm-base-%{version}.jar
install -m 644 xdbm-search/target/%{name}-xdbm-search-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xdbm-search-%{version}.jar
install -m 644 xdbm-tools/target/%{name}-xdbm-tools-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xdbm-tools-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version} ||:
ln -sf %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} #ghost
rm -rf target/site/apidocs

# manual
install -d -m 0755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} ||:

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%post server
# install apacheds (but don't activate)
/sbin/chkconfig --add %{name}
# Create automated links - since all needed extensions may not have been
# installed for this jvm output is muted
# Try to set a sensible jvm
unset JAVA_HOME
[ -r %{_sysconfdir}/sysconfig/%{name} ] && . %{_sysconfdir}/sysconfig/%{name}
[ -z "$JAVA_HOME" ] && [ -r %{_sysconfdir}/java/java.conf ] && \
    . %{_sysconfdir}/java/java.conf
[ -z "$JAVA_HOME" ] && JAVA_HOME=%{_jvmdir}/java
# Remove old automated symlinks
for repository in %{_var}/lib/%{name}/lib ; do
    find $repository -name '\[*\]*.jar' -not -type d | xargs rm -f
done
build-jar-repository %{_var}/lib/%{name}/lib \
antlr \
apacheds/core-shared \
apacheds/core \
apacheds/kerberos-shared \
apacheds/protocol-changepw \
apacheds/protocol-kerberos \
apacheds/protocol-ldap \
apacheds/protocol-shared \
apacheds/server-jndi \
apacheds-shared-asn1-codec \
apacheds-shared-asn1 \
apacheds-shared-bouncycastle-reduced \
apacheds-shared-ldap \
backport-util-concurrent \
commons-collections \
commons-logging \
mina11/core \
mina11/filter-ssl \
spring2/beans \
spring2/context \
spring2/core \
2>&1


%files base
%dir %{_javadir}/%{name}
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%endif

%files all
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%{_javadir}/%{name}/all*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/all*-%{version}.jar.*
%endif

%files bootstrap
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%{_javadir}/%{name}/bootstrap*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/bootstrap*-%{version}.jar.*
%endif

%files core
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%{_javadir}/%{name}/core*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/core-plugin-%{version}.jar.*
%endif

%files jdbm
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%{_javadir}/%{name}/jdbm*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/jdbm*-%{version}.jar.*
%endif

%files kerberos
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%{_javadir}/%{name}/kerberos-shared*.jar
%{_javadir}/%{name}/interceptor-kerberos*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/kerberos-shared-%{version}.jar.*
%{_libdir}/gcj/%{name}/interceptor-kerberos-%{version}.jar.*
%endif

%files mitosis
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%{_javadir}/%{name}/mitosis*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/mitosis*-%{version}.jar.*
%endif

%files protocol-changepw
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%{_javadir}/%{name}/protocol-changepw*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/protocol-changepw-%{version}.jar.*
%endif

%files protocol-dhcp
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%{_javadir}/%{name}/protocol-dhcp*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/protocol-dhcp-%{version}.jar.*
%endif

%files protocol-dns
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%{_javadir}/%{name}/protocol-dns*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/protocol-dns-%{version}.jar.*
%endif

%files protocol-kerberos
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%{_javadir}/%{name}/protocol-kerberos*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/protocol-kerberos-%{version}.jar.*
%endif

%files protocol-ldap
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%{_javadir}/%{name}/protocol-ldap*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/protocol-ldap-%{version}.jar.*
%endif

%files protocol-ntp
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%{_javadir}/%{name}/protocol-ntp*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/protocol-ntp-%{version}.jar.*
%endif

%files protocol-shared
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%{_javadir}/%{name}/protocol-shared*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/protocol-shared-%{version}.jar.*
%endif

%files schema
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%{_javadir}/%{name}/schema*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/schema*-%{version}.jar.*
%endif

%files server
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%{_javadir}/%{name}/server*.jar
%attr(755,root,root) %{_sysconfdir}/rc.d/init.d/%{name}
%{_sysconfdir}/sysconfig/%{name}
#%attr(-,apacheds,apacheds) %dir %{_datadir}/%{name}
%attr(-,apacheds,apacheds) %{_datadir}/%{name}
#%{_datadir}/%{name}/bin
#%{_datadir}/%{name}/conf
#%{_datadir}/%{name}/lib
#%{_datadir}/%{name}/var
%attr(-,apacheds,apacheds) %{_var}/lib/%{name}
%attr(-,apacheds,apacheds) %{_var}/log/%{name}
%attr(-,apacheds,apacheds) %{_var}/lib/%{name}
%if %{gcj_support}
%{_libdir}/gcj/%{name}/server-main-%{version}.jar.*
%endif

%files utils
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%{_javadir}/%{name}/utils*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/utils*-%{version}.jar.*
%endif

%files xbean-spring
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%{_javadir}/%{name}/xbean-spring*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/xbean-spring*-%{version}.jar.*
%endif

%files xdbm
%doc target/maven-shared-archive-resources/META-INF/LICENSE
%{_javadir}/%{name}/xdbm*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/xdbm*-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

#%files manual
#%doc %{_docdir}/%{name}-%{version}

%changelog
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

