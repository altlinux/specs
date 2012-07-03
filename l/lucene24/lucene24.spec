# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 2.4.1
%define name lucene24
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

#def_with db
%bcond_with             db
%bcond_without          repolib

%define repodir %{_javadir}/repository.jboss.com/apache-lucene/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define gcj_support 0

%define oname    lucene

Name:           lucene24
Version:        2.4.1
Release:        alt4_6jpp6
Epoch:          0
Summary:        High-performance, full-featured text search engine
License:        ASL 2.0
Group:          Development/Java
URL:            http://lucene.apache.org/
Source0:        http://www.apache.org/dist/lucene/java/lucene-2.4.1-src.tar.gz
Source1:        http://repo1.maven.org/maven2/org/apache/lucene/lucene-analyzers/2.4.1/lucene-analyzers-2.4.1.pom
Source2:        http://repo1.maven.org/maven2/org/apache/lucene/lucene-ant/2.4.1/lucene-ant-2.4.1.pom
Source3:        http://repo1.maven.org/maven2/org/apache/lucene/lucene-bdb/2.4.1/lucene-bdb-2.4.1.pom
Source4:        http://repo1.maven.org/maven2/org/apache/lucene/lucene-bdb-je/2.4.1/lucene-bdb-je-2.4.1.pom
Source5:        http://repo1.maven.org/maven2/org/apache/lucene/lucene-benchmark/2.4.1/lucene-benchmark-2.4.1.pom
Source6:        http://repo1.maven.org/maven2/org/apache/lucene/lucene-contrib/2.4.1/lucene-contrib-2.4.1.pom
Source7:        http://repo1.maven.org/maven2/org/apache/lucene/lucene-core/2.4.1/lucene-core-2.4.1.pom
Source8:        http://repo1.maven.org/maven2/org/apache/lucene/lucene-demos/2.4.1/lucene-demos-2.4.1.pom
Source9:        http://repo1.maven.org/maven2/org/apache/lucene/lucene-highlighter/2.4.1/lucene-highlighter-2.4.1.pom
Source10:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-lucli/2.4.1/lucene-lucli-2.4.1.pom
Source11:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-memory/2.4.1/lucene-memory-2.4.1.pom
Source12:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-misc/2.4.1/lucene-misc-2.4.1.pom
Source13:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-parent/2.4.1/lucene-parent-2.4.1.pom
Source14:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-queries/2.4.1/lucene-queries-2.4.1.pom
Source15:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-regex/2.4.1/lucene-regex-2.4.1.pom
Source16:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-snowball/2.4.1/lucene-snowball-2.4.1.pom
Source17:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-spellchecker/2.4.1/lucene-spellchecker-2.4.1.pom
Source18:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-surround/2.4.1/lucene-surround-2.4.1.pom
Source19:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-swing/2.4.1/lucene-swing-2.4.1.pom
# Source20:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-wikipedia/2.3.2/lucene-wikipedia-2.3.2.pom
Source21:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-wordnet/2.4.1/lucene-wordnet-2.4.1.pom
Source22:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-xml-query-parser/2.4.1/lucene-xml-query-parser-2.4.1.pom
Patch0:         lucene-no-classpath-in-manifest.patch
Patch1:         lucene-no-get.patch
Patch4:         lucene-2.4.1-db-javadoc.patch
Source100:      lucene-1.9-OSGi-MANIFEST.MF
Source200:      lucene-1.9-analysis-OSGi-MANIFEST.MF
# Modifed from <http://repository.jboss.com/apache-lucene/2.2.0/component-info.xml>
Source300:      lucene-component-info.xml
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-junit
%if %with db
BuildRequires:  berkeleydb >= 0:2.0.90
# FIXME: (dwalluck): db support requires berkeleydb-native (berkeleydb-native.jar) in JPP17, db4-java (db.jar) in Fedora, db4.7 (db4.7.jar) in Mandriva
# BuildRequires:  berkeleydb-native
BuildRequires:  db4-java
%endif
BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-digester
BuildRequires:  apache-commons-logging
BuildRequires:  java-javadoc
BuildRequires:  javacc
BuildRequires:  jline
BuildRequires:  jtidy
BuildRequires:  log4j
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  junit
BuildRequires:  regexp
BuildRequires:  zip
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
Jakarta Lucene is a high-performance, full-featured text search engine
written entirely in Java. It is a technology suitable for nearly any
application that requires full-text search, especially cross-platform.

