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

%define gcj_support 0

%define oname   xmlrpc

Name:           xmlrpc2
Version:        2.0.1
Release:        alt1_6jpp6
Epoch:          0
Summary:        Java XML-RPC implementation
License:        Apache Software License
Group:          Development/Java
Url:            http://ws.apache.org/xmlrpc/
Source0:        http://archive.apache.org/dist/ws/xmlrpc/source/xmlrpc-2.0.1-src.tar.gz
Source1:        xmlrpc-2.0.1.pom
Requires: servlet_2_4_api
Requires: apache-commons-httpclient
Requires: apache-commons-codec >= 1.3
Requires: junit
Provides:       %{oname} = %{epoch}:%{version}-%{release}
Obsoletes:      %{oname} < %{epoch}:%{version}-%{release}
BuildRequires: ant >= 0:1.7.1
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: servlet_2_4_api
BuildRequires: junit
BuildRequires: apache-commons-httpclient
BuildRequires: apache-commons-codec >= 1.3
%if ! %{gcj_support}
Buildarch:      noarch
%endif
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Source44: import.info

%description
Apache XML-RPC is a Java implementation of XML-RPC, a popular protocol
that uses XML over HTTP to implement remote procedure calls.
Apache XML-RPC was previously known as Helma XML-RPC. If you have code
using the Helma library, all you should have to do is change the import
statements in your code from helma.xmlrpc.* to org.apache.xmlrpc.*.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{version}
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%build
export CLASSPATH=%(build-classpath jsse commons-httpclient commons-codec servletapi5 junit 2>/dev/null)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.dir=./bin -Dbuild.dest=./bin -Dsrc.dir=./src -Dfinal.name=%{oname}-%{version} -Djavadoc.destdir=./docs/apidocs -Dhave.deps=true jar
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.dir=./bin -Dbuild.dest=./bin -Dsrc.dir=./src -Dfinal.name=%{oname}-%{version} -Djavadoc.destdir=./docs/apidocs -Dhave.deps=true javadocs

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 bin/%{oname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 bin/%{oname}-%{version}-applet.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-applet-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

%add_to_maven_depmap %{oname} %{oname} %{version} JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt README.txt
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-applet-2.0.1.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_6jpp6
- jpp 6 release

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_5jpp5
- new jpp release

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_4jpp1.7
- converted from JPackage by jppimport script

