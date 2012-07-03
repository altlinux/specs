Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define real_name	rhino
%define oldname		old%{real_name}
%define cvs_version	1_5
%define tar_version	15
%define pre		R3


Name:		rhino15
Version:	1.5
Release:	alt2_0.R3.6jpp5
Epoch:		0
Summary:	JavaScript for Java
License:	MPL
Source0:	ftp://ftp.mozilla.org/pub/js/%{real_name}%{tar_version}%{pre}.zip
Source1:	http://java.sun.com/products/jfc/tsc/articles/treetable2/downloads/src.zip
Url:		http://www.mozilla.org/rhino/
Group:		Development/Java
BuildRequires: ant
BuildArch:	noarch
Provides:	oldrhino
Obsoletes:	oldrhino < 0:1.6

%description
Rhino is an open-source implementation of JavaScript written entirely
in Java. It is typically embedded into Java applications to provide
scripting to end users.

%package manual
Summary:	Manual for %{name}
Group:		Development/Java

%description manual
Documentation for %{name}.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Documentation

%description javadoc
Javadoc for %{name}.

%prep
%setup -n %{real_name}%{cvs_version}%{pre}

%build
perl -p -i -e 's|<javadoc sourcefiles="\${apiClasses}"|<javadoc sourcefiles="org.mozilla.\*"|;' build.xml
perl -p -i -e 's|<get src.*>||;' toolsrc/build.xml
# Fix path between manual and javadocs.
perl -pi -e 's|"apidocs/index.html"|"%{_javadocdir}/%{name}-%{version}/index.html"|' docs/doc.html
install -d -m 755 build
install -m 644 %{SOURCE1} build/swingExSrc.zip
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 -Dbuild.compiler=modern jar javadoc

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/%{real_name}%{cvs_version}%{pre}/js.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && ln -sf %{name}-%{version}.jar oldjs-%{version}.jar)
(cd $RPM_BUILD_ROOT%{_javadir} && ln -sf %{name}-%{version}.jar %{oldname}-%{version}.jar)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}
cp -pr build/%{real_name}%{cvs_version}%{pre}/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}
rm -rf build/%{real_name}%{cvs_version}/docs/apidocs

%files
%{_javadir}/*

%files manual
%doc build/%{real_name}%{cvs_version}%{pre}/docs/*

%files javadoc
%{_javadocdir}/%{oldname}-%{version}

%changelog
* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_0.R3.6jpp5
- fixed build with java 5

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_0.R3.6jpp1.7
- converted from JPackage by jppimport script

