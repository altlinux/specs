BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 2.1.0
%define name jboss-man
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

%define repodir %{_javadir}/repository.jboss.com/jboss/jboss-man/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define reltag SP1
%define namedversion %{version}.%{reltag}

Name:           jboss-man
Version:        2.1.0
Release:        alt3_2.SP1.2jpp6
Epoch:          0
Summary:        JBoss Man
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn -q export http://anonsvn.jboss.org/repos/jbossas/projects/jboss-man/tags/2.1.0.SP1/ jboss-man-2.1.0 && tar cjf jboss-man-2.1.0.tar.bz2 jboss-man-2.1.0
Source0:        jboss-man-2.1.0.tar.bz2
Source1:        jboss-man-jpp-depmap.xml
Source2:        jboss-man-settings.xml
Source3:        jboss-man-component-info.xml
Patch0:         jboss-man-pom.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jboss-common-core
Requires:       jboss-common-logging-spi
Requires:       jboss-mdr
Requires:       jboss-reflect
Requires:       jpackage-utils
BuildRequires:  commons-parent >= 0:9
BuildRequires:  jpackage-utils
BuildRequires:  maven2 >= 0:2.0.7
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-source
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-release
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  ant-junit
BuildRequires:  javassist
BuildRequires:  jaxb_2_1_api
BuildRequires:  jboss-common-logging-log4j
BuildRequires:  jboss-profiler
BuildRequires:  jboss-test
BuildRequires:  junit4
BuildRequires:  log4j
BuildRequires:  jboss-common-core
BuildRequires:  jboss-common-logging-spi
BuildRequires:  jboss-mdr
BuildRequires:  jboss-parent
BuildRequires:  jboss-reflect
BuildArch:      noarch
Source44: import.info

%description
JBoss managed and metatype.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
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
%patch0 -p0 -b .sav0

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
        -Dmaven.test.skip \
        -Dskip-enforce \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:aggregate

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p metatype/target/jboss-metatype.jar $RPM_BUILD_ROOT%{_javadir}/jboss-metatype-%{version}.jar
cp -p managed/target/jboss-managed.jar $RPM_BUILD_ROOT%{_javadir}/jboss-managed-%{version}.jar
#cp -p managed/target/jboss-managed-api.jar $RPM_BUILD_ROOT%{_javadir}/jboss-managed-api-%{version}.jar
#cp -p managed/target/jboss-managed-plugins.jar $RPM_BUILD_ROOT%{_javadir}/jboss-managed-plugins-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
cp -p pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
%add_to_maven_depmap org.jboss.man %{name}-parent %{namedversion} JPP %{name}-parent
cp -p metatype/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jboss-metatype.pom
%add_to_maven_depmap org.jboss.man jboss-metatype %{namedversion} JPP jboss-metatype
cp -p managed/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jboss-managed.pom
%add_to_maven_depmap org.jboss.man jboss-managed %{namedversion} JPP jboss-managed

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
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
cp -p $RPM_BUILD_ROOT%{_javadir}/jboss-managed.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-managed.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/jboss-metatype.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-metatype.jar
%endif

%files
%{_javadir}/jboss-metatype-%{version}.jar
%{_javadir}/jboss-metatype.jar
%{_javadir}/jboss-managed-%{version}.jar
%{_javadir}/jboss-managed.jar
%{_datadir}/maven2/poms/JPP-jboss-managed.pom
%{_datadir}/maven2/poms/JPP-jboss-metatype.pom
%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt3_2.SP1.2jpp6
- build w/java6

* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt2_2.SP1.2jpp6
- new jpp relase

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt2_2.SP1.1jpp6
- fixed build with new jboss-test

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt1_2.SP1.1jpp6
- new version

