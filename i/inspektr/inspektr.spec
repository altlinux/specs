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


Summary:        Non-Intruisive Auditing and Logging 
Name:           inspektr
Version:        0.6.1
Release:        alt2_1jpp5
Epoch:          0
Group:          Development/Java
License:        Apache Software License 2.0
URL:            http://code.google.com/p/inspektr/
Source0:        inspektr-0.6.1.tar.gz
# svn export http://inspektr.googlecode.com/svn/tags/inspektr-0-6-1/ inspektr-0.6.1

Source1:        %{name}-jpp-depmap.xml
Source2:        %{name}-settings.xml

Patch0:         inspektr-core-pom.patch
Patch1:         inspektr-core-testContext.patch
Patch2:         inspektr-core-log4j.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: junit
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin

BuildRequires: excalibur-avalon-framework
BuildRequires: servlet_2_4_api
BuildRequires: spring2-beans
BuildRequires: spring2-jdbc
BuildRequires: spring2-test
BuildRequires: spring2-webmvc

Requires: excalibur-avalon-framework
Requires: servlet_2_4_api
Requires: spring2-beans
Requires: spring2-jdbc
Requires: spring2-webmvc

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%description
The Inspektr project allows for non-intrusive auditing and 
logging by using annotations and aspects.
It also includes a generic Grails-based web application to 
view statistics and audit logs stored in various data 
sources.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}

%description javadoc
%{summary}.

%prep
%setup -q 

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2

# alt; aspectj 1.5.4
sed -i 's,<groupId>aspectj</groupId>,<groupId>org.aspectj</groupId>,' inspektr-core/pom.xml

%build
cp %{SOURCE2} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        -Dmaven.test.failure.ignore=true \
        install javadoc:javadoc

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.inspektr inspektr %{version} JPP %{name}

install -m 644 inspektr-core/target/inspektr-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-core-%{version}.jar
install -m 644 inspektr-core/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-core.pom
%add_to_maven_depmap org.inspektr inspektr-core %{version} JPP %{name}-core

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)


# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core
cp -pr inspektr-core/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Sun Jan 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.6.1-alt2_1jpp5
- adapted for new aspectj

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.6.1-alt1_1jpp5
- first build

