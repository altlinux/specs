BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 1.7.10
%define name groovy17
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

%global namedversion %{version}
%global bname groovy
%global majmin 17

Name:           groovy%{majmin}
Version:        1.7.10
Release:        alt2_3jpp6
Epoch:          0
Summary:        Groovy scripting language
License:        ASL 2.0
Group:          Development/Java
URL:            http://groovy.codehaus.org/
# svn export http://svn.codehaus.org/groovy/tags/GROOVY_1_7_10/ groovy-1.7.10 && tar cjf groovy-1.7.10.tar.bz2 groovy-1.7.10
# Exported revision 22122.
Source0:        groovy-%{namedversion}.tar.bz2
Source1:        http://repository.codehaus.org/org/codehaus/groovy/groovy-all/1.7.10/groovy-all-%{namedversion}.pom
Patch0:         groovy%{majmin}-build.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires:       ant
Requires:       ant-junit
Requires:       ant-trax
Requires:       antlr
Requires:       objectweb-asm
Requires:       bsf
Requires:       jakarta-commons-cli
Requires:       jakarta-commons-logging
Requires:       jarjar
Requires:       jline
Requires:       jpackage-utils
Requires:       jsp_2_0_api
Requires:       junit
Requires:       livetribe-jsr223
Requires:       mx4j
Requires:       servlet_2_4_api
Requires:       xpp3-minimal
Requires:       xstream
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-antlr
BuildRequires:  ant-junit
BuildRequires:  ant-trax
BuildRequires:  antlr
BuildRequires:  aqute-bndlib
BuildRequires:  cewolf
BuildRequires:  checkstyle4
BuildRequires:  cobertura
#BuildRequires:  eclipse-rcp
BuildRequires:  jcommon
BuildRequires:  jfreechart
BuildRequires:  junit4
BuildRequires:  lucene1
BuildRequires:  maven-ant-tasks
BuildRequires:  openejb1
BuildRequires:  xmlunit
BuildRequires:  objectweb-asm
BuildRequires:  bsf
BuildRequires:  cglib21 >= 0:2.1.3
BuildRequires:  hsqldb
BuildRequires:  apache-commons-parent
BuildRequires:  jakarta-commons-beanutils
BuildRequires:  jakarta-commons-cli
BuildRequires:  jakarta-commons-codec
BuildRequires:  jakarta-commons-collections
BuildRequires:  jakarta-commons-httpclient
BuildRequires:  jakarta-commons-lang
BuildRequires:  jakarta-commons-logging
BuildRequires:  apache-commons-primitives
BuildRequires:  apache-ivy
BuildRequires:  jakarta-oro
BuildRequires:  jansi
BuildRequires:  jarjar
BuildRequires:  jline
BuildRequires:  jmock
BuildRequires:  jsp_2_0_api
BuildRequires:  lucene
BuildRequires:  livetribe-jsr223
BuildRequires:  mx4j
BuildRequires:  openejb1
BuildRequires:  qdox
BuildRequires:  servlet_2_4_api
BuildRequires:  xpp3-minimal
BuildRequires:  xstream
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
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n groovy-%{namedversion}
find -type f \( -name "*.jar" -a -not -name "GroovyJarTest.jar" \) | xargs -t rm
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

%patch0 -p0 -b .sav0

