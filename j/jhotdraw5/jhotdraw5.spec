Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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

# Use rpmbuild --without gcj to disable gcj bits
%define with_gcj %{?_with_gcj:1}%{!?_with_gcj:0}

Name:           jhotdraw5
Version:        5.2
Release:        alt2_1jpp6
Summary:        2D Graphics Framework

Group:          Development/Java
License:        LGPL
URL:            http://www.jhotdraw.org/
Source0:        http://sourceforge.net/projects/jhotdraw/files/JHotDraw/5.2/JHotDraw5.2.zip
Source1:        %{name}-%{version}.pom
Patch0:         jhotdraw-BUILD.patch

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant

%if %{with_gcj}
BuildRequires: java-gcj-compat-devel >= 1.0.31
Requires(post): java-gcj-compat >= 1.0.31
Requires(postun): java-gcj-compat >= 1.0.31
%else
BuildArch:      noarch
%endif
Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0


%description
JHotDraw is a two-dimensional graphics framework for 
structured drawing editors that is written in Java. 
It is based on Erich Gamma's JHotDraw, which is copyright 
1996, 1997 by IFA Informatik and Erich Gamma.


%package javadoc
Summary:        Javadoc documentation for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documentation for %{name}
Group:          Development/Java
BuildArch: noarch

%description manual
%{summary}.


%prep
%setup -q -n JHotDraw -c
%patch0 -b .orig

%build
rm jhotdraw.jar
%{ant}  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Ddest.dir=$(pwd) -f build/BUILD.XML jar all


%install
install -d $RPM_BUILD_ROOT%{_javadir} \
        $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
        $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
install -m 644 jhotdraw.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

cp -pr documentation/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.jhotdraw jhotdraw %{version} JPP %{name}

%if %{with_gcj}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/%{name}*.jar
%if %{with_gcj}
%{_libdir}/gcj/%{name}
%endif
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}

%files manual
%{_docdir}/%{name}-%{version}


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 5.2-alt2_1jpp6
- built with java 6

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 5.2-alt1_1jpp6
- new version

