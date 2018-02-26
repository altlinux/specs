Patch33: plugin-support-1.0-alpha-1-alt-maven3.patch
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 1.0
%define name plugin-support
# Copyright (c) 2000-2011, JPackage Project
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

%define reltag .alpha_1
%define namedreltag -alpha-1
%global namedversion %{version}%{?namedreltag}

Name:           plugin-support
Version:        1.0
Release:        alt3_1.alpha_1jpp6
Epoch:          0
Summary:        Plugin Support
Group:          Development/Java
License:        MIT and ASL 2.0
URL:            http://mojo.codehaus.org/plugin-support/
# svn export https://svn.codehaus.org/mojo/tags/plugin-support-1.0-alpha-1/ plugin-support-1.0-alpha-1 && tar cjf plugin-support-1.0-alpha-1.tar.bz2 plugin-support-1.0-alpha-1
# Exported revision 13666.
Source0:        plugin-support-1.0-alpha-1.tar.bz2
Source1:        plugin-support-settings.xml
Source2:        plugin-support-jpp-depmap.xml
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       ant >= 0:1.6.5
Requires:       apache-commons-jexl >= 0:1.1
Requires:       commons-lang >= 0:2.3
Requires:       commons-logging >= 0:1.0.4
Requires:       maven2 >= 0:2.0.4
Requires:       mojo-parent
Requires:       jpackage-utils
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  apache-commons-jexl >= 0:1.1
BuildRequires:  commons-lang >= 0:2.3
BuildRequires:  commons-logging >= 0:1.0.4
BuildRequires:  maven2 >= 0:2.0.4
BuildRequires:  mojo-parent
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-idea
BuildRequires:  commons-parent
BuildRequires:  jpackage-utils
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven2-plugin-site
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-doxia
BuildRequires:  maven-doxia-sitetools
BuildRequires:  mojo-parent
BuildArch:      noarch
Source44: import.info

%description
Provides common support classes and components for plugins.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n plugin-support-%{namedversion}

%{__cp} -p %{SOURCE1} maven2-settings.xml

%{__sed} -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file:`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file:`pwd`/external_repo</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file:`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:%{_datadir}/maven2/plugins</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:%{_datadir}/eclipse/plugins</url>|g" maven2-settings.xml

%{__mkdir} external_repo
%{__ln_s} %{_javadir} external_repo/JPP

%patch33

%build
export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
export MAVEN_OPTS="-Djava.awt.headless=true"
mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.test.failure.ignore=true \
        package javadoc:aggregate

%install

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p target/plugin-support-%{namedversion}.jar %{buildroot}%{_javadir}/plugin-support-%{namedversion}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{namedversion}*; do ln -s ${jar} `echo ${jar} | sed "s|-%{namedversion}||g"`; done)

# poms
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-plugin-support.pom
%add_to_maven_depmap org.codehaus.mojo plugin-support %{namedversion} JPP plugin-support

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/plugin-support-%{namedversion}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/plugin-support-%{namedversion}
ln -s plugin-support-%{namedversion} %{buildroot}%{_javadocdir}/plugin-support

%files
%{_javadir}/plugin-support-%{namedversion}.jar
%{_javadir}/plugin-support.jar
%{_datadir}/maven2/poms/JPP-plugin-support.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/plugin-support-%{namedversion}
%{_javadocdir}/plugin-support

%changelog
* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_1.alpha_1jpp6
- fixed build with maven3

* Mon Feb 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_1.alpha_1jpp6
- fixed build

* Tue Jan 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1.alpha_1jpp6
- new version

