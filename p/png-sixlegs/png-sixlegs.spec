BuildRequires: /proc
BuildRequires: jpackage-1.4-compat
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

%define name            png-sixlegs
%define version         1.3.0
%define release         2jpp

Name:           %{name}
Version:        %{version}
Release:        alt1_2jpp1.7
Epoch:          0
Summary:        PNG decoder
License:        GPL with library exception
Group:          Development/Java
Source0:        http://ovh.dl.sourceforge.net/sourceforge/javapng/%{name}-%{version}.tar.gz
URL:            http://www.sixlegs.com/software/png/
BuildRequires: jpackage-utils > 1.5
BuildRequires: ant
Buildarch:      noarch
Buildroot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
PNG decoder. Supports all valid bit depths (grayscale/color), interlacing,
paletted images, alpha channel/transparency, gamma correction, access to all
standard chunks, private chunk handling, and progressive display.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
# remove all CVS files
for dir in `find . -type d -name CVS`; do rm -rf $dir; done
for file in `find . -type f -name .cvsignore`; do rm -rf $file; done

%build
mkdir build
javac -d build -sourcepath src src/main/com/sixlegs/image/png/*.java
cd build
jar c0vf %{name}.jar com

%install
#jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -D -m 644 build/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
#javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp LICENSE.txt README.txt $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%files
%doc LICENSE.txt README.txt
%{_javadir}/*.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}

%changelog
* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_2jpp1.7
- converted from JPackage by jppimport script

