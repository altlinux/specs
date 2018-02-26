BuildRequires: xpp3-minimal
BuildRequires: backport-util-concurrent
BuildRequires: docbook-xml docbook-dtds
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 3.3.2
%define name hibernate3
# Copyright (c) 2000-2010, JPackage Project
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with sources_jars
%bcond_with sources_jars
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/hibernate/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


%define reltag GA
%define base_version 3.3
%define hname Hibernate3
%define namedversion %{version}.%{reltag}

Summary:        Relational persistence and query service
Name:           hibernate3
Version:        3.3.2
Release:        alt4_1jpp6
Epoch:          1
License:        LGPLv2+
URL:            http://www.hibernate.org/
Group:          Databases
# svn -q export http://anonsvn.jboss.org/repos/hibernate/core/tags/hibernate-3.3.2.GA/ && tar cjf hibernate-3.3.2.GA.tar.bz2 hibernate-3.3.2.GA
Source0:        hibernate-3.3.2.GA.tar.bz2
Source1:        %{name}-component-info.xml
Source2:        %{name}-JBossORG-EULA.txt
Source3:        %{name}-jpp-depmap.xml
Source4:        %{name}-settings.xml
Patch0:         %{name}-pom.xml.patch
Patch1:         %{name}-core-pom.xml.patch
Patch3:		%{name}-parent-pom.xml.patch
Patch4:         hibernate3-branch_3_3_jdbc4.patch
Patch5:         hibernate3-testsuite-pom.xml.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  java-javadoc >= 1.5.0
BuildRequires:  maven-enforcer-api
BuildRequires:  maven-shared-enforcer-rule-api
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven2
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-enforcer
BuildRequires:  maven-injection-plugin
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-release
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-source
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven2-plugin-surefire-report
BuildRequires:  maven2-plugin-war
# Requires mojo-maven2-plugin-antlr due to http://jira.codehaus.org/browse/MANTLR-24
BuildRequires:  mojo-maven2-plugin-antlr

BuildRequires:  jboss-parent
BuildRequires:  javassist >= 0:3.9.0
BuildRequires:  jakarta-commons-collections >= 0:3.1
BuildRequires:  antlr >= 0:2.7.6
## xml/xstl handling
BuildRequires:  dom4j >= 0:1.6.1
BuildRequires:  jaxen >= 0:1.1
BuildRequires:  log4j >= 0:1.2.14

## Treecache
BuildRequires:  jboss-cache-core >= 3.1.0
BuildRequires:  concurrent >= 0:1.3.4
## Replication
#BuildRequires:  jgroups >= 0:2.4.6
## cache providers
BuildRequires:  ehcache >= 0:1.2.3
BuildRequires:  oscache >= 0:2.2
BuildRequires:  swarmcache
## connection pool
# FIXME BuildRequires:  c3p0 >= 0:0.9.1
BuildRequires:  c3p0
BuildRequires:  proxool >= 0:0.8.3
BuildRequires:  hsqldb
BuildRequires:  slf4j >= 1.5.6
BuildRequires:  jboss-jacc-1.1-api
BuildRequires:  jboss-jaspi-1.0-api
BuildRequires:  jboss-transaction-1.0.1-api
BuildRequires:  cglib >= 0:2.2

# The bytecode provides can be either javassist(default) or cglib
# cglib requires asm
Requires:  cglib >= 0:2.2
Requires:  objectweb-asm >= 3.1
Requires:  javassist >= 0:3.9.0
# Always required:
Requires:  jakarta-commons-collections >= 0:3.1
Requires:  jakarta-commons-logging-jboss >= 0:1.1
Requires:  antlr >= 0:2.7.6
Requires:  dom4j >= 0:1.6.1
# Required if one wants to deserialize a Configuration in order to improve
# startup performance
#Optional:  jaxen >= 0:1.1
Requires:  jboss-transaction-1.0.1-api
BuildArch:      noarch
Source44: import.info

%description
Hibernate is a powerful, ultra-high performance 
object/relational persistence and query service 
for Java. Hibernate lets you develop persistent 
objects following common Java idiom - including 
association, inheritance, polymorphism, composition 
and the Java collections framework. Extremely 
fine-grained, richly typed object models are 
possible. The Hibernate Query Language, designed 
as a "minimal" object-oriented extension to SQL, 
provides an elegant bridge between the object and 
relational worlds. Hibernate is now the most 
popular ORM solution for Java.


%if %with repolib
%package	 repolib
Summary:	 Artifacts to be uploaded to a repository library
Group:		 Development/Java

%description	 repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio
%endif

%package zip
Summary:        Zip distrubution for %{name}
Group:          Development/Java

