BuildRequires: maven2-plugin-compiler maven-surefire-maven-plugin maven2-plugin-jar maven2-plugin-install maven2-plugin-javadoc jmock maven-doxia-sitetools
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

Name:           swingx
Version:        1.6
Release:        alt2_1jpp6
Summary:        Extensions to the Swing GUI toolkit

Group:          Development/Java
License:        LGPL
URL:            https://swingx.dev.java.net/

Source0:        https://swingx.dev.java.net/files/documents/2981/144879/swingx-1.6-src.zip

Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Patch0:         swingx-pom.patch


BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-provider-junit4
BuildRequires: mojo-maven2-plugin-emma
BuildRequires: jhlabs-filters
BuildRequires: junit4

Requires: jpackage-utils >= 0:5.0.0
Requires: jhlabs-filters

Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0

BuildArch:      noarch
Source44: import.info

%description
Contains extensions to the Swing GUI toolkit, including new
and enhanced components that provide functionality commonly
required by rich client applications. Highlights include:
* Sorting, filtering, highlighting for tables, trees, and lists
* Find/search
* Auto-completion
* Login/authentication framework
* TreeTable component
* Collapsible panel component
* Date picker component
* Tip-of-the-Day component
Many of these features will eventually be incorporated into
the Swing toolkit, although API compatibility will not be
guaranteed. The SwingX project focuses exclusively on the
raw components themselves.

%package javadoc 
Summary:        Javadocs for %{name} 
Group:          Development/Java
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
 
%description javadoc 
%{summary}. 

%prep
%setup -q -n %{name}-%{version}-src 
cp -p %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
%patch0 -b .orig
mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}
export MAVEN_OPTS="-Dmaven2.jpp.mode=true -Dmaven2.jpp.depmap.file=%{SOURCE2} -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -Djava.awt.headless=true -Daggregate=true -Dallow.test.failure.ignore=true -Dmaven.test.failure.ignore=true"
export MAVEN_SETTINGS=$(pwd)/settings.xml

%{_bindir}/mvn-jpp \
        -e \
        -s $MAVEN_SETTINGS \
        install javadoc:javadoc


%install
%__rm -rf %{buildroot}

# jar
%__mkdir_p %{buildroot}%{_javadir}
%__install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%{version}/}; done)

# poms
%__mkdir_p %{buildroot}%{_datadir}/maven2/poms
%__install -m 644 pom.xml \
               $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# javadoc 
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version} 
%__cp -a target/site/apidocs/* \
               %{buildroot}%{_javadocdir}/%{name}-%{version}
%__ln_s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} 

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc 
%{_javadocdir}/%{name}-%{version} 
%{_javadocdir}/%{name} 

%changelog
* Sun Jan 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.6-alt2_1jpp6
- fixed build

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_1jpp6
- new version

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1_7jpp6
- new version

