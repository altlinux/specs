Patch33: apacheds10-pom-fix-build-alt.patch
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
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

%define oname apacheds

Summary:        Embeddable LDAP server
Name:           apacheds10
Version:        1.0.2
Release:        alt6_4jpp5
Epoch:          0
Group:          Development/Java
License:        Apache 2.0 License
URL:            http://directory.apache.org/subprojects/apacheds/
Source0:        %{name}-%{version}.tar.gz
# svn export http://svn.apache.org/repos/asf/directory/apacheds/tags/1.0.2/ apacheds-1.0.2

Source1:        directory-pom-1.0.4.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-settings.xml
Source4:        %{name}.init
Source5:        %{name}.sysconfig
Source6:        %{name}-bootstrapper.properties
Source7:        %{name}-log4j.properties
Source8:        %{name}-server.xml


Patch0:         %{name}-core-plugin-pom_xml.patch
Patch1:         %{name}-core-pom_xml.patch
Patch2:         %{name}-core-unit-pom_xml.patch
Patch3:         %{name}-protocol-shared-pom_xml.patch
Patch4:         %{name}-protocol-ldap-pom_xml.patch
Patch5:         %{name}-kerberos-shared-pom_xml.patch
Patch6:         %{name}-server-main-pom_xml.patch
Patch7:         %{name}-server-jndi-pom_xml.patch
Patch8:         %{name}-server-tools-pom_xml.patch
Patch9:         %{name}-server-unit-pom_xml.patch
Patch10:        %{name}-site_xml.patch
Patch11:        %{name}-server-sar-pom_xml.patch
Patch12:        %{name}-server-ssl-pom_xml.patch
Patch13:        %{name}-pom_xml.patch
Patch14:        %{name}-1.0.0-AbstractSarMojo.patch
Patch15:        %{name}-schema-archetype-pom_xml.patch
Patch16:        %{name}-testcase-archetype-pom_xml.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-default-skin
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven2-plugin-source
BuildRequires: maven-release
BuildRequires: maven-surefire-plugin
BuildRequires: mojo-maven2-plugin-antlr
BuildRequires: junit

BuildRequires: antlr
BuildRequires: apacheds-daemon10-bootstrappers
BuildRequires: apacheds-shared10-ldap
BuildRequires: apacheds-shared10-asn1
BuildRequires: apacheds-shared10-asn1-codec
BuildRequires: backport-util-concurrent
BuildRequires: bouncycastle
BuildRequires: excalibur-avalon-logkit
BuildRequires: jakarta-commons-cli
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-daemon
BuildRequires: jakarta-commons-io
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: jdbm
BuildRequires: ldapsdk
BuildRequires: mina10 >= 0:1.0.2
BuildRequires: mina10-filter-ssl >= 0:1.0.2
BuildRequires: jboss4-system
BuildRequires: jboss4-jmx
BuildRequires: nlog4j
BuildRequires: plexus-archiver
BuildRequires: plexus-utils
BuildRequires: spring-beans
BuildRequires: spring-context
BuildRequires: spring-core
BuildRequires: velocity

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

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

%description base
%{summary}.

%package core-plugin
Group:          Development/Java
Summary:        ApacheDS Core Plugin (Maven 2)
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-core-shared = %{epoch}:%{version}-%{release}
Requires: maven2 >= 0:2.0.7
Requires: antlr
Requires: excalibur-avalon-logkit
Requires: jakarta-commons-collections
Requires: velocity

%description core-plugin
A collection of tools as plugins to manage various tasks
associated with the directory server.

%package core-shared
Group:          Development/Java
Summary:        ApacheDS Core Shared
Requires: %{name}-base = %{epoch}:%{version}-%{release}

%description core-shared
Shared classes between the core plugin and the core to 
prevent cyclic dependencies since the core uses the core
plugin.

