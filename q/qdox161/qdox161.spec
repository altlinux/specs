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

%define oname qdox

Name:           qdox161
Version:        1.6.1
Release:        alt2_7jpp6
Epoch:          0
Summary:        Extract class/interface/method definitions from sources
License:        ASL 2.0
URL:            http://qdox.codehaus.org/
Group:          Development/Java
# svn co https://svn.codehaus.org/qdox/tags/QDOX_1_6_1/qdox
# tar czvf qdox-1.6.1-src.tar.gz qdox
Source0:        qdox-1.6.1-src.tar.gz
Source1:        qdox-1.6.1.pom
Source2:        qdox-LocatedDef.java
Source3:        qdox-build.xml
Patch0:         qdox-1.6.1-byaccj.patch
Patch1:         qdox-1.6.1-jflex.patch
Patch2:         qdox-1.6.1-test.patch
BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: byaccj
BuildRequires: java-cup
BuildRequires: jflex
BuildRequires: jmock
Provides:  qdox = 0:%{version}-%{release}
Source44: import.info

%description
QDox is a high speed, small footprint parser 
for extracting class/interface/method definitions 
from source files complete with JavaDoc @tags. 
It is designed to be used by active code 
generators or documentation tools. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{oname}
chmod -Rf a+rX,u+w,g-w,o-w bootstrap
rm -r bootstrap
%patch0 -p1
%patch1 -p1
%patch2 -p1
cp -p %{SOURCE2} src/java/com/thoughtworks/qdox/parser/structs/LocatedDef.java 
sed -e "s/@VERSION@/%{version}/g" %{SOURCE3} > build.xml

%build
export OPT_JAR_LIST="junit ant/ant-junit"
mkdir -p target/src/java/com/thoughtworks/qdox/parser/impl
export CLASSPATH=`pwd`/target/classes:`pwd`/target/test-classes:$(build-classpath java-cup jflex jmock junit)
%{java} JFlex.Main \
    -d src/java/com/thoughtworks/qdox/parser/impl \
    src/grammar/lexer.flex
pushd target
%{_bindir}/byaccj \
    -Jnorun \
    -Jnoconstruct \
    -Jclass=Parser \
    -Jsemantic=Value \
    -Jpackage=com.thoughtworks.qdox.parser.impl \
    ../src/grammar/parser.y
popd
mv target/Parser.java src/java/com/thoughtworks/qdox/parser/impl
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.sysclasspath=only jar javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{oname}-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-qdox161.pom
%add_to_maven_depmap %{oname} %{oname} %{version} JPP %{name}

%files
%doc LICENSE.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Mon Jan 31 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_7jpp6
- set target 5

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_7jpp6
- new version

