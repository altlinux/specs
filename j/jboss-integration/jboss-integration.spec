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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/jboss/integration/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define reltag GA
%define namedversion %{version}.%{reltag}

Name:           jboss-integration
Version:        5.1.0
Release:	alt2_4jpp6
Epoch:          0
Summary:        JBoss Integration
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
Source0:        jboss-integration-5.1.0.tar.gz
# svn export http://anonsvn.jboss.org/repos/jbossas/projects/integration/tags/5.1.0.GA/ jboss-integration-5.1.0
Source1:        jboss-integration-jpp-depmap.xml
Source2:        jboss-integration-settings.xml
Source3:        jboss-integration-component-info.xml
Source4:        jboss-profileservice-spi-component-info.xml
BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-release
BuildRequires: maven-surefire-maven-plugin

BuildRequires: gnu-trove
BuildRequires: jboss-jca-1.5-api
BuildRequires: jacorb
BuildRequires: jboss-aop2
BuildRequires: jboss-common-core
BuildRequires: jboss-common-logging-spi
BuildRequires: jboss-man
BuildRequires: jboss-microcontainer2
BuildRequires: jboss-parent
BuildRequires: jboss-vfs2
BuildRequires: jboss-transaction-1.0.1-api

Requires: gnu-trove
Requires: jboss-jca-1.5-api
Requires: jacorb
Requires: jboss-aop2
Requires: jboss-common-core
Requires: jboss-common-logging-spi
Requires: jboss-man
Requires: jboss-microcontainer2
Requires: jboss-vfs2
Requires: jboss-transaction-1.0.1-api

%description
JBoss integration.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q 

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
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install

mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Daggregate=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        javadoc:javadoc


%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

%add_to_maven_depmap org.jboss.integration %{name}-parent %{namedversion} JPP/%{name} %{name}-parent

install -m 644 build/target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-%{version}.jar
%add_to_maven_depmap org.jboss.integration %{name} %{namedversion} JPP/%{name} %{name}

install -m 644 jboss-classloading-spi/target/jboss-classloading-spi-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-classloading-spi-%{version}.jar
%add_to_maven_depmap org.jboss.integration jboss-classloading-spi %{namedversion} JPP/%{name} jboss-classloading-spi
install -m 644 jboss-corba-ots-spi/target/jboss-corba-ots-spi-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-corba-ots-spi-%{version}.jar
%add_to_maven_depmap org.jboss.integration jboss-corba-ots-spi %{namedversion} JPP/%{name} jboss-corba-ots-spi
install -m 644 jboss-deployment-spi/target/jboss-deployment-spi-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployment-spi-%{version}.jar
%add_to_maven_depmap org.jboss.integration jboss-deployment-spi %{namedversion} JPP/%{name} jboss-deployment-spi
install -m 644 jboss-jca-spi/target/jboss-jca-spi-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-jca-spi-%{version}.jar
%add_to_maven_depmap org.jboss.integration jboss-jca-spi %{namedversion} JPP/%{name} jboss-jca-spi
install -m 644 jboss-profileservice-spi/target/jboss-profileservice-spi-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-profileservice-spi-%{version}.jar
%add_to_maven_depmap org.jboss.integration jboss-profileservice-spi %{namedversion} JPP/%{name} jboss-profileservice-spi
install -m 644 jboss-transaction-spi/target/jboss-transaction-spi-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-transaction-spi-%{version}.jar
%add_to_maven_depmap org.jboss.integration jboss-transaction-spi %{namedversion} JPP/%{name} jboss-transaction-spi

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-parent.pom
install -m 644 build/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom
install -m 644 jboss-classloading-spi/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-classloading-spi.pom
install -m 644 jboss-corba-ots-spi/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-corba-ots-spi.pom
install -m 644 jboss-deployment-spi/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployment-spi.pom
install -m 644 jboss-jca-spi/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-jca-spi.pom
install -m 644 jboss-profileservice-spi/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-profileservice-spi.pom
install -m 644 jboss-transaction-spi/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-transaction-spi.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -rf target/site/apidocs/* \
                  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}.%{reltag}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-classloading-spi.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-classloading-spi.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-integration.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-integration.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-corba-ots-spi.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-corba-ots-spi.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployment-spi.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-deployment-spi.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-jca-spi.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-jca-spi.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-transaction-spi.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-transaction-spi.jar
%define repodir %{_javadir}/repository.jboss.com/jboss/profileservice-spi/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}.%{reltag}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-profileservice-spi.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-profileservice-spi.jar
%endif

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/jboss-classloading-spi-%{version}.jar
%{_javadir}/%{name}/jboss-classloading-spi.jar
%{_javadir}/%{name}/jboss-integration-%{version}.jar
%{_javadir}/%{name}/jboss-integration.jar
%{_javadir}/%{name}/jboss-corba-ots-spi-%{version}.jar
%{_javadir}/%{name}/jboss-corba-ots-spi.jar
%{_javadir}/%{name}/jboss-deployment-spi-%{version}.jar
%{_javadir}/%{name}/jboss-deployment-spi.jar
%{_javadir}/%{name}/jboss-jca-spi-%{version}.jar
%{_javadir}/%{name}/jboss-jca-spi.jar
%{_javadir}/%{name}/jboss-profileservice-spi-%{version}.jar
%{_javadir}/%{name}/jboss-profileservice-spi.jar
%{_javadir}/%{name}/jboss-transaction-spi-%{version}.jar
%{_javadir}/%{name}/jboss-transaction-spi.jar
%{_datadir}/maven2/poms/JPP.%{name}-%{name}-parent.pom
%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-classloading-spi.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-corba-ots-spi.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployment-spi.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-jca-spi.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-profileservice-spi.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-transaction-spi.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.1.0-alt2_4jpp6
- built with patched assembly plugin

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.1.0-alt1_4jpp6
- new version

