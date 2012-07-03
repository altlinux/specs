BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define reltag %{nil}
%define namedversion %{version}%{?reltag}

Name:           jbosscache-support
Version:        1.6
Release:        alt2_2jpp6
Epoch:          0
Summary:        JBoss Cache Support Modules
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn -q export http://anonsvn.jboss.org/repos/jbosscache/support/tags/1.6/ jbosscache-support-1.6 && tar cjf jbosscache-support-1.6.tar.bz2 jbosscache-support-1.6
Source0:        jbosscache-support-1.6.tar.bz2
Source1:        jbosscache-support-jpp-depmap.xml
Source2:        jbosscache-support-settings.xml
Patch0:         jbosscache-support-common-pom.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jpackage-utils
BuildRequires: commons-parent >= 0:9
BuildRequires: maven-shared-filtering
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: log4j >= 0:1.2.14
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-deploy
BuildRequires: maven2-plugin-eclipse
BuildRequires: maven2-plugin-enforcer
BuildRequires: maven2-plugin-idea
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin
BuildRequires: testng >= 0:5.1
BuildArch:      noarch
Source44: import.info

%description
Grouping of JBoss Cache support modules.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires: jpackage-utils
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
%patch0 -p0 -b .sav0


%build
export MAVEN_REPO_LOCAL=$(pwd)/maven2-brew
%{_bindir}/mvn-jpp -e \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        -Dmaven.test.skip=true \
        -DaltDeploymentRepository=oss-releases::default::file://$(pwd)/maven2-brew \
	install        

find maven2-brew \! -path '*/org/jboss/cache/*' -type f -print -delete ||:
find maven2-brew -exec rmdir -p {} \; 2>/dev/null ||:

%install

pushd maven2-brew

# jars
mkdir -p %{buildroot}%{_javadir}/%{name}
cp -p org/jboss/cache/jbosscache-doc-xslt-support/%{namedversion}/jbosscache-doc-xslt-support-%{namedversion}-sources.jar %{buildroot}%{_javadir}/%{name}
cp -p org/jboss/cache/jbosscache-doc-xslt-support/%{namedversion}/jbosscache-doc-xslt-support-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{namedversion}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} -e "s|-%{namedversion}||g"`; done)

# poms
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p org/jboss/cache/jbosscache-common-parent/%{namedversion}/jbosscache-common-parent-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jbosscache-common-parent.pom
cp -p org/jboss/cache/jbosscache-doc-xslt-support/%{namedversion}/jbosscache-doc-xslt-support-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jbosscache-doc-xslt-support.pom
cp -p org/jboss/cache/jbosscache-support/%{namedversion}/jbosscache-support-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jbosscache-support.pom

popd

# depmaps
%add_to_maven_depmap org.jboss.cache jbosscache-common-parent %{namedversion} JPP/%{name} jbosscache-common-parent
%add_to_maven_depmap org.jboss.cache jbosscache-doc-xslt-support %{namedversion} JPP/%{name} jbosscache-doc-xslt-support
%add_to_maven_depmap org.jboss.cache jbosscache-support %{namedversion} JPP/%{name} jbosscache-support

%if %with repolib
# repolib
mkdir -p %{buildroot}%{_javadir}/repository.jboss.com
cp -pr maven2-brew %{buildroot}%{_javadir}/repository.jboss.com
%endif

%files
%dir %{_javadir}*/%{name}
%{_javadir}*/%{name}/jbosscache-doc-xslt-support-%{namedversion}-sources.jar
%{_javadir}*/%{name}/jbosscache-doc-xslt-support-sources.jar
%{_javadir}*/%{name}/jbosscache-doc-xslt-support-%{namedversion}.jar
%{_javadir}*/%{name}/jbosscache-doc-xslt-support.jar
%{_datadir}/maven2/poms/JPP.%{name}-jbosscache-common-parent.pom
%{_datadir}/maven2/poms/JPP.%{name}-jbosscache-doc-xslt-support.pom
%{_datadir}/maven2/poms/JPP.%{name}-jbosscache-support.pom
%{_mavendepmapfragdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}*
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_2jpp6
- fixed build with maven3

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_2jpp6
- new version

