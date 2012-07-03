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

%define namedversion 1.1-rc-3
%define bname groovy

Name:           groovy11
Summary:        Groovy scripting language
Url:            http://groovy.codehaus.org/
Version:        1.1
Release:        alt5_0.rc3.1jpp5
Epoch:          0
License:        Apache Software License 2.0
Group:          Development/Java
Source0:        groovy-1.1-rc3.tar.gz
# svn export http://svn.codehaus.org/groovy/tags/GROOVY_1_1_RC_3/groovy/ groovy-1.1-rc3


Source1:        groovy11-all.pom
Source2:        groovy11-all-minimal.pom

Patch0:         groovy-1.1-build-maven.patch
Patch1:         groovy-1.1-build-setup.patch
Patch2:         groovy-1.1-build.patch

BuildRequires: jpackage-utils >= 0:1.7.4

BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-antlr
BuildRequires: ant-junit
BuildRequires: antlr
BuildRequires: checkstyle
BuildRequires: cobertura
BuildRequires: junit
BuildRequires: xmlunit

BuildRequires: asm2 >= 0:2.2
BuildRequires: bsf
BuildRequires: cglib >= 0:2.1.3
BuildRequires: hsqldb
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-cli
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-httpclient
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-oro
BuildRequires: jarjar
BuildRequires: jline
BuildRequires: jmock
BuildRequires: jsp_2_0_api
BuildRequires: lucene
BuildRequires: mockobjects
BuildRequires: mx4j
BuildRequires: openejb1
BuildRequires: qdox
BuildRequires: servlet_2_4_api
BuildRequires: xpp3
BuildRequires: xstream

#
Requires: ant
Requires: ant-junit
Requires: antlr
Requires: asm2
Requires: bsf
Requires: jakarta-commons-cli
Requires: jakarta-commons-logging
Requires: jarjar
Requires: jline
Requires: jsp_2_0_api
Requires: junit
Requires: mockobjects
Requires: mx4j
Requires: servlet_2_4_api
Requires: xpp3
Requires: xstream

Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4
BuildArch:      noarch


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
%setup -q -n groovy-1.1-rc3
chmod -R go=u-w *
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
#mv bootstrap/maven-ant-tasks-2.0.7.jar.no bootstrap/maven-ant-tasks-2.0.7.jar

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2

#rm .externalToolBuilders/Groovy\ ensureGrammars.launch

mkdir -p target/lib/test
pushd target/lib/test
ln -sf $(build-classpath xmlunit)
ln -sf $(build-classpath xpp3)
ln -sf $(build-classpath ant/ant-junit)
ln -sf $(build-classpath bsf)
ln -sf $(build-classpath jmock)
ln -sf $(build-classpath jsp_2_0_api)
ln -sf $(build-classpath cglib-nodep)
ln -sf $(build-classpath asm2/asm2-tree)
ln -sf $(build-classpath jline)
ln -sf $(build-classpath asm2/asm2)
ln -sf $(build-classpath hsqldb)
ln -sf $(build-classpath mockobjects-core)
ln -sf $(build-classpath servlet_2_4_api)
ln -sf $(build-classpath jmock-cglib)
ln -sf $(build-classpath antlr)
ln -sf $(build-classpath junit)
ln -sf $(build-classpath asm2/asm2-util)
ln -sf $(build-classpath ant-launcher)
ln -sf $(build-classpath ant)
ln -sf $(build-classpath commons-logging)
ln -sf $(build-classpath asm2/asm2-analysis)
ln -sf $(build-classpath mx4j/mx4j)
ln -sf $(build-classpath xstream)
ln -sf $(build-classpath asm2/asm2-attrs)
ln -sf $(build-classpath commons-cli)
popd
mkdir -p target/lib/compile
pushd target/lib/compile
ln -sf $(build-classpath xpp3)
ln -sf $(build-classpath bsf)
ln -sf $(build-classpath jsp_2_0_api)
ln -sf $(build-classpath asm2/asm2-tree)
ln -sf $(build-classpath jline)
ln -sf $(build-classpath asm2/asm2)
ln -sf $(build-classpath mockobjects-core)
ln -sf $(build-classpath servlet_2_4_api)
ln -sf $(build-classpath antlr)
ln -sf $(build-classpath junit)
ln -sf $(build-classpath asm2/asm2-util)
ln -sf $(build-classpath ant)
ln -sf $(build-classpath asm2/asm2-analysis)
ln -sf $(build-classpath mx4j/mx4j)
ln -sf $(build-classpath xstream)
ln -sf $(build-classpath commons-cli)
popd
mkdir -p target/lib/runtime
pushd target/lib/runtime
ln -sf $(build-classpath xpp3)
ln -sf $(build-classpath ant/ant-junit)
ln -sf $(build-classpath bsf)
ln -sf $(build-classpath jsp_2_0_api)
ln -sf $(build-classpath asm2/asm2-tree)
ln -sf $(build-classpath jline)
ln -sf $(build-classpath asm2/asm2)
ln -sf $(build-classpath mockobjects-core)
ln -sf $(build-classpath servlet_2_4_api)
ln -sf $(build-classpath antlr)
ln -sf $(build-classpath junit)
ln -sf $(build-classpath asm2/asm2-util)
ln -sf $(build-classpath ant-launcher)
ln -sf $(build-classpath ant)
ln -sf $(build-classpath commons-logging)
ln -sf $(build-classpath asm2/asm2-analysis)
ln -sf $(build-classpath mx4j/mx4j)
ln -sf $(build-classpath xstream)
ln -sf $(build-classpath commons-cli)
popd
mkdir -p target/lib/tools
pushd target/lib/tools
ln -sf $(build-classpath oro)
ln -sf $(build-classpath commons-logging)
ln -sf $(build-classpath log4j)
ln -sf $(build-classpath asm2/asm2)
ln -sf $(build-classpath checkstyle)
ln -sf $(build-classpath antlr)
ln -sf $(build-classpath qdox)
ln -sf $(build-classpath jarjar)
ln -sf $(build-classpath commons-beanutils-core)
ln -sf $(build-classpath cobertura)
ln -sf $(build-classpath commons-collections)
ln -sf $(build-classpath commons-lang)
ln -sf $(build-classpath commons-cli)
popd
mkdir -p target/lib/examples
pushd target/lib/examples
ln -sf $(build-classpath lucene)
ln -sf $(build-classpath openejb1/loader)
ln -sf $(build-classpath commons-httpclient)
popd

