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

Summary:        Webapp Test Tool
Name:           openqa-selenium-core
Version:        1.0.1
Release:        alt1_2jpp6
Epoch:          0
License:        Apache Software License 2.0
URL:            http://www.openqa.org/selenium-core/
Group:          Development/Java
Source0:        selenium-core-1.0.1.tar.gz
# svn export http://svn.openqa.org/svn/selenium-core/tags/REL-1.0.1/ selenium-core-1.0.1
Source1:        selenium-core-jpp-depmap.xml
Source2:        selenium-core-settings.xml
Source3:        selenium-core-generated-sources.tar.gz
Patch0:         selenium-core-pom.patch

BuildRequires: jpackage-utils >= 0:1.7.3

BuildRequires: maven2 >= 2.0.7
BuildRequires: maven2-plugin-ant
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-clean
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-release
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-maven-plugin
BuildRequires: jsunit
BuildRequires: junit
BuildRequires: subversion

BuildRequires: ant-trax
BuildRequires: excalibur-avalon-framework
BuildRequires: bouncycastle
BuildRequires: jakarta-commons-logging
BuildRequires: jetty5
BuildRequires: jline
BuildRequires: openqa-selenium-rc-server-coreless >= 0:1.0.1
BuildRequires: rhino16
BuildRequires: servlet_2_4_api

Requires: junit
Requires: openqa-selenium-rc-server-coreless
Requires: rhino16
Requires: jline

Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildArch:      noarch
Source44: import.info

%description
Selenium Core is a test tool for web applications. Selenium
Core tests run directly in a browser, just as realusers do. 
and they run in Internet Explorer, Mozilla and Firefox on 
Windows, Linux and Macintosh. No other test tool covers 
such a wide array of platforms.

%prep
%setup -q -n selenium-core-%{version}
gzip -dc %{SOURCE3} | tar xf -
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .sav0

#ln -sf $(build-classpath js16) src/main/resources/doctool/js.jar
#rm src/main/resources/doctool/js.jar.no
cp %{SOURCE2} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

%build

export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
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
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        -Dmaven.dependency.rhino.js.jar.path=$(build-classpath js16) \
        install || cat target/generated-resources/core/iedoc.xml

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/selenium-core-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/selenium-core-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-selenium-core.pom
%add_to_maven_depmap org.openqa.selenium.core selenium-core %{version} JPP selenium-core
%add_to_maven_depmap org.seleniumhq.selenium.core selenium-core %{version} JPP selenium-core

%files
%doc license/selenium_license.txt
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}

%changelog
* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_2jpp6
- new version

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt0.1jpp
- bootstrap

