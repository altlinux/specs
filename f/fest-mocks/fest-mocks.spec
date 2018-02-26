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

%define module mocks

Name:           fest-%{module}
Version:        1.1.1
Release:        alt3_0.r1039.1jpp7
Summary:        Fixtures for Easy Software Testing Mocks

Group:          Development/Java
License:        Apache License, Version 2.0
URL:            http://fest.easytesting.org/
Source0:        fest-mocks-1.1.1-r1039.tgz
# svn export http://svn.codehaus.org/fest/trunk/fest-mocks fest-mocks-1.1.1
# tar czf fest-mocks-1.1.1-r1039.tgz fest-mocks-1.1.1
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        fest-1.0.1.pom
# See http://svn.codehaus.org/fest/trunk/fest/pom.xml
#Patch0:         fest-util-pom.patch

BuildRequires:  maven >= 0:2.0.8
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  fest-assembly
BuildRequires:  easymock-classextension2
BuildRequires:  cglib
Requires:  jpackage-utils >= 0:5.0.0
Requires:  easymock-classextension2
Requires:  cglib

Requires(post):    jpackage-utils >= 0:5.0.0
Requires(postun):  jpackage-utils >= 0:5.0.0

BuildArch:      noarch
Source44: import.info

%description
Utility methods used by FEST modules.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q

mkdir external_repo
ln -s %{_javadir} external_repo/JPP
cp -p %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml
mkdir -p .m2/repository/org/easytesting/fest/1.0.1/
cp %{SOURCE3} .m2/repository/org/easytesting/fest/1.0.1/fest-1.0.1.pom
jar xf $(build-classpath fest/assembly)
rm -rf META-INF
#%patch0 -b .sav

%build
export SETTINGS=$(pwd)/settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}
export MAVEN_OPTS="-Dmaven2.jpp.depmap.file=%{SOURCE2} -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -Dmaven.test.failure.ignore=true"
%{_bindir}/mvn-jpp \
        -e \
        -s ${SETTINGS} \
        install javadoc:javadoc


%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/fest

install -m 644 target/%{name}-%{version}.jar \
       $RPM_BUILD_ROOT%{_javadir}/fest/%{module}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/fest && for jar in *-%{version}*; do \
ln -s ${jar} ${jar/-%{version}/}; done)

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}.pom
%add_to_maven_depmap org.easytesting %{name} %{version} JPP/fest %{module}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc LICENSE.txt
%dir %{_javadir}/fest
%{_javadir}/fest/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}*

%changelog
* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_0.r1039.1jpp7
- fixed build with maven3

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3_0.r1039.1jpp6
- added maven2-plugin-resources dep

* Sun Jan 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_0.r1039.1jpp6
- fixed build

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_0.r1039.1jpp6
- new version

