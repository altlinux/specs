BuildRequires: maven-plugin-cobertura maven-surefire-provider-junit4 maven-enforcer-plugin maven-antrun-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mojo-taglist-maven-plugin
%define version 2.4
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

Name:           mojo-taglist-maven-plugin
Version:        2.4
Release:        alt1_1jpp6
Epoch:          0
Summary:        Taglist Maven Plugin
Group:          Development/Java
License:        MIT and ASL 2.0
URL:            http://mojo.codehaus.org/taglist-maven-plugin/
# svn export https://svn.codehaus.org/mojo/tags/taglist-maven-plugin-2.4/ mojo-taglist-maven-plugin-2.4 && tar cjf mojo-taglist-maven-plugin-2.4.tar.bz2 mojo-taglist-maven-plugin-2.4
# Exported revision 16747.
Source0:        mojo-taglist-maven-plugin-2.4.tar.bz2
Source1:        mojo-taglist-maven-plugin-settings.xml
Source2:        mojo-taglist-maven-plugin-jpp-depmap.xml
Patch0:         mojo-taglist-maven-plugin-doxia.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
Requires:       maven2
Requires:       maven-shared-reporting-impl
Requires:       plexus-container-default >= 0:1.0
Requires:       plexus-utils
BuildRequires:  commons-parent
BuildRequires:  jpackage-utils
BuildRequires:  maven2
BuildRequires:  maven-shared-reporting-impl
BuildRequires:  maven-shared-plugin-testing-harness
BuildRequires:  plexus-container-default >= 0:1.0
BuildRequires:  plexus-utils
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-changes
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven2-plugin-site
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-doxia
BuildRequires:  maven-doxia-sitetools
BuildRequires:  modello
BuildRequires:  mojo-parent
BuildRequires:  plexus-containers-component-javadoc
BuildArch:      noarch
Provides:       mojo-maven2-plugin-taglist = %{epoch}:%{version}-%{release}
Obsoletes:      mojo-maven2-plugin-taglist = 17
#Provides:       taglist-maven-plugin = %{epoch}:%{version}-%{release}
#Obsoletes:      taglist-maven-plugin < %{epoch}:%{version}-%{release}
Source44: import.info

%description
The Taglist Maven Plugin generates a report on various tags
found in the code, like @todo or //TODO tags.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q 
%patch0 -p0 -b .sav0

%{__cp} -p %{SOURCE1} maven2-settings.xml

%{__sed} -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

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
        -Dmaven.test.failure.ignore=true \
        package javadoc:aggregate


%install

# jars
mkdir -p %{buildroot}%{_javadir}/mojo
cp -p target/taglist-maven-plugin-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}-%{namedversion}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{namedversion}*; do ln -s ${jar} `echo ${jar} | sed "s|-%{namedversion}||g"`; done)
ln -s %{name}-%{namedversion}.jar %{buildroot}%{_javadir}/taglist-maven-plugin.jar
ln -s ../%{name}-%{namedversion}.jar %{buildroot}%{_javadir}/mojo/taglist-maven-plugin.jar

# poms
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.codehaus.mojo taglist-maven-plugin %{namedversion} JPP %{name}

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
ln -s %{name}-%{namedversion} %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/*.jar
%{_javadir}/mojo/*.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{namedversion}
%{_javadocdir}/%{name}

%changelog
* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_1jpp6
- separate package

