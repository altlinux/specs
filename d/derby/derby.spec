BuildRequires: felix-framework
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# one of the sources is a zip file
BuildRequires: unzip
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

%define without_tests %{!?_with_tests:1}%{?_with_tests:0}
%define with_tests %{?_with_tests:1}%{!?_with_tests:0}


%define gcj_support 0


Name:           derby
Version:        10.6.2.1
Release:        alt3_2jpp6
Epoch:          0
Summary:        Derby DB (ex Cloudscape)

Group:          Databases
License:        ASL 2.0
URL:            http://db.apache.org/derby/
Source0:        http://www.apache.org/dist/db/derby/db-derby-10.6.2.1/db-derby-10.6.2.1-src.tar.gz
Source1:        http://prdownloads.sourceforge.net/dita-ot/DITA-OT1.1.2.1_bin-ASL.zip
Source2:        http://repo2.maven.org/maven2/org/apache/derby/derby/10.6.2.1/derby-10.6.2.1.pom
Source3:        http://repo2.maven.org/maven2/org/apache/derby/derbyclient/10.6.2.1/derbyclient-10.6.2.1.pom
Source4:        http://repo2.maven.org/maven2/org/apache/derby/derbyLocale_cs/10.6.2.1/derbyLocale_cs-10.6.2.1.pom
Source5:        http://repo2.maven.org/maven2/org/apache/derby/derbyLocale_de_DE/10.6.2.1/derbyLocale_de_DE-10.6.2.1.pom
Source6:        http://repo2.maven.org/maven2/org/apache/derby/derbyLocale_es/10.6.2.1/derbyLocale_es-10.6.2.1.pom
Source7:        http://repo2.maven.org/maven2/org/apache/derby/derbyLocale_fr/10.6.2.1/derbyLocale_fr-10.6.2.1.pom
Source8:        http://repo2.maven.org/maven2/org/apache/derby/derbyLocale_hu/10.6.2.1/derbyLocale_hu-10.6.2.1.pom
Source9:        http://repo2.maven.org/maven2/org/apache/derby/derbyLocale_it/10.6.2.1/derbyLocale_it-10.6.2.1.pom
Source10:       http://repo2.maven.org/maven2/org/apache/derby/derbyLocale_ja_JP/10.6.2.1/derbyLocale_ja_JP-10.6.2.1.pom
Source11:       http://repo2.maven.org/maven2/org/apache/derby/derbyLocale_ko_KR/10.6.2.1/derbyLocale_ko_KR-10.6.2.1.pom
Source12:       http://repo2.maven.org/maven2/org/apache/derby/derbyLocale_pl/10.6.2.1/derbyLocale_pl-10.6.2.1.pom
Source13:       http://repo2.maven.org/maven2/org/apache/derby/derbyLocale_pt_BR/10.6.2.1/derbyLocale_pt_BR-10.6.2.1.pom
Source14:       http://repo2.maven.org/maven2/org/apache/derby/derbyLocale_ru/10.6.2.1/derbyLocale_ru-10.6.2.1.pom
Source15:       http://repo2.maven.org/maven2/org/apache/derby/derbyLocale_zh_CN/10.6.2.1/derbyLocale_zh_CN-10.6.2.1.pom
Source16:       http://repo2.maven.org/maven2/org/apache/derby/derbyLocale_zh_TW/10.6.2.1/derbyLocale_zh_TW-10.6.2.1.pom
Source17:       http://repo2.maven.org/maven2/org/apache/derby/derbynet/10.6.2.1/derbynet-10.6.2.1.pom
Source18:       http://repo2.maven.org/maven2/org/apache/derby/derbyrun/10.6.2.1/derbyrun-10.6.2.1.pom
Source19:       http://repo2.maven.org/maven2/org/apache/derby/derbytools/10.6.2.1/derbytools-10.6.2.1.pom
Source20:       http://repo2.maven.org/maven2/org/apache/derby/derby-project/10.6.2.1/derby-project-10.6.2.1.pom

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant
BuildRequires: ant17
BuildRequires: ant17-nodeps
BuildRequires: ant17-trax
BuildRequires: avalon-framework
#BuildRequires: felix
BuildRequires: jakarta-commons-io
BuildRequires: jakarta-commons-logging
BuildRequires: javacc
BuildRequires: junit
BuildRequires: oro
BuildRequires: servlet_2_4_api
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: xmlgraphics-commons
BuildRequires: xmlgraphics-batik-rasterizer
BuildRequires: xmlgraphics-fop
Requires: jta
Requires: oro
Requires: servletapi5
Requires: xalan-j2
Requires: xerces-j2
Requires: xml-commons-jaxp-1.3-apis
Source44: import.info

