BuildRequires: rome
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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

%define gcj_support 0

%define oname activemq

Name:           activemq4
Summary:        ActiveMQ Message Broker
Url:            http://activemq.apache.org/
Version:        4.1.2
Release:        alt8_2jpp6
Epoch:          0
License:        Apache Software License 2.0
Group:          Development/Java
Source0:        activemq-4.1.2.tar.gz
# svn export http://svn.apache.org/repos/asf/activemq/tags/activemq-4.1.2/

Source1:        activemq4-settings.xml
Source2:        activemq4-jpp-depmap.xml
#Source3:        apache-jar-resource-bundle-1.3.jar

Patch0:         activemq4-pom.patch
Patch1:         activemq4-optional-HttpClientTransport.patch
Patch2:         activemq4-web-console-pom.patch
Patch3:         activemq4-web-pom.patch
Patch4:         activemq4-xmpp-pom.patch


BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  junit
BuildRequires:  maven2 >= 0:2.0.8
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-eclipse
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven2-plugin-rar
BuildRequires:  maven2-plugin-remote-resources
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-shade
BuildRequires:  maven2-plugin-stage
BuildRequires:  maven2-plugin-war
#BuildRequires:  maven-jaxb2-plugin
BuildRequires:  maven-release
BuildRequires:  maven-shared-downloader
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit
#BuildRequires:  mvn-anno-mojo
BuildRequires:  mojo-maven2-plugin-build-helper
BuildRequires:  mojo-maven2-plugin-exec
BuildRequires:  mojo-maven2-plugin-javacc
BuildRequires:  mojo-maven2-plugin-rat
BuildRequires:  maven-plugin-bundle
BuildRequires:  javacc3
BuildRequires:  jetty6-maven2-plugins
BuildRequires:  geronimo-genesis
BuildRequires:  geronimo-genesis2
BuildRequires:  apache-jar-resource-bundle

BuildRequires:  apacheds-base
BuildRequires:  apacheds-shared-ldap
# = directory-shared:ldap-common:jar:0.9.2
BuildRequires:  apacheds10-protocol-ldap
# = directory-protocols:ldap-protocol:jar:0.9.2
BuildRequires:  apacheds10-core-shared
# = directory:apacheds-shared:jar:0.9.2
BuildRequires:  apacheds10-protocol-kerberos
# = directory-protocols:kerberos-protocol:jar:0.5
BuildRequires:  asn1
# = directory-asn1:asn1-codec:jar:0.3.2
# = directory-asn1:asn1-der:jar:0.3.2
BuildRequires:  apacheds10-core
# = directory:apacheds-core:jar:0.9.2

BuildRequires:  activeio3
BuildRequires:  annogen
BuildRequires:  ant
BuildRequires:  aopalliance
BuildRequires:  atomikos-transactions-essentials
BuildRequires:  axis
BuildRequires:  backport-util-concurrent
BuildRequires:  derby
BuildRequires:  groovy15
BuildRequires:  groovy-module-gram
BuildRequires:  j2ee_connector_1_5_api
BuildRequires:  geronimo-j2ee-management-1.0-api
BuildRequires:  j2ee_management_1_0_api
BuildRequires:  jacc_1_0_api
BuildRequires:  jaf_1_1_api
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-httpclient
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-pool
BuildRequires:  apache-commons-primitives
BuildRequires:  jakarta-taglibs-standard
BuildRequires:  jdom
BuildRequires:  jetty6-core
BuildRequires:  jms_1_1_api
BuildRequires:  jrms
BuildRequires:  jta_1_0_1B_api
BuildRequires:  junit
BuildRequires:  log4j
BuildRequires:  mina11
BuildRequires:  mina11-filter-ssl
BuildRequires:  mx4j
BuildRequires:  qdox
BuildRequires:  rome
BuildRequires:  saxon7
BuildRequires:  geronimo-jaf-1.1-api
BuildRequires:  geronimo-jsp-2.1-api
BuildRequires:  servlet_2_5_api
BuildRequires:  sitemesh
BuildRequires:  slf4j
BuildRequires:  spring2-all
BuildRequires:  spring2-webmvc
BuildRequires:  smack2
BuildRequires:  stax_1_0_api
BuildRequires:  sun-jaxb-2.1-api
BuildRequires:  sun-jaxb-2.1-impl
BuildRequires:  wstx
BuildRequires:  xalan-j2
BuildRequires:  xbean
BuildRequires:  xmlbeans
BuildRequires:  xpp3-minimal
BuildRequires:  xstream

