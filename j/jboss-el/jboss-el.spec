BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2010, JPackage Project
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

%define reltag CR5
%define version_full %{version}.%{reltag}

%define repodir %{_javadir}/repository.jboss.com/org/jboss/el/%{version_full}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

Name:           jboss-el
Version:        1.0_02
Release:        alt1_0.CR5.2jpp6
Epoch:          0
Summary:        Extended EL implementation
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn -q export http://anonsvn.jboss.org/repos/jboss-el/tags/1.0_02.CR5/ jboss-el-1.0_02.CR5 && tar cjf jboss-el-1.0_02.CR5.tar.bz2 jboss-el-1.0_02.CR5
Source0:        %{name}-%{version_full}.tar.bz2
Source1:        jboss-el-jpp-depmap.xml
Source2:        jboss-el-settings.xml
Source3:        jboss-el-component-info.xml
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: el_1_0_api
BuildRequires: el_1_0_api
BuildRequires: jpackage-utils
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: junit4 >= 0:4.2
BuildRequires: maven-ant-tasks
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-deploy
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-release
BuildRequires: maven-surefire-maven-plugin
BuildArch:      noarch
Source44: import.info

%description
JBoss EL is a extended EL implementation, distributed with Seam.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%if %with repolib
%package repolib
Summary:         Artifacts to be uploaded to a repository library
Group:           Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n %{name}-%{version_full}
%{_bindir}/find -type f -name "*.?ar" | %{_bindir}/xargs -t %{__rm}

%{__ln_s} $(build-classpath junit4) lib/junit-4.2.jar
%{__ln_s} $(build-classpath maven-ant-tasks) lib/maven-ant-tasks.jar

%{__cp} -p %{SOURCE2} maven2-settings.xml

%{__sed} -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

%{__mkdir} external_repo
%{__ln_s} %{_javadir} external_repo/JPP

%build
%if 0
export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository

%{_bindir}/mvn-jpp -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        -DaltDeploymentRepository=jboss-releases::default::file://$(pwd)/maven2-brew \
        install javadoc:javadoc
%else
export CLASSPATH=
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
%{ant} -Dincludeantruntime=false -Dbuild.sysclasspath=first clean build test
%endif

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}/%{name}
%if 0
%{__cp} -p target/jboss-el-%{version_full}.jar %{buildroot}%{_javadir}/%{name}-%{version_full}.jar
%else
%{__cp} -p dist/jboss-el.jar %{buildroot}%{_javadir}/%{name}-%{version_full}.jar
%{__cp} -p dist/jboss-el-api.jar %{buildroot}%{_javadir}/%{name}-api-%{version_full}.jar
%{__cp} -p dist/jboss-el-sources.jar %{buildroot}%{_javadir}/%{name}-sources-%{version_full}.jar
%{__cp} -p dist/jboss-el-test.jar %{buildroot}%{_javadir}/%{name}-test-%{version_full}.jar
%endif
(cd %{buildroot}%{_javadir} && for jar in *-%{version_full}.?ar; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version_full}||g"`; done)

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.jboss.el jboss-el %{version} JPP %{name}

%if 0
# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{project_version}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{project_version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%endif

%if %with repolib
if [ -d maven2-brew ]; then
    %{__mkdir_p} %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
    %{__cp} -pr maven2-brew/* %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
fi
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{SOURCE1} %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version_full}.jar %{buildroot}%{repodirlib}/jboss-el.jar
%{__cp} -p %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom %{buildroot}%{repodirlib}/jboss-el.pom
%endif

%files
%{_javadir}/%{name}-%{version_full}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-api-%{version_full}.jar
%{_javadir}/%{name}-api.jar
%{_javadir}/%{name}-sources-%{version_full}.jar
%{_javadir}/%{name}-sources.jar
%{_javadir}/%{name}-test-%{version_full}.jar
%{_javadir}/%{name}-test.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%if 0
%files javadoc
%{_javadocdir}/%{name}-%{project_version}
%{_javadocdir}/%{name}
%endif

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0_02-alt1_0.CR5.2jpp6
- new version

