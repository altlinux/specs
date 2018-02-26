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

%define namedversion 1.6.9
%define bname groovy

Name:           groovy16
Summary:        Groovy scripting language
Url:            http://groovy.codehaus.org/
Version:        1.6.9
Release:        alt2_3jpp6
Epoch:          0
License:        Apache Software License 2.0
Group:          Development/Java
Source0:        groovy-1.6.9.tar.gz
# svn export http://svn.codehaus.org/groovy/tags/GROOVY_1_6_9/ groovy-1.6.9
Source1:        http://repository.codehaus.org/org/codehaus/groovy/groovy-all/1.6.9/groovy-all-1.6.9.pom
Patch0:         groovy16-build.patch

BuildRequires: jpackage-utils >= 0:1.7.5

BuildRequires: ant17 >= 0:1.7.1
BuildRequires: ant17-antlr
BuildRequires: ant17-junit
BuildRequires: ant17-trax
BuildRequires: antlr
BuildRequires: aqute-bndlib
BuildRequires: cewolf
BuildRequires: checkstyle4
BuildRequires: cobertura
#BuildRequires:  eclipse-rcp
BuildRequires: jcommon
BuildRequires: jfreechart
BuildRequires: junit
BuildRequires: lucene1
BuildRequires: maven-ant-tasks
BuildRequires: openejb1
BuildRequires: xmlunit

BuildRequires: asm2 >= 0:2.2
BuildRequires: bsf
BuildRequires: cglib21 >= 0:2.1.3
BuildRequires: hsqldb
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-cli
BuildRequires: apache-commons-codec
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-httpclient
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: apache-ivy
BuildRequires: jakarta-oro
BuildRequires: jarjar
BuildRequires: jline
BuildRequires: jmock
BuildRequires: jsp_2_0_api
BuildRequires: lucene
BuildRequires: livetribe-jsr223
BuildRequires: mx4j
BuildRequires: openejb1
BuildRequires: qdox161
BuildRequires: servlet_2_4_api
BuildRequires: xpp3-minimal
BuildRequires: xstream

#
Requires: ant
Requires: ant-junit
Requires: ant-trax
Requires: antlr
Requires: asm2
Requires: bsf
Requires: jakarta-commons-cli
Requires: jakarta-commons-logging
Requires: jarjar
Requires: jline
Requires: jsp_2_0_api
Requires: junit
Requires: livetribe-jsr223
Requires: mx4j
Requires: servlet_2_4_api
Requires: xpp3-minimal
Requires: xstream

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
BuildArch:      noarch
Source44: import.info


%description
Groovy is a new agile dynamic language for the JVM 
combining lots of great features from languages like 
Python, Ruby and Smalltalk and making them available 
to the Java developers using a Java-like syntax.
Groovy is designed to help you get things done on the 
Java platform in a quicker, more concise and fun way - 
bringing the power of Python and Ruby inside the Java 
platform. 
Groovy can be used as an alternative compiler to javac 
to generate standard Java bytecode to be used by any 
Java project or it can be used dynamically as an 
alternative language such as for scripting Java objects, 
templating or writing unit test cases.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n groovy-%{version}
chmod -R go=u-w *
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
pushd bootstrap
ln -s $(build-classpath maven-ant-tasks)
popd
pushd cruise/reporting-app/WEB-INF/lib/
ln -s $(build-classpath xmlgraphics-batik/awt-util) batik-awt-util.jar
ln -s $(build-classpath xmlgraphics-batik/svggen) batik-svggen.jar
ln -s $(build-classpath xmlgraphics-batik/util) batik-util.jar
ln -s $(build-classpath cewolf) 
ln -s $(build-classpath commons-logging) 
ln -s $(build-classpath jcommon) 
ln -s $(build-classpath jfreechart) 
popd
mv security/GroovyJarTest.jar.no security/GroovyJarTest.jar

%patch0 -b .sav0