Requires:       activeio3
Requires:       backport-util-concurrent
Requires:       apache-commons-logging
Requires:       jms_1_1_api

%if %{gcj_support}
BuildRequires:    gnu-crypto
BuildRequires:          java-gcj-compat-devel
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info

%description
Apache ActiveMQ is a popular and powerful open source Message
Broker and Enterprise Integration Patterns provider.
Apache ActiveMQ is fast, supports many Cross Language Clients
and Protocols, comes with easy to use Enterprise Integration
Patterns and many advanced features while fully supporting
JMS 1.1 and J2EE 1.4. 

%package all
Summary:        All of %{name}
Group:          Development/Java
Requires:       %{name}-console = %{epoch}:%{version}-%{release}
Requires:       %{name}-optional = %{epoch}:%{version}-%{release}
Requires:       derby

%description all
%{summary}.

%package console
Summary:        Console from %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       apache-commons-pool
Requires:       jms_1_1_api
Requires:       mx4j
Requires:       spring2-all
Requires:       xbean

%description console
%{summary}.

%package jaas
Summary:        JAAS from %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       apache-commons-logging

%description jaas
%{summary}.

%package maven-plugins
Summary:        Maven2 Plugins from %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-console = %{epoch}:%{version}-%{release}
Requires:       activeio3
Requires:       backport-util-concurrent
Requires:       derby
Requires:       jms_1_1_api
Requires:       j2ee_management_1_0_api
Requires:       maven2

%description maven-plugins
%{summary}.

%package openwire-generator
Summary:        Openwire Generator from %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       ant
Requires:       annogen
Requires:       groovy-module-gram
Requires:       groovy15

%description openwire-generator
%{summary}.

%package optional
Summary:        Optional from %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       activeio3
Requires:       aopalliance
Requires:       axis
Requires:       apache-commons-collections
Requires:       apache-commons-httpclient
Requires:       apache-commons-pool
Requires:       jetty6-core
Requires:       junit
Requires:       log4j
Requires:       spring2-all
Requires:       xpp3
Requires:       xstream

%description optional
%{summary}.

%package ra
Summary:        Resource Adapter from %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       derby
Requires:       j2ee_connector_1_5_api
Requires:       j2ee_management_1_0_api
Requires:       log4j
Requires:       spring2-all
Requires:       xbean

%description ra
%{summary}.

%package web
Summary:        Web Module from %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jdom
Requires:       jetty6-core
Requires:       rome
Requires:       servlet_2_5_api
Requires:       xbean
Requires:       xpp3

%description web
%{summary}.

%package web-console
Summary:        Web Console from %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-console = %{epoch}:%{version}-%{release}
Requires:       %{name}-web = %{epoch}:%{version}-%{release}
Requires:       %{name}-xmpp = %{epoch}:%{version}-%{release}
Requires:       activeio3
Requires:       j2ee_management_1_0_api
Requires:       jacc_1_0_api
Requires:       jakarta-taglibs-standard
Requires:       jms_1_1_api
Requires:       jta_1_0_1B_api
Requires:       log4j
Requires:       servlet_2_5_api
Requires:       sitemesh
Requires:       slf4j
Requires:       spring2-all
Requires:       spring2-webmvc
Requires:       xbean
Requires:       xpp3
Requires:       xstream

%description web-console
%{summary}.

%package web-demo
Summary:        Web Demo from %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-web = %{epoch}:%{version}-%{release}
Requires:       activeio3
Requires:       jms_1_1_api
Requires:       jta_1_0_1B_api
Requires:       j2ee_management_1_0_api
Requires:       jacc_1_0_api
Requires:       spring2-all
Requires:       xbean
Requires:       xpp3
Requires:       xstream

%description web-demo
%{summary}.

%package xmpp
Summary:        XMPP Module from %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       activeio3
Requires:       jaf_1_1_api
Requires:       stax_1_0_api
Requires:       spring2-all
Requires:       smack2
Requires:       sun-jaxb-2.1-api
Requires:       sun-jaxb-2.1-impl
Requires:       wstx
Requires:       xstream

%description xmpp
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{oname}-%{version}
chmod -R go=u-w *
for f in $(find . -name "*.jar"); do
  mv $f $f.no
