Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
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

Name:           jarjar
Version:        1.0
Release:        alt3_5jpp7
Summary:        Jar Jar Links
License:        ASL 2.0
URL:            http://code.google.com/p/jarjar/
Group:          Development/Java
# svn export http://jarjar.googlecode.com/svn/tags/release-1-0/jarjar jarjar-1.0
Source0:        jarjar-src-1.0.zip
Source1:        jarjar.pom
Source2:        jarjar-util.pom
# Change version from "snapshot" to "1.0"
Patch0:         jarjar-1.0-build_xml.patch
# Add a cast to make a method unambiguous
Patch1:         jarjar-AntJarProcessor-cast.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  junit
BuildRequires:  objectweb-asm
BuildRequires:  gnu-regexp
BuildRequires:  maven
Requires:       objectweb-asm
Requires:       gnu-regexp
Requires:       jpackage-utils >= 0:1.7.2
Requires(post):    jpackage-utils >= 0:1.7.2
Requires(postun):  jpackage-utils >= 0:1.7.2

BuildArch:      noarch

# Work around weird file permission problems
%define __jar_repack %{nil}
Source44: import.info

%description
Jar Jar Links is a utility that makes it easy to repackage Java 
libraries and embed them into your own distribution. This is 
useful for two reasons:
You can easily ship a single jar file with no external dependencies. 
You can avoid problems where your library depends on a specific 
version of a library, which may conflict with the dependencies of 
another library.

%package maven-plugin
Summary:        Maven plugin for %{name}
Group:          Development/Java
Requires:       maven
Requires:       %{name} = %{version}-%{release}
Obsoletes: %{name}-maven2-plugin <= 1.0
Provides: %{name}-maven2-plugin = %{version}-%{release}

%description maven-plugin
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}
# remove all binary libs
rm -f lib/*.jar
%patch0 -p1
%patch1 -p1

%build
pushd lib
ln -sf $(build-classpath gnu-regexp)
ln -sf $(build-classpath objectweb-asm/asm-3.1) asm-3.1.jar
ln -sf $(build-classpath objectweb-asm/asm-commons-3.1) asm-commons-3.1.jar
ln -sf $(build-classpath maven/maven-plugin-api) maven-plugin-api.jar
popd
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=$(build-classpath ant)
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar jar-util javadoc mojo test

%install
# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}

install -m 644 dist/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -m 644 dist/%{name}-util-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-util.jar
install -m 644 dist/%{name}-plugin-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-maven-plugin.jar

%add_to_maven_depmap jarjar           %{name} %{version} JPP %{name}
%add_to_maven_depmap tonic            %{name} %{version} JPP %{name}
%add_to_maven_depmap com.tonicsystems %{name} %{version} JPP %{name}
%add_to_maven_depmap jarjar           %{name}-util %{version} JPP %{name}-util
%add_to_maven_depmap tonic            %{name}-util %{version} JPP %{name}-util
%add_to_maven_depmap com.tonicsystems %{name}-util %{version} JPP %{name}-util
%add_to_maven_depmap jarjar           %{name}-plugin %{version} JPP %{name}-plugin
%add_to_maven_depmap tonic            %{name}-plugin %{version} JPP %{name}-plugin
%add_to_maven_depmap com.tonicsystems %{name}-plugin %{version} JPP %{name}-plugin

sed -i -e s/@VERSION@/%{version}/g maven/pom.xml

# poms
install -pD -T -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
install -pD -T -m 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-util.pom
install -pD -T -m 644 maven/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-plugin.pom

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
# compat for old groovy 1 jpp5
%add_to_maven_depmap com.tonicsystems jarjar %{version} JPP %{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%doc COPYING
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-util.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavenpomdir}/JPP-%{name}-util.pom
%{_mavendepmapfragdir}/*

%files maven-plugin
%{_mavenpomdir}/JPP-%{name}-plugin.pom
%{_javadir}/%{name}-maven-plugin.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_5jpp7
- fc version

* Tue Jan 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_3jpp6
- fixed build of portals-bridges

* Tue Jan 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_3jpp6
- added compat depmap

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_3jpp6
- new jpp relase

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt1_2jpp5
- converted from JPackage by jppimport script

* Sat Nov 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt1_1jpp1.7
- updated to new jpackage release

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt1_2jpp1.7
- converted from JPackage by jppimport script

