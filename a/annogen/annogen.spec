#TODO:  Patch1 is fixed manually for java 7
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


# To make the tarball:
# svn export svn://svn.annogen.codehaus.org/annogen/scm/annogen/tags/release-0_1_0/ annogen

Name:           annogen
Summary:        Framework to help work with JSR175 Annotations
Version:        0.1.1
Release:	alt3_8jpp6
Epoch:          0
URL:            http://annogen.codehaus.org/
License:        Apache Software License 2.0
Group:          Development/Java
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-%{version}.pom

Patch0:         annogen-build-jam-test.patch
Patch1:         annogen-build-distribution.patch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  ant-junit
BuildRequires:  junit >= 0:3.8.2
BuildRequires:  antlr >= 0:2.7.4
BuildRequires:  findbugs >= 0:0.9.1
BuildRequires:  bcel >= 0:5.1
BuildRequires:  stax_1_0_api
BuildRequires:  bea-stax >= 0:1.2.0
BuildRequires:  dom4j >= 0:1.6.1
BuildRequires:  qdox >= 0:1.10
BuildRequires:  xerces-j2 >= 0:2.7.1
Requires:       antlr >= 0:2.7.4
Requires:       bcel >= 0:5.1
Requires:       stax_1_0_api
Requires:       dom4j >= 0:1.6.1
Requires:       qdox >= 0:1.10
Requires:       xerces-j2 >= 0:2.7.1

BuildArch:      noarch

Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
Annogen is a framework which helps you work with JSR175 Annotations. 
In a nutshell, Annogen generates a proxy layer in front of your Annotations.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}

find . -name '*.?ar' | xargs rm -f

ln -sf $(build-classpath antlr) external/lib
ln -sf $(build-classpath bcel) external/lib
ln -sf $(build-classpath bea-stax-api) external/lib/stax-api.jar
ln -sf $(build-classpath bea-stax-ri) external/lib/stax-impl.jar
ln -sf $(build-classpath dom4j) external/lib
ln -sf $(build-classpath qdox) external/lib
ln -sf $(build-classpath junit) external/lib
ln -sf $(build-classpath xerces-j2) external/lib


build-jar-repository -s -p external/findbugs \
findbugs/findbugs.jar \
findbugs/findbugs-ant.jar

%patch0 -b .sav0
%patch1 -b .sav1

%build
unset CLASSPATH

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  distribution test jam.test

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/distribution/%{name}-%{version}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/distribution/docs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.1.1-alt3_8jpp6
- fixed build with java 7 (fixed patch1)

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.1.1-alt2_8jpp6
- converted from JPackage by jppimport script

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1.1-alt2_8jpp5
- selected java5 compiler explicitly

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1.1-alt1_8jpp5
- new jpackage release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1.1-alt1_3jpp5
- converted from JPackage by jppimport script

* Mon Dec 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.1.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

