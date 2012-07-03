Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
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

%define base_name cactus

%define with_tests %{!?_with_tests:0}%{?_with_tests:1}
%define without_tests %{!?_with_tests:1}%{?_with_tests:0}

Summary:        Cactus unit test framework for server-side java code 
Name:           jakarta-%{base_name}
Version:        1.7.2
Release:        alt5_4jpp5
Epoch:          0
License:        Apache Software License
URL:            http://jakarta.apache.org/cactus/
Group:          Development/Java
Source0:        %{name}-src-%{version}.zip
Source1:        cactus-missing-testinput.tar.gz
Source2:        pom-maven2jpp-depcat.xsl
Source3:        pom-maven2jpp-newdepmap.xsl
Source4:        pom-maven2jpp-mapdeps.xsl
Source5:        jakarta-cactus-1.7.2-jpp-depmap.xml
Source6:        cactus-1.7.2.pom
Source7:        cactus-ant-1.7.2.pom
Source8:        cactus-maven-1.7.2.pom


Patch1:         jakarta-cactus-src-1.7.2-framework-build_xml.patch
Patch2:         jakarta-cactus-src-1.7.2-integration-ant-build_xml.patch
Patch3:         jakarta-cactus-src-1.7.1-samples-servlet-build_xml.patch
#171## patch from cargo-0.5 to cargo-0.9
Patch4:         jakarta-cactus-src-1.7.2-CactifyWarTask.patch
Patch5:         jakarta-cactus-src-1.7.2-WebXmlMergeTask.patch
Patch6:         jakarta-cactus-src-1.7.2-CactifyEarTask.patch
Patch7:         jakarta-cactus-src-1.7.2-TestCactifyEarTask.patch
Patch8:         jakarta-cactus-src-1.7.2-TestCactifyWarTask.patch
#171## patches for maven plugin
Patch9:         jakarta-cactus-src-1.7.2-maven-plugin-project_xml.patch
Patch10:        jakarta-cactus-src-1.7.2-maven-plugin-project_properties.patch
Patch11:        jakarta-cactus-src-1.7.2-project_properties.patch
Patch12:        jakarta-cactus-1.7.2-notest.patch

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: maven1 >= 0:1.1
BuildRequires: maven1-plugins-base
BuildRequires: maven1-plugin-license
BuildRequires: maven1-plugin-test
BuildRequires: saxon-scripts
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit >= 0:1.6
BuildRequires: ant-nodeps >= 0:1.6
BuildRequires: ant-trax >= 0:1.6
BuildRequires: junit
BuildRequires: antlr
BuildRequires: aspectj
BuildRequires: cargo0 >= 0:0.9
BuildRequires: checkstyle4
BuildRequires: httpunit
BuildRequires: tomcat5-jasper
BuildRequires: jetty5
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-httpclient
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-taglibs-standard
BuildRequires: log4j
BuildRequires: mockobjects
BuildRequires: nekohtml
BuildRequires: regexp
BuildRequires: rhino
BuildRequires: servlet_2_3_api
BuildRequires: geronimo-j2ee-1.4-apis
BuildRequires: geronimo-jsp-2.0-api
BuildRequires: geronimo-servlet-2.4-api
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis
Requires: ant
Requires: aspectj
Requires: cargo0
Requires: httpunit
Requires: jasper5
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-codec
Requires: jakarta-commons-collections
Requires: jakarta-commons-httpclient
Requires: jakarta-commons-logging
Requires: jakarta-taglibs-standard
Requires: log4j
Requires: mockobjects
Requires: nekohtml
Requires: regexp
Requires: servletapi4
Requires: geronimo-j2ee-1.4-apis
Requires: geronimo-jsp-2.0-api
Requires: geronimo-servlet-2.4-api
#Requires:  xerces-j2
#Requires:  xml-commons-apis
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

BuildArch:      noarch


