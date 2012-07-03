Packager: Igor Vlasenko <viy@altlinux.ru>
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

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/com/sun/xml/stream/buffer/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define gcj_support 0


Name:           sun-xmlstreambuffer
Version:        0.7
Release:        alt1_4jpp6
Epoch:          0
Summary:        XML Stream Buffer
License:        CDDL
Group:          Development/Java
URL:            https://xmlstreambuffer.dev.java.net/
Source0:        sun-xmlstreambuffer-%{version}.tar.gz
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs login
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -r HEAD -d sun-xmlstreambuffer-0.7 xmlstreambuffer/streambuffer
Source1:        streambuffer-%{version}.pom
Source2:        CDDLv1.0.html
Source3:        sun-xmlstreambuffer-component-info.xml
Patch0:         sun-xmlstreambuffer-build-impl.patch
Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4
Requires: jaf_1_1_api
Requires: stax_1_0_api
Requires: stax-ex
BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: jaf_1_1_api
BuildRequires: stax_1_0_api
BuildRequires: stax-ex
BuildRequires: wstx
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
A stream buffer is a stream-based representation of an XML 
infoset in Java. Stream buffers are designed to: provide 
very efficient stream-based memory representations of XML 
infosets; and be created and processed using any Java-based 
XML API.

Conceptually a stream buffer is similar to the representation
used in the Xerces deferred DOM implementation, with the crucial
difference that a stream buffer does not store hierarchal
information like parent and sibling information. The deferred
DOM implementation reduces memory usage when large XML documents
are parsed but only a subset of the document needs to be processed.
(Note that using deferred DOM will be more expensive than
non-deferred DOM in terms of memory and processing if all
the document is traversed.)

Stream buffers may be used as an efficient alternative to DOM where:

* most or all of an XML infoset will eventually get traversed; and/or

* targeted access to certain parts of an XML infoset are required 
  and need to be efficiently processed using stream-based APIs like
  SAX or StAX.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q 
find . -name "*.jar" | xargs -t rm
%patch0 -p0

install -pm 644 %{SOURCE2} CDDLv1.0.html

ln -sf $(build-classpath jaf_1_1_api) lib/activation.jar
ln -sf $(build-classpath stax_1_0_api) lib/jsr173_api.jar
ln -sf $(build-classpath stax-ex) lib/stax-ex.jar
ln -sf $(build-classpath junit) lib/junit.jar
ln -sf $(build-classpath wstx/wstx-asl) lib/

%build
export CLASSPATH=
export OPT_JAR_LIST="`%{__cat} %{_sysconfdir}/ant.d/junit`"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 
%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/streambuffer.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && ln -s %{name}-%{version}.jar %{name}.jar)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap com.sun.xml.stream.buffer streambuffer %{version} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %with repolib
%{__install} -d -m 755 %{buildroot}%{repodir}
%{__install} -d -m 755 %{buildroot}%{repodirlib}
%{__install} -p -m 644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 755 %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE2} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/streambuffer.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc CDDLv1.0.html
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_4jpp6
- added repolib

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_3jpp5
- fixed repocop warnings

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_1jpp5
- converted from JPackage by jppimport script

