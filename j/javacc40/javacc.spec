BuildRequires: /proc
BuildRequires: jpackage-compat
%define newname javacc
# Copyright (c) 2000-2005, JPackage Project
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


Name:           javacc40
Version:        4.0
Release:        alt1_3jpp5
Epoch:          0
Summary:        A parser/scanner generator for java
License:        BSD
Source0:	javacc-4.0src.tar.gz
Source1:	javacc
Source2:	jjdoc
Source3:	jjtree
URL:            https://javacc.dev.java.net/
Group:          Development/Java
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Requires: jpackage-utils >= 0:1.5
BuildRequires: ant /bin/bash ant-junit junit >= 0:3.8.1
Conflicts: javacc

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description 
Java Compiler Compiler (JavaCC) is the most popular parser generator for use
with Java applications. A parser generator is a tool that reads a grammar
specification and converts it to a Java program that can recognize matches to
the grammar. In addition to the parser generator itself, JavaCC provides other
standard capabilities related to parser generation such as tree building (via
a tool called JJTree included with JavaCC), actions, debugging, etc.

%package manual
Summary:        Manual for %{name}
Group:          Development/Documentation

%description manual
Manual for %{name}.

%package demo
Summary:        Examples for %{name}
Group:          Development/Documentation

%description demo
Examples for %{name}.

%prep
%setup -q -n javacc
cp %{SOURCE1} javacc
cp %{SOURCE2} jjdoc
cp %{SOURCE3} jjtree
mv www/doc .

%build
ant \
  -Dversion=%{version} \
  jar

%install
rm -fr $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 bin/lib/javacc.jar $RPM_BUILD_ROOT%{_javadir}/%{newname}-%{version}.jar
ln -s %{newname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{newname}.jar
install -d -m 755 $RPM_BUILD_ROOT/%{_bindir}
install -m 755 javacc jjdoc jjtree $RPM_BUILD_ROOT/%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp -pr examples $RPM_BUILD_ROOT/%{_datadir}/%{name}

%files
%{_javadir}/*.jar
%doc LICENSE README
#%defattr(0755,root,root,0755)
/usr/bin/*

%files manual
%doc doc/*

%files demo
%{_datadir}/%{name}/*

%changelog
* Sat Feb 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.0-alt1_3jpp5
- compat version

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:4.0-alt1_3jpp1.7
- converted from JPackage by jppimport script

* Fri Mar 03 2006 Mikhail Zabaluev <mhz@altlinux.ru> 4.0-alt1
- 4.0
- Use macros from rpm-build-java
- Patch0: set target version for javac

* Tue Sep 09 2003 Mikhail Zabaluev <mhz@altlinux.ru> 3.2-alt1
- Released for ALT Linux
