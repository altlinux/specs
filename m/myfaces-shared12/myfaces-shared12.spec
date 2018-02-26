BuildRequires: qdox
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat testng maven-surefire-provider-testng

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

%define parent  myfaces

Summary:        MyFaces shared 12
Name:           myfaces-shared12
Version:        3.0.4
Release:        alt4_1jpp5
Epoch:          0
License:        Apache Software License 2.0
URL:            http://myfaces.apache.org/
Group:          Development/Java
Source0:        myfaces-shared-3.0.4.tar.gz
# svn export http://svn.apache.org/repos/asf/myfaces/shared/tags/3_0_4/ myfaces-shared-3.0.4

Source1:        myfaces-shared12-jpp-depmap.xml
Source2:        myfaces-shared12-settings.xml
Source3:        myfaces-master-5.pom

Patch0:         myfaces-shared12-pom.patch
Patch1:         myfaces-shared12-impl-pom.patch
Patch2:         myfaces-shared12-tomahawk-pom.patch

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-dependency
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin

BuildRequires: cargo
BuildRequires: easymock-classextension2
BuildRequires: httpunit
BuildRequires: jakarta-cactus
BuildRequires: junit
BuildRequires: shale-test

BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-el
BuildRequires: jakarta-commons-logging
BuildRequires: jsp_2_1_api
BuildRequires: myfaces-core12-api
BuildRequires: portlet_1_0_api
BuildRequires: servlet_2_3_api


Requires: jakarta-commons-codec
Requires: jakarta-commons-el
Requires: jakarta-commons-logging
Requires: jsp_2_1_api
Requires: myfaces-core12-api
Requires: portlet_1_0_api
Requires: servlet_2_3_api
BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

%description
The MyFaces Shared project provides base classes for usage 
in both the MyFaces Implementation and the MyFaces Tomahawk 
components.
Note: When bound to myfaces-impl or myfaces-tomahawk the 
shared classes get another namespace. That is:
myfaces-impl: org.apache.myfaces.shared_impl.* 
   instead of org.apache.myfaces.shared.*
myfaces-tomahawk: org.apache.myfaces.shared_tomahawk.* 
       instead of org.apache.myfaces.shared.*</description>

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%prep
%setup -q -n myfaces-shared-%{version}

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2

# alt; aspectj 1.5.4
sed -i 's,<groupId>aspectj</groupId>,<groupId>org.aspectj</groupId>,' pom.xml

%build
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
mkdir -p ${MAVEN_REPO_LOCAL}/JPP/maven2/default_poms/
#cp %{SOURCE3} ${MAVEN_REPO_LOCAL}/JPP/maven2/default_poms/org.apache.myfaces.maven-myfaces-master.pom
cp %{SOURCE3} ${MAVEN_REPO_LOCAL}/JPP/maven2/default_poms/org.apache.myfaces-myfaces.pom
install -Dm644 %{SOURCE3} ${MAVEN_REPO_LOCAL}/org/apache/myfaces/myfaces/5/myfaces-5.pom
install -Dm644 %{SOURCE3} ${MAVEN_REPO_LOCAL}/org/apache/myfaces/myfaces/6/myfaces-6.pom

mvn-jpp -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install:install-file -DgroupId=org.testng -DartifactId=testng -Dversion=5.1 -Dclassifier=jdk15 -Dpackaging=jar -Dfile=/usr/share/java/testng-jdk15.jar

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc


%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{parent}

install -m 644 core/target/myfaces-shared-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/shared12-core-%{version}.jar
install -m 644 shared-impl/target/myfaces-shared-impl-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/shared12-impl-%{version}.jar
install -m 644 shared-tomahawk/target/myfaces-shared-tomahawk-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/shared12-tomahawk-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir}/%{parent} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-shared12-project.pom
%add_to_maven_depmap org.apache.myfaces.shared myfaces-shared-project %{version} JPP/%{parent} shared12-project
install -m 644 core/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-shared12-core.pom
%add_to_maven_depmap org.apache.myfaces.shared myfaces-shared-core %{version} JPP/%{parent} shared12-core
install -m 644 shared-impl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-shared12-impl.pom
%add_to_maven_depmap org.apache.myfaces.shared myfaces-shared-impl %{version} JPP/%{parent} shared12-impl
install -m 644 shared-tomahawk/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-shared12-tomahawk.pom
%add_to_maven_depmap org.apache.myfaces.shared myfaces-shared-tomahawk %{version} JPP/%{parent} shared12-tomahawk

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/impl
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/tomahawk
cp -pr core/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core
cp -pr shared-impl/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/impl
cp -pr shared-tomahawk/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/tomahawk
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc core/src/main/resources/META-INF/LICENSE.txt
%dir %{_javadir}/%{parent}
%{_javadir}/%{parent}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Apr 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt4_1jpp5
- fixed build with new plexus-containers

* Sun Jan 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt3_1jpp5
- adapted pom for new aspectj

* Mon Sep 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt2_1jpp5
- fixed build with new maven 2.0.8

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt1_1jpp5
- new jpp release

