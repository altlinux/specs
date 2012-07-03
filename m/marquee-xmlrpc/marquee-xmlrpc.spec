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

%define name	marquee-xmlrpc
%define version	1.3
%define release	1jpp

Name:		%{name}
Version:	%{version}
Release:	alt2_1jpp1.7
Epoch:		0
Summary:	An xmlrpc library
License:	LGPL
URL:		http://xmlrpc.sourceforge.net
Group:		Development/Java
Source0:	%{name}.tar.gz
Patch0:		marquee-build.patch
Patch1:		exceptions.patch
Patch2:		bigdecimal.patch
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: junit
BuildRequires: servletapi5
Requires: servletapi5
BuildArch:	noarch

%description 
A simple xmlrpc library for java.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
Javadoc for %{name}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation

%description manual
Documents for %{name}.

%prep
%setup -q -n xmlrpc
%patch0 -p0 -b .sav
%patch1 -p0 -b .sav
%patch2 -p0 -b .sav
find . -name "*.jar" -exec rm -f {} \;
find . -depth -name "CVS" -exec rm -rf {} \;
build-jar-repository -p lib/ \
junit \
servlet

%build
export LANG=en_US.ISO8859-1
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jars
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f javadoc.xml javadoc

%install

install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/lib/xmlrpc.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
#install -m 644 lib/minml.jar $RPM_BUILD_ROOT%{_javadir}/marquee-minml-%{version}.jar
install -m 644 build/lib/objectcomm.jar $RPM_BUILD_ROOT%{_javadir}/marquee-objectcomm-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 644 doc/*.html  $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr doc/images  $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 644 doc/*.pdf  $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/Marquee_XML-RPC-Library.pdf

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%files
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_1jpp1.7
- fixed build with java 7

* Tue Jul 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp1.7
- converted from JPackage by jppimport script

