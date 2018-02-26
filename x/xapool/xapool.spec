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


Name:		xapool
Summary:	XAPOOL: open source XA Pool
Url:		http://xapool.experlog.com/
Version:	1.5.0
Release:	alt3_3jpp6
Epoch:		0
License:	LGPL
Group:		Development/Java
BuildArch:	noarch
Source0:	xapool-%{version}-src.tgz
Source1:        http://repo1.maven.org/maven2/com/experlog/xapool/1.5.0/xapool-1.5.0.pom
Patch0:         xapool-build.patch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
BuildRequires: jta_1_0_1B_api
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info


%description
XAPool is an open source XA Pool !
It allows to pool objects, JDBC connections 
and XA connections 

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}-src
chmod -R go=u-w *
find . -name "*.jar" -exec rm -f {} \;
%patch0 -b .sav0

%build
pushd externals
ln -sf $(build-classpath jta_1_0_1B_api) jta-spec1_0_1.jar
popd

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 output/dist/lib/%{name}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
%add_to_maven_depmap com.experlog %{name} %{version} JPP %{name}
# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/dist/jdoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} 

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt3_3jpp6
- jpp 6 release

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt3_2jpp5
- new jpp release

* Thu Feb 26 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt3_1jpp5
- fixed build

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt2_1jpp5
- fixed build with java 5

* Thu Nov 22 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

