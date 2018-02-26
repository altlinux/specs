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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with bootstrap
%bcond_with bootstrap
#def_with gcj_support
%bcond_with gcj_support
%bcond_without repolib

# FIXME: (dwalluck): Requires jpp17 bootstrap for jtidy

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define repodir %{_javadir}/repository.jboss.com/dom4j/1.6.1-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

Name:           dom4j
Version:        1.6.1
Release:	alt4_13jpp6
Epoch:          0
Summary:        DOM4J
License:        BSD
URL:            http://www.dom4j.org/
Group:          Development/Java
Source0:        dom4j-1.6.1.tar.gz
Source1:        dom4j_rundemo.sh
Source2:        dom4j-build.xml
Source3:        http://repo1.maven.org/maven2/dom4j/dom4j/1.6.1/dom4j-1.6.1.pom
Source4:        dom4j-1.6.1-component-info.xml
# http://repository.jboss.com/jboss/dom4j-jarjar/1.6.1/build/build.xml
Source5:        dom4j-jarjar-build.xml
Source6:        dom4j-jarjar-component-info.xml
Patch0:         dom4j-1.6.1-build_xml.patch
Patch1:         dom4j-1.6.1-bug1618750.patch
Patch2:         dom4j-1.6.1-endorsed-dir.patch
Patch3:         dom4j-jdk6.patch
BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: jarjar
BuildRequires: ant >= 0:1.6.5
BuildRequires: junit
BuildRequires: ant-junit
BuildRequires: ant-trax
BuildRequires: ant-apache-resolver
BuildRequires: jtidy
BuildRequires: junitperf
BuildRequires: isorelax
#BuildRequires: jaxen-bootstrap >= 0:1.1-0.b7
%if %with bootstrap
BuildRequires: jaxen-bootstrap >= 0:1.1-1
%else
BuildRequires: jaxen >= 0:1.1-2
%endif
BuildRequires: msv
BuildRequires: relaxngDatatype
BuildRequires: stax_1_0_api
BuildRequires: ws-jaxme
BuildRequires: xalan-j2 >= 0:2.7
BuildRequires: xerces-j2
BuildRequires: jaxp = 1.2
BuildRequires: xpp2
BuildRequires: xpp3
BuildRequires: msv-xsdlib
Requires: xpp2
Requires: xpp3
Requires: xerces-j2
Requires: msv
Requires: msv-xsdlib
Requires: relaxngDatatype
Requires: isorelax
%if %with bootstrap
Requires: jaxen-bootstrap >= 0:1.1-1
%else
Requires: jaxen >= 0:1.1-1
%endif
Requires: stax_1_0_api
Requires: ws-jaxme
Requires: xalan-j2
Requires: jaxp = 1.2
Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
dom4j is an Open Source XML framework for Java. dom4j allows you to read,
write, navigate, create and modify XML documents. dom4j integrates with 
DOM and SAX and is seamlessly integrated with full XPath support. 

Note: To use the msv JARV factory (com.sun.msv.verifier.jarv.TheFactoryImpl)
make sure isorelax.jar (from the 'isorelax' RPM) is in the ClassPath.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.

%package jarjar
Summary:        JarJar of %{name} for JBoss
Group:          Development/Java

%description jarjar
A jarjard version of dom4j that moves the classes to the
org.jboss.dom4j package space and strips the following packages:

   org.dom4j.jaxb.*
   org.dom4j.swing.*
   org.dom4j.xpath.*
   org.dom4j.xpp.*

%package jarjar-repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description jarjar-repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package demo
Summary:        Samples for %{name}
Group:          Development/Documentation
Requires: dom4j = %{epoch}:%{version}-%{release}

%description demo
Samples for %{name}.

%package manual
Summary:        Manual for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
# replace run.sh
cp %{SOURCE1} run.sh
cp %{SOURCE2} build.xml
# remove binary libs
find . -name "*.jar" -exec rm -f {} \;
#for j in $(find . -name "*.jar"); do 
#    mv $j $j.no
#done
# function matrix-concat not available
rm -f src/test/org/dom4j/xpath/MatrixConcatTest.java
# won't succeed in headless environment
rm src/test/org/dom4j/bean/BeansTest.java
# FIXME Bug in Xalan 2.6 -- reactivate with Xalan 2.7
#rm src/test/org/dom4j/XPathExamplesTest.java
# fix for deleted jars
mv build.xml build.xml.orig
sed -e '/unjar/d' -e 's|,cookbook/\*\*,|,|' build.xml.orig > build.xml
# FIXME: (yyang): failed in JDK6
rm -f src/test/org/dom4j/ThreadingTest.java
# FIXME: (yyang): failed in JDK6, maybe failed to load russArticle.xml because it's russian encoding
rm -f src/test/org/dom4j/io/StaxTest.java

