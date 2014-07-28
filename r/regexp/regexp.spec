# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
Obsoletes: jakarta-regexp = 1.4-alt1
Obsoletes: jakarta-regexp = 1.4-alt2
Obsoletes: jakarta-regexp = 1.4-alt3
Obsoletes: jakarta-regexp = 1.4-alt4
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name regexp
%define version 1.5
# Copyright (c) 2000-2005, JPackage Project
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

%global full_name       jakarta-%{name}

Name:           regexp
Version:        1.5
Release:        alt1_10jpp7
Epoch:          0
Summary:        Simple regular expressions API
License:        ASL 2.0
Group:          Development/Java
Url:            http://jakarta.apache.org/%{name}/
Source0:        http://www.apache.org/dist/jakarta/regexp/jakarta-regexp-%{version}.tar.gz
Source1:        http://repo.maven.apache.org/maven2/%{full_name}/%{full_name}/1.4/%{full_name}-1.4.pom
BuildRequires:  jpackage-utils >= 0:1.6

BuildRequires:  ant >= 1.6
BuildArch:      noarch
Source44: import.info
Provides: jakarta-regexp = %{version}-%{release}

%description
Regexp is a 100% Pure Java Regular Expression package that was
graciously donated to the Apache Software Foundation by Jonathan Locke.
He originally wrote this software back in 1996 and it has stood up quite
well to the test of time.
It includes complete Javadoc documentation as well as a simple Applet
for visual debugging and testing suite for compatibility.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{full_name}-%{version}
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%build
mkdir lib
ant -Djakarta-site2.dir=. jar javadocs


%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 build/*.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
cp -r docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}

install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap -a regexp:regexp

%files
%doc LICENSE
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_10jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_9jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_2jpp6
- new jpp relase

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_1jpp5
- new version

* Sun Oct 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_3jpp1.7
- resurrected from misplaced in obsolete

* Wed Jun 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_3jpp1.7
- converted from JPackage by jppimport script

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_3jpp1.7
- converted from JPackage by jppimport script

