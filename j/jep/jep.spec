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

%define ext_version   1.1.1

Name:           jep
Version:        2.4.1
Release:        alt1_1jpp5
Epoch:          0
Summary:        Java Math Expression Parser

Group:          Development/Java
License:        GPL
URL:            http://www.singularsys.com/jep/
Source0:        http://www.singularsys.com/download/jep-2.4.1-ext-1.1.1-gpl.zip
Source1:        %{name}-%{version}.pom
Source2:        %{name}-ext-%{ext_version}.pom


BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-nodeps

BuildRequires: javacc3
BuildRequires: jama
BuildRequires: junit

Requires: jama

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
Jep is a Java library for parsing and evaluating 
mathematical expressions. With this package you can allow 
your users to enter an arbitrary formula as a string, and 
instantly evaluate it. Jep supports user defined variables,
constants, and functions. A number of common mathematical 
functions and constants are included.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
Javadoc for %{name}


%prep
%setup -q -n jep-2.4.1-ext-1.1.1-gpl
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
ln -sf $(build-classpath jama) lib/Jama-1.0.2.jar
ln -sf $(build-classpath javacc3) lib/javacc.jar
ln -sf $(build-classpath junit) lib/junit.jar


%build
export JRE1_2HOME=%{_jvmdir}/java/jre
export JAVACCHOME=$(pwd)/lib
ant jar javadoc

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 dist/jep-2.4.1.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 dist/ext-1.1.1.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-ext-%{ext_version}.jar
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
%add_to_maven_depmap %{name} ext %{ext_version} JPP %{name}-ext
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -sf %{name}-ext-%{ext_version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-ext.jar

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-ext.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/*.jar
%doc LICENSE-gpl.txt
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt1_1jpp5
- new version

