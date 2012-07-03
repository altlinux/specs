Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat ognl
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


Summary:        Spring LDAP
Name:           spring-ldap
Version:        1.2.1
Release:        alt4_1jpp5
Epoch:          0
Group:          Development/Java
License:        Apache License 2.0
URL:            http://www.springframework.org/ldap
Source0:        spring-ldap-1.2.1.tar.gz
# svn export http://springframework.svn.sourceforge.net/svnroot/springframework/spring-ldap/tags/spring-ldap-1.2.1/

Source1:        %{name}-jpp-depmap.xml
Source2:        %{name}-settings.xml

Patch0:         spring-ldap-pom.patch
Patch1:         spring-ldap-spring-ldap-article-pom.patch
Patch2:         spring-ldap-spring-ldap-person-pom.patch
Patch3:         spring-ldap-spring-ldap-pom.patch
Patch4:         spring-ldap-spring-ldap-tiger-pom.patch
Patch33:	spring-ldap-1.2.1-alt-pom-javacc5.patch


BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: junit
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin
BuildRequires: mojo-maven2-plugin-javacc

BuildRequires: acegi-security
BuildRequires: chainedoptions
BuildRequires: ldapbp
BuildRequires: spring-dao
BuildRequires: spring-webflow
BuildRequires: spring2-web
BuildRequires: spring2-webmvc
BuildRequires: apacheds10-core
BuildRequires: apacheds10-core-shared
BuildRequires: apacheds10-kerberos-shared
BuildRequires: apacheds10-protocol-changepw
BuildRequires: apacheds10-protocol-kerberos
BuildRequires: apacheds10-protocol-ldap
BuildRequires: apacheds10-protocol-shared
BuildRequires: apacheds10-server-jndi
BuildRequires: apacheds10-server-main
BuildRequires: apacheds10-server-ssl
BuildRequires: apacheds-shared-asn1
BuildRequires: apacheds-shared-ldap
BuildRequires: apacheds-shared-asn1-codec
BuildRequires: gsbase
BuildRequires: mina10
BuildRequires: mina10-filter-ssl



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
Spring LDAP is a Java library for simplifying LDAP
operations, based on the pattern of Spring's JdbcTemplate. 
The framework relieves the user of common chores, such as 
looking up and closing contexts, looping through results, 
encoding/decoding values and filters, and more.
The LdapTemplate class encapsulates all the plumbing work 
involved in traditional LDAP programming, such as creating 
a DirContext, looping through NamingEnumerations, handling 
exceptions and cleaning up resources. This leaves the 
programmer to handle the important stuff - where to find 
data (DNs and Filters) and what do do with it (map to and 
from domain objects, bind, modify, unbind, etc.), in the 
same way that JdbcTemplate relieves the programmer of all 
but the actual SQL and how the data maps to the domain 
model.
In addition to this, Spring LDAP provides transaction 
support, a pooling library, exception translation from 
NamingExceptions to a mirrored unchecked Exception hierarchy, 
as well as several utilities for working with filters, LDAP 
paths and Attributes.
Spring LDAP requires J2SE 1.4 or higher to run, and works 
with Spring Framework 2.0.x as well as 2.5.x. J2SE 1.4 or 
higher is required for building the release binaries from 
sources. Release 1.2.1 also requires an installation of 
JavaCC 4.0 when building from source. That is not necessary 
for release 1.3.x, since it uses Maven2, which handles all 
such dependencies behind the scenes.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}

%description javadoc
%{summary}.

%prep
%setup -q 
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
%patch33 -b .sav33 -p1

%build
export LANG=en_US.ISO8859-1
cp %{SOURCE2} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        -Daggregate=true \
        javadoc:javadoc

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
%add_to_maven_depmap org.springframework.ldap %{name} %{version} JPP %{name}-parent

install -m 644 %{name}/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.springframework %{name} %{version} JPP %{name}
install -m 644 %{name}/target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

install -m 644 %{name}-tiger/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-tiger.pom
%add_to_maven_depmap org.springframework %{name}-tiger %{version} JPP %{name}-tiger
install -m 644 %{name}-tiger/target/%{name}-tiger-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tiger-%{version}.jar

install -m 644 %{name}-person/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-person-sample.pom
%add_to_maven_depmap org.springframework %{name}-person-sample %{version} JPP %{name}-person-sample
install -m 644 %{name}-person/target/%{name}-person-sample-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-person-sample-%{version}.jar

install -m 644 %{name}-article/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-person-article.pom
%add_to_maven_depmap org.springframework %{name}-person-article %{version} JPP %{name}-person-article
install -m 644 %{name}-article/target/%{name}-person-article-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-person-article-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)


# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt4_1jpp5
- fixed build with java 7

* Fri Mar 18 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt3_1jpp5
- fixed build with new javacc5

* Sun Sep 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt2_1jpp5
- fixed build with new maven 2.0.8

* Sun Mar 15 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_1jpp5
- maven 2.0.7 build

* Sat Mar 14 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt0.1jpp
maven 2.0.7 bootstrap