%description
Cactus is a simple test framework for unit testing 
server-side java code (Servlets, EJBs, Tag Libs, 
Filters, ...). The intent of Cactus is to lower the 
cost of writing tests for server-side code. It uses 
JUnit and extends it. Cactus implements an 
in-container strategy 

%package maven-plugin
Summary:        Cactus Maven Plugin
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: rhino

%description maven-plugin
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
Javadoc for %{name}.

%package manual
Summary:        Docs for %{name}
Group:          Development/Documentation

%description manual
Docs for %{name}.

%prep
%setup -q -n %{name}-src-%{version}
gzip -dc %{SOURCE1} | tar -xf -
chmod -R go=u-w *
cp -pr samples/servlet/src/java/j2ee13 samples/servlet/src/java/j2ee14
cp -pr samples/servlet/src/test-cactus/j2ee13 samples/servlet/src/test-cactus/j2ee14
cp -pr samples/servlet/src/scripts/j2ee13 samples/servlet/src/scripts/j2ee14
cp -pr samples/servlet/src/webapp/j2ee13 samples/servlet/src/webapp/j2ee14
cp -pr samples/ejb/src/scripts/j2ee13 samples/ejb/src/scripts/j2ee14
cp -pr samples/ejb/src/webapp/j2ee13 samples/ejb/src/webapp/j2ee14
cp -pr samples/ejb/src/application/j2ee13 samples/ejb/src/application/j2ee14

%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5
%patch6 -b .sav6
%patch7 -b .sav7
%patch8 -b .sav8
%patch9 -b .sav9
%patch10 -b .sav10
%patch11 -b .sav11
%if %{without_tests}
%patch12 -b .notest
%endif

%build
mkdir default
cp default-project.xml default/project.xml

mkdir -p .maven/repository/servletapi/jars/
ln -sf $(build-classpath servlet_2_3_api) \
           .maven/repository/servletapi/jars/servletapi-2.3.jar

export DEPCAT=$(pwd)/jakarta-cactus-1.7.2-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE2} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE3} > jakarta-cactus-1.7.2-depmap.new.xml

for p in $(find . -name "*project.xml"); do
    pushd $(dirname $p)
    b=$(basename $p)
    cp ${b} ${b}.orig
    /usr/bin/saxon -o ${b} ${b}.orig %{SOURCE4} map=%{SOURCE5}
    popd
done

echo antlr.jar=$(build-classpath antlr) >> build.properties
echo aspectjrt.jar=$(build-classpath aspectjrt) >> build.properties
echo aspectj-tools.jar=$(build-classpath aspectjtools) >> build.properties
echo cargo.jar = $(build-classpath cargo0/cargo0-core-uberjar) >> build.properties
echo checkstyle.jar=$(build-classpath checkstyle4) >> build.properties
echo commons.beanutils.jar=$(build-classpath commons-beanutils) >> build.properties
echo commons.collections.jar=$(build-classpath commons-collections) >> build.properties
echo commons.httpclient.jar=$(build-classpath commons-httpclient) >> build.properties
echo commons.logging.jar=$(build-classpath commons-logging) >> build.properties
echo httpunit.jar=$(build-classpath httpunit) >> build.properties
echo j2ee.13.jar=$(build-classpath geronimo-j2ee-1.4-apis) >> build.properties
echo j2ee.14.jar=$(build-classpath geronimo-j2ee-1.4-apis) >> build.properties
echo jasper-compiler.jar=$(build-classpath jasper5-compiler) >> build.properties
echo jasper-runtime.jar=$(build-classpath jasper5-runtime) >> build.properties
echo jetty.jar=$(build-classpath jetty5/jetty5) >> build.properties
echo js.jar=$(build-classpath js) >> build.properties
echo jstl.jar=$(build-classpath taglibs-core) >> build.properties
echo junit.jar=$(build-classpath junit) >> build.properties
echo log4j.jar=$(build-classpath log4j) >> build.properties
echo mockobjects.jar=$(build-classpath mockobjects-core) >> build.properties
echo nekohtml.jar=$(build-classpath nekohtml) >> build.properties
echo regexp.jar=$(build-classpath regexp) >> build.properties
#echo servlet.22.jar=$(build-classpath servletapi3) >> build.properties
echo servlet.23.jar=$(build-classpath servlet_2_3_api) >> build.properties
echo servlet.24.jar=$(build-classpath geronimo-servlet-2.4-api) >> build.properties
echo jsp.20.jar=$(build-classpath jspapi) >> build.properties
echo standard.jar=$(build-classpath jakarta-taglibs-standard) >> build.properties
echo xerces.jar=$(build-classpath xerces-j2) >> build.properties
echo xmlapis.jar=$(build-classpath xml-commons-jaxp-1.3-apis) >> build.properties
echo cactus.port=9992 >> build.properties


