Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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


Summary:        WSO2 Web Services Framework for Javascript Rhino
Name:           axiom-e4x
Version:        0.0
Release:        alt3_0.20080828.1jpp5
Epoch:          0
Group:          Development/Java
License:        ASL 2.0
URL:            http://wso2.org/projects/wsf/js/rhino
Source0:        axiom-e4x-20080828.tar.gz
# svn export https://wso2.org/repos/wso2/trunk/wsf/javascript/rhino/e4ximpl/ e4ximpl-20080828

Source1:        %{name}-jpp-depmap.xml
Source2:        %{name}-settings.xml
Source3:        wsf-javasript-rhino.pom

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: junit
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-dependency
BuildRequires: maven2-plugin-enforcer
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin

BuildRequires: rhino
BuildRequires: stax_1_0_api
BuildRequires: sun-jaf
BuildRequires: sun-mail
BuildRequires: ws-commons-axiom
BuildRequires: wstx

Requires: rhino

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
WSO2 WSF/JavaScript Rhino consists of the following components:
* E4X Implementation in Rhino:
  E4X stands for ECMAScript (a scripting programming language,
  standardized by Ecma International in the ECMA-262 
  specification) for XML.
  E4X is as an extension to JavaScript language to provide
  native support for XML processing. E4X support in Rhino is 
  re-implemented using Apache AXIOM in order to make JavaScript
  Web services faster in Apache Axis2/Java.
* JavaScript Message Receiver:
  This message receiver allows JavaScript services to be 
  deployed in Apache Axis2/Java. It has built-in support for 
  Rhino's load and print functions. The service should return 
  an E4X XML object in order to use this message receiver.
* Rino version of WSRequest:
  WSRequest.js (src/WSRequest.js) is a JavaScript implementation 
  of the WSRequest API 
  (http://www.wso2.org/wiki/display/wsfajax/wsrequest_specification)
  using Axis2's client API.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}

%description javadoc
%{summary}.

%prep
%setup -q -n e4ximpl-20080828

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
mkdir -p $MAVEN_REPO_LOCAL/JPP/maven2/default_poms
cp %{SOURCE3} $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/org.wso2.wsf.javascript-wsf-javascript-rhino.pom
install -Dm644 %{SOURCE3} $MAVEN_REPO_LOCAL/org/wso2/wsf/javascript/wsf-javascript-rhino/SNAPSHOT/wsf-javascript-rhino-SNAPSHOT.pom

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-wsf-javascript-rhino.pom
%add_to_maven_depmap org.wso2.wsf.javascript wsf-javascript-rhino SNAPSHOT JPP wsf-javascript-rhino

install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.wso2.wsf.javascript %{name} %{version} JPP %{name}
install -m 644 target/axiom-e4x-SNAPSHOT.jar \
               $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
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
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.0-alt3_0.20080828.1jpp5
- fixed build with java 7

* Thu Sep 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.0-alt2_0.20080828.1jpp5
- fixed build with new maven 2.0.8

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.0-alt1_0.20080828.1jpp5
- first build

