BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2011, JPackage Project
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


Name:           jetty-build-support
Summary:        Jetty 7 build support
Url:            http://www.eclipse.org/jetty/
Version:        1.0
Release:        alt1_1jpp6
Epoch:          0
License:        Apache Software License 2.0
Group:          Development/Java
Source0:        jetty-build-support-1.0.tgz
# svn export http://dev.eclipse.org/svnroot/rt/org.eclipse.jetty/jetty-toolchain/tags/jetty-build-support-1.0/
# tar czf jetty-build-support-1.0.tgz jetty-build-support-1.0/

Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        jetty-toolchain-1.3.pom
# get it from http://dev.eclipse.org/svnroot/rt/org.eclipse.jetty/jetty-toolchain/tags/jetty-toolchain-1.3/pom.xml
Source4:        jetty-parent-15.pom

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-enforcer
BuildRequires: maven2-plugin-idea
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-release
BuildRequires: maven2-plugin-remote-resources
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: apache-commons-parent

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

BuildArch:      noarch
Source44: import.info

%description
Build Support for Jetty (Contains Enforcer Rules, PMD 
Rulesets, etc ...)

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
chmod -R go=u-w *
cp %{SOURCE1} settings.xml

%build
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL/org/eclipse/jetty/toolchain/jetty-toolchain/1.3/
cp %{SOURCE3} $MAVEN_REPO_LOCAL/org/eclipse/jetty/toolchain/jetty-toolchain/1.3/jetty-toolchain-1.3.pom
mkdir -p $MAVEN_REPO_LOCAL/org/eclipse/jetty/jetty-parent/15/
cp %{SOURCE4} $MAVEN_REPO_LOCAL/org/eclipse/jetty/jetty-parent/15/jetty-parent-15.pom

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export SETTINGS=$(pwd)/settings.xml

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $SETTINGS \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

%add_to_maven_depmap org.eclipse.jetty jetty-parent 15 JPP jetty-parent
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jetty-parent.pom

%add_to_maven_depmap org.eclipse.jetty.toolchain jetty-toolchain 1.3 JPP jetty-toolchain
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jetty-toolchain.pom

%add_to_maven_depmap org.eclipse.jetty.toolchain %{name} %{version} JPP %{name}
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
install -m 644 target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/*

%changelog
* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp6
- new jpp release

