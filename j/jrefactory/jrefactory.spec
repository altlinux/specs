BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
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

#def_with gcj_support
%bcond_with gcj_support
#def_with netbeans
%bcond_with netbeans

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           jrefactory
Version:        2.9.19
Release:        alt2_1jpp6
Epoch:          0
Summary:        JRefactory and Pretty Print
License:        ASL-like
Group:          Development/Java
URL:            http://jrefactory.sourceforge.net/
# cvs -Q -z3 -d:pserver:anonymous@jrefactory.cvs.sourceforge.net:/cvsroot/jrefactory co -rJRefactory-2_9_19 -P -d jrefactory-2.9.19 JRefactory && tar cjf jrefactory-2.9.19.tar.bz2 jrefactory-2.9.19
Source0:        jrefactory-2.9.19.tar.bz2
Source1:        jrefactory.pom
Patch0:         jrefactory-netbeans.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
BuildRequires:  ant
BuildRequires:  jpackage-utils >= 0:1.5
%if %with netbeans
BuildRequires:  netbeans-platform
%endif
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
JRefactory provides a variety of refactoring and pretty printing tools

%prep
%setup -q
%if %without netbeans
%patch0 -p0 -b .sav0
rm -r src/org/acm/seguin/ide/netbeans
%endif

mv src/settings/.Refactory settings/sample

perl -p -i -e 's|^Class-Path:.*||' \
        src/meta-inf/refactory.mf

%build
%if %without netbeans
export CLASSPATH=
%else
export CLASSPATH=%{_datadir}/netbeans/platform11/core/core.jar
%endif
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar

%install

mkdir -p %{buildroot}%{_javadir}
cp -p ant.build/lib/jrefactory.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} ${jar/-%{version}/}; done)

mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap jrefactory jrefactory %{version} JPP %{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc docs/{*.html,*.jpg,*.gif,*.txt} settings/sample
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.9.19-alt2_1jpp6
- built with java 6 due to com.sun.image.codec.jpeg

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.9.19-alt1_1jpp6
- new jpp relase

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.8.9-alt2_6jpp5
- fixed build with java 5

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.8.9-alt1_6jpp1.7
- converted from JPackage by jppimport script

