Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6-compat
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

%define spname      ldapsp
%define filtname    ldapfilt
%define beansname   ldapbeans
%define gcj_support 0

Name:           ldapsdk
Version:        4.18
Release:        alt1_2jpp6
Epoch:          1
Summary:        Enables applications to manage information stored in an LDAP directory
Group:          Development/Java
License:        MPL
URL:            http://www.mozilla.org/directory/
# cvs -d:pserver:anonymous@cvs-mirror.mozilla.org:/cvsroot export -r LDAPJavaSDK_418 DirectorySDKSourceJava && tar cjf ldapsdk-4.18.tar.bz2 mozilla
Source0:        ldapsdk-%{version}.tar.bz2
Requires: jaas
Requires: jndi
Requires: jpackage-utils >= 0:1.5
Requires: jss
BuildRequires: ant
BuildRequires: jaas
BuildRequires: jndi
BuildRequires: jpackage-utils >= 0:1.5
BuildRequires: jss
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Provides:       ldapjdk = %{epoch}:%{version}-%{release}
Obsoletes:      ldapjdk <= 1:4.17-1jpp
BuildArch:      noarch

%description
The Mozilla LDAP SDKs enable you to write applications which access,
manage, and update the information stored in an LDAP directory.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
Provides:       ldapjdk-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      ldapjdk-javadoc <= 1:4.17-1jpp
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
find . -type f -name "*.jar" | xargs -t rm

%build
pushd mozilla/directory/java-sdk/ldapjdk/lib
build-jar-repository -s . jss4 jsse jaas jndi
ln -s $(build-classpath jss4) jss32_stub.jar
popd

cd mozilla/directory/java-sdk
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first dist

%install

# jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 mozilla/directory/java-sdk/dist/packages/ldapjdk.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -p -m 644 mozilla/directory/java-sdk/dist/packages/%{spname}.jar $RPM_BUILD_ROOT%{_javadir}/%{spname}-%{version}.jar
install -p -m 644 mozilla/directory/java-sdk/dist/packages/%{filtname}.jar $RPM_BUILD_ROOT%{_javadir}/%{filtname}-%{version}.jar
install -p -m 644 mozilla/directory/java-sdk/dist/packages/%{beansname}.jar $RPM_BUILD_ROOT%{_javadir}/%{beansname}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/ldapjdk-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -s ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr mozilla/directory/java-sdk/dist/doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/ldapjdk-%{version}
ln -s ldapjdk-%{version} $RPM_BUILD_ROOT%{_javadocdir}/ldapjdk

%files
%doc mozilla/directory/buildjsdk.txt mozilla/directory/java-sdk/{ldapsp-relnotes.htm,relnotes.htm}
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/ldapjdk-%{version}.jar
%{_javadir}/ldapjdk.jar
%{_javadir}/%{spname}*.jar
%{_javadir}/%{filtname}*.jar
%{_javadir}/%{beansname}*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%{_libdir}/gcj/%{name}/%{spname}-%{version}.jar.*
%{_libdir}/gcj/%{name}/%{filtname}-%{version}.jar.*
%{_libdir}/gcj/%{name}/%{beansname}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{_javadocdir}/ldapjdk-%{version}
%{_javadocdir}/ldapjdk

%changelog
* Tue Mar 30 2010 Igor Vlasenko <viy@altlinux.ru> 1:4.18-alt1_2jpp6
- new version

* Mon Sep 22 2008 Igor Vlasenko <viy@altlinux.ru> 1:4.17-alt1_3jpp5
- fixed build with java5

* Fri May 25 2007 Igor Vlasenko <viy@altlinux.ru> 1:4.17-alt1_3jpp1.7
- converted from JPackage by jppimport script