%description zip
Zip distribution for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n hibernate-%{namedversion}

cp -p %{SOURCE4} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP


%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1
%patch3 -p0 -b .sav3
%patch4 -p0 -b .sav4
%patch5 -p0 -b .sav5

sed -i 's|__DOCS_DIR_PLACEHOLDER__|%{_javadocdir}/java|g' ./parent/pom.xml
sed -i 's|__DOCS_DIR_PLACEHOLDER__|%{_javadocdir}/java|g' ./core/pom.xml

%build

export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE3} \
        -Dmaven.test.failure.ignore=true \
        install -DdisableDistribution=true
#        -Dmaven.test.skip=true \

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE3} \
        -Dmaven.test.failure.ignore=true \
        javadoc:javadoc -DdisableDistribution=true
#        -Dmaven.test.skip=true \

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}

cp -p core/target/hibernate-core-%{version}.%{reltag}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-core-%{version}.jar
cp -p jmx/target/hibernate-jmx-%{version}.%{reltag}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-jmx-%{version}.jar
cp -p cache-jbosscache2/target/hibernate-jbosscache2-%{version}.%{reltag}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-jbosscache2-%{version}.jar
cp -p cache-ehcache/target/hibernate-ehcache-%{version}.%{reltag}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-ehcache-%{version}.jar
cp -p cache-oscache/target/hibernate-oscache-%{version}.%{reltag}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-oscache-%{version}.jar
cp -p cache-swarmcache/target/hibernate-swarmcache-%{version}.%{reltag}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-swarmcache-%{version}.jar
cp -p connection-c3p0/target/hibernate-c3p0-%{version}.%{reltag}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-c3p0-%{version}.jar
cp -p connection-proxool/target/hibernate-proxool-%{version}.%{reltag}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-proxool-%{version}.jar

%if %with sources_jars
# sources jars
cp -p core/target/hibernate-core-%{version}.%{reltag}-sources.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-core-sources-%{version}.jar
cp -p jmx/target/hibernate-jmx-%{version}.%{reltag}-sources.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-jmx-sources-%{version}.jar
cp -p cache-jbosscache2/target/hibernate-jbosscache2-%{version}.%{reltag}-sources.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-jbosscache2-sources-%{version}.jar
cp -p cache-ehcache/target/hibernate-ehcache-%{version}.%{reltag}-sources.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-ehcache-sources-%{version}.jar
cp -p cache-oscache/target/hibernate-oscache-%{version}.%{reltag}-sources.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-oscache-sources-%{version}.jar
cp -p cache-swarmcache/target/hibernate-swarmcache-%{version}.%{reltag}-sources.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-swarmcache-sources-%{version}.jar
cp -p connection-c3p0/target/hibernate-c3p0-%{version}.%{reltag}-sources.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-c3p0-sources-%{version}.jar
cp -p connection-proxool/target/hibernate-proxool-%{version}.%{reltag}-sources.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-proxool-sources-%{version}.jar
%endif

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|%{name}|hibernate|g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc
cp -p etc/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc

# pom
%add_to_maven_depmap org.hibernate hibernate-core %{namedversion} JPP %{name}-core
%add_to_maven_depmap org.hibernate hibernate-jmx %{namedversion} JPP %{name}-jmx
%add_to_maven_depmap org.hibernate hibernate-jbosscache2 %{namedversion} JPP %{name}-jbosscache2
%add_to_maven_depmap org.hibernate hibernate-c3p0 %{namedversion} JPP %{name}-c3p0
%add_to_maven_depmap org.hibernate hibernate-ehcache %{namedversion} JPP %{name}-ehcache
%add_to_maven_depmap org.hibernate hibernate-oscache %{namedversion} JPP %{name}-oscache
%add_to_maven_depmap org.hibernate hibernate-proxool %{namedversion} JPP %{name}-proxool
%add_to_maven_depmap org.hibernate hibernate-swarmcache %{namedversion} JPP %{name}-swarmcache

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%add_to_maven_depmap org.hibernate hibernate-parent %{namedversion} JPP %{name}-parent
install -m 644 parent/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
%add_to_maven_depmap org.hibernate hibernate %{namedversion} JPP %{name}
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
install -m 644 core/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-core.pom
install -m 644 jmx/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-jmx.pom
install -m 644 cache-jbosscache2/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-jbosscache2.pom
install -m 644 connection-c3p0/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-c3p0.pom
install -m 644 cache-ehcache/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-ehcache.pom
install -m 644 cache-oscache/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-oscache.pom
install -m 644 connection-proxool/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-proxool.pom
install -m 644 cache-swarmcache/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-swarmcache.pom

