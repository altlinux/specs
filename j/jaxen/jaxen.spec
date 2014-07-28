# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
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

Name:           jaxen
Version:        1.1.3
Release:        alt3_9jpp7
Epoch:          0
Summary:        An XPath engine written in Java
License:        BSD
URL:            http://jaxen.codehaus.org/
Group:          Development/Java
Source0:        http://dist.codehaus.org/jaxen/distributions/jaxen-%{version}-src.tar.gz
Source1:        build.xml
Source2:        http://repo1.maven.org/maven2/%{name}/%{name}/%{version}/%{name}-%{version}.pom
Requires:       dom4j >= 0:1.6.1
Requires:       jdom >= 0:1.0-0.rc1.1jpp
Requires:       xalan-j2
Requires:       xerces-j2
BuildRequires:  ant >= 0:1.6 jpackage-utils >= 0:1.6 junit ant-junit
BuildRequires:  dom4j >= 0:1.6.1
BuildRequires:  jdom >= 0:1.0-0.rc1.1jpp
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
Provides:       jaxen-bootstrap <= %{version}-%{release}
Obsoletes:      jaxen-bootstrap <= %{version}-%{release}
BuildArch:      noarch
Source44: import.info

%description
Jaxen is an XPath engine written in Java to work against a variety of XML
based object models such as DOM, dom4j and JDOM together with Java
Beans.

%package demo
Summary:        Samples for %{name}
Group:          Development/Documentation
Requires:       jaxen = 0:%{version}-%{release}

%description demo
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
find . -name "*.jar" -exec rm -f {} \;
cp %{SOURCE1} .
cp %{SOURCE2} pom.xml
mkdir -p target/lib
pushd target/lib
build-jar-repository . dom4j-1.6.1.jar jdom-1.0.jar 
ln -s %{_javadir}/xerces-j2.jar xercesImpl-2.6.2.jar
popd
rm -rf src/java/main/org/jaxen/xom
rm src/java/test/org/jaxen/test/XOM*.java
%pom_remove_dep xom:xom
%pom_remove_dep :maven-cobertura-plugin
%pom_remove_dep :maven-findbugs-plugin

%build
mkdir .maven
export CLASSPATH=$(build-classpath xml-commons-apis)
ant -Dant.build.sysclasspath=first jar javadoc

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{name}-%{version}.jar \
$RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/samples
cp -pr src/java/samples/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/samples

# POM and depmap
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap -a saxpath:saxpath

%files
%doc LICENSE.txt
%{_javadir}/*
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc %{_javadocdir}/*

%files demo
%{_datadir}/%{name}-%{version}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt3_9jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt3_5jpp7
- fc update

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt3_1jpp6
- fixed build with moved maven1

* Tue Oct 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt2_1jpp6
- rebuild with target=5 (to avoid class poisoning)

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_1jpp6
- new version

* Mon Jun 15 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_3jpp5
- added repolib

* Fri Nov 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Mon Apr 30 2007 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.4beta2
- added JPackage compat stuff

* Fri Mar 24 2006 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt0.3beta2
- Fix typo in requires of javadoc package

* Wed Mar 22 2006 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt0.2beta2
- Fix build with j2se1.5

* Sat Apr 23 2005 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt0.1beta2
- Initial build for ALT Linux Sisyphus