%description
The Derby project develops open source database technology 
that is: Pure Java, Easy to use, Small footprint, Standards 
based, Secure.
The core of the technology, Derby.s database engine is a 
full functioned relational embedded database engine. JDBC 
and SQL are the programming APIs. 
The Derby network server increases the reach of the Derby 
database engine by providing traditional client server 
functionality. The network server allows clients to connect 
over TCP/IP using the standard DRDA protocol. The network 
server allows the Derby engine to support networked JDBC, 
ODBC/CLI, Perl and PHP. 
Database Utilities:
ij -- a tool that allows SQL scripts to be executed against 
      any JDBC database. 
dblook -- Schema extraction tool for a Derby database. 
sysinfo -- Utility to display version numbers and class path. 

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
Javadoc for %{name}

%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    manual
Documents for %{name}

%package        demo
Summary:        Examples for %{name}
Group:          Development/Documentation

%description    demo
Examples for %{name}

%prep
%setup -q -c
ln -s db-%{name}-%{version}-doc-src doc
pushd doc
unzip -q %{SOURCE1}
popd

for j in $(find . -name "*.jar"); do
        mv $j $j.no
done
mv doc/DITA-OT1.1.2.1/lib/dost.jar.no doc/DITA-OT1.1.2.1/lib/dost.jar

%if 1
ln -sf $(build-classpath avalon-framework) doc/lib/avalon-framework-4.2.0.jar
ln -sf $(build-classpath xmlgraphics-batik/rasterizer) doc/lib
ln -sf $(build-classpath commons-io) doc/lib/commons-io-1.1.jar
ln -sf $(build-classpath commons-logging) doc/lib/commons-logging-1.0.4.jar
ln -sf $(build-classpath xmlgraphics-commons) doc/lib/xmlgraphics-commons-1.1.jar
ln -sf $(build-classpath xmlgraphics-fop) doc/lib/fop.jar
ln -sf $(build-classpath xalan-j2) doc/lib/xalan-2.7.0.jar
ln -sf $(build-classpath xalan-j2-serializer) doc/lib/serializer-2.7.0.jar
ln -sf $(build-classpath xerces-j2) doc/lib/xercesImpl-2.7.1.jar
ln -sf $(build-classpath xml-commons-jaxp-1.3-apis) doc/lib/xml-apis-1.3.02.jar
%endif

cp %{SOURCE1} doc/lib

pushd db-%{name}-%{version}-src
mv java/testing/org/apache/derbyTesting/functionTests/testData/v1/j1v1.jar.no \
   java/testing/org/apache/derbyTesting/functionTests/testData/v1/j1v1.jar
mv java/testing/org/apache/derbyTesting/functionTests/testData/v2/j1v2.jar.no \
   java/testing/org/apache/derbyTesting/functionTests/testData/v2/j1v2.jar
mv java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_emc1.jar.no \
   java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_emc1.jar
mv java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_emc2.jar.no \
   java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_emc2.jar
mv java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_emc2l.jar.no \
   java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_emc2l.jar
mv java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_emc2s.jar.no \
   java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_emc2s.jar
mv java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_emc2sm.jar.no \
   java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_emc2sm.jar
mv java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_emcaddon.jar.no \
   java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_emcaddon.jar
mv java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_id.jar.no \
   java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_id.jar
mv java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_java.jar.no \
   java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_java.jar
