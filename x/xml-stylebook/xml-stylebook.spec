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

%define section devel

Name:           xml-stylebook
Version:        1.0
Release:        alt1_0.b3_xalan2.5jpp5
Epoch:          0
Summary:        Apache XML Stylebook
License:        ASL 2.0
URL:            http://xml.apache.org/
Group:          Development/Java
# cvs -d :pserver:anoncvs@cvs.apache.org:/home/cvspublic login
# cvs -d :pserver:anoncvs@cvs.apache.org:/home/cvspublic export -r HEAD xml-stylebook
Source0:        xml-stylebook-1.0-b2-src.tar.gz
Patch0:         xml-stylebook-image-printer.patch
BuildRequires: ant >= 0:1.6
BuildRequires: jpackage-utils >= 0:1.5
BuildArch:      noarch
Provides: stylebook = %{version}
Obsoletes: stylebook < 1.0-alt1

%description
XML Apache Stylebook.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .image-printer

%build
export OPT_JAR_LIST=:
export CLASSPATH=
ant -Ddebug=on

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}

cp -p bin/stylebook-1.0-b3_xalan-2.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
ln -s xml-stylebook.jar $RPM_BUILD_ROOT/%{_javadir}/stylebook.jar

%files
%{_javadir}/stylebook.jar
%doc LICENSE.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%changelog
* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b3_xalan2.5jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b3_xalan2.3jpp5
- converted from JPackage by jppimport script

* Sat Apr 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b3_xalan2.2jpp1.7
- converted from JPackage by jppimport script

* Wed Apr 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt0.2_0.b3_xalan2.2jpp1.7
- converted from JPackage by jppimport script

* Tue Apr 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt0.2.b3
- Updated to the latest SVN snapshot
- Use macros from rpm-build-java
- Patch0: set source and target options for javac

* Fri Sep 19 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt0.1.b3
- Ported to Sisyphus from JPackage
