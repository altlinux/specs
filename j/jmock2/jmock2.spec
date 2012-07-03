BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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

%define gcj_support 0

%define oname   jmock

Name:           jmock2
Version:        2.5.1
Release:        alt2_1jpp6
Epoch:          0
Summary:        Test Java code using mock objects

Group:          Development/Java
License:        Open Source
URL:            http://jmock.codehaus.org/
Source0:        jmock-2.5.1.tgz
# svn export http://svn.codehaus.org/jmock/tags/2.5.1/ jmock-2.5.1

Source1:        http://repo1.maven.org/maven2/org/jmock/jmock/2.5.1/jmock-2.5.1.pom
Source2:        http://repo1.maven.org/maven2/org/jmock/jmock-junit3/2.5.1/jmock-junit3-2.5.1.pom
Source3:        http://repo1.maven.org/maven2/org/jmock/jmock-junit4/2.5.1/jmock-junit4-2.5.1.pom
Source4:        http://repo1.maven.org/maven2/org/jmock/jmock-legacy/2.5.1/jmock-legacy-2.5.1.pom
Source5:        http://repo1.maven.org/maven2/org/jmock/jmock-parent/2.5.1/jmock-parent-2.5.1.pom
Source6:        http://repo1.maven.org/maven2/org/jmock/jmock-script/2.5.1/jmock-script-2.5.1.pom
Patch0:         jmock2-DeterministicScheduler.patch


%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-junit
BuildRequires:  junit >= 0:3.8.1
BuildRequires:  junit44
BuildRequires:  bsh2
BuildRequires:  cglib21 >= 0:2.1.3
BuildRequires:  hamcrest
BuildRequires:  objenesis
Requires:  bsh2
Requires:  cglib21 >= 0:2.1.3
Requires:  hamcrest
Requires:  objenesis
Requires:  junit >= 0:3.8.1
Requires:  junit44
%if %{gcj_support}
BuildRequires:    gnu-crypto
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Source44: import.info

%description
jMock is a library that supports test-driven development
of Java2 code with mock objects.
Mock objects help you design and test the interactions 
between the objects in your programs.
The jMock library:
* makes it quick and easy to define mock objects, so you 
  don't break the rhythm of programming.
* lets you precisely specify the interactions between your 
  objects, reducing the brittleness of your tests.
* works well with the autocompletion and refactoring 
  features of your IDE
* plugs into your favourite test framework
* is easy to extend.


%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{oname}-%{version}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .sav0
pushd lib
ln -sf $(build-classpath bsh2/bsh) bsh-core-2.0b4.jar
ln -sf $(build-classpath cglib21-nodep) cglib-nodep-2.1_3.jar
ln -sf $(build-classpath hamcrest/core) hamcrest-core-1.1.jar
ln -sf $(build-classpath hamcrest/library) hamcrest-library-1.1.jar
ln -sf $(build-classpath junit) junit-3.8.1.jar
ln -sf $(build-classpath junit44) junit-4.4.jar
ln -sf $(build-classpath objenesis) objenesis-1.0.jar
popd

%build

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dversion=%{version}

%install

install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 build/%{oname}-%{version}/%{oname}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-%{version}.jar
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom
%add_to_maven_depmap org.jmock jmock %{version} JPP/%{name} %{name}

install -m 644 build/%{oname}-%{version}/%{oname}-junit3-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-junit3-%{version}.jar
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-junit3.pom
%add_to_maven_depmap org.jmock jmock-junit3 %{version} JPP/%{name} %{name}-junit3

install -m 644 build/%{oname}-%{version}/%{oname}-junit4-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-junit4-%{version}.jar
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-junit4.pom
%add_to_maven_depmap org.jmock jmock-junit4 %{version} JPP/%{name} %{name}-junit4

install -m 644 build/%{oname}-%{version}/%{oname}-legacy-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-legacy-%{version}.jar
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-legacy.pom
%add_to_maven_depmap org.jmock jmock-legacy %{version} JPP/%{name} %{name}-legacy

install -m 644 build/%{oname}-%{version}/%{oname}-tests-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-tests-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-parent.pom
%add_to_maven_depmap org.jmock jmock-parent %{version} JPP/%{name} %{name}-parent

#
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/%{oname}-%{version}/doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt
%{_javadir}/%{name}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}*%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt2_1jpp6
- built with java 6

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_1jpp6
- new jpp relase

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt3_1jpp5
- fixed build; use cglib21

* Sun Jan 18 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt2_1jpp5
- fixed build

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_1jpp5
- converted from JPackage by jppimport script

