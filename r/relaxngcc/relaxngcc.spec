# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
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

%define gcj_support 0

%define cvsdate 20031218

Summary:        RELAX NG Compiler Compiler
Name:           relaxngcc
Version:        1.12
Release:        alt2_2jpp6
Epoch:          0
License:        Apache Software License-like
URL:            http://relaxngcc.sourceforge.net/
Group:          Development/Java
Source0:	http://prdownloads.sourceforge.net/relaxngcc/relaxngcc-20031218.zip
Source1:	relaxngcc-build.xml
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7
BuildRequires:  ant-nodeps
BuildRequires:  jakarta-commons-jelly
BuildRequires:  msv-msv
BuildRequires:  msv-xsdlib
BuildRequires:  relaxngDatatype
#BuildRequires:  xerces-j2
#BuildRequires:  xml-commons-apis
Requires:  ant >= 0:1.7
Requires:  jakarta-commons-jelly
Requires:  msv-msv
Requires:  msv-xsdlib
Requires:  relaxngDatatype
#Requires:  xerces-j2
#Requires:  xml-commons-apis
%if %{gcj_support}
BuildRequires:          java-gcj-compat-devel
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info

%description
RelaxNGCC is a tool for generating Java source code from a 
given RELAX NG grammar. By embedding code fragments in the 
grammar like yacc or JavaCC, you can take appropriate 
actions while parsing valid XML documents against the 
grammar.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n %{name}-%{cvsdate}
cp %{SOURCE1} build.xml
mkdir lib
for j in $(find . -name "*.jar"); do
	mv $j $j.no
done
cp relaxngcc.jar.no lib/bootstrap-relaxngcc.jar

%build
pushd lib
#BUILD/relaxngcc-20031218/msv.jar.no
ln -sf $(build-classpath msv-msv) .
#BUILD/relaxngcc-20031218/relaxngDatatype.jar.no
ln -sf $(build-classpath relaxngDatatype) .
#BUILD/relaxngcc-20031218/xerces.jar.no
#ln -sf $(build-classpath xerces-j2) .
#BUILD/relaxngcc-20031218/xsdlib.jar.no
ln -sf $(build-classpath msv-xsdlib) .
#
ln -sf $(build-classpath commons-jelly) .
popd

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadoc

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p %{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr doc/en/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.12-alt2_2jpp6
- new jpp relase

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.12-alt2_1jpp5
- fixed build with java 5

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.12-alt1_1jpp1.7
- converted from JPackage by jppimport script

