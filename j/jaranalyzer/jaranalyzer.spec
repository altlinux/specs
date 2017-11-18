BuildRequires: javapackages-local
Packager: Igor Vlasenko <viy@altlinux.ru>
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


Summary:        Dependency Management Utility
Name:           jaranalyzer
Version:        1.1
Release:	alt6_2jpp6
Epoch:          0
License:        BSD-style
URL:            http://www.kirkk.com/main/Main/JarAnalyzer
Group:          Development/Java
Source0:        http://www.kirkk.com/main/zip/JarAnalyzer-src-1.1.zip
Source1:        jaranalyzer-1.1.script
Source2:        jaranalyzer-1.1.pom
Patch0:         jaranalyzer-1.1-build_xml.patch
BuildRequires: jpackage-utils
BuildRequires: ant 
BuildRequires: ant-junit
BuildRequires: bcel
BuildRequires: regexp

Requires: bcel
Requires: regexp
%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4

%description
JarAnalyzer is a dependency management utility for jar files. 
It's primary purpose is to traverse through a directory, parse 
each of the jar files in that directory, and identify the 
dependencies between the jar files. The output is an xml file 
representing the PhysicalDependencies between the jar files.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c -n %{name}-%{version}
# remove all binary libs
for j in $(find lib -name "*.jar"); do
    mv $j $j.no
done

%patch0 -b .sav

%build
pushd lib
ln -sf $(build-classpath regexp) jakarta-regexp-1.3.jar
ln -sf $(build-classpath bcel) bcel-5.1.jar
popd

ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 

%install

install -d -m 0755 $RPM_BUILD_ROOT%{_bindir}
install -m 0755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/runxmlsummary

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}

install -m 0644 bin/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

# pom and depmap frags
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files -f .mfiles
%doc bin/license.txt
%attr(755,root,root) %{_bindir}/runxmlsummary
%{_javadir}/*.jar
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt6_2jpp6
- added BR: javapackages-local for javapackages 5

* Sun Feb 14 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt5_2jpp6
- build with java8

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt4_2jpp5
- use junit 4

* Fri Mar 29 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_2jpp5
- explicitly use junit3

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_1jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp5
- converted from JPackage by jppimport script

