Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define namedversion 5.0.3.GA

Name:           jboss-naming
Version:        5.0.3
Release:	alt1_3jpp6
Epoch:          0
Summary:        JBoss Naming
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
Source0:        jboss-naming-5.0.3.tar.gz
# svn export http://anonsvn.jboss.org/repos/jbossas/projects/naming/tags/5.0.3.GA/ jboss-naming-5.0.3
Source1:        jboss-naming-jpp-depmap.xml
Source2:        jboss-naming-settings.xml
Source3:        http://repository.jboss.org/maven2/org/jboss/jboss-parent/4/jboss-parent-4.pom
Source9:        jboss-test-1.1.4.jar

BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-antrun
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
BuildRequires: maven-surefire-provider-junit
BuildRequires: mojo-maven2-plugin-rmic
BuildRequires: jboss-microcontainer2
BuildRequires: jboss-parent
BuildRequires: jboss-test
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: jboss-common-core
BuildRequires: jboss-common-logging-spi

Requires: jboss-common-core
Requires: jboss-common-logging-spi

%description
JBoss Naming.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
mkdir -p jnpclient/src/main/java
touch jnpclient/src/main/java/No.java

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
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository
mkdir -p $MAVEN_REPO_LOCAL/org.jboss.jbossas/
# FIXME: (dwalluck): shoud depend on external package
ln -s $MAVEN_REPO_LOCAL/org/jboss/jbossas/jboss-as-j2se/%{namedversion}/jboss-as-j2se-%{namedversion}-tests.jar $MAVEN_REPO_LOCAL/org.jboss.jbossas/jboss-as-j2se-tests.jar

%{_bindir}/mvn-jpp -e \
        -s ${M2SETTINGS} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
install:install-file -DgroupId=org.jboss.test -DartifactId=jboss-test -Dversion=1.1.1.GA -Dpackaging=jar -Dfile=%{SOURCE9}


%{_bindir}/mvn-jpp -e \
        -s ${M2SETTINGS} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install 

%{_bindir}/mvn-jpp -e \
        -s ${M2SETTINGS} \
        -Daggregate=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        javadoc:javadoc 

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 jnpclient/target/jnp-client-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jnp-client-%{version}.jar
%add_to_maven_depmap org.jboss.naming jnp-client %{namedversion} JPP/%{name} jnp-client
install -m 644 jnpserver/target/jnpserver-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jnpserver-%{version}.jar
%add_to_maven_depmap org.jboss.naming jnpserver %{namedversion} JPP/%{name} jnpserver

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%add_to_maven_depmap org.jboss.naming jboss-naming-build %{namedversion} JPP/%{name} build
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-build.pom
install -m 644 jnpclient/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jnp-client.pom
install -m 644 jnpserver/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jnpserver.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -rf target/site/apidocs/* \
                  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/jnp-client-%{version}.jar
%{_javadir}/%{name}/jnp-client.jar
%{_javadir}/%{name}/jnpserver-%{version}.jar
%{_javadir}/%{name}/jnpserver.jar
%{_datadir}/maven2/poms/JPP.jboss-naming-build.pom
%{_datadir}/maven2/poms/JPP.jboss-naming-jnp-client.pom
%{_datadir}/maven2/poms/JPP.jboss-naming-jnpserver.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0.3-alt1_3jpp6
- new version

