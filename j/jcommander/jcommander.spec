BuildRequires: maven2-plugin-enforcer
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 1.18
%define name jcommander
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

%bcond_with repolib

%global namedversion %{version}

Name:           jcommander
Version:        1.18
Release:        alt3_1jpp6
Epoch:          0
Summary:        A Java framework to parse command line options with annotations
License:        ASL 2.0
Group:          Development/Java
URL:            http://jcommander.org
# git clone https://github.com/cbeust/jcommander.git && cd jcommander && git archive --prefix="jcommander-1.18/" --format=tar jcommander-1.18 | bzip2 > ../jcommander-1.18.tar.bz2
Source0:        jcommander-1.18.tar.bz2
Patch0:         jcommander-pom.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
BuildRequires:  oss-parent >= 0:3
# XXX: 6.1.1
# FIXME: circular
#BuildRequires:  testng
BuildRequires:  maven2
# XXX: 2.1.0
BuildRequires:  maven-plugin-bundle
# XXX: 2.3.1
BuildRequires:  maven2-plugin-compiler
# XXX: 2.3.1
BuildRequires:  maven2-plugin-jar
# XXX: 2.7
BuildRequires:  maven2-plugin-javadoc
# XXX: 2.4.1
BuildRequires:  maven2-plugin-resources
# XXX: 2.1.1
BuildRequires:  maven2-plugin-source
# XXX: 2.7.1
BuildRequires:  maven-surefire-plugin
BuildArch:      noarch
Source44: import.info

%description
A Java framework to parse command line options with annotations.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

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
%patch0 -p1 -b .sav0

%build
export MAVEN_REPO_LOCAL=`pwd`/.m2/repository
export MAVEN_OPTS="-Xms1g -Xmx1g"
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -DaltDeploymentRepository=${ALT_DEPLOYMENT_REPOSITORY} -Dmaven.test.skip install javadoc:aggregate

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p target/jcommander-%{namedversion}-sources.jar %{buildroot}%{_javadir}/%{name}-%{namedversion}-sources.jar
%{__cp} -p target/jcommander-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}-%{namedversion}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{namedversion}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} -e "s|-%{namedversion}||g"`; done)

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom


# depmaps
%add_to_maven_depmap com.beust jcommander %{namedversion} JPP %{name}

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
ln -s %{name}-%{namedversion} %{buildroot}%{_javadocdir}/%{name}

%if %with repolib
mkdir -p %{buildroot}%{_javadir}/repository.jboss.com
cp -pr maven2-brew %{buildroot}%{_javadir}/repository.jboss.com
%endif

%files
%{_javadir}*/%{name}-%{namedversion}-sources.jar
%{_javadir}*/%{name}-sources.jar
%{_javadir}*/%{name}-%{namedversion}.jar
%{_javadir}*/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{namedversion}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}*
%exclude %dir %{_javadocdir}
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.18-alt3_1jpp6
- fixed build with maven3

* Fri Jan 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.18-alt2_1jpp6
- fixed build

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.18-alt1_1jpp6
- jpp6 release

