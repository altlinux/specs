%define _without_tests 1
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# Copyright (c) 2000-2012, JPackage Project
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

# If you don't want to run the unit tests
# give rpmbuild option '--without tests'

%define with_tests %{!?_without_tests:1}%{?_without_tests:0}
%define without_tests %{?_without_tests:1}%{!?_without_tests:0}

%define cname         castor

Summary:        An open source data binding framework for Java
Name:           castor0
Version:        0.9.9.1
Release:        alt5_4jpp6
Epoch:          0
Group:          Development/Java
License:        Exolab Software License, BSD-like
URL:            http://castor.codehaus.org/
Source0:        http://dist.codehaus.org/castor/0.9.9.1/castor-0.9.9.1-src.tgz
Source1:        http://repo1.maven.org/maven2/castor/castor/0.9.9.1/castor-0.9.9.1.pom
Patch0:         castor0-ConnectionProxy.patch
Patch1:         castor0-PreparedStatementProxy.patch
Patch2:         castor0-ClobImpl.patch

%if ! %{gcj_support}
BuildArch:      noarch
%endif
Requires:       adaptx
Requires:       cglib
Requires:       apache-commons-logging
#Requires:       jndi
Requires:       jta_1_0_1B_api
Requires:       ldapsdk
Requires:       oro
Requires:       regexp
#Requires:       xerces-j2
BuildRequires:  adaptx
BuildRequires:  ant
BuildRequires:  cglib
BuildRequires:  checkstyle
BuildRequires:  apache-commons-logging
#BuildRequires:  jdbc-stdext
#BuildRequires:  jndi
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  jta_1_0_1B_api
BuildRequires:  ldapsdk
BuildRequires:  log4j
BuildRequires:  oro
BuildRequires:  regexp
#BuildRequires:  xerces-j2
%if %{with_tests}
BuildRequires:  mockejb
BuildRequires:  tyrex
%endif
Provides:  %{cname} = %{epoch}:%{version}-%{release}
Obsoletes: %{cname} < %{epoch}:%{version}-%{release}
%if %{gcj_support}
BuildRequires:     java-gcj-compat-devel
Requires(post):    java-gcj-compat
Requires(postun):  java-gcj-compat
%endif
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Source44: import.info


%description
Castor is an open source data binding framework for Java. It's basically
the shortest path between Java objects, XML documents and SQL tables.
Castor provides Java to XML binding, Java to SQL persistence, and then
some more.

%package test
Group:          Development/Java
Summary:        Tests for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       junit
BuildRequires:  junit

%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description test
Tests for %{name}.

%package xml
Group:          Development/Java
Summary:        XML support for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description xml
XML support for Castor.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package doc
Summary:        Documentation for %{name}
Group:          Development/Documentation

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{cname}-%{version}
find . -name "*.jar" -exec rm -f {} \;
perl -p -i -e 's|org.apache.xerces.utils.regex|org.apache.xerces.impl.xpath.regex|g;' \
src/main/org/exolab/castor/util/XercesRegExpEvaluator.java
find . -name "*.java" -exec perl -p -i -e 's|assert\(|assertTrue\(|g;' {} \;
find . -name "*.java" -exec perl -p -i -e 's|_test.name\(\)|_test.getName\(\)|g;' {} \;

## FIXME: These tests require mockejb, which we don't have yet.
#rm -f src/tests/jdo/JDOJ2EECategory.java
#rm -f src/tests/jdo/TestTransactionManagedEnvironment.java
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2

%build
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java
export CLASSPATH=%(build-classpath \
adaptx \
cglib \
checkstyle \
commons-logging \
jta_1_0_1B_api \
junit \
ldapsdk \
oro \
regexp \
)
#jdbc-stdext \
#jndi \
#xerces-j2 \
%if %{with_tests}
CLASSPATH=$CLASSPATH:$(build-classpath \
mockejb \
tyrex \
)
%endif
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -buildfile src/build.xml jar
%if %{with_tests}
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -buildfile src/build.xml CTFjar
%endif
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -buildfile src/build.xml javadoc

%install

# jar
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -m 644 dist/%{cname}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__install} -m 644 dist/%{cname}-%{version}-xml.jar %{buildroot}%{_javadir}/%{name}-xml-%{version}.jar
%if %{with_tests}
%{__install} -m 644 dist/CTF-%{version}.jar %{buildroot}%{_javadir}/%{name}-tests-%{version}.jar
%endif
pushd %{buildroot}%{_javadir}
   for jar in *-%{version}.jar; do 
      ln -sf ${jar} $(echo $jar| sed  -e "s|-%{version}||g")
   done
popd

# pom and depmap frags
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%add_to_maven_depmap %{cname} %{cname} %{version} JPP %{name}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
%{__install} -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr build/doc/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}

# do this last, since it will delete all build directories
export CLASSPATH=%(build-classpath adaptx log4j)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -buildfile src/build.xml doc

# like magic
%jpackage_script org.exolab.castor.builder.SourceGenerator %{nil} %{nil} xerces-j2:%{name} %{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files
%doc src/etc/{CHANGELOG,LICENSE,README}
%attr(0755,root,root) %{_bindir}/%{name}
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/castor-0.9.9.1.jar.*
%endif
%config(noreplace,missingok) /etc/java/%{name}.conf

%if %{with_tests}
%files test
%{_javadir}/%{name}-tests-%{version}.jar
%{_javadir}/%{name}-tests.jar
%endif

%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/castor-test-0.9.9.1.jar.*
%endif

%files xml
%{_javadir}/%{name}-xml-%{version}.jar
%{_javadir}/%{name}-xml.jar

%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/castor-xml-0.9.9.1.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}

%files doc
%doc build/doc/*

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt5_4jpp6
- built with java 6

* Sat Jan 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt4_4jpp6
- converted from JPackage by jppimport script

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt4_3jpp5
- fixed build

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt3_3jpp5
- selected java5 compiler explicitly

* Tue Oct 07 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt2_3jpp5
- fixed unmet

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt1_3jpp5
- converted from JPackage by jppimport script

