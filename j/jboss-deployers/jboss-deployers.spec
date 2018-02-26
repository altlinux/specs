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

%define repodir %{_javadir}/repository.jboss.com/jboss/jboss-deployers/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define reltag GA
%define namedversion %{version}.%{reltag}

Name:           jboss-deployers
Version:        2.0.7
Release:	alt1_4jpp6
Epoch:          0
Summary:        JBoss Deployers
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn export http://anonsvn.jboss.org/repos/jbossas/projects/jboss-deployers/tags/2.0.7.GA/ jboss-deployers-2.0.7
Source0:        jboss-deployers-2.0.7.tar.gz
Source1:        jboss-deployers-jpp-depmap.xml
Source2:        jboss-deployers-settings.xml
Source3:        jboss-deployers-component-info.xml
Source9:        jboss-test-1.1.4.jar
Patch0:         jboss-deployers-pom.patch

BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-release
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: ant-junit
BuildRequires: jboss-aop2
BuildRequires: jboss-common-logging-log4j
BuildRequires: jboss-test
BuildRequires: junit

BuildRequires: javassist
BuildRequires: jboss-cl
BuildRequires: jboss-common-core
BuildRequires: jboss-common-logging-spi
BuildRequires: jboss-integration
BuildRequires: jboss-man
BuildRequires: jboss-mdr
BuildRequires: jboss-microcontainer2
BuildRequires: jboss-parent
BuildRequires: jboss-vfs2
BuildRequires: jbossxb2
BuildRequires: stax_1_0_api

Requires: javassist
Requires: jboss-cl
Requires: jboss-common-core
Requires: jboss-common-logging-spi
Requires: jboss-integration
Requires: jboss-man
Requires: jboss-mdr
Requires: jboss-microcontainer2
Requires: jboss-vfs2
Requires: jbossxb2
Requires: stax_1_0_api

%description
JBoss deployers.

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
%patch0 -b .sav0

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

mvn-jpp -e \
        -s ${M2SETTINGS} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
install:install-file -DgroupId=org.jboss.test -DartifactId=jboss-test -Dversion=1.1.1.GA -Dpackaging=jar -Dfile=%{SOURCE9}


mvn-jpp -e \
        -s ${M2SETTINGS} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install 

mvn-jpp -e \
        -s ${M2SETTINGS} \
        -Daggregate=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        javadoc:javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
