Patch33: myfaces-maven2-plugins-alt-maven3.patch
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

Summary:        Apache MyFaces Buildtools Maven2 Plugins
Name:           myfaces-maven2-plugins
Version:        1.0.0
Release:        alt4_1jpp5
Epoch:          0
License:        Apache Software License 2.0
URL:            http://myfaces.apache.org/
Group:          Development/Java
Source0:        myfaces-maven2-plugins-1.0.0.tar.gz
# svn export http://svn.apache.org/repos/asf/myfaces/myfaces-build-tools/tags/m2_plugins_100_release/ myfaces-maven2-plugins-1.0.0

Source1:        %{name}-jpp-depmap.xml
Source2:        %{name}-settings.xml
Source3:        myfaces-master.pom

Patch0:         myfaces-maven2-plugins-pom.patch

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-checkstyle
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin

BuildRequires: bea-stax
BuildRequires: jakarta-commons-digester
BuildRequires: jakarta-commons-io
BuildRequires: javacc3
BuildRequires: plexus-compiler
BuildRequires: plexus-utils
BuildRequires: saxon
BuildRequires: stax_1_0_api

Requires: maven2
Requires: bea-stax
Requires: jakarta-commons-digester
Requires: jakarta-commons-io
Requires: javacc3
Requires: plexus-compiler
Requires: plexus-utils
Requires: saxon
Requires: stax_1_0_api

BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3


%description
MyFaces projects all use Maven 2.x to compile the code, run
testing, etc. However sometimes the standard maven plugins 
are not enough for the special requirements of MyFaces 
projects. Therefore a number of custom Maven plugins have 
been created.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%prep
%setup -q 

%patch0 -b .sav0
%patch33

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
mkdir -p ${MAVEN_REPO_LOCAL}/JPP/maven2/default_poms/
cp %{SOURCE3} ${MAVEN_REPO_LOCAL}/JPP/maven2/default_poms/org.apache.myfaces-myfaces.pom
install -Dm644 %{SOURCE3} ${MAVEN_REPO_LOCAL}/org/apache/myfaces/myfaces/5/myfaces-5.pom

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
      install:install-file -DgroupId=net.java.dev.javacc -DartifactId=javacc -Dversion=3.2 -Dpackaging=jar -Dfile=/usr/share/java/javacc3.jar


mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Daggregate=true \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc


%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{parent}
install -m 644 myfaces-faces-plugin/target/myfaces-faces-plugin-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/faces-plugin-%{version}.jar
install -m 644 myfaces-i18n-plugin/target/myfaces-i18n-plugin-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/i18n-plugin-%{version}.jar
install -m 644 myfaces-javacc-plugin/target/myfaces-javacc-plugin-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/javacc-plugin-%{version}.jar
install -m 644 myfaces-javascript-plugin/target/myfaces-javascript-plugin-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/javascript-plugin-%{version}.jar
install -m 644 myfaces-jdev-plugin/target/myfaces-jdev-plugin-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/jdev-plugin-%{version}.jar
install -m 644 myfaces-wagon-plugin/target/myfaces-wagon-plugin-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/wagon-plugin-%{version}.jar
install -m 644 myfaces-xrts-plugin/target/myfaces-xrts-plugin-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/xrts-plugin-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{parent} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-buildtools.pom
%add_to_maven_depmap org.apache.myfaces.buildtools myfaces-plugin-parent %{version} JPP/%{parent} buildtools
install -m 644 myfaces-faces-plugin/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-faces-plugin.pom
%add_to_maven_depmap org.apache.myfaces.buildtools myfaces-faces-plugin %{version} JPP/%{parent} faces-plugin
install -m 644 myfaces-i18n-plugin/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-i18n-plugin.pom
%add_to_maven_depmap org.apache.myfaces.buildtools myfaces-i18n-plugin %{version} JPP/%{parent} i18n-plugin
install -m 644 myfaces-javacc-plugin/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-javacc-plugin.pom
%add_to_maven_depmap org.apache.myfaces.buildtools myfaces-javacc-plugin %{version} JPP/%{parent} javacc-plugin
install -m 644 myfaces-javascript-plugin/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-javascript-plugin.pom
%add_to_maven_depmap org.apache.myfaces.buildtools myfaces-javascript-plugin %{version} JPP/%{parent} javascript-plugin
install -m 644 myfaces-jdev-plugin/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-jdev-plugin.pom
%add_to_maven_depmap org.apache.myfaces.buildtools myfaces-jdev-plugin %{version} JPP/%{parent} jdev-plugin
install -m 644 myfaces-wagon-plugin/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-wagon-plugin.pom
%add_to_maven_depmap org.apache.myfaces.buildtools myfaces-wagon-plugin %{version} JPP/%{parent} wagon-plugin
install -m 644 myfaces-xrts-plugin/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-xrts-plugin.pom
%add_to_maven_depmap org.apache.myfaces.buildtools myfaces-xrts-plugin %{version} JPP/%{parent} xrts-plugin

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc LICENSE.txt
%{_javadir}/%{parent}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt4_1jpp5
- fixed build with java 7

* Sun Feb 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt3_1jpp5
- fixed build

* Mon Sep 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt2_1jpp5
- fixed build with new maven 2.0.8

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_1jpp5
- new jpp release

