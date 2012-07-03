BuildRequires: oss-parent
Patch32: selenium-rc-alt-maven3.patch
BuildRequires: mojo-parent gmaven-runtime-1.5 gmaven-runtime-1.6 gmaven-runtime-1.7
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
#define _with_bootstrap2 1

%define gcj_support 0

%define with_bootstrap %{!?_with_bootstrap:0}%{?_with_bootstrap:1}
%define without_bootstrap %{?_with_bootstrap:0}%{!?_with_bootstrap:1}

%define with_bootstrap2 %{!?_with_bootstrap2:0}%{?_with_bootstrap2:1}
%define without_bootstrap2 %{?_with_bootstrap2:0}%{!?_with_bootstrap2:1}

Summary:        Selenium Remote Control
Name:           openqa-selenium-rc
Version:        1.0.1
Release:        alt5_5jpp6
Epoch:          0
License:        ASL 2.0
URL:            http://www.openqa.org/selenium-rc/
Group:          Development/Java
Source0:        selenium-rc-1.0.1.tar.gz
# svn export http://svn.openqa.org/svn/selenium-rc/tags/REL-1.0.1 selenium-rc-1.0.1
Source1:        selenium-rc-jpp-depmap.xml
Source2:        selenium-rc-settings.xml
Patch0:         selenium-rc-server-coreless-pom.patch
Patch1:         selenium-rc-clients-pom.patch
Patch2:         selenium-rc-bootstrap.patch
Patch3:         selenium-rc-bootstrap2.patch


BuildRequires: jpackage-utils >= 0:1.7.3

BuildRequires: maven2 >= 2.0.7
BuildRequires: maven2-plugin-ant
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-idea
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-release
BuildRequires: maven2-plugin-resources
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: junit44

BuildRequires: ant-trax
BuildRequires: bouncycastle
BuildRequires: cglib
BuildRequires: excalibur-avalon-framework
BuildRequires: jakarta-commons-logging
BuildRequires: jetty5
BuildRequires: servlet_2_4_api
BuildRequires: easymock2
BuildRequires: easymock-classextension2
BuildRequires: objenesis
BuildRequires: subversion

%if %{without_bootstrap}
BuildRequires: gmaven
BuildRequires: gmaven-runtime-1.5
BuildRequires: groovy15
BuildRequires: openqa-selenium-core
BuildRequires: qdox
BuildRequires: testng >= 0:5.8
%endif
%if %{without_bootstrap} && %{without_bootstrap2}
BuildRequires: openqa-selenium-ide
%endif

Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: bouncycastle
Requires: cglib
Requires: excalibur-avalon-framework
Requires: jakarta-commons-logging
Requires: servlet_2_4_api
Requires: objenesis

BuildArch:      noarch
Source44: import.info
Patch33: selenium-rc-gmaven13-alt.patch

%description
Selenium Remote Control is a test tool that allows you to 
write automated application UI tests in any programming 
language against any HTTP website using any mainstream 
JavaScript-enabled browser.
Selenium Remote Control provides a Selenium Server, which 
can automatically start/stop/control any supported browser.
It works by using Selenium Core, a pure-HTML+JS library that
performs automated tasks in JavaScript.

%package server-coreless
Summary:        Coreless Server Module from %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description server-coreless
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if %{without_bootstrap}
%package server
Summary:        Server Module from %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description server
%{summary}.


%package xlator
Summary:        Xlator Module from %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description xlator
%{summary}.

%package java-client-driver
Summary:        Java Client Driver Module from %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description java-client-driver
%{summary}.
%endif

%prep
%setup -q -n selenium-rc-%{version}
#%setup -q -n selenium-rc-%{version} -T -D -a 3
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
mv server-coreless/src/main/resources/customProfileDirCUSTFFCHROME/extensions/readystate@openqa.org/chrome/readystate.jar.no \
server-coreless/src/main/resources/customProfileDirCUSTFFCHROME/extensions/readystate@openqa.org/chrome/readystate.jar
cp %{SOURCE2} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml
%patch0 -b .sav0
#%patch1 -b .sav1
%if %{with_bootstrap}
%patch2 -b .sav2
%endif
%if %{with_bootstrap2}
%patch3 -b .sav3
%endif

sed -i -e s,DEREncodableVector,ASN1EncodableVector,g `grep -rl DEREncodableVector .`

#sed -i -e s,org.codehaus.groovy.maven,org.codehaus.gmaven, clients/java/pom.xml
#sed -i -e s,gmaven-runtime-default,gmaven-runtime-loader, clients/java/pom.xml
%patch33 -p1
%patch32

%build
export LANG=en_US.ISO8859-1
mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository

mkdir -p $MAVEN_REPO_LOCAL/bouncycastle
ln -sf $(build-classpath bcprov) $MAVEN_REPO_LOCAL/bouncycastle/bcprov-jdk15.jar
MAVEN_SETTINGS=$(pwd)/settings.xml
#mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
#        -e \
#        -s $MAVEN_SETTINGS \
#        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
#        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
#	install:install-file -DgroupId=org.codehaus.gmaven.runtime -DartifactId=gmaven-runtime -Dversion=1.0-rc-3 -Dpackaging=jar -Dfile=/usr/share/java/gmaven

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $MAVEN_SETTINGS \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
	install:install-file -DgroupId=bouncycastle -DartifactId=bcprov-jdk15 -Dversion=135 -Dpackaging=jar -Dfile=$(build-classpath bcprov)

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $MAVEN_SETTINGS \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
       install:install-file -DgroupId=org.testng -DartifactId=testng -Dversion=5.8 -Dclassifier=jdk15 -Dpackaging=jar -Dfile=$(build-classpath testng)


mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $MAVEN_SETTINGS \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.test.skip.exec=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 server-coreless/target/selenium-server-coreless-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/selenium-server-coreless-%{version}.jar
%if %{without_bootstrap}
install -m 644 selenium-server/target/selenium-server-%{version}-standalone.jar \
      $RPM_BUILD_ROOT%{_javadir}/selenium-server-standalone-%{version}.jar
install -m 644 selenium-server/target/selenium-server-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/selenium-server-%{version}.jar
install -m 644 clients/java/target/selenium-java-client-driver-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/selenium-java-client-driver-%{version}.jar
%if %{without_bootstrap2}
install -m 644 xlator/target/selenium-xlator-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/selenium-xlator-%{version}.jar
%endif
%endif
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-selenium-rc.pom
%add_to_maven_depmap org.openqa.selenium selenium-rc %{version} JPP selenium-rc
%add_to_maven_depmap org.seleniumhq.selenium selenium-rc %{version} JPP selenium-rc
install -m 644 server-coreless/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-selenium-server-coreless.pom
%add_to_maven_depmap org.openqa.selenium.server selenium-server-coreless %{version} JPP selenium-server-coreless
%add_to_maven_depmap org.seleniumhq.selenium.server selenium-server-coreless %{version} JPP selenium-server-coreless
%if %{without_bootstrap}
install -m 644 selenium-server/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-selenium-server.pom
%add_to_maven_depmap org.openqa.selenium.server selenium-server %{version} JPP selenium-server
%add_to_maven_depmap org.seleniumhq.selenium.server selenium-server %{version} JPP selenium-server
install -m 644 clients/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-selenium-client-drivers.pom
%add_to_maven_depmap org.openqa.selenium.client-drivers selenium-client-drivers %{version} JPP selenium-client-drivers
%add_to_maven_depmap org.seleniumhq.selenium.client-drivers selenium-client-drivers %{version} JPP selenium-client-drivers
install -m 644 clients/java/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-selenium-java-client-driver.pom
%add_to_maven_depmap org.openqa.selenium.client-drivers selenium-java-client-driver %{version} JPP selenium-java-client-driver
%add_to_maven_depmap org.seleniumhq.selenium.client-drivers selenium-java-client-driver %{version} JPP selenium-java-client-driver
install -m 644 xlator/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-selenium-xlator.pom
%add_to_maven_depmap org.openqa.selenium selenium-xlator %{version} JPP selenium-xlator
%add_to_maven_depmap org.seleniumhq.selenium selenium-xlator %{version} JPP selenium-xlator
%endif


# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/coreless
cp -pr server-coreless/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/coreless
%if %{without_bootstrap}
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/clients
%if %{without_bootstrap2}
cp -pr clients/java/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/clients
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/xlator
cp -pr xlator/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/xlator
%endif
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files 
%doc license/selenium_license.txt
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files server-coreless
%{_javadir}/selenium-server-coreless*.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %{without_bootstrap}
%files server
%{_javadir}/selenium-server-%{version}.jar
%{_javadir}/selenium-server.jar
%{_javadir}/selenium-server-standalone*.jar

%if %{without_bootstrap2}
%files xlator
%{_javadir}/selenium-xlator*.jar
%endif

%files java-client-driver
%{_javadir}/selenium-java-client-driver*.jar
%endif

%changelog
* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt5_5jpp6
- fixed build with new testng and xbean

* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt4_5jpp6
- fixed build with maven3

* Sat Feb 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt3_5jpp6
- fixed build

* Wed Sep 07 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt2_5jpp6
- fixed build w/new bouncycastle

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_5jpp6
- new version

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.2-alt1_1jpp
- bootstrap