# javadoc
# core/target/site/apidocs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-core-%{version}
cp -pr core/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-core-%{version}
rm -rf core/target/site/apidocs
#jmx/target/site/apidocs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jmx-%{version}
cp -pr jmx/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jmx-%{version}
rm -rf jmx/target/site/apidocs
#cache-jbosscache2/target/site/apidocs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jbosscache2-%{version}
cp -pr cache-jbosscache2/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jbosscache2-%{version}
rm -rf cache-jbosscache2/target/site/apidocs
#cache-swarmcache/target/site/apidocs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-swarmcache-%{version}
cp -pr cache-swarmcache/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-swarmcache-%{version}
rm -rf cache-swarmcache/target/site/apidocs
#connection-c3p0/target/site/apidocs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-c3p0-%{version}
cp -pr connection-c3p0/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-c3p0-%{version}
rm -rf connection-c3p0/target/site/apidocs
#cache-ehcache/target/site/apidocs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-ehcache-%{version}
cp -pr cache-ehcache/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-ehcache-%{version}
rm -rf cache-ehcache/target/site/apidocs
#connection-proxool/target/site/apidocs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-proxool-%{version}
cp -pr connection-proxool/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-proxool-%{version}
rm -rf connection-proxool/target/site/apidocs
#cache-oscache/target/site/apidocs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-oscache-%{version}
cp -pr cache-oscache/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-oscache-%{version}
rm -rf cache-oscache/target/site/apidocs

(cd $RPM_BUILD_ROOT%{_javadocdir} && for doc in *-%{version}; do ln -sf ${doc} `echo $doc| sed "s|%{name}|hibernate|g"`; done)
(cd $RPM_BUILD_ROOT%{_javadocdir} && for doc in *-%{version}; do ln -sf ${doc} `echo $doc| sed "s|-%{version}||g"`; done)

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}.%{reltag}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 755 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 755 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 755 %{PATCH3} $RPM_BUILD_ROOT%{repodirsrc}

# install jars
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-core-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate-core.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-jmx-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate-jmx.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-jbosscache2-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate-jbosscache2.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-c3p0-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate-c3p0.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-ehcache-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate-ehcache.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-oscache-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate-oscache.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-proxool-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate-proxool.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-swarmcache-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate-swarmcache.jar

%if %with sources_jars
# install source jars
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-core-sources-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate-core-sources.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-jmx-sources-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate-jmx-sources.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-jbosscache2-sources-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate-jbosscache2-sources.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-c3p0-sources-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate-c3p0-sources.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-ehcache-sources-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate-ehcache-sources.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-oscache-sources-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate-oscache-sources.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-proxool-sources-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate-proxool-sources.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-swarmcache-sources-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/hibernate-swarmcache-sources.jar
%endif
%endif
# compat symlink
ln -s hibernate3-core.jar %buildroot%_javadir/hibernate3.jar

