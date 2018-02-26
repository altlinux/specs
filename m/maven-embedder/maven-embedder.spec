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

%bcond_without maven


Name:           maven-embedder
Version:        2.0.4
Release:        alt2_5jpp6
Epoch:          0
Summary:        Maven Embedder
License:        ASL 2.0
Group:          Development/Java
URL:            http://maven.apache.org/
# svn export http://svn.apache.org/repos/asf/maven/components/tags/maven-embedder-2.0.4/
# Note: Exported revision 776856.
# tar czf maven-embedder-2.0.4-src.tgz maven-embedder-2.0.4
Source0:        %{name}-%{version}-src.tgz
Source1:        %{name}-build.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-settings.xml
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: maven2
BuildRequires: jpackage-utils >= 0:1.7.3
%if %with maven
BuildRequires: maven2 >= 0:2.0.4
BuildRequires: maven2-plugin-ant
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-checkstyle
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-pmd
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-doxia
BuildRequires: maven-doxia-sitetools
BuildRequires: tomcat5
BuildRequires: tomcat5-servlet-2.4-api
BuildRequires: excalibur-avalon-logkit
BuildRequires: excalibur-avalon-framework
BuildRequires: checkstyle4
%else
BuildRequires: ant
%endif
Conflicts: maven2 < 0:2.0.6
BuildArch:      noarch

%description
The Maven Embedder is used by the Maven CLI, by IDE integration projects like
Mevenide and potentially any tool that needs to embed Maven's capabilities.
You could embed Maven in a Continuous Integration application to run Maven
build, an application lifecycle management (ALF) tool, or Ant tasks that
utilize Maven's functionality.

These are just a few examples of what the Maven Embedder can be used for.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
 
%{__cp} -p %{SOURCE1} build.xml

%if %with maven
%{__cp} -p %{SOURCE3} settings.xml
%{__sed} -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
%{__sed} -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
%{__sed} -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
%endif

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}

%if %with maven
export MAVEN_SETTINGS=$(pwd)/settings.xml
# disable tests because they download stuff from the net
# ignoring failures only needed for mock environments
%{_bindir}/mvn-jpp \
        -e \
        -s ${MAVEN_SETTINGS} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven.test.skip=true \
        install javadoc:javadoc
%else
export OPT_JAR_LIST=:
export CLASSPATH=$(build-classpath \
commons-codec \
commons-httpclient \
commons-logging \
jdom \
maven2/artifact \
maven2/artifact-manager \
maven2/core \
maven2/model \
maven2/monitor \
maven2/plugin-api \
maven2/plugin-descriptor \
maven2/plugin-registry \
maven2/profile \
maven2/project \
maven2/repository-metadata \
maven2/settings \
maven-wagon/provider-api \
maven-wagon/file \
maven-wagon/http \
plexus/classworlds \
plexus/container-default \
plexus/interactivity-api \
plexus/utils \
)
CLASSPATH=${CLASSPATH}:target/classes:target/test-classes
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
%endif

%install

# jar
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p target/maven-embedder-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__mkdir_p} %{buildroot}%{_javadir}/maven2
%{__ln_s} ../%{name}-%{version}.jar %{buildroot}%{_javadir}/maven2/embedder-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)
(cd %{buildroot}%{_javadir}/maven2 && for jar in *-%{version}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}/%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache.maven maven-embedder %{version} JPP %{name}

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/maven2/embedder-%{version}.jar
%{_javadir}/maven2/embedder.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sun Sep 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt2_5jpp6
- updated to a12.

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt2_1jpp5
- fixes for java6 support

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_1jpp5
- converted from JPackage by jppimport script

