BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
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

#def_with gcj_support
%bcond_with gcj_support

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           hivemind
Version:        1.1.1
Release:        alt1_4jpp6
Epoch:          0
Summary:        HiveMind Microkernel
Group:          Development/Java
License:        ASL 2.0
URL:            http://hivemind.apache.org/
Source0:        hivemind-1.1.1.tar.gz
Source1:        http://repo1.maven.org/maven2/hivemind/hivemind/1.1.1/hivemind-1.1.1.pom
Source2:        http://repo1.maven.org/maven2/hivemind/hivemind-lib/1.1.1/hivemind-lib-1.1.1.pom
Source3:        http://repo1.maven.org/maven2/hivemind/hivemind-jmx/1.1.1/hivemind-jmx-1.1.1.pom
Patch0:         hivemind-hivebuild-properties.patch
Patch1:         hivemind-framework-build.patch
Patch2:         hivemind-hivebuild-module.patch
Patch3:         hivemind-hivebuild-module-properties.patch
Patch4:         hivemind-library-build.patch
Patch5:         hivemind-jmx-build.patch
Patch6:         hivemind-jmx-TestMBeanRegistry.patch
Patch7:         hivemind-examples-build.patch
Patch8:         hivemind-examples-TestTaskExecutor.patch
Patch9:         hivemind-junit-no-fail.patch
Requires:       easymock
Requires:       easymock-classextension
Requires:       apache-commons-logging
Requires:       jakarta-oro
Requires:       javassist
Requires:       junit
Requires:       log4j
Requires:       servlet_2_3_api
#Requires:       xml-commons-jaxp-1.3-apis
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-junit
BuildRequires:  ant-trax
BuildRequires:  aopalliance
BuildRequires:  cglib
BuildRequires:  easymock
BuildRequires:  easymock-classextension
BuildRequires:  geronimo-ejb-2.1-api
BuildRequires:  groovy15
BuildRequires:  apache-commons-logging
BuildRequires:  jakarta-oro
BuildRequires:  javassist
BuildRequires:  junit
BuildRequires:  log4j
BuildRequires:  mx4j
BuildRequires:  servletapi4
BuildRequires:  spring-all
#BuildRequires:  xerces-j2
#BuildRequires:  xml-commons-jaxp-1.3-apis
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
HiveMind is an services and configuration microkernel. Its 
features are also referred to as Inversion of Control (IoC) 
Container or Lightweight Container. The adoption of HiveMind 
in an application ensures the use of certain design principles 
which improve encapsulation, modularization, testability and 
reusability. 

%package lib
Summary:        Library extensions for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       aopalliance
Requires:       ejb
Requires:       groovy15
Requires:       spring-all

%description lib
%{summary}.

%package jmx
Summary:        JMX extensions for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       mx4j

%description jmx
%{summary}.

%package demo
Summary:        Examples for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       ejb

%description demo
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
%{_bindir}/find -type f -name "*.jar" -a -type f \( ! -name empty.jar -a ! -name module.jar -a ! -name TestRegistryBuilder.jar \) | %{_bindir}/xargs -t %{__rm}
%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav
%patch4 -b .sav
%patch5 -b .sav
%patch6 -b .sav
%patch7 -b .sav
%patch8 -b .sav
%patch9 -b .sav
mkdir -p repository/JPP/jars
pushd repository/JPP/jars
ln -s $(build-classpath ant) ant-.jar
ln -s $(build-classpath commons-logging) commons-logging-.jar
ln -s $(build-classpath javassist) javassist-.jar
ln -s $(build-classpath servlet_2_3_api) servletapi-.jar
ln -s $(build-classpath oro) oro-.jar
ln -s $(build-classpath log4j) log4j-.jar
ln -s $(build-classpath easymock) easymock-.jar
ln -s $(build-classpath easymock-classextension) easymockclassextension-.jar
ln -s $(build-classpath cglib-nodep) cglib-full-.jar
ln -s $(build-classpath junit) junit-.jar
ln -s $(build-classpath xerces-j2) xercesImpl-.jar
ln -s $(build-classpath geronimo-ejb-2.1-api) geronimo-ejb-2.1-api-.jar
ln -s $(build-classpath spring) spring-full-.jar
ln -s $(build-classpath groovy15) groovy-jsr-all-.jar
ln -s $(build-classpath aopalliance) aopalliance-.jar
ln -s $(build-classpath mx4j/mx4j) mx4j-.jar
ln -s $(build-classpath mx4j/mx4j-tools) mx4j-tools-.jar
ln -s $(build-classpath mx4j/mx4j-remote) mx4j-remote-.jar
popd

mkdir tmp
mkdir -p ext-package/lib
touch ext-package/download-warning-marker
ln -s $(build-classpath xml-commons-jaxp-1.3-apis) ext-package/lib/xml-apis-.jar

%build
export CLASSPATH=$(build-classpath antlr groovy15 asm2)
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/{junit,trax}`
export RD=$(pwd)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first -Dscratch.dir=${RD}/tmp -Droot.dir=${RD} install run-reports
pushd framework
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first -Dscratch.dir=${RD}/tmp -Droot.dir=${RD} javadoc
popd
pushd library
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first -Dscratch.dir=${RD}/tmp -Droot.dir=${RD} javadoc
popd
pushd jmx
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first -Dscratch.dir=${RD}/tmp -Droot.dir=${RD} javadoc
popd

%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{name}-jmx-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{name}-lib-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
install -m 644 examples/target/%{name}-examples-%{version}.jar \
                                                  $RPM_BUILD_ROOT%{_javadir}
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-hivemind.pom
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-hivemind-lib.pom
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-hivemind-jmx.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
%add_to_maven_depmap %{name} %{name}-lib %{version} JPP %{name}-lib
%add_to_maven_depmap %{name} %{name}-jmx %{version} JPP %{name}-jmx

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/framework
cp -pr tmp/jakarta-hivemind/target/docs/hivemind/apidocs/* \
                $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/framework
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jmx
cp -pr tmp/jakarta-hivemind/target/docs/hivemind-jmx/apidocs/* \
                $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jmx
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/library
cp -pr tmp/jakarta-hivemind/target/docs/hivemind-lib/apidocs/* \
                $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/library
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files jmx
%{_javadir}/%{name}-jmx-%{version}.jar
%{_javadir}/%{name}-jmx.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-jmx-%{version}.jar.*
%endif

%files lib
%{_javadir}/%{name}-lib-%{version}.jar
%{_javadir}/%{name}-lib.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-lib-%{version}.jar.*
%endif

%files demo
%{_javadir}/%{name}-examples-%{version}.jar
%{_javadir}/%{name}-examples.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-examples-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_4jpp6
- new jpp relase

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_3jpp5
- new jpp release

* Tue Nov 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_2jpp5
- fixed build w/java5

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

