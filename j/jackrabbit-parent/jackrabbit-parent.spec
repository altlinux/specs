#BuildRequires: maven-shared-doxia-tools
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
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

%bcond_without repolib

Name:           jackrabbit-parent
Version:        5
Release:        alt2_1jpp6
Epoch:          0
Summary:        Apache Jackrabbit
License:        ASL 2.0
Group:          Development/Java
URL:            http://labs.jackrabbit.com/jackrabbit/
# svn export http://svn.apache.org/repos/asf/jackrabbit/parent/tags/5 jackrabbit-parent-5 && tar cjf jackrabbit-parent-5.tar.bz2 jackrabbit-parent-5
# Exported revision 1151163.
Source0:        jackrabbit-parent-5.tar.bz2
Patch0:         jackrabbit-parent-pom.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
BuildRequires:  maven2
BuildRequires:  maven2-plugin-deploy
BuildRequires:  jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
Apache Jackrabbit is an open source project for creating and maintaining
software and documentation related to the Content Repository for Java
Technology API (JCR) and its implementation as the Apache Jackrabbit
content repository.

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
#export MAVEN_REPO_LOCAL=`pwd`/.m2/repository
#export ALT_DEPLOYMENT_REPOSITORY=oss-releases::default::file:`pwd`/maven2-brew
#mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -DaltDeploymentRepository=${ALT_DEPLOYMENT_REPOSITORY} deploy

%install

%add_to_maven_depmap org.apache.jackrabbit parent %{version} JPP %{name}

%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

%if %with repolib
%{__mkdir_p} %{buildroot}%{_javadir}/repository.jboss.com
%{__cp} -pr maven2-brew %{buildroot}%{_javadir}/repository.jboss.com
%endif

%files
%doc LICENSE.txt NOTICE.txt
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:5-alt2_1jpp6
- fixed build

* Thu Sep 15 2011 Igor Vlasenko <viy@altlinux.ru> 0:5-alt1_1jpp6
- new version

