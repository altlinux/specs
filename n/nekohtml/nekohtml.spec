# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
BuildRequires: /proc
BuildRequires: jpackage-compat
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
Version:        1.9.14
Release:        alt2_11jpp7
Epoch:          0
Summary:        HTML scanner and tag balancer
License:        ASL 2.0
URL:            http://nekohtml.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# http://www.jpackage.org/cgi-bin/viewvc.cgi/*checkout*/rpms/devel/nekohtml/nekohtml-filter.sh?root=jpackage&content-type=text%2Fplain
Source1:        %{name}-filter.sh
Source2:        nekohtml-component-info.xml
Source3:        http://repo1.maven.org/maven2/net/sourceforge/nekohtml/nekohtml/1.9.14/nekohtml-1.9.14.pom
Patch0:         %{name}-crosslink.patch
Patch1:         %{name}-jars.patch
Group:          Development/Java
Requires:       bcel
Requires:       jpackage-utils >= 0:1.6
Requires:       xerces-j2 >= 0:2.7.1
Requires:       xml-commons-apis
BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  java-javadoc
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
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Demo for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{_bindir}/find . -name "*.jar" | %{_bindir}/xargs -t %{__rm}
%{__perl} -pi -e 's/\r$//g' *.txt doc/*.html
%{__rm} -r doc/javadoc

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
    clean jar jar-xni doc 
# test - disabled because it makes the build failing

%install
# Jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 %{name}{,-samples,-xni}.jar $RPM_BUILD_ROOT%{_javadir}/

# Scripts
install -Dpm 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}-filter

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap -a nekohtml:nekohtml

# Javadocs
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -a build/doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc --no-dereference LICENSE.txt README.txt doc/*.html
%attr(755,root,root) %{_bindir}/%{name}-filter
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-xni.jar

%files javadoc
%{_javadocdir}/%{name}

%files demo
%{_javadir}/%{name}-samples.jar

%changelog
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

