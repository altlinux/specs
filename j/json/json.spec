%define _unpackaged_files_terminate_build 1
%define _without_javadoc 1

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
Version:	20260814
Release:	alt1
Summary:	JavaScript Object Notation
License:		ALT-Public-Domain
Group:		Development/Java
URL: https://github.com/stleary/JSON-java
VCS: https://github.com/stleary/JSON-java

Source0: json-%version.tar
Patch0: json-test-cycle.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.moditect:moditect-maven-plugin)
BuildRequires: mvn(org.mockito:mockito-core)

BuildArch:	noarch

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

%prep
%setup -q -n json-%version
%patch0 -p1
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%mvn_file org.json:json json

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 20260814-alt1
- New version.

* Thu Oct 01 2026 Anton Meleshnikov <alton@altlinux.org> 0:20080425-alt8
- fixed FTBFS

* Sun Jun 05 2022 Igor Vlasenko <viy@altlinux.org> 0:20080425-alt7_2jpp6
- migrated to %%mvn_artifact

* Fri Jul 02 2021 Igor Vlasenko <viy@altlinux.org> 0:20080425-alt6_2jpp6
- java11 build

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
