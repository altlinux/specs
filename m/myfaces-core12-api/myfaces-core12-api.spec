BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define parent myfaces

Summary:        JSF 1.2 API 
Name:           myfaces-core12-api
Version:        1.2.3
Release:        alt6_2jpp6
Epoch:          0
License:        Apache Software License 2.0
URL:            http://myfaces.apache.org/
Group:          Development/Java
Source0:        myfaces-core-1.2.3.tar.gz
# svn export http://svn.apache.org/repos/asf/myfaces/core/tags/1_2_3/ myfaces-core-1.2.3

Source1:        myfaces-core12-api-jpp-depmap.xml
Source2:        myfaces-core12-api-settings.xml
Source3:        myfaces-master-5.pom

Patch0:         myfaces-core12-api-pom.patch
Patch1:         myfaces-core12-api-api-pom.patch

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-testng
BuildRequires: testng
BuildRequires: junit44
BuildRequires: mojo-maven2-plugin-cobertura
BuildRequires: myfaces-maven2-plugins

BuildRequires: easymock2
BuildRequires: easymock-classextension2
BuildRequires: jakarta-taglibs-standard
BuildRequires: shale-test
BuildRequires: servlet_2_5_api
BuildRequires: jsp_2_1_api
BuildRequires: jmock
BuildRequires: el_1_0_api
BuildRequires: jakarta-commons-logging
BuildRequires: apache-commons-beanutils

Requires: jakarta-taglibs-standard
Provides:  jsf_1_2_api
BuildArch:      noarch
Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0
Source44: import.info
BuildRequires: jstl


%description
JavaServer(tm) Faces is a new and upcoming web application framework 
that accomplishes the MVC paradigm. It is comparable to the 
well-known Struts Framework but has features and concepts that 
are beyond those of Struts; especially the component orientation. 
Look at Sun's JavaServer(tm) Page to learn more about the Java 
Specification Request 127  and to download the specification. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.


%package parent
Group: Development/Java
Summary: Parent pom for %name
Provides: myfaces-core-api-parent = %version-%release
Obsoletes: myfaces-core11-api-parent < %version-%release
# pom dependency on jstl:jstl:jar:1.2
Requires: jstl


%description parent
%summary parent


%prep
%setup -q -n myfaces-core-%{version}

%patch0 -b .sav0
%patch1 -b .sav1
# this one fails to compile; easymock 2.5 instead of 2.3
rm api/src/test/java/javax/faces/component/_ValueExpressionToValueBindingTest.java

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
mkdir -p ${MAVEN_REPO_LOCAL}/org/apache/myfaces/myfaces/5/
cp %{SOURCE3} ${MAVEN_REPO_LOCAL}/org/apache/myfaces/myfaces/5/myfaces-5.pom

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
       -Dmaven.test.failure.ignore=true \
        install javadoc:javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{parent}
install -m 644 api/target/myfaces-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/core12-api-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{parent} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
touch $RPM_BUILD_ROOT%{_javadir}/jsf_1_2_api.jar

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-core12.pom
%add_to_maven_depmap org.apache.myfaces.core myfaces-core-project %{version} JPP/%{parent} core12
install -m 644 api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-core12-api.pom
%add_to_maven_depmap org.apache.myfaces.core myfaces-api %{version} JPP/%{parent} core12-api
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-master.pom
%add_to_maven_depmap org.apache.myfaces myfaces 5 JPP/%{parent} master

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsf_1_2_api_myfaces-core12-api<<EOF
/usr/share/java/jsf_1_2_api.jar	/usr/share/java/myfaces/core12-api.jar	10200
EOF

%files
%_altdir/jsf_1_2_api_myfaces-core12-api
%doc assembly/src/main/resources/LICENSE.txt
%exclude %{_javadir}/*.jar
%{_javadir}/%{parent}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%exclude %{_datadir}/maven2/poms/JPP.myfaces-master.pom

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files parent
%{_datadir}/maven2/poms/JPP.myfaces-master.pom


%changelog
* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt6_2jpp6
- fixed build with new testng and xbean

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt5_2jpp6
- fixed build with java 7

* Tue Jan 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt4_2jpp6
- added parent pom subpackage

* Tue Jan 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt3_2jpp6
- new jpp release

* Tue Nov 02 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt3_1jpp5
- build with wstx 3.2.8

* Mon Sep 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt2_1jpp5
- fixed build with new maven 2.0.8

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt1_1jpp5
- new jpp release