%package core
Group:          Development/Java
Summary:        ApacheDS Core
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-core-shared = %{epoch}:%{version}-%{release}
Requires: jakarta-commons-collections
Requires: jakarta-commons-daemon
Requires: jakarta-commons-lang
Requires: jdbm
Requires: nlog4j

%description core
Server's core contains the JNDI provider, interceptors, 
schema, and database subsystems. The core is the heart 
of the server without protocols enabled.

%package core-unit
Group:          Development/Java
Summary:        ApacheDS Core Unit
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: antlr
Requires: apacheds-shared-asn1
Requires: jakarta-commons-io
Requires: junit
Requires: nlog4j

%description core-unit
Integration and performance tests.

%package kerberos-shared
Group:          Development/Java
Summary:        ApacheDS Protocol Kerberos Shared
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-protocol-shared = %{epoch}:%{version}-%{release}
Requires: apacheds-shared-asn1
Requires: bouncycastle
Requires: mina10 >= 0:1.0.2
Requires: mina10-filter-ssl >= 0:1.0.2

%description kerberos-shared
The Kerberos protocol provider for ApacheDS.

%package protocol-changepw
Group:          Development/Java
Summary:        ApacheDS Protocol Change Password
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-kerberos-shared = %{epoch}:%{version}-%{release}
Requires: nlog4j

%description protocol-changepw
The Change Password protocol provider for ApacheDS.

%package protocol-dhcp
Group:          Development/Java
Summary:        ApacheDS Protocol Dhcp
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-protocol-shared = %{epoch}:%{version}-%{release}
Requires: mina10 >= 0:1.0.2
Requires: nlog4j

%description protocol-dhcp
The DHCP protocol provider for ApacheDS.

%package protocol-dns
Group:          Development/Java
Summary:        ApacheDS Protocol Dns
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-protocol-shared = %{epoch}:%{version}-%{release}
Requires: mina10 >= 0:1.0.2
Requires: nlog4j

%description protocol-dns
The DNS protocol provider for ApacheDS.

%package protocol-kerberos
Group:          Development/Java
Summary:        ApacheDS Protocol Kerberos
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-kerberos-shared = %{epoch}:%{version}-%{release}
Requires: nlog4j

%description protocol-kerberos
The Kerberos protocol provider for ApacheDS.

%package protocol-ldap
Group:          Development/Java
Summary:        ApacheDS Protocol Ldap
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: apacheds-shared-asn1
Requires: apacheds-shared-asn1-codec
Requires: mina10 >= 0:1.0.2
Requires: nlog4j

%description protocol-ldap
The LDAPv3 protocol provider for ApacheDS.

%package protocol-ntp
Group:          Development/Java
Summary:        ApacheDS Protocol Ntp
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-protocol-shared = %{epoch}:%{version}-%{release}
Requires: mina10 >= 0:1.0.2
Requires: nlog4j

%description protocol-ntp
The NTP protocol provider for ApacheDS.

%package protocol-shared
Group:          Development/Java
Summary:        ApacheDS Protocol Shared
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: junit
Requires: nlog4j

%description protocol-shared
Shared library that is used by all protocol providers 
in ApacheDS.

%package sar-plugin
Group:          Development/Java
Summary:        ApacheDS Server Sar Maven Plugin
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: maven2 >= 0:2.0.7
Requires: plexus-utils

%description sar-plugin
%{summary}.

%package schema-archetype
Group:          Development/Java
Summary:        ApacheDS Schema Archetype
Requires: %{name}-base = %{epoch}:%{version}-%{release}

%description schema-archetype
%{summary}.

%package server-jndi
Group:          Development/Java
Summary:        ApacheDS Server JNDI
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-protocol-changepw = %{epoch}:%{version}-%{release}
Requires: %{name}-protocol-kerberos = %{epoch}:%{version}-%{release}
Requires: %{name}-protocol-ldap = %{epoch}:%{version}-%{release}
Requires: %{name}-protocol-ntp = %{epoch}:%{version}-%{release}
Requires: backport-util-concurrent
Requires: nlog4j

