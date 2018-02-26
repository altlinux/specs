BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2011, JPackage Project
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

Name:           ezmorph
Version:        1.0.6
Release:        alt1_1jpp6
Epoch:          0
Summary:        EZMorph
License:        Apache Software License 2.0
Group:          Development/Java
URL:            http://ezmorph.sourceforge.net/
BuildArch:      noarch
Source0:        ezmorph-1.0.6.tgz
# cvs -d:pserver:anonymous@ezmorph.cvs.sourceforge.net:/cvsroot/ezmorph login
# cvs -z3 -d:pserver:anonymous@ezmorph.cvs.sourceforge.net:/cvsroot/ezmorph export -r REL_1_0_6 -d ezmorph-1.0.6 ezmorph
# tar czf ../SOURCES/ezmorph-1.0.6.tgz ezmorph-1.0.6/


Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml

Patch0:         ezmorph-pom.patch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  maven2 >= 0:2.0.8
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-resources

BuildRequires:  apache-commons-parent
Source44: import.info


%description
EZMorph is simple java library for transforming an Object 
to another Object.
EZMorph's key strenghts are:
* Supports transformations for primitives and Objects
* Supports transformations for multidimensional arrays
* Supports transformations with DynaBeans
* JDK 1.3.1 compatible
* Small memory footprint (~76K)
EZMorph comes with another feature: ArrayAssertions . JUnit
3.x does not have an assertEquals() method for asserting 
array equality, and JUnit 4.x has a limited one (it only 
supports Object[] not primitive arrays). With ArrayAssertions 
is possible to compare a boolean[] with a boolean[] or even a 
Boolean[], an those arrays can be multidimensional too.

EZMorph began life as the converter package on Json-lib but 
seeing that the features provided were more generic than JSON 
parsing, it became a project on its own. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
%patch0 -b .sav0

cp -p %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

%build
export CLASSPATH=
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}
export MAVEN_SETTINGS=$(pwd)/settings.xml

%{_bindir}/mvn-jpp \
        -e \
        -s ${MAVEN_SETTINGS} \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        install javadoc:javadoc

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 0644 target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap net.sf.ezmorph ezmorph %{version} JPP %{name}

(cd $RPM_BUILD_ROOT%{_javadir}
for jar in *-%{version}*.jar; do ln -sf ${jar} `echo ${jar} | sed "s|-%{version}||g"`;done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt1_1jpp6
- new version

