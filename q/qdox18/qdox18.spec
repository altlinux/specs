Patch33: qdox18-alt-no-xsite.patch
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc sun-annotation-1.0-api
BuildRequires: jpackage-compat
# Copyright (c) 2000-2009, JPackage Project
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

%define gcj_support 0

# If you don't want to build with maven, and use straight ant instead,
# give rpmbuild option '--without maven'

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}

%define oname   qdox

Summary:        Extract class/interface/method definitions from sources
Name:           qdox18
Version:        1.8
Release:        alt3_1jpp5
Epoch:          0
License:        Apache-style Software License
URL:            http://qdox.codehaus.org/
Group:          Development/Java
Source0:        qdox-1.8-src.tar.gz
# svn export http://svn.codehaus.org/qdox/tags/qdox-1.8/ 

Source1:        qdox-1.8-build.xml
Source2:        qdox-settings.xml
Source3:        qdox-1.8-jpp-depmap.xml
Patch0:         qdox-1.8-pom.patch
Patch1:         qdox-1.8-lexer_flex.patch

BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit >= 0:1.6
BuildRequires: junit >= 0:3.8.1
BuildRequires: byaccj
BuildRequires: jflex
%if %{with_maven}
BuildRequires: maven2 >= 2.0.7
BuildRequires: maven2-plugin-ant
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-dependency
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-release
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-plugin
BuildRequires: jmock >= 0:1.0
%endif
BuildRequires: excalibur-avalon-framework
BuildRequires: excalibur-avalon-logkit
BuildRequires: jakarta-slide-webdavclient
BuildRequires: qdox
#BuildRequires: xsite

Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4

%if ! %{gcj_support}
BuildArch:      noarch
%endif

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

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

%if %{with_maven}
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.
%endif

%prep
%setup -q -n %{oname}-%{version}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
rm bootstrap/yacc.linux
ln -s /usr/bin/byaccj bootstrap/yacc.linux
ln -s $(build-classpath jflex) bootstrap
ln -s $(build-classpath java-cup) bootstrap
cp %{SOURCE1} build.xml
cp %{SOURCE2} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml

%patch0 -b .sav0
%patch1 -b .sav1
%patch33 -b .sav33

%build
%if %{with_maven}
mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mvn-jpp \
        -e \
	-Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5 \
        -s settings.xml \
        -Dmaven2.jpp.depmap.file=%{SOURCE3} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        ant:ant install javadoc:javadoc

%else
mkdir -p src/java/com/thoughtworks/qdox/parser/impl
export CLASSPATH=$(build-classpath jmock jflex):target/classes:target/test-classes
java JFlex.Main \
    -d src/java/com/thoughtworks/qdox/parser/impl \
    src/grammar/lexer.flex
pushd src
byaccj \
    -Jnorun \
    -Jnoconstruct \
    -Jclass=Parser \
    -Jsemantic=Value \
    -Jpackage=com.thoughtworks.qdox.parser.impl \
    grammar/parser.y
popd
mv src/Parser.java src/java/com/thoughtworks/qdox/parser/impl
ant -Dbuild.sysclasspath=only jar test javadoc
%endif

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{oname}-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
%add_to_maven_depmap  com.thoughtworks.qdox qdox %{version} JPP %{name}


# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %{with_maven}
rm -rf target/site/apidocs
#cp -pr target/site $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%if %{with_maven}
#files manual
#doc %{_docdir}/%{name}-%{version}/site
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt3_1jpp5
- fixed build with java 7

* Wed Jan 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt2_1jpp5
- fixed build - added sun-annotation-1.0-api

* Mon Jun 15 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_1jpp5
- new version

