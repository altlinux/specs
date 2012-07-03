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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}


Name:           bytecode
Version:        0.92
Release:        alt1_1jpp6
Epoch:          0
Summary:        Java bytecode manipulation library
License:        LGPLv2+
Group:          Development/Java
URL:            http://biojava.org/
# svn -q export svn://code.open-bio.org/biojava/bytecode/tags/bytecode-0_92 bytecode-0.92 && tar cjf bytecode-0.92.tar.bz2 bytecode-0.92
# This is actually post 0.92, trunk revision 7230
# svn -q export -r 7230 svn://code.open-bio.org/biojava/bytecode/trunk bytecode-0.92 && tar cjf bytecode-0.92.tar.bz2 bytecode-0.92
Source0:        bytecode-0.92.tar.bz2
Patch0:         bytecode-buildxml.patch
Patch1:         bytecode-junit.patch
Patch2:         bytecode-buildxml.tests.patch
Requires: jpackage-utils
BuildRequires: ant
BuildRequires: jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
The library presents itself as a collection of routines to manipulate Java
bytecode. It allows for the dynamic creation of Java class files without
using of Javac. Such tailored code can be used, i.e. as for the upstream's
motivation of the BioJava developers, to generate implementations of
Hidden Markov Models. It thus acts much like inline assembly for Java.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch0 -p0 -b .sav0
%patch1 -p1 -b .sav1
%patch2 -p1 -b .sav2

%{__mkdir_p} demos resources

%build
export OPT_JAR_LIST=:
export CLASSPATH=
%{ant} -Dversion=%{version} dist

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__install} -p -m 0644 dist/bytecode-%{version}/lib/bytecode.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr dist/bytecode-%{version}/docs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.92-alt1_1jpp6
- new version

