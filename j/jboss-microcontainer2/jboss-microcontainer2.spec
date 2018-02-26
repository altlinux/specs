Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc cglib
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

%bcond_without integration
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/jboss/microcontainer/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define oname jboss-microcontainer
%define reltag GA
%define namedversion %{version}.%{reltag}

Name:           jboss-microcontainer2
Version:        2.0.8
Release:	alt4_3jpp6
Epoch:          0
Summary:        JBoss Microcontainer
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn -q export http://anonsvn.jboss.org/repos/jbossas/projects/microcontainer/tags/2.0.8.GA/ jboss-microcontainer-2.0.8
Source0:        jboss-microcontainer-2.0.8.tar.gz
Source1:        jboss-microcontainer-jpp-depmap.xml
Source2:        jboss-microcontainer-settings.xml
Source3:        jboss-microcontainer-component-info.xml
Patch0:         jboss-microcontainer-pom.patch
#Patch1:         jboss-microcontainer-kernel-pom.patch
Patch2:         jboss-microcontainer-wo-int.patch

BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: maven2 >= 0:2.0.7
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
BuildRequires: maven-surefire-maven-plugin
BuildRequires: jboss-parent
BuildRequires: jboss-test
BuildRequires: ant-junit

BuildRequires: jboss-common-logging-log4j
BuildRequires: jboss-man
BuildRequires: jboss-mdr
BuildRequires: jbossxb2
%if %with integration
BuildRequires: gnu-trove
BuildRequires: google-guice1
BuildRequires: jboss-aop2
%endif

Requires: jboss-common-logging-log4j
Requires: jboss-man
Requires: jboss-mdr
Requires: jbossxb2
%if %with integration
Requires: jboss-aop2
%endif

%description
JBoss microcontainer.

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
%if %without integration
%patch2 -b .sav2
%else
%patch0 -b .sav0
%endif
#%patch1 -b .sav1

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
export MAVEN_OPTS="-Dmaven.test.skip=true -Dskip-enforce=true -Daggregate=true -Dmaven.repo.local=$MAVEN_REPO_LOCAL -Dmaven2.jpp.depmap.file=%{SOURCE1}"

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        install 

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        javadoc:javadoc 

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 kernel/target/jboss-kernel.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-kernel-%{version}.jar
#install -m 644 kernel/target/jboss-kernel-tests.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-kernel-tests-%{version}.jar
install -m 644 dependency/target/jboss-dependency.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-dependency-%{version}.jar

%if %with integration
install -m 644 aop-mc-int/target/jboss-aop-mc-int.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-aop-mc-int-%{version}.jar
install -m 644 guice-int/target/jboss-guice-int.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-guice-int-%{version}.jar
install -m 644 spring-int/target/jboss-spring-int.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-spring-int-%{version}.jar
%endif
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%add_to_maven_depmap org.jboss.microcontainer %{oname} %{namedversion} JPP/%{name} %{oname}
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{oname}.pom
%add_to_maven_depmap org.jboss.microcontainer jboss-kernel %{namedversion} JPP/%{name} jboss-kernel
install -m 644 kernel/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-kernel.pom
%add_to_maven_depmap org.jboss.microcontainer jboss-dependency %{namedversion} JPP/%{name} jboss-dependency
install -m 644 dependency/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-dependency.pom
%if %with integration
%add_to_maven_depmap org.jboss.microcontainer jboss-aop-mc-int %{namedversion} JPP/%{name} jboss-aop-mc-int
install -m 644 aop-mc-int/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-aop-mc-int.pom
%add_to_maven_depmap org.jboss.microcontainer jboss-guice-int %{namedversion} JPP/%{name} jboss-guice-int
install -m 644 guice-int/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-guice-int.pom
%add_to_maven_depmap org.jboss.microcontainer jboss-spring-int %{namedversion} JPP/%{name} jboss-spring-int
install -m 644 spring-int/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-spring-int.pom
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
#install -p -m 644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH2} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{oname}.pom $RPM_BUILD_ROOT%{repodirlib}/jboss-microcontainer.pom
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-dependency.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-dependency.jar
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-dependency.pom $RPM_BUILD_ROOT%{repodirlib}/jboss-dependency.pom
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-kernel.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-kernel.jar
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-kernel.pom $RPM_BUILD_ROOT%{repodirlib}/jboss-kernel.pom
%if %with integration
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-aop-mc-int.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-aop-mc-int.jar
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-aop-mc-int.pom $RPM_BUILD_ROOT%{repodirlib}/jboss-aop-mc-int.pom
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-guice-int.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-guice-int.jar
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-guice-int.pom $RPM_BUILD_ROOT%{repodirlib}/jboss-guice-int.pom
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-spring-int.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-spring-int.jar
cp -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-spring-int.pom $RPM_BUILD_ROOT%{repodirlib}/jboss-spring-int.pom
%else
perl -pi -e 's/^.*jboss-.*-int.jar.*\n$//g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
%endif
%endif

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/jboss-dependency-%{version}.jar
%{_javadir}/%{name}/jboss-dependency.jar
%{_javadir}/%{name}/jboss-kernel-%{version}.jar
%{_javadir}/%{name}/jboss-kernel.jar
#%{_javadir}/%{name}/jboss-kernel-tests-%{version}.jar
#%{_javadir}/%{name}/jboss-kernel-tests.jar
%if %with integration
%{_javadir}/%{name}/jboss-aop-mc-int-%{version}.jar
%{_javadir}/%{name}/jboss-aop-mc-int.jar
%{_javadir}/%{name}/jboss-guice-int-%{version}.jar
%{_javadir}/%{name}/jboss-guice-int.jar
%{_javadir}/%{name}/jboss-spring-int-%{version}.jar
%{_javadir}/%{name}/jboss-spring-int.jar
%endif
%{_datadir}/maven2/poms/JPP.%{name}-jboss-dependency.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-kernel.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-microcontainer.pom
%if %with integration
%{_datadir}/maven2/poms/JPP.%{name}-jboss-aop-mc-int.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-guice-int.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-spring-int.pom
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
* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt4_3jpp6
- fixed build with maven3
- do not package jboss-kernel-tests.jar

* Sun Mar 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt3_3jpp6
- fixed build with google-guice

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt2_3jpp6
- fixed build with new jboss-test

* Wed Feb 09 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt1_3jpp6
- full build (with integration)

* Wed Feb 09 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt1_0jpp6
- new version

