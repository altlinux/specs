# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
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

%global short_name    framework
%global short_Name    Avalon

Name:        avalon-%{short_name}
Version:     4.3
Release:     alt4_15jpp8
Epoch:       0
Summary:     Java components interfaces
License:     ASL 2.0
URL:         http://avalon.apache.org/%{short_name}/
Group:       Development/Other
Source0:     http://archive.apache.org/dist/excalibur/avalon-framework/source/%{name}-api-%{version}-src.tar.gz
Source1:     http://archive.apache.org/dist/excalibur/avalon-framework/source/%{name}-impl-%{version}-src.tar.gz

# pom files are not provided in tarballs so get them from external site
Source2:     http://repo1.maven.org/maven2/avalon-framework/%{name}-api/%{version}/%{name}-api-%{version}.pom
Source3:     http://repo1.maven.org/maven2/avalon-framework/%{name}-impl/%{version}/%{name}-impl-%{version}.pom

# remove jmock from dependencies because we don't have it
Patch0:     %{name}-impl-pom.patch
Patch1:     %{name}-xerces.patch

Requires:    apache-commons-logging
Requires:    avalon-logkit
Requires:    log4j
Requires:    xalan-j2

BuildRequires:    ant
BuildRequires:	  ant-junit
BuildRequires:	  apache-commons-logging
BuildRequires:    avalon-logkit
BuildRequires:    javapackages-local
# For converting jar into OSGi bundle
BuildRequires:    aqute-bnd
BuildRequires:    junit
BuildRequires:	  log4j


BuildArch:    	  noarch

Obsoletes:    %{name}-manual <= 0:4.1.4
Source44: import.info

%description
The Avalon framework consists of interfaces that define relationships
between commonly used application components, best-of-practice pattern
enforcements, and several lightweight convenience implementations of the
generic components.
What that means is that we define the central interface Component. We
also define the relationship (contract) a component has with peers,
ancestors and children.

%package javadoc
Summary:      API documentation %{name}
Group:        Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-api-%{version}
tar xvf %{SOURCE1}

cp %{SOURCE2} .

pushd %{name}-impl-%{version}/
cp %{SOURCE3} .
%patch0
%patch1 -p2
popd

%build
export CLASSPATH=%(build-classpath avalon-logkit junit commons-logging log4j)
export CLASSPATH="$CLASSPATH:../target/%{name}-api-%{version}.jar"
ant jar test javadoc
# Convert to OSGi bundle
bnd wrap target/%{name}-api-%{version}.jar

# build implementation now
pushd %{name}-impl-%{version}
# tests removed because we don't have jmock
rm -rf src/test/*
ant jar javadoc
# Convert to OSGi bundle
bnd wrap target/%{name}-impl-%{version}.jar
popd

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/
install -d -m 755 $RPM_BUILD_ROOT/%{_mavenpomdir}

install -m 644 %{name}-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-api.jar
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}/%{name}-api

# pom file
install -pm 644 %{name}-api-%{version}.pom $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}-api.pom
%add_maven_depmap JPP-%{name}-api.pom %{name}-api.jar -a "org.apache.avalon.framework:%{name}-api"

# javadocs
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/%{name}-api/

install -m 644 %{name}-impl-%{version}/%{name}-impl-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-impl.jar
ln -sf %{_javadir}/%{name}-impl.jar ${RPM_BUILD_ROOT}%{_javadir}/%{name}.jar

# pom file
install -pm 644 %{name}-impl-%{version}/%{name}-impl-%{version}.pom $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}-impl.pom
%add_maven_depmap JPP-%{name}-impl.pom %{name}-impl.jar -a "org.apache.avalon.framework:%{name}-impl,%{name}:%{name}"

# javadocs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}/%{name}-impl
cp -pr %{name}-impl-%{version}/dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/%{name}-impl/


%files -f .mfiles
%doc LICENSE.txt NOTICE.txt
%{_javadir}/%{name}.jar

%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt4_15jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt4_14jpp8
- java 8 mass update

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt2_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt2_8jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt1_7jpp7
- new release

* Tue May 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt1_5jpp7
- fc build

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.1.5-alt3_2jpp5
- fixed build with moved maven1

* Sun Feb 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.1.5-alt2_2jpp5
- fixed build

* Sat Jan 24 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.1.5-alt1_2jpp5
- restored in separate package due to repolib