mkdir -p target/lib/compile
pushd target/lib/compile
ln -s $(build-classpath ant) ant.jar
ln -s $(build-classpath ant/ant-antlr) ant-antlr.jar
ln -s $(build-classpath antlr)
ln -s $(build-classpath objectweb-asm/asm)
ln -s $(build-classpath objectweb-asm/asm-analysis)
ln -s $(build-classpath objectweb-asm/asm-tree)
ln -s $(build-classpath objectweb-asm/asm-util)
ln -s $(build-classpath bsf)
ln -s $(build-classpath commons-cli)
ln -s $(build-classpath apache-ivy)
ln -s $(build-classpath jansi)
ln -s $(build-classpath jline)
ln -s $(build-classpath jsp_2_0_api)
ln -s $(build-classpath junit4)
ln -s $(build-classpath livetribe-jsr223)
ln -s $(build-classpath servlet_2_4_api)
ln -s $(build-classpath xstream)
popd
mkdir -p target/lib/examples
pushd target/lib/examples
ln -s $(build-classpath commons-httpclient)
ln -s $(build-classpath lucene1)
ln -s $(build-classpath openejb1/loader)
#ln -s $(ls /usr/lib/eclipse/plugins/org.eclipse.osgi_3*.jar)
popd
mkdir -p target/lib/extras
pushd target/lib/extras
ln -s $(build-classpath mx4j/mx4j)
popd
mkdir -p target/lib/runtime
pushd target/lib/runtime
ln -s $(build-classpath ant) ant.jar
ln -s $(build-classpath ant-launcher) ant-launcher.jar
ln -s $(build-classpath ant/ant-junit) ant-junit.jar
ln -s $(build-classpath antlr)
ln -s $(build-classpath objectweb-asm/asm)
ln -s $(build-classpath objectweb-asm/asm-analysis)
ln -s $(build-classpath objectweb-asm/asm-tree)
ln -s $(build-classpath objectweb-asm/asm-util)
ln -s $(build-classpath bsf)
ln -s $(build-classpath commons-cli)
ln -s $(build-classpath commons-logging)
ln -s $(build-classpath apache-ivy)
ln -s $(build-classpath jline)
ln -s $(build-classpath jsp_2_0_api)
ln -s $(build-classpath junit4)
ln -s $(build-classpath servlet_2_4_api)
ln -s $(build-classpath xstream)
popd
mkdir -p target/lib/test
pushd target/lib/test
ln -s $(build-classpath ant) ant.jar
ln -s $(build-classpath ant/ant-antlr) ant-antlr.jar
ln -s $(build-classpath ant/ant-junit) ant-junit.jar
ln -s $(build-classpath ant-launcher) ant-launcher.jar
ln -s $(build-classpath ant-testutil) ant-testutil.jar
ln -s $(build-classpath antlr)
ln -s $(build-classpath objectweb-asm/asm)
ln -s $(build-classpath objectweb-asm/asm-analysis)
ln -s $(build-classpath objectweb-asm/asm-attrs)
ln -s $(build-classpath objectweb-asm/asm-tree)
ln -s $(build-classpath objectweb-asm/asm-util)
ln -s $(build-classpath bsf)
ln -s $(build-classpath cglib21-nodep)
ln -s $(build-classpath commons-cli)
ln -s $(build-classpath commons-logging)
ln -s $(build-classpath commons-primitives)
ln -s $(build-classpath hsqldb)
ln -s $(build-classpath apache-ivy)
ln -s $(build-classpath jline)
ln -s $(build-classpath jmock)
ln -s $(build-classpath jmock-cglib)
ln -s $(build-classpath jsp_2_0_api)
ln -s $(build-classpath junit4)
ln -s $(build-classpath livetribe-jsr223)
ln -s $(build-classpath qdox)
ln -s $(build-classpath servlet_2_4_api)
ln -s $(build-classpath xmlunit)
ln -s $(build-classpath xstream)
popd
mkdir -p target/lib/tools
pushd target/lib/tools
ln -s $(build-classpath ant) ant.jar
ln -s $(build-classpath antlr)
ln -s $(build-classpath objectweb-asm/asm)
ln -s $(build-classpath objectweb-asm/asm-tree)
ln -s $(build-classpath aqute-bndlib)
#ln -s $(build-classpath backport-util-concurrent)
ln -s $(build-classpath checkstyle4)
ln -s $(build-classpath cobertura)
ln -s $(build-classpath commons-beanutils)
ln -s $(build-classpath commons-cli)
ln -s $(build-classpath commons-collections)
ln -s $(build-classpath commons-lang)
ln -s $(build-classpath commons-logging)
ln -s $(build-classpath jarjar)
ln -s $(build-classpath log4j)
ln -s $(build-classpath oro)
ln -s $(build-classpath qdox)
popd

