Packager: Igor Vlasenko <viy@altlinux.ru>
%define oldname jal
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



Name:           sg-jal
Version:        20031117
Release:        alt1_4jpp5
Epoch:          0
Summary:        A partial STL port by the C++ Standard Template Library authors
License:        X11-like
Source0:	http://vigna.dsi.unimi.it/jal/jal-20031117-src.tar.gz
URL:            http://vigna.dsi.unimi.it/jal/
Group:          Development/Java
BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: /bin/bash /usr/bin/perl
BuildRequires: /usr/bin/perl

%description 
A partial STL port by the C++ Standard Template Library authors.

%package javadoc
Summary:        Javadoc for %{oldname}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{oldname}.

%prep
%setup -q -n %{oldname}-%{version}

%build
./instantiate -n byte bytes
./instantiate -n short shorts
./instantiate -n char chars
./instantiate -n int ints
./instantiate -n long longs
./instantiate -n float floats
./instantiate -n double doubles
./instantiate Object objects
./instantiate String strings
mkdir -p src/jal
mv bytes shorts chars ints longs floats doubles objects strings src/jal
ant \
  -Dversion=%{version} \
  -Dj2se.apiurl=%{_javadocdir}/java \
  jar javadoc

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{oldname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/
ln -s %{oldname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{oldname}.jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}
ln -s %{oldname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{oldname} # ghost symlink

%files
%doc README
%{_javadir}/*.jar

%files javadoc
%doc %{_javadocdir}/%{oldname}-%{version}
%doc %{_javadocdir}/%{oldname}

%changelog
* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:20031117-alt1_4jpp5
- use default jpp profile

* Mon Sep 08 2008 Igor Vlasenko <viy@altlinux.ru> 0:20031117-alt1_3jpp5
- converted from JPackage by jppimport script

