BuildRequires: maven2-plugin-site jetty6-servlet-2.5-api
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


Name:           dojotoolkit
Version:        1.2.3
Release:        alt3_1jpp5
Epoch:          0
Summary:        Dojo Toolkit
License:        Apache Software License 2.0
Group:          Development/Java
URL:            http://www.dojotoolkit.org/
Source0:        %{name}-%{version}.tar.gz
# svn export http://svn.dojotoolkit.org/src/tags/release-1.2.3/ dojo-1.2.3

Source1:        %{name}-%{version}-build.xml
Source2:        %{name}-%{version}-jpp-depmap.xml
Source3:        %{name}-%{version}-settings.xml


BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.6.5
BuildRequires: maven2-common-poms
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-ant
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-dependency
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-war
BuildRequires: maven-surefire-plugin
BuildRequires: mojo-maven2-plugin-exec
BuildRequires: jakarta-slide-webdavclient
BuildRequires: jetty6-maven2-plugins
BuildRequires: xpp3-minimal


Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
Cometd is a scalable HTTP-based event routing bus that uses
a Ajax Push technology pattern known as Comet. The term 
'Comet' was coined by Alex Russell in his post Comet: Low 
Latency Data for the Browser.

The org.cometd java package is intended to be the standard 
java server-side API and implementation for cometd.
Currently there is only the API as a standard component, 
which is implemented by:
* Jetty-6 which provides the current cometd-java 
  implementation. The Jetty-6 release contains the 
  org.mortbay.cometd.continuation.ContinuationCometdServlet 
  class which is written against the Jetty-specific 
  Continuation API, which will run scalably only on the 
  Jetty server.
* Jetty-7 pre-release contains an implementation of the 
  cometd-java API written against the proposed standard 
  servlet-3.0 suspend/resume API. This 
  org.mortbay.cometd.continuation.SuspendingCometdServlet 
  will eventually be the cometd-java implementation and 
  will work on all servlet-3.0 compliant browser.
* Glassfish Grizzly currently has a java implementation of 
  bayeux based on an early version of the dojox.servlet API.
* Tomcat 6 has a prototype working against a modified 
  version of this API 

%prep
%setup -q 
cp %{SOURCE1} build.xml
cp %{SOURCE3} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL
mkdir -p $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export M2_SETTINGS=$(pwd)/settings.xml
cd util/maven
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $M2_SETTINGS \
        -Dmaven.test.failure.ignore=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install

%install
# jars/poms
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 util/maven/dojo-war/target/dojo-war-1.2.3.war $RPM_BUILD_ROOT%{_javadir}/%{name}/dojo-war-1.2.3.jar

%add_to_maven_depmap org.dojotoolkit dojo-project %{version} JPP dojo-project
install -m 644 util/maven/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-dojo-project.pom

%add_to_maven_depmap org.dojotoolkit dojo-war %{version} JPP/%{name} dojo-war
install -m 644 util/maven/dojo-war/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-dojo-war.pom

%add_to_maven_depmap org.dojotoolkit dojo %{version} JPP dojo
install -m 644 util/maven/dojo/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-dojo.pom

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

%files 
%{_javadir}/%{name}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%changelog
* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt3_1jpp5
- built with patched assembly plugin

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt2_1jpp5
- fixed build

* Tue Mar 17 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt1_1jpp5
- first build

