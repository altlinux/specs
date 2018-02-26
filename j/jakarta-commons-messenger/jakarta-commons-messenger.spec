BuildRequires: geronimo-jta-1.0.1B-api
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

%define gcj_support 0

%define section   devel
%define base_name commons-messenger
%define jakarta_version 1.0

Name:           jakarta-%{base_name}
Version:        1.0
Release:        alt2_0.d10.6jpp5
Epoch:          1
Summary:        Commons Messenger JMS framework 

Group:          Development/Java
License:        Apache Software License
URL:            http://jakarta.apache.org/commons/sandbox/messenger/
Source0:        http://cvs.apache.org/builds/jakarta-commons/nightly/commons-messenger/commons-messenger-src-20040113.tar.gz
Source1:        commons-messenger-1.0-dev-10.pom
Patch0:         commons-messenger-build.patch

%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit
BuildRequires: junit >= 0:3.8.1
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-digester
BuildRequires: servlet_2_3_api
BuildRequires: jms_1_1_api
BuildRequires: jta_1_0_1B_api
#BuildRequires:  xml-commons-apis >= 0:1.0
Requires: jakarta-commons-logging
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-collections
Requires: jakarta-commons-digester
Requires: servlet_2_3_api
Requires: jms_1_1_api
Requires: jta_1_0_1B_api
#Requires:       xml-commons-apis >= 0:1.0
#Requires:       jaxp_parser_impl
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3


%description
Messenger is a JMS (Java Message Service) framework which makes it 
very easy to use JMS in Web Service and Web Application environments. 
Messenger implements session pooling (which can be quite hard to do 
with JMS) which makes JMS very easy to work with. Also Messenger hides 
much of the complexity of JMS behind a simple facade API, the Messenger 
interface. 
In addition Messenger provides an XML deployment configuration file to 
avoid having to litter your code with complex deployment configuration 
details in your application code. 
Messenger also provides a Messagelet Engine which is a JMS based 
container that can be deployed in any Servlet Engine to process JMS 
messages via MessageListeners, Message Driven Objects, Servlets or JSP. 

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{base_name}
%patch0 -b .sav0

%build
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=$(build-classpath \
jakarta-commons-logging-api \
jakarta-commons-logging jakarta-commons-beanutils jakarta-commons-collections \
jakarta-commons-digester servlet_2_3_api jms_1_1_api jta_1_0_1B_api )
CLASSPATH=target/classes:target/test-classes:$CLASSPATH
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 -Dbuild.sysclasspath=only test dist

%install
install -Dpm 644 dist/%{base_name}-%{jakarta_version}-dev-10.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{base_name}-%{version}.jar
ln -s %{base_name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{base_name}.jar

%add_to_maven_depmap %{base_name} %{base_name} %{version} JPP %{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt README.txt RELEASE-NOTES.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt2_0.d10.6jpp5
- fixed build

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_0.d10.6jpp5
- new jpp release

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.d10-alt2_5jpp5
- fixed build with java 5

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.d10-alt1_5jpp1.7
- converted from JPackage by jppimport script

