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


Summary:        Multipart input stream parser
Name:           pell-multipart
Version:        1.30
Release:        alt1_0.rc1.4jpp5
Epoch:          0
License:        LGPL
URL:            http://www.geocities.com/jasonpell/programs.html
Group:          Development/Java
Source0:        MultipartRequest-1.30rc1.zip
Source1:        pell-multipart-build.xml
Source2:        http://repo1.maven.org/maven2/opensymphony/pell-multipart/2.1.5/pell-multipart-2.1.5.pom
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: servlet_2_4_api
Requires: servlet_2_4_api
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

%description
Parses a Multipart form data input stream 
and writes out any files found, making 
available a hashtable of other url parameters.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package demo
Summary:        Samples for %{name}
Group:          Development/Documentation

%description demo
%{summary}.

%prep
%setup -T -c %{name}-%{version}
unzip -q %{SOURCE0}
cp %{SOURCE1} build.xml
find . -name "*.jar" -exec rm {} \;

%build
export CLASSPATH=$(build-classpath servlet_2_4_api)
ant 

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p output/dist/lib/%{name}-%{version}rc1.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
%add_to_maven_depmap opensymphony %{name} 2.1.5 JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/dist/jdoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%doc LICENSE lesser.txt
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}-%{version}

%changelog
* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.30-alt1_0.rc1.4jpp5
- new jpackage release

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.30-alt1_0.rc1.3jpp1.7
- converted from JPackage by jppimport script

