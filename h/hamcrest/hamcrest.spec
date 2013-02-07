# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

# This option controls integration which requires easymock2 and jmock
%bcond_without integration

# This option controls jarjar on qdox
# Since bundling the qdox classes prevents upgrades, we disable it by default
#def_with jarjar
%bcond_with jarjar

# This option controls tests which requires ant-junit and testng
#def_with tests
%bcond_with tests

# If integration is disabled, then tests are disabled
%if %without integration
#def_with tests
%bcond_with tests
%endif

Name:           hamcrest
Version:        1.1
Release:        alt2_21jpp7
Epoch:          0
Summary:        Library of matchers for building test expressions
License:        BSD
URL:            http://code.google.com/p/hamcrest/
Group:          Development/Java
Source0:        http://hamcrest.googlecode.com/files/hamcrest-1.1.tgz
Source1:        http://repo1.maven.org/maven2/org/hamcrest/hamcrest-parent/1.1/hamcrest-parent-1.1.pom
Source2:        http://repo1.maven.org/maven2/org/hamcrest/hamcrest-library/1.1/hamcrest-library-1.1.pom
Source3:        http://repo1.maven.org/maven2/org/hamcrest/hamcrest-integration/1.1/hamcrest-integration-1.1.pom
Source4:        http://repo1.maven.org/maven2/org/hamcrest/hamcrest-generator/1.1/hamcrest-generator-1.1.pom
Source5:        http://repo1.maven.org/maven2/org/hamcrest/hamcrest-core/1.1/hamcrest-core-1.1.pom
Source6:        http://repo1.maven.org/maven2/org/hamcrest/hamcrest-all/1.1/hamcrest-all-1.1.pom
Source7:        hamcrest-text-1.1.pom
Source8:        hamcrest-core-MANIFEST.MF
Source9:        hamcrest-library-MANIFEST.MF
Source10:       hamcrest-text-MANIFEST.MF
Source11:       hamcrest-integration-MANIFEST.MF
Source12:       hamcrest-generator-MANIFEST.MF
Patch0:         hamcrest-1.1-build.patch
Patch1:         hamcrest-1.1-no-jarjar.patch
Patch2:         hamcrest-1.1-no-integration.patch
%if %with integration
Requires:       easymock2
#Requires:       jmock
%endif
Requires:       qdox
BuildRequires:  jpackage-utils >= 0:1.7.4
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  ant-junit
BuildRequires:  zip
BuildRequires:  easymock2
%if %with jarjar
BuildRequires:  jarjar
%endif
BuildRequires:  junit
BuildRequires:  qdox
%if %with tests
BuildRequires:  testng
%endif

BuildArch:      noarch
Source44: import.info

%description
Provides a library of matcher objects (also known as constraints or predicates)
allowing 'match' rules to be defined declaratively, to be used in other
frameworks. Typical scenarios include testing frameworks, mocking libraries and
UI validation rules.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
Javadoc for %%{name}.

%package demo
Group:          Development/Java
Summary:        Demos for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       junit
%if %with tests
Requires:       testng
%endif

%description demo
Demonstrations and samples for %%{name}.

