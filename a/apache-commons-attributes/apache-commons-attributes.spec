BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2010, JPackage Project
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with gcj_support
%bcond_with gcj_support

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define base_name attributes
%define short_name commons-attributes

Name:           apache-%{short_name}
Version:        2.2
Release:        alt2_6jpp6
Epoch:          0
Summary:        Apache Commons Attributes Package
Group:          Development/Java
License:        ASL 2.0
URL:            http://commons.apache.org/attributes
Source0:        commons-attributes-2.2-src.tar.gz
Source1:        commons-attributes-api-2.2.pom
Source2:        commons-attributes-compiler-2.2.pom
Patch0:         commons-attributes-2.2-plugin_jelly.patch
Patch1:         commons-attributes-2.2-build.patch
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires: ant
#Requires: qdox
BuildRequires: ant >= 0:1.7
BuildRequires: ant-junit
BuildRequires: junit >= 0:3.8.2
BuildRequires: jakarta-commons-beanutils
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: qdox161
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Provides:       jakarta-%{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{epoch}:%{version}-%{release}
Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name} < %{epoch}:%{version}-%{release}
Source44: import.info

%description
Commons Attributes enables Java programmers to 
use C#/.Net-style attributes in their code.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       jakarta-%{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-javadoc < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{short_name}-%{version}
%patch0 -b .sav0
%patch1 -b .sav1

%build
export OPT_JAR_LIST="`%{__cat} %{_sysconfdir}/ant.d/junit`"

export CLASSPATH=$(build-classpath qdox161)
CLASSPATH=target/classes:target/test-classes:$CLASSPATH
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist

%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}

install -pm 644 dist/%{short_name}-api-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-api-%{version}.jar
install -pm 644 dist/%{short_name}-compiler-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-compiler-%{version}.jar

ln -s %{name}-api-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-api.jar
ln -s %{name}-api-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{short_name}-api-%{version}.jar
ln -s %{short_name}-api-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{short_name}-api.jar
ln -s %{short_name}-api-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/jakarta-%{short_name}-api-%{version}.jar
ln -s %{short_name}-api-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/jakarta-%{short_name}-api.jar
ln -s %{name}-compiler-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-compiler.jar
ln -s %{name}-compiler-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{short_name}-compiler-%{version}.jar
ln -s %{short_name}-compiler-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{short_name}-compiler.jar
ln -s %{short_name}-compiler-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/jakarta-%{short_name}-compiler-%{version}.jar
ln -s %{short_name}-compiler-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/jakarta-%{short_name}-compiler.jar

%add_to_maven_depmap %{short_name} %{short_name}-api %{version} JPP %{short_name}-api
%add_to_maven_depmap %{short_name} %{short_name}-compiler %{version} JPP %{short_name}-compiler

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-api.pom
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-compiler.pom

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-*%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/*

%changelog
* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_6jpp6
- built with qdox161

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_6jpp6
- add obsoletes

