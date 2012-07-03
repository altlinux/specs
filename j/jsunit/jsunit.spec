Patch32: jsunit-1.3-alt-fix-pom-models-maven3.patch
BuildRequires: maven-shared-plugin-tools-api  maven-shared-plugin-tools-beanshell maven-shared-plugin-tools-java maven-shared-plugin-testing-harness maven2-plugin-site
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

Name:           jsunit    
Version:        1.3
Release:        alt4_4jpp6
Epoch:          0
Summary:        Simple framework to write repeatable tests in JavaScript
License:        ASL 2.0
Group:          Development/Java
URL:            http://jsunit.berlios.de/
Source0:        http://download.berlios.de/jsunit/jsunit-1.3.tar.gz
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit >= 0:1.6.5
BuildRequires: ant-trax >= 0:1.6.5
# Scope test
BuildRequires: jmock >= 0:1.1.0
BuildRequires: jpackage-utils
BuildRequires: maven2
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven-release
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-plugin
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch: noarch
%endif
Source44: import.info

%description
JsUnit is a simple framework to write repeatable tests in
JavaScript. It is an instance of the xUnit architecture for unit
testing frameworks. JsUnit is a port of JUnit 3.8.1 originally
written by Erich Gamma and Kent Beck. It covers the core system
and the examples.

%package demo
Summary:        Demo for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description demo
Demo for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%{_bindir}/find -type d -name ".svn" | %{_bindir}/xargs -t %{__rm} -r
%{__chmod} -Rf a+rX,u+w,g-w,o-w .
%patch32

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
%{__mkdir_p} ${MAVEN_REPO_LOCAL}
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -Dmaven.repo.local=${MAVEN_REPO_LOCAL} install javadoc:javadoc

export CLASSPATH=$(build-classpath js):`pwd`/ant/target/jsunit-ant-%{version}.jar:`pwd`/jsunit/target/jsunit-%{version}.jar
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/{junit,trax}`
pushd jsunit/samples
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 
popd

%install

%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p ant/target/jsunit-ant-%{version}.jar %{buildroot}%{_javadir}/%{name}-ant-%{version}.jar
%{__cp} -p jsunit/target/jsunit-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__cp} -p maven2/target/jsunit-maven2-plugin-%{version}.jar %{buildroot}%{_javadir}/%{name}-maven2-plugin-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -a jsunit/docs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# demo
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}/samples/
%{__cp} -pr jsunit/samples/* %{buildroot}%{_datadir}/%{name}/samples/

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
# jsunit-parent
%add_to_maven_depmap de.berlios.jsunit jsunit-parent %{version} JPP %{name}-parent
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
# jsunit
%add_to_maven_depmap de.berlios.jsunit jsunit %{version} JPP %{name}
%{__cp} -p jsunit/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
# jsunit-ant
%add_to_maven_depmap de.berlios.jsunit jsunit-ant %{version} JPP %{name}-ant
%{__cp} -p ant/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-ant.pom
# jsunit-maven2-plugin
%add_to_maven_depmap de.berlios.jsunit jsunit-maven2-plugin %{version} JPP %{name}-maven2-plugin
%{__cp} -p maven2/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-maven2-plugin.pom

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt NOTICE.txt README.txt
%dir %{_datadir}/%{name}
%{_javadir}/jsunit-%{version}.jar
%{_javadir}/jsunit-ant-%{version}.jar
%{_javadir}/jsunit-ant.jar
%{_javadir}/jsunit-maven2-plugin-%{version}.jar
%{_javadir}/jsunit-maven2-plugin.jar
%{_javadir}/jsunit.jar
%{_datadir}/maven2/poms/JPP-jsunit-ant.pom
%{_datadir}/maven2/poms/JPP-jsunit-maven2-plugin.pom
%{_datadir}/maven2/poms/JPP-jsunit-parent.pom
%{_datadir}/maven2/poms/JPP-jsunit.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root,) %{_libdir}/gcj/%{name}/*.jar.*
%endif

%files demo
%dir %{_datadir}/%{name}/samples
%{_datadir}/%{name}/samples/money/
%{_datadir}/%{name}/samples/pom.xml
%{_datadir}/%{name}/samples/build.xml
%{_datadir}/%{name}/samples/demo/
%{_datadir}/%{name}/samples/IE.wsf
%{_datadir}/%{name}/samples/SimpleTest.js
%{_datadir}/%{name}/samples/ArrayTest.js
%{_datadir}/%{name}/samples/IE.js
%attr(0755,root,root) %{_datadir}/%{name}/samples/AllTestsBV
%{_datadir}/%{name}/samples/AllTestsBV.jsp
%attr(0755,root,root) %{_datadir}/%{name}/samples/AllTestsNS
%{_datadir}/%{name}/samples/AllTestsNS.html
%{_datadir}/%{name}/samples/AllTests.html
%{_datadir}/%{name}/samples/AllTests.js
%{_datadir}/%{name}/samples/AllTests.sln
%{_datadir}/%{name}/samples/AllTests.vup
%{_datadir}/%{name}/samples/AllTests.wsf
%{_datadir}/%{name}/samples/AllTests.asp

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt4_4jpp6
- fixed build

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_4jpp6
- added maven2-plugin-resources dep

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_4jpp6
- fixed build

* Thu Oct 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_4jpp6
- new version

