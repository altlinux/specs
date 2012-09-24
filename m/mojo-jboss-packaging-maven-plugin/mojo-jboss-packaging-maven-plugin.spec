BuildRequires: maven-plugin-cobertura maven-surefire-provider-junit4 maven-enforcer-plugin maven-antrun-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mojo-jboss-packaging-maven-plugin
%define version 2.2
# Copyright (c) 2000-2012, JPackage Project
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

%define reltag %{?nil}
%define namedreltag %{?nil}
%global namedversion %{version}%{?namedreltag}

Name:           mojo-jboss-packaging-maven-plugin
Version:        2.2
Release:        alt1_1jpp6
Epoch:          0
Summary:        JBoss Packaging Maven Plugin
Group:          Development/Java
License:        MIT and ASL 2.0
URL:            http://mojo.codehaus.org/jboss-packaging-maven-plugin/
# svn export https://svn.codehaus.org/mojo/tags/jboss-packaging-maven-plugin-2.2/ mojo-jboss-packaging-maven-plugin-2.2 && tar cjf mojo-jboss-packaging-maven-plugin-2.2.tar.bz2 mojo-jboss-packaging-maven-plugin-2.2

Source0:        mojo-jboss-packaging-maven-plugin-2.2.tar.bz2
Source1:        mojo-jboss-packaging-maven-plugin-settings.xml
Source2:        mojo-jboss-packaging-maven-plugin-jpp-depmap.xml
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
Requires:       mojo-parent
Requires:       maven2
Requires:       maven-enforcer-plugin
Requires:       maven-shared-archiver
Requires:       maven-shared-filtering
Requires:       mojo-parent
Requires:       plexus-archiver
Requires:       plexus-interpolation
Requires:       plexus-utils
BuildRequires:  commons-parent
BuildRequires:  jpackage-utils
BuildRequires:  mojo-parent
BuildRequires:  maven2
BuildRequires:  maven2-plugin-changes
BuildRequires:  maven2-plugin-invoker
BuildRequires:  maven-shared-archiver
BuildRequires:  maven-shared-filtering
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  mojo-parent
BuildRequires:  plexus-archiver
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-utils
Provides:       mojo-maven2-plugin-jboss-packaging = %{epoch}:%{version}-%{release}
Obsoletes:      mojo-maven2-plugin-jboss-packaging = 17
Provides:       jboss-packaging-maven-plugin = %{epoch}:%{version}-%{release}
Obsoletes:      jboss-packaging-maven-plugin < %{epoch}:%{version}-%{release}
BuildArch:      noarch
Source44: import.info

%description
Maven plugin for generating various JBoss deployable archive files.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q 

%{__cp} -p %{SOURCE1} maven2-settings.xml

%{__sed} -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file:`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file:`pwd`/external_repo</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file:`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:%{_datadir}/maven2/plugins</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:%{_datadir}/eclipse/plugins</url>|g" maven2-settings.xml

%{__mkdir} external_repo
%{__ln_s} %{_javadir} external_repo/JPP

%build
export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
export MAVEN_OPTS="-Djava.awt.headless=true"
%{_bindir}/mvn-jpp \
        -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        package javadoc:aggregate

#       -Dmaven.test.failure.ignore=true \

%install

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p target/jboss-packaging-maven-plugin-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}-%{namedversion}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{namedversion}*; do ln -s ${jar} `echo ${jar} | sed "s|-%{namedversion}||g"`; done)
# compat symlinks for obsoleted rpms
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jboss-packaging-maven-plugin.jar
mkdir -p %{buildroot}%{_javadir}/mojo
ln -sf ../%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/jboss-packaging-maven-plugin.jar

# poms
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.codehaus.mojo jboss-packaging-maven-plugin %{namedversion} JPP %{name}

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
ln -s %{name}-%{namedversion} %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}-%{namedversion}.jar
%{_javadir}/%{name}.jar
%{_javadir}/jboss-packaging-maven-plugin.jar
%{_javadir}/mojo/jboss-packaging-maven-plugin.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{namedversion}
%{_javadocdir}/%{name}

%changelog
* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_1jpp6
- separate package

