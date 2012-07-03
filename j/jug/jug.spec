Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: ant-log4j
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

%define with_native %{?_with_native:1}%{!?_with_native:0}
%define without_native %{!?_with_native:1}%{?_with_native:0}


Name:           jug
Version:        2.0.0
Release:        alt1_1jpp6
Epoch:          0
Summary:        Java UUID Generator
License:        Apache Software License 2.0
Url:            http://jug.safehaus.org/
Group:          Development/Java
Source0:        http://jug.safehaus.org/curr/jug-src.tar.gz
Source1:        jug-asl-2.0.0.pom
Source2:        jug-lgpl-2.0.0.pom
Patch0:         jug-makefile.patch
Patch1:         jug-UUIDTimer.patch
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 1.6.5
BuildRequires: junit >= 3.8.1
BuildRequires: ant-apache-log4j
Requires: ant-apache-log4j
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

%if %{without_native}
BuildArch:      noarch
%endif
Source44: import.info

%description
JUG is a pure java UUID generator, that can be used either
as a component in a bigger application, or as a standalone
command line tool (a la 'uuidgen'). UUIDs are 128-bit 
Universally Unique IDentifiers (aka GUID, Globally Unique
IDentifier used in Windows world).
JUG generates UUIDs according to the IETF UUID draft 
specification (and further clarified in UUID URN name space
IETF draft ) 8211; all 3 'official' types defined by the 
draft 8211; is fast, portable and Open Source (as well as
Free Software ).
You can use JUG in your application according to the
license terms of LGPL (Lesser General Public License); or,
from version 2.0 on, ASL.
From version 1.0.0 on, native code (invoked via JNI) for 
accessing Ethernet MAC address is included with Jug 
distribution. Big thanks to Paul Blankenbaker and DJ Hagberg
(amongst others) for their code contributions!
Note that using this functionality is optional: onlys
time+location - based generation needs MAC address, and
even with it, one can just pass the address from a
configuration file.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -c
mkdir lib
%patch0 -b .sav0
%patch1 -b .sav1

%build
%if %{with_native}
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 compile
pushd src/c
make EthernetAddress.h
make native
popd
%endif
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -DNativeLibDir=src/c jars test javadoc


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/%{name}-lgpl-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/
install -m 644 build/%{name}-asl-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/

# create unprefixed and unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir}
for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done
)

%add_to_maven_depmap org.safehaus.jug %{name}-asl %{version} JPP %{name}-asl
%add_to_maven_depmap org.safehaus.jug %{name}-lgpl %{version} JPP %{name}-lgpl

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-asl.pom
install -m 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-lgpl.pom

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr release-notes $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%doc %{_docdir}/%{name}-%{version}/*
%dir %{_docdir}/%{name}-%{version}
%{_javadir}/*.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Thu Oct 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt1_1jpp6
- fixed build

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt1_1jpp5
- new version

