BuildRequires: ant-optional maven-antrun-plugin
Patch33:	jackrabbit-1.5.7-alt-pom-javacc5.patch
Patch34:	jackrabbit-1.5.7-alt-pom-no-maven-one.patch
BuildRequires: mojo-parent
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


Name:           jackrabbit
Version:        1.5.7
Release:        alt7_2jpp6
Epoch:          0
Summary:        Apache Jackrabbit JCR Implementation
License:        Apache Software License 2.0
Url:            http://jackrabbit.apache.org/
Group:          Development/Java
Source0:        http://www.apache.org/dist/jackrabbit/source/jackrabbit-%{version}-src.jar

Source1:        jackrabbit-1.5.7-settings.xml
Source2:        jackrabbit-1.5.7-jpp-depmap.xml
Patch0:         jackrabbit-1.5.7-poms.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven2-default-skin
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-checkstyle
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-dependency
BuildRequires: maven2-plugin-eclipse
BuildRequires: maven2-plugin-idea
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-one
BuildRequires: maven2-plugin-pmd
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-rar
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven2-plugin-source
BuildRequires: maven2-plugin-war
BuildRequires: maven-model >= 0:3.0.2-4
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: mojo-maven2-plugin-build-helper
BuildRequires: mojo-maven2-plugin-javacc
BuildRequires: maven-plugin-bundle
BuildRequires: jetty6-maven2-plugins
BuildRequires: junit
BuildRequires: javacc3
BuildRequires: derby
BuildRequires: easymock
BuildRequires: fonts-ttf-liberation

BuildRequires: apache-commons-parent
BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-digester
BuildRequires: jakarta-commons-httpclient
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang
BuildRequires: cglib
BuildRequires: concurrent
BuildRequires: j2ee_connector_1_5_api
BuildRequires: apache-poi
BuildRequires: jcr_1_0_api
BuildRequires: jetty6
BuildRequires: geronimo-jsp-2.1-api
BuildRequires: jta_1_0_1B_api
BuildRequires: lucene24 >= 0:2.3.2
BuildRequires: pdfbox
BuildRequires: servlet_2_3_api
BuildRequires: geronimo-servlet-2.5-api
BuildRequires: slf4j
#BuildRequires:  xerces-j2

Requires: apache-commons-beanutils
Requires: apache-commons-collections
Requires: apache-commons-digester
Requires: jakarta-commons-httpclient
Requires: apache-commons-io
Requires: apache-commons-lang
Requires: cglib
Requires: concurrent
Requires: j2ee_connector_1_5_api
Requires: apache-poi
Requires: jcr_1_0_api
Requires: jta_1_0_1B_api
#Requires: lucene >= 0:2.3.2
Requires: pdfbox
Requires: servlet_2_3_api
Requires: servlet_2_5_api
Requires: slf4j
#Requires:       xerces-j2

BuildArch:      noarch

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info


%description
The Jackrabbit Project has been formed to develop an open source 
implementation of the Content Repository for Java Technology API 
(JCR), being specified within the Java Community Process as 
JSR-170. Day Software, the JSR-170 specification lead, 
has licensed an initial implementation of the JCR reference 
implementation for use as seed code for this project. JCR 
specifies an API for application developers (and application 
frameworks) to use for interaction with modern content 
repositories that provide content services such as searching, 
versioning, transactions, etc. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q 
# remove all binary libs
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%patch0 -b .sav0
%patch33
%patch34