%package javadoc
Summary:        Javadoc for Lucene
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package demo
Summary:        Lucene demonstration library
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description demo
%{summary}.

%package contrib
Summary:        Lucene contributed extensions
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jline

%description contrib
%{summary}.

%package contrib-benchmark
Summary:        Lucene contributed benchmark
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       apache-commons-beanutils
Requires:       apache-commons-collections
Requires:       apache-commons-digester
Requires:       apache-commons-logging
#Requires:       xerces-j2
#Requires:       xml-commons-jaxp-1.3-apis

%description contrib-benchmark
%{summary}.

%if %with db
%package contrib-db
Summary:        Lucene contributed bdb extensions
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       berkeleydb >= 0:2.0.90
# Requires:       berkeleydb-native
Requires:       db4-java

%description contrib-db
%{summary}.
%endif

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p0
%patch1 -p0
%patch4 -p1
find . -name "*.jar" | xargs -t rm

%if %without db
rm -r contrib/db
%endif

%build
# berkeleydb-native or db
export CLASSPATH=$(build-classpath \
%if %with db
berkeleydb \
db \
%endif
commons-digester jline jtidy junit regexp)

export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Djavacc.home=%{_bindir}/javacc \
  -Djavacc.jar=%{_javadir}/javacc.jar \
  -Djavacc.jar.dir=%{_javadir} \
  -Djavadoc.link=%{_javadocdir}/java \
  -Dversion=%{version} \
package-all-binary

mkdir -p META-INF
cp %{SOURCE100} META-INF/MANIFEST.MF

#zip -qqu build/lucene-core-%{version}.jar META-INF/MANIFEST.MF
jar umf META-INF/MANIFEST.MF build/lucene-core-%{version}.jar

rm -f META-INF/MANIFEST.MF
cp %{SOURCE200} META-INF/MANIFEST.MF
#zip -qqu build/contrib/analyzers/lucene-analyzers-%{version}.jar META-INF/MANIFEST.MF
jar umf META-INF/MANIFEST.MF build/contrib/analyzers/lucene-analyzers-%{version}.jar 

%install

# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -p -m 0644 build/%{oname}-core-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
install -p -m 0644 build/%{oname}-demos-%{version}.jar %{buildroot}%{_javadir}/%{name}-demos-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# contrib jars
install -d -m 0755 %{buildroot}%{_javadir}/%{name}-contrib

for c in analyzers ant benchmark highlighter lucli memory misc queries regex similarity snowball spellchecker surround swing wikipedia wordnet xml-query-parser; do
    install -p -m 0644 build/contrib/$c/%{oname}-${c}-%{version}.jar \
                %{buildroot}%{_javadir}/%{name}-contrib/${c}-%{version}.jar
done

