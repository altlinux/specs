Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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

%define namedversion 2.0.3.SP1
%define oname jbosssx

Name:           jbosssx2
Version:        2.0.3.1
Release:	alt3_4jpp6
Epoch:          0
Summary:        JBoss SX
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn export http://anonsvn.jboss.org/repos/jbossas/projects/security/security-jboss-sx/tags/2.0.3.SP1/ jbosssx-2.0.3.1 && tar czf jbosssx-2.0.4.SP1.tar.gz jbosssx-2.0.4.SP1
Source0:        jbosssx-2.0.3.1.tar.gz
Source1:        jbosssx2-jpp-depmap.xml
Source2:        jbosssx2-settings.xml
Patch0:         jbosssx2-acl-pom.patch
Patch1:         jbosssx2-buildparentandjbosssx.patch
Patch2:         jbosssx2-buildall.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: dtdparser
Requires: hibernate3
Requires: hibernate3-entitymanager
Requires: jacc_1_0_api
Requires: jaspi_1_0_api
Requires: jaxb_2_1_api
Requires: jboss-common-logging-log4j
Requires: jboss-naming
Requires: jboss-security-spi
Requires: jboss-security-xacml
Requires: jbossxb2
Requires: jpa_3_0_api
Requires: stax_1_0_api
Requires: glassfish-jaxb
BuildRequires: ant-junit
BuildRequires: berkeleydb-je32
BuildRequires: dtdparser
BuildRequires: geronimo-jta-1.1-api
BuildRequires: glassfish-jaxb
BuildRequires: glassfish-persistence-1.0b-api
BuildRequires: hibernate3
BuildRequires: hibernate3-annotations
BuildRequires: hibernate3-entitymanager
BuildRequires: hsqldb
BuildRequires: jacc_1_0_api
BuildRequires: jaspi_1_0_api
BuildRequires: jaxb_2_1_api
BuildRequires: jboss4-jmx
BuildRequires: jboss-common-logging-log4j
BuildRequires: jboss-javaee
BuildRequires: jboss-microcontainer2
BuildRequires: jboss-naming
BuildRequires: jboss-parent
BuildRequires: jboss-profiler
BuildRequires: jboss-security-spi
BuildRequires: jboss-security-xacml
BuildRequires: jboss-test
BuildRequires: jbossxb2
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: junit
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-release
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-jboss-deploy-plugin
BuildRequires: mojo-maven2-plugin-javacc
BuildRequires: opends
BuildRequires: slf4j
BuildRequires: stax_1_0_api
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis
BuildArch:      noarch

%description
JBoss SX.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -b .sav0
%patch1 -b .sav1
mkdir -p jbosssx-client/src/main/java
touch jbosssx-client/src/main/java/No.java

cp -p %{SOURCE2} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%build
export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository

mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.test.skip \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
	install:install-file -DgroupId=javax.transaction -DartifactId=jta -Dversion=1.1 -Dpackaging=jar -Dfile=/usr/share/java/jta_1_1_api.jar

# To work around a problem with the javacc compiler, we first build
# jbosssx, move the generated sources, and then rebuild everything
mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.test.skip \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        -fn \
        install

