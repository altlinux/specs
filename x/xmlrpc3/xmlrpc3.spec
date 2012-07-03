BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2005, JPackage roject
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

%global mainname xmlrpc

Name:       xmlrpc3
Version:    3.1.3
Release:    alt1_5jpp6
Summary:    Java XML-RPC implementation
License:    ASL 2.0
Group:      Development/Java
URL:        http://ws.apache.org/xmlrpc/
Source0:    http://www.apache.org/dist//ws/xmlrpc/sources/apache-xmlrpc-%{version}-src.tar.bz2
Source1:    %{name}-jpp-depmap.xml
# FIXME:  file this upstream
# The tests pom.xml doesn't include necessary dependencies on junit and
# servletapi
Patch0:     %{name}-addjunitandservletapitotestpom.patch
# Add OSGi MANIFEST information
Patch1:     %{name}-client-addosgimanifest.patch
Patch2:     %{name}-common-addosgimanifest.patch

BuildRequires:  maven2 >= 2.0.4
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-eclipse
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-source
BuildRequires:  maven2-plugin-site
BuildRequires:  ws-jaxme
BuildRequires:  ws-commons-util
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  servlet25
BuildRequires:	tomcat6
BuildRequires:  junit
BuildRequires:  jakarta-commons-httpclient
BuildRequires:  apache-commons-logging

BuildArch:    noarch
Source44: import.info

%description
Apache XML-RPC is a Java implementation of XML-RPC, a popular protocol
that uses XML over HTTP to implement remote procedure calls.
Apache XML-RPC was previously known as Helma XML-RPC. If you have code
using the Helma library, all you should have to do is change the import
statements in your code from helma.xmlrpc.* to org.apache.xmlrpc.*.

%package javadoc
Summary:    Javadoc for %{name}
Group:      Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package common
Summary:    Common classes for XML-RPC client and server implementations
Group:      Development/Java
Obsoletes:  %{name}-common-devel <= %{version}
Requires:   ws-jaxme
Requires:   ws-commons-util
Requires:   jpackage-utils >= 0:1.6
Requires:   apache-commons-logging
Requires(post): jpackage-utils
Requires(postun): jpackage-utils

%description common
%{summary}.

%package client
Summary:    XML-RPC client implementation
Group:      Development/Java
Requires:   %{name}-common
Requires:   jakarta-commons-httpclient
Obsoletes:  %{name}-client-devel <= %{version}

%description client
%{summary}.

%package server
Summary:    XML-RPC server implementation
Group:      Development/Java
Requires:   %{name}-client
Requires:   junit
Requires:   servlet25
Obsoletes:  %{name}-server-devel <= %{version}

%description server
%{summary}.

%prep
%setup -q -n apache-%{mainname}-%{version}-src
pushd server
%patch0 -b .sav
popd
pushd client
%patch1 -b .sav
popd
pushd common
%patch2 -b .sav
popd

sed -i 's/\r//' LICENSE.txt

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL
# ignore test failure because server part needs network
mvn-jpp \
  -e \
  -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
  -Dmaven2.jpp.depmap.file=%{SOURCE1} \
  -Dmaven.test.failure.ignore=true \
  install javadoc:aggregate

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 client/target/%{mainname}-client-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-client.jar
install -m 644 server/target/%{mainname}-server-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-server.jar
install -m 644 common/target/%{mainname}-common-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-common.jar

# install maven pom files
install -Dm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
install -Dm 644 common/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-common.pom
install -Dm 644 client/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-client.pom
install -Dm 644 server/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-server.pom

# ... and maven depmaps
%add_to_maven_depmap org.apache.xmlrpc %{mainname} %{version} JPP %{name}
%add_to_maven_depmap org.apache.xmlrpc %{mainname}-common %{version} JPP %{name}-common
%add_to_maven_depmap org.apache.xmlrpc %{mainname}-client %{version} JPP %{name}-client
%add_to_maven_depmap org.apache.xmlrpc %{mainname}-server %{version} JPP %{name}-server

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%pre javadoc
# workaround rpm bug, can be removed in F-17
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/*

%files common
%doc LICENSE.txt
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavenpomdir}/JPP-%{name}-common.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}-common.jar

%files client
%{_mavenpomdir}/JPP-%{name}-client.pom
%{_javadir}/%{name}-client.jar

%files server
%{_mavenpomdir}/JPP-%{name}-server.pom
%{_javadir}/%{name}-server.jar

%changelog
* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 3.1.3-alt1_5jpp6
- update to new release by jppimport

* Sat Mar 21 2009 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_3.9jpp5
- fixed build

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_2.9jpp5
- new version

* Tue Oct 21 2008 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_0.4jpp5
- fixed build; resurrected from orphaned.

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_0.4jpp1.7
- converted from JPackage by jppimport script

