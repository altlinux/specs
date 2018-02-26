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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_with repolib

%define parent_version 1.1
%define project_version 1.2
%define project_site_version 1.2
%define server_root_version 1.1
%define server_site_version 1.0
%define server_site_real_version 2.2.0
%define server_site_real_versiond 2-2-0

Name:           james-project
Version:        %{project_version}
Release:        alt2_2jpp6
Epoch:          0
Summary:        Apache JAMES Project
License:        ASL 2.0
Group:          Development/Java
URL:            http://james.apache.org/
# svn export http://svn.apache.org/repos/asf/james/project/tags/james-project-1.2/ && tar cjf james-project-1.2.tar.bz2 james-project-1.2
# Exported revision 1048881.
Source0:        james-project-1.2.tar.bz2
Source1:        james-project-jpp-depmap.xml
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jpackage-utils
Requires: james-parent >= 0:%{parent_version}
BuildRequires: apache-commons-parent
BuildRequires: james-parent >= 0:%{parent_version}
BuildRequires: jpackage-utils
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-deploy
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-source
BuildArch:      noarch
Source44: import.info

%description
The Apache JAMES Project.

%package -n james-server-root
Summary:        JAMES Server
Version:        %{server_root_version}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{project_version}-%{release}
Requires: james-server-site-2-2-0 = %{epoch}:%{server_site_version}-%{release}

%description -n james-server-root
Apache JAMES Server.

%package -n james-server-site-%{server_site_real_versiond}
Summary:        JAMES Server %{server_site_real_version} Documentation
Version:        %{server_site_version}
Group:          Development/Java
Requires: james-server-root = %{epoch}:%{server_root_version}-%{release}

%description -n james-server-site-%{server_site_real_versiond}
Apache JAMES Server %{server_site_real_version} Documentation.

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
export MAVEN_REPO_LOCAL=$(pwd)/maven2-brew
%{__mkdir_p} ${MAVEN_REPO_LOCAL}
%{_bindir}/mvn-jpp -e \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        -DaltDeploymentRepository=oss-releases::default::file://$(pwd)/maven2-brew \
	install \
         javadoc:javadoc

%install

%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms

%if 0
%{__cp} -p maven2-brew/org/apache/james/james-project/%{project_version}/james-project-%{project_version}-site.xml
%endif
%if 0
%{__cp} -p maven2-brew/org/apache/james/james-project/%{project_version}/james-project-%{project_version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP-james-project.pom
%else
%{__cp} -p maven2-brew/org/apache/james/james-project/*/james-project-*.pom %{buildroot}%{_datadir}/maven2/poms/JPP-james-project.pom
%endif
%add_to_maven_depmap org.apache.james james-project %{project_version} JPP james-project

%if 0
%{__cp} -p maven2-brew/org/apache/james/james-server-root/%{server_root_version}/james-server-root-%{server_root_version}-site.xml
%endif
%if 0
%{__cp} -p maven2-brew/org/apache/james/james-server-root/%{server_root_version}/james-server-root-%{server_root_version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP-james-server-root.pom
%else
%{__cp} -p maven2-brew/org/apache/james/james-server-root/*/james-server-root-*.pom %{buildroot}%{_datadir}/maven2/poms/JPP-james-server-root.pom
%endif
%add_to_maven_depmap org.apache.james james-server-root %{server_root_version} JPP james-server-root

%if 0
%{__cp} -p maven2-brew/org/apache/james/james-server-site-%{server_site_real_versiond}/%{server_site_version}/james-server-site-%{server_site_real_versiond}-%{server_site_version}-site.xml
%endif
%if 0
%{__cp} -p maven2-brew/org/apache/james/james-server-site-%{server_site_real_versiond}/%{server_site_version}/james-server-site-%{server_site_real_versiond}-%{server_site_version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP-james-server-site-%{server_site_real_versiond}.pom
%else
%{__cp} -p maven2-brew/org/apache/james/james-server-site-%{server_site_real_versiond}/*/james-server-site-%{server_site_real_versiond}-*.pom %{buildroot}%{_datadir}/maven2/poms/JPP-james-server-site-%{server_site_real_versiond}.pom
%endif
%add_to_maven_depmap org.apache.james james-server-site-%{server_site_real_versiond} %{server_site_version} JPP james-server-site-%{server_site_real_versiond}

%if %with repolib
%{__mkdir_p} %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
%{__cp} -pr maven2-brew/* %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
%endif

%files
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files -n james-server-root
%{_datadir}/maven2/poms/JPP-james-server-root.pom

%files -n james-server-site-%{server_site_real_versiond}
%{_datadir}/maven2/poms/JPP-james-server-site-%{server_site_real_versiond}.pom

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_2jpp6
- fixed build with maven3

* Sun Jan 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_2jpp6
- new version

