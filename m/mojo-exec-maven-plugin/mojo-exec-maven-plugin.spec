BuildRequires: maven-plugin-cobertura maven-surefire-provider-junit4
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mojo-exec-maven-plugin
%define version 1.2.1
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

Name:           mojo-exec-maven-plugin
Version:        1.2.1
Release:        alt1_1jpp7
Epoch:          0
Summary:        Execute system and Java programs
Group:          Development/Java
License:        ASL 2.0
URL:            http://mojo.codehaus.org/exec-maven-plugin/
# svn export http://svn.codehaus.org/mojo/tags/exec-maven-plugin-1.2.1/ mojo-exec-maven-plugin-1.2.1 && tar czf mojo-exec-maven-plugin-1.2.1.tgz mojo-exec-maven-plugin-1.2.1

Source0:        mojo-exec-maven-plugin-1.2.1.tgz
Source1:        mojo-exec-maven-plugin-settings.xml
Source2:        mojo-exec-maven-plugin-jpp-depmap.xml
Patch0:         mojo-exec-maven-plugin-pom.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
Requires:       mojo-parent
Requires:       maven2
Requires:       maven-shared-invoker
Requires:       maven-toolchain
Requires:       apache-commons-exec
Requires:       plexus-container-default
Requires:       plexus-utils
BuildRequires:  mojo-parent
BuildRequires:  maven2
BuildRequires:  apache-commons-exec
BuildRequires:  plexus-container-default
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-utils
BuildRequires:  jpackage-utils
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-invoker
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven-plugin-testing-harness
BuildRequires:  maven-shared-invoker
BuildRequires:  maven-toolchain
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  animal-sniffer
BuildRequires:  mojo-signatures
BuildArch:      noarch
Provides:       mojo-maven2-plugin-exec = %{epoch}:%{version}-%{release}
Obsoletes:      mojo-maven2-plugin-exec > 17
Provides:       exec-maven-plugin = %{epoch}:%{version}-%{release}
Obsoletes:      exec-maven-plugin < %{epoch}:%{version}-%{release}
Source44: import.info

Patch1: mojo-exec-maven-plugin-alt-maven3-pom.patch


%description
Execution of system and Java programs.

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

%patch0 -b .sav0

%{__mkdir} external_repo
%{__ln_s} %{_javadir} external_repo/JPP

%patch1 -p0

%build
export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository

%{_bindir}/mvn-jpp \
        -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.test.failure.ignore=true \
        package javadoc:aggregate


%install

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p target/exec-maven-plugin-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}-%{namedversion}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{namedversion}*; do ln -s ${jar} `echo ${jar} | sed "s|-%{namedversion}||g"`; done)
# compat symlinks for obsoleted rpms
mkdir -p %{buildroot}%{_javadir}/mojo
ln -sf ../%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/exec-maven-plugin.jar

# poms
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.codehaus.mojo exec-maven-plugin %{namedversion} JPP %{name}

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
ln -s %{name}-%{namedversion} %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}-%{namedversion}.jar
%{_javadir}/%{name}.jar
%{_javadir}/mojo/exec-maven-plugin.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{namedversion}
%{_javadocdir}/%{name}

%changelog
* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_1jpp7
- new version

