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


Name:           aries-parent
Summary:        Apache Aries Parent
Url:            http://aries.apache.org
Version:        0.3
Release:        alt1_1jpp6
Epoch:          1
License:        Apache 2.0 License
Group:          Development/Java
Source0:        aries-parent-0.3.tgz
# svn export https://svn.apache.org/repos/asf/aries/trunk/parent/ aries-parent-0.3

Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  maven2 >= 0:2.0.8
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-enforcer
BuildRequires:  maven2-plugin-idea
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven2-plugin-pmd
BuildRequires:  maven2-plugin-release
BuildRequires:  maven2-plugin-remote-resources
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  mojo-maven2-plugin-findbugs
BuildRequires:  mojo-maven2-plugin-properties
BuildRequires:  apache-commons-parent
BuildRequires:  ant-contrib
BuildRequires:  maven-plugin-bundle
BuildRequires:  apache-jar-resource-bundle

Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5

BuildArch:      noarch
Source44: import.info

%description
Apache Aries Parent.

%prep
%setup -q 
chmod -R go=u-w *
cp %{SOURCE1} settings.xml

%build
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export SETTINGS=$(pwd)/settings.xml

mvn-jpp \
        -e \
        -s $SETTINGS \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -DobrRepository=NONE \
        install 

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/aries
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

%add_to_maven_depmap org.apache.aries parent %{version} JPP/aries parent
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.aries-parent.pom

%add_to_maven_depmap org.apache.aries default-parent %{version} JPP/aries default-parent
install -m 644 default-parent/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.aries-default-parent.pom

%add_to_maven_depmap org.apache.aries java5-parent %{version} JPP/aries java5-parent
install -m 644 default-parent/java5-parent/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.aries-java5-parent.pom

%add_to_maven_depmap org.apache.aries java6-parent %{version} JPP/aries java6-parent
install -m 644 default-parent/java6-parent/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.aries-java6-parent.pom

%files
%dir %{_javadir}/aries
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%changelog
* Thu Feb 09 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.3-alt1_1jpp6
- new version

