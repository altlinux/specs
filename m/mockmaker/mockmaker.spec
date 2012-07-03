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

%define name		mockmaker
%define version		1.12.0
%define release		2jpp


Name:		%{name}
Summary:	MockMaker
Url:		http://mockmaker.sourceforge.net/
Version:	%{version}
Release:	alt2_2jpp1.7
Epoch:		0
License:	BSD style
Group:		Development/Java
BuildArch:	noarch
Source0:	mockmaker-1.12.0-src.tar.gz
##cvs -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/mockmaker login
##cvs -z3 -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/mockmaker export -r HEAD MockMaker
Patch0:		mockmaker-1.12.0-build_xml.patch
BuildRequires: ant
BuildRequires: junit
BuildRequires: qdox161
BuildRequires: mockobjects
Requires: mockobjects
#Requires: qdox

%description
MockMaker is a program for creating source code for 
mock object classes. Given an interface, it writes 
the source code for a mock object class that implements 
the interface and allows instances of that class to 
have expectations set about how many times a method 
is called, what parameters each method is called with, 
and to pre-set return values for methods. In many cases 
(possibly most cases), the classes produced by MockMaker 
are exactly what you want a mock class to do.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Documentation

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n MockMaker
chmod -R go=u-w *
find . -name "*.jar" -exec rm -f {} \;
pushd lib
    ln -sf $(build-classpath ant) ant.jar
    ln -sf $(build-classpath junit) junit.jar
    ln -sf $(build-classpath mockobjects-core) mmmockobjects.jar
    ln -sf $(build-classpath qdox161) qdox.jar
popd

%patch0 -b .sav

%build
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4

%install
unzip -q MockMaker1_12_0.zip

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 MockMaker/lib/MockMaker.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# config + tests
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/config
cp -p MockMaker/mockmaker.cfg $RPM_BUILD_ROOT%{_datadir}/%{name}/config
cp -p MockMaker/old.cfg $RPM_BUILD_ROOT%{_datadir}/%{name}/config
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/tests
cp -p MockMaker/mockmaker/tests/AcceptableInterface.class $RPM_BUILD_ROOT%{_datadir}/%{name}/tests

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%files
%doc MockMaker/*.html
%{_javadir}/*
%{_datadir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.12.0-alt2_2jpp1.7
- fixed build with new qdox

* Mon Jul 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.12.0-alt1_2jpp1.7
- converted from JPackage by jppimport script

