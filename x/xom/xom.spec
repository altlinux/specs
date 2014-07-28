# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: dom4j
BuildRequires: /proc
BuildRequires: jpackage-compat
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

# To build with dom4j issue rpmbuild --with dom4j xom.spec

%define with_dom4j %{?_with_dom4j:1}%{!?_with_dom4j:0}
%define without_dom4j %{!?_with_dom4j:1}%{?_with_dom4j:0}

Summary:        XML Pull Parser
Name:           xom
Version:        1.0
Release:        alt1_12jpp7
Epoch:          1
License:        LGPLv2
URL:            http://www.xom.nu
Group:          Development/Java
Source0:        http://www.cafeconleche.org/XOM/xom-1.0.tar.gz
Source1:        http://central.maven.org/maven2/xom/xom/1.0/xom-1.0.pom

# Evidently gjdoc doesn't know about the noqualifier option; also, it
# must do linkoffline and not link
Patch0:         %{name}-gjdocissues.patch
# FIXME:  file this
# I don't know if this is a libgcj bug or if this is a legitimate typo
# in build.xml
Patch1:         %{name}-betterdocclasspath.patch
# Replace icu4j by java.text from JDK to reduce dependency chain
Patch2:         %{name}-Replace-icu4j-with-JDK.patch

BuildRequires:  ant >= 0:1.6 jpackage-utils >= 0:1.6
BuildRequires:  junit
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
%if %{with_dom4j}
BuildRequires:  dom4j
%endif
BuildRequires:  xml-commons-apis

BuildRequires:  tagsoup
# Use JAXP implementation in libgcj
BuildRequires:  libgcj
BuildRequires:  xml-commons-resolver
BuildRequires:  servlet

Requires:  xalan-j2
Requires:  xerces-j2
Requires:  xml-commons-apis
Requires:  jpackage-utils
BuildArch: noarch
Source44: import.info

%description
XOM is a new XML object model. It is an open source (LGPL),
tree-based API for processing XML with Java that strives
for correctness, simplicity, and performance, in that order.
XOM is designed to be easy to learn and easy to use. It
works very straight-forwardly, and has a very shallow
learning curve. Assuming you're already familiar with XML,
you should be able to get up and running with XOM very quickly.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%package demo
Summary:        Samples for %{name}
Group:          Development/Java
Requires:       %{name} = 0:%{version}

%description demo
%{summary}.

%prep
%setup -q -n XOM
%patch0
%patch1
%patch2 -p1
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
# disable tests that require icu4j
rm -f src/nu/xom/tests/{Encoding,Verifier}Test.java

cp %{SOURCE1} pom.xml
# fix xml stuff in pom
sed -i 's%<project>%<project xmlns="http://maven.apache.org/POM/4.0.0" \
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" \
xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 \
http://maven.apache.org/maven-v4_0_0.xsd ">%' pom.xml
# remove it from pom.xml since it's not needed anymore
%pom_remove_dep com.ibm.icu:icu4j


%build
pushd lib
ln -sf $(build-classpath junit) junit.jar
ln -sf $(build-classpath xerces-j2) xercesImpl.jar
ln -sf $(build-classpath xalan-j2) xalan.jar
ln -sf $(build-classpath xml-commons-apis) xmlParserAPIs.jar
popd
mkdir lib2
pushd lib2
ln -sf $(build-classpath tagsoup) tagsoup-1.0rc1.jar
ln -sf $(build-classpath xml-commons-resolver) resolver.jar

%if %{with_dom4j}
ln -sf $(build-classpath dom4j) dom4j.jar
%endif

ln -sf $(build-classpath servlet) servlet.jar
popd

ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 jar samples betterdoc

# Fix encoding
sed -i 's/\r//g' LICENSE.txt
pushd apidocs
for f in `find -name \*.css -o -name \*.html`; do
  sed -i 's/\r//g' $f
done
popd

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 build/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -m 644 build/xom-samples.jar $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc overview.html
%doc README.txt
%doc LICENSE.txt
%doc Todo.txt
%doc lgpl.txt
%doc %{name}.graffle
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/*

%files demo
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/xom-samples.jar

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_12jpp7
- new release

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_9jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.6-alt1_2jpp6
- new jpp relase

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_1jpp5
- new version

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_0.b2.4jpp5
- jpp5 build

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_6jpp1.7
- updated to new jpackage release

* Sat Dec 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_5jpp1.7
fixes jvm 5.0 poisoning

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_5jpp1.7
- full-fledged build

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_5jpp1.7
- imported with jppimport script; note: bootstrapped version

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_4jpp1.7
- imported with jppimport script; note: bootstrapped version

