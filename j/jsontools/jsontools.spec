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

Name:           jsontools
Version:        1.5
Release:        alt1_1jpp6
Epoch:          0
Summary:        Java Tools for the JSON Format
License:        LGPL
Group:          Development/Java
URL:            http://jsontools.berlios.de/
BuildArch:      noarch
Source0:        jsontools-1.5.tgz
# svn export http://svn.berlios.de/svnroot/repos/jsontools/tags/core-1.5/ jsontools-1.5
# tar czf ../SOURCES/jsontools-1.5.tgz jsontools-1.5/

Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  maven2 >= 0:2.0.8
BuildRequires:  maven2-plugin-antlr
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-resources
BuildRequires:  apache-commons-parent

BuildRequires:  antlr

Requires:  antlr

Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Source44: import.info

%description
JSON (JavaScript Object Notation) is a file format to represent
data. It is similar to XML but has different characteristics.
It is suited to represent configuration information, implement
communication protocols and so on. XML is more suited to
represent annotated documents. JSON parsing is very fast, the
parser can be kept lean and mean. It is easy for humans to read
and write. It is based on a subset of the JavaScript Programming
Language, Standard ECMA-262 3rd Edition - December 1999. JSON is
a text format that is completely language independent but uses
conventions that are familiar to programmers of the C-family of
languages, including C, C++, C#, Java, JavaScript, Perl, Python,
and many others. These properties make JSON an ideal
data-interchange language. The format is specified on
http://www.json.org/, for the details please visit this site.
JSON is a very simple format. As a result, the parsing and
rendering is fast and easy, you can concentrate on the content
of the file in stead of the format. In XML it is often difficult
to fully understand all features (e.g. name spaces, validation,
...). As a result, XML tends to become part of the problem i.s.o.
the solution. In JSON everything is well defined, all aspects of
the representation are clear, you can concentrate on how you are
going to represent your application concepts.
Following tools are available:
1. Parser: Parse JSON text files and convert these to a Java model.
2. Renderer: Render a Java representation into text.
3. Serializer: Serialize plain POJO clusters to a JSON
   representation. The goal is to provide a serializing mechanism
   which can cope with all kinds of Java datastructures (recursion,
   references, primitive types, ...) .
4. Mapper: Map POJO to JSON, this time the JSON text should be as
   clean as possible. This tool is the best choice when data has
   to be communicated between Java and other programming languages
   who can parse JSON.
5. Validator: Validate the contents of a JSON file using a JSON
   schema.



%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 

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
install -p -m 0644 target/%{name}-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap com.sdicons.jsontools jsontools-core %{version} JPP %{name}

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
* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_1jpp6
- new version

