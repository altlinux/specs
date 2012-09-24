BuildRequires: maven-plugin-cobertura maven-surefire-provider-junit4 maven-enforcer-plugin maven-antrun-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name mojo-javacc-maven-plugin
%define version 2.6
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

Name:           mojo-javacc-maven-plugin
Version:        2.6
Release:        alt1_1jpp6
Epoch:          0
Summary:        JavaCC Maven Plugin
Group:          Development/Java
License:        ASL 2.0
URL:            http://mojo.codehaus.org/javacc-maven-plugin/
# svn export http://svn.codehaus.org/mojo/tags/javacc-maven-plugin-2.6/ mojo-javacc-maven-plugin-2.6 && tar czf mojo-javacc-maven-plugin-2.6.tgz mojo-javacc-maven-plugin-2.6

Source0:        mojo-javacc-maven-plugin-2.6.tgz
Source1:        mojo-javacc-maven-plugin-settings.xml
Source2:        mojo-javacc-maven-plugin-jpp-depmap.xml

Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
Requires:       mojo-parent
Requires:       maven2
Requires:       maven-doxia
Requires:       maven-doxia-sitetools
Requires:       maven-shared-reporting-impl
Requires:       javacc
Requires:       jtb
Requires:       plexus-utils
BuildRequires:  mojo-parent
BuildRequires:  maven2
BuildRequires:  javacc
BuildRequires:  jtb
BuildRequires:  plexus-utils
BuildRequires:  jpackage-utils
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-invoker
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven-doxia
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-shared-reporting-impl
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  junit
BuildArch:      noarch
Provides:       mojo-maven2-plugin-javacc = %{epoch}:%{version}-%{release}
Obsoletes:      mojo-maven2-plugin-javacc = 17
Source44: import.info

%description
This plugin uses the JavaCC parser generator to process 
JavaCC grammar files and generate the appropriate Java 
source files. For general information about JavaCC, see 
the JavaCC web site.
JavaCC grammar files use the extension .jj. This plugin can
be used to locate and process all grammar files within a
specified directory. Java source files will be written to a
common generated-sources output directory, typically located
in the build output directory. By default, the plugin will
run during the generate-sources phase, but it can be
configured to run in other phases as well.
The plugin can also be be used to call the JJTree and JTB
tools. JJTree is a preprocessor for JavaCC that inserts parse
tree building actions at various places in the JavaCC source.
More information about JJTree can be found on the JJTree site.
JTB (Java Tree Builder) is another syntax tree builder. Just
like JJTree, it works as a preprocessor for JavaCC grammar
files and inserts code to build syntax trees from a parsed
input stream. More information about JTB in general and a
feature comparison with JJTree can be found on the JTB web site.
Finally, this plugin contains a goal for running JJDoc. JJDoc
is a simple tool that generates BNF documentation for the JavaCC
grammar files. This can be used to generate a report for your
project site using the Maven reporting tools.

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
cp -p target/javacc-maven-plugin-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}-%{namedversion}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{namedversion}*; do ln -s ${jar} `echo ${jar} | sed "s|-%{namedversion}||g"`; done)
# compat symlinks for obsoleted rpms
mkdir -p %{buildroot}%{_javadir}/mojo
ln -sf ../%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/mojo/javacc-maven-plugin.jar

# poms
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.codehaus.mojo javacc-maven-plugin %{namedversion} JPP %{name}

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
ln -s %{name}-%{namedversion} %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}-%{namedversion}.jar
%{_javadir}/%{name}.jar
%{_javadir}/mojo/javacc-maven-plugin.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{namedversion}
%{_javadocdir}/%{name}

%changelog
* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_1jpp6
- separate package

