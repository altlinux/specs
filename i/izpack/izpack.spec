Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define gcj_support 0


Summary:        IZPack installer generator
Name:           izpack
Version:        3.8.1
Release:        alt1_4jpp5
Epoch:          0
License:        Apache Software License 2.0
URL:            http://www.izforge.com/izpack/
Group:          Development/Java
Source0:        izpack-3.8.1-src.tar.gz
# svn export http://svn.berlios.de/svnroot/repos/izpack/izpack-src/tags/release-3-8-1/
Source1:        izpack-compiler-3.8.1.pom
Source2:        izpack-installer-3.8.1.pom
Source3:        izpack-izevent-3.8.1.pom
Source4:        izpack-standalone-compiler-3.8.1.pom
Source5:        izpack-uninstaller-3.8.1.pom
Source6:        izpack-uninstaller-ext-3.8.1.pom


BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: regexp
Requires: regexp
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%description
IzPack is an installers generator for the Java platform. It 
produces lightweight installers that can be run on any operating 
system where a Java virtual machine is available. Depending on 
the operating system, it can be launched by a double-click or a 
simple 'java -jar installer.jar' on a shell. The most common use 
is to distribute applications for the Java platform, but you can 
also use it for other kinds of projects. The main benefit of 
IzPack is that it provides a clean and unique way of distributing 
a project to users using different operating systems. IzPack is 
reported to run on :
* Unix-like systems, mostly Linux and BSD
* MacOS X
* Windows variants
A big care has been put in making IzPack as small as possible in 
order to reduce the weight of IzPack itself in the final installer 
archive. Also, IzPack has been designed around modularity and 
flexibility. As a consequence, you are able to specify how your 
installer should be by selecting the panels that you want to show 
to the final user. Sometimes there are even several panels for the 
same usage so that you can pick the one that suits the best your 
needs. If ever you don't find your way through the available panels, 
you can still develop your own ones with the nice and easy IzPack 
API. There's even an embedded XML parser !


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%package manual
Summary:        Manual for %{name}
Group:          Development/Documentation

%description manual
%{summary}.

%package demo
Summary:        Samples for %{name}
Group:          Development/Documentation

%description demo
%{summary}.

%prep
%setup -q -n %{name}-%{version}-src
# remove all binary libs
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
  mv $j $j.no
done


%build
pushd lib
ln -sf $(build-classpath regexp) jakarta-regexp-1.3.jar
ln -sf $(build-classpath ant) .
popd
cd src
ant all build.javadoc

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}

cp -p lib/uninstaller.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/uninstaller-%{version}.jar
%add_to_maven_depmap %{name} %{name}-uninstaller %{version} JPP/%{name} uninstaller

cp -p lib/compiler.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/compiler-%{version}.jar
%add_to_maven_depmap %{name} %{name}-compiler %{version} JPP/%{name} compiler

cp -p lib/uninstaller-ext.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/uninstaller-ext-%{version}.jar
%add_to_maven_depmap %{name} %{name}-uninstaller-ext %{version} JPP/%{name} uninstaller-ext

cp -p lib/installer.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/installer-%{version}.jar
%add_to_maven_depmap %{name} %{name}-installer %{version} JPP/%{name} installer

cp -p lib/standalone-compiler.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/standalone-compiler-%{version}.jar
%add_to_maven_depmap %{name} %{name}-standalone-compiler %{version} JPP/%{name} standalone-compiler

cp -p lib/izevent.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/izevent-%{version}.jar
%add_to_maven_depmap %{name} %{name}-izevent %{version} JPP/%{name} izevent

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-compiler.pom
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-installer.pom
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-izevent.pom
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-standalone-compiler.pom
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-uninstaller.pom
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-uninstaller-ext.pom

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/izpack/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr doc/nanoxml/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p *.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# resources
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/bin
cp -pr bin/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/bin
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/bin/native

# samples
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/sample
cp -pr sample/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/sample

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_docdir}/%{name}-%{version}/*.txt
%{_javadir}/%{name}/*.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%files demo
%{_datadir}/%{name}-%{version}

%changelog
* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.8.1-alt1_4jpp5
- new jpp release

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.8.1-alt1_3jpp5
- fixed repocop warnings

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.8.1-alt1_3jpp1.7
- converted from JPackage by jppimport script

