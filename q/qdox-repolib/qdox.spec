%define oldname qdox
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_with maven

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'

%define _with_repolib 1

%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/qdox/1.6.1-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define gcj_support 0


Name:           qdox-repolib
Version:        1.6.1
Release:        alt4_5jpp6
Epoch:          1
Summary:        Extract class/interface/method definitions from sources
License:        ASL 2.0
URL:            http://qdox.codehaus.org/
Group:          Development/Java
# svn co https://svn.codehaus.org/qdox/tags/QDOX_1_6_1/qdox
# tar czvf qdox-1.6.1-src.tar.gz qdox
Source0:        qdox-1.6.1-src.tar.gz
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        qdox-1.6-jpp-depmap.xml
Source5:        qdox-LocatedDef.java
Source6:        qdox-build.xml
Source7:        qdox-component-info.xml
Patch0:         qdox-1.6.1-byaccj.patch
Patch1:         qdox-1.6.1-jflex.patch
Patch2:         qdox-1.6.1-test.patch
BuildRequires: jpackage-utils >= 0:1.6
%if %with maven
BuildRequires: maven >= 0:1.1
BuildRequires: maven-plugins-base
BuildRequires: maven-plugin-license
BuildRequires: maven-plugin-test
BuildRequires: maven-plugin-xdoc
BuildRequires: saxon
BuildRequires: saxon-scripts
BuildRequires: jmock >= 0:1.0
BuildRequires: mockobjects >= 0:0.09
%endif
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit >= 0:1.6
BuildRequires: junit >= 0:3.8.1
BuildRequires: byaccj
BuildRequires: java-cup
BuildRequires: jflex
BuildRequires: jmock
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%endif
Source44: import.info

%description
QDox is a high speed, small footprint parser 
for extracting class/interface/method definitions 
from source files complete with JavaDoc @tags. 
It is designed to be used by active code 
generators or documentation tools. 

%if %{with_repolib}
%package repolib
Summary:         Artifacts to be uploaded to a repository library
Group:           Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{oldname}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{oldname}
chmod -Rf a+rX,u+w,g-w,o-w bootstrap
rm -r bootstrap
%patch0 -p1
%patch1 -p1
%patch2 -p1
cp -p %{SOURCE5} src/java/com/thoughtworks/qdox/parser/structs/LocatedDef.java 
sed -e "s/@VERSION@/%{version}/g" %{SOURCE6} > build.xml

%if %{with_repolib}
tag=`echo %{oldname}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{SOURCE7}
%endif

%build
%if %with maven
export DEPCAT=$(pwd)/qdox-1.6-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    %{_bindir}/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
%{_bindir}/saxon $DEPCAT %{SOURCE2} > qdox-1.6-depmap.new.xml
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    %{_bindir}/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

export MAVEN_HOME_LOCAL=$(pwd)/.maven
export CLASSPATH=$(build-classpath junit)
maven \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.home.local=$MAVEN_HOME_LOCAL \
        -Dqdox.byaccj.executable=byaccj \
        jar javadoc
%else
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
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
%endif

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{oldname}-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{oldname}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}
ln -s %{oldname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %{with_repolib}
        install -d -m 755 $RPM_BUILD_ROOT%{repodir}
        install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
        install -p -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{repodir}/component-info.xml
        install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
        install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
        cp -p $RPM_BUILD_ROOT%{_javadir}/qdox.jar $RPM_BUILD_ROOT%{repodirlib}
%endif

%if %{with_repolib}
%files
%{repodir}
%endif

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt4_5jpp6
- fixed build with moved maven1

* Thu Feb 09 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt3_5jpp6
- compat build

* Tue Oct 26 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt2_5jpp6
- rebuild with target=5

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt1_5jpp6
- new version

* Fri Feb 13 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt1_5jpp5
- reverted to version 1.6.1

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt1_1jpp5
- fixed build with jpackage 5

* Sun Jul 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt1_1jpp1.7
- rebuilt with maven1

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_4jpp1.7
- converted from JPackage by jppimport script

