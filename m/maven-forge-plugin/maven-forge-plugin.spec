BuildRequires: maven-plugin-tools maven-shared-plugin-tools-api maven-shared-plugin-tools-beanshell maven-shared-plugin-tools-java
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


Name:           maven-forge-plugin
Version:        1.0.0
Release:        alt3_1jpp6
Epoch:          0
Summary:        Terracotta Forge Maven plugin
License:        Terracotta Public License
Group:          Development/Java
URL:            http://www.terracotta.org/
Source0:        %{name}-%{version}.tgz
# svn export http://svn.terracotta.org/svn/forge/projects/maven-forge-plugin/tags/release-1.0.0/ maven-forge-plugin-1.0.0
# tar czf maven-forge-plugin-1.0.0.tgz maven-forge-plugin-1.0.0/
Source1:        %{name}-%{version}-jpp-depmap.xml
Source2:        %{name}-%{version}-settings.xml
##

BuildArch:      noarch

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant >= 0:1.7
BuildRequires: apache-commons-parent
BuildRequires: maven2-common-poms
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven2-plugin-ant
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-source
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-release
BuildRequires: maven-shared-plugin-testing-harness
BuildRequires: subversion


Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0
Source44: import.info

%description
Terracotta Forge maven plugin.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
cp %{SOURCE2} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export M2_SETTINGS=$(pwd)/settings.xml
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $M2_SETTINGS \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
	-Dmaven.test.skip=true \
        install javadoc:javadoc

%install
# jars/poms
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

%add_to_maven_depmap org.terracotta %{name} %{version} JPP %{name}
install -m 644 pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-%{name}.pom
install -m 644 target/%{name}-%{version}.jar \
               $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* \
                    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files 
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt3_1jpp6
- fixed build with maven3

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt2_1jpp6
- rebuild to restore plexus components info

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_1jpp6
- new version