(cd %{buildroot}%{_javadir}/%{name}-contrib && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# benchmark contrib jars
install -d -m 0755 %{buildroot}%{_javadir}/%{name}-contrib-benchmark
install -p -m 0644 build/contrib/benchmark/%{oname}-benchmark-%{version}.jar \
                %{buildroot}%{_javadir}/%{name}-contrib-benchmark/benchmark-%{version}.jar
(cd %{buildroot}%{_javadir}/%{name}-contrib-benchmark && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%if %with db
# bdb contrib jars
install -d -m 0755 %{buildroot}%{_javadir}/%{name}-contrib-db
install -p -m 0644 build/contrib/db/bdb/%{oname}-bdb-%{version}.jar \
                %{buildroot}%{_javadir}/%{name}-contrib-db/bdb-%{version}.jar
install -p -m 0644 build/contrib/db/bdb-je/%{oname}-bdb-je-%{version}.jar \
                %{buildroot}%{_javadir}/%{name}-contrib-db/bdb-je-%{version}.jar
(cd %{buildroot}%{_javadir}/%{name}-contrib-db && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
%endif

# poms
install -d -m 0755 %{buildroot}%{_datadir}/maven2/poms
install -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-contrib-analyzers.pom
%add_to_maven_depmap org.apache.lucene lucene-analyzers %{version} JPP/%{name}-contrib analyzers
install -p -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-contrib-ant.pom
%add_to_maven_depmap org.apache.lucene lucene-ant %{version} JPP/%{name}-contrib ant
%if %with db
install -p -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-contrib-db-bdb.pom
%add_to_maven_depmap org.apache.lucene lucene-bdb %{version} JPP/%{name}-contrib-db bdb
install -p -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-contrib-db-bdb-je.pom
%add_to_maven_depmap org.apache.lucene lucene-bdb-je %{version} JPP/%{name}-contrib-db bdb-je
%endif
install -p -m 0644 %{SOURCE5} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-contrib-benchmark-benchmark.pom
%add_to_maven_depmap org.apache.lucene lucene-benchmark %{version} JPP/%{name}-contrib-benchmark benchmark
install -p -m 0644 %{SOURCE6} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-contrib.pom
%add_to_maven_depmap org.apache.lucene lucene-contrib %{version} JPP/%{name} contrib
install -p -m 0644 %{SOURCE7} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache.lucene lucene-core %{version} JPP %{name}
install -p -m 0644 %{SOURCE8} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-demos.pom
%add_to_maven_depmap org.apache.lucene lucene-demos %{version} JPP %{name}-demos
install -p -m 0644 %{SOURCE9} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-contrib-highlighter.pom
%add_to_maven_depmap org.apache.lucene lucene-highlighter %{version} JPP/%{name}-contrib highlighter
install -p -m 0644 %{SOURCE10} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-contrib-lucli.pom
%add_to_maven_depmap org.apache.lucene lucene-lucli %{version} JPP/%{name}-contrib lucli
install -p -m 0644 %{SOURCE11} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-contrib-memory.pom
%add_to_maven_depmap org.apache.lucene lucene-memory %{version} JPP/%{name}-contrib memory
install -p -m 0644 %{SOURCE12} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-contrib-misc.pom
%add_to_maven_depmap org.apache.lucene lucene-misc %{version} JPP/%{name}-contrib misc
install -p -m 0644 %{SOURCE13} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-parent.pom
%add_to_maven_depmap org.apache.lucene lucene-parent %{version} JPP/%{name} parent
install -p -m 0644 %{SOURCE14} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-contrib-queries.pom
%add_to_maven_depmap org.apache.lucene lucene-queries %{version} JPP/%{name}-contrib queries
install -p -m 0644 %{SOURCE15} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-contrib-regexp.pom
%add_to_maven_depmap org.apache.lucene lucene-regexp %{version} JPP/%{name}-contrib regexp
install -p -m 0644 %{SOURCE16} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-contrib-snowball.pom
%add_to_maven_depmap org.apache.lucene lucene-snowball %{version} JPP/%{name}-contrib snowball
install -p -m 0644 %{SOURCE17} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-contrib-spellchecker.pom
%add_to_maven_depmap org.apache.lucene lucene-spellchecker %{version} JPP/%{name}-contrib spellchecker
install -p -m 0644 %{SOURCE18} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-contrib-surround.pom
%add_to_maven_depmap org.apache.lucene lucene-surround %{version} JPP/%{name}-contrib surround
install -p -m 0644 %{SOURCE19} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-contrib-swing.pom
%add_to_maven_depmap org.apache.lucene lucene-swing %{version} JPP/%{name}-contrib swing
install -p -m 0644 %{SOURCE21} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-contrib-wordnet.pom
%add_to_maven_depmap org.apache.lucene lucene-wordnet %{version} JPP/%{name}-contrib wordnet
install -p -m 0644 %{SOURCE22} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-contrib-xml-query-parser.pom
%add_to_maven_depmap org.apache.lucene lucene-xml-query-parser %{version} JPP/%{name}-contrib xml-query-parser

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/docs/api/* \
  %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# webapp
install -d -m 0755 %{buildroot}%{_datadir}/%{name}-%{version}
install -p -m 0644 build/%{oname}web.war \
  %{buildroot}%{_datadir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %with repolib
mkdir -p %{buildroot}%{repodir}
mkdir -p %{buildroot}%{repodirlib}
cp -p %{SOURCE300} %{buildroot}%{repodir}/component-info.xml
sed -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
mkdir -p %{buildroot}%{repodirsrc}
cp -p %{SOURCE0} %{buildroot}%{repodirsrc}
cp -p %{SOURCE100} %{buildroot}%{repodirsrc}
cp -p %{SOURCE200} %{buildroot}%{repodirsrc}
cp -p %{PATCH0} %{buildroot}%{repodirsrc}
cp -p %{PATCH1} %{buildroot}%{repodirsrc}
cp -p %{PATCH4} %{buildroot}%{repodirsrc}
cp -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/lucene.jar
%endif

%post
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db || :
fi
%endif

%postun
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db || :
fi
%endif

%files
%doc CHANGES.txt LICENSE.txt README.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/%{name}-%{version}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files contrib
%dir %{_javadir}/%{name}-contrib
%{_javadir}/%{name}-contrib/analyzers-%{version}.jar
%{_javadir}/%{name}-contrib/analyzers.jar
%{_javadir}/%{name}-contrib/ant-%{version}.jar
%{_javadir}/%{name}-contrib/ant.jar
%{_javadir}/%{name}-contrib/benchmark-%{version}.jar
%{_javadir}/%{name}-contrib/benchmark.jar
%{_javadir}/%{name}-contrib/highlighter-%{version}.jar
%{_javadir}/%{name}-contrib/highlighter.jar
%{_javadir}/%{name}-contrib/lucli-%{version}.jar
%{_javadir}/%{name}-contrib/lucli.jar
%{_javadir}/%{name}-contrib/memory-%{version}.jar
%{_javadir}/%{name}-contrib/memory.jar
%{_javadir}/%{name}-contrib/misc-%{version}.jar
%{_javadir}/%{name}-contrib/misc.jar
%{_javadir}/%{name}-contrib/queries-%{version}.jar
%{_javadir}/%{name}-contrib/queries.jar
%{_javadir}/%{name}-contrib/regex-%{version}.jar
%{_javadir}/%{name}-contrib/regex.jar
%{_javadir}/%{name}-contrib/similarity-%{version}.jar
%{_javadir}/%{name}-contrib/similarity.jar
%{_javadir}/%{name}-contrib/snowball-%{version}.jar
%{_javadir}/%{name}-contrib/snowball.jar
%{_javadir}/%{name}-contrib/spellchecker-%{version}.jar
%{_javadir}/%{name}-contrib/spellchecker.jar
%{_javadir}/%{name}-contrib/surround-%{version}.jar
%{_javadir}/%{name}-contrib/surround.jar
%{_javadir}/%{name}-contrib/swing-%{version}.jar
%{_javadir}/%{name}-contrib/swing.jar
%{_javadir}/%{name}-contrib/wikipedia-%{version}.jar
%{_javadir}/%{name}-contrib/wikipedia.jar
%{_javadir}/%{name}-contrib/wordnet-%{version}.jar
%{_javadir}/%{name}-contrib/wordnet.jar
%{_javadir}/%{name}-contrib/xml-query-parser-%{version}.jar
%{_javadir}/%{name}-contrib/xml-query-parser.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/analyzers-%{version}.jar.*
%{_libdir}/gcj/%{name}/ant-%{version}.jar.*
%{_libdir}/gcj/%{name}/benchmark-%{version}.jar.*
%{_libdir}/gcj/%{name}/highlighter-%{version}.jar.*
%{_libdir}/gcj/%{name}/luceneweb.war.*
%{_libdir}/gcj/%{name}/lucli-%{version}.jar.*
%{_libdir}/gcj/%{name}/memory-%{version}.jar.*
%{_libdir}/gcj/%{name}/misc-%{version}.jar.*
%{_libdir}/gcj/%{name}/queries-%{version}.jar.*
%{_libdir}/gcj/%{name}/regex-%{version}.jar.*
%{_libdir}/gcj/%{name}/snowball-%{version}.jar.*
%{_libdir}/gcj/%{name}/spellchecker-%{version}.jar.*
%{_libdir}/gcj/%{name}/surround-%{version}.jar.*
%{_libdir}/gcj/%{name}/swing-%{version}.jar.*
%{_libdir}/gcj/%{name}/wikipedia-%{version}.jar.*
%{_libdir}/gcj/%{name}/wordnet-%{version}.jar.*
%{_libdir}/gcj/%{name}/xml-query-parser-%{version}.jar.*
%endif

%files contrib-benchmark
%{_javadir}/%{name}-contrib-benchmark

%if %with db
%files contrib-db
%{_javadir}/%{name}-contrib-db
%{_libdir}/gcj/%{name}/bdb-%{version}.jar.*
%{_libdir}/gcj/%{name}/bdb-je-%{version}.jar.*
%endif

%files demo
%{_javadir}/%{name}-demos-%{version}.jar
%{_javadir}/%{name}-demos.jar

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt4_6jpp6
- new jpp relase

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt4_5jpp6
- compat build

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt3_5jpp6
- rebuild without osgi provides

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt2_5jpp6
- added pom

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt2_1jpp5
- added provides for lucene2-demo

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt1_1jpp5
- new version

* Tue Mar 17 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt2_jvm5
- added maven poms, added Provides: lucene23

* Thu Jan 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_jvm5
- Sisyphus upload; thanks to Alexey Morozov.

* Fri Jan 23 2009 Alexey Morozov <morozov@altlinux.org> 0:2.4.0-alt0.1
- updated to 2.4.0

* Fri Dec 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_3.4jpp5
- updated to 2.3.1; added provides lucene22

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt5jvm4.2
- renamed to lucene2 to avoid conflicts with lucene1

* Tue Nov 20 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt4jvm4.2
- enabled check, disabled devel, added contrib

* Mon Nov 05 2007 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt3jvm4.2
- NMU: added -devel subpackage

* Tue Jul 17 2007 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt2
- NMU: partial jpackage compatibility added
- enabled demo (required for eclipse).
- demo is packaged according to jpackage.
- added source=1.4 and target=1.4

* Fri Mar 16 2007 Eugene Ostapets <eostapets@altlinux.ru> 2.1.0-alt1
- Update to 2.1.0 release

* Thu Nov 30 2006 Eugene Ostapets <eostapets@altlinux.ru> 2.0.0-alt1
- Update to 2.0.0 release

* Fri Mar 03 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.9.1-alt1
- Updated to 1.9.1
- Disabled tests (fail to build for some bogus reason)
- Disabled demo by default

* Wed Dec 08 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.3-alt1
- Updated to 1.4.3
- Spec cleanup for rpm-build-java

* Tue Jun 08 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.3-alt1
- New upstream release
- Disable debug for non-debug builds

* Tue Sep 09 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.2-alt1
- Released for ALT Linux
