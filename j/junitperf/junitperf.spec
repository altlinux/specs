Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# Copyright (c) 2000-2007, JPackage Project
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

Name:           junitperf
Version:        1.9.1
Release:        alt1_17jpp8
Summary:        JUnit extension for performance and scalability testing
License:        BSD
Source0:        http://www.clarkware.com/software/junitperf-1.9.1.zip
Source1:        https://repository.jboss.org/nexus/content/repositories/thirdparty-uploads/junitperf/junitperf/%{version}/junitperf-%{version}.pom
URL:            http://www.clarkware.com/software/JUnitPerf.html
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  javapackages-local
BuildRequires:  junit >= 3.2
BuildArch:      noarch
Requires:       junit >= 3.2
Source44: import.info

%description
JUnitPerf is a collection of JUnit test decorators used to measure the
performance and scalability of functionality contained within existing
JUnit tests.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%package demo
Group: Development/Java
Summary:        Demos and samples for %{name}
Requires:       %{name} = %{version}

%description demo
%{summary}.

%prep
%setup -q -n %{name}-%{version}

# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;

%build
CLASSPATH=$(build-classpath junit) ant -Dbuild.sysclasspath=first jar test javadoc

# request maven artifact installation
%mvn_artifact %{SOURCE1} dist/junitperf-%{version}.jar

%install
%mvn_install

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/docs/api/* %{buildroot}%{_javadocdir}/%{name}

# demo
install -d -m 0755 %{buildroot}%{_datadir}/%{name}
cp -pr samples %{buildroot}%{_datadir}/%{name}

%files -f .mfiles
%doc LICENSE README docs/JUnitPerf.html
%dir %{_javadir}/%{name}

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%files demo
%doc LICENSE
%{_datadir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.1-alt1_17jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.1-alt1_16jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.1-alt1_12jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.1-alt1_11jpp7
- new release

* Fri Mar 15 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.9.1-alt1_8jpp7
- fc update

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.9.1-alt1_3jpp5
- new jpackage release

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.9.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

* Mon Apr 25 2005 Vladimir Lettiev <crux@altlinux.ru> 1.9.1-alt1
- Initial build for ALT Linux Sisyphus

