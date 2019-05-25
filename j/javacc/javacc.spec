Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
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

Name:           javacc
Version:        7.0.4
Release:        alt1_2jpp8
Epoch:          0
Summary:        A parser/scanner generator for java
License:        BSD
URL:            http://javacc.org
Source0:        https://github.com/javacc/javacc/archive/%{version}.tar.gz

BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  javacc
# Explicit javapackages-tools requires since scripts use
# /usr/share/java-utils/java-functions
Requires:       javapackages-tools

BuildArch:      noarch
Source44: import.info

%description
Java Compiler Compiler (JavaCC) is the most popular parser generator for use
with Java applications. A parser generator is a tool that reads a grammar
specification and converts it to a Java program that can recognize matches to
the grammar. In addition to the parser generator itself, JavaCC provides other
standard capabilities related to parser generation such as tree building (via
a tool called JJTree included with JavaCC), actions, debugging, etc.

%package manual
Group: Development/Java
Summary:        Manual for %{name}
BuildArch: noarch

%description manual
Manual for %{name}.

%package demo
Group: Development/Java
Summary:        Examples for %{name}
Requires:       %{name} = %{version}-%{release}

%description demo
Examples for %{name}.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

# Remove binary information in the source tar
find . -name "*.jar" -delete
find . -name "*.class" -delete

find ./examples -type f -exec sed -i 's/\r//' {} \;

%build
build-jar-repository -p bootstrap javacc

# There is maven pom which doesn't really work for building. The tests don't
# work either (even when using bundled jars).
ant jar javadoc

# The pom dependencies are also wrong
%mvn_artifact --skip-dependencies pom.xml target/javacc-%{version}.jar

%install
%mvn_file : %{name}

%mvn_install -J target/javadoc

%jpackage_script javacc '' '' javacc javacc true
ln -s %{_bindir}/javacc %{buildroot}%{_bindir}/javacc.sh
%jpackage_script jjdoc '' '' javacc jjdoc true
%jpackage_script jjtree '' '' javacc jjtree true

%files -f .mfiles
%doc --no-dereference LICENSE
%doc README
%{_bindir}/javacc
%{_bindir}/javacc.sh
%{_bindir}/jjdoc
%{_bindir}/jjtree

%files manual
%doc www/*

%files demo
%doc examples

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 0:7.0.4-alt1_2jpp8
- new version

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0:7.0.2-alt1_4jpp8.qa1
- NMU: applied repocop patch

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:7.0.2-alt1_4jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0:7.0.2-alt1_3jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt6_14jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt6_13jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt5jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt4_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt4_8jpp7
- new release

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt4_7jpp7
- applied repocop patches

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt3_7jpp7
- new fc release

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt3_5jpp7
- applied repocop patches

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt2_5jpp7
- added bindir/javacc for the sake of openjpa

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt1_5jpp7
- fc version

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt1_5jpp6
- new jpp relase

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2-alt1_1jpp5.qa1
- NMU (by repocop): the following fixes applied:
  * pkg-contains-cvs-or-svn-control-dir for javacc-manual
  * postclean-05-filetriggers for spec file

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2-alt1_1jpp5
- new jpackage release

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:4.0-alt1_3jpp1.7
- converted from JPackage by jppimport script

* Fri Mar 03 2006 Mikhail Zabaluev <mhz@altlinux.ru> 4.0-alt1
- 4.0
- Use macros from rpm-build-java
- Patch0: set target version for javac

* Tue Sep 09 2003 Mikhail Zabaluev <mhz@altlinux.ru> 3.2-alt1
- Released for ALT Linux
