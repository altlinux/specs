BuildRequires: gmaven maven-plugin-descriptor
BuildRequires: mojo-parent
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


%define gcj_support %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_without_gcj_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gcj_support:0}}}

Summary:        Webapp Test IDE
Name:           openqa-selenium-ide
Version:        1.0.2
Release:        alt3_1jpp6
Epoch:          0
License:        Apache Software License 2.0
URL:            http://www.openqa.org/selenium-ide/
Group:          Development/Java
Source0:        selenium-ide-1.0.2.tar.gz
# svn export http://svn.openqa.org/svn/selenium-ide/tags/REL-1.0.2/src/ selenium-ide-1.0.2

Source1:        selenium-ide-jpp-depmap.xml
Source2:        selenium-ide-settings.xml
Patch0:         selenium-ide-pom.patch

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: maven2 >= 2.0.7
BuildRequires: maven2-plugin-ant
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-clean
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-release
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: mojo-maven2-plugin-build-helper
BuildRequires: junit44

BuildRequires: bouncycastle
BuildRequires: cglib21 < 0:2.2
BuildRequires: excalibur-avalon-framework
BuildRequires: jakarta-commons-logging
BuildRequires: jetty5
BuildRequires: openqa-selenium-core >= 0:1.0.1
BuildRequires: openqa-selenium-rc-server-coreless >= 0:1.0.1
BuildRequires: openqa-selenium-rc-java-client-driver >= 0:1.0.1
BuildRequires: servlet_2_4_api


Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildArch:      noarch
Source44: import.info

%description
Selenium IDE is an integrated development environment for 
Selenium tests. It is implemented as a Firefox extension, 
and allows you to record, edit, and debug tests. Selenium 
IDE includes the entire Selenium Core, allowing you to 
easily and quickly record and play back tests in the actual
environment that they will run.

%prep
%setup -q -n selenium-ide-%{version}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .sav0

cp %{SOURCE2} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL
mkdir -p $MAVEN_REPO_LOCAL/bouncycastle
ln -sf $(build-classpath bcprov) $MAVEN_REPO_LOCAL/bouncycastle/bcprov-jdk15.jar

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5 \
        -e \
        -s $(pwd)/settings.xml \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install:install-file -DgroupId=bouncycastle -DartifactId=bcprov-jdk15 -Dversion=135 -Dpackaging=jar -Dfile=$(build-classpath bcprov)

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        -Dskip-integration-test \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install


%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/selenium-ide-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/selenium-ide-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-selenium-ide.pom
%add_to_maven_depmap org.openqa.selenium.ide selenium-ide %{version} JPP selenium-ide
%add_to_maven_depmap org.seleniumhq.selenium.ide selenium-ide %{version} JPP selenium-ide

%files
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}

%changelog
* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt3_1jpp6
- fixed build with maven3

* Sat Feb 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_1jpp6
- fixed build

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_1jpp6
- new version

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt0.1jpp
- bootstrap

