BuildRequires: testng qdox
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

%define repodir %{_javadir}/repository.jboss.com/jboss/cache/jbosscache-core/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define reltag GA
%define namedversion %{version}.%{reltag}

Name:           jboss-cache-core
Version:        3.1.0
Release:        alt4_3jpp6
Epoch:          0
Summary:        JBoss Cache Core
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn -q export http://anonsvn.jboss.org/repos/jbosscache/core/tags/3.1.0.GA/ jboss-cache-core-3.1.0
Source0:        jboss-cache-core-3.1.0.tar.gz
Source1:        jboss-cache-core-jpp-depmap.xml
Source2:        jboss-cache-core-settings.xml
Source3:        http://repository.jboss.org/maven2/org/jboss/cache/jbosscache-common-parent/1.3/jbosscache-common-parent-1.3.pom
Source4:        http://repository.jboss.com/maven2/org/jboss/cache/jbosscache-support/1.3/jbosscache-support-1.3.pom
Source5:        jboss-cache-core-component-info.xml

BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-eclipse
BuildRequires: maven2-plugin-enforcer
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-release
BuildRequires: maven-shared-enforcer-rule-api
BuildRequires: maven-surefire-maven-plugin
BuildRequires: bsh2
BuildRequires: easymock2
BuildRequires: hsqldb
BuildRequires: jboss-parent
BuildRequires: jbossts
BuildRequires: noderunner-http
BuildRequires: servlet_2_5_api
BuildRequires: testng

BuildRequires: berkeleydb-je3
BuildRequires: c3p0
BuildRequires: derby
BuildRequires: jakarta-commons-logging
BuildRequires: jboss-common-core
BuildRequires: jcip-annotations
BuildRequires: jdbm
BuildRequires: jgroups
BuildRequires: jta_1_1_api
BuildRequires: noderunner-amazon-s3

Requires: jakarta-commons-logging
Requires: jboss-common-core
Requires: jgroups
Requires: jta_1_1_api

%description
JBoss cache core.

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
mkdir -p $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/
cp -p %{SOURCE3} $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/org.jboss.cache-jbosscache-common-parent.pom
cp -p %{SOURCE4} $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/org.jboss.cache-jbosscache-support.pom
install -Dm 644 %{SOURCE3} $MAVEN_REPO_LOCAL/org/jboss/cache/jbosscache-common-parent/1.5/jbosscache-common-parent-1.5.pom
install -Dm644 %{SOURCE4} $MAVEN_REPO_LOCAL/org/jboss/cache/jbosscache-support/1.3/jbosscache-support-1.3.pom

mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.test.skip=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
      install:install-file -DgroupId=org.testng -DartifactId=testng -Dversion=5.8 -Dclassifier=jdk15 -Dpackaging=jar -Dfile=$(build-classpath testng)


mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.test.skip=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/jbosscache-core.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
#install -m 644 target/jbosscache-core-tests.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tests-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jbosscache-core-%{version}.jar
#ln -s %{name}-tests-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jbosscache-core-tests-%{version}.jar
%add_to_maven_depmap org.jboss.cache jbosscache-core %{namedversion} JPP %{name}
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%add_to_maven_depmap org.jboss.cache jbosscache-common-parent 1.3 JPP jbosscache-common-parent
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jbosscache-common-parent.pom
%add_to_maven_depmap org.jboss.cache jbosscache-support 1.3 JPP jbosscache-support
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jbosscache-support.pom
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -rf target/site/apidocs/* \
                  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jbosscache-core-%{version}
ln -s jbosscache-core-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jbosscache-core

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}.%{reltag}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/jbosscache-core.jar
%endif

%files
%{_javadir}/jboss-cache-core-%{version}.jar
#%{_javadir}/jboss-cache-core-tests-%{version}.jar
#%{_javadir}/jboss-cache-core-tests.jar
%{_javadir}/jboss-cache-core.jar
%{_javadir}/jbosscache-core-%{version}.jar
#%{_javadir}/jbosscache-core-tests-%{version}.jar
#%{_javadir}/jbosscache-core-tests.jar
%{_javadir}/jbosscache-core.jar
%{_datadir}/maven2/poms/JPP-jboss-cache-core.pom
%{_datadir}/maven2/poms/JPP-jbosscache-common-parent.pom
%{_datadir}/maven2/poms/JPP-jbosscache-support.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{_javadocdir}/jbosscache-core-%{version}
%{_javadocdir}/jbosscache-core

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt4_3jpp6
- fixed build

* Sat Apr 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt3_3jpp6
- fixed build with new plexus-containers

* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt2_3jpp6
- fixed build with maven3

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt1_3jpp6
- new version