%description server-jndi
The JNDI provider which launches the core and associated
network services: Changepw, Kerberos, LDAP, and NTP if
all are configured. By default only LDAP is configured
to startup.

%package server-main
Group:          Development/Java
Summary:        ApacheDS Server Main
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-server-jndi = %{epoch}:%{version}-%{release}
Requires: apacheds-daemon10-bootstrappers
#Requires:       jakarta-commons-daemon-jsvc
Requires: jakarta-commons-logging
Requires: nlog4j
Requires: spring-beans
Requires: spring-context
Requires: spring-core
Requires(post): %{name}-core-shared = %{epoch}:%{version}-%{release}
Requires(post): %{name}-core = %{epoch}:%{version}-%{release}
Requires(post): %{name}-kerberos-shared = %{epoch}:%{version}-%{release}
Requires(post): %{name}-protocol-changepw = %{epoch}:%{version}-%{release}
Requires(post): %{name}-protocol-kerberos = %{epoch}:%{version}-%{release}
Requires(post): %{name}-protocol-ldap = %{epoch}:%{version}-%{release}
Requires(post): %{name}-protocol-shared = %{epoch}:%{version}-%{release}
Requires(post): %{name}-server-jndi = %{epoch}:%{version}-%{release}
Requires(post): %{name}-server-ssl = %{epoch}:%{version}-%{release}
Requires(post): antlr
Requires(post): apacheds-shared-asn1-codec
Requires(post): apacheds-shared-asn1
Requires(post): apacheds-shared-ldap
Requires(post): backport-util-concurrent
Requires(post): bouncycastle
Requires(post): jakarta-commons-collections
Requires(post): jakarta-commons-logging
Requires(post): jdbm
Requires(post): mina10
Requires(post): mina10-filter-ssl
Requires(post): spring-beans
Requires(post): spring-context
Requires(post): spring-core

%description server-main
%{summary}.

%package server-sar
Group:          Development/Java
Summary:        ApacheDS Server Sar (JBoss 3.x)
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-server-ssl = %{epoch}:%{version}-%{release}
Requires: apacheds-daemon10-bootstrappers
Requires: jakarta-commons-logging
Requires: jboss4-system
Requires: jboss4-jmx
Requires: nlog4j
Requires: spring-beans
Requires: spring-context
Requires: spring-core

%description server-sar
A server archive file for ApacheDS to run within a 
JBoss 3.x instance.

%package server-ssl
Group:          Development/Java
Summary:        ApacheDS Server SSL
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-server-jndi = %{epoch}:%{version}-%{release}
Requires: nlog4j
Requires: mina10 >= 0:1.0.2

%description server-ssl
An SSL support module for LDAPS with ApacheDS.

%package server-tools
Group:          Development/Java
Summary:        ApacheDS Server Tools
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-server-main = %{epoch}:%{version}-%{release}
Requires: apacheds-daemon10-bootstrappers
Requires: jakarta-commons-cli
Requires: jakarta-commons-lang

%description server-tools
Contained within this executable jar are various 
commandline utilities for ApacheDS.

%package server-unit
Group:          Development/Java
Summary:        ApacheDS Server Unit
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-core-unit = %{epoch}:%{version}-%{release}
Requires: %{name}-server-jndi = %{epoch}:%{version}-%{release}
Requires: backport-util-concurrent
Requires: junit
Requires: ldapsdk
Requires: nlog4j

%description server-unit
Unit testing framework for ApacheDS Server JNDI Provider.

%package testcase-archetype
Group:          Development/Java
Summary:        ApacheDS Testcase Archetype
Requires: %{name}-base = %{epoch}:%{version}-%{release}

%description testcase-archetype
%{summary}.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}

%description javadoc
%{summary}.

%package manual
Group:          Development/Documentation
Summary:        Documents for %{name}

%description manual
%{summary}.

