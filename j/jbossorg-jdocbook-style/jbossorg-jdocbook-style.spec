Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat jboss-parent3
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


Name:           jbossorg-jdocbook-style
Version:        1.1.0
Release:        alt2_1jpp5
Epoch:          0
Summary:        JBoss.org Documentation Styles
License:        LGPL
Url:            http://www.jboss.org/
Group:          Development/Java
Source0:        jbossorg-jdocbook-style-1.1.0.tar.gz
# svn export http://anonsvn.jboss.org/repos/jbossas/tags/JBossOrg_jDocBook_Style_1_1_0_GA/ jbossorg-jdocbook-style-1.1.0

Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        jboss-parent-3.pom
## get it from http://anonsvn.jboss.org/repos/labs/labs/jbossbuild/jboss-parent/tags/jboss-parent-3/pom.xml

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven-jdocbook-style-plugin

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5


BuildArch:      noarch

%description
The JDocBook styles for the JBoss.org Documentation.

%prep
%setup -q 
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

cp %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml

%build
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
mkdir -p $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/
cp %{SOURCE3} $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/org.jboss-jboss-parent.pom

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

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

%add_to_maven_depmap org.jboss %{name} %{version} JPP %{name}
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
install -m 644 target/%{name}-%{version}.jar \
           $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%changelog
* Thu Sep 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt2_1jpp5
- fixed build with new maven 2.0.8

* Mon Jun 15 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_1jpp5
- new version

