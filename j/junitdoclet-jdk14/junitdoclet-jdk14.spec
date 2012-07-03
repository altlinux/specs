# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2010, JPackage Project
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


Summary:        JUnit Doclet test generator for JDK 1.4
Name:           junitdoclet-jdk14
Version:        1.0.2
Release:        alt3_7jpp6
Epoch:          0
License:        LGPL
URL:            http://www.junitdoclet.org/
Group:          Development/Java
Source0:        JUnitDoclet_1.0.2_jdk1.4.zip
Patch0:         junitdoclet-jdk142.patch
Patch1:         junitdoclet-jdk14-build.patch
Patch2:         junitdoclet-jdk14-DocImpl.patch
Patch3:         junitdoclet-jdk14-ProgramElementDocImpl.patch
Patch4:         junitdoclet-jdk14-ClassDocImpl.patch
Patch5:         junitdoclet-jdk14-MethodDocImpl.patch
Patch6:         junitdoclet-jdk14-PackageDocImpl.patch
Patch7:         junitdoclet-jdk14-ParameterImpl.patch

BuildRequires:  jpackage-utils >= 0:5.0.0
BuildRequires:  ant >= 0:1.7
BuildRequires:  ant-junit
%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires:    gnu-crypto
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Source44: import.info

%description
Especially creating and maintaining a test structure is 
often used as an excuse. JUnitDoclet lowers the step 
toward JUnit. It generates skeletons of TestCases based 
on your application source code. And it supports you to 
reorganize tests during refactoring. Suddenly all the 
excuses don't count any longer. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents and Examples for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -T -c -n JUnitDoclet.1.0.2
(cd ..
unzip -q %{SOURCE0}
)
rm JUnitDoclet.jar
rm *.txt
unzip -q src.zip
rm src.zip

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5
%patch6 -b .sav6
%patch7 -b .sav7

%build
export OPT_JAR_LIST="ant-launcher ant/ant-junit junit"
export CLASSPATH=
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/JUnitDoclet.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/res
cp -p res/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/res

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr build/JUnitDoclet.unreleased/doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm --exclude %{_docdir}/%{name}-%{version}/ide/packagelister.jar
%endif

%files
%doc %{_docdir}/%{name}-%{version}/lgpl.txt
%{_javadir}/*.jar
%{_datadir}/%{name}-%{version}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt3_7jpp6
- new jpp relase

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt3_6jpp5
- fixes for java6 support

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_6jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_6jpp5
- converted from JPackage by jppimport script

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_5jpp1.7
- converted from JPackage by jppimport script