%prep
%setup -q -n %{oname}-%{version}

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
#%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5
#%patch6 -b .sav6
%patch7 -b .sav7
#%patch8 -b .sav8
#%patch9 -b .sav9
#%patch10 -b .sav10
%patch11 -b .sav11
#%patch12 -b .sav12
%patch13 -b .sav13
%patch14 -b .sav14
%patch15 -b .sav15
%patch16 -b .sav16

%patch33

%build
mkdir -p .m2/JPP/maven2/default_poms
cp %{SOURCE1} \
.m2/JPP/maven2/default_poms/org.apache.directory-build.pom

cp sar-plugin/pom.xml \
.m2/JPP/maven2/default_poms/org.apache.directory.server-apacheds-sar-plugin.pom

mkdir -p .m2/JPP/lcrypto-jdk14/131
pushd .m2/JPP/
ln -sf $(build-classpath bcprov) lcrypto-jdk14.jar
popd

# maven208 hacks
install -Dm644 %{SOURCE1} .m2/org/apache/directory/build/1.0.5/build-1.0.5.pom
install -Dm644 sar-plugin/pom.xml .m2/org/apache/directory/server/apacheds-sar-plugin/2.0.8/apacheds-sar-plugin-2.0.8.pom

#export JAVA_HOME=%{_jvmdir}/java-1.5.0
export MAVEN_OPTS="-Xmx512m"


#pushd sar-plugin
#mvn-jpp -e \
#	-Dmaven.compile.target=1.5 \
#	-Dmaven.javadoc.source=1.5 \
#        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
#        install
#popd
#mkdir -p .m2/org.apache.directory.server
#cp sar-plugin/target/apacheds-sar-plugin-%{version}.jar \
#    .m2/org.apache.directory.server/apacheds-sar-plugin.jar
# maven208 hacks
#mvn-jpp -e \
#        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
#    	install:install-file -DgroupId=org.apache.directory.server -DartifactId=apacheds-sar-plugin -Dversion=2.0.8 -Dpackaging=maven-plugin -Dfile=sar-plugin/target/apacheds-sar-plugin-%{version}.jar
#echo end maven208 hacks

mvn-jpp -e \
        -P release \
	-Dmaven.compile.target=1.5 \
	-Dmaven.javadoc.source=1.5 \
	-Dmaven.test.skip=true \
	-Dmaven.test.skip.exec=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        install
#pushd server-sar
#mvn-jpp -e \
#	-Dmaven.compile.target=1.5 \
#	-Dmaven.javadoc.source=1.5 \
#        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
#        install
#popd
mvn-jpp -e \
        -P release \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
	-Dmaven.compile.target=1.5 \
	-Dmaven.javadoc.source=1.5 \
        javadoc:javadoc
%if 0
mvn-jpp -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
	-Dmaven.compile.target=1.5 \
	-Dmaven.javadoc.source=1.5 \
        -N \
        site
%endif

%install

# system
install -d -m 0755 $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d
install -m 0755 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/%{name}
install -d -m 0755 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}

# home
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
ln -sf /usr/sbin/jsvc apacheds
ln -sf $(build-classpath apacheds-daemon10-bootstrappers) bootstrapper.jar
ln -sf $(build-classpath nlog4j) logger.jar
ln -sf $(build-classpath commons-daemon) daemon.jar
popd
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}/conf
install -m 0755 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/%{name}/conf/bootstrapper.properties
install -m 0755 %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/%{name}/conf/log4j.properties
install -m 0755 %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/%{name}/conf/server.xml

install -d -m 0755 $RPM_BUILD_ROOT%{_var}/lib/%{name}/lib/ext

install -d -m 0755 $RPM_BUILD_ROOT/var/lib/%{name}
ln -sf /var/lib/%{name} $RPM_BUILD_ROOT%{_datadir}/%{name}/var
install -d -m 0755 $RPM_BUILD_ROOT%{_var}/log/%{name}
ln -sf %{_var}/log/%{name} $RPM_BUILD_ROOT/var/lib/%{name}/log
install -d -m 0755 $RPM_BUILD_ROOT/var/lib/%{name}/run
ln -sf %{_var}/tmp $RPM_BUILD_ROOT/var/lib/%{name}/tmp
install -d -m 0755 $RPM_BUILD_ROOT/var/lib/%{name}/partitions
ln -sf %{_var}/lib/%{name}/lib $RPM_BUILD_ROOT%{_datadir}/%{name}/lib

