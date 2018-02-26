Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: wsdl4j
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


# To make the tarball:
#  export CVSROOT=:pserver:anoncvs@anoncvs.internet2.edu:/home/cvs/shibboleth
#  cvs login
#  cvs export -r Rel_1_1_FINAL_B opensaml

Name:           opensaml
Summary:        Open source implementation of the SAML 1.0 and 1.1 specifications
Version:        1.1b
Release:        alt1_2jpp5
Epoch:          0

URL:            http://www.opensaml.org/
License:        Apache Public License v2.0
Group:          Development/Java
Source0:        %{name}-%{version}.tgz
Source1:        http://repo2.maven.org/maven2/org/opensaml/opensaml/1.1/opensaml-1.1.pom

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: ant-nodeps
BuildRequires: junit >= 0:3.8.1
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-logging
BuildRequires: log4j
BuildRequires: servlet_2_4_api
BuildRequires: wsdl4j
BuildRequires: xalan-j2 >= 0:2.7.0
BuildRequires: xml-security >= 0:1.3
Requires: jakarta-commons-codec
Requires: jakarta-commons-logging
Requires: log4j
Requires: servlet_2_4_api
Requires: wsdl4j
Requires: xalan-j2 >= 0:2.7.0
Requires: xml-security >= 0:1.3

BuildArch: noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

%description
OpenSAML is a set of open source Java and C++ libraries that implement the
SAML 1.0 and 1.1 specifications.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}

mv java/* .
rm -rf java

find . -name "*.jar" | xargs rm -f

build-jar-repository endorsed \
     xalan-j2 \

#     xerces-j2 \
#     xml-commons-apis \
#     xml-commons-resolver

build-jar-repository lib \
     commons-codec \
     commons-logging \
     junit \
     log4j \
     servlet_2_4_api \
     wsdl4j \
     xalan-j2 \
     xml-security

# Uncomment the line below to show output... do we really want to see test 
# output though? since haltonerror is true, any failed test will abort build 
# anyways, so it won't be missed.

#sed -i -e s:'<junit printsummary="no" fork="yes" haltonfailure="yes" haltonerror="yes" dir="${root}">':'<junit printsummary="yes" fork="yes" haltonfailure="yes" haltonerror="yes" dir="${root}">':g build.xml

%build
ant dist javadocs

%install

# main package
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/opensaml-1.1.jar \
    $RPM_BUILD_ROOT%{_javadir}/opensaml-%{version}.jar
ln -s opensaml-%{version}.jar \
    $RPM_BUILD_ROOT%{_javadir}/opensaml.jar
%add_to_maven_depmap org.opensaml %{name} 1.1 JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT/%{_javadocdir}/%{name}-%{version}
cp -pr doc/api/* \
    $RPM_BUILD_ROOT/%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT/%{_javadocdir}/%{name}

%files
%dir %{_javadir}
%{_javadir}/opensaml-%{version}.jar
%{_javadir}/opensaml.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1b-alt1_2jpp5
- new jpackage release

* Sun Oct 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1b-alt1_1jpp1.7
- converted from JPackage by jppimport script