mv java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_ot1.jar.no \
   java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_ot1.jar
mv java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_ot2.jar.no \
   java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_ot2.jar
mv java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_ot3.jar.no \
   java/testing/org/apache/derbyTesting/functionTests/tests/lang/dcl_ot3.jar
mv java/testing/org/apache/derbyTesting/functionTests/tests/lang/dummy_vti.jar.no \
   java/testing/org/apache/derbyTesting/functionTests/tests/lang/dummy_vti.jar
mv java/testing/org/apache/derbyTesting/functionTests/tests/perf/existingDb.jar.no \
   java/testing/org/apache/derbyTesting/functionTests/tests/perf/existingDb.jar
mv java/testing/org/apache/derbyTesting/functionTests/tests/store/brtestjar.jar.no \
   java/testing/org/apache/derbyTesting/functionTests/tests/store/brtestjar.jar
mv java/testing/org/apache/derbyTesting/functionTests/tests/store/obtest_customer.jar.no \
   java/testing/org/apache/derbyTesting/functionTests/tests/store/obtest_customer.jar
mv java/testing/org/apache/derbyTesting/functionTests/tests/tools/dblook_test.jar.no \
   java/testing/org/apache/derbyTesting/functionTests/tests/tools/dblook_test.jar
#tools/java/geronimo-spec-servlet-2.4-rc4.jar.no
ln -sf $(build-classpath servlet_2_4_api) tools/java
#tools/java/jakarta-oro-2.0.8.jar.no
ln -sf $(build-classpath jakarta-oro) tools/java
#tools/java/javacc.jar.no
ln -sf $(build-classpath javacc) tools/java
#tools/java/serializer.jar.no
ln -sf $(build-classpath xalan-j2-serializer) tools/java
#tools/java/xalan.jar.no
ln -sf $(build-classpath xalan-j2) tools/java
#tools/java/xercesImpl.jar.no
ln -sf $(build-classpath xerces-j2) tools/java
popd

%build
export CLASSPATH=$(build-classpath ant17)
pushd db-%{name}-%{version}-src
ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
   -Dant.library.dir=%{_javadir} \
   -Djunit=$(build-classpath junit) \
   -Doro=$(build-classpath oro) \
   -Dosgi=$(build-classpath felix/org.osgi.core.jar) \
   -Dservlet24=$(build-classpath servlet_2_4_api) \
   -DxercesImpl=$(build-classpath xalan-j2 xerces-j2) \
   all
ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  buildjars
ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
   -Dant.library.dir=%{_javadir} \
   -Djunit=$(build-classpath junit) \
   -Doro=$(build-classpath oro) \
   -Dosgi=$(build-classpath felix/org.osgi.core.jar) \
   -Dservlet24=$(build-classpath servlet_2_4_api) \
   -DxercesImpl=$(build-classpath xalan-j2 xerces-j2) \
   javadoc
popd

pushd doc
ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  html
ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  monohtml
popd

%install

# jars
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 %{SOURCE20} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derby-project.pom
%add_to_maven_depmap org.apache.derby derby-project %{version} JPP/%{name} derby-project
install -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derby.pom
%add_to_maven_depmap org.apache.derby derby %{version} JPP/%{name} derby
pushd db-derby-10.6.2.1-src/
install -m 644 jars/sane/derby.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derby-%{version}.jar
install -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derby.pom
%add_to_maven_depmap org.apache.derby derby %{version} JPP/%{name} derby

install -m 644 jars/sane/derbyclient.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derbyclient-%{version}.jar
install -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derbyclient.pom
%add_to_maven_depmap org.apache.derby derbyclient %{version} JPP/%{name} derbyclient

install -m 644 jars/sane/derbyLocale_cs.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derbyLocale_cs-%{version}.jar
install -m 644 %{SOURCE4} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derbyLocale_cs.pom
%add_to_maven_depmap org.apache.derby derbyLocale_cs %{version} JPP/%{name} derbyLocale_cs

