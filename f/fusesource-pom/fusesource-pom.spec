Patch33: fusesource-pom-1.8-migration-to-component-metadata.patch
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

Name:           fusesource-pom
Version:        1.8
Release:        alt4_1jpp6
Epoch:          0
Summary:        FuseSource POM
License:        ASL 2.0
Group:          Development/Java
URL:            http://labs.jboss.com/jboss/
%if 0
mkdir -p fusesource-pom-1.8 && cd fusesource-pom-1.8 && wget -U "" http://repo1.maven.org/maven2/org/fusesource/fusesource-pom/1.8/fusesource-pom-1.8.pom && mv fusesource-pom-1.8.pom pom.xml && cd ..  && \
    tar cjf fusesource-pom-1.8.tar.bz2 fusesource-pom-1.8
%endif
Source0:        fusesource-pom-1.8.tar.bz2
Patch0: fusesource-pom-pom.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
Requires:       maven2
Requires:       maven2-plugin-antrun
Requires:       maven2-plugin-clean
Requires:       maven2-plugin-compiler
Requires:       maven2-plugin-deploy
Requires:       maven2-plugin-docck
Requires:       maven2-plugin-enforcer
Requires:       maven2-plugin-install
Requires:       maven2-plugin-invoker
Requires:       maven2-plugin-jar
Requires:       maven2-plugin-javadoc
Requires:       maven2-plugin-plugin
Requires:       maven2-plugin-release
Requires:       maven2-plugin-resources
Requires:       maven2-plugin-remote-resources
Requires:       maven2-plugin-site
Requires:       maven2-plugin-source
Requires:       maven-surefire-plugin
Requires:       maven-wagon
#Requires:       plexus-maven-plugin
Requires:	plexus-containers-component-metadata
Requires:       modello-maven-plugin
BuildRequires:  maven2
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-clean
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-deploy
BuildRequires:  maven2-plugin-docck
BuildRequires:  maven2-plugin-enforcer
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-invoker
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven2-plugin-release
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-remote-resources
BuildRequires:  maven2-plugin-site
BuildRequires:  maven2-plugin-source
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-wagon
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  modello-maven-plugin
BuildRequires:  jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
This is a shared POM parent for FuseSource Maven projects.

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
%patch33

%build
#mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
#        -DaltDeploymentRepository=jboss-releases::default::file://$(pwd)/maven2-brew \
        

%install

%add_to_maven_depmap org.fusesource fusesource-pom %{version} JPP %{name}

%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

%if %with repolib
%{__mkdir_p} %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
%{__cp} -pr maven2-brew/* %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
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
* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt4_1jpp6
- dropped unused plexus-maven-plugin dependencies

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt3_1jpp6
- build w/o plexus-maven-plugin

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt2_1jpp6
- fixed build with maven3; disabled repolib

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_1jpp6
- new jpp relase

* Mon Aug 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_3jpp6
- maven1 translation

* Fri Mar 18 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_3jpp6
- fixed modello plugin dependency

* Fri Feb 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_3jpp6
- new version

