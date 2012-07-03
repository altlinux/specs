BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 2.0.6
%define name jboss-cl
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

%define repodir %{_javadir}/repository.jboss.com/jboss/jboss-cl/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define reltag GA
%define namedversion %{version}.%{reltag}

Name:           jboss-cl
Version:        2.0.6
Release:	alt2_3jpp6
Epoch:          0
Summary:        JBoss Classloading
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn export http://anonsvn.jboss.org/repos/jbossas/projects/jboss-cl/tags/2.0.6.GA/ jboss-cl-2.0.6
Source0:        jboss-cl-2.0.6.tar.gz
Source1:        jboss-cl-jpp-depmap.xml
Source2:        jboss-cl-settings.xml
Source3:        jboss-cl-component-info.xml
Patch0:         jboss-cl-pom.patch
BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  maven2 >= 0:2.0.7
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-source
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-release
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  ant-junit
BuildRequires:  javassist >= 0:3.9.0
BuildRequires:  jboss-test
BuildRequires:  junit44

BuildRequires:  jboss-common-core
BuildRequires:  jboss-common-logging-spi
BuildRequires:  jboss-integration
BuildRequires:  jboss-man
BuildRequires:  jboss-microcontainer2
BuildRequires:  jboss-parent
BuildRequires:  jboss-vfs2
BuildRequires:  jbossxb2 >= 0:2.0.1

Requires:  jboss-common-core
Requires:  jboss-common-logging-spi
Requires:  jboss-integration
Requires:  jboss-man
Requires:  jboss-microcontainer2
Requires:  jboss-vfs2
Requires:  jbossxb2 >= 0:2.0.1

BuildRequires: commons-parent
Source44: import.info

%description
JBoss classloading.

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

sed -i /relativePath/d classloading-vfs/pom.xml


%build
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -Daggregate=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        javadoc:javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

%add_to_maven_depmap org.jboss.cl jboss-cl %{namedversion} JPP/%{name} jboss-cl
install -m 644 classloading-vfs/target/jboss-classloading-vfs.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-classloading-vfs-%{version}.jar
%add_to_maven_depmap org.jboss.cl jboss-classloading-vfs %{namedversion} JPP/%{name} jboss-classloading-vfs
install -m 644 classloading/target/jboss-classloading.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-classloading-%{version}.jar
%add_to_maven_depmap org.jboss.cl jboss-classloading %{namedversion} JPP/%{name} jboss-classloading
install -m 644 classloader/target/jboss-classloader.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-classloader-%{version}.jar
%add_to_maven_depmap org.jboss.cl jboss-classloader %{namedversion} JPP/%{name} jboss-classloader
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom
install -m 644 classloading-vfs/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-classloading-vfs.pom
install -m 644 classloading/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-classloading.pom
install -m 644 classloader/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss-classloader.pom

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
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-classloader.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-classloader.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-classloading.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-classloading.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-classloading-vfs.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-classloading-vfs.jar
%endif

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/jboss-classloading-vfs-%{version}.jar
%{_javadir}/%{name}/jboss-classloading-vfs.jar
%{_javadir}/%{name}/jboss-classloading-%{version}.jar
%{_javadir}/%{name}/jboss-classloading.jar
%{_javadir}/%{name}/jboss-classloader-%{version}.jar
%{_javadir}/%{name}/jboss-classloader.jar
%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-classloading-vfs.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-classloading.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-classloader.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Mar 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt2_3jpp6
- fixed build with maven3

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt1_3jpp6
- new jpp release

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt1_2jpp6
- new version

