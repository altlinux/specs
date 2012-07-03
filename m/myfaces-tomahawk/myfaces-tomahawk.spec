Patch34: myfaces-tomahawk-alt-maven3.patch
BuildRequires: mojo-parent
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.5.0-compat
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

Summary:        MyFaces Tomahawk
Name:           myfaces-tomahawk
Version:        1.1.6
Release:        alt7_1jpp5
Epoch:          0
License:        Apache Software License 2.0
URL:            http://myfaces.apache.org/
Group:          Development/Java
Source0:        myfaces-tomahawk-1.1.6.tar.gz
# svn export http://svn.apache.org/repos/asf/myfaces/tomahawk/tags/1_1_6/ myfaces-tomahawk-1.1.6

Source1:        myfaces-tomahawk-jpp-depmap.xml
Source2:        myfaces-tomahawk-settings.xml
Source3:        myfaces-master-5.pom

Patch0:         myfaces-tomahawk-dependency-maven-plugin.patch
Patch1:         myfaces-tomahawk-core-pom.patch
Patch2:         myfaces-tomahawk-no-maven-taglib-plugin.patch
Patch3:         myfaces-tomahawk-examples-simple-pom.patch
Patch4:         myfaces-tomahawk-sandbox-core-pom.patch
Patch5:         myfaces-tomahawk-ExcelExportPhaseListener.patch
Patch6:         myfaces-tomahawk-RequestParameterResponseWrapper.patch
Patch7:         myfaces-tomahawk-sandbox15-core-pom.patch

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: junit
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-changelog
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-dependency
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven2-plugin-war
BuildRequires: cargo0-maven2-plugin
BuildRequires: maven-jxr
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-report-plugin
BuildRequires: mojo-maven2-plugin-build-helper
BuildRequires: mojo-maven2-plugin-taglist
BuildRequires: mojo-maven2-plugin-xslt

BuildRequires: aspectj
BuildRequires: bcel
BuildRequires: cargo0
BuildRequires: cglib
BuildRequires: easymock
BuildRequires: easymock-classextension
BuildRequires: el_1_0_api
BuildRequires: jakarta-cactus
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-el
BuildRequires: jakarta-commons-fileupload
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-validator
BuildRequires: jakarta-oro
BuildRequires: jakarta-poi
BuildRequires: jakarta-taglibs-standard
BuildRequires: jmock
BuildRequires: jpa_1_0B_api
BuildRequires: jsp_2_0_api
BuildRequires: myfaces-core11-api
BuildRequires: myfaces-core11-impl
BuildRequires: myfaces-shared11
BuildRequires: portlet_1_0_api
BuildRequires: servlet_2_3_api
BuildRequires: shale-test
BuildRequires: spring2-all
BuildRequires: struts >= 0:1.3.8
BuildRequires: struts-tiles
BuildRequires: xpp3-minimal

Requires: bcel
Requires: cglib
Requires: el_1_0_api
Requires: jakarta-commons-codec
Requires: jakarta-commons-collections
Requires: jakarta-commons-el
Requires: jakarta-commons-fileupload
Requires: jakarta-commons-lang
Requires: jakarta-commons-logging
Requires: jakarta-commons-validator
Requires: jakarta-oro
Requires: jakarta-taglibs-standard
Requires: jpa_1_0B_api
Requires: jsp_2_0_api
Requires: myfaces-core11-api
Requires: myfaces-shared11
Requires: portlet_1_0_api
Requires: servlet_2_3_api
Requires: struts >= 0:1.3.8
Requires: struts-tiles

BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Patch33: myfaces-tomahawk-1.1.6-alt-bcel52.patch

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
BuildArch: noarch

%description javadoc
%{summary}.

%package demo
Summary:        Examples for %{name}
Group:          Development/Java

%description demo
%{summary}.

%prep
%setup -q 

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5
%patch6 -b .sav6
%patch7 -b .sav7

rm core/src/test/java/org/apache/myfaces/test/AbstractTagLibTestCase.java
rm core/src/test/java/org/apache/myfaces/test/MyFacesTagLibTestCase.java
%patch33 -p1
%patch34

# alt; aspectj 1.5.4
sed -i 's,<groupId>aspectj</groupId>,<groupId>org.aspectj</groupId>,' core/pom.xml

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
cp %{SOURCE3} ${MAVEN_REPO_LOCAL}/JPP/maven2/default_poms/org.apache.myfaces-myfaces.pom

mvn-jpp -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
    	install:install-file -DgroupId=org.apache.myfaces.shared -DartifactId=myfaces-shared-tomahawk -Dversion=2.0.6 -Dclassifier=sources -Dpackaging=jar -Dfile=/usr/share/java/myfaces/shared11-tomahawk.jar

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc


%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{parent}

install -m 644 core/target/tomahawk-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/tomahawk-%{version}.jar
install -m 644 sandbox/core/target/tomahawk-sandbox-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/tomahawk-sandbox-%{version}.jar
install -m 644 sandbox15/core/target/tomahawk-sandbox15-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/tomahawk-sandbox15-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir}/%{parent} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/
install -m 644 examples/blank/target/myfaces-example-blank.war $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/
install -m 644 examples/simple/target/myfaces-example-simple.war $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/
install -m 644 examples/tiles/target/myfaces-example-tiles.war $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/
install -m 644 examples/wap/target/myfaces-example-wap.war $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/
install -m 644 sandbox/examples/target/tomahawk-sandbox-examples.war $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/
install -m 644 sandbox15/examples/target/tomahawk-sandbox15-examples.war $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-tomahawk-project.pom
%add_to_maven_depmap org.apache.myfaces.tomahawk tomahawk-project %{version} JPP/%{parent} tomahawk-project
install -m 644 core/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-tomahawk-core.pom
%add_to_maven_depmap org.apache.myfaces.tomahawk tomahawk %{version} JPP/%{parent} tomahawk
install -m 644 sandbox/core/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-tomahawk-sandbox.pom
%add_to_maven_depmap org.apache.myfaces.tomahawk tomahawk-sandbox %{version} JPP/%{parent} tomahawk-sandbox
install -m 644 sandbox15/core/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-tomahawk-sandbox15.pom
%add_to_maven_depmap org.apache.myfaces.tomahawk tomahawk-sandbox15 %{version} JPP/%{parent} tomahawk-sandbox15

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/sandbox
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/sandbox15
cp -pr core/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core
cp -pr sandbox/core/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/sandbox
cp -pr sandbox15/core/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/sandbox15
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

%files demo
%{_datadir}/%{name}-%{version}

%changelog
* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt7_1jpp5
- fixed build with maven3

* Sat Feb 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt6_1jpp5
- fixed build

* Sun Jan 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt5_1jpp5
- adapted for new aspectj

* Sun Nov 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt4_1jpp5
- fixed build; use cargo0

* Mon Sep 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt3_1jpp5
- fixed build with new maven 2.0.8

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt2_1jpp5
- selected java5 compiler explicitly

* Thu Jun 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_1jpp5
- new jpp release

