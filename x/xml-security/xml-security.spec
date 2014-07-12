Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
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
Version:        1.5.5
Release:        alt1_1jpp7
Epoch:          0
Summary:        Implementation of W3C security standards for XML
License:        ASL 2.0
URL:            http://santuario.apache.org/
Source0:        http://archive.apache.org/dist/santuario/java-library/1_5_5/xml-security-src-1_5_5.zip
# Certain tests fail with new JUnit
Patch0:         %{name}-removed-tests.patch

Requires:       apache-commons-logging
Requires:       log4j
Requires:       xalan-j2
Requires:       xerces-j2
Requires:       xml-commons-apis
Requires:       bouncycastle

BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  junit
BuildRequires:  apache-commons-logging
BuildRequires:  log4j
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis
BuildRequires:  bouncycastle

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
%setup -q -n xml-security-1_5_5
%patch0 -p1

sed -i "s|bcprov-jdk15on|bcprov-jdk16|" pom.xml

%build

mvn-rpmbuild package javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{oname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{oname}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr samples/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_javadir}/%{oname}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE NOTICE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%files demo
%doc LICENSE NOTICE
%{_datadir}/%{name}

%changelog
* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt1_1jpp7
- update

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0:1.4.5-alt1_4jpp7.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for xml-security

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