%prep
%setup -q
find . -type f -name "*.jar" | xargs -t rm
rm -fr hamcrest-integration/src/main/java/org/hamcrest/integration/JMock1Adapter.java
rm -fr hamcrest-integration/src/main/java/org/hamcrest/JMock1Matchers.java
rm -fr hamcrest-unit-test/src/main/java/org/hamcrest/integration/JMock1AdapterTest.java
# BUILD/hamcrest-%{version}/lib/generator/jarjar-1.0rc3.jar.no
%if %with jarjar
ln -sf $(build-classpath jarjar) lib/generator/
%endif
# BUILD/hamcrest-1.1/lib/generator/qdox-1.6.1.jar.no
ln -sf $(build-classpath qdox) lib/generator/
# BUILD/hamcrest-1.1/lib/integration/easymock-2.2.jar.no
%if %with integration
ln -sf $(build-classpath easymock2) lib/integration/
%endif
# BUILD/hamcrest-1.1/lib/integration/jmock-1.10RC1.jar.no
%if %with integration
ln -sf $(build-classpath jmock) lib/integration/
%endif
# BUILD/hamcrest-1.1/lib/integration/junit-3.8.1.jar.no
ln -sf $(build-classpath junit) lib/integration/
# BUILD/hamcrest-1.1/lib/integration/testng-4.6-jdk15.jar.no
%if %with tests
ln -sf $(build-classpath testng-jdk15) lib/integration/
%endif
%patch0 -p0
%if %without jarjar
%patch1 -p1
%endif
%if %without integration
#%patch2 -p1
%endif

perl -pi -e 's/\r$//g' LICENSE.txt

%build
export CLASSPATH=$(build-classpath qdox)
export OPT_JAR_LIST="junit ant/ant-junit"
ant -Dant.build.javac.source=1.5 -Dversion=%{version} -Dbuild.sysclasspath=first clean core generator library text bigjar javadoc

# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE8} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/%{name}-core-%{version}.jar META-INF/MANIFEST.MF

rm -fr META-INF
mkdir -p META-INF
cp -p %{SOURCE9} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/%{name}-library-%{version}.jar META-INF/MANIFEST.MF

rm -fr META-INF
mkdir -p META-INF
cp -p %{SOURCE10} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/%{name}-text-%{version}.jar META-INF/MANIFEST.MF

rm -fr META-INF
mkdir -p META-INF
cp -p %{SOURCE11} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/%{name}-integration-%{version}.jar META-INF/MANIFEST.MF

rm -fr META-INF
mkdir -p META-INF
cp -p %{SOURCE12} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/%{name}-generator-%{version}.jar META-INF/MANIFEST.MF

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-parent.pom
%add_maven_depmap JPP.%{name}-parent.pom

install -m 644 build/%{name}-all-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/all.jar
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-all.pom
%add_maven_depmap JPP.%{name}-all.pom %{name}/all.jar

install -m 644 build/%{name}-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core.jar
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-core.pom
%add_maven_depmap JPP.%{name}-core.pom %{name}/core.jar

install -m 644 build/%{name}-generator-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/generator.jar
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-generator.pom
%add_maven_depmap JPP.%{name}-generator.pom %{name}/generator.jar

install -m 644 build/%{name}-library-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/library.jar
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-library.pom
%add_maven_depmap JPP.%{name}-library.pom %{name}/library.jar

%if %with integration
install -m 644 build/%{name}-integration-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/integration.jar
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-integration.pom
%add_maven_depmap JPP.%{name}-integration.pom %{name}/integration.jar
%endif

install -m 644 build/%{name}-text-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/text.jar
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-text.pom
%add_maven_depmap JPP.%{name}-text.pom %{name}/text.jar

%if %with tests
install -m 644 build/%{name}-unit-test-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/unit-test.jar
%endif

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr %{name}-examples $RPM_BUILD_ROOT%{_datadir}/%{name}/

%files
%doc LICENSE.txt
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/all.jar
%{_javadir}/%{name}/core.jar
%{_javadir}/%{name}/generator.jar
%if %with integration
%{_javadir}/%{name}/integration.jar
%endif
%{_javadir}/%{name}/library.jar
%{_javadir}/%{name}/text.jar
%if %with tests
%{_javadir}/%{name}/unit-test.jar
%endif
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%changelog
* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_21jpp7
- fc update

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_19jpp7
- java6 build for jmock2

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_19jpp7
- fc release

* Tue Oct 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_9.2jpp6
- added OSGi manifest for eclipse

* Fri Jan 16 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_8jpp5
- rebuild to fix jmock2

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp5
- converted from JPackage by jppimport script

