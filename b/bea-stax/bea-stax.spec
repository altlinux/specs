# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
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


Summary:        Streaming API for XML
URL:            http://dev2dev.bea.com/technologies/stax/index.jsp
Source0:        stax-src-1.2.0_rc1-dev.zip
Source1:        http://repository.jboss.org/maven2/stax/stax/1.2.0/stax-1.2.0.pom
Name:           bea-stax
Version:        1.2.0
Release:        alt2_0.rc1.4jpp6
Epoch:          0
License:        Apache Software License 2
Group:          Development/Java
BuildArch:      noarch

BuildRequires:  jpackage-utils >= 0:5.0.0
BuildRequires:  ant >= 0:1.7
Requires:       jpackage-utils >= 0:5.0.0
Requires:	%{name}-api = %{epoch}:%{version}-%{release}
Source44: import.info
Obsoletes: stax-bea <= 1.0-alt1


%description
The Streaming API for XML (StAX) is a groundbreaking 
new Java API for parsing and writing XML easily and 
efficiently. 

%package api
Summary:        The StAX API.
Group:          Development/Documentation
%description api
%{summary}

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}

%prep
%setup -q -c -n %{name}-%{version}

%build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 all javadoc

%install

# jar
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 0644 build/stax-api-1.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-api-%{version}.jar
install -p -m 0644 build/stax-1.2.0_rc1-dev.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-ri-%{version}.jar
ln -s %{name}-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-api.jar
ln -s %{name}-ri-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-ri.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-bea-stax-ri.pom
%add_to_maven_depmap stax stax %{version} JPP bea-stax-ri

%files
%{_javadir}/%{name}-ri-%{version}.jar
%{_javadir}/%{name}-ri.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files api
%{_javadir}/%{name}-api-%{version}.jar
%{_javadir}/%{name}-api.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}


%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt2_0.rc1.4jpp6
- new jpp relase

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt2_0.rc1.3jpp5
- new jpackage release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_0.rc1.3jpp5
- converted from JPackage by jppimport script

* Fri Apr 27 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_0.rc1.2jpp1.7
- converted from JPackage by jppimport script