install -m 644 jars/sane/derbyLocale_de_DE.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derbyLocale_de_DE-%{version}.jar
install -m 644 %{SOURCE5} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derbyLocale_de_DE.pom
%add_to_maven_depmap org.apache.derby derbyLocale_de_DE %{version} JPP/%{name} derbyLocale_de_DE

install -m 644 jars/sane/derbyLocale_es.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derbyLocale_es-%{version}.jar
install -m 644 %{SOURCE6} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derbyLocale_es.pom
%add_to_maven_depmap org.apache.derby derbyLocale_es %{version} JPP/%{name} derbyLocale_es

install -m 644 jars/sane/derbyLocale_fr.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derbyLocale_fr-%{version}.jar
install -m 644 %{SOURCE7} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derbyLocale_fr.pom
%add_to_maven_depmap org.apache.derby derbyLocale_fr %{version} JPP/%{name} derbyLocale_fr

install -m 644 jars/sane/derbyLocale_hu.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derbyLocale_hu-%{version}.jar
install -m 644 %{SOURCE8} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derbyLocale_hu.pom
%add_to_maven_depmap org.apache.derby derbyLocale_hu %{version} JPP/%{name} derbyLocale_hu

install -m 644 jars/sane/derbyLocale_it.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derbyLocale_it-%{version}.jar
install -m 644 %{SOURCE9} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derbyLocale_it.pom
%add_to_maven_depmap org.apache.derby derbyLocale_it %{version} JPP/%{name} derbyLocale_it

install -m 644 jars/sane/derbyLocale_ja_JP.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derbyLocale_ja_JP-%{version}.jar
install -m 644 %{SOURCE10} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derbyLocale_ja_JP.pom
%add_to_maven_depmap org.apache.derby derbyLocale_ja_JP %{version} JPP/%{name} derbyLocale_ja_JP

install -m 644 jars/sane/derbyLocale_ko_KR.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derbyLocale_ko_KR-%{version}.jar
install -m 644 %{SOURCE11} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derbyLocale_ko_KR.pom
%add_to_maven_depmap org.apache.derby derbyLocale_ko_KR %{version} JPP/%{name} derbyLocale_ko_KR

install -m 644 jars/sane/derbyLocale_pl.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derbyLocale_pl-%{version}.jar
install -m 644 %{SOURCE12} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derbyLocale_pl.pom
%add_to_maven_depmap org.apache.derby derbyLocale_pl %{version} JPP/%{name} derbyLocale_pl

install -m 644 jars/sane/derbyLocale_pt_BR.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derbyLocale_pt_BR-%{version}.jar
install -m 644 %{SOURCE13} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derbyLocale_pt_BR.pom
%add_to_maven_depmap org.apache.derby derbyLocale_pt_BR %{version} JPP/%{name} derbyLocale_pt_BR

install -m 644 jars/sane/derbyLocale_ru.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derbyLocale_ru-%{version}.jar
install -m 644 %{SOURCE14} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derbyLocale_ru.pom
%add_to_maven_depmap org.apache.derby derbyLocale_ru %{version} JPP/%{name} derbyLocale_ru

install -m 644 jars/sane/derbyLocale_zh_CN.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derbyLocale_zh_CN-%{version}.jar
install -m 644 %{SOURCE15} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derbyLocale_zh_CN.pom
%add_to_maven_depmap org.apache.derby derbyLocale_zh_CN %{version} JPP/%{name} derbyLocale_zh_CN

install -m 644 jars/sane/derbyLocale_zh_TW.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derbyLocale_zh_TW-%{version}.jar
install -m 644 %{SOURCE16} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derbyLocale_zh_TW.pom
%add_to_maven_depmap org.apache.derby derbyLocale_zh_TW %{version} JPP/%{name} derbyLocale_zh_TW

install -m 644 jars/sane/derbynet.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derbynet-%{version}.jar
install -m 644 %{SOURCE17} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derbynet.pom
%add_to_maven_depmap org.apache.derby derbynet %{version} JPP/%{name} derbynet

