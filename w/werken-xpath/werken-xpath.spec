# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
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

%define dotname werken.xpath

Name:           werken-xpath
Version:        0.9.4
Release:        alt1_15.beta.12.7jpp8
Epoch:          0
Summary:        XPath implementation using JDOM
License:        Saxpath
Source0:        %{name}-%{version}.tar.xz
Source1:        http://repo1.maven.org/maven2/%{name}/%{name}/%{version}/%{name}-%{version}.pom
# used to generate Source0, upstream has no tarball like this anymore
Source2:        generate-tarball.sh
Patch0:         %{name}-ElementNamespaceContext.patch
Patch1:         %{name}-Partition.patch
Patch2:         %{name}-ParentStep.patch
Patch3:         %{name}-NodeTypeStep.patch
Patch4:         %{name}-UnAbbrStep.patch
Patch5:         %{name}-StringFunction.patch
Patch6:         %{name}-Test.patch
Patch7:         %{name}-Driver.patch
Patch8:         %{name}-runtests_sh.patch
URL:            http://sourceforge.net/projects/werken-xpath/
Requires:       jdom
BuildRequires:  ant >= 0:1.6
BuildRequires:  antlr-tool
BuildRequires:  jdom
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis
BuildRequires:  javapackages-local
Group:          Development/Other
BuildArch:      noarch
Provides:       werken.xpath = %{epoch}:%{version}-%{release}
Obsoletes:      werken.xpath < 0.9.4
Source44: import.info

%description
werken.xpath is an implementation of the W3C XPath Recommendation, on
top of the JDOM library.  It takes as input a XPath expression, and a
JDOM tree, and returns a NodeSet (java.util.List) of selected
elements.  Is is being used in the development of the
as-yet-unreleased werken.xslt (eXtensible Stylesheet Language) and the
werken.canonical (XML canonicalization) packages.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildRequires:  java-javadoc
Provides:       werken.xpath-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      werken.xpath-javadoc < 0.9.4
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

# -----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav
%patch4 -b .sav
%patch5 -b .sav
%patch6 -b .sav
%patch7 -b .sav
%patch8 -b .sav

# remove all binary libs
for j in $(find . -name "*.jar"); do
         mv $j $j.no
done

cp %{SOURCE1} .

# -----------------------------------------------------------------------------

%build
export CLASSPATH=$(build-classpath jdom antlr xerces-j2 xml-commons-apis)
ant -Dbuild.compiler=modern package javadoc compile-test
# Note that you'll have to java in PATH for this to work, it is by default
# when using a JPackage JVM.
CLASSPATH=$CLASSPATH:build/werken.xpath.jar:build/test/classes
sh runtests.sh

# -----------------------------------------------------------------------------

%install
# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/%{dotname}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# maven
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{name}-%{version}.pom \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap


# -----------------------------------------------------------------------------

%files -f .mfiles
%doc INSTALL LICENSE LIMITATIONS README TODO

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

# -----------------------------------------------------------------------------

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9.4-alt1_15.beta.12.7jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9.4-alt1_14.beta.12.6jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.9.4-alt1_12.beta.12.5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.9.4-alt1_10.beta.12.4jpp7
- new release

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 0:0.9.4-alt1_8.beta.12.4jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.4-alt1_0.beta.15jpp6
- new jpp relase

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.4-alt1_0.beta.13jpp5
- new jpp release

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.4-alt1_0.beta.13jpp1.7
- updated to new jpackage release

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.4-alt1_0.beta.12jpp1.7
- converted from JPackage by jppimport script

* Sun Jul 03 2005 Vladimir Lettiev <crux@altlinux.ru> 0.9.4-alt0.2beta
- added xml-commons-apis to classpath
- changed rpmgroup of javadoc package

* Fri May 06 2005 Vladimir Lettiev <crux@altlinux.ru> 0.9.4-alt0.1beta
- Initial build for ALT Linux Sisyphus

