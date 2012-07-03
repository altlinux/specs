%define oldname jakarta-commons-cli
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

%define gcj_support 0

%define base_name       cli
%define short_name      commons-%{base_name}
%define section         devel

Name:           jakarta-commons-cli11
Version:        1.1
Release:        alt3_2jpp6
Epoch:          1
Summary:        Jakarta Commons CLI, a Command Line Interface for Java
License:        ASL 2.0
Group:          Development/Java
URL:            http://jakarta.apache.org/commons/cli/
Source0:        http://archive.apache.org/dist/jakarta/commons/cli/source/%{short_name}-%{version}-src.tar.gz
Patch0:         %{oldname}-crosslink.patch
Patch1:         %{oldname}-MultiOptions.patch
# XXX: (dwalluck): These are optional
#Requires:       jakarta-commons-lang
#Requires:       jakarta-commons-logging
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit >= 0:1.6
BuildRequires: junit
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: jpackage-utils
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif

%description
The CLI library provides a simple and easy to use API for working with
the command line arguments and options.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildRequires: java-javadoc
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -p0
%patch1 -p0
find . -name '*.jar' -exec rm -f '{}' \;

%build
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=$(build-classpath commons-logging commons-lang)
export CLASSPATH="$CLASSPATH:target/classes:target/test-classes"
 # for tests
mkdir lib
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Dbuild.sysclasspath=only \
  -Dfinal.name=%{short_name} \
  -Dj2se.javadoc=%{_javadocdir}/java \
  jar test dist

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{short_name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|jakarta-||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt README.txt
%{_javadir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt3_2jpp6
- compat build

* Sat Sep 04 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt2_2jpp6
- added multiarg patch

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt2_1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt1_1jpp5
- converted from JPackage by jppimport script

* Sat Aug 11 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt2_8jpp1.7
- converted from JPackage by jppimport script

* Fri Aug 10 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_8jpp1.7
- converted from JPackage by jppimport script

* Wed Apr 18 2007 Damir Shayhutdinov <damir@altlinux.ru> 2.0-alt0.svn530128
- Updated to revision 530128 (20070418)

* Wed May 04 2005 Vladimir Lettiev <crux@altlinux.ru> 2.0-alt0.1
- Initial build for ALTLinux Sisyphus
- svn snapshot 20050504

