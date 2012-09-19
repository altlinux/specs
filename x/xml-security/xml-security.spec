# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
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

%global oname xmlsec

Name:           xml-security
Version:        1.4.5
Release:        alt1_4jpp7
Epoch:          0
Summary:        Implementation of W3C security standards for XML
License:        ASL 2.0
URL:            http://santuario.apache.org/
Group:          Development/Java
Source0:        http://archive.apache.org/dist/santuario/java-library/xml-security-src-1_4_5.zip
Source1:        xml-security-component-info.xml
Source2:        http://repo1.maven.org/maven2/org/apache/santuario/xmlsec/1.4.5/xmlsec-1.4.5.pom
Patch0:         xml-security-build_xml.patch
Patch1:         xml-security-disable-test-fail.patch
Patch2:         xml-security-notest.patch

Requires:       apache-commons-logging
Requires:       log4j
Requires:       xalan-j2 >= 0:2.7
Requires:       xerces-j2 >= 0:2.7

BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  apache-commons-logging
BuildRequires:  log4j
BuildRequires:  xalan-j2 >= 0:2.7
BuildRequires:  xerces-j2 >= 0:2.7
BuildArch:      noarch
Source44: import.info

%description
The XML Security project is aimed at providing implementation 
of security standards for XML. Currently the focus is on the 
W3C standards :
- XML-Signature Syntax and Processing; and
- XML Encryption Syntax and Processing.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Samples for %{name}
Group:          Development/Java

%description demo
Samples for %{name}.

%prep
%setup -q -n xml-security-1_4_5
%patch0 -p0
%patch1 -p0
%patch2 -p0

find . -name \*.jar -type f -exec rm -f {} \;

mkdir -p libs/endorsed
pushd libs
ln -s $(build-classpath commons-logging)
ln -s $(build-classpath commons-logging-api)
ln -s $(build-classpath junit)
ln -s $(build-classpath log4j)
ln -s $(build-classpath xalan-j2)
ln -s $(build-classpath xalan-j2-serializer)
ln -s $(build-classpath xerces-j2)
ln -s $(build-classpath xml-commons-jaxp-1.3-apis)
popd

%build
ant -Djava.endorsed.dirs=libs build.src build.jar build.docs
# FIXME: (dwalluck) AES key size above 128 will fail with default Sun JCE provider policy
# ant -Djava.endorsed.dirs=libs -Dlib.xalan.3=libs/xml-commons-jaxp-1.3-apis.jar test

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/%{oname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{oname}.jar
install -m 644 build/xmlsecSamples-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-samples.jar
ln -s %{name}-samples.jar $RPM_BUILD_ROOT%{_javadir}/xmlsecSamples.jar

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/docs/html/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{oname}.pom
%add_maven_depmap JPP-%{oname}.pom %{oname}.jar -a "org.apache.santuario:xmlsec"

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr src_samples/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%files
%doc LICENSE
%{_javadir}/%{name}.jar
%{_javadir}/%{oname}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%files demo
%doc LICENSE
%{_javadir}/%{name}-samples.jar
%{_javadir}/xmlsecSamples.jar
%{_datadir}/%{name}

%changelog
* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.5-alt1_4jpp7
- new release

* Sun Mar 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt3_0jpp6
- added depmap for org.apache.santuario:xmlsec:jar

* Wed Oct 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt2_0jpp6
- added jbossas42 compatible repolib

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt1_0jpp6
- new version (closes: #20786)

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt1_5jpp6
- new version

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt2_2jpp5
- use default jpp profile

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_2jpp5
- jpp5 build

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

