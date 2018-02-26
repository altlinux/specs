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

%define namedversion 1

Name:           google-parent
Version:        1
Release:        alt1_0.760.1jpp6
Epoch:          0
Summary:        Google code parent pom
License:        ASL 2.0
Group:          Development/Java
URL:            http://code.google.com/p/google-maven-repository
Source0:        http://google-maven-repository.googlecode.com/svn-history/r760/repository/com/google/google/1/google-1.pom
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires: maven2 >= 0:2.0.8
BuildRequires: jpackage-utils >= 0:1.7.5
BuildArch:      noarch
Source44: import.info

%description
Google code projects parent pom.

%prep
%setup -q -c -T

%build
#nope

%install

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE0} %{buildroot}%{_datadir}/maven2/poms/JPP-google.pom
%add_to_maven_depmap com.google google %{namedversion} JPP google

%files
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%changelog
* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1-alt1_0.760.1jpp6
- new version

