# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
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

%global     short_name      logkit
%global     camelcase_short_name      LogKit

Name:        avalon-%{short_name}
Version:     2.1
Release:     alt2_24jpp8
Epoch:       0
Summary:     Java logging toolkit
License:     ASL 2.0
Group:       Development/Other
URL:         http://avalon.apache.org/%{short_name}/
Source0:     http://archive.apache.org/dist/excalibur/%{name}/source/%{name}-%{version}-src.zip
Source1:     http://repo1.maven.org/maven2/avalon-logkit/avalon-logkit/%{version}/%{name}-%{version}.pom
Patch0:      fix-java6-compile.patch
Patch1:      avalon-logkit-pom-deps.patch
Patch2:      avalon-logkit-encoding.patch
Patch3:      java7.patch
Requires:    avalon-framework >= 0:4.1.4
Requires:    glassfish-servlet-api
Requires:    geronimo-jms
Requires:    javamail

BuildRequires:    javapackages-local
BuildRequires:    ant
BuildRequires:    javamail
BuildRequires:    ant-junit
BuildRequires:    log4j
BuildRequires:    avalon-framework >= 0:4.1.4
# Required for converting jars to OSGi bundles
BuildRequires:    aqute-bnd
BuildRequires:    glassfish-servlet-api
BuildRequires:    geronimo-jms

BuildArch:    noarch
Source44: import.info


%description
LogKit is a logging toolkit designed for secure performance orientated
logging in applications. To get started using LogKit, it is recomended
that you read the whitepaper and browse the API docs.

%package javadoc
Summary:    Javadoc for %{name}
Group:        Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch0

cp %{SOURCE1} pom.xml
%patch1
%patch2 -p1
%patch3
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

# LogFactor5 is no longer distributed with log4j
rm -rf src/java/org/apache/log/output/lf5

%build
export CLASSPATH=$(build-classpath log4j javamail/mailapi jms glassfish-servlet-api jdbc-stdext avalon-framework junit):$PWD/build/classes
ant -Dencoding=ISO-8859-1 -Dnoget=true clean jar javadoc
# Convert to OSGi bundle
bnd wrap target/%{name}-%{version}.jar

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT/%{_mavenpomdir}

install -m 644 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "%{short_name}:%{short_name},org.apache.avalon.logkit:%{name}"

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_24jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_22jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_13jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_12jpp7
- new release

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_11jpp7
- added avalon:avalon-logkit depmap

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_11jpp7
- new release

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_4jpp5
- selected java5 compiler explicitly

* Sat Jan 24 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp5
- restored in separate package due to repolib

