Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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


Name:           tlddoc
Version:        1.3
Release:	alt1_3jpp6
Epoch:          0
Summary:        Tag Library Documentation Generator
License:        BSD
URL:            https://taglibrarydoc.dev.java.net/
Group:          Development/Java
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs login
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -r TLDDOC-1_3 -d tlddoc-1.3 taglibrarydoc && tar cjf tlddoc-1.3.tar.bz2 tlddoc-1.3
Source0:        tlddoc-1.3.tar.bz2
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/taglibrarydoc/tlddoc/1.3/tlddoc-1.3.pom
Patch0:         tlddoc-1.2-build_xml.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit >= 0:1.6
BuildRequires: jpackage-utils >= 0:1.5
BuildRequires: javacc
BuildArch:      noarch
Source44: import.info

%description
Tag Library Documentation Generator is a utility for automatically 
generating javadoc-style documentation for JavaServer PagesTM  
(JSP TM) Technology Tag Libraries. It accepts a set of tag libraries 
as input, and generates a set of HTML files as output. It can also be 
used to generate tag library documenation for JavaServer Faces UI
components.
Included in the output is a full description of each defined tag 
library, the tags contained within those tag libraries, and how to 
use those tags. 

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
Requires: xpp2 >= 0:2.1.10

%description demo
%{summary}.

%prep
%setup -q
%patch0 -p0
# a.jar and b.jar are test jars that contain no binaries
#find . -name "*.jar" | xargs -t rm

%build
export CLASSPATH=
export OPT_JAR_LIST="ant/ant-nodeps javacc"

cd taglibrarydoc
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -DJAVACC_HOME=%{_javadir} test

%install

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p taglibrarydoc/dist/taglibrarydoc-`echo %{version} | sed -e 's/\./_/'`/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# pom
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap taglibrarydoc tlddoc %{version} JPP %{name}

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr taglibrarydoc/build/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# manual
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr taglibrarydoc/doc/* %{buildroot}%{_docdir}/%{name}-%{version}

%files
%doc taglibrarydoc/license.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_3jpp6
- added pom

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp5
- fixed repocop warnings

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_2jpp1.7
- converted from JPackage by jppimport script

