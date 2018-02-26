BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2010, JPackage Project
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
Release:        alt4_7jpp6
Epoch:          0
License:        ASL-style
URL:            http://www.extreme.indiana.edu/xgws/xsoap/xpp/
Group:          Development/Java
Source0:        http://www.extreme.indiana.edu/xgws/xsoap/xpp/download/PullParser2/PullParser2.1.10.tgz
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/pull-parser/pull-parser/2.1.10/pull-parser-2.1.10.pom
Patch0:         xpp2-build_xml.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
Requires:       xml-commons-jaxp-1.3-apis
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  jpackage-utils
BuildRequires:  junit
BuildRequires:  xml-commons-jaxp-1.3-apis
BuildArch:      noarch
Source44: import.info

%description
XML Pull Parser 2 (XPP2) is a simple and fast incremental XML parser.
NOTE: XPP2 is no longer developed and is on maintenance mode. 
All active developement concentrates on its successor XPP3/MXP1

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Manual for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%package demo
Summary:        Samples for %{name}
Group:          Development/Documentation
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description demo
%{summary}.

%prep
%setup -q -n %{originalname}%{version}
# remove all binary libs
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}
%{__mv} LICENSE.txt LICENSE.txt.orig
%{_bindir}/iconv -f iso8859-1 -t utf8 -o LICENSE.txt LICENSE.txt.orig
%patch0 -p0 -b .sav0

%build
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
export CLASSPATH=$(build-classpath xml-commons-jaxp-1.3-apis)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 all api api.impl
export CLASSPATH=$CLASSPATH:$(build-classpath junit):`pwd`/build/tests:build/lib/PullParser-%{version}.jar
%{java} AllTests

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}

cp -p build/lib/%{originalname}-intf-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-intf-%{version}.jar
cp -p build/lib/%{originalname}-standard-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-standard-%{version}.jar
cp -p build/lib/%{originalname}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
cp -p build/lib/%{originalname}-x2-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-x2-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap pull-parser pull-parser %{version} JPP %{name}

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/api
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/api_impl
cp -pr doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/api
cp -pr doc/api_impl/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/api_impl
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

rm -rf doc/{build.txt,api,api_impl}

# manual
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}
cp -pr doc/* $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}
cp -p README.html $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}
cp -p LICENSE.txt $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr src/java/samples/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/%{name}

%files
%{_datadir}/doc/%{name}-%{version}/README.html
%{_datadir}/doc/%{name}-%{version}/LICENSE.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}-intf.jar
%{_javadir}/%{name}-intf-%{version}.jar
%{_javadir}/%{name}-standard.jar
%{_javadir}/%{name}-standard-%{version}.jar
%{_javadir}/%{name}-x2.jar
%{_javadir}/%{name}-x2-%{version}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%{_datadir}/doc/%{name}-%{version}
%{_datadir}/doc/%{name}

%files demo
%{_datadir}/%{name}-%{version}
%{_datadir}/%{name}

%changelog
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