# bin
#BUILD/apacheds-1.0.0/schema-archetype/apacheds-schema-archetype.sh
#BUILD/apacheds-1.0.0/server-main/apacheds.sh
#BUILD/apacheds-1.0.0/testcase-archetype/apacheds-testcase-archetype.sh

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 core-plugin/target/%{oname}-core-plugin-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-plugin-%{version}.jar
install -m 644 core-plugin/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-core-plugin.pom
%add_to_maven_depmap org.apache.directory.server apacheds-core-plugin %{version} JPP/%{name} core-plugin

install -m 644 core-shared/target/%{oname}-core-shared-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-shared-%{version}.jar
install -m 644 core-shared/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-core-shared.pom
%add_to_maven_depmap org.apache.directory.server apacheds-core-shared %{version} JPP/%{name} core-shared

install -m 644 core/target/%{oname}-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-%{version}.jar
install -m 644 core/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-core.pom
%add_to_maven_depmap org.apache.directory.server apacheds-core %{version} JPP/%{name} core

install -m 644 core-unit/target/%{oname}-core-unit-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-unit-%{version}.jar
install -m 644 core-unit/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-core-unit.pom
%add_to_maven_depmap org.apache.directory.server apacheds-core-unit %{version} JPP/%{name} core-unit

install -m 644 kerberos-shared/target/%{oname}-kerberos-shared-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/kerberos-shared-%{version}.jar
install -m 644 kerberos-shared/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-kerberos-shared.pom
%add_to_maven_depmap org.apache.directory.server apacheds-kerberos-shared %{version} JPP/%{name} kerberos-shared

install -m 644 protocol-changepw/target/%{oname}-protocol-changepw-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/protocol-changepw-%{version}.jar
install -m 644 protocol-changepw/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-protocol-changepw.pom
%add_to_maven_depmap org.apache.directory.server apacheds-protocol-changepw %{version} JPP/%{name} protocol-changepw

install -m 644 protocol-dhcp/target/%{oname}-protocol-dhcp-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/protocol-dhcp-%{version}.jar
install -m 644 protocol-dhcp/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-protocol-dhcp.pom
%add_to_maven_depmap org.apache.directory.server apacheds-protocol-dhcp %{version} JPP/%{name} protocol-dhcp

install -m 644 protocol-dns/target/%{oname}-protocol-dns-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/protocol-dns-%{version}.jar
install -m 644 protocol-dns/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-protocol-dns.pom
%add_to_maven_depmap org.apache.directory.server apacheds-protocol-dns %{version} JPP/%{name} protocol-dns

install -m 644 protocol-kerberos/target/%{oname}-protocol-kerberos-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/protocol-kerberos-%{version}.jar
install -m 644 protocol-kerberos/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-protocol-kerberos.pom
%add_to_maven_depmap org.apache.directory.server apacheds-protocol-kerberos %{version} JPP/%{name} protocol-kerberos

install -m 644 protocol-ldap/target/%{oname}-protocol-ldap-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/protocol-ldap-%{version}.jar
install -m 644 protocol-ldap/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-protocol-ldap.pom
%add_to_maven_depmap org.apache.directory.server apacheds-protocol-ldap %{version} JPP/%{name} protocol-ldap

install -m 644 protocol-ntp/target/%{oname}-protocol-ntp-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/protocol-ntp-%{version}.jar
install -m 644 protocol-ntp/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-protocol-ntp.pom
%add_to_maven_depmap org.apache.directory.server apacheds-protocol-ntp %{version} JPP/%{name} protocol-ntp

