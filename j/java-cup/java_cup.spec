%define oldname java_cup
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

%define pkg_version     11a
%define with_bootstrap  0

Name:           java-cup
Version:        0.11a
Release:        alt1_9jpp7
Epoch:          2
Summary:        Java source interpreter
License:        BSD and LGPLv2
URL:            http://www.cs.princeton.edu/%%7Eappel/modern/java/CUP/
#svn export -r 21 https://www2.in.tum.de/repos/cup/develop/ java_cup-0.11a 
#tar cjf java_cup-0.11a.tar.bz2 java_cup-0.11a/
Source0:        java_cup-0.11a.tar.bz2
Source1:        java_cup-pom.xml
Source2:	%{oldname}-runtime-MANIFEST.MF
Patch0:         %{oldname}-build.patch
Patch1:         java_cup-0.11a-manifest.patch
BuildRequires:  zip
BuildRequires:  ant
BuildRequires:  jpackage-utils >= 0:1.5
BuildRequires:	jflex
%if ! %{with_bootstrap}
BuildRequires:	java_cup >= 1:0.11
%endif
Group:          Development/Java
BuildArch:      noarch

Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Source44: import.info
Provides: java_cup = %{epoch}:%{version}-%release

%description
java_cup is a LALR Parser Generator for Java

%package javadoc
Summary:        Javadoc for java_cup
Group:          Development/Java
BuildArch: noarch

%description javadoc
Javadoc for java_cup

%package manual
Summary:        Documentation for java_cup
Group:          Development/Java
BuildArch: noarch

%description manual
Documentation for java_cup.

%prep
%setup -q -n %{oldname}-%{version} 
%patch0 -b .build
%patch1 -p1 -b .manifest
cp %{SOURCE1} pom.xml

# remove all binary files
find -name "*.class" -delete

%if ! %{with_bootstrap}
# remove prebuilt JFlex
rm -rf java_cup-0.11a/bin/JFlex.jar

# remove prebuilt java_cup, if not bootstrapping
rm -rf java_cup-0.11a/bin/java-cup-11.jar
%endif

%build
%if ! %{with_bootstrap}
export CLASSPATH=$(build-classpath java_cup java_cup-runtime jflex)
%endif

ant
find -name parser.cup -delete
ant javadoc

%install
# inject OSGi manifest
mkdir -p META-INF
cp -p %{SOURCE2} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u dist/java-cup-%{pkg_version}-runtime.jar META-INF/MANIFEST.MF

# jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/java-cup-%{pkg_version}.jar $RPM_BUILD_ROOT%{_javadir}/%{oldname}-%{version}.jar
install -m 644 dist/java-cup-%{pkg_version}-runtime.jar $RPM_BUILD_ROOT%{_javadir}/%{oldname}-runtime-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}
cp -pr dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}
(cd $RPM_BUILD_ROOT%{_javadocdir} && ln -sf %{oldname}-%{version} %{oldname})

%add_to_maven_depmap java_cup java_cup %{version} JPP java_cup

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{oldname}.pom
# jpp compat
ln -s java_cup-runtime.jar %buildroot%_javadir/java-cup-runtime.jar
ln -s java_cup.jar %buildroot%_javadir/java-cup.jar


%files
%doc changelog.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
# jpp compat
#%_javadir/java-cup-runtime.jar
#%_javadir/java-cup.jar


%files manual
%doc manual.html

%files javadoc
%doc %{_javadocdir}/%{oldname}-%{version}
%doc %{_javadocdir}/%{oldname}

%changelog
* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 2:0.11a-alt1_9jpp7
- fc release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 2:0.11-alt2_0.a.2jpp5
- use default jpp profile

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 2:0.11-alt1_0.a.2jpp5
- new version

