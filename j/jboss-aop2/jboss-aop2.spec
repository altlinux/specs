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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_with integration
%bcond_with jrockit
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/jboss/aop/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define oname jboss-aop
%define reltag GA
%define namedversion %{version}.%{reltag}

Name:           jboss-aop2
Version:        2.1.1
Release:        alt3_0jpp6
Epoch:          0
Summary:        JBoss AOP
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn -q export http://anonsvn.jboss.org/repos/jbossas/projects/aop/tags/JBoss_AOP_2_1_1_GA/ jboss-aop-2.1.1
Source0:        jboss-aop-2.1.1.tar.gz
Source1:        jboss-aop-jpp-depmap.xml
Source2:        jboss-aop-settings.xml
Source3:        jboss-aop-component-info.xml
Source9:	jboss-test-1.1.4.jar
Patch0:         jboss-aop-pom-maven-version.patch
Patch1:         jboss-aop2-SystemOutLoggerPlugin.patch
Patch2:         jboss-aop-pom-disable-integration.patch
Patch3:         jboss-aop2-asintegration-core-pom.patch
Patch4:         jboss-aop2-asintegration-jmx-pom.patch
Patch5:         jboss-aop2-asintegration-mc-pom.patch
Patch6:         jboss-aop2-build-pom.patch

BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-enforcer
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-release
BuildRequires: maven-shared-enforcer-rule-api
BuildRequires: maven-shared-plugin-testing-harness
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-surefire-report-maven-plugin
BuildRequires: ant >= 0:1.7.0
BuildRequires: gnu-trove
BuildRequires: jarjar
BuildRequires: jboss-parent
BuildRequires: jboss-profiler
BuildRequires: jboss-test
BuildRequires: junit
BuildRequires: qdox161

BuildRequires: bsh
BuildRequires: concurrent
BuildRequires: dom4j
BuildRequires: javacc
BuildRequires: javassist
BuildRequires: jboss-common-core
BuildRequires: jboss-common-logging-log4j
BuildRequires: jboss-common-logging-spi
BuildRequires: jboss-man
BuildRequires: jboss-mdr
BuildRequires: jboss-microcontainer2
BuildRequires: jboss-reflect
BuildRequires: jboss-vfs2
BuildRequires: j2ee_connector_1_5_api
BuildRequires: log4j
BuildRequires: servlet_2_5_api
BuildRequires: snmptrapappender
BuildRequires: xdoclet
BuildRequires: xerces-j2
BuildRequires: xjavadoc

%if %with integration
BuildRequires: ant-junit
BuildRequires: jboss-bootstrap
BuildRequires: jboss-cl
BuildRequires: jboss-deployers
BuildRequires: jboss-integration
BuildRequires: jboss4-system
BuildRequires: jboss5-libs
BuildRequires: maven-jbossaop-plugin
%endif

Requires: bsh
Requires: concurrent
Requires: dom4j
Requires: javacc
Requires: javassist
Requires: jboss-common-core
Requires: jboss-common-logging-log4j
Requires: jboss-common-logging-spi
Requires: jboss-man
Requires: jboss-mdr
Requires: jboss-microcontainer2
Requires: jboss-reflect
Requires: jboss-vfs2
Requires: j2ee_connector_1_5_api
Requires: log4j
Requires: servlet_2_5_api
Requires: snmptrapappender
Requires: xdoclet
Requires: xerces-j2
Requires: xjavadoc

%description
JBoss AOP.

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
%setup -q -n %{oname}-%{version}
%patch0 -b .sav0
%patch1 -b .sav1
%if %without integration
%patch2 -b .sav2
%else
%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5
%endif
%if %without jrockit
%patch6 -b .sav6
%endif

cp -p %{SOURCE2} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

sed -i '/directory>\/<\/directory/d' aop/src/assembly/single.xml
sed -i '/outputDirectory>\/<\/outputDirectory/d' aop/src/assembly/single.xml

%build
export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
export MAVEN_OPTS="-Xmx384m"

mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
	install:install-file -DgroupId=jboss -DartifactId=jboss-test -Dversion=1.0.3.GA -Dpackaging=jar -Dfile=%{SOURCE9}


mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
%if %with jrockit
        -Djrockit.home=%{_jvmdir}/java-1.5.0-oracle \
%endif
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install

mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Daggregate=true \
%if %with jrockit
        -Djrockit.home=%{_jvmdir}/java-1.5.0-oracle \
%endif
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        javadoc:javadoc

%install

# scripts
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 aop/src/resources/bin/aopc.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-aopc
install -m 755 aop/src/resources/bin/run-loadHotSwap.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-run-load15HotSwap
install -m 755 aop/src/resources/bin/run-load.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-run-load15
install -m 755 aop/src/resources/bin/run-precompiled.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-run-precompiled15


# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 aop/target/%{oname}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}-%{version}.jar
install -m 644 aop/target/%{oname}-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}-client-%{version}.jar
install -m 644 aop/target/%{oname}-single.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}-single-%{version}.jar
install -m 644 aop/target/%{oname}-tests.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}-tests-%{version}.jar
install -m 644 aspects/target/%{oname}-aspects.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}-aspects-%{version}.jar
%if %with jrockit
install -m 644 jrockit-pluggable-instrumentor/target/jrockit-pluggable-instrumentor.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jrockit-pluggable-instrumentor-%{version}.jar
%endif
install -m 644 pluggable-instrumentor/target/pluggable-instrumentor.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/pluggable-instrumentor-%{version}.jar
%if %with integration
install -m 644 aophelper/target/aophelper.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/aophelper-%{version}.jar
install -m 644 deployers/target/jboss-aop-deployers.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}-deployers-%{version}.jar
install -m 644 asintegration-core/target/jboss-aop-asintegration-core.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}-asintegration-core-%{version}.jar
install -m 644 asintegration-jmx/target/jboss-aop-asintegration-jmx.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}-asintegration-jmx-%{version}.jar
install -m 644 asintegration-mc/target/jboss-aop-asintegration-mc.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}-asintegration-mc-%{version}.jar
%endif

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{oname}-parent.pom
%add_to_maven_depmap org.jboss.aop %{oname}-parent %{namedversion} JPP/%{name} %{oname}-parent
install -m 644 aop/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{oname}.pom
%add_to_maven_depmap org.jboss.aop %{oname} %{namedversion} JPP/%{name} %{oname}
install -m 644 aspects/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{oname}-aspects.pom
%add_to_maven_depmap org.jboss.aop %{oname}-aspects %{namedversion} JPP/%{name} %{oname}-aspects
%if %with jrockit
install -m 644 jrockit-pluggable-instrumentor/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jrockit-pluggable-instrumentor.pom
%add_to_maven_depmap org.jboss.aop jrockit-pluggable-instrumentor %{namedversion} JPP/%{name} jrockit-pluggable-instrumentor
%endif
install -m 644 pluggable-instrumentor/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-pluggable-instrumentor.pom
%add_to_maven_depmap org.jboss.aop pluggable-instrumentor %{namedversion} JPP/%{name} pluggable-instrumentor

