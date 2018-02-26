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


Name:           pnuts
Version:        1.2
Release:        alt2_1jpp5
Epoch:          0
Summary:        Pnuts Script Language

Group:          Development/Java
License:        Sun Public License
URL:            https://pnuts.dev.java.net/
Source0:        pnuts-1.2-src.tar.gz
# 
# svn export http://opensvn.csie.org/Pnuts/1.2/ pnuts-1.2-src
Source1:        %{name}-%{version}.pom
Patch0:         %{name}-%{version}-Pnuts.patch
Patch1:         %{name}-%{version}-servlet-build.patch


BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-nodeps
BuildRequires: javacc3
BuildRequires: servlet_2_4_api
BuildRequires: jsp_2_0_api
BuildRequires: xalan-j2


Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
Pnuts is a script language for Java environment. It enables
interaction with Java environment, simple Web scripting, 
customization for Java programs, and so on.
* Simple and clean syntax
* Interactive interpreter
* Extensible through its module system
* Customizable and embeddable through Pnuts API
* Dynamic/static translation to JVM bytecode
* One of the fastest scripting language implementations on JVM
* Inherits many advantages of Java (security, portability, etc.) 

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.


%prep
%setup -q  -n %{name}-%{version}-src
for j in $(find modules/lib -name "*.jar"); do
    mv $j $j.no
done
ln -sf $(build-classpath jsp_2_0_api) modules/lib/jsp.jar
ln -sf $(build-classpath servlet_2_4_api) modules/lib/servlet.jar
ln -sf $(build-classpath xalan-j2) modules/lib/xalan.jar

%patch0 -b .sav0
%patch1 -b .sav1

ln -s $(build-classpath javacc3) javacc.jar

%build
ant \
    -Dtop=$(pwd) \
    -Djavacc.home=`pwd` \
    all apidoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 dist/%{name}-%{version}/lib/%{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap com.sun.script pnuts-engine %{version} JPP %{name}
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -m 644 dist/%{name}-%{version}/modules/%{name}-modules.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-modules-%{version}.jar
%add_to_maven_depmap com.sun.script pnuts-modules %{version} JPP %{name}-modules
ln -sf %{name}-modules-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-modules.jar


# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr apidoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/*.jar
%doc LICENSE.txt
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


%changelog
* Sun Mar 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_1jpp5
- build with javacc3

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_1jpp5
- new version