%add_to_maven_depmap org.jboss.deployers %{name} %{namedversion} JPP/%{name} %{name}
install -m 644 deployers-client-spi/target/jboss-deployers-client-spi.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-client-spi-%{version}.jar
%add_to_maven_depmap org.jboss.deployers jboss-deployers-client-spi %{namedversion} JPP/%{name} jboss-deployers-client-spi
install -m 644 deployers-client/target/jboss-deployers-client.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-client-%{version}.jar
%add_to_maven_depmap org.jboss.deployers jboss-deployers-client %{namedversion} JPP/%{name} jboss-deployers-client
install -m 644 deployers-client/target/jboss-deployers-client-tests.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-client-tests-%{version}.jar
%add_to_maven_depmap org.jboss.deployers jboss-deployers-client-tests %{namedversion} JPP/%{name} jboss-deployers-client-tests
install -m 644 deployers-core-spi/target/jboss-deployers-core-spi.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-core-spi-%{version}.jar
%add_to_maven_depmap org.jboss.deployers jboss-deployers-core-spi %{namedversion} JPP/%{name} jboss-deployers-core-spi
install -m 644 deployers-core/target/jboss-deployers-core.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-core-%{version}.jar
%add_to_maven_depmap org.jboss.deployers jboss-deployers-core %{namedversion} JPP/%{name} jboss-deployers-core
install -m 644 deployers-core/target/jboss-deployers-core-tests.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-core-tests-%{version}.jar
%add_to_maven_depmap org.jboss.deployers jboss-deployers-core-tests %{namedversion} JPP/%{name} jboss-deployers-core-tests
install -m 644 deployers-impl/target/jboss-deployers-impl.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-impl-%{version}.jar
%add_to_maven_depmap org.jboss.deployers jboss-deployers-impl %{namedversion} JPP/%{name} jboss-deployers-impl
install -m 644 deployers-impl/target/jboss-deployers-impl-tests.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-impl-tests-%{version}.jar
%add_to_maven_depmap org.jboss.deployers jboss-deployers-impl-tests %{namedversion} JPP/%{name} jboss-deployers-impl-tests
install -m 644 deployers-spi/target/jboss-deployers-spi.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-spi-%{version}.jar
%add_to_maven_depmap org.jboss.deployers jboss-deployers-spi %{namedversion} JPP/%{name} jboss-deployers-spi
install -m 644 deployers-structure-spi/target/jboss-deployers-structure-spi.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-structure-spi-%{version}.jar
%add_to_maven_depmap org.jboss.deployers jboss-deployers-structure-spi %{namedversion} JPP/%{name} jboss-deployers-structure-spi
install -m 644 deployers-structure-spi/target/jboss-deployers-structure-spi-tests.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-structure-spi-tests-%{version}.jar
%add_to_maven_depmap org.jboss.deployers jboss-deployers-structure-spi-tests %{namedversion} JPP/%{name} jboss-deployers-structure-spi-tests
install -m 644 deployers-vfs-spi/target/jboss-deployers-vfs-spi.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-vfs-spi-%{version}.jar
%add_to_maven_depmap org.jboss.deployers jboss-deployers-vfs-spi %{namedversion} JPP/%{name} jboss-deployers-vfs-spi
install -m 644 deployers-vfs/target/jboss-deployers-vfs.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-vfs-%{version}.jar
%add_to_maven_depmap org.jboss.deployers jboss-deployers-vfs %{namedversion} JPP/%{name} jboss-deployers-vfs
install -m 644 deployers-vfs/target/jboss-deployers-vfs-tests.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-vfs-tests-%{version}.jar
%add_to_maven_depmap org.jboss.deployers jboss-deployers-vfs-tests %{namedversion} JPP/%{name} jboss-deployers-vfs-tests

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom
install -m 644 deployers-client-spi/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployers-client-spi.pom
install -m 644 deployers-client/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployers-client.pom
install -m 644 deployers-core-spi/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployers-core-spi.pom
install -m 644 deployers-core/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployers-core.pom
install -m 644 deployers-impl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployers-impl.pom
install -m 644 deployers-spi/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployers-spi.pom
install -m 644 deployers-structure-spi/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployers-structure-spi.pom
install -m 644 deployers-vfs-spi/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployers-vfs-spi.pom
install -m 644 deployers-vfs/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployers-vfs.pom

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
install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-vfs.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-deployers-vfs.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-vfs-spi.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-deployers-vfs-spi.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-spi.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-deployers-spi.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-structure-spi.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-deployers-structure-spi.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-client-spi.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-deployers-client-spi.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-core-spi.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-deployers-core-spi.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-core.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-deployers-core.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-client.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-deployers-client.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployers-impl.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-deployers-impl.jar
%endif

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/jboss-deployers-vfs-%{version}.jar
%{_javadir}/%{name}/jboss-deployers-vfs.jar
%{_javadir}/%{name}/jboss-deployers-vfs-spi-%{version}.jar
%{_javadir}/%{name}/jboss-deployers-vfs-spi.jar
%{_javadir}/%{name}/jboss-deployers-spi-%{version}.jar
%{_javadir}/%{name}/jboss-deployers-spi.jar
%{_javadir}/%{name}/jboss-deployers-structure-spi-%{version}.jar
%{_javadir}/%{name}/jboss-deployers-structure-spi.jar
%{_javadir}/%{name}/jboss-deployers-client-spi-%{version}.jar
%{_javadir}/%{name}/jboss-deployers-client-spi.jar
%{_javadir}/%{name}/jboss-deployers-core-spi-%{version}.jar
%{_javadir}/%{name}/jboss-deployers-core-spi.jar
%{_javadir}/%{name}/jboss-deployers-core-%{version}.jar
%{_javadir}/%{name}/jboss-deployers-core.jar
%{_javadir}/%{name}/jboss-deployers-client-%{version}.jar
%{_javadir}/%{name}/jboss-deployers-client.jar
%{_javadir}/%{name}/jboss-deployers-impl-%{version}.jar
%{_javadir}/%{name}/jboss-deployers-impl.jar
%{_javadir}/%{name}/jboss-deployers-client-tests-%{version}.jar
%{_javadir}/%{name}/jboss-deployers-client-tests.jar
%{_javadir}/%{name}/jboss-deployers-core-tests-%{version}.jar
%{_javadir}/%{name}/jboss-deployers-core-tests.jar
%{_javadir}/%{name}/jboss-deployers-impl-tests-%{version}.jar
%{_javadir}/%{name}/jboss-deployers-impl-tests.jar
%{_javadir}/%{name}/jboss-deployers-structure-spi-tests-%{version}.jar
%{_javadir}/%{name}/jboss-deployers-structure-spi-tests.jar
%{_javadir}/%{name}/jboss-deployers-vfs-tests-%{version}.jar
%{_javadir}/%{name}/jboss-deployers-vfs-tests.jar
%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployers-client-spi.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployers-client.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployers-core-spi.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployers-core.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployers-impl.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployers-spi.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployers-structure-spi.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployers-vfs-spi.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-deployers-vfs.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.7-alt1_4jpp6
- new version