%if %with integration
install -m 644 aophelper/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-aophelper.pom
%add_to_maven_depmap org.jboss.aop aophelper %{namedversion} JPP/%{name} aophelper
install -m 644 deployers/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{oname}-deployers.pom
%add_to_maven_depmap org.jboss.aop %{oname}-deployers %{namedversion} JPP/%{name} %{oname}-deployers
install -m 644 asintegration-core/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{oname}-asintegration-core.pom
%add_to_maven_depmap org.jboss.aop %{oname}-asintegration-core %{namedversion} JPP/%{name} %{oname}-asintegration-core
install -m 644 asintegration-jmx/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{oname}-asintegration-jmx.pom
%add_to_maven_depmap org.jboss.aop %{oname}-asintegration-jmx %{namedversion} JPP/%{name} %{oname}-asintegration-jmx
install -m 644 asintegration-mc/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{oname}-asintegration-mc.pom
%add_to_maven_depmap org.jboss.aop %{oname}-asintegration-mc %{namedversion} JPP/%{name} %{oname}-asintegration-mc
%endif

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
install -p -m 644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
%if %without integration
install -p -m 644 %{PATCH2} $RPM_BUILD_ROOT%{repodirsrc}
%endif
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-aop.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/pluggable-instrumentor.jar $RPM_BUILD_ROOT%{repodirlib}/pluggable-instrumentor.jar
%if %with integration
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}-asintegration-core.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-aop-asintegration-core.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}-asintegration-jmx.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-aop-asintegration-jmx.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}-asintegration-mc.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-aop-asintegration-mc.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}-deployers.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-aop-deployers.jar
%else
perl -pi -e 's/^.*jboss-aop-asintegration-core\.jar.*\n$//g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
perl -pi -e 's/^.*jboss-aop-asintegration-jmx\.jar.*\n$//g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
perl -pi -e 's/^.*jboss-aop-asintegration-mc\.jar.*\n$//g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
perl -pi -e 's/^.*jboss-aop-deployers\.jar.*\n$//g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
%endif
%if %with jrockit
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jrockit-pluggable-instrumentor.jar $RPM_BUILD_ROOT%{repodirlib}/jrockit-pluggable-instrumentor.jar
%else
perl -pi -e 's/^.*jrockit-pluggable-instrumentor\.jar.*\n$//g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
%endif
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}-client.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-aop-client.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/%{oname}-aspects.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-aop-aspects.jar
%endif

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{oname}-%{version}.jar
%{_javadir}/%{name}/%{oname}.jar
%{_javadir}/%{name}/%{oname}-aspects-%{version}.jar
%{_javadir}/%{name}/%{oname}-aspects.jar
%{_javadir}/%{name}/%{oname}-client-%{version}.jar
%{_javadir}/%{name}/%{oname}-client.jar
%{_javadir}/%{name}/%{oname}-single-%{version}.jar
%{_javadir}/%{name}/%{oname}-single.jar
%{_javadir}/%{name}/%{oname}-tests-%{version}.jar
%{_javadir}/%{name}/%{oname}-tests.jar
%{_javadir}/%{name}/pluggable-instrumentor-%{version}.jar
%{_javadir}/%{name}/pluggable-instrumentor.jar
%{_datadir}/maven2/poms/JPP.%{name}-%{oname}-parent.pom
%{_datadir}/maven2/poms/JPP.%{name}-%{oname}.pom
%{_datadir}/maven2/poms/JPP.%{name}-%{oname}-aspects.pom
%if %with jrockit
%{_datadir}/maven2/poms/JPP.%{name}-jrockit-pluggable-instrumentor.pom
%endif
%{_datadir}/maven2/poms/JPP.%{name}-pluggable-instrumentor.pom
%if %with integration
%attr(0755,root,root) %{_bindir}/%{name}*
%{_javadir}/%{name}/aophelper-%{version}.jar
%{_javadir}/%{name}/aophelper.jar
%{_javadir}/%{name}/%{oname}-deployers-%{version}.jar
%{_javadir}/%{name}/%{oname}-deployers.jar
%{_javadir}/%{name}/%{oname}-asintegration-core-%{version}.jar
%{_javadir}/%{name}/%{oname}-asintegration-core.jar
%{_javadir}/%{name}/%{oname}-asintegration-jmx-%{version}.jar
%{_javadir}/%{name}/%{oname}-asintegration-jmx.jar
%{_javadir}/%{name}/%{oname}-asintegration-mc-%{version}.jar
%{_javadir}/%{name}/%{oname}-asintegration-mc.jar
%{_datadir}/maven2/poms/JPP.%{name}-aophelper.pom
%{_datadir}/maven2/poms/JPP.%{name}-%{oname}-deployers.pom
%{_datadir}/maven2/poms/JPP.%{name}-%{oname}-asintegration-core.pom
%{_datadir}/maven2/poms/JPP.%{name}-%{oname}-asintegration-jmx.pom
%{_datadir}/maven2/poms/JPP.%{name}-%{oname}-asintegration-mc.pom
%endif
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt3_0jpp6
- build w/java6

* Sat Feb 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_0jpp6
- fixed build

* Wed Feb 09 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_0jpp6
- new version

