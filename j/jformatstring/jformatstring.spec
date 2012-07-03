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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_with gcj_support

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

Name:           jformatstring
Version:        0
Epoch:          0
Release:        alt1_0.3.20081016svnjpp6
Summary:        Java library for format string checks
Group:          Development/Java
License:        GPLv2
URL:            https://jformatstring.dev.java.net/
# svn -q export -r 8 https://jformatstring.dev.java.net/svn/jformatstring/trunk/jFormatString jformatstring-0 --username guest --password guest && tar cjf jformatstring-0.tar.bz2 jformatstring-0
Source0:        jformatstring-0.tar.bz2
Provides:       jFormatString = %{epoch}:%{version}-%{release}
Obsoletes:      jFormatString < %{epoch}:%{version}-%{release}
BuildRequires: ant
BuildRequires: java-javadoc
BuildRequires: jpackage-utils
BuildRequires: junit4
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif

%description
This project is derived from Sun's implementation of java.util.Formatter. It 
is designed to allow compile time checks as to whether or not a use of format 
string will be erronous when executed at runtime.

This code is derived from the OpenJDK implementation, jdk1.7.0-b35. As such, 
it is licensed under the same license as OpenJDK, GPL v2 + the Classpath 
exception.

This project is preliminary, and the API is subject to change. The library 
produced by compiling this project is used by the FindBugs project. To avoid 
any licensing questions due to incompatible licenses (FindBugs is licensed 
under the LGPL), it is broken out as a separate project. While there may be 
some confusion/discussion about the licenses, the FindBugs project does not 
interpret the FindBugs LGPL license to be any stronger than GPL v2 + the 
Classpath exception.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires: java-javadoc
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q

mkdir lib
pushd lib
%{__ln_s} $(build-classpath junit4)
popd

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant}
%{javadoc} -d javadoc \
           -source 1.5 \
           -sourcepath src/java \
           -classpath build/classes:$(build-classpath junit4) \
           -link %{_javadocdir}/java \
           edu.umd.cs.findbugs.formatStringChecker

%install

%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p build/jFormatString.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/jFormatString-%{version}.jar
%{__ln_s} jFormatString-%{version}.jar %{buildroot}%{_javadir}/jFormatString.jar

%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/jFormatString-%{version}
%{__ln_s} jFormatString-%{version} %{buildroot}%{_javadocdir}/jFormatString

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif
%if %{gcj_support}

%post
if [ -x %{_bindir}/rebuild-gcj-db ]; then
    %{_bindir}/rebuild-gcj-db
fi

%postun
if [ -x %{_bindir}/rebuild-gcj-db ]; then
    %{_bindir}/rebuild-gcj-db
fi
%endif

%files
%doc LICENSE
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/jFormatString-%{version}.jar
%{_javadir}/jFormatString.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{_javadocdir}/jFormatString-%{version}
%{_javadocdir}/jFormatString

%changelog
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:0-alt1_0.3.20081016svnjpp6
- new version