install -m 644 protocol-shared/target/%{oname}-protocol-shared-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/protocol-shared-%{version}.jar
install -m 644 protocol-shared/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-protocol-shared.pom
%add_to_maven_depmap org.apache.directory.server apacheds-protocol-shared %{version} JPP/%{name} protocol-shared

#install -m 644 sar-plugin/target/%{oname}-sar-plugin-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/sar-plugin-%{version}.jar
#install -m 644 sar-plugin/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-sar-plugin.pom
#%add_to_maven_depmap org.apache.directory.server apacheds-sar-plugin %{version} JPP/%{name} sar-plugin

install -m 644 schema-archetype/target/%{oname}-schema-archetype-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/schema-archetype-%{version}.jar
install -m 644 schema-archetype/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-schema-archetype.pom
%add_to_maven_depmap org.apache.directory.server apacheds-schema-archetype %{version} JPP/%{name} schema-archetype

install -m 644 server-jndi/target/%{oname}-server-jndi-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/server-jndi-%{version}.jar
install -m 644 server-jndi/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-server-jndi.pom
%add_to_maven_depmap org.apache.directory.server apacheds-server-jndi %{version} JPP/%{name} server-jndi

install -m 644 server-main/target/%{oname}-server-main-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/server-main-%{version}.jar
install -m 644 server-main/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-server-main.pom
%add_to_maven_depmap org.apache.directory.server apacheds-server-main %{version} JPP/%{name} server-main

#install -m 644 server-sar/target/%{oname}-server-sar-%{version}.sar $RPM_BUILD_ROOT%{_javadir}/%{name}/server-sar-%{version}.sar
#install -m 644 server-sar/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-server-sar.pom
#%add_to_maven_depmap org.apache.directory.server apacheds-server-sar %{version} JPP/%{name} server-sar

install -m 644 server-ssl/target/%{oname}-server-ssl-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/server-ssl-%{version}.jar
install -m 644 server-ssl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-server-ssl.pom
%add_to_maven_depmap org.apache.directory.server apacheds-server-ssl %{version} JPP/%{name} server-ssl

install -m 644 server-tools/target/%{oname}-server-tools-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/server-tools-%{version}.jar
install -m 644 server-tools/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-server-tools.pom
%add_to_maven_depmap org.apache.directory.server apacheds-server-tools %{version} JPP/%{name} server-tools

install -m 644 server-unit/target/%{oname}-server-unit-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/server-unit-%{version}.jar
install -m 644 server-unit/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-server-unit.pom
%add_to_maven_depmap org.apache.directory.server apacheds-server-unit %{version} JPP/%{name} server-unit

install -m 644 testcase-archetype/target/%{oname}-testcase-archetype-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/testcase-archetype-%{version}.jar
install -m 644 testcase-archetype/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-testcase-archetype.pom
%add_to_maven_depmap org.apache.directory.server apacheds-testcase-archetype %{version} JPP/%{name} testcase-archetype

install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-build.pom
%add_to_maven_depmap org.apache.directory.server build %{version} JPP/%{name} build

install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-parent-build.pom
%add_to_maven_depmap org.apache.directory build %{version} JPP/%{name} parent-build

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -sf %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} #ghost
rm -rf target/site/apidocs

# manual
install -d -m 0755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#cp -pr target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%pre server-main
%{_sbindir}/groupadd -r apacheds 2> /dev/null || :
%{_sbindir}/useradd -r -c "ApacheDS" -g apacheds \
    -d %{_datadir}/%{name} apacheds 2> /dev/null || :

%post server-main
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
apacheds10/core-shared \
apacheds10/core \
apacheds10/kerberos-shared \
apacheds10/protocol-changepw \
apacheds10/protocol-kerberos \
apacheds10/protocol-ldap \
apacheds10/protocol-shared \
apacheds10/server-jndi \
apacheds10/server-main \
apacheds10/server-ssl \
apacheds-shared-asn1-codec \
apacheds-shared-asn1 \
apacheds-shared-ldap \
backport-util-concurrent \
commons-collections \
commons-logging \
jdbm \
mina10/core \
mina10/filter-ssl \
spring/beans \
spring/context \
spring/core \
2>&1


