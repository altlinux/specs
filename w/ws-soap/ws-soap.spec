Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: servletapi4
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

%define gcj_support 0

%define oname		soap
%define cvs_version	2_3_1

Name:		ws-soap
Version:	2.3.1
Release:	alt1_5jpp5
Epoch:		0
Summary:        Simple Object Access Protocol
License:        Apache Software License
Group:          Development/Java
Url:            http://ws.apache.org/soap/
Source0:        http://www.apache.org/dist/ws/soap/version-2.3.1/soap-src-2.3.1.tar.gz
Requires: jpackage-utils >= 0:1.6
Requires: ejb
Requires: jaf
Requires: javamail
Requires: servletapi5
Requires: xerces-j2
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 1.6.5
BuildRequires: ejb
BuildRequires: jaf
BuildRequires: javamail
BuildRequires: servletapi5
BuildRequires: xerces-j2
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%description
The Apache Soap project is an implementation of the draft W3C protocol
by the same name. It is based on, and supersedes, the IBM SOAP4J
implementation.

From the draft W3C specification: SOAP is a lightweight protocol for
exchange of information in a decentralized, distributed environment. It
is an XML based protocol that consists of three parts: an envelope that
defines a framework for describing what is in a message and how to
process it, a set of encoding rules for expressing instances of
application-defined datatypes, and a convention for representing remote
procedure calls and responses.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{cvs_version}
find . -name "*.jar" -exec rm -f {} \;

%build
export CLASSPATH=$(build-classpath ejb jaf javamail servletapi4 xerces-j2)
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 compile
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 javadocs

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/lib/%{oname}.jar \
            $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%if %{gcj_support}
%post
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%files
%doc LICENSE
%{_javadir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}

%changelog
* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_5jpp5
- fixed build with java 5

* Sun Oct 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_5jpp1.7
- converted from JPackage by jppimport script

