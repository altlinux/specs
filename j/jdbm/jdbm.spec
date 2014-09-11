Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
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

Name:           jdbm
Version:        1.0
Release:        alt2_6jpp7
Summary:        A transactional persistence engine for Java

Group:          Development/Java
License:        BSD with attribution
URL:            http://jdbm.sourceforge.net/
BuildArch:      noarch
# cvs -d:pserver:anonymous@jdbm.cvs.sourceforge.net:/cvsroot/jdbm login
# cvs -z3 -d:pserver:anonymous@jdbm.cvs.sourceforge.net:/cvsroot/jdbm co -P -r V1_0 jdbm-1.0
# find jdbm-1.0/ -name "CVS" -type d -exec rm -rf {} \;
# tar cJf jdbm-1.0.tar.xz jdbm-1.0/
Source0:        jdbm-1.0.tar.xz
Source1:        http://repo1.maven.org/maven2/jdbm/jdbm/1.0/jdbm-1.0.pom

# needs support for UTF-8 characters in source code
Patch0:         jdbm-enable-utf8-build.patch
# example code contains non-UTF-8 characters
Patch1:         jdbm-fix-utf8-example.patch

BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  junit

Requires:       jpackage-utils
Source44: import.info

%description
A transactional persistence engine for Java. 
It aims to be for Java what GDBM is for Perl, Python, C, 
etcetera: a simple persistence engine that is lightweight 
and fast.

%package javadoc
Summary:    Javadoc for %{name}
Group:      Development/Java
Requires:   jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}
chmod -R go=u-w *
find . -name "*.jar" -exec rm -f {} \;

%patch0 -p1
%patch1 -p1

# Fix example code line endings
sed -i 's///g' src/examples/FruitBasket.java

%build
ant -f src/build.xml main examples tests jar javadoc

%check
ant -f src/build.xml tests.run

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc src/examples CHANGES.txt LICENSE.txt README.txt TODO.txt
%{_javadir}/*
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_3jpp7
- new release

* Fri Mar 15 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_2jpp7
- fc update

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_2jpp5
- fixed build with java 7

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp5
- converted from JPackage by jppimport script

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.20-alt1_2jpp1.7
- converted from JPackage by jppimport script

