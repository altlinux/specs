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

%define bname xmldb
%define cvs_version 20041010


Name:           xmldb-api
Version:        0.1
Release:        alt4_0.20041010.5jpp6
Epoch:          1
Summary:        XML:DB API for Java
License:        BSD
Group:          Development/Java
URL:            http://xmldb-org.sourceforge.net
# cvs -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/xmldb-org login
# cvs -z3 -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/xmldb-org export -D 2004-10-10 xapi
Source0:        xmldb-xapi-%{cvs_version}-src.tar.gz
Source1:        xmldb-api-20041010.pom
Source2:        xmldb-api-sdk-20041010.pom
Source3:        xmldb-common-20041010.pom

Patch0:         xmldb-api-java5-enum.patch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
BuildRequires: junit
BuildRequires: xalan-j2
Requires: jpackage-utils >= 0:1.7.5
Requires: xalan-j2
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info

%description
The API interfaces are what driver developers must implement when creating a
new driver and are the interfaces that applications are developed against. 
Along with the interfaces a concrete DriverManager implementation is also
provides.

%package sdk
Summary:        SDK for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description sdk
The reference implementation provides a very simple file system based
implementation of the XML:DB API. This provides what is basically a very
simple native XML database that uses directories to represent collections and
just stores the XML in files.

The driver development kit provides a set of base classes that can be 
extended to simplify and speed the development of XML:DB API drivers. These
classes are used to provide the basis for the reference implementation and
therefore a simple example of how a driver can be implemented. Using the SDK
classes significantly reduces the amount of code that must be written to
create a new driver.

Along with the SDK base classes the SDK also contains a set of jUnit test
cases that can be used to help validate the driver while it is being
developed. The test cases are still in development but there are enough tests
currently to be useful.

%package -n %{bname}-common
Summary:        Common package for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description -n %{bname}-common
XMLDB common Package, originally Infozone Tools

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n xapi
%patch0 -p1
find . -name "*.jar" | xargs -t rm
# FIXME: (dwalluck): These use org.apache.xalan.xpath 
rm src/common/org/xmldb/common/xml/queries/xalan/XPathQueryImpl.java
rm src/common/org/xmldb/common/xml/queries/xalan/XObjectImpl.java
rm src/common/org/xmldb/common/xml/queries/xalan/XPathQueryFactoryImpl.java
rm src/common/org/xmldb/common/xml/queries/xt/XPathQueryImpl.java
rm src/common/org/xmldb/common/xml/queries/xt/XPathQueryFactoryImpl.java

%build
export CLASSPATH=$(build-classpath junit xalan-j2)
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Djarname=%{name} -Dsdk.jarname=%{name}-sdk dist

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/xmldb/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 dist/xmldb/%{name}-sdk.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-sdk-%{version}.jar
install -m 644 dist/xmldb/%{bname}-common.jar $RPM_BUILD_ROOT%{_javadir}/%{bname}-common-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

# poms
# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap xmldb xmldb-api %{version} JPP %{name}
install -m 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-sdk.pom
%add_to_maven_depmap xmldb xmldb-api-sdk %{version} JPP %{name}-sdk
install -m 644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{bname}-common.pom
%add_to_maven_depmap xmldb xmldb-common %{version} JPP %{bname}-common

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr src/build/javadoc/full/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc src/{AUTHORS,LICENSE,README,config.xml}
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files sdk
%{_javadir}/%{name}-sdk-%{version}.jar
%{_javadir}/%{name}-sdk.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-sdk-%{version}.jar.*
%endif

%files -n %{bname}-common
%{_javadir}/%{bname}-common-%{version}.jar
%{_javadir}/%{bname}-common.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{bname}-common-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 1:0.1-alt4_0.20041010.5jpp6
- jpp 6 release

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 1:0.1-alt4_0.20041010.4jpp5
- use default jpp profile

* Mon Sep 08 2008 Igor Vlasenko <viy@altlinux.ru> 1:0.1-alt3_0.20041010.4jpp5
- converted from JPackage by jppimport script

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 1:0.1-alt2_0.20041010.4jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 1:0.1-alt2.2_0.2.20011111cvs.1jpp5
- rebuild with java 5

