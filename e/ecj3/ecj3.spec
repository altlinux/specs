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

%bcond_with repolib


Name:           ecj3
Version:        3.7
Release:        alt2_1jpp6
Epoch:          1
Summary:        Eclipse Compiler for Java
Group:          Development/Java
License:        EPL
URL:            http://www.eclipse.org/
Source0:        http://mirrors.ibiblio.org/pub/mirrors/eclipse/eclipse/downloads/drops/R-3.7-201106131736/ecjsrc-3.7.jar
Source1:        core-3.7.pom
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
BuildRequires:  ant
BuildRequires:  jpackage-utils
%if %with repolib
BuildRequires:  maven2-plugin-deploy
%endif
BuildArch:      noarch
Source44: import.info

%description
Eclipse Compiler for Java.

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
%setup -q -c

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 
%if %with repolib
export MAVEN_REPO_LOCAL=`pwd`/.m2/repository
export URL=file:`pwd`/maven2-brew
mvn-jpp -e -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  deploy:deploy-file -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -DpomFile=%{SOURCE1}  -Dfile=ecj.jar -Durl=${URL} -DrepositoryId=oss-releases
%endif

%install

%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p ecj.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.eclipse.jdt core %{version} JPP %{name}

%if %with repolib
%{__mkdir_p} %{buildroot}%{_javadir}/repository.jboss.com
%{__cp} -pr maven2-brew %{buildroot}%{_javadir}/repository.jboss.com
%endif

%files
%{_javadir}*/%{name}-%{version}.jar
%{_javadir}*/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}*
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.7-alt2_1jpp6
- fixed build with maven3

* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.7-alt1_1jpp6
- new jpp relase

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 1:3.6-alt1_2jpp6
- new version

