BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 0.0.2
%define name maven-notice-plugin
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

#def_with repolib
%bcond_with repolib

%define repodir %{_javadir}/repository.jboss.com/org/apache/httpcomponents/%{name}/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define namedversion %{version}

Name:           maven-notice-plugin
Version:        0.0.2
Release:        alt1_1jpp6
Epoch:          0
Summary:        Maven NOTICE and LICENSE plugin
License:        ASL 2.0
URL:            http://svn.apache.org/repos/asf/httpcomponents/maven-notice-plugin
Group:          Development/Java
# svn export http://svn.apache.org/repos/asf/httpcomponents/maven-notice-plugin/tags/0.0.2-RC1/ maven-notice-plugin-0.0.2 && tar cjf maven-notice-plugin-0.0.2.tar.bz2 maven-notice-plugin-0.0.2
# Exported revision 1042827.
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source4:        %{name}-component-info.xml
Patch0:         maven-notice-plugin-pom.patch
Patch1:         maven2-plugin-notice-NoticeMojo-constructor.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jakarta-commons-io
Requires: jpackage-utils
Requires: maven2
BuildRequires: apache-commons-parent >= 0:7
BuildRequires: jakarta-commons-io
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-invoker
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-release
BuildRequires: maven-surefire-maven-plugin
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: junit
BuildArch:      noarch
Source44: import.info

%description
Maven plugin for automatic generation of NOTICE and LICENSE resources.

%if 0
%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.
%endif

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
%setup -q 
%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1

cp -p %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%build
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
export M2_SETTINGS=$(pwd)/settings.xml
%{_bindir}/mvn-jpp \
                -e \
                -s ${M2_SETTINGS} \
                -Dmaven2.jpp.depmap.file=%{SOURCE2} \
                -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
                install \
%if 0
                javadoc:aggregate
%endif

%install

# jars
mkdir -p %{buildroot}%{_javadir}
mkdir -p %{buildroot}%{_datadir}/maven2/poms
install -p -m 644 target/%{name}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -s ${jar} `/bin/echo $jar | sed "s|-%{version}||g"`; done)

# pom
install -p -m 644 pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache.httpcomponents maven-notice-plugin %{namedversion} JPP %{name}

%if 0
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%endif

%if %with repolib
mkdir -p %{buildroot}%{repodir}
mkdir -p %{buildroot}%{repodirlib}
install -p -m 644 %{SOURCE4} %{buildroot}%{repodir}/component-info.xml
tag=`echo %{namedversion}-brew`
sed -i "s/@VERSION@/$tag/g" %{buildroot}%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
mkdir -p %{buildroot}%{repodirsrc}
cp -p %{SOURCE0} %{buildroot}%{repodirsrc}
cp -p %{PATCH0} %{buildroot}%{repodirsrc}
cp -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/%{name}.jar
cp -p %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom %{buildroot}%{repodirlib}/%{name}.pom
%endif

%files
%{_javadir}*/%{name}-%{version}.jar
%{_javadir}*/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%if 0
%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%endif

%if %with repolib
%files repolib
%dir %{_javadir}*
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.0.2-alt1_1jpp6
- new version

