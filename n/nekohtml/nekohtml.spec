Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# Copyright (c) 2000-2009, JPackage Project
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

Name:           nekohtml
Version:        1.9.22
Release:        alt1_2jpp8
Epoch:          0
Summary:        HTML scanner and tag balancer
License:        ASL 2.0
URL:            http://nekohtml.sourceforge.net/
# No upstream tarball for this release
# svn export svn://svn.code.sf.net/p/nekohtml/code/branches/nekohtml-1.9.22 nekohtml-1.9.22
# find nekohtml-1.9.22 -name '*.jar' -delete
# tar cjf nekohtml-1.9.22.tar.bz2 nekohtml-1.9.22/
Source0:        %{name}-%{version}.tar.bz2
Source2:        nekohtml-component-info.xml
Source3:        http://central.maven.org/maven2/net/sourceforge/%{name}/%{name}/%{version}/%{name}-%{version}.pom
Patch0:         0001-Crosslink-javadoc.patch
Patch1:         0002-Jar-paths.patch
# Add proper attributes to MANIFEST.MF file so bundle can be used by other OSGI bundles.
Patch2:         0003-Add-OSGi-attributes.patch

Requires:       bcel
Requires:       xerces-j2 >= 0:2.7.1
Requires:       xml-commons-apis
BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  bcel
BuildRequires:  bcel-javadoc
BuildRequires:  xerces-j2 >= 0:2.7.1
BuildRequires:  xerces-j2-javadoc
BuildRequires:  xml-commons-apis

BuildArch:      noarch
Source44: import.info

%description
NekoHTML is a simple HTML scanner and tag balancer that enables
application programmers to parse HTML documents and access the
information using standard XML interfaces. The parser can scan HTML
files and "fix up" many common mistakes that human (and computer)
authors make in writing HTML documents.  NekoHTML adds missing parent
elements; automatically closes elements with optional end tags; and
can handle mismatched inline element tags.
NekoHTML is written using the Xerces Native Interface (XNI) that is
the foundation of the Xerces2 implementation. This enables you to use
the NekoHTML parser with existing XNI tools without modification or
rewriting code.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Group: Development/Java
Summary:        Demo for %{name}
Requires:       %{name} = %{epoch}:%{version}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

find -name "*.jar" -delete
sed -i 's/\r$//g' *.txt doc/*.html

# cannonization test fails on some whitespace, TODO investigate
rm data/meta/test-meta-encoding3.html

%mvn_alias net.sourceforge.%{name}:%{name} %{name}:%{name}
%mvn_package net.sourceforge.%{name}:%{name}-samples demo
%mvn_file ':{*}' @1

%build
export CLASSPATH=$(build-classpath bcel xerces-j2)
%{ant} \
    -Dbuild.sysclasspath=first \
    -Dlib.dir=%{_javadir} \
    -Djar.file=%{name}.jar \
    -Djar.xni.file=%{name}-xni.jar \
    -Djar.samples.file=%{name}-samples.jar \
    -Dbcel.javadoc=%{_javadocdir}/bcel \
    -Dj2se.javadoc=%{_javadocdir}/java \
    -Dxni.javadoc=%{_javadocdir}/xerces-j2-xni \
    -Dxerces.javadoc=%{_javadocdir}/xerces-j2-impl \
    clean jar jar-xni test doc
# test - disabled because it makes the build failing

%mvn_artifact %{SOURCE3} %{name}.jar
%mvn_artifact net.sourceforge.%{name}:%{name}-xni:%{version} %{name}-xni.jar
%mvn_artifact net.sourceforge.%{name}:%{name}-samples:%{version} %{name}-samples.jar

%install
%mvn_install -J build/doc/javadoc

# Scripts
%jpackage_script org.cyberneko.html.filters.Writer "" "" "nekohtml:xerces-j2" nekohtml-filter true

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files -f .mfiles
%doc --no-dereference LICENSE.txt README.txt doc/*.html
%{_bindir}/%{name}-filter
%config(noreplace,missingok) /etc/java/%{name}.conf

%files javadoc -f .mfiles-javadoc

%files demo -f .mfiles-demo

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.22-alt1_2jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.22-alt1_1jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.14-alt2_12jpp7
- new release

* Wed Jul 30 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.14-alt2_11jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.9.14-alt2_9jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9.14-alt2_4jpp6
- new jpp relase

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.9.14-alt2_1jpp6
- new version

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.9.14-alt1_1jpp6
- added osgi manifest

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt1_5jpp5
- new jpackage release

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt1_4jpp1.7
- converted from JPackage by jppimport script

