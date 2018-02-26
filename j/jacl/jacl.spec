Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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


Name:           jacl
Version:        1.4.1
Release:        alt1_1jpp5
Epoch:          0
Summary:        Java Tcl integration

Group:          Development/Java
License:        BSD
URL:            http://tcljava.sourceforge.net/docs/website/index.html
Source0:        http://downloads.sourceforge.net/tcljava/jacl1.4.1.tar.gz
Source1:        jacl-1.4.1.pom
Source2:        tcljava-1.4.1.pom


BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: make


Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
Jacl is a self-contained implementation of a Tcl interpreter,
written entirely in Java. Jacl also includes features that 
facilitate communication between a Java interpreter and a 
Tcl interpreter. Jacl is typically used to incorporate 
scripting functionality into an existing Java application. 
Jacl is the ideal solution for users that want to add Tcl 
scripting to a Java application, but don't want to deal 
with the complexities of native code that come with Tcl 
Blend.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}%{version}
mkdir -p build/dist

%build
cd build
../configure --prefix=$(pwd)/dist --with-jdk=%{_jvmdir}/java
make
make install

javadoc -classpath dist/lib/tcljava1.4.1/jacl.jar:dist/lib/tcljava1.4.1/tcljava.jar \
        -sourcepath ../src/jacl/:../src/tcljava/ -d dist/apidocs sunlabs.brazil.util.regexp tcl.lang

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 build/dist/lib/tcljava1.4.1/itcl.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/itcl-%{version}.jar
install -m 644 build/dist/lib/tcljava1.4.1/jacl.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/jacl-%{version}.jar
install -m 644 build/dist/lib/tcljava1.4.1/janino.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/janino-%{version}.jar
install -m 644 build/dist/lib/tcljava1.4.1/tcljava.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/tcljava-%{version}.jar
install -m 644 build/dist/lib/tcljava1.4.1/tjc.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/tjc-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)



# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jacl.pom
%add_to_maven_depmap jacl jacl %{version} JPP/%{name} jacl
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-tcljava.pom
%add_to_maven_depmap jacl tcljava %{version} JPP/%{name} tcljava

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/dist/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt1_1jpp5
- new version

