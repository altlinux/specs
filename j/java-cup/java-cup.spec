Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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

#define with()

#define without()

#define bcond_with()

#define bcond_without()


%def_with                bootstrap

%define gcj_support        0
%define cvs_version        11a

Name:           java-cup
Version:        0.11
Release:        alt2_0.a.2jpp5
Epoch:          2
Summary:        LALR Parser Generator in Java
License:        BSD
URL:            http://www2.cs.tum.edu/projects/cup/
# https://www2.in.tum.de/WebSVN/dl.php?repname=CUP&path=/develop/&rev=0&isdir=1
Source0:        develop.tar.bz2
Source1:        java-cup.script
Source2:        java-cup-generated-files.tar.bz2
Patch0:         java-cup-javadoc.patch
Patch1:         java-cup-no-classpath-in-manifest.patch
Patch2:         java-cup-no-cup-no-jflex.patch
Patch3:         java-cup-classpath.patch
# Missing symbolFactory initialization in lr_parser, causes sinjdoc to crash
Patch4:         java-cup-lr_parser-constructor.patch
BuildRequires: ant
%if_without bootstrap
BuildRequires: java-cup
BuildRequires: jflex
%endif
Obsoletes:      java_cup < %{epoch}:%{version}-%{release}
Provides:       java_cup = %{epoch}:%{version}-%{release}
Group:          Development/Java
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
Buildarch:      noarch
%endif

%description
java-cup is a LALR Parser Generator in Java.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package manual
Summary:        Documentation for %{name}
Group:          Development/Java
BuildArch: noarch

%description manual
Documentation for %{name}.

%prep
%setup -q -n develop
%patch0 -p1
%patch1 -p1
%if_with bootstrap
%setup -q -T -D -a 2 -n develop
%patch2 -p1
%else
%{_bindir}/find . -name '*.jar' | %{_bindir}/xargs %{__rm}
%patch3 -p1
%endif
%patch4 -p1
%{__perl} -pi -e 's/1\.2/1.5/g' build.xml
%{__mkdir_p} classes dist

%build
%if_with bootstrap
export CLASSPATH=
%else
export CLASSPATH=$(build-classpath java-cup jflex)
%endif
export OPT_JAR_LIST=:
%ant
%ant javadoc

%install

# jar
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -a dist/%{name}-%{cvs_version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__cp} -a dist/%{name}-%{cvs_version}-runtime.jar %{buildroot}%{_javadir}/%{name}-runtime-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# compatibility symlinks
(cd %{buildroot}%{_javadir} && %{__ln_s} %{name}.jar java_cup.jar && %{__ln_s} %{name}-runtime.jar java_cup-runtime.jar)

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -a dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
(cd %{buildroot}%{_javadocdir} && %{__ln_s} %{name}-%{version} %{name})

%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -p -m 755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc changelog.txt
%attr(0755,root,root) %{_bindir}/%{name}
%{_javadir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif

%files manual
%doc manual.html

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 2:0.11-alt2_0.a.2jpp5
- use default jpp profile

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 2:0.11-alt1_0.a.2jpp5
- new version