%patch0 -p0 -b .sav
%patch1 -p1
%if 0
%patch2 -p1
%endif
%patch3 -p1

perl -pi -e 's/\r//g' LICENSE.txt docs/clover/*.css docs/style/*.css docs/xref/*.css docs/xref-test/*.css src/doc/style/*.css docs/benchmarks/xpath/*.java

# jarjar
cp -p %{SOURCE5} dom4j-jarjar-build.xml

pushd lib
ln -sf $(build-classpath xpp2)
ln -sf $(build-classpath relaxngDatatype)
pushd endorsed
ln -sf $(build-classpath jaxp12) 
popd
ln -sf $(build-classpath jaxme/jaxmeapi) 
ln -sf $(build-classpath msv-xsdlib) 
ln -sf $(build-classpath msv-msv) 
ln -sf $(build-classpath jaxen) 
ln -sf $(build-classpath stax_1_0_api) 
pushd test
ln -sf $(build-classpath junitperf) 
ln -sf $(build-classpath junit) 
popd
ln -sf $(build-classpath xpp3) 
pushd tools
ln -sf $(build-classpath jaxme/jaxmexs) 
ln -sf $(build-classpath xalan-j2) 
ln -sf $(build-classpath xalan-j2-serializer) 
ln -sf $(build-classpath jaxme/jaxmejs) 
ln -sf $(build-classpath jtidy) 
ln -sf $(build-classpath isorelax) 
ln -sf $(build-classpath jaxme/jaxme2) 
ln -sf $(build-classpath xerces-j2) 
popd
popd

%build
export CLASSPATH=
export OPT_JAR_LIST="junit ant/ant-junit"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 all samples 
# manually dropped test
#test

# jarjar
cp -p build/dom4j.jar dom4j-1.6.1.jar
export CLASSPATH=$(build-classpath jarjar)
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f dom4j-jarjar-build.xml
rm dom4j-1.6.1.jar

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

cp -p build/dom4j.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
# jarjar
cp -p output/dom4j-jarjar.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-jarjar-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap dom4j dom4j %{version} JPP %{name}

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -rf docs/apidocs
cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/classes/org/dom4j
cp -pr xml $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/src
cp -pr src/samples $RPM_BUILD_ROOT%{_datadir}/%{name}/src
cp -pr build/classes/org/dom4j/samples $RPM_BUILD_ROOT%{_datadir}/%{name}/classes/org/dom4j
install -m 0755 run.sh $RPM_BUILD_ROOT%{_datadir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i "s/@VERSION@/%{version}-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{SOURCE2} $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH2} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH3} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/dom4j.jar
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom $RPM_BUILD_ROOT%{repodirlib}/dom4j.pom
# jarjar
%define repodir %{_javadir}/repository.jboss.com/jboss/dom4j-jarjar/1.6.1-brew
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i "s/@VERSION@/%{version}-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH2} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH3} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-jarjar-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/dom4j-jarjar.jar
%endif

%files
%doc LICENSE.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files jarjar
%{_javadir}/%{name}-jarjar.jar
%{_javadir}/%{name}-jarjar-%{version}.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%files demo
%{_datadir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}
%dir %{_javadir}/repository.jboss.com
%{_javadir}/repository.jboss.com/dom4j

%files jarjar-repolib
%dir %{_javadir}
%dir %{_javadir}/repository.jboss.com
%{_javadir}/repository.jboss.com/jboss
%endif

%changelog
* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt4_13jpp6
- switched to jpp due to repolib and fixed build

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt3_7jpp7
- fc version

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_13jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_10jpp5
- use default jpp profile

* Wed Sep 10 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_8jpp5
- converted from JPackage by jppimport script

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_8jpp5
- converted from JPackage by jppimport script

* Sun May 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_4jpp1.7
- converted from JPackage by jppimport script

* Mon Apr 25 2005 Vladimir Lettiev <crux@altlinux.ru> 1.6-alt1
- Initial release for ALT Linux Sisyphus