mkdir -p target/lib/compile
pushd target/lib/compile
ln -sf $(build-classpath ant17)
ln -sf $(build-classpath antlr)
ln -sf $(build-classpath asm2/asm2)
ln -sf $(build-classpath asm2/asm2-analysis)
ln -sf $(build-classpath asm2/asm2-tree)
ln -sf $(build-classpath asm2/asm2-util)
ln -sf $(build-classpath bsf)
ln -sf $(build-classpath commons-cli)
ln -sf $(build-classpath apache-ivy)
ln -sf $(build-classpath jline)
ln -sf $(build-classpath jsp_2_0_api)
ln -sf $(build-classpath junit)
ln -sf $(build-classpath livetribe-jsr223)
ln -sf $(build-classpath servlet_2_4_api)
ln -sf $(build-classpath xstream)
popd
mkdir -p target/lib/examples
pushd target/lib/examples
ln -sf $(build-classpath commons-httpclient)
ln -sf $(build-classpath lucene1)
ln -sf $(build-classpath openejb1/loader)
#ln -sf $(ls /usr/lib/eclipse/plugins/org.eclipse.osgi_3*.jar)
popd
mkdir -p target/lib/extras
pushd target/lib/extras
ln -sf $(build-classpath mx4j/mx4j)
popd
mkdir -p target/lib/runtime
pushd target/lib/runtime
ln -sf $(build-classpath ant17)
ln -sf $(build-classpath ant17-launcher)
ln -sf $(build-classpath ant17/ant17-junit)
ln -sf $(build-classpath antlr)
ln -sf $(build-classpath asm2/asm2)
ln -sf $(build-classpath asm2/asm2-analysis)
ln -sf $(build-classpath asm2/asm2-tree)
ln -sf $(build-classpath asm2/asm2-util)
ln -sf $(build-classpath bsf)
ln -sf $(build-classpath commons-cli)
ln -sf $(build-classpath commons-logging)
ln -sf $(build-classpath apache-ivy)
ln -sf $(build-classpath jline)
ln -sf $(build-classpath jsp_2_0_api)
ln -sf $(build-classpath junit)
ln -sf $(build-classpath servlet_2_4_api)
ln -sf $(build-classpath xstream)
popd
mkdir -p target/lib/test
pushd target/lib/test
ln -sf $(build-classpath ant17)
ln -sf $(build-classpath ant17/ant17-junit)
ln -sf $(build-classpath ant17-launcher)
ln -sf $(build-classpath antlr)
ln -sf $(build-classpath asm2/asm2)
ln -sf $(build-classpath asm2/asm2-analysis)
ln -sf $(build-classpath asm2/asm2-attrs)
ln -sf $(build-classpath asm2/asm2-tree)
ln -sf $(build-classpath asm2/asm2-util)
ln -sf $(build-classpath bsf)
ln -sf $(build-classpath cglib21-nodep)
ln -sf $(build-classpath commons-cli)
ln -sf $(build-classpath commons-logging)
ln -sf $(build-classpath hsqldb)
ln -sf $(build-classpath apache-ivy)
ln -sf $(build-classpath jline)
ln -sf $(build-classpath jmock)
ln -sf $(build-classpath jmock-cglib)
ln -sf $(build-classpath jsp_2_0_api)
ln -sf $(build-classpath junit)
ln -sf $(build-classpath livetribe-jsr223)
ln -sf $(build-classpath servlet_2_4_api)
ln -sf $(build-classpath xmlunit)
ln -sf $(build-classpath xstream)
popd
mkdir -p target/lib/tools
pushd target/lib/tools
ln -sf $(build-classpath antlr)
ln -sf $(build-classpath asm2/asm2)
ln -sf $(build-classpath asm2/asm2-tree)
ln -sf $(build-classpath aqute-bndlib)
#ln -sf $(build-classpath backport-util-concurrent)
ln -sf $(build-classpath checkstyle4)
ln -sf $(build-classpath cobertura)
ln -sf $(build-classpath commons-beanutils)
ln -sf $(build-classpath commons-cli)
ln -sf $(build-classpath commons-collections)
ln -sf $(build-classpath commons-lang)
ln -sf $(build-classpath commons-logging)
ln -sf $(build-classpath jarjar)
ln -sf $(build-classpath log4j)
ln -sf $(build-classpath oro)
ln -sf $(build-classpath qdox161)
popd


%build
export OPT_JAR_LIST="maven-ant-tasks ant17/ant17-trax ant17/ant17-antlr ant17/ant17-junit junit"
export ANT_OPTS="-DskipFetch=true -DforceRetro=false -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5"
ant17 install javadoc 

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 target/dist/%{bname}-%{namedversion}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 target/dist/%{bname}-all-%{namedversion}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-all-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms and depmap frags
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.codehaus.groovy groovy %{namedversion} JPP %{name}
%add_to_maven_depmap org.codehaus.groovy groovy16 %{namedversion} JPP %{name}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-all.pom
%add_to_maven_depmap org.codehaus.groovy groovy-all %{namedversion} JPP %{name}-all
%add_to_maven_depmap org.codehaus.groovy groovy16-all %{namedversion} JPP %{name}-all

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/html/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# bin
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 target/install/bin/groovy $RPM_BUILD_ROOT%{_bindir}/groovy16
install -m 755 target/install/bin/groovyc $RPM_BUILD_ROOT%{_bindir}/groovyc16
install -m 755 target/install/bin/groovyConsole $RPM_BUILD_ROOT%{_bindir}/groovyConsole16
install -m 755 target/install/bin/groovysh $RPM_BUILD_ROOT%{_bindir}/groovysh16
install -m 755 target/install/bin/java2groovy $RPM_BUILD_ROOT%{_bindir}/java2groovy16
install -m 755 target/install/bin/startGroovy $RPM_BUILD_ROOT%{_bindir}/startGroovy16

# conf
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/conf
install -m 644 target/install/conf/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/conf

# lib
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/embeddable
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/embeddable
ln -sf %{_javadir}/groovy16-all.jar
popd

# lib
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/lib
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/lib
build-jar-repository -s -p . \
ant \
ant/ant-junit \
ant-launcher \
antlr \
asm2/asm2-analysis \
asm2/asm2 \
asm2/asm2-tree \
asm2/asm2-util \
bsf \
commons-cli \
commons-logging \
jline \
jsp_2_0_api \
junit \
apache-ivy \
mx4j/mx4j \
servlet_2_4_api \
xpp3 \
xstream \

ln -sf %{_javadir}/groovy16.jar
popd

# bugfix: Package groovy16 has broken dep on /usr/bin/startGroovy
sed -i -e 's,startGroovy,startGroovy16,g' %buildroot%_bindir/*


%files
%doc LICENSE.txt
%{_javadir}/*
%attr(755, root, root) %{_bindir}/*
%{_datadir}/%{name}-%{version}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}*

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.9-alt2_3jpp6
- fixed parasyte dep on groovy10

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.9-alt1_3jpp6
- new version

