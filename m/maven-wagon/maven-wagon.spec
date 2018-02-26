# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2007, JPackage Project
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

%global bname     wagon

Name:           maven-%{bname}
Version:        1.0
Release:        alt9_3jpp7
Epoch:          0
Summary:        Tools to manage artifacts and deployment
License:        ASL 2.0
Group:          Development/Java
URL:            http://maven.apache.org/wagon
Source0:        http://repo1.maven.org/maven2/org/apache/maven/wagon/wagon/%{version}/wagon-%{version}-source-release.zip

Source1:        wagon-1.0-jpp-depmap.xml
Patch1:         disable-tck.patch
Patch2:         %{name}-migration-to-component-metadata.patch

BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  ant >= 0:1.6
BuildRequires:  junit
BuildRequires:  maven
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-project-info-reports-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-enforcer-plugin
#BuildRequires:  maven2-default-skin
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  maven-scm-test
BuildRequires:  xerces-j2
BuildRequires:  classworlds
BuildRequires:  nekohtml
BuildRequires:  ganymed-ssh2
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-net
BuildRequires:  jakarta-commons-httpclient
BuildRequires:  apache-commons-logging
#BuildRequires:  jakarta-slide-webdavclient
BuildRequires:  jsch
BuildRequires:  jtidy
BuildRequires:  plexus-container-default
BuildRequires:  plexus-interactivity
BuildRequires:  plexus-utils
BuildRequires:  servletapi5
BuildRequires:  xml-commons-apis
BuildRequires:  easymock
BuildRequires:  jsoup

Requires:       ganymed-ssh2
Requires:       jakarta-commons-httpclient
Requires:       apache-commons-net
#Requires:       jakarta-slide-webdavclient
Requires:       jsch
Requires:       jtidy
Requires:       jsoup
Requires:       plexus-interactivity
Requires:       plexus-utils
Requires:       xml-commons-apis
Requires:       nekohtml
Requires:       xerces-j2
Source44: import.info

%description
Maven Wagon is a transport abstraction that is used in Maven's
artifact and repository handling code. Currently wagon has the
following providers:
* File
* HTTP
* FTP
* SSH/SCP
* WebDAV (in progress)

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
Documents for %{name}.

%prep
%setup -q -n wagon-%{version}

#FIXME: have to drop wagon-webdav-jackrabbit until jackrabbit is available
sed -i "s|<module>wagon-webdav-jackrabbit</module>|<!-- <module>wagon-webdav-jackrabbit</module> -->|" wagon-providers/pom.xml

%patch1
%patch2 -p1

# To wire out jetty, plexus-avalon-personality and plexus-ftpd requirement
rm -f wagon-providers/wagon-ftp/src/test/java/org/apache/maven/wagon/providers/ftp/FtpWagonTest.java
rm -f wagon-providers/wagon-http-lightweight/src/test/java/org/apache/maven/wagon/providers/http/LightweightHttpWagonGzipTest.java
rm -f wagon-providers/wagon-http/src/test/java/org/apache/maven/wagon/providers/http/HttpWagonGzipTest.java
rm -f wagon-provider-test/src/main/java/org/apache/maven/wagon/http/HttpWagonTestCase.java

%build
mvn-rpmbuild \
        -e \
        -Dmaven.local.depmap.file=%{SOURCE1} \
        -Dmaven.test.skip=true \
        install javadoc:aggregate

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

install -m 644 \
  wagon-provider-api/target/wagon-provider-api-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/provider-api.jar
%add_to_maven_depmap org.apache.maven.wagon wagon-provider-api %{version} JPP/%{name} provider-api

install -m 644 \
  wagon-providers/wagon-file/target/wagon-file-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/file.jar
%add_to_maven_depmap org.apache.maven.wagon wagon-file %{version} JPP/%{name} file

install -m 644 \
  wagon-providers/wagon-ftp/target/wagon-ftp-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/ftp.jar
%add_to_maven_depmap org.apache.maven.wagon wagon-ftp %{version} JPP/%{name} ftp

install -m 644 \
  wagon-providers/wagon-http/target/wagon-http-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/http.jar

%add_to_maven_depmap org.apache.maven.wagon wagon-http %{version} JPP/%{name} http

install -m 644 \
  wagon-providers/wagon-http-lightweight/target/wagon-http-lightweight-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/http-lightweight.jar
