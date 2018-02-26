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


Summary:        Automaton based regluar expression API for Java
Name:           jrexx
Version:        1.1.1
Release:        alt2_4jpp5
Epoch:          0
License:        LGPL
URL:            http://www.karneim.com/jrexx/
Group:          Development/Java
Source0:        jrexx-1.1.1-src.zip
Source1:        jrexx-build.xml
Source2:        http://repo1.maven.org/maven2/jrexx/jrexx/1.1.1/jrexx-1.1.1.pom
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

%description
jrexx is a powerful easy-to-use regular expression 
API for textual pattern matching. Technically jrexx 
uses a minimized deterministic FSA (finite state 
automaton) and compiles the textual representation 
of the regular expression into such an automaton. 
Besides the usual pattern matching functionality, 
jrexx provides an introspection API for exploration 
of the automaton's structure by 'states' and 
'transitions'. Since the automaton is deterministic 
and minimized the pattern matching alogorithm is 
extremly fast (compared to the java regular 
expression API in JDK1.4) and works with huge 
patterns and input texts. Since FSA can be handled 
as sets, jrexx also offers all basic set operations 
for complement, union, intersection and difference, 
which is not provided by other regex implementations 
(as far as we know). 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -T -c %{name}-%{version}
unzip -q %{SOURCE0}
cp %{SOURCE1} build.xml

%build
export LANG=en_US.ISO8859-1
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 dist

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p output/dist/lib/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/dist/jdoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt2_4jpp5
- fixed build with java 7

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_4jpp5
- new jpackage release

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_3jpp1.7
- converted from JPackage by jppimport script