export OPT_JAR_LIST="ant/ant-nodeps ant/ant-junit junit ant/ant-trax xalan-j2 xalan-j2-serializer aspectjtools"
export CLASSPATH=$(build-classpath commons-codec)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
        -Drepo.url=file://usr/share/java/ \
        -Dbuild.sysclasspath=first \
        dist

export MAVEN_HOME_LOCAL=$(pwd)/.maven
pushd integration/maven
maven -e \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.home.local=$MAVEN_HOME_LOCAL \
        plugin:install-now
popd

%install

# jars

install -dm 755 $RPM_BUILD_ROOT%{_javadir}/cactus-14
cp -p framework/dist-14/lib/cactus-%{version}.jar \
         $RPM_BUILD_ROOT%{_javadir}/cactus-14/jakarta-cactus-%{version}.jar
cp -p integration/ant/dist-14/lib/cactus-ant-%{version}.jar \
         $RPM_BUILD_ROOT%{_javadir}/cactus-14/jakarta-cactus-ant-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/cactus-14 && for jar in %{name}*-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|jakarta-||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/cactus-14 && for jar in %{base_name}*-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
%add_to_maven_depmap cactus cactus %{version} JPP/cactus-14 cactus
%add_to_maven_depmap cactus cactus-ant %{version} JPP/cactus-14 cactus-ant
%add_to_maven_depmap cactus cactus-maven %{version} JPP/maven/plugins maven-cactus-plugin

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cactus-14-cactus.pom
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cactus-14-cactus-ant.pom
install -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.maven.plugins-maven-cactus-plugin.pom

# plugin
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven/plugins
install -m 644 integration/maven/target/%{base_name}-maven-%{version}.jar \
 $RPM_BUILD_ROOT%{_datadir}/maven/plugins/maven-%{base_name}-plugin-%{version}.jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/maven-plugins
pushd $RPM_BUILD_ROOT%{_javadir}/maven-plugins
ln -sf \
 %{_datadir}/maven/plugins/maven-%{base_name}-plugin-%{version}.jar \
 maven-%{base_name}-plugin.jar
popd

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr framework/web/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr framework/dist-14/doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp documentation/licenses/apache-2.0.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -rf documentation/dist/doc/api
cp -pr documentation/dist/doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%doc %{_docdir}/%{name}-%{version}/apache-2.0.txt
%{_datadir}/%{name}-%{version}
%{_javadir}/cactus-14
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files maven-plugin
%doc %{_docdir}/%{name}-%{version}/apache-2.0.txt
%{_datadir}/maven/plugins/maven-%{base_name}-plugin*.jar
%{_javadir}/maven-plugins/maven-%{base_name}-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt5_4jpp5
- fixed build with moved maven1

* Mon Aug 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt4_4jpp5
- maven1 dependency translaton

* Sun Jan 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt3_4jpp5
- adapted pom for new aspectj

* Thu Nov 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt2_4jpp5
- build with cargo0

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt1_4jpp5
- new jpp release

* Tue Nov 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt1_3jpp5
- java 5 build

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt1_3jpp1.7
- updated to new jpackage release

* Sat Nov 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt1_2jpp1.7
- converted from JPackage by jppimport script

