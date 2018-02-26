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


Name:		gif89encoder
Version:	0.90
Release:	alt1_0.b.3jpp5
Epoch:		0
Summary:	Java class library for encoding GIF's
License:	BSD
URL:		http://jmge.net/java/gifenc/
Group:		Development/Java
Source0:	http://jmge.net/java/gifenc/Gif89Encoder090b.zip
Source1:	gif89encoder-0.90b.pom
Requires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

%if ! %{gcj_support}
BuildArch:      noarch
%endif

%description
This Java class library for encoding GIF's is likely to be of 
utility to many other programmers. It covers more of the extended 
GIF89a feature set, including animation and embedded textual 
comments, than any other free Java GIF encoder.

%package	javadoc
Summary:	Javadoc for %{name}
Group:		Development/Documentation

%description	javadoc
Javadoc for %{name}.

%prep
%setup -q -c
%__rm -f lib/classes.jar

%build
%__mkdir_p build/lib
%__mkdir_p build/javadocs

pushd src

%javac `find . -name "*.java"`
%jar cfm ../build/lib/%{name}.jar /dev/null `find . -name "*.class"`
%javadoc -d ../build/javadocs `find . -name "*.java"`

popd

%install
%__rm -rf %{buildroot}

# jars
%__mkdir_p %{buildroot}%{_javadir}
%__install -p -m 644 build/lib/%{name}.jar \
%{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%{version}/}; done)
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -a build/javadocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
(cd %{buildroot}%{_javadocdir} && %__ln_s %{name}-%{version} %{name})

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc readme.txt
%{_javadir}/%{name}.jar
%{_javadir}//%{name}-%{version}.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif


%files javadoc
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/*
%{_javadocdir}/%{name}

%changelog
* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.90-alt1_0.b.3jpp5
- new jpp release

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.90-alt1_0.b.2jpp1.7
- converted from JPackage by jppimport script

