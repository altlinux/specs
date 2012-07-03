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

%define oname groovy

Name:           groovy10
Summary:        Groovy scripting language
Url:            http://groovy.codehaus.org/
Version:        1.0
Release:        alt4_4jpp6
Epoch:          0
License:        BSD/Apache-style Software License
Group:          Development/Java
Source0:        groovy-1.0.tar.gz
# svn export http://svn.codehaus.org/groovy/tags/GROOVY_1_0/ groovy-1.0

Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        groovy-1.0-jpp-depmap.xml
Source5:        groovy.policy
Source6:        http://repo1.maven.org/maven2/groovy/groovy/1.0/groovy-1.0.pom
Patch0:         groovy-1.0-maven_xml.patch
Patch1:         groovy-1.0-tck-build_xml.patch
Patch2:         groovy-1.0-project_xml.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
BuildRequires: ant-junit
BuildRequires: antlr
BuildRequires: junit
BuildRequires: maven1 >= 0:1.1
BuildRequires: maven1-plugins-base
BuildRequires: maven1-plugin-antlr
BuildRequires: maven1-plugin-license
BuildRequires: maven1-plugin-test
BuildRequires: maven1-plugin-xdoc
BuildRequires: saxon
BuildRequires: saxon-scripts

BuildRequires: asm2 >= 0:2.2
BuildRequires: axion
BuildRequires: bsf
BuildRequires: cglib21
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-cli
BuildRequires: apache-commons-codec
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-httpclient
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-primitives
BuildRequires: jakarta-oro
BuildRequires: jarjar
BuildRequires: jmock
BuildRequires: junit
BuildRequires: mockobjects
BuildRequires: nekohtml
BuildRequires: openejb1
BuildRequires: qdox
BuildRequires: radeox
BuildRequires: regexp
BuildRequires: jsp_2_0_api
BuildRequires: servlet_2_4_api
BuildRequires: velocity
BuildRequires: xpp3
BuildRequires: xstream

#
Requires: ant >= 0:1.7.1
Requires: ant-junit
Requires: antlr
Requires: asm2
Requires: axion
Requires: bsf
Requires: cglib21
Requires: jakarta-commons-cli
Requires: apache-commons-codec
Requires: jakarta-commons-collections
Requires: jakarta-commons-httpclient
Requires: jakarta-commons-logging
Requires: jakarta-commons-primitives
Requires: jakarta-oro
Requires: jarjar
Requires: jmock
Requires: junit
Requires: mockobjects
Requires: nekohtml
Requires: openejb1
Requires: qdox
Requires: radeox
Requires: regexp
Requires: jsp_2_0_api
Requires: servlet_2_4_api
Requires: xpp3
Requires: xstream

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
BuildArch:      noarch
Provides:       groovy = %{epoch}:%{version}-%{release}
Obsoletes:      groovy < %{epoch}:%{version}-%{release}
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
%setup -q -n groovy-1.0
chmod -R go=u-w *
find . -name "*.jar" -exec rm -f {} \;

export DEPCAT=$(pwd)/groovy-1.0-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in project.xml groovy-core/project.xml; do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > groovy-1.0-depmap.new.xml


%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav

sed -i -e 's|^PROGNAME|GROOVY_HOME=/usr/share/groovy-1.0; PROGNAME|' src/bin/startGroovy

# doesn't make real sense in Java 6
rm -rf groovy-core/src/main/groovy/sql/
rm -rf src/main/groovy/sql/
rm -rf src/test/groovy/sql/
rm groovy-core/src/test/groovy/bugs/ForAndSqlBug.groovy
rm src/test/groovy/bugs/ForAndSqlBug.groovy


%build
for p in project.xml groovy-core/project.xml; do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
      -Dmaven.repo.remote=file:/usr/share/maven1/repository \
      -Dmaven.home.local=$(pwd)/.maven \
      generate
export MAVEN_OPTS="-Xmx512m -XX:MaxPermSize=256m"
maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
      -Dmaven.repo.remote=file:/usr/share/maven1/repository \
      -Dmaven.home.local=$(pwd)/.maven \
      -Dmaven.test.failure.ignore=true \
      -Dmaven.test.error.ignore=true \
      java:compile
%{_jvmdir}/java/bin/javac  -target 1.5 -source 1.5 -d target/classes -classpath $(build-classpath commons-cli antlr):target/classes groovy-core/src/main/org/codehaus/groovy/antlr/java/*.java
maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
      -Dmaven.repo.remote=file:/usr/share/maven1/repository \
      -Dmaven.home.local=$(pwd)/.maven \
      -Dmaven.test.failure.ignore=true \
      -Dmaven.test.error.ignore=true \
      groovy:make-install javadoc:generate 

# delete DOS files
rm target/install/bin/*.bat

%install
find . -name "*.sav" -exec rm {} \;
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/install/lib/%{oname}-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 target/install/lib/%{oname}-starter.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-starter-%{version}.jar
install -m 644 target/install/embeddable/%{oname}-all-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-all-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
%add_to_maven_depmap groovy groovy %{version} JPP %{name}
%add_to_maven_depmap groovy groovy-all %{version} JPP %{name}-all

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# bin
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 target/install/bin/* $RPM_BUILD_ROOT%{_bindir}

# conf
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/conf
install -m 644 target/install/conf/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/conf

# lib
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/embeddable
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/embeddable
ln -sf %{javadir}/groovy10-all.jar
popd

# lib
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/lib
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/lib
build-jar-repository -p -s . \
ant \
ant/ant-junit \
ant-launcher \
antlr \
asm2/asm2-analysis \
asm2/asm2-attrs \
asm2/asm2 \
asm2/asm2-tree \
asm2/asm2-util \
axion \
bsf \
cglib21-nodep \
commons-cli \
commons-codec \
commons-collections \
commons-httpclient \
commons-logging \
commons-primitives \
jarjar \
jmock-cglib \
jmock \
junit \
openejb1/loader \
mockobjects-core \
nekohtml \
oro \
qdox \
radeox \
regexp \
jsp_2_0_api \
servlet_2_4_api \
xpp3 \
xstream \


ln -sf %{_javadir}/groovy10.jar
ln -sf %{_javadir}/groovy10-starter.jar
popd

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
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_4jpp6
- fixed build with moved maven1

* Tue Nov 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_4jpp6
- added -XX:MaxPermSize=256m to fix the build

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_4jpp6
- use maven1

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_4jpp6
- new jpp release

