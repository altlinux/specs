BuildRequires: geronimo-jta-1.0.1B-api
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: jakarta-commons-logging
BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define gcj_support 0


Summary:        An open source data binding framework for Java
Name:           castor
Version:        1.1.2.1
Release:	alt3_4jpp5
Epoch:          0
Group:          Development/Java
License:        Exolab Software License, BSD-like
URL:            http://castor.codehaus.org/
Source0:        castor-1.1.2.1.tar.gz
# svn export http://svn.codehaus.org/castor/castor/tags/1.1.2.1/ castor-1.1.2.1

Source1:        castor-jpp-depmap.xml
Source2:        castor-1.1.2.1.pom
Source3:        castor-anttasks-1.1.2.1.pom
Source4:        castor-codegen-1.1.2.1.pom
Source5:        castor-ddlgen-1.1.2.1.pom
Patch0:         castor-1.1.2.1-pom.patch
Patch1:         castor-cpactf-build.patch
Patch2:         castor-1.1.2.1-CastorCodeGenTask.patch
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Requires: cglib
Requires: jdbc-stdext
Requires: jndi
Requires: jta_api
Requires: ldapsdk
Requires: log4j
Requires: oro
Requires: regexp
Requires: xerces-j2
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-trax
BuildRequires: cglib
BuildRequires: jakarta-commons-logging
BuildRequires: jdbc-stdext
BuildRequires: jndi
BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: jta_1_0_1B_api
BuildRequires: junit
BuildRequires: ldapsdk
BuildRequires: log4j
BuildRequires: mockejb
BuildRequires: oro
BuildRequires: regexp
BuildRequires: tyrex
BuildRequires: xalan-j2
BuildRequires: xerces-j2

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4

%description
Castor is an open source data binding framework for Java. It's basically
the shortest path between Java objects, XML documents and SQL tables.
Castor provides Java to XML binding, Java to SQL persistence, and then
some more.

%package test
Group:          Development/Java
Summary:        Tests for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: junit
BuildRequires: junit
%if %{gcj_support}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description test
Tests for %{name}.

%package xml
Group:          Development/Java
Summary:        XML support for %{name}.
Requires: %{name} = %{epoch}:%{version}-%{release}
%if %{gcj_support}
Requires(post): java-gcj-compat
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
%setup -q
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
mkdir -p bin/lib

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2

pushd lib
ln -sf $(build-classpath cglib-nodep) cglib-full-2.0.2.jar
ln -sf $(build-classpath commons-logging) commons-logging-1.1.jar
ln -sf $(build-classpath oro)
ln -sf $(build-classpath regexp)
ln -sf $(build-classpath jta_1_0_1B_api) jta1.0.1.jar
#BUILD/castor-1.1.2.1/lib/jtf-0.1.jar.no
ln -sf $(build-classpath junit) junit_3.8.2.jar
ln -sf $(build-classpath ldapsdk) ldapjdk_4.1.jar
ln -sf $(build-classpath log4j) log4j-1.2.13.jar
pushd tests
ln -sf $(build-classpath mockejb)
ln -sf $(build-classpath tyrex) tyrex-1.0.jar
popd
ln -sf $(build-classpath xerces-j2)
ln -sf $(build-classpath xalan-j2)
ln -sf $(build-classpath xalan-j2-serializer)
popd


%build

export CLASSPATH=$(build-classpath xalan-j2 xalan-j2-serializer)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -buildfile src/build.xml jar.all CTFjar

%install

# jar
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -m 644 dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__install} -m 644 dist/%{name}-%{version}-commons.jar %{buildroot}%{_javadir}/%{name}-commons-%{version}.jar
%{__install} -m 644 dist/%{name}-%{version}-xml.jar %{buildroot}%{_javadir}/%{name}-xml-%{version}.jar
%{__install} -m 644 dist/%{name}-%{version}-codegen.jar %{buildroot}%{_javadir}/%{name}-codegen-%{version}.jar
%{__install} -m 644 dist/%{name}-%{version}-ddlgen.jar %{buildroot}%{_javadir}/%{name}-ddlgen-%{version}.jar
%{__install} -m 644 dist/%{name}-%{version}-xmlctf.jar %{buildroot}%{_javadir}/%{name}-xmlctf-%{version}.jar
%{__install} -m 644 dist/%{name}-%{version}-anttasks.jar %{buildroot}%{_javadir}/%{name}-anttasks-%{version}.jar
%{__install} -m 644 dist/CTF-%{version}.jar %{buildroot}%{_javadir}/%{name}-tests-%{version}.jar

pushd %{buildroot}%{_javadir}
   for jar in *-%{version}.jar; do 
      ln -sf ${jar} $(echo $jar| sed  -e "s|-%{version}||g")
   done
popd

# pom and depmap frags
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%add_to_maven_depmap org.codehaus.castor %{name} %{version} JPP %{name}
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.codehaus.castor %{name}-anttasks %{version} JPP %{name}-anttasks
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-anttasks.pom
%add_to_maven_depmap org.codehaus.castor %{name}-codegen %{version} JPP %{name}-codegen
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-codegen.pom
%add_to_maven_depmap org.codehaus.castor %{name}-ddlgen %{version} JPP %{name}-ddlgen
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-ddlgen.pom

# javadoc
%{__install} -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr build/doc/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}

# do this last, since it will delete all build directories
export CLASSPATH=%(build-classpath xalan-j2 xalan-j2-serializer)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -buildfile src/build.xml doc

# like magic
%jpackage_script org.exolab.castor.builder.SourceGenerator %{nil} %{nil} xerces-j2:%{name} %{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%post javadoc
%{__rm} -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%files
%doc src/doc/*.txt
%attr(0755,root,root) %{_bindir}/%{name}
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-anttasks-%{version}.jar
%{_javadir}/%{name}-anttasks.jar
%{_javadir}/%{name}-commons-%{version}.jar
%{_javadir}/%{name}-commons.jar
%{_javadir}/%{name}-codegen-%{version}.jar
%{_javadir}/%{name}-codegen.jar
%{_javadir}/%{name}-ddlgen-%{version}.jar
%{_javadir}/%{name}-ddlgen.jar
%{_datadir}/maven2
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%{_libdir}/gcj/%{name}/%{name}-anttasks-%{version}.jar.*
%{_libdir}/gcj/%{name}/%{name}-commons-%{version}.jar.*
%{_libdir}/gcj/%{name}/%{name}-codegen-%{version}.jar.*
%{_libdir}/gcj/%{name}/%{name}-ddlgen-%{version}.jar.*
%endif
%config(noreplace,missingok) /etc/java/%{name}.conf

%files test
%{_javadir}/%{name}-tests-%{version}.jar
%{_javadir}/%{name}-tests.jar
%{_javadir}/%{name}-xmlctf-%{version}.jar
%{_javadir}/%{name}-xmlctf.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-test-%{version}.jar.*
%endif

%files xml
%{_javadir}/%{name}-xml-%{version}.jar
%{_javadir}/%{name}-xml.jar

%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-xml-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}

%files doc
%doc build/doc/*

%changelog
* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2.1-alt3_4jpp5
- fixed build

* Tue May 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2.1-alt2_4jpp5
- fixes for java6 support

* Tue Feb 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2.1-alt1_4jpp5
- new version

* Tue Nov 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt1_2jpp5
- fixed build

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

