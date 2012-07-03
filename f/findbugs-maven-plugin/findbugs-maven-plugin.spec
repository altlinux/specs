BuildRequires: /proc maven-plugin-descriptor
BuildRequires: jpackage-compat
%define version 2.3.2
%define name findbugs-maven-plugin
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

%define reltag SNAPSHOT
%global namedversion %{version}-%{reltag}

Name:           findbugs-maven-plugin
Version:        2.3.2
Release:        alt2_0.3.SNAPSHOTjpp6
Epoch:          0
Summary:        FindBugs Maven Plugin
Group:          Development/Java
License:        MIT and ASL 2.0
URL:            http://mojo.codehaus.org/findbugs-maven-plugin/
# svn export https://svn.codehaus.org/mojo/trunk/mojo/findbugs-maven-plugin/ findbugs-maven-plugin-2.3.2 && tar cjf findbugs-maven-plugin-2.3.2.tar.bz2 findbugs-maven-plugin-2.3.2
# Exported revision 13608.
Source0:        findbugs-maven-plugin-2.3.2.tar.bz2
Source1:        findbugs-maven-plugin-settings.xml
Source2:        findbugs-maven-plugin-jpp-depmap.xml
Patch0:         findbugs-maven-plugin-pom.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       findbugs >= 0:1.3.9
Requires:       gmaven
Requires:       jpackage-utils
Requires:       mojo-parent
Requires:       plexus-utils
BuildRequires:  findbugs >= 0:1.3.9
BuildRequires:  gmaven
BuildRequires:  gmaven-runtime-1.5
BuildRequires:  gmaven-runtime-1.7
BuildRequires:  plexus-utils
BuildRequires:  mojo-maven2-plugin-cobertura
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven2-plugin-pmd
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-checkstyle
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-eclipse
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-enforcer
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven2-plugin-site
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-doxia
BuildRequires:  mojo-parent
BuildRequires:  junit4
BuildArch:      noarch
Source44: import.info

%description
This Plug-In generates reports based on the FindBugs Library.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

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
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        package javadoc:aggregate

%install

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p target/findbugs-maven-plugin-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}-%{namedversion}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{namedversion}*; do ln -s ${jar} `echo ${jar} | sed "s|-%{namedversion}||g"`; done)

# poms
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.codehaus.mojo findbugs-maven-plugin %{namedversion} JPP %{name}

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
ln -s %{name}-%{namedversion} %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}-%{namedversion}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{namedversion}
%{_javadocdir}/%{name}

%changelog
* Wed Mar 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3.2-alt2_0.3.SNAPSHOTjpp6
- fixed build with maven3

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3.2-alt1_0.3.SNAPSHOTjpp6
- disabled xfire