%files base
%dir %{_javadir}/%{name}
%{_datadir}/maven2/poms
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%endif

%files core-plugin
%doc core-plugin/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/core-plugin*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/core-plugin-%{version}.jar.*
%endif

%files core-shared
%doc core-shared/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/core-shared*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/core-shared-%{version}.jar.*
%endif

%files core
%doc core/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/core-%{version}.jar
%{_javadir}/%{name}/core.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/core-%{version}.jar.*
%endif

%files core-unit
%doc core-unit/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/core-unit*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/core-unit-%{version}.jar.*
%endif

%files kerberos-shared
%doc kerberos-shared/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/kerberos-shared*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/kerberos-shared-%{version}.jar.*
%endif

%files protocol-changepw
%doc protocol-changepw/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/protocol-changepw*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/protocol-changepw-%{version}.jar.*
%endif

%files protocol-dhcp
%doc protocol-dhcp/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/protocol-dhcp*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/protocol-dhcp-%{version}.jar.*
%endif

%files protocol-dns
%doc protocol-dns/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/protocol-dns*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/protocol-dns-%{version}.jar.*
%endif

%files protocol-kerberos
%doc protocol-kerberos/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/protocol-kerberos*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/protocol-kerberos-%{version}.jar.*
%endif

%files protocol-ldap
%doc protocol-ldap/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/protocol-ldap*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/protocol-ldap-%{version}.jar.*
%endif

%files protocol-ntp
%doc protocol-ntp/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/protocol-ntp*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/protocol-ntp-%{version}.jar.*
%endif

%files protocol-shared
%doc protocol-shared/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/protocol-shared*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/protocol-shared-%{version}.jar.*
%endif

#%files sar-plugin
#%doc sar-plugin/src/main/resources/META-INF/LICENSE.txt
#%{_javadir}/%{name}/sar-plugin*.jar
#%if %{gcj_support}
#%{_libdir}/gcj/%{name}/sar-plugin-%{version}.jar.*
#%endif

%files schema-archetype
%doc schema-archetype/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/schema-archetype*.jar

%files server-jndi
%doc server-jndi/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/server-jndi*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/server-jndi-%{version}.jar.*
%endif

%files server-main
%doc server-main/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/server-main*.jar
%attr(755,root,root) %{_sysconfdir}/rc.d/init.d/%{name}
%{_sysconfdir}/sysconfig/%{name}
%attr(-,apacheds,apacheds) %{_datadir}/%{name}
%attr(-,apacheds,apacheds) /var/lib/%{name}
%attr(-,apacheds,apacheds) %{_var}/log/%{name}
%attr(-,apacheds,apacheds) %{_var}/lib/%{name}

%if %{gcj_support}
%{_libdir}/gcj/%{name}/server-main-%{version}.jar.*
%endif

#%files server-sar
#%doc server-sar/src/main/resources/META-INF/LICENSE.txt
#%{_javadir}/%{name}/server-sar*.sar

%files server-ssl
%doc server-ssl/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/server-ssl*.jar

%files server-tools
%doc server-tools/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/server-tools*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/server-tools-%{version}.jar.*
%endif

%files server-unit
%doc server-unit/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/server-unit*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/server-unit-%{version}.jar.*
%endif

%files testcase-archetype
%doc testcase-archetype/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}/testcase-archetype*.jar

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

#files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Fri May 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt6_4jpp5
- fixed build

* Sat Sep 25 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt5_4jpp5
- fixed build with new maven 2.0.8

* Fri Sep 17 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt4_4jpp5
- fixed build

* Sun Mar 15 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt3_4jpp5
- fixes in build-jar-repository

* Wed Mar 11 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_4jpp5
- fixed user

* Fri Mar 06 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_4jpp5
- first build

