BuildRequires: javapackages-local
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
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


Name:		json
Summary:	JavaScript Object Notation
Url:		http://www.json.org/java/index.html
Version:	20080425
Release:	alt5_2jpp6
Epoch:		0
License:	Open Source
Group:		Development/Java
BuildArch:	noarch
Source0:	http://www.json.org/java/json.zip
Source1:	json-20080425.pom
BuildRequires:  jpackage-utils
Source44: import.info


%description
JSON (JavaScript Object Notation) is a lightweight data-
interchange format. It is easy for humans to read and write.
It is easy for machines to parse and generate. It is based
on a subset of the JavaScript Programming Language, Standard
ECMA-262 3rd Edition - December 1999. JSON is a text format
that is completely language independent but uses conventions
that are familiar to programmers of the C-family of languages,
including C, C++, C#, Java, JavaScript, Perl, Python, and
many others. These properties make JSON an ideal
data-interchange language.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -c -n %{name}-%{version}
chmod -R go=u-w *
mkdir src
mv org src

%build
mkdir -p target/classes
%{_jvmdir}/java/bin/javac  -target 1.6 -source 1.6 -d target/classes $(find src -name "*.java")
%{_jvmdir}/java/bin/jar cf target/%{name}.jar -C target/classes org
#mkdir -p target/site/apidocs
#%{_jvmdir}/java/bin/javadoc -d target/site/apidocs $(find src -name "*.java")

%install
%define installname %{name}-%{version}
%define installname %{name}

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{installname}.jar

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-json.pom
%add_maven_depmap -v %{version} JPP-json.pom %{installname}.jar

# javadoc
#install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
#cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
#ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files -f .mfiles
%{_javadir}/*

#%files javadoc
#%doc %{_javadocdir}/%{name}-%{version}
#%doc %{_javadocdir}/%{name}

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:20080425-alt5_2jpp6
- added BR: javapackages-local for javapackages 5

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:20080425-alt4_2jpp6
- build as compat

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:20080425-alt3_2jpp6
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:20080425-alt2_2jpp6
- new jpp relase

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:20080425-alt2_1jpp5
- fixes for java6 support

* Fri Feb 13 2009 Igor Vlasenko <viy@altlinux.ru> 0:20080425-alt1_1jpp5
- new version