%add_to_maven_depmap org.apache.maven.wagon wagon-http-lightweight %{version} JPP/%{name} http-lightweight

install -m 644 \
  wagon-providers/wagon-http-shared/target/wagon-http-shared-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/http-shared.jar
%add_to_maven_depmap org.apache.maven.wagon wagon-http-shared %{version} JPP/%{name} http-shared

install -m 644 \
  wagon-providers/wagon-scm/target/wagon-scm-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/scm.jar
%add_to_maven_depmap org.apache.maven.wagon wagon-scm %{version} JPP/%{name} scm

install -m 644 \
  wagon-providers/wagon-ssh/target/wagon-ssh-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/ssh.jar
%add_to_maven_depmap org.apache.maven.wagon wagon-ssh %{version} JPP/%{name} ssh

install -m 644 \
  wagon-providers/wagon-ssh-common/target/wagon-ssh-common-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/ssh-common.jar
%add_to_maven_depmap org.apache.maven.wagon wagon-ssh-common %{version} JPP/%{name} ssh-common

install -m 644 \
  wagon-providers/wagon-ssh-common-test/target/wagon-ssh-common-test-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/ssh-common-test.jar
%add_to_maven_depmap org.apache.maven.wagon wagon-ssh-common-test %{version} JPP/%{name} ssh-common-test

install -m 644 \
  wagon-providers/wagon-ssh-external/target/wagon-ssh-external-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/ssh-external.jar
%add_to_maven_depmap org.apache.maven.wagon wagon-ssh-external %{version} JPP/%{name} ssh-external

#Until webdav is available, map it to an empty dep
#install -m 644 \
#  wagon-providers/wagon-webdav-jackrabbit/target/wagon-webdav-jackrabbit-%{version}-%{blevel}.jar \
#  $RPM_BUILD_ROOT%{_javadir}/%{name}/web-jackrabbit-%{version}.jar
#%%add_to_maven_depmap org.apache.maven.wagon wagon-webdav-jackrabbit %{version} JPP/%{name} webdav-jackrabbit

#install -m 644 \
#  wagon-providers/wagon-webdav/target/wagon-webdav-%{version}-%{blevel}.jar \
#  $RPM_BUILD_ROOT%{_javadir}/%{name}/webdav-%{version}.jar
#%%add_to_maven_depmap org.apache.maven.wagon wagon-webdav %{version} JPP/%{name} webdav

install -m 644 \
  wagon-provider-test/target/wagon-provider-test-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/provider-test.jar
%add_to_maven_depmap org.apache.maven.wagon wagon-provider-test %{version} JPP/%{name} provider-test

%add_to_maven_depmap org.apache.maven.wagon wagon %{version} JPP/%{name} wagon
%add_to_maven_depmap org.apache.maven.wagon wagon-providers %{version} JPP/%{name} providers

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-wagon-wagon.pom
install -m 644 wagon-provider-api/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-wagon-provider-api.pom
install -m 644 wagon-provider-test/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-wagon-provider-test.pom
install -m 644 wagon-providers/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-wagon-providers.pom
install -m 644 wagon-providers/wagon-file/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-wagon-file.pom
install -m 644 wagon-providers/wagon-ftp/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-wagon-ftp.pom
install -m 644 wagon-providers/wagon-http-shared/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-wagon-http-shared.pom
install -m 644 wagon-providers/wagon-http-lightweight/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-wagon-http-lightweight.pom
install -m 644 wagon-providers/wagon-http/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-wagon-http.pom
install -m 644 wagon-providers/wagon-scm/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-wagon-scm.pom
install -m 644 wagon-providers/wagon-ssh-common/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-wagon-ssh-common.pom
install -m 644 wagon-providers/wagon-ssh-common-test/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-wagon-ssh-common-test.pom
install -m 644 wagon-providers/wagon-ssh-external/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-wagon-ssh-external.pom
install -m 644 wagon-providers/wagon-ssh/pom.xml \
    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-wagon-ssh.pom
#install -m 644 wagon-providers/wagon-webdav/pom.xml \
#    $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-wagon-webdav.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#install -m 644 wagon-provider-api/LICENSE.txt \
#                $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%{_javadir}/*
%{_mavenpomdir}/*.pom
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt9_3jpp7
- complete build

* Sun Mar 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt8jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

