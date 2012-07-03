BuildRequires: /proc
BuildRequires: jpackage-compat
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


Name:		xmlpull-api
Version:	1.1.4
Release:	alt2_1jpp1.7
Epoch:		0
Summary:	XmlPull v1 API is a simple to use XML pull parsing API 
License:	Public Domain
Url:		http://www.xmlpull.org/
Group:		Development/Java
Source0:	%{name}-%{version}.tar.gz
##cvs -d :pserver:anonymous@cvs.xmlpull.org:/l/extreme/cvspub login (password='cvsanon')
##cvs -d :pserver:anonymous@cvs.xmlpull.org:/l/extreme/cvspub export -r XMLPULL_1_1_4 xmlpull-api

BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 1.4.1
BuildRequires: junit >= 3.8.1

BuildArch:	noarch

%description
XmlPull v1 API is a simple to use XML pull parsing API that was
designed for simplicity and very good performance both in constrained
environment such as defined by J2ME and on server side when used in
J2EE application servers.

%prep
%setup -q -n %{name}

sed -i -e s:"<property name=\"version\" value=\"1_1_3_1\"/>":"<property name=\"version\" value=\"1_1_4\"/>":g build.xml

%build
export LANG=en_US.ISO8859-1
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/lib/xmlpull_1_1_4.jar \
		$RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

# create unprefixed and unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir}
for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done
)

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp *.txt *.html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%doc %{_docdir}/%{name}-%{version}/*
%dir %{_docdir}/%{name}-%{version}
%{_javadir}/*.jar


%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt2_1jpp1.7
- fixed build with java 7

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt1_1jpp1.7
- converted from JPackage by jppimport script

