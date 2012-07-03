Patch33: alt-maven3.patch
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 3.0.0
%define name spring-build-aws-maven
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}


%define upstream_tag .RELEASE
%define upstream_version %{version}%{?upstream_tag}

Name:           spring-build-aws-maven
Summary:        Spring Build Aws Maven
Version:        3.0.0
Release:        alt2_1jpp6
Epoch:          0
License:        ASL 2.0
Group:          Development/Java
URL:            http://www.springframework.org/
# git clone git://git.springsource.org/spring-build/aws-maven.git
# mkdir spring-build-aws-maven-3.0.0.RELEASE
# cd aws-maven
# git archive 3.0.0.RELEASE | tar -x -C ../spring-build-aws-maven-3.0.0.RELEASE
# cd ..
# tar czf ../SOURCES/spring-build-aws-maven-3.0.0.RELEASE.tgz spring-build-aws-maven-3.0.0.RELEASE/

Source0:        %{name}-%{upstream_version}.tgz
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Patch0:         %{name}-SimpleStorageServiceWagon.patch

BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7
BuildRequires:  apache-commons-parent >= 0:12
BuildRequires:  maven2 >= 0:2.0.8
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-resources

BuildRequires:  jets3t
BuildRequires:  maven-wagon
BuildRequires:  apache-commons-httpclient

Requires:  apache-commons-httpclient
Requires:  jets3t
Requires:  maven-wagon

Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Source44: import.info


%description
Spring is a layered Java/J2EE application framework, 
based on code published in Expert One-on-One J2EE 
Design and Development by Rod Johnson (Wrox, 2002). 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
Requires:       %{name}-javadoc = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description manual
%{summary}.

%package devel
Summary:        Source jars for %{name}
Group:          Development/Java

%description devel
%{summary}.

%prep
%setup -q -n %{name}-%{upstream_version}
chmod -R go=u-w *
%patch0 -b .sav0

%patch33

cp -p %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}

export MAVEN_SETTINGS=$(pwd)/settings.xml

cd org.springframework.build.aws.maven/
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s ${MAVEN_SETTINGS} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        install javadoc:javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/spring-build

install -m 644 org.springframework.build.aws.maven/target/org.springframework.build.aws.maven-3.0.0.RELEASE.jar \
               $RPM_BUILD_ROOT%{_javadir}/spring-build/org.springframework.build.aws.maven-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir}/spring-build && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

%add_to_maven_depmap org.springframework.build.aws org.springframework.build.aws.maven %{upstream_version} JPP/spring-build org.springframework.build.aws.maven

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 org.springframework.build.aws.maven/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.spring-build-org.springframework.build.aws.maven.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr org.springframework.build.aws.maven/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%dir %{_javadir}/spring-build
%{_javadir}/spring-build/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.0-alt2_1jpp6
- fixed build with maven3

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.0-alt1_1jpp6
- new release