sed -i -e s,qdox161,qdox,g ../../SOURCES/*-jpp-depmap.xml


%build
cp %{SOURCE1} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository
export MAVEN_OPTS="-Xmx512m"
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dproject.build.outputDirectory=target/classes \
        -Dproject.build.directory=target \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        install 
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dproject.build.outputDirectory=target/classes \
        -Dproject.build.directory=target \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        javadoc:javadoc


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 jackrabbit-api/target/jackrabbit-api-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/api-%{version}.jar
install -m 644 jackrabbit-api/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-api.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-api %{version} JPP/%{name} api

install -m 644 jackrabbit-classloader/target/jackrabbit-classloader-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/classloader-%{version}.jar
install -m 644 jackrabbit-classloader/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-classloader.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-classloader %{version} JPP/%{name} classloader

install -m 644 jackrabbit-core/target/jackrabbit-core-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/core-%{version}.jar
install -m 644 jackrabbit-core/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-core.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-core %{version} JPP/%{name} core

install -m 644 jackrabbit-jca/target/jackrabbit-jca-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jca-%{version}.jar
install -m 644 jackrabbit-jca/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-jca.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-jca %{version} JPP/%{name} jca

install -m 644 jackrabbit-jcr2spi/target/jackrabbit-jcr2spi-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jcr2spi-%{version}.jar
install -m 644 jackrabbit-jcr2spi/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-jcr2spi.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-jcr2spi %{version} JPP/%{name} jcr2spi

install -m 644 jackrabbit-jcr2spi/target/jackrabbit-jcr2spi-%{version}-tests.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jcr2spi-tests-%{version}.jar

install -m 644 jackrabbit-jcr-benchmark/target/jackrabbit-jcr-benchmark-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jcr-benchmark-%{version}.jar
install -m 644 jackrabbit-jcr-benchmark/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-jcr-benchmark.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-jcr-benchmark %{version} JPP/%{name} jcr-benchmark

install -m 644 jackrabbit-jcr-commons/target/jackrabbit-jcr-commons-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jcr-commons-%{version}.jar
install -m 644 jackrabbit-jcr-commons/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-jcr-commons.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-jcr-commons %{version} JPP/%{name} jcr-commons

install -m 644 jackrabbit-jcr-rmi/target/jackrabbit-jcr-rmi-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jcr-rmi-%{version}.jar
install -m 644 jackrabbit-jcr-rmi/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-jcr-rmi.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-jcr-rmi %{version} JPP/%{name} jcr-rmi

install -m 644 jackrabbit-jcr-server/target/jackrabbit-jcr-server-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jcr-server-%{version}.jar
install -m 644 jackrabbit-jcr-server/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-jcr-server.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-jcr-server %{version} JPP/%{name} jcr-server

install -m 644 jackrabbit-jcr-servlet/target/jackrabbit-jcr-servlet-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jcr-servlet-%{version}.jar
install -m 644 jackrabbit-jcr-servlet/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-jcr-servlet.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-jcr-servlet %{version} JPP/%{name} jcr-servlet

install -m 644 jackrabbit-jcr-tests/target/jackrabbit-jcr-tests-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jcr-tests-%{version}.jar
install -m 644 jackrabbit-jcr-tests/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-jcr-tests.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-jcr-tests %{version} JPP/%{name} jcr-tests

install -m 644 jackrabbit-ocm-nodemanagement/target/jackrabbit-ocm-nodemanagement-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/ocm-nodemanagement-%{version}.jar
install -m 644 jackrabbit-ocm-nodemanagement/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-ocm-nodemanagement.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-ocm-nodemanagement %{version} JPP/%{name} ocm-nodemanagement

install -m 644 jackrabbit-ocm/target/jackrabbit-ocm-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/ocm-%{version}.jar
install -m 644 jackrabbit-ocm/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-ocm.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-ocm %{version} JPP/%{name} ocm

install -m 644 jackrabbit-spi2jcr/target/jackrabbit-spi2jcr-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/spi2jcr-%{version}.jar
install -m 644 jackrabbit-spi2jcr/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-spi2jcr.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-spi2jcr %{version} JPP/%{name} spi2jcr

install -m 644 jackrabbit-spi-commons/target/jackrabbit-spi-commons-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/spi-commons-%{version}.jar
install -m 644 jackrabbit-spi-commons/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-spi-commons.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-spi-commons %{version} JPP/%{name} spi-commons

install -m 644 jackrabbit-spi/target/jackrabbit-spi-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/spi-%{version}.jar
install -m 644 jackrabbit-spi/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-spi.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-spi %{version} JPP/%{name} spi

install -m 644 jackrabbit-spi/target/jackrabbit-spi-%{version}-tests.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/spi-tests-%{version}.jar

install -m 644 jackrabbit-standalone/target/jackrabbit-standalone-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/standalone-%{version}.jar
install -m 644 jackrabbit-standalone/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-standalone.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-standalone %{version} JPP/%{name} standalone

install -m 644 jackrabbit-text-extractors/target/jackrabbit-text-extractors-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/text-extractors-%{version}.jar
install -m 644 jackrabbit-text-extractors/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-text-extractors.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-text-extractors %{version} JPP/%{name} text-extractors

install -m 644 jackrabbit-webapp/target/jackrabbit-webapp-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/webapp-%{version}.jar
install -m 644 jackrabbit-webapp/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-webapp.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-webapp %{version} JPP/%{name} webapp

install -m 644 jackrabbit-webdav/target/jackrabbit-webdav-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/webdav-%{version}.jar
install -m 644 jackrabbit-webdav/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-webdav.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-webdav %{version} JPP/%{name} webdav

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

install -m 644 pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-jackrabbit.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit %{version} JPP/%{name} jackrabbit

install -m 644 jackrabbit-parent/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jackrabbit-parent.pom
%add_to_maven_depmap org.apache.jackrabbit jackrabbit-parent %{version} JPP/%{name} parent

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
#cp -pr target/site/apidocs/* \
#    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
#rm -rf target/site/apidocs

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#cp -pr target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}


%files 
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/%{name}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

#files manual
#doc %{_docdir}/%{name}-%{version}

%changelog
* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.7-alt7_2jpp6
- dropped felix-maven2 dependency

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.7-alt6_2jpp6
- fixed build with maven3

* Sat Feb 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.7-alt5_2jpp6
- fixed build

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.7-alt4_2jpp6
- built with compat lucene24

* Fri Mar 18 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.7-alt3_2jpp6
- fixed build with new javacc5

* Sun Feb 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.7-alt2_2jpp6
- fixed build with new javacc3

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.7-alt1_2jpp6
- new version

