BuildRequires: maven2-plugin-site
Packager: Igor Vlasenko <viy@altlinux.ru>
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


%define maven_skins_version 3
%define default_skin_version 1.1
%define classic_skin_version 1.1
%define stylus_skin_version 1.1
%define application_skin_version 1.0

Name:           maven2-skins
Version:        %{maven_skins_version}
Release:	alt2_3jpp5
Epoch:          0
Summary:        Maven Skins
License:        ASL 2.0
Group:          Development/Java
URL:            http://maven.apache.org/skins/
Source0:        maven2-skins-3-r526741.tar.gz
# svn export -r 526741 http://svn.apache.org/repos/asf/maven/skins/trunk/ maven2-skins-3-r526741
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml

Patch0:         maven2-skins-poms.patch


BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.4

BuildRequires: maven2-common-poms
BuildRequires: maven2
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-plugin

Requires: maven2

Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4

%description
The Maven Skins.

%package -n maven2-default-skin
Summary:        Maven Default Skin
Group:          Development/Java
Version:        %{default_skin_version}
Requires: %{name} = 0:%{maven_skins_version}-%{release}

%description -n maven2-default-skin
%{summary}.

%package -n maven2-classic-skin
Summary:        Maven Classic Skin
Group:          Development/Java
Version:        %{classic_skin_version}
Requires: %{name} = 0:%{maven_skins_version}-%{release}

%description -n maven2-classic-skin
%{summary}.

%package -n maven2-stylus-skin
Summary:        Maven Stylus Skin
Group:          Development/Java
Version:        %{stylus_skin_version}
Requires: %{name} = 0:%{maven_skins_version}-%{release}

%description -n maven2-stylus-skin
%{summary}.

%package -n maven2-application-skin
Summary:        Maven Application Skin
Group:          Development/Java
Version:        %{application_skin_version}
Requires: %{name} = 0:%{maven_skins_version}-%{release}

%description -n maven2-application-skin
%{summary}.

%prep
%setup -q -n %{name}-%{maven_skins_version}-r526741
cp %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
%patch0 -b .sav0

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/
cp pom.xml $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/org.apache.maven.skins-maven-skins.pom

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export M2_SETTINGS=$(pwd)/settings.xml
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $M2_SETTINGS \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install

%install
# jars/poms
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/maven2
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

%add_to_maven_depmap org.apache.maven.skins maven-skins %{maven_skins_version} JPP/maven2 maven-skins
install -m 644 pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.maven2-maven-skins.pom

install -m 0644 maven-default-skin/target/maven-default-skin-%{default_skin_version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven2/default-skin-%{default_skin_version}.jar
install -m 0644 maven-default-skin/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.maven2-default-skin.pom
%add_to_maven_depmap org.apache.maven.skins maven-default-skin %{default_skin_version} JPP/maven2 default-skin

install -m 0644 maven-classic-skin/target/maven-classic-skin-%{classic_skin_version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven2/classic-skin-%{classic_skin_version}.jar
install -m 0644 maven-classic-skin/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.maven2-classic-skin.pom
%add_to_maven_depmap org.apache.maven.skins maven-classic-skin %{classic_skin_version} JPP/maven2 classic-skin

install -m 0644 maven-stylus-skin/target/maven-stylus-skin-%{stylus_skin_version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven2/stylus-skin-%{stylus_skin_version}.jar
install -m 0644 maven-stylus-skin/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.maven2-stylus-skin.pom
%add_to_maven_depmap org.apache.maven.skins maven-stylus-skin %{stylus_skin_version} JPP/maven2 stylus-skin

install -m 0644 maven-application-skin/target/maven-application-skin-%{application_skin_version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven2/application-skin-%{application_skin_version}.jar
install -m 0644 maven-application-skin/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.maven2-application-skin.pom
%add_to_maven_depmap org.apache.maven.skins maven-application-skin %{application_skin_version} JPP/maven2 application-skin

pushd $RPM_BUILD_ROOT%{_javadir}/maven2
   ln -fs default-skin-%{default_skin_version}.jar default-skin.jar
   ln -fs classic-skin-%{classic_skin_version}.jar classic-skin.jar
   ln -fs stylus-skin-%{stylus_skin_version}.jar stylus-skin.jar
   ln -fs application-skin-%{application_skin_version}.jar application-skin.jar
popd

%files
%{_datadir}/maven2/*
%{_mavendepmapfragdir}/*

%files -n maven2-default-skin
%{_javadir}/maven2/default-skin*.jar

%files -n maven2-classic-skin
%{_javadir}/maven2/classic-skin*.jar

%files -n maven2-stylus-skin
%{_javadir}/maven2/stylus-skin*.jar

%files -n maven2-application-skin
%{_javadir}/maven2/application-skin*.jar

%changelog
* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:3-alt2_3jpp5
- fixed build

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:3-alt1_3jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3-alt1_2jpp5
- converted from JPackage by jppimport script

* Sat Jul 05 2008 Igor Vlasenko <viy@altlinux.ru> 0:3-alt1_1jpp5
- converted from JPackage by jppimport script