done
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
mkdir -p activemq-xmpp/target/generated-sources
# tests seem obsolete wrt apacheds
rm -rf activemq-jaas/src/test/
# needs older jmock
rm -f activemq-ra/src/test/java/org/apache/activemq/ra/ActiveMQAsfEndpointWorkerTest.java

cp %{SOURCE1} settings.xml

%build
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
#mkdir -p $MAVEN_REPO_LOCAL/org.apache
#cp %{SOURCE3} $MAVEN_REPO_LOCAL/org.apache/apache-jar-resource-bundle.jar

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export SETTINGS=$(pwd)/settings.xml
export MAVEN_OPTS="-Xmx256M"


mvn-jpp \
        -e \
        -s $SETTINGS \
        -Dtest=false \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install:install-file -DgroupId=rome -DartifactId=rome \
        -Dversion=0.8 -Dpackaging=jar -Dfile=$(build-classpath rome-0.9)
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $SETTINGS \
        -Dtest=false \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -DfailIfNoTests=false \
        install

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $SETTINGS \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        javadoc:aggregate

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms


install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache.activemq activemq-parent %{version} JPP %{name}

install -m 644 %{oname}-all/target/%{oname}-all-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-all-%{version}.jar
install -m 644 %{oname}-all/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-all.pom
%add_to_maven_depmap org.apache.activemq activemq-all %{version} JPP %{name}-all

install -m 644 %{oname}-console/target/%{oname}-console-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/console-%{version}.jar
install -m 644 %{oname}-console/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-console.pom
%add_to_maven_depmap org.apache.activemq activemq-console %{version} JPP/%{name} console

install -m 644 %{oname}-core/target/%{oname}-core-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/core-%{version}.jar
install -m 644 %{oname}-core/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-core.pom
%add_to_maven_depmap org.apache.activemq activemq-core %{version} JPP/%{name} core

install -m 644 %{oname}-jaas/target/%{oname}-jaas-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/jaas-%{version}.jar
install -m 644 %{oname}-jaas/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jaas.pom
%add_to_maven_depmap org.apache.activemq activemq-jaas %{version} JPP/%{name} jaas

install -m 644 %{oname}-jmdns_1.0/target/%{oname}-jmdns_1.0-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/jmdns_1.0-%{version}.jar
install -m 644 %{oname}-jmdns_1.0/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jmdns_1.0.pom
%add_to_maven_depmap org.apache.activemq activemq-jmdns_1.0 %{version} JPP/%{name} jmdns_1.0

install -m 644 %{oname}-openwire-generator/target/%{oname}-openwire-generator-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/openwire-generator-%{version}.jar
install -m 644 %{oname}-openwire-generator/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-openwire-generator.pom
%add_to_maven_depmap org.apache.activemq activemq-openwire-generator %{version} JPP/%{name} openwire-generator

install -m 644 %{oname}-optional/target/%{oname}-optional-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/optional-%{version}.jar
install -m 644 %{oname}-optional/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-optional.pom
%add_to_maven_depmap org.apache.activemq activemq-optional %{version} JPP/%{name} optional

install -m 644 %{oname}-ra/target/%{oname}-ra-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/ra-%{version}.jar
install -m 644 %{oname}-ra/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-ra.pom
%add_to_maven_depmap org.apache.activemq activemq-ra %{version} JPP/%{name} ra

install -m 644 %{oname}-run/target/%{oname}-run-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/run-%{version}.jar
install -m 644 %{oname}-run/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-run.pom
%add_to_maven_depmap org.apache.activemq activemq-run %{version} JPP/%{name} run

install -m 644 %{oname}-web/target/%{oname}-web-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/web-%{version}.jar
install -m 644 %{oname}-web/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-web.pom
%add_to_maven_depmap org.apache.activemq activemq-web %{version} JPP/%{name} web

install -m 644 %{oname}-xmpp/target/%{oname}-xmpp-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/xmpp-%{version}.jar
install -m 644 %{oname}-xmpp/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-xmpp.pom
%add_to_maven_depmap org.apache.activemq activemq-xmpp %{version} JPP/%{name} xmpp

install -m 644 %{oname}-rar/target/%{oname}-rar-%{version}.rar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/rar-%{version}.rar
install -m 644 %{oname}-rar/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-rar.pom
%add_to_maven_depmap org.apache.activemq activemq-rar %{version} JPP/%{name} rar

