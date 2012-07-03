BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without repolib


Name:           jbossorg-docbook-xslt
Version:        1.1.0
Release:        alt2_2jpp6
Epoch:          0
Summary:        JBoss.org DocBook XSLT
License:        LGPLv2+
Url:            http://www.jboss.org/
Group:          Development/Java
# svn export http://anonsvn.jboss.org/repos/jbossas/tags/JBossOrg_DocBook_XSLT_1_1_0_GA/ jbossorg-docbook-xslt-1.1.0
Source0:        jbossorg-docbook-xslt-1.1.0.tar.gz
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Patch0:         docbook-pom-xml.patch
Patch1:         jbossorg-docbook-xslt-fop.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
Requires:       docbook-xsl >= 0:1.75.0
Requires:       jhighlight >= 0:1.0
BuildRequires:  commons-parent >= 0:5
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-wagon
BuildRequires:  maven2
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-deploy
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-resources
BuildRequires:  docbook-xsl >= 0:1.75.0
BuildRequires:  jhighlight >= 0:1.0
BuildArch:      noarch
Source44: import.info

%description
The main project to transform DocBook XML into XHTML and
other formats for JBoss.org Documentation.

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
export LANG=en_US.UTF-8
export M2_SETTINGS=$(pwd)/settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s ${M2_SETTINGS} \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -DaltDeploymentRepository=jboss-releases::default::file://$(pwd)/maven2-brew \
        deploy

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} ${jar/-%{version}/}; done)

%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.jboss jbossorg-docbook-xslt %{version} JPP %{name}

%if %with repolib
%{__mkdir_p} %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
%{__cp} -pr maven2-brew/* %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
%endif

%files
%{_javadir}*/%{name}-%{version}.jar
%{_javadir}*/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}*/
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Mon Feb 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt2_2jpp6
- new jpp relase

* Thu Sep 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt2_1jpp5
- fixed build with new maven 2.0.8

* Mon Jun 15 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_1jpp5
- new version

