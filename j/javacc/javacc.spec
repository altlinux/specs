Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
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
Version:        5.0
Release:        alt6_14jpp8
Epoch:          0
Summary:        A parser/scanner generator for java
License:        BSD
Source0:        http://java.net/projects/%{name}/downloads/download/%{name}-%{version}src.tar.gz
Source1:        javacc.sh
Source2:        jjdoc
Source3:        jjtree
Patch0:         0001-Add-javadoc-target-to-build.xml.patch
URL:            http://javacc.java.net/
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  junit
BuildRequires:  javacc

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
Requires:       %{name} = %{version}

%description demo
Examples for %{name}.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}

%patch0 -p1

# Remove binary information in the source tar
find . -name "*.jar" -delete
find . -name "*.class" -delete

find ./examples -type f -exec sed -i 's/\r//' {} \;

ln -s `build-classpath javacc` bootstrap/javacc.jar

sed -i 's/source="1.4"/source="1.5"/g' src/org/javacc/{parser,jjdoc,jjtree}/build.xml

%build
# Use the bootstrap javacc.jar to generate some required
# source java files. After these source files are generated we
# remove the bootstrap jar and build the binary from source.
ant -f src/org/javacc/parser/build.xml parser-files
ant -f src/org/javacc/jjtree/build.xml tree-files
find . -name "*.jar" -delete
ant jar javadoc

%install
# jar
install -Dpm 644 bin/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# bin
install -Dp -T -m 755 %{SOURCE1} %{buildroot}/%{_bindir}/javacc.sh
install -Dp -T -m 755 %{SOURCE2} %{buildroot}/%{_bindir}/jjdoc
install -Dp -T -m 755 %{SOURCE3} %{buildroot}/%{_bindir}/jjtree

# javadoc
install -d -p 755 %{buildroot}/%{_javadocdir}/%{name}
cp -rp api/* %{buildroot}/%{_javadocdir}/%{name}

# pom
install -Dpm 644 pom.xml %{buildroot}/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar
ln -s javacc.sh %buildroot%_bindir/%name


%files -f .mfiles
%{_javadir}/*.jar
%doc LICENSE README
%{_bindir}/*
%_bindir/%name

%files manual
%doc LICENSE README
%doc www/*

%files demo
%doc examples

%files javadoc
%doc LICENSE README
%{_javadocdir}/%{name}

%changelog
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