install -m 644 jars/sane/derbyrun.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derbyrun-%{version}.jar
install -m 644 %{SOURCE18} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derbyrun.pom
%add_to_maven_depmap org.apache.derby derbyrun %{version} JPP/%{name} derbyrun

%if %{with_tests}
install -m 644 jars/sane/derbyTesting.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derbyTesting-%{version}.jar
%endif

install -m 644 jars/sane/derbytools.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/derbytools-%{version}.jar
install -m 644 %{SOURCE19} \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.derby-derbytools.pom
%add_to_maven_depmap org.apache.derby derbytools %{version} JPP/%{name} derbytools
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)


install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 jars/sane/derby.war \
        $RPM_BUILD_ROOT%{_datadir}/%{name}/derby-%{version}.war
install -m 644 LICENSE $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 NOTICE $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 README $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 RELEASE-NOTES.html $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 STATUS $RPM_BUILD_ROOT%{_datadir}/%{name}

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/publishedapi $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/engine $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}
cp -pr javadoc/language $RPM_BUILD_ROOT%{_docdir}/%{name}/javadoc-language
cp -pr javadoc/tools $RPM_BUILD_ROOT%{_docdir}/%{name}/javadoc-tools
popd

install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}/fo
cp doc/out/*/*.fo $RPM_BUILD_ROOT%{_docdir}/%{name}/fo
rm doc/out/*/*.fo
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}/html_single
install -m 0644 doc/out/adminguide/adminguide-single.html $RPM_BUILD_ROOT%{_docdir}/%{name}/html_single
rm doc/out/adminguide/adminguide-single.html
install -m 0644 doc/out/devguide/devguide-single.html $RPM_BUILD_ROOT%{_docdir}/%{name}/html_single
rm doc/out/devguide/devguide-single.html
install -m 0644 doc/out/getstart/getstart-single.html $RPM_BUILD_ROOT%{_docdir}/%{name}/html_single
rm doc/out/getstart/getstart-single.html
cp -pr doc/out/images $RPM_BUILD_ROOT%{_docdir}/%{name}/html_single
install -m 0644 doc/out/ref/ref-single.html $RPM_BUILD_ROOT%{_docdir}/%{name}/html_single
rm doc/out/ref/ref-single.html
install -m 0644 doc/out/tools/tools-single.html $RPM_BUILD_ROOT%{_docdir}/%{name}/html_single
rm doc/out/tools/tools-single.html
install -m 0644 doc/out/tuning/tuning-single.html $RPM_BUILD_ROOT%{_docdir}/%{name}/html_single
rm doc/out/tuning/tuning-single.html
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}/html
cp -pr doc/out/adminguide $RPM_BUILD_ROOT%{_docdir}/%{name}/html
cp -pr doc/out/devguide $RPM_BUILD_ROOT%{_docdir}/%{name}/html
cp -pr doc/out/getstart $RPM_BUILD_ROOT%{_docdir}/%{name}/html
cp -pr doc/out/getstart $RPM_BUILD_ROOT%{_docdir}/%{name}/html
cp -pr doc/out/images $RPM_BUILD_ROOT%{_docdir}/%{name}/html
cp -pr doc/out/ref $RPM_BUILD_ROOT%{_docdir}/%{name}/html
cp -pr doc/out/tools $RPM_BUILD_ROOT%{_docdir}/%{name}/html
cp -pr doc/out/tuning $RPM_BUILD_ROOT%{_docdir}/%{name}/html

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/%{name}
%{_datadir}/%{name}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/derby*-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}

%changelog
* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:10.6.2.1-alt3_2jpp6
- dropped felix dependency

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:10.6.2.1-alt2_2jpp6
- built with java 6

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:10.6.2.1-alt1_2jpp6
- new version

* Sat Feb 28 2009 Igor Vlasenko <viy@altlinux.ru> 0:10.3.3.0-alt2_1jpp6
- packaged jdbc driver

* Thu Jan 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:10.3.3.0-alt1_1jpp6
- new version

* Wed Nov 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:10.1.1.0-alt2_1jpp1.7
- force build with java4

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:10.1.1.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

