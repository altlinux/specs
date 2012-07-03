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


Name:           saxpath
Version:        1.0
Release:        alt2_4jpp6
Epoch:          0
Summary:        Java XPath engine for use on a variety of XML object models
License:        Open Source
URL:            http://sourceforge.net/projects/saxpath/
Group:          Development/Java
Source0:        http://downloads.sourceforge.net/saxpath/saxpath-%{version}.tar.gz
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/saxpath/saxpath/1.0-FCS/saxpath-1.0-FCS.pom
BuildRequires: ant
BuildRequires: ant-trax
BuildRequires: jpackage-utils >= 0:1.7.5
BuildArch:      noarch
Source44: import.info

%description
SAXPath is a Java XPath engine for use on a variety of XML object models
including dom4j, DOM and JavaBeans.

%package manual
Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}-FCS
mkdir -p src/conf
cat >> src/conf/MANIFEST.MF << EOF
Manifest-Version: 1.0
Extension-Name: org.saxpath
Specification-Title: saxpth
Specification-Version: 1.0 FCS
Specification-Vendor: werken digital.
Created-By: Ant 1.4.1
Implementation-Vendor:  werken digital.
Implementation-Version: 1.0
Implementation-Title: saxpath
EOF
find . -name "*.jar" | xargs rm

%build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 all

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 build/%{name}.jar \
$RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap saxpath %{name} %{version} JPP %{name}

%files
%doc build/doc/{*.css,*.html,images,style}
%{_javadir}/*
%{_datadir}/maven2/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_4jpp6
- new jpp release

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_3jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_3jpp5
- converted from JPackage by jppimport script

