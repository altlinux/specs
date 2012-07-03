BuildRequires: xpp3-minimal
Patch33: gshell-2.6.2-alt-no-deploy.patch
BuildRequires: /proc apache-commons-jexl
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 2.6.2
%define name gshell
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

#def_with gcj_support
%bcond_with gcj_support
%bcond_with repolib

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define namedversion %{version}


Name:           gshell
Version:        2.6.2
Release:        alt3_0jpp6
Epoch:          0
Summary:        GShell
License:        ASL 2.0
URL:            http://sonatype.org
Group:          Development/Java
# git clone git://github.com/sonatype/gshell.git && cd gshell && git checkout gshell-2.6.2 && rm -rf .git && cd .. && mv gshell gshell-2.6.2 && tar cjf gshell-2.6.2.tar.bz2 gshell-2.6.2
Source0:        gshell-2.6.2.tar.bz2
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Patch0:         gshell-pom.patch
Patch1:         gshell-javacc.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jakarta-commons-vfs >= 0:1.0
Requires:       jpackage-utils
Requires:       oro >= 0:2.0.8
Requires:       google-guice >= 0:2.0
Requires:       sisu-guice >= 0:2.9.2
BuildRequires:  apache-commons-parent
# XXX: 1.4
BuildRequires:  apache-jar-resource-bundle >= 0:1.2
BuildRequires:  bsf >= 0:2.4.0
BuildRequires:  forge-parent >= 0:5
BuildRequires:  google-guice >= 0:2.0
BuildRequires:  sonatype-gossip >= 0:1.5
BuildRequires:  jakarta-commons-cli >= 0:1.2
BuildRequires:  apache-commons-jexl >= 0:1.1
BuildRequires:  jakarta-commons-vfs >= 0:1.0
BuildRequires:  mojo-maven2-plugin-javacc >= 0:2.6
BuildRequires:  junit
BuildRequires:  jline2 >= 0:2.5
BuildRequires:  logback
BuildRequires:  maven2-plugin-dependency
BuildRequires:  maven2-plugin-release
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  oro >= 0:2.0.8
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-container-default
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-utils
BuildRequires:  sisu
BuildRequires:  sisu-guice >= 0:2.9.2
BuildRequires:  slf4j
BuildRequires:  xstream
BuildArch:      noarch
Source44: import.info

%description
GShell.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%if 0
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
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
%patch33

%{__rm} gshell-core/src/main/java/org/sonatype/gshell/parser/impl/AST*.java

# FIXME: needs some dependencies
#%{__rm} -r gshell-core/src/main/java/org/sonatype/gshell/guice

%build
export MAVEN_REPO_LOCAL=$(pwd)/maven2-brew
%{_bindir}/mvn-jpp \
        -e \
        -Dmaven2.jpp.mode=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -DaltDeploymentRepository=oss-releases::default::file://$(pwd)/maven2-brew \
        -Dmaven.test.skip.exec=true \
        -DskipAssembly=true \
         install \
        javadoc:aggregate \
%if 0
        site
%endif

%install

pushd maven2-brew
mkdir -p %{buildroot}%{_javadir}/%{name}
cp -p org/sonatype/gshell/commands/gshell-file/%{namedversion}/gshell-file-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/gshell/commands/gshell-logging/%{namedversion}/gshell-logging-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/gshell/commands/gshell-network/%{namedversion}/gshell-network-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/gshell/commands/gshell-pref/%{namedversion}/gshell-pref-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/gshell/commands/gshell-standard/%{namedversion}/gshell-standard-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/gshell/gshell-bootstrap/%{namedversion}/gshell-bootstrap-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/gshell/gshell-core/%{namedversion}/gshell-core-%{namedversion}-tests.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/gshell/gshell-core/%{namedversion}/gshell-core-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/gshell/gshell-gossip/%{namedversion}/gshell-gossip-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/gshell/gshell-launcher/%{namedversion}/gshell-launcher-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/gshell/gshell-plexus/%{namedversion}/gshell-plexus-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/gshell/gshell-ui/%{namedversion}/gshell-ui-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/gshell/gshell-util/%{namedversion}/gshell-util-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{namedversion}*; do ln -s ${jar} ${jar/-%{namedversion}/}; done)

mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p org/sonatype/gshell/commands/gshell-commands/%{namedversion}/gshell-commands-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gshell-commands.pom
cp -p org/sonatype/gshell/commands/gshell-file/%{namedversion}/gshell-file-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gshell-file.pom
cp -p org/sonatype/gshell/commands/gshell-logging/%{namedversion}/gshell-logging-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gshell-logging.pom
cp -p org/sonatype/gshell/commands/gshell-network/%{namedversion}/gshell-network-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gshell-network.pom
cp -p org/sonatype/gshell/commands/gshell-pref/%{namedversion}/gshell-pref-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gshell-pref.pom
cp -p org/sonatype/gshell/commands/gshell-standard/%{namedversion}/gshell-standard-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gshell-standard.pom
cp -p org/sonatype/gshell/gshell/%{namedversion}/gshell-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gshell.pom
cp -p org/sonatype/gshell/gshell-bootstrap/%{namedversion}/gshell-bootstrap-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gshell-bootstrap.pom
cp -p org/sonatype/gshell/gshell-core/%{namedversion}/gshell-core-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gshell-core.pom
cp -p org/sonatype/gshell/gshell-gossip/%{namedversion}/gshell-gossip-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gshell-gossip.pom
cp -p org/sonatype/gshell/gshell-launcher/%{namedversion}/gshell-launcher-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gshell-launcher.pom
cp -p org/sonatype/gshell/gshell-plexus/%{namedversion}/gshell-plexus-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gshell-plexus.pom
cp -p org/sonatype/gshell/gshell-ui/%{namedversion}/gshell-ui-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gshell-ui.pom
cp -p org/sonatype/gshell/gshell-util/%{namedversion}/gshell-util-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gshell-util.pom
popd

%add_to_maven_depmap org.sonatype.gshell.commands gshell-commands %{namedversion} JPP/%{name} gshell-commands
%add_to_maven_depmap org.sonatype.gshell.commands gshell-file %{namedversion} JPP/%{name} gshell-file
%add_to_maven_depmap org.sonatype.gshell.commands gshell-logging %{namedversion} JPP/%{name} gshell-logging
%add_to_maven_depmap org.sonatype.gshell.commands gshell-network %{namedversion} JPP/%{name} gshell-network
%add_to_maven_depmap org.sonatype.gshell.commands gshell-pref %{namedversion} JPP/%{name} gshell-pref
%add_to_maven_depmap org.sonatype.gshell.commands gshell-standard %{namedversion} JPP/%{name} gshell-standard
%add_to_maven_depmap org.sonatype.gshell gshell %{namedversion} JPP/%{name} gshell
%add_to_maven_depmap org.sonatype.gshell gshell-bootstrap %{namedversion} JPP/%{name} gshell-bootstrap
%add_to_maven_depmap org.sonatype.gshell gshell-core %{namedversion} JPP/%{name} gshell-core
%add_to_maven_depmap org.sonatype.gshell gshell-gossip %{namedversion} JPP/%{name} gshell-gossip
%add_to_maven_depmap org.sonatype.gshell gshell-launcher %{namedversion} JPP/%{name} gshell-launcher
%add_to_maven_depmap org.sonatype.gshell gshell-plexus %{namedversion} JPP/%{name} gshell-plexus
%add_to_maven_depmap org.sonatype.gshell gshell-ui %{namedversion} JPP/%{name} gshell-ui
%add_to_maven_depmap org.sonatype.gshell gshell-util %{namedversion} JPP/%{name} gshell-util

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
ln -s %{name}-%{namedversion} %{buildroot}%{_javadocdir}/%{name}

