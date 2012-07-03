Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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

%bcond_without          repolib
%bcond_without          ant

%define repodir %{_javadir}/repository.jboss.com/jboss/jboss-vfs/%{version_full}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define gcj_support 0

%define version_full %{version}.GA

Name:           jboss-vfs    
Version:        1.0.0
Release:        alt1_2jpp5
Epoch:          0
Summary:        JBoss VFS library
License:        LGPLv2+
Group:          Development/Java
URL:            http://labs.jboss.com
# svn export http://anonsvn.jboss.org/repos/jbossas/projects/vfs/tags/1.0.0.GA/ jboss-vfs-1.0.0.GA
# tar cjf jboss-vfs-1.0.0.GA.tar.bz2 jboss-vfs-1.0.0.GA
Source0:        jboss-vfs-1.0.0.GA.tar.bz2
Source1:        jboss-vfs-component-info.xml
Source2:        build.xml
Source3:        maven-build.properties
Source4:        maven-build.xml
Patch0:         jboss-vfs-1.0.0-pom.patch
Requires: jboss-common
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jboss-common
BuildRequires: jboss-common
BuildRequires: jpackage-utils
%if %with ant
BuildRequires: ant
%else
BuildRequires: concurrent
BuildRequires: jakarta-commons-collections
BuildRequires: junit4
BuildRequires: maven2-common-poms
BuildRequires: maven-doxia
BuildRequires: maven-shared
BuildRequires: maven-shared-archiver
BuildRequires: maven-shared-reporting-impl
BuildRequires: maven-surefire
BuildRequires: maven-wagon
BuildRequires: plexus-archiver
BuildRequires: plexus-compiler
BuildRequires: plexus-container-default
BuildRequires: plexus-containers
BuildRequires: plexus-digest
BuildRequires: plexus-i18n
BuildRequires: plexus-utils
BuildRequires: plexus-velocity
BuildRequires: velocity14
BuildRequires: jboss-parent
BuildRequires: jboss-test
BuildRequires: maven2
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-release
BuildRequires: maven-surefire-booter
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-report-plugin
%endif
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch: noarch
%endif

%description
JBoss VFS library.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
Javadoc for %{name}.

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
%setup -q -n jboss-vfs-%{version_full}
%patch0 -p1
%if %with ant
%{__cp} -p %{SOURCE2} %{SOURCE3} %{SOURCE4} .
%endif

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL
%if %without ant
mvn-jpp -Dmaven.repo.local=$MAVEN_REPO_LOCAL install javadoc:javadoc
%else
export CLASSPATH=$(build-classpath jboss-common/jboss-common)
export OPT_JAR_LIST=:
%{ant} -Dmaven.repo.local=$MAVEN_REPO_LOCAL -Dmaven.test.skip=true -Dmaven.mode.offline=true jar javadoc
pushd src/main/java
%{jar} cf ../../../target/jboss-vfs-sources.jar `find -type f -name '*.java'`
popd
%endif

%install

%{__mkdir_p} %{buildroot}%{_javadir}/jboss
%{__cp} -a target/jboss-vfs.jar %{buildroot}%{_javadir}/jboss/%{name}-%{version}.jar
%{__cp} -a target/jboss-vfs-sources.jar %{buildroot}%{_javadir}/jboss/%{name}-sources-%{version}.jar
(cd %{buildroot}%{_javadir}/jboss && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -a target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# poms
%add_to_maven_depmap jboss jboss-vfs %{version_full} JPP/%jboss %{name}
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -a pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jboss.%{name}.pom

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -a %{SOURCE1} %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version_full}-brew/g" %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -a %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -a %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/jboss/jboss-vfs-%{version}.jar %{buildroot}%{repodirlib}/jboss-vfs.jar
%{__cp} -p %{buildroot}%{_javadir}/jboss/jboss-vfs-sources-%{version}.jar %{buildroot}%{repodirlib}/jboss-vfs-sources.jar
%endif

%files
%dir %{_javadir}/jboss
%{_javadir}/jboss/%{name}-%{version}.jar
%{_javadir}/jboss/%{name}.jar
%{_javadir}/jboss/%{name}-sources-%{version}.jar
%{_javadir}/jboss/%{name}-sources.jar
%{_datadir}/maven2/poms//JPP.jboss.%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root,) %{_libdir}/gcj/%{name}/*.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_2jpp5
- new version

