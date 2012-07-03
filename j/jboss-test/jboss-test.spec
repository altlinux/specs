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

%define repodir %{_javadir}/repository.jboss.com/jboss/test/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define reltag GA
%define namedversion %{version}.%{reltag}

Name:           jboss-test
Version:        1.1.4
Release:	alt1_4jpp6
Epoch:          1
Summary:        JBoss Test
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn -q export http://anonsvn.jboss.org/repos/jbossas/projects/test/tags/1.1.4.GA/ jboss-test-1.1.4 && tar cjf jboss-test-1.1.4.tar.bz2 jboss-test-1.1.4
Source0:        jboss-test-1.1.4.tar.bz2
Source1:        jboss-test-jpp-depmap.xml
Source2:        jboss-test-settings.xml
Source3:        jboss-test-component-info.xml
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: ant-junit >= 0:1.7.0
Requires: jboss-common-core
Requires: jboss-common-logging-log4j
Requires: jboss-profiler
Requires: jboss-server-manager
Requires: log4j
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-dependency
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-release
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: jboss-deploy-maven-plugin
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: jboss-profiler
BuildRequires: junit
BuildRequires: jboss-common-core
BuildRequires: jboss-common-logging-log4j
BuildRequires: jboss-parent
BuildRequires: jboss-server-manager
BuildRequires: log4j
BuildArch:      noarch
Source44: import.info

%description
JBoss Test.

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

# ant 1.8 support hack
for i in `find . -name buildmagic.ent`; do sed -i 's,fail unless="buildmagic.ant.compatible",fail if="never",' $i; done

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
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dskip-enforce \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -m 644 pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.jboss.test jboss-test %{namedversion} JPP %{name}

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %with repolib
install -d -m 755 %{buildroot}%{repodir}
install -d -m 755 %{buildroot}%{repodirlib}
install -p -m 644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}.%{reltag}-brew/g' %{buildroot}%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
install -d -m 755 %{buildroot}%{repodirsrc}
install -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
install -p -m 644 %{SOURCE1} %{buildroot}%{repodirsrc}
install -p -m 644 %{SOURCE2} %{buildroot}%{repodirsrc}
cp -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/jboss-test.jar
%endif

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Feb 09 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.1.4-alt1_4jpp6
- new version

* Fri Sep 17 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.0.0-alt1_2jpp6
- ant 1.8.x support

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.0.0-alt1_2jpp5
- new version

* Wed Oct 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.0-alt1_0.JBossMC_1_0_1.1jpp1.7
- converted from JPackage by jppimport script

