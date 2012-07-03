# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
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

%define readln_min_ver  5.0
%define debug_package %{nil}

Name:           libreadline-java
Version:        0.8.0
Release:        alt2_12jpp6
Epoch:          0
Summary:        Java wrapper for the GNU-readline library
License:        LGPL
Source0:        http://download.sourceforge.net/java-readline/libreadline-java-0.8.0-src.tar.gz
Url:            http://java-readline.sf.net/
Requires:       readline >= 0:%{readln_min_ver}
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  libreadline-devel
BuildRequires:  libtinfo-devel
Provides:       java_readline
Provides:       gnu.readline
Group:          Development/Java
##AutoReqProv:    no
Source44: import.info

%description
Java-Readline is a port of GNU Readline for Java.  Or, to be more 
precise, it is a JNI-wrapper to Readline. It is distributed under 
the LGPL.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
find . -name "*.jar" -exec rm -f {} \;
%__subst s,termcap,tinfo, src/native/Makefile

%build
#export JAVA_HOME=%{java_home}
export PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH
%__make T_LIBS=JavaReadline
%__make apidoc

%install
# jar
%__mkdir_p %{buildroot}%{_jnidir}
%__install -m 644 %{name}.jar %{buildroot}%{_jnidir}/%{name}-%{version}.jar
(cd %{buildroot}%{_jnidir} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)
# lib
%__mkdir_p %{buildroot}%{_libdir}
%__install -m 755 libJavaReadline.so %{buildroot}%{_libdir}/libJavaReadline.so.%{version}
(cd %{buildroot}%{_libdir} && ln -sf libJavaReadline.so.%{version} libJavaReadline.so)

# javadoc
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -a api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%__ln_s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc ChangeLog NEWS README README.1st VERSION
%{_libdir}/*.so*
%{_jnidir}/*.jar

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Sun Feb 26 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.8.0-alt2_12jpp6
- build with new jnidir

* Sun Mar 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.8.0-alt2_12jpp5
- fixed repocop warnings

* Mon May 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.8.0-alt2_11jpp1.7
- fixed requires

* Tue May 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.8.0-alt1_11jpp1.7
- converted from JPackage by jppimport script

