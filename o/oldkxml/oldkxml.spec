Packager: Igor Vlasenko <viy@altlinux.ru>
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


Name:		oldkxml
Version:	1.21
Release:	alt1_6jpp6
Epoch:		0
Summary:	XML pull parser and writer suitable for all Java platforms
License:	Enhydra Public License
URL:		http://kxml.objectweb.org/
Group:		Development/Java
Source0:	http://kxml.objectweb.org/software/downloads/current/kxml-source.zip
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7
BuildArch:      noarch
Source44: import.info

%description
The kXML project provides an XML pull parser and writer suitable for all
Java platforms including the Java 2 Micro Edition (CLDC/MIDP/CDC).
Because of its small footprint size, it is especially suited for Applets
or Java appications running on mobile devices like Palm Pilots or MIDP
enabled cell phones

kXML was originally developed at the AI Unit of the University of
Dortmund as a "side product" of the COMRIS project. In the COMRIS
project, the API was used in the Information Layer module(s) to parse
XMLified FIPA messages and to generate template based XHTML pages. The
template based XHTML generation is currently used in the MLnet teaching
server, too. kXML is also used in the Enhydra kXML-RPC and kSOAP
projects.

kXML key features are:

    * XML Namespace support
    * "Relaxed" mode for parsing HTML or other SGML formats
    * Small Memory footprint
    * A Pull-based parser for simplified parsing of nested / modularized XML
      structures
    * XML writing support including namespace handling
    * Optional kDOM
    * Optional WAP support (WBXML/WML)

%package	javadoc
Summary:	Javadoc for %{name}
Group:		Development/Documentation
BuildArch: noarch

%description	javadoc
Javadoc for %{name}.

%prep
%setup -q -c

%build
%javac `find . -name "*.java"`
mkdir -p api
%javadoc -d api `find . -name "*.java"`
cat > MANIFEST.MF << EOF
Manifest-Version: 1.0
EOF
%jar cvmf MANIFEST.MF %{name}.jar `find . -name "*.class"`

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

# javadoc
install -p -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
(cd $RPM_BUILD_ROOT%{_javadocdir} && ln -sf %{name}-%{version} %{name})

%files
%{_javadir}/*.jar

%files javadoc
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/*
%ghost %dir %{_javadocdir}/%{name}

%changelog
* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.21-alt1_6jpp6
- new version

