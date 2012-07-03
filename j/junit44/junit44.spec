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

Name:           junit44
Version:        4.4
Release:        alt1_1jpp6
Epoch:          0
Summary:        Java regression test package
License:        CPL
Url:            http://www.junit.org/
Group:          Development/Java
Source0:        junit-4.4.tar.gz
# steps to reproduce
# cvs -d:pserver:anonymous@junit.cvs.sourceforge.net:/cvsroot/junit login
# cvs -z3 -d:pserver:anonymous@junit.cvs.sourceforge.net:/cvsroot/junit export -r r44 junit
# mv junit junit-4.4
# tar czf junit-4.4.tar.gz junit-4.4/

Source1:        junit-4.4.pom
Patch0:         junit4-4.4-AllTests.patch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
BuildRequires: dos2unix
BuildRequires: hamcrest
Requires: hamcrest
%if ! %{gcj_support}
Buildarch:     noarch
%endif

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
JUnit is a regression testing framework written by Erich Gamma and Kent Beck. 
It is used by the developer who implements unit tests in Java. JUnit is Open
Source Software, released under the Common Public License Version 1.0 and 
JUnit is Open Source Software, released under the IBM Public License and
hosted on SourceForge.


%package manual
Group:          Development/Java
Summary:        Manual for %{name}
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Group:          Development/Java
Summary:        Demos for %{name}
Requires: %{name} = %{version}-%{release}

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n junit-%{version}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
ln -sf $(build-classpath hamcrest/core) lib/hamcrest-core-1.1.jar
rm src/org/junit/tests/BothTest.java
%patch0 -b .sav0

%build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  dist

find -name \*.htm -o -name \*.html | xargs dos2unix

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 junit%{version}/junit-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir} 
ln -sf %{name}-%{version}.jar %{name}.jar
popd
# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap junit junit %{version} JPP %{name}
%add_to_maven_depmap junit junit44 %{version} JPP %{name}
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/junit-%{version}
cp -pr junit%{version}/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/junit-%{version}
# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/demo/junit # Not using %name for last part because it is 
                                                                # part of package name
cp -pr junit%{version}/junit/* $RPM_BUILD_ROOT%{_datadir}/%{name}/demo/junit

%if %{gcj_support}
# these --exclude options work around an aot-compile-rpm problem with test.jar
%{_bindir}/aot-compile-rpm \
     --exclude usr/share/%{name}/demo \
     --exclude usr/share/%{name}/demo/junit/tests/runner/test.jar
%endif 

ln -s junit-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc cpl-v10.html README.html
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/junit-%{version}.jar.*
%endif

%files manual
%doc junit%{version}/doc/*

%files javadoc
%doc %{_javadocdir}/junit-%{version}
%doc %{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%changelog
* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.4-alt1_1jpp6
- jpp 6 release

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.4-alt1_1jpp5
- compat version

