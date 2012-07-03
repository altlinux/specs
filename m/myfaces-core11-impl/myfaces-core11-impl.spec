BuildRequires: mojo-parent
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat maven2-plugin-checkstyle
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

Summary:        Myfaces JSF 1.1 implementation
Name:           myfaces-core11-impl
Version:        1.1.5
Release:        alt5_2jpp5
Epoch:          0
License:        Apache Software License 2.0
URL:            http://myfaces.apache.org/
Group:          Development/Java
Source0:        myfaces-core-1.1.5.tar.gz
# svn export http://svn.apache.org/repos/asf/myfaces/core/tags/1_1_5/ myfaces-core-1.1.5

Source1:        myfaces-core11-impl-jpp-depmap.xml
Source2:        myfaces-core11-impl-settings.xml
Source3:        myfaces-master.pom

Patch0:         myfaces-core11-impl-parent-pom.patch
Patch1:         myfaces-core11-impl-pom.patch
Patch2:         myfaces-core11-impl-HtmlTextRendererTest.patch
Patch3:         myfaces-core11-impl-PropertyResolverTestCase.patch
Patch4:         myfaces-core11-impl-FacesConfigValidatorTestCase.patch

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
BuildRequires: mojo-maven2-plugin-build-helper
BuildRequires: mojo-maven2-plugin-xslt

BuildRequires: cargo
BuildRequires: jakarta-cactus
BuildRequires: junit
BuildRequires: shale-test

BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-digester
BuildRequires: jakarta-commons-el10
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-taglibs-standard
BuildRequires: jsp_2_0_api
BuildRequires: myfaces-core11-api = %{version}
BuildRequires: myfaces-shared11
BuildRequires: portlet_1_0_api
BuildRequires: servlet_2_3_api

Requires: jakarta-commons-beanutils
Requires: jakarta-commons-codec
Requires: jakarta-commons-collections
Requires: jakarta-commons-digester
Requires: jakarta-commons-el10
Requires: jakarta-commons-lang
Requires: jakarta-commons-logging
Requires: jakarta-taglibs-standard
Requires: jsp_2_0_api
Requires: myfaces-core11-api = %{version}
Requires: myfaces-shared11
Requires: portlet_1_0_api
Requires: servlet_2_3_api
Obsoletes: myfaces <= 0:1.1.0
Provides:  myfaces = %{epoch}:%{version}-%{release}

BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3


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

%prep
%setup -q -n myfaces-core-%{version}

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4

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
cp %{SOURCE3} ${MAVEN_REPO_LOCAL}/JPP/maven2/default_poms/org.apache.myfaces-myfaces.pom
install -Dm644 %{SOURCE3} ${MAVEN_REPO_LOCAL}/org/apache/myfaces/maven/myfaces-master/1.0.5/myfaces-master-1.0.5.pom

mvn-jpp -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
	install:install-file -DgroupId=org.apache.myfaces.shared -DartifactId=myfaces-shared-impl -Dversion=2.0.5 -Dclassifier=sources -Dpackaging=jar -Dfile=/usr/share/java/myfaces/shared11-impl.jar

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc


%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{parent}
mkdir tmpd
pushd tmpd
jar xf $(build-classpath myfaces/core11-api)
jar xf ../impl/target/myfaces-impl-%{version}.jar
jar cf ../myfaces-all-%{version}.jar *
popd
rm -rf tmpd
install -m 644 myfaces-all-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/myfaces-all-%{version}.jar
install -m 644 impl/target/myfaces-impl-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/core11-impl-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{parent} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
ln -sf core11-impl.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/myfaces-impl.jar
ln -sf core11-api.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/myfaces-jsf-api.jar

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 impl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-core11-impl.pom
%add_to_maven_depmap org.apache.myfaces.core myfaces-impl %{version} JPP/%{parent} core11-impl

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr impl/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc assembly/src/main/resources/LICENSE.txt
%{_javadir}/%{parent}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sat Feb 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.5-alt5_2jpp5
- fixed build

* Sun Jan 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.5-alt4_2jpp5
- adapted for new aspectj

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.5-alt3_2jpp5
- fixed build

* Mon Sep 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.5-alt2_2jpp5
- fixed build with new maven 2.0.8

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.5-alt1_2jpp5
- new jpp release

