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


Name:           excalibur-io
Version:        1.1
Release:        alt1_2jpp1.7
Epoch:          0
Summary:        Excalibur IO Utils
License:        Apache Software License
URL:            http://excalibur.apache.org/
Group:          Development/Java
Source0:        http://www.apache.org/dist/avalon/excalibur/components/deprecated/io/excalibur-io-1.1.tar.bz2
Source1:        excalibur-io-build.xml
BuildRequires: ant
BuildRequires: jpackage-utils >= 0:1.6
BuildArch:      noarch

%description
Avalon Excalibur was created in order to ease development of new
projects. To that end, Excalibur contains a number of ready to use
components and utilities that handle everything from command line
parsing to thread concurrency management.
The components in the Excalibur package have been well tested and do
work reliably.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

# -----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
# remove all binary libs
for j in $(find . -name "*.jar"); do
	mv $j $j.no
done
mkdir -p src/java
pushd src/java
unzip -q ../../src.zip
popd
cp %{SOURCE1} build.xml


# -----------------------------------------------------------------------------

%build

ant -Dnoget=true dist

# -----------------------------------------------------------------------------

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}/excalibur
cp -p dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/excalibur/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/excalibur && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -sf %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# -----------------------------------------------------------------------------

%files
%doc KEYS LICENSE.txt
%{_javadir}/excalibur/*.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

# -----------------------------------------------------------------------------

%changelog
* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

