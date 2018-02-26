# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define _without_maven 1
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
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

#def_with gcj_support
%bcond_with gcj_support
#def_with maven
%bcond_with maven

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           xstream
Version:        1.3.1
Release:        alt1_4jpp6
Epoch:          0
Summary:        XML serialization library
Group:          Development/Java
License:        BSD-Style
URL:            http://xstream.codehaus.org/
Source0:        http://repository.codehaus.org/com/thoughtworks/xstream/xstream-distribution/1.3.1/xstream-distribution-1.3.1-src.zip
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Patch0:         xstream-build_xml.patch
Patch1:         xstream-pom_xml.patch
Patch2:         xstream-xstream-pom_xml.patch
Patch3:         xstream-xstream-distribution-pom_xml.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       cglib
Requires:       dom4j
Requires:       jakarta-commons-lang
Requires:       jakarta-oro
Requires:       jdom
Requires:       jettison
Requires:       joda-time
Requires:       jpackage-utils
Requires:       stax_1_0_api
Requires:       wstx
Requires:       xom
Requires:       xpp3
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  ant-junit
# XXX: ant 1.8.x
BuildRequires:  ant-nodeps
BuildRequires:  ant-trax
# should really be java-fonts, but openjdk provides java-fonts without any font files!
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  junit >= 0:3.8.1
%if %with maven
BuildRequires:  maven2 >= 0:2.0.7
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-dependency
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-source
BuildRequires:  maven-release
BuildRequires:  maven-surefire-plugin
BuildRequires:  jakarta-slide-webdavclient
BuildRequires:  xsite
%endif
BuildRequires:  bea-stax
BuildRequires:  cglib >= 0:2.1.3
BuildRequires:  dom4j >= 0:1.6.1
BuildRequires:  jakarta-commons-lang >= 0:2.1
BuildRequires:  jakarta-oro >= 0:2.0.8
BuildRequires:  jdom >= 0:1.0
BuildRequires:  jettison >= 0:1.0
BuildRequires:  jmock >= 0:1.0.1
BuildRequires:  joda-time >= 0:1.2.1
BuildRequires:  stax_1_0_api
BuildRequires:  wstx >= 0:3.1.1
BuildRequires:  xalan-j2 >= 0:2.7.0
BuildRequires:  xom >= 0:1.0
BuildRequires:  xpp3 >= 0:1.1.3.4
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
XStream is a simple library to serialize objects to XML 
and back again. A high level facade is supplied that 
simplifies common use cases. Custom objects can be serialized 
without need for specifying mappings. Speed and low memory 
footprint are a crucial part of the design, making it suitable 
for large object graphs or systems with high message throughput. 
No information is duplicated that can be obtained via reflection. 
This results in XML that is easier to read for humans and more 
compact than native Java serialization. XStream serializes internal 
fields, including private and final. Supports non-public and inner 
classes. Classes are not required to have default constructor. 
Duplicate references encountered in the object-model will be 
maintained. Supports circular references. By implementing an 
interface, XStream can serialize directly to/from any tree 
structure (not just XML). Strategies can be registered allowing 
customization of how particular types are represented as XML. 
When an exception occurs due to malformed XML, detailed diagnostics 
are provided to help isolate and fix the problem.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if %with maven
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.
%endif

%prep
%setup -q
%if %with maven
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
cp -p %{SOURCE1} settings.xml
%endif
find . -name "*.jar" | xargs -t rm

# This test requires megginson's sax2
rm xstream/src/test/com/thoughtworks/xstream/io/xml/SaxWriterTest.java
# These sources are for Java5
# Keep them now
#rm -r xstream/src/java/com/thoughtworks/xstream/annotations/
#rm -r xstream/src/test/com/thoughtworks/acceptance/annotations/

mkdir -p xstream-distribution/target/xsite

perl -pi -e 's/\r$//g' LICENSE.txt

%if %with maven
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP
%else
pushd xstream/lib
# cglib-nodep-2.1_3.jar.no
ln -s $(build-classpath cglib-nodep)
# commons-lang-2.1.jar.no
ln -s $(build-classpath commons-lang)
# dom4j-1.6.1.jar.no
ln -s $(build-classpath dom4j)
# jdom-1.0.jar.no
ln -s $(build-classpath jdom)
# jettison-1.0-RC1.jar.no
ln -s $(build-classpath jettison)
# jmock-1.0.1.jar.no
ln -s $(build-classpath jmock)
# joda-time-1.2.1.jar.no
ln -s $(build-classpath joda-time)
# junit-3.8.1.jar.no
ln -s $(build-classpath junit)
# oro-2.0.8.jar.no
ln -s $(build-classpath oro)
# stax-1.2.0.jar.no
ln -s $(build-classpath bea-stax-ri)
# stax-api-1.0.1.jar.no
ln -s $(build-classpath stax_1_0_api)
# wstx-asl-3.2.0.jar.no
ln -s $(build-classpath wstx/wstx-asl)
# xml-writer-0.2.jar.no

#xom-1.1.jar.no
ln -s $(build-classpath xom)
# xpp3_min-1.1.3.4.O.jar.no
ln -s $(build-classpath xpp3)
popd
%endif

%build
%if %with maven
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        -Dmaven2.jpp.mode=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc
%else
export CLASSPATH=$(build-classpath jaxen)
export OPT_JAR_LIST="`cat %{_sysconfdir}/ant.d/{junit,nodeps,trax}`"
pushd xstream
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first -Dversion=%{version} library javadoc
popd
%endif

%install

install -Dpm 644 xstream/target/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%if %with maven
install -Dpm 644 xstream-benchmark/target/%{name}-benchmark-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-benchmark-%{version}.jar
%else
install -Dpm 644 xstream/target/%{name}-benchmark-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-benchmark-%{version}.jar
%endif

%add_to_maven_depmap com.thoughtworks.xstream xstream %{version} JPP %{name}
%add_to_maven_depmap com.thoughtworks.xstream xstream-benchmark %{version} JPP %{name}-benchmark
%add_to_maven_depmap com.thoughtworks.xstream xstream-parent %{version} JPP %{name}-parent

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -s ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
install -pm 644 xstream/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
install -pm 644 xstream-benchmark/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-benchmark.pom

#
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core
%if %with maven
cp -pr xstream/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core
%else
cp -pr xstream/target/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core
%endif
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/benchmark
%if %with maven
cp -pr xstream-benchmark/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/benchmark
%else
cp -pr xstream/target/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/benchmark
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
%if %with maven
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/xsite
rm -rf xstream-distribution/target/xsite/javadoc 
cp -pr xstream-distribution/target/xsite/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/xsite
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/xstream-benchmark-%{version}.jar
%{_javadir}/xstream-benchmark.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_datadir}/maven2/poms/JPP-%{name}-benchmark.pom
%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-*%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with maven
%files manual
%doc %{_docdir}/%{name}-%{version}
%endif

%changelog
* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_4jpp6
- new jpp relase

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_1jpp5
- new version

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_2jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt1_3jpp5
- converted from JPackage by jppimport script

* Thu Nov 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt1_1jpp1.7
- updated to new jpackage release

* Tue Jul 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_1jpp1.7
- converted from JPackage by jppimport script