%build
export CLASSPATH=
export OPT_JAR_LIST="maven-ant-tasks ant/ant-trax ant/ant-antlr ant/ant-junit junit4"
export ANT_OPTS="-DskipFetch=true -DforceRetro=falsei -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5"
%{ant} -Duser.home=`pwd`/.groovy dist

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}

install -p -m 644 target/dist/%{bname}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}-%{namedversion}.jar
#install -p -m 644 target/dist/%{bname}-all-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}-all-%{namedversion}.jar
install -p -m 644 target/install/embeddable/%{bname}-all-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}-all-%{namedversion}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{namedversion}*; do ln -s ${jar} `echo $jar| sed  "s|-%{namedversion}||g"`; done)

# poms and depmap frags
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -p -m 644 pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.codehaus.groovy groovy %{namedversion} JPP %{name}
%add_to_maven_depmap org.codehaus.groovy %{name} %{namedversion} JPP %{name}
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-all.pom
%add_to_maven_depmap org.codehaus.groovy groovy-all %{namedversion} JPP %{name}-all
%add_to_maven_depmap org.codehaus.groovy %{name}-all %{namedversion} JPP %{name}-all

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
cp -pr target/html/api/* %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
ln -s %{name}-%{namedversion} %{buildroot}%{_javadocdir}/%{name}

# bin
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{namedversion}
install -p -m 755 target/install/bin/groovy %{buildroot}%{_datadir}/%{name}-%{namedversion}/groovy%{majmin}
install -p -m 755 target/install/bin/groovyc %{buildroot}%{_datadir}/%{name}-%{namedversion}/groovyc%{majmin}
install -p -m 755 target/install/bin/groovyConsole %{buildroot}%{_datadir}/%{name}-%{namedversion}/groovyConsole%{majmin}
install -p -m 755 target/install/bin/groovysh %{buildroot}%{_datadir}/%{name}-%{namedversion}/groovysh%{majmin}
install -p -m 755 target/install/bin/java2groovy %{buildroot}%{_datadir}/%{name}-%{namedversion}/java2groovy%{majmin}
install -p -m 755 target/install/bin/startGroovy %{buildroot}%{_datadir}/%{name}-%{namedversion}/startGroovy%{majmin}
install -d -m 755 %{buildroot}%{_bindir}
for i in %{buildroot}%{_datadir}/%{name}-%{namedversion}/*; do
  ln -s %{_datadir}/%{name}-%{namedversion}/`basename $i` %{buildroot}%{_bindir}/`basename $i`
done

# conf
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{namedversion}/conf
cp -pr target/install/conf/* %{buildroot}%{_datadir}/%{name}-%{namedversion}/conf

# lib
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{namedversion}/embeddable
pushd %{buildroot}%{_datadir}/%{name}-%{namedversion}/embeddable
ln -s %{_javadir}/%{name}-all.jar groovy-all-%{namedversion}.jar
popd

# lib
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{namedversion}/lib
pushd %{buildroot}%{_datadir}/%{name}-%{namedversion}/lib
for i in \
ant \
ant/ant-junit \
ant-launcher \
antlr \
objectweb-asm/asm-analysis \
objectweb-asm/asm \
objectweb-asm/asm-tree \
objectweb-asm/asm-util \
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
; do
ln -s $(build-classpath $i) .;
done
ln -s %{_javadir}/%{name}.jar groovy-%{namedversion}.jar
popd

ln -s %{name}-%{namedversion} %{buildroot}%{_datadir}/%{name}
# bugfix: Package groovy17 has broken dep on /usr/bin/startGroovy
sed -i -e 's,startGroovy,startGroovy17,g' %buildroot%_datadir/%{name}-%{version}/*roov* ||:

%files
%doc LICENSE.txt
%{_bindir}/groovy%{majmin}
%{_bindir}/groovyConsole%{majmin}
%{_bindir}/groovyc%{majmin}
%{_bindir}/groovysh%{majmin}
%{_bindir}/java2groovy%{majmin}
%{_bindir}/startGroovy%{majmin}
%attr(0755,root,root) %{_datadir}/%{name}-%{namedversion}/groovy%{majmin}
%attr(0755,root,root) %{_datadir}/%{name}-%{namedversion}/groovyConsole%{majmin}
%attr(0755,root,root) %{_datadir}/%{name}-%{namedversion}/groovyc%{majmin}
%attr(0755,root,root) %{_datadir}/%{name}-%{namedversion}/groovysh%{majmin}
%attr(0755,root,root) %{_datadir}/%{name}-%{namedversion}/java2groovy%{majmin}
%attr(0755,root,root) %{_datadir}/%{name}-%{namedversion}/startGroovy%{majmin}
%{_javadir}*/%{name}-%{namedversion}.jar
%{_javadir}*/%{name}.jar
%{_javadir}*/%{name}-all-%{namedversion}.jar
%{_javadir}*/%{name}-all.jar
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}-%{namedversion}
%dir %{_datadir}/%{name}-%{namedversion}/conf
# FIXME: (dwalluck): move to %%{_sysconfdir}
%config(noreplace) %{_datadir}/%{name}-%{namedversion}/conf/groovy-starter.conf
%dir %{_datadir}/%{name}-%{namedversion}/embeddable
%{_datadir}/%{name}-%{namedversion}/embeddable/groovy-all-%{namedversion}.jar
%dir %{_datadir}/%{name}-%{namedversion}/lib
%{_datadir}/%{name}-%{namedversion}/lib/ant-junit.jar
%{_datadir}/%{name}-%{namedversion}/lib/ant-launcher.jar
%{_datadir}/%{name}-%{namedversion}/lib/ant.jar
%{_datadir}/%{name}-%{namedversion}/lib/antlr.jar
%{_datadir}/%{name}-%{namedversion}/lib/apache-ivy.jar
%{_datadir}/%{name}-%{namedversion}/lib/asm-analysis.jar
%{_datadir}/%{name}-%{namedversion}/lib/asm-tree.jar
%{_datadir}/%{name}-%{namedversion}/lib/asm-util.jar
%{_datadir}/%{name}-%{namedversion}/lib/asm.jar
%{_datadir}/%{name}-%{namedversion}/lib/bsf.jar
%{_datadir}/%{name}-%{namedversion}/lib/commons-cli.jar
%{_datadir}/%{name}-%{namedversion}/lib/commons-logging.jar
%{_datadir}/%{name}-%{namedversion}/lib/groovy-%{namedversion}.jar
%{_datadir}/%{name}-%{namedversion}/lib/jline.jar
%{_datadir}/%{name}-%{namedversion}/lib/jsp_2_0_api.jar
%{_datadir}/%{name}-%{namedversion}/lib/junit.jar
%{_datadir}/%{name}-%{namedversion}/lib/mx4j.jar
%{_datadir}/%{name}-%{namedversion}/lib/servlet_2_4_api.jar
%{_datadir}/%{name}-%{namedversion}/lib/xpp3.jar
%{_datadir}/%{name}-%{namedversion}/lib/xstream.jar
%{_datadir}/maven2/poms/JPP-%{name}-all.pom
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{namedversion}
%{_javadocdir}/%{name}

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.10-alt2_3jpp6
- fixed parasite dep on groovy10

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.10-alt1_3jpp6
- new version

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.7.6-alt1_1jpp6
- new version