%{__cp} -pr jbosssx/target/generated-sources/javacc/org/jboss/security/auth/login/* jbosssx/src/main/java/org/jboss/security/auth/login/

# Now build add
%{__patch} -p0 < %{PATCH2}

mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.test.skip \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install

mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Daggregate \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        javadoc:javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

%add_to_maven_depmap org.jboss.security jboss-security-acl-impl %{namedversion} JPP/%{name} jboss-security-acl-impl
install -m 644 acl/target/jboss-security-acl-impl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-security-acl-impl-%{namedversion}.jar
%add_to_maven_depmap org.jboss.security %{oname} %{namedversion} JPP/%{name} %{oname}
install -m 644 assembly/target/%{oname}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}-%{namedversion}.jar
%add_to_maven_depmap org.jboss.security identity-impl %{namedversion} JPP/%{name} identity-impl
install -m 644 identity/target/identity-impl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/identity-impl-%{namedversion}.jar
%add_to_maven_depmap org.jboss.security jbosssx-bridge-as4 %{namedversion} JPP/%{name} jbosssx-bridge-as4
install -m 644 jbosssx-bridge-as4/target/jbosssx-bridge-as4-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}-bridge-as4-%{namedversion}.jar
%add_to_maven_depmap org.jboss.security jbosssx-client %{namedversion} JPP/%{name} jbosssx-client
install -m 644 jbosssx-client/target/jbosssx-client-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}-client-%{namedversion}.jar
%add_to_maven_depmap org.jboss.security jbosssx-mc-int %{namedversion} JPP/%{name} jbosssx-mc-int
install -m 644 jbosssx-mc-int/target/jbosssx-mc-int.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jbosssx-mc-int-%{namedversion}.jar
%add_to_maven_depmap org.jboss.security jbosssx-bare %{namedversion} JPP/%{name} jbosssx-bare
install -m 644 jbosssx/target/jbosssx-bare.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jbosssx-bare-%{namedversion}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{namedversion}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{namedversion}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%add_to_maven_depmap org.jboss.security %{oname}-pom %{namedversion} JPP/%{name} %{oname}-pom
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{oname}-pom.pom
%add_to_maven_depmap org.jboss.security %{oname}-parent %{namedversion} JPP/%{name} %{oname}-parent
install -m 644 parent/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{oname}-parent.pom
install -m 644 acl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-security-acl-impl.pom
install -m 644 assembly/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{oname}.pom
install -m 644 identity/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-identity-impl.pom
install -m 644 jbosssx-bridge-as4/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jbosssx-bridge-as4.pom
install -m 644 jbosssx-client/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jbosssx-client.pom
install -m 644 jbosssx-mc-int/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jbosssx-mc-int.pom
install -m 644 jbosssx/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jbosssx-bare.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{namedversion}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{namedversion}
ln -s %{name}-%{namedversion} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/identity-impl-%{namedversion}.jar
%{_javadir}/%{name}/identity-impl.jar
%{_javadir}/%{name}/jboss-security-acl-impl-%{namedversion}.jar
%{_javadir}/%{name}/jboss-security-acl-impl.jar
%{_javadir}/%{name}/jbosssx-%{namedversion}.jar
%{_javadir}/%{name}/jbosssx-bare-%{namedversion}.jar
%{_javadir}/%{name}/jbosssx-bare.jar
%{_javadir}/%{name}/jbosssx-bridge-as4-%{namedversion}.jar
%{_javadir}/%{name}/jbosssx-bridge-as4.jar
%{_javadir}/%{name}/jbosssx-client-%{namedversion}.jar
%{_javadir}/%{name}/jbosssx-client.jar
%{_javadir}/%{name}/jbosssx-mc-int-%{namedversion}.jar
%{_javadir}/%{name}/jbosssx-mc-int.jar
%{_javadir}/%{name}/jbosssx.jar
%{_datadir}/maven2/poms/JPP.%{name}-identity-impl.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-security-acl-impl.pom
%{_datadir}/maven2/poms/JPP.%{name}-jbosssx-bare.pom
%{_datadir}/maven2/poms/JPP.%{name}-jbosssx-bridge-as4.pom
%{_datadir}/maven2/poms/JPP.%{name}-jbosssx-client.pom
%{_datadir}/maven2/poms/JPP.%{name}-jbosssx-mc-int.pom
%{_datadir}/maven2/poms/JPP.%{name}-jbosssx-parent.pom
%{_datadir}/maven2/poms/JPP.%{name}-jbosssx-pom.pom
%{_datadir}/maven2/poms/JPP.%{name}-jbosssx.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{namedversion}
%{_javadocdir}/%{name}

%changelog
* Wed Mar 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.3.1-alt3_4jpp6
- build w/java6

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.3.1-alt2_4jpp6
- fixed build with new jboss-test

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.3.1-alt1_4jpp6
- new version

