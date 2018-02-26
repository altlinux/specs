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

%define namedversion   1.0.beta4

# If you don't want to build with maven, and use straight ant instead,
# give rpmbuild option '--without maven'

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}

Name:           cometd-java
Version:        1.0
Release:        alt3_0.b4.1jpp6
Epoch:          0
Summary:        Cometd Java API
License:        Apache Software License 2.0
Group:          Development/Java
URL:            http://maven.apache.org/
Source0:        %{name}-%{namedversion}.tar.gz
# svn export http://svn.cometd.com/tags/1.0.beta4/cometd-java/ cometd-java-1.0.beta4


Source1:        %{name}-%{version}-build.xml
Source2:        %{name}-%{version}-jpp-depmap.xml
Source3:        %{name}-%{version}-settings.xml
Source4:        cometd-project.pom


BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.6.5
%if %{with_maven}
BuildRequires: maven2-common-poms
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-ant
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-source
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-plugin
BuildRequires: maven-release
BuildRequires: jakarta-slide-webdavclient
%endif


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

%package api
Summary:        API for %{name}
Group:          Development/Java

%description api
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{namedversion}
cp %{SOURCE1} build.xml
cp %{SOURCE3} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml

%build
%if %{with_maven}
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL
mkdir -p $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/
cp %{SOURCE4} $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/org.cometd-cometd-project.pom
# maven208 hacks
install -Dm644 %{SOURCE4} $MAVEN_REPO_LOCAL/org/cometd/cometd-project/1.0.beta4/cometd-project-1.0.beta4.pom

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export M2_SETTINGS=$(pwd)/settings.xml
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $M2_SETTINGS \
        -Dmaven.test.failure.ignore=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        ant:ant install javadoc:javadoc
%else
export CLASSPATH=
#export CLASSPATH=$(build-classpath \
#)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dmaven.settings.offline=true -Dbuild.sysclasspath=only jar javadoc
%endif

%install
# jars/poms
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

%add_to_maven_depmap org.cometd cometd-project %{version} JPP cometd-project
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-cometd-project.pom

%add_to_maven_depmap org.cometd.java cometd-java-project %{version} JPP cometd-java-project
install -m 644 pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-cometd-java-project.pom

install -m 644 api/target/cometd-api-%{version}-SNAPSHOT.jar \
               $RPM_BUILD_ROOT%{_javadir}/cometd-api-%{version}.jar
%add_to_maven_depmap org.cometd.java cometd-api %{version} JPP cometd-api
install -m 644 api/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-cometd-api.pom

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr api/target/site/apidocs/* \
                    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files api
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b4.1jpp6
- fixed build with maven3

* Thu Sep 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.b4.1jpp6
- fixed build with new maven 2.0.8

* Tue May 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b4.1jpp6
- new version