%files
%_javadir/hibernate3.jar
%doc lgpl.txt
%{_javadir}/%{name}-c3p0-%{version}.jar
%{_javadir}/%{name}-c3p0.jar
%{_javadir}/%{name}-core-%{version}.jar
%{_javadir}/%{name}-core.jar
%{_javadir}/%{name}-ehcache-%{version}.jar
%{_javadir}/%{name}-ehcache.jar
%{_javadir}/%{name}-jbosscache2-%{version}.jar
%{_javadir}/%{name}-jbosscache2.jar
%{_javadir}/%{name}-jmx-%{version}.jar
%{_javadir}/%{name}-jmx.jar
%{_javadir}/%{name}-oscache-%{version}.jar
%{_javadir}/%{name}-oscache.jar
%{_javadir}/%{name}-proxool-%{version}.jar
%{_javadir}/%{name}-proxool.jar
%{_javadir}/%{name}-swarmcache-%{version}.jar
%{_javadir}/%{name}-swarmcache.jar
%{_javadir}/hibernate-c3p0-%{version}.jar
%{_javadir}/hibernate-c3p0.jar
%{_javadir}/hibernate-core-%{version}.jar
%{_javadir}/hibernate-core.jar
%{_javadir}/hibernate-ehcache-%{version}.jar
%{_javadir}/hibernate-ehcache.jar
%{_javadir}/hibernate-jbosscache2-%{version}.jar
%{_javadir}/hibernate-jbosscache2.jar
%{_javadir}/hibernate-jmx-%{version}.jar
%{_javadir}/hibernate-jmx.jar
%{_javadir}/hibernate-oscache-%{version}.jar
%{_javadir}/hibernate-oscache.jar
%{_javadir}/hibernate-proxool-%{version}.jar
%{_javadir}/hibernate-proxool.jar
%{_javadir}/hibernate-swarmcache-%{version}.jar
%{_javadir}/hibernate-swarmcache.jar
%if %with sources_jars
%{_javadir}/%{name}-c3p0-sources-%{version}.jar
%{_javadir}/%{name}-c3p0-sources.jar
%{_javadir}/%{name}-core-sources-%{version}.jar
%{_javadir}/%{name}-core-sources.jar
%{_javadir}/%{name}-ehcache-sources-%{version}.jar
%{_javadir}/%{name}-ehcache-sources.jar
%{_javadir}/%{name}-jbosscache2-sources-%{version}.jar
%{_javadir}/%{name}-jbosscache2-sources.jar
%{_javadir}/%{name}-jmx-sources-%{version}.jar
%{_javadir}/%{name}-jmx-sources.jar
%{_javadir}/%{name}-oscache-sources-%{version}.jar
%{_javadir}/%{name}-oscache-sources.jar
%{_javadir}/%{name}-proxool-sources-%{version}.jar
%{_javadir}/%{name}-proxool-sources.jar
%{_javadir}/%{name}-swarmcache-sources-%{version}.jar
%{_javadir}/%{name}-swarmcache-sources.jar
%endif
%{_datadir}/%{name}-%{version}
%{_datadir}/maven2/poms/JPP-%{name}-c3p0.pom
%{_datadir}/maven2/poms/JPP-%{name}-core.pom
%{_datadir}/maven2/poms/JPP-%{name}-ehcache.pom
%{_datadir}/maven2/poms/JPP-%{name}-jbosscache2.pom
%{_datadir}/maven2/poms/JPP-%{name}-jmx.pom
%{_datadir}/maven2/poms/JPP-%{name}-oscache.pom
%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_datadir}/maven2/poms/JPP-%{name}-proxool.pom
%{_datadir}/maven2/poms/JPP-%{name}-swarmcache.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-ehcache
%{_javadocdir}/%{name}-ehcache-%{version}
%{_javadocdir}/%{name}-jbosscache2
%{_javadocdir}/%{name}-jbosscache2-%{version}
%{_javadocdir}/%{name}-oscache
%{_javadocdir}/%{name}-oscache-%{version}
%{_javadocdir}/%{name}-swarmcache
%{_javadocdir}/%{name}-swarmcache-%{version}
%{_javadocdir}/%{name}-c3p0
%{_javadocdir}/%{name}-c3p0-%{version}
%{_javadocdir}/%{name}-proxool
%{_javadocdir}/%{name}-proxool-%{version}
%{_javadocdir}/%{name}-core
%{_javadocdir}/%{name}-core-%{version}
%{_javadocdir}/%{name}-jmx
%{_javadocdir}/%{name}-jmx-%{version}
%{_javadocdir}/hibernate-ehcache
%{_javadocdir}/hibernate-ehcache-%{version}
%{_javadocdir}/hibernate-jbosscache2
%{_javadocdir}/hibernate-jbosscache2-%{version}
%{_javadocdir}/hibernate-oscache
%{_javadocdir}/hibernate-oscache-%{version}
%{_javadocdir}/hibernate-swarmcache
%{_javadocdir}/hibernate-swarmcache-%{version}
%{_javadocdir}/hibernate-c3p0
%{_javadocdir}/hibernate-c3p0-%{version}
%{_javadocdir}/hibernate-proxool
%{_javadocdir}/hibernate-proxool-%{version}
%{_javadocdir}/hibernate-core
%{_javadocdir}/hibernate-core-%{version}
%{_javadocdir}/hibernate-jmx
%{_javadocdir}/hibernate-jmx-%{version}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sun Jun 10 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.3.2-alt4_1jpp6
- build with maven-enforcer-api

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.3.2-alt3_1jpp6
- fixed build with new testng and xbean

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.3.2-alt2_1jpp6
- build w/java6

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.3.2-alt1_1jpp6
- new jpp release

* Fri Feb 04 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.3.2-alt1_0.7jpp6
- new version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt3_1.SP1_CP01.9jpp5
- fixed build; use cglib21

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt2_1.SP1_CP01.9jpp5
- selected java5 compiler explicitly

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt1_1.SP1_CP01.9jpp5
- new jpp release

* Fri Jun 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt1_1.SP1_CP01.1jpp5
- new version

* Thu Mar 19 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt2_0.cr2.1jpp5
- fixed build

* Fri Dec 05 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_0.cr2.1jpp5
- fixed build with java 5

* Tue Jan 22 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_0.cr2.1jpp1.7
- nobootstrap build

