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


Summary:        Radeox Wiki rendering engine 
Name:           radeox
Version:        0.9
Release:        alt3_0.beta.4jpp6
Epoch:          0
License:        LGPL
URL:            http://radeox.org/
Group:          Development/Java
Source0:        %{name}-%{version}-BETA-src.tgz
Source1:        http://repo1.maven.org/maven2/radeox/radeox/0.9/radeox-0.9.pom
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: jakarta-commons-logging
BuildRequires: oro
BuildRequires: picocontainer
BuildRequires: junitperf

Requires: jakarta-commons-logging
Requires: oro
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

BuildArch:      noarch
Source44: import.info

%description
Radeox API is a lightwight wiki markup rendering 
engine API to make render engines for wikis more portable.
Radeox RE is a Wiki rendering engine implementation that 
implements the Radeox API in Java. The engine renders 
wiki markup to XHTML. The goal is to develop a feature 
rich, easy to maintain wiki library with a low bug count 
so writing your own Wiki implementation is a breeze.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}-BETA
# remove all binary libs
for f in $(find . -name "*.jar"); do mv $f $f.not; done
pushd lib
ln -s $(build-classpath commons-logging) .
ln -s $(build-classpath oro) jakarta-oro.jar
ln -s $(build-classpath junit) .
ln -s $(build-classpath junitperf) .
#ln -s $(build-classpath picocontainer) .
popd
# Pico-Example needs hierarchical picocontainer
rm -rf src/org/radeox/example

%build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 test

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p lib/%{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr conf $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
%add_to_maven_depmap %{name} %{name}-oro %{version} JPP %{name}

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%doc license.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_datadir}/%{name}-%{version}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*


%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}


%changelog
* Sat Jan 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt3_0.beta.4jpp6
- java 5 build

* Sat Jan 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt2_0.beta.4jpp6
- java 5 build

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt1_0.beta.4jpp6
- new version

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt1_0.beta.3jpp5
- new jpp release

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt1_0.beta.2jpp1.7
- converted from JPackage by jppimport script