%if 0
# manual
mkdir -p %{buildroot}%{_docdir}/%{name}-%{namedversion}
cp -pr target/target/site/* %{buildroot}%{_docdir}/%{name}-%{namedversion}
rm -r %{buildroot}%{_docdir}/%{name}-%{namedversion}/apidocs
%endif

%if %with repolib
%{__mkdir_p} %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
%{__cp} -pr maven2-brew/* %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
%endif

%files
%doc README.md
%dir %{_javadir}*/%{name}
%exclude %dir %{_javadocdir}/%{name}
%{_javadir}/%{name}/gshell-standard-%{namedversion}.jar
%{_javadir}/%{name}/gshell-standard.jar
%{_javadir}/%{name}/gshell-bootstrap-%{namedversion}.jar
%{_javadir}/%{name}/gshell-bootstrap.jar
%{_javadir}/%{name}/gshell-core-%{namedversion}-tests.jar
%{_javadir}/%{name}/gshell-core-%{namedversion}.jar
%{_javadir}/%{name}/gshell-core-tests.jar
%{_javadir}/%{name}/gshell-core.jar
%{_javadir}/%{name}/gshell-file-%{namedversion}.jar
%{_javadir}/%{name}/gshell-file.jar
%{_javadir}/%{name}/gshell-gossip-%{namedversion}.jar
%{_javadir}/%{name}/gshell-gossip.jar
%{_javadir}/%{name}/gshell-launcher-%{namedversion}.jar
%{_javadir}/%{name}/gshell-launcher.jar
%{_javadir}/%{name}/gshell-logging-%{namedversion}.jar
%{_javadir}/%{name}/gshell-logging.jar
%{_javadir}/%{name}/gshell-network-%{namedversion}.jar
%{_javadir}/%{name}/gshell-network.jar
%{_javadir}/%{name}/gshell-plexus-%{namedversion}.jar
%{_javadir}/%{name}/gshell-plexus.jar
%{_javadir}/%{name}/gshell-pref-%{namedversion}.jar
%{_javadir}/%{name}/gshell-pref.jar
%{_javadir}/%{name}/gshell-ui-%{namedversion}.jar
%{_javadir}/%{name}/gshell-ui.jar
%{_javadir}/%{name}/gshell-util-%{namedversion}.jar
%{_javadir}/%{name}/gshell-util.jar
%{_datadir}/maven2/poms/JPP.%{name}-gshell-bootstrap.pom
%{_datadir}/maven2/poms/JPP.%{name}-gshell-commands.pom
%{_datadir}/maven2/poms/JPP.%{name}-gshell-core.pom
%{_datadir}/maven2/poms/JPP.%{name}-gshell-file.pom
%{_datadir}/maven2/poms/JPP.%{name}-gshell-gossip.pom
%{_datadir}/maven2/poms/JPP.%{name}-gshell-launcher.pom
%{_datadir}/maven2/poms/JPP.%{name}-gshell-logging.pom
%{_datadir}/maven2/poms/JPP.%{name}-gshell-network.pom
%{_datadir}/maven2/poms/JPP.%{name}-gshell-plexus.pom
%{_datadir}/maven2/poms/JPP.%{name}-gshell-pref.pom
%{_datadir}/maven2/poms/JPP.%{name}-gshell-standard.pom
%{_datadir}/maven2/poms/JPP.%{name}-gshell-ui.pom
%{_datadir}/maven2/poms/JPP.%{name}-gshell-util.pom
%{_datadir}/maven2/poms/JPP.%{name}-gshell.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{namedversion}
%{_javadocdir}/%{name}

%if 0
%files manual
%doc %{_docdir}/%{name}-%{namedversion}
%endif

%if %with repolib
%files repolib
%dir %{_javadir}*/
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6.2-alt3_0jpp6
- fixed build; added BR: xpp3-minimal

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6.2-alt2_0jpp6
- fixed build with maven3

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6.2-alt1_0jpp6
- build with mojo javacc plugin

* Mon Mar 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.6.2-alt0.1jpp
- bootstrap

