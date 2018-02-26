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

%define gcj_support 0



Name:           aelfred
Version:        1.2
Release:        alt1_0.a.9jpp5
Epoch:          0
Summary:        Java-based XML parser
License:        BSD-Style
Url:            http://www.microstar.com/XML/
Source0:        http://card4u.fhnon.de/XMLKlassen/microstar-Parser/aelfred.zip
Source1:        http://repo2.maven.org/maven2/aelfred/aelfred/1.2/aelfred-1.2.pom
Group:          Development/Java
BuildRequires: ant
BuildRequires: jpackage-utils >= 0:1.7.3
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description
AElfred is a new Java-based XML parser from Microstar Software Ltd.
(http://www.microstar.com/), an established provider of XML and SGML
solutions. AElfred is distributed for free (with full source) for both
commercial and non-commercial use, and is designed for easy and
efficient use over the Internet.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Demo for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
Group:          Development/Java

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -c
# remove all binary libs
find . -name "*.jar" -exec %__rm -f {} \;
find . -name "*.class" -exec %__rm -f {} \;
%__rm -rf HTML/*

%build
export JAVA_HOME=%{java_home}
export PATH=%{java_home}/bin:$PATH
export CLASSPATH=
cd src
%javac -source 1.4 `find . -name \*.java`
%javadoc -source 1.4 -d ../HTML `find . -name \*.java`

%install

# jar
export JAVA_HOME=%{java_home}
%__mkdir_p %{buildroot}%{_datadir}/maven2/poms
%__cp -a %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

cd src
%__mkdir_p %{buildroot}%{_javadir}
%jar cvmf /dev/null %{name}.jar -C . com/
%__cp -a %{name}.jar \
%{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%{version}/}; done)

# javadoc
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -a ../HTML/* %{buildroot}%{_javadocdir}/%{name}-%{version}
(cd %{buildroot}%{_javadocdir} && %__ln_s %{name}-%{version} %{name})

# data
%__mkdir_p %{buildroot}%{_datadir}/%{name}/Demo
%__cp -a *.class %{buildroot}%{_datadir}/%{name}/Demo

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%doc README.txt FILES
%{_javadir}/*
%dir %{_datadir}/%{name}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/*
%ghost %dir %{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}/Demo

%changelog
* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_0.a.9jpp5
- new version

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_0.a.8jpp1.7
- converted from JPackage by jppimport script