%build
#export CLASSPATH=$(build-classpath xalan-j2-serializer)
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -DskipTests=true install javadoc 

find . -name "*.bat" -exec rm {} \;
find . -name "*.sav*" -exec rm {} \;

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/dist/%{bname}-%{namedversion}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 target/dist/%{bname}-all-%{namedversion}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-all-%{version}.jar
install -m 644 target/dist/%{bname}-all-minimal-%{namedversion}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-all-minimal-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms and depmap frags
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.codehaus.groovy groovy %{namedversion} JPP %{name}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-all.pom
%add_to_maven_depmap org.codehaus.groovy groovy-all %{namedversion} JPP %{name}-all
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-all-minimal.pom
%add_to_maven_depmap org.codehaus.groovy groovy-all-minimal %{namedversion} JPP %{name}-all-minimal

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/html/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# bin
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 target/install/bin/groovy $RPM_BUILD_ROOT%{_bindir}/groovy11
install -m 755 target/install/bin/groovyc $RPM_BUILD_ROOT%{_bindir}/groovyc11
install -m 755 target/install/bin/groovyConsole $RPM_BUILD_ROOT%{_bindir}/groovyConsole11
install -m 755 target/install/bin/groovysh $RPM_BUILD_ROOT%{_bindir}/groovysh11
install -m 755 target/install/bin/java2groovy $RPM_BUILD_ROOT%{_bindir}/java2groovy11
install -m 755 target/install/bin/startGroovy $RPM_BUILD_ROOT%{_bindir}/startGroovy11

# conf
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/conf
install -m 644 target/install/conf/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/conf

# lib
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/embeddable
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/embeddable
ln -sf %{_javadir}/%name-all.jar
popd

# lib
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/lib
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/lib
build-jar-repository . \
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
mockobjects-core \
mx4j/mx4j \
servlet_2_4_api \
xpp3 \
xstream \

ln -sf %{_javadir}/%name.jar
popd

# bugfix: Package groovy11 has broken dep on /usr/bin/startGroovy
sed -i -e 's,startGroovy,startGroovy11,g' %buildroot%_bindir/*

%preun
if [ "$1" = "0" ]; then
  rm %{_datadir}/%{name}-%{version}/lib/*.jar
fi

%pre
rm -f %{_datadir}/%{name}-%{version}/lib/*

%post
rebuild-jar-repository %{_datadir}/%{name}-%{version}/lib
:

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%doc LICENSE.txt
%{_javadir}/*
%attr(755, root, root) %{_bindir}/*
%{_datadir}/%{name}-%{version}
%{_datadir}/maven2
%{_mavendepmapfragdir}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt5_0.rc3.1jpp5
- fixed broken dep on /usr/bin/startGroovy

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt4_0.rc3.1jpp5
- fixed broken groovy symlink

* Tue May 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_0.rc3.1jpp5
- fixes for java6 support

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_0.rc3.1jpp5
- rebuild with new lucene

* Sun Oct 05 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_0.rc3.1jpp5
- converted from JPackage by jppimport script

