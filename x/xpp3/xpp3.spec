# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
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

%define oversion 1.1.3_8

Summary:        XML Pull Parser
Name:           xpp3
Version:        1.1.3.8
Release:        alt1_8jpp7
Epoch:          1
License:        ASL 1.1
URL:            http://www.extreme.indiana.edu/xgws/xsoap/xpp/mxp1/index.html
Group:          Development/Java
Source0:        http://www.extreme.indiana.edu/dist/java-repository/xpp3/distributions/xpp3-%{oversion}_src.tgz
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/xpp3/xpp3/1.1.3.4.O/xpp3-1.1.3.4.O.pom
Source2:        http://mirrors.ibiblio.org/pub/mirrors/maven2/xpp3/xpp3_xpath/1.1.3.4.O/xpp3_xpath-1.1.3.4.O.pom
Source3:        http://mirrors.ibiblio.org/pub/mirrors/maven2/xpp3/xpp3_min/1.1.3.4.O/xpp3_min-1.1.3.4.O.pom
Patch0:         %{name}-link-docs-locally.patch
Requires:       jpackage-utils >= 0:1.6
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6
BuildRequires:  junit
BuildRequires:  xml-commons-apis
BuildRequires:  /usr/bin/perl
Requires:       jpackage-utils
Requires:       junit
Requires:       xml-commons-apis
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils

BuildArch:      noarch
Source44: import.info

%description
Xml Pull Parser 3rd Edition (XPP3) MXP1 is a new XmlPull
parsing engine that is based on ideas from XPP and in
particular XPP2 but completely revised and rewritten to
take best advantage of latest JIT JVMs such as Hotspot in JDK 1.4.

%package minimal
Summary:        Minimal XML Pull Parser
Group:          Development/Java
Requires:       jpackage-utils
Requires:       junit
Requires:       xml-commons-apis
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils

%description minimal
Minimal XML pull parser implementation.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{oversion}
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%patch0

%build
export CLASSPATH=$(build-classpath xml-commons-apis junit)
ant xpp3 junit apidoc

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/%{name}-%{oversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
cp -p build/%{name}_min-%{oversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-minimal.jar
cp -p build/%{name}_xpath-%{oversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-xpath.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

rm -rf doc/{build.txt,api}

install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE3} \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}-minimal.pom
%add_to_maven_depmap %{name} %{name}_min %{version} JPP %{name}-minimal

mv %{buildroot}%{_mavendepmapfragdir}/%{name} %{buildroot}%{_mavendepmapfragdir}/%{name}-minimal
install -pm 644 %{SOURCE1} \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

install -pm 644 %{SOURCE2} \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}-xpath.pom
%add_to_maven_depmap %{name} %{name}_xpath %{version} JPP %{name}-xpath


%files
%doc README.html LICENSE.txt doc/*
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-xpath.jar
%{_mavenpomdir}/JPP-%{name}-xpath.pom
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files minimal
%doc LICENSE.txt
%{_mavendepmapfragdir}/%{name}-minimal
%{_mavenpomdir}/JPP-%{name}-minimal.pom
%{_javadir}/%{name}-minimal.jar

%files javadoc
%doc %{_javadocdir}/*

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.1.3.8-alt1_8jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.1.3.8-alt1_7jpp7
- fc update

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt2_2jpp6
- split maven-fragments for minimal subpackage

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt1_2jpp6
- added pom

* Wed Feb 25 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3.8-alt3_1jpp5
- added xpp3_min pom

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3.8-alt2_1jpp5
- jpackage 5.0

* Tue Jul 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3.8-alt1_1jpp1.7
- updated to new jpackage release

* Thu Mar 23 2006 Vladimir Lettiev <crux@altlinux.ru> 1.1.3.4-alt2m
- Fix build with j2se-1.5

* Sun Apr 24 2005 Vladimir Lettiev <crux@altlinux.ru> 1.1.3.4-alt1m
- Initial build for ALT Linux Sisyphus

