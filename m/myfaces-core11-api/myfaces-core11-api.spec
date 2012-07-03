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

%define parent myfaces

Summary:        JSF 1.1 API
Name:           myfaces-core11-api
Version:        1.1.5
Release:        alt4_2jpp6
Epoch:          0
License:        Apache Software License 2.0
URL:            http://myfaces.apache.org/
Group:          Development/Java
Source0:        myfaces-core-1.1.5.tar.gz
# svn export http://svn.apache.org/repos/asf/myfaces/core/tags/1_1_5/ myfaces-core-1.1.5

Source1:        myfaces-core11-api-jpp-depmap.xml
Source2:        myfaces-core11-api-settings.xml
Source3:        myfaces-maven-1.0.5.pom

Patch0:         myfaces-core11-UIComponentBaseTest.patch
Patch1:         myfaces-core11-DateTimeConverterTest.patch
Patch2:         myfaces-core11-api-parent-pom.patch
Patch3:         myfaces-core11-api-pom.patch

BuildRequires: jpackage-utils >= 0:1.7.3
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

BuildRequires: easymock-classextension
BuildRequires: jakarta-taglibs-standard
BuildRequires: shale-test

Requires: jakarta-taglibs-standard
Provides:  jsf_1_1_api
BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

Requires: myfaces-core-api-parent >= %version-%release

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

%description javadoc
%{summary}.

%package parent
Summary:        Parent pom for %{name}
Group:          Development/Java
Provides: myfaces-core-api-parent = %version-%release

%description parent
%{summary}.

%prep
%setup -q -n myfaces-core-%{version}

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3

# alt; aspectj 1.5.4
sed -i 's,<groupId>aspectj</groupId>,<groupId>org.aspectj</groupId>,' api/pom.xml

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
cp %{SOURCE3} ${MAVEN_REPO_LOCAL}/JPP/maven2/default_poms/org.apache.myfaces.maven-myfaces-master.pom
install -Dm644 %{SOURCE3} ${MAVEN_REPO_LOCAL}/org/apache/myfaces/maven/myfaces-master/1.0.5/myfaces-master-1.0.5.pom


mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc


%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{parent}
install -m 644 api/target/myfaces-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/core11-api-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{parent} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
# don't: this symlink will be brought in by myfaces-core11-impl which  will provide legacy myfaces
#ln -sf core11-api.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/myfaces-jsf-api.jar
touch $RPM_BUILD_ROOT%{_javadir}/jsf_1_1_api.jar

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-master.pom
%add_to_maven_depmap org.apache.myfaces.maven myfaces-master 1.0.5 JPP/%{parent} master
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-core11.pom
%add_to_maven_depmap org.apache.myfaces.core myfaces-core-project %{version} JPP/%{parent} core11
install -m 644 api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-core11-api.pom
%add_to_maven_depmap org.apache.myfaces.core myfaces-api %{version} JPP/%{parent} core11-api

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsf_1_1_api_%{name}<<EOF
/usr/share/java/jsf_1_1_api.jar	/usr/share/java/myfaces/core11-api.jar	10100
EOF

%files
%_altdir/jsf_1_1_api_%{name}
%doc assembly/src/main/resources/LICENSE.txt
%exclude %{_javadir}/*.jar
%{_javadir}/%{parent}/*.jar
%{_datadir}/maven2/poms/JPP.myfaces-core11*pom
%{_mavendepmapfragdir}/*

%files parent
%{_datadir}/maven2/poms/JPP.myfaces-master.pom

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Mon Jan 31 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.5-alt4_2jpp6
- restored parent subpackage

* Sun Jan 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.5-alt3_2jpp6
- fixed build

* Tue Jan 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.5-alt3_2jpp5
- renamed master pom

* Mon Sep 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.5-alt2_2jpp5
- fixed build with new maven 2.0.8

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.5-alt1_2jpp5
- new jpp release

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.5-alt1_1jpp5
- new version

