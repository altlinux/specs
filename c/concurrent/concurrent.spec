# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# Copyright (c) 2000-2007, JPackage Project
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

Name:           concurrent
Version:        1.3.4
Release:        alt1_21jpp8
Epoch:          0
Summary:        Utility classes for concurrent Java programming
License:        Public Domain
Source0:        http://gee.cs.oswego.edu/dl/classes/EDU/oswego/cs/dl/current/concurrent.tar.gz
# Source1 not used, kept for reference
Source1:        %{name}-%{version}.build.xml
Source2:        %{name}-%{version}.pom
Patch0:         concurrent-build.patch
Patch1:         JDK-8-support.patch
URL:            http://gee.cs.oswego.edu/dl/classes/EDU/oswego/cs/dl/util/concurrent/intro.html
Group:          Development/Java

BuildArch:      noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  ant
BuildRequires:  javapackages-local

Requires: javapackages-tools rpm-build-java
Source44: import.info

%description 
This package provides standardized, efficient versions of utility classes
commonly encountered in concurrent Java programming. This code consists of
implementations of ideas that have been around for ages, and is merely intended
to save you the trouble of coding them.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -c -q
mkdir -p src/EDU/oswego/cs/dl/util
mv concurrent src/EDU/oswego/cs/dl/util
# Build with debug on
pushd src/EDU/oswego/cs/dl/util/concurrent
%patch0
%patch1 -p1
popd
sed -i -e 's/..\/sun-u.c.license.pdf/http:\/\/gee.cs.oswego.edu\/dl\/classes\/EDU\/oswego\/cs\/dl\/util\/sun-u.c.license.pdf/' src/EDU/oswego/cs/dl/util/concurrent/intro.html

%build
pushd src/EDU/oswego/cs/dl/util/concurrent

ant \
  -Dversion=%{version} \
  -Dj2se.apiurl=%{_javadocdir}/java \
  dist javadoc

popd

%install
# JAR
%mvn_artifact %{SOURCE2} src/EDU/oswego/cs/dl/util/concurrent/lib/concurrent.jar

# JAVADOCS
%mvn_install -J src/EDU/oswego/cs/dl/util/concurrent/docs/

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc src/EDU/oswego/cs/dl/util/concurrent/intro.html

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt1_21jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt1_20jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt1_17jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt1_16jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt1_15jpp7
- fc update

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt1_10jpp6
- new jpp release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt1_9jpp5
- new jpackage release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt1_8jpp5
- converted from JPackage by jppimport script

* Wed Jun 13 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt1_7jpp1.7
- updated to new jpackage release

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt1_6jpp1.7
- converted from JPackage by jppimport script

