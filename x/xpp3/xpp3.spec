Packager: Igor Vlasenko <viy@altlinux.ru>
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


%define cvs_oversion 1_1_4c
%define oversion 1.1.4c

Name:           xpp3
Version:        1.1.4
Release:	alt2_2jpp6
Epoch:          0
Summary:        XML Pull Parser
License:        ASL 1.1
Group:          Development/Java
URL:            http://www.extreme.indiana.edu/xgws/xsoap/xpp/mxp1/index.html
Source0:        http://www.extreme.indiana.edu/dist/java-repository/xpp3/distributions/xpp3-1.1.4c_all.tgz
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/xpp3/xpp3/1.1.4c/xpp3-1.1.4c.pom
Source2:        http://mirrors.ibiblio.org/pub/mirrors/maven2/xpp3/xpp3_min/1.1.4c/xpp3_min-1.1.4c.pom
Source3:        http://mirrors.ibiblio.org/pub/mirrors/maven2/xpp3/xpp3_xpath/1.1.4c/xpp3_xpath-1.1.4c.pom
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jpackage-utils
BuildRequires: ant
BuildRequires: jpackage-utils
BuildRequires: junit
BuildRequires: xml-commons-jaxp-1.3-apis
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

%description minimal
Minimal XML pull parser implementation.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n xpp3-%{oversion}
%{_bindir}/find . -name "*.jar" | %{_bindir}/xargs -t rm
mkdir -p src/java/addons_tests

%build
export OPT_JAR_LIST=:
export CLASSPATH=$(build-classpath xml-commons-jaxp-1.3-apis junit)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 all apidoc junit

%install

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p build/%{name}-%{oversion}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
cp -p build/%{name}_min-%{oversion}.jar %{buildroot}%{_javadir}/%{name}-minimal-%{version}.jar
ln -s %{name}-minimal-%{version}.jar %{buildroot}%{_javadir}/%{name}_min-%{version}.jar
cp -p build/%{name}_xpath-%{oversion}.jar %{buildroot}%{_javadir}/%{name}-xpath-%{version}.jar
ln -s %{name}-xpath-%{version}.jar %{buildroot}%{_javadir}/%{name}_xpath-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr doc/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-minimal.pom
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-xpath.pom
%add_to_maven_depmap xmlpull xmlpull %{version} JPP %{name}
%add_to_maven_depmap xpp3 xpp3 %{version} JPP %{name}
%add_to_maven_depmap_at xpp3-minimal xpp3 xpp3_min %{version} JPP %{name}-minimal
%add_to_maven_depmap xpp3 xpp3_xpath %{version} JPP %{name}-xpath

%files
%doc README.html LICENSE.txt doc/*
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_datadir}/maven2/poms/JPP-%{name}-xpath.pom
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}_xpath.jar
%{_javadir}/%{name}_xpath-%{version}.jar
%{_javadir}/%{name}-xpath.jar
%{_javadir}/%{name}-xpath-%{version}.jar
%{_mavendepmapfragdir}/%{name}

%files minimal
%{_mavendepmapfragdir}/%{name}-minimal
%{_datadir}/maven2/poms/JPP-%{name}-minimal.pom
%{_javadir}/%{name}-minimal.jar
%{_javadir}/%{name}-minimal-%{version}.jar
%{_javadir}/%{name}_min.jar
%{_javadir}/%{name}_min-%{version}.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
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