install -m 644 %{oname}-web-console/target/%{oname}-web-console-%{version}.war \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/web-console-%{version}.war
install -m 644 %{oname}-web-console/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-web-console.pom
%add_to_maven_depmap org.apache.activemq activemq-web-console %{version} JPP/%{name} web-console

install -m 644 %{oname}-web-demo/target/%{oname}-web-demo-%{version}.war \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/web-demo-%{version}.war
install -m 644 %{oname}-web-demo/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-web-demo.pom
%add_to_maven_depmap org.apache.activemq activemq-web-demo %{version} JPP/%{name} web-demo

install -m 644 %{oname}-tooling/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-tooling.pom
%add_to_maven_depmap org.apache.activemq activemq-tooling %{version} JPP/%{name} tooling

install -m 644 %{oname}-tooling/maven-activemq-memtest-plugin/target/maven-activemq-memtest-plugin-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/maven-activemq-memtest-plugin-%{version}.jar
install -m 644 %{oname}-tooling/maven-activemq-memtest-plugin/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-maven-activemq-memtest-plugin.pom
%add_to_maven_depmap org.apache.activemq.tooling maven-activemq-memtest-plugin %{version} JPP/%{name} maven-activemq-memtest-plugin

install -m 644 %{oname}-tooling/maven-activemq-perf-plugin/target/maven-activemq-perf-plugin-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/maven-activemq-perf-plugin-%{version}.jar
install -m 644 %{oname}-tooling/maven-activemq-perf-plugin/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-maven-activemq-perf-plugin.pom
%add_to_maven_depmap org.apache.activemq.tooling maven-activemq-perf-plugin %{version} JPP/%{name} maven-activemq-perf-plugin

install -m 644 %{oname}-tooling/maven-activemq-plugin/target/maven-activemq-plugin-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}/maven-activemq-plugin-%{version}.jar
install -m 644 %{oname}-tooling/maven-activemq-plugin/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-maven-activemq-plugin.pom
%add_to_maven_depmap org.apache.activemq.tooling maven-activemq-plugin %{version} JPP/%{name} maven-activemq-plugin

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/plugins
pushd $RPM_BUILD_ROOT%{_datadir}/maven2/plugins
ln -sf %{_javadir}/%{name}/maven-activemq-memtest-plugin.jar
ln -sf %{_javadir}/%{name}/maven-activemq-perf-plugin.jar
ln -sf %{_javadir}/%{name}/maven-activemq-plugin.jar
popd

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for r in *-%{version}.rar; do ln -sf ${r} `echo $r| sed  "s|-%{version}\.rar|.jar|g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for w in *-%{version}.war; do ln -sf ${w} `echo $w| sed  "s|-%{version}\.war|.jar|g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/core*.jar
%{_javadir}/%{name}/jmdns*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files all
%{_javadir}/%{name}*.jar

%files console
%{_javadir}/%{name}/console*.jar
%{_javadir}/%{name}/run*.jar

%files jaas
%{_javadir}/%{name}/jaas*.jar

%files maven-plugins
%{_javadir}/%{name}/maven*.jar
%{_datadir}/maven2/plugins/*.jar

%files openwire-generator
%{_javadir}/%{name}/openwire*.jar

%files optional
%{_javadir}/%{name}/optional*.jar

%files ra
%{_javadir}/%{name}/ra*.jar
%{_javadir}/%{name}/*.rar

%files web
%{_javadir}/%{name}/web*.jar

%files xmpp
%{_javadir}/%{name}/xmpp*.jar

%files web-console
%{_javadir}/%{name}/web-console*

%files web-demo
%{_javadir}/%{name}/web-demo*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.1.2-alt8_2jpp6
- dropped maven-jaxb2-plugin dependency

* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.1.2-alt7_2jpp6
- dropped felix-maven2 dependency

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.1.2-alt6_2jpp6
- build w/java6

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.1.2-alt5_2jpp6
- fixed build

* Fri Mar 18 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.1.2-alt5_1jpp5
- fixed build with new javacc5

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.1.2-alt4_1jpp5
- fixed build: use maven2-plugin-shade

* Wed Jan 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.1.2-alt3_1jpp5
- build with new commons primitives

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.1.2-alt2_1jpp5
- fixed build with new maven 2.0.8

* Sun Mar 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.1.2-alt1_1jpp5
- new version

