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

%bcond_with repolib

Name:           oss-parent
Version:        6
Release:        alt2_2jpp6
Epoch:          0
Summary:        Sonatype OSS Parent
License:        LGPLv2+
Group:          Development/Java
URL:            http://repository.sonatype.org/
Source0:	oss-parent-6.tar.bz2
Provides:       sonatype-oss-parent = %{epoch}:%{version}-%{release}
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
BuildRequires:  commons-parent
BuildRequires:  jpackage-utils
BuildRequires:  maven2
BuildRequires:  maven2-plugin-deploy
BuildRequires:  maven2-plugin-enforcer
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-source
BuildArch:      noarch
Source44: import.info

%description
Sonatype helps open source projects to set up maven repositories on
http://oss.sonatype.org.

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

%build
%if %with repolib
export MAVEN_REPO_LOCAL=`pwd`/.m2/repository
export ALT_DEPLOYMENT_REPOSITORY=oss-releases::default::file:`pwd`/maven2-brew
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -DaltDeploymentRepository=${ALT_DEPLOYMENT_REPOSITORY} \
        
%endif

%install

%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.sonatype.oss oss-parent %{version} JPP %{name}

%if %with repolib
%{__mkdir_p} %{buildroot}%{_javadir}/repository.jboss.com
%{__cp} -pr maven2-brew %{buildroot}%{_javadir}/repository.jboss.com
%endif

%files
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}*
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 0:6-alt2_2jpp6
- fixed build with maven3
- disabled repolib

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:6-alt1_2jpp6
- new jpp relase

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:3-alt1_0.1jpp6
- new version

