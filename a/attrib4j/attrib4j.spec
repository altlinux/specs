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


Summary:        Custom metadata for elements of Java class or interface
Name:           attrib4j
Version:        0.9.0
Release:        alt2_4jpp5
Epoch:          0
License:        LGPL
URL:            http://attrib4j.sourceforge.net/
Group:          Development/Java
Source0:        attrib4j-0.9.0.zip
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit >= 0:1.6
BuildRequires: junit
BuildRequires: bcel
Requires: bcel
BuildArch:      noarch

%description
The basic goal of the project is to support the 
inclusion and extraction of custom metadata 
associated with various program elements of a 
Java class or interface. An individual element 
of metadata associated with a program element, 
for example a method, is commonly referred to as 
an attribute. These attributes are inserted at 
compile time and then can be retrieved later at 
runtime. 



%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%prep
%setup -T -c -n %{name}-%{version}
cd ..
unzip -q %{SOURCE0}
unzip -o -q %{name}-%{version}/%{name}-%{version}-src.zip
cd %{name}-%{version}
find . -name "*.jar" -exec rm {} \;
rm -rf src/main/attrib4j/cfparse

%build
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=$(build-classpath bcel)
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 -Dbuild.sysclasspath=first test release

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink


%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar

%files javadoc
%doc %{_javadocdir}

# -----------------------------------------------------------------------------

%changelog
* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.0-alt2_4jpp5
- fixed build with java 5

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.0-alt1_4jpp1.7
- converted from JPackage by jppimport script

