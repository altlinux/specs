# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# Copyright (c) 2000-2007, JPackage Project
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

%define originalname PullParser

Summary:        XML Pull Parser
Name:           xpp2
Version:        2.1.10
Release:        alt4_23jpp8
Epoch:          0
License:        xpp and ASL 1.1 and Public Domain
URL:            http://www.extreme.indiana.edu/xgws/xsoap/xpp/
Group:          Development/Other
Source0:        http://www.extreme.indiana.edu/xgws/xsoap/xpp/download/PullParser2/PullParser2.1.10.tgz
Patch0:         xpp2-build_xml.patch
BuildRequires:  ant >= 0:1.6
BuildRequires:  ant-junit >= 0:1.6
BuildRequires:  javapackages-local
BuildRequires:  junit
BuildRequires:  xml-commons-apis
Requires:       xml-commons-apis
Requires: javapackages-tools rpm-build-java
BuildArch:      noarch
Provides:  xpp2-doc = 0:%{version}-%{release}
Obsoletes: xpp2-doc < 0:2.1.10-18
Source44: import.info

%description
XML Pull Parser 2 (XPP2) is a simple and fast incremental XML parser.
NOTE: XPP2 is no longer developed and is on maintenance mode.
All active development concentrates on its successor XPP3/MXP1.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
%{summary}.

%package demo
Summary:        Samples for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}

%description demo
%{summary}.

%prep
%setup -q -n %{originalname}%{version}
# remove all binary libs and prebuilt classes
find \( -name *.class -o -name *.jar \) -delete

%patch0 -b .sav

# Fix encoding of licence file
iconv -f ISO-8859-1 -t UTF-8 LICENSE.txt > LICENSE.txt.utf8
mv LICENSE.txt.utf8 LICENSE.txt

%build
export CLASSPATH=$(build-classpath xml-commons-apis)
ant all api api.impl
CLASSPATH=$CLASSPATH:$(build-classpath junit):build/tests:build/lib/PullParser-2.1.10.jar
java AllTests

%install
# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}

cp -p build/lib/%{originalname}-intf-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-intf.jar
cp -p build/lib/%{originalname}-standard-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-standard.jar
cp -p build/lib/%{originalname}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
cp -p build/lib/%{originalname}-x2-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-x2.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}/api
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}/api_impl
cp -pr doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/api
cp -pr doc/api_impl/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/api_impl
rm -rf doc/{build.txt,api,api_impl}

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr src/java/samples/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%files
%doc LICENSE.txt README.html doc
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-intf.jar
%{_javadir}/%{name}-standard.jar
%{_javadir}/%{name}-x2.jar

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.10-alt4_23jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.10-alt4_22jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.10-alt4_16jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.1.10-alt4_11.3jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.10-alt4_7jpp6
- new jpp relase

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.10-alt4_6jpp5
- fixed docdir ownership

* Fri Feb 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.10-alt3_6jpp5
- rebuild for jpp5

* Fri May 25 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.10-alt3_6jpp1.7
- rebuild with java-1.4

* Wed Apr 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.10-alt2_6jpp1.7
- converted from JPackage by jppimport script

* Thu Mar 23 2006 Vladimir Lettiev <crux@altlinux.ru> 2.1.10-alt2
- Fix build with j2se-1.5

* Sun Apr 24 2005 Vladimir Lettiev <crux@altlinux.ru> 2.1.10-alt1
- Initial build for ALT Linux Sisyphus

