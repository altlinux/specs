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


Name:           el-impl
Version:        1.0
Release:        alt1_1jpp5
Epoch:          0
Summary:        Unified Expression Language Implementation

Group:          Development/Java
License:        CDDL + GPL2
URL:            https://uel.dev.java.net/
Source0:        https://maven-repository.dev.java.net/repository/el-impl/java-sources/el-impl-1.0-sources.jar
Source1:        https://maven-repository.dev.java.net/repository/el-impl/poms/el-impl-1.0.pom


BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: el_1_0_api

Requires: el_1_0_api

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
This project provides an implementation of the Expression Language (EL). 

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
%{summary}.


%prep
%setup -q -c
mkdir src
mv com src

%build
mkdir bin
export CLASSPATH=$(build-classpath \
el_1_0_api \
)
javac -d bin $(find src -name "*.java")
javadoc -d apidocs -sourcepath src com.sun.el

jar cf %{name}-%{version}.jar -C bin com

%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

install -m 644 %{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp5
- first build

