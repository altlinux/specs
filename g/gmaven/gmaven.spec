BuildRequires: mojo-parent
Patch33: gmaven-1.3-alt-fix-build.patch
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

#def_with shitty
%bcond_with shitty
#def_with gcj_support
%bcond_with gcj_support
%bcond_without repolib

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define namedversion 1.3

Name:           gmaven
Version:        1.3
Release:        alt3_3jpp6
Epoch:          0
Summary:        Groovy Maven Integration
Group:          Development/Java
License:        ASL 2.0
URL:            http://groovy.codehaus.org/GMaven
# svn export http://svn.codehaus.org/gmaven/tags/gmaven-1.3/ && tar cjf gmaven-1.3.tar.bz2 gmaven-1.3
# Exported revision 
Source0:        %{name}-%{namedversion}.tar.bz2
Source1:        %{name}-jpp-depmap.xml
Source2:        %{name}-settings.xml
Patch0:         gmaven-poms.patch
Patch1:         gmaven-gshell-io.patch
Patch2:         gmaven-javadoc.patch
Patch3:         gmaven-gossip.patch
Obsoletes:      mojo-maven2-groovy <= 0:16
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires:       ant
Requires:       codehaus-parent >= 0:1
Requires:       %{name}-provider = 0:1.5
Requires:       sonatype-gossip
Requires:       gshell
Requires:       jakarta-commons-lang
Requires:       jline
Requires:       jpackage-utils
Requires:       junit
Requires:       maven-shared-file-management
Requires:       maven-shared-reporting-impl
Requires:       plexus-container-default
Requires:       plexus-digest
Requires:       plexus-utils
Requires:       qdox
Requires:       slf4j
BuildRequires:  apache-jar-resource-bundle >= 0:1.3
BuildRequires:  codehaus-parent >= 0:1
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  junit
BuildRequires:  maven2 >= 0:2.0.7
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-dependency
BuildRequires:  maven2-plugin-deploy
BuildRequires:  maven2-plugin-enforcer
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-source
#BuildRequires:  maven-archetype2
BuildRequires:  maven-archetype
BuildRequires:  maven2-plugin-site
BuildRequires:  maven-surefire-plugin
BuildRequires:  mojo-maven2-plugin-build-helper
BuildRequires:  mojo-maven2-plugin-cobertura
%if %with shitty
BuildRequires:  mojo-maven2-plugin-shitty
%endif
#BuildRequires:  plexus-maven-plugin
BuildRequires:  ant
BuildRequires:  sonatype-gossip
BuildRequires:  groovy10
BuildRequires:  groovy15
BuildRequires:  groovy16
BuildRequires:  groovy17
BuildRequires:  gshell
BuildRequires:  jakarta-commons-lang
BuildRequires:  jline
BuildRequires:  junit
BuildRequires:  maven-shared-file-management
BuildRequires:  maven-shared-reporting-impl
BuildRequires:  plexus-container-default
BuildRequires:  plexus-digest
BuildRequires:  plexus-utils
BuildRequires:  qdox
BuildRequires:  slf4j
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info

%description
GMaven provides integration of the Groovy language into Maven.
With GMaven you can:
* Build Groovy Projects
* Execute Groovy Code
* Run Groovy Tools
* Implement Maven Plugins
Advanced:
* Groovy Runtime
* Advanced Configuration

%package runtime-1.5
Group:          Development/Java
Summary:        Groovy 1.5 Runtime for %{name}
Provides:       %{name}-provider = 0:1.5
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       groovy15

%description runtime-1.5
%{summary}.

%package runtime-1.6
Group:          Development/Java
Summary:        Groovy 1.6 Runtime for %{name}
Provides:       %{name}-provider = 0:1.6
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       groovy16

%description runtime-1.6
%{summary}.

%package runtime-1.7
Group:          Development/Java
Summary:        Groovy 1.7 Runtime for %{name}
Provides:       %{name}-provider = 0:1.7
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       groovy17

%description runtime-1.7
%{summary}.

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
%setup -q -n gmaven-%{namedversion}
%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1
%patch2 -p0 -b .sav2
%patch3 -p0 -b .sav3
%patch33 -p1 -b .sav33

%build
%{_bindir}/mvn-jpp -e \
        -Dmaven.repo.local=$(pwd)/maven2-brew \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        -DaltDeploymentRepository=oss-releases::default::file://$(pwd)/maven2-brew \
        install javadoc:aggregate

%install

# jars
mkdir -p %{buildroot}%{_javadir}/%{name}
pushd maven2-brew
cp -p org/codehaus/gmaven/archetypes/gmaven-archetype-basic/%{namedversion}/gmaven-archetype-basic-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/codehaus/gmaven/archetypes/gmaven-archetype-mojo/%{namedversion}/gmaven-archetype-mojo-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
#cp -p org/codehaus/gmaven/examples/clean-maven-plugin/%{namedversion}/clean-maven-plugin-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
#cp -p org/codehaus/gmaven/examples/install-maven-plugin/%{namedversion}/install-maven-plugin-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/codehaus/gmaven/feature/gmaven-feature-api/%{namedversion}/gmaven-feature-api-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/codehaus/gmaven/feature/gmaven-feature-support/%{namedversion}/gmaven-feature-support-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/codehaus/gmaven/gmaven-mojo/%{namedversion}/gmaven-mojo-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/codehaus/gmaven/gmaven-mojo-support/%{namedversion}/gmaven-mojo-support-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/codehaus/gmaven/gmaven-packaging/%{namedversion}/gmaven-packaging-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/codehaus/gmaven/gmaven-plugin/%{namedversion}/gmaven-plugin-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/codehaus/gmaven/gmaven-testsuite/%{namedversion}/gmaven-testsuite-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/codehaus/gmaven/runtime/gmaven-runtime-1.5/%{namedversion}/gmaven-runtime-1.5-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/codehaus/gmaven/runtime/gmaven-runtime-1.6/%{namedversion}/gmaven-runtime-1.6-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/codehaus/gmaven/runtime/gmaven-runtime-1.7/%{namedversion}/gmaven-runtime-1.7-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/codehaus/gmaven/runtime/gmaven-runtime-api/%{namedversion}/gmaven-runtime-api-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/codehaus/gmaven/runtime/gmaven-runtime-loader/%{namedversion}/gmaven-runtime-loader-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/codehaus/gmaven/runtime/gmaven-runtime-support/%{namedversion}/gmaven-runtime-support-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/codehaus/gmaven/support/filter-plugin/%{namedversion}/filter-plugin-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/codehaus/mojo/groovy-maven-plugin/%{namedversion}/groovy-maven-plugin-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
#cp -p org/codehaus/gmaven/archetypes/gmaven-archetype-basic/%{namedversion}/gmaven-archetype-basic-%{namedversion}.maven-archetype %{buildroot}%{_javadir}/%{name}/
#cp -p org/codehaus/gmaven/archetypes/gmaven-archetype-mojo/%{namedversion}/gmaven-archetype-mojo-%{namedversion}.maven-archetype %{buildroot}%{_javadir}/%{name}/
#cp -p org/codehaus/gmaven/gmaven/%{namedversion}/gmaven-%{namedversion}-site.xml %{buildroot}%{_javadir}/%{name}/
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{namedversion}*; do ln -s ${jar} `/bin/echo ${jar} | sed "s|-%{namedversion}||g"`; done)

mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p org/codehaus/gmaven/archetypes/gmaven-archetype-basic/%{namedversion}/gmaven-archetype-basic-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-archetype-basic.pom
cp -p org/codehaus/gmaven/archetypes/gmaven-archetype-mojo/%{namedversion}/gmaven-archetype-mojo-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-archetype-mojo.pom
cp -p org/codehaus/gmaven/archetypes/gmaven-archetypes/%{namedversion}/gmaven-archetypes-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-archetypes.pom
#cp -p org/codehaus/gmaven/examples/clean-maven-plugin/%{namedversion}/clean-maven-plugin-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-clean-maven-plugin.pom
#cp -p org/codehaus/gmaven/examples/gmaven-examples/%{namedversion}/gmaven-examples-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-examples.pom
#cp -p org/codehaus/gmaven/examples/install-maven-plugin/%{namedversion}/install-maven-plugin-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-install-maven-plugin.pom
cp -p org/codehaus/gmaven/feature/gmaven-feature/%{namedversion}/gmaven-feature-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-feature.pom
cp -p org/codehaus/gmaven/feature/gmaven-feature-api/%{namedversion}/gmaven-feature-api-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-feature-api.pom
cp -p org/codehaus/gmaven/feature/gmaven-feature-support/%{namedversion}/gmaven-feature-support-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-feature-support.pom
cp -p org/codehaus/gmaven/gmaven/%{namedversion}/gmaven-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven.pom
cp -p org/codehaus/gmaven/gmaven-mojo/%{namedversion}/gmaven-mojo-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-mojo.pom
cp -p org/codehaus/gmaven/gmaven-mojo-support/%{namedversion}/gmaven-mojo-support-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-mojo-support.pom
cp -p org/codehaus/gmaven/gmaven-packaging/%{namedversion}/gmaven-packaging-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-packaging.pom
cp -p org/codehaus/gmaven/gmaven-plugin/%{namedversion}/gmaven-plugin-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-plugin.pom
cp -p org/codehaus/gmaven/gmaven-testsuite/%{namedversion}/gmaven-testsuite-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-testsuite.pom
cp -p org/codehaus/gmaven/runtime/gmaven-runtime/%{namedversion}/gmaven-runtime-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-runtime.pom
cp -p org/codehaus/gmaven/runtime/gmaven-runtime-1.5/%{namedversion}/gmaven-runtime-1.5-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-runtime-1.5.pom
cp -p org/codehaus/gmaven/runtime/gmaven-runtime-1.6/%{namedversion}/gmaven-runtime-1.6-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-runtime-1.6.pom
cp -p org/codehaus/gmaven/runtime/gmaven-runtime-1.7/%{namedversion}/gmaven-runtime-1.7-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-runtime-1.7.pom
cp -p org/codehaus/gmaven/runtime/gmaven-runtime-api/%{namedversion}/gmaven-runtime-api-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-runtime-api.pom
cp -p org/codehaus/gmaven/runtime/gmaven-runtime-loader/%{namedversion}/gmaven-runtime-loader-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-runtime-loader.pom
cp -p org/codehaus/gmaven/runtime/gmaven-runtime-support/%{namedversion}/gmaven-runtime-support-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-runtime-support.pom
cp -p org/codehaus/gmaven/support/filter-plugin/%{namedversion}/filter-plugin-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-filter-plugin.pom
cp -p org/codehaus/gmaven/support/gmaven-support/%{namedversion}/gmaven-support-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-gmaven-support.pom
cp -p org/codehaus/mojo/groovy-maven-plugin/%{namedversion}/groovy-maven-plugin-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-groovy-maven-plugin.pom
popd

%add_to_maven_depmap org.codehaus.gmaven.archetypes gmaven-archetype-basic %{namedversion} JPP/%{name} gmaven-archetype-basic
%add_to_maven_depmap org.codehaus.gmaven.archetypes gmaven-archetype-mojo %{namedversion} JPP/%{name} gmaven-archetype-mojo
%add_to_maven_depmap org.codehaus.gmaven.archetypes gmaven-archetypes %{namedversion} JPP/%{name} gmaven-archetypes
#add_to_maven_depmap org.codehaus.gmaven.examples clean-maven-plugin %{namedversion} JPP/%{name} clean-maven-plugin
#add_to_maven_depmap org.codehaus.gmaven.examples gmaven-examples %{namedversion} JPP/%{name} gmaven-examples
#add_to_maven_depmap org.codehaus.gmaven.examples install-maven-plugin %{namedversion} JPP/%{name} install-maven-plugin
%add_to_maven_depmap org.codehaus.gmaven.feature gmaven-feature %{namedversion} JPP/%{name} gmaven-feature
%add_to_maven_depmap org.codehaus.gmaven.feature gmaven-feature-api %{namedversion} JPP/%{name} gmaven-feature-api
%add_to_maven_depmap org.codehaus.gmaven.feature gmaven-feature-support %{namedversion} JPP/%{name} gmaven-feature-support
%add_to_maven_depmap org.codehaus.gmaven gmaven %{namedversion} JPP/%{name} gmaven
%add_to_maven_depmap org.codehaus.gmaven gmaven-mojo %{namedversion} JPP/%{name} gmaven-mojo
%add_to_maven_depmap org.codehaus.gmaven gmaven-mojo-support %{namedversion} JPP/%{name} gmaven-mojo-support
%add_to_maven_depmap org.codehaus.gmaven gmaven-packaging %{namedversion} JPP/%{name} gmaven-packaging
%add_to_maven_depmap org.codehaus.gmaven gmaven-plugin %{namedversion} JPP/%{name} gmaven-plugin
%add_to_maven_depmap org.codehaus.gmaven gmaven-testsuite %{namedversion} JPP/%{name} gmaven-testsuite
%add_to_maven_depmap org.codehaus.gmaven.runtime gmaven-runtime %{namedversion} JPP/%{name} gmaven-runtime
%add_to_maven_depmap org.codehaus.gmaven.runtime gmaven-runtime-1.5 %{namedversion} JPP/%{name} gmaven-runtime-1.5
%add_to_maven_depmap org.codehaus.gmaven.runtime gmaven-runtime-1.6 %{namedversion} JPP/%{name} gmaven-runtime-1.6
%add_to_maven_depmap org.codehaus.gmaven.runtime gmaven-runtime-1.7 %{namedversion} JPP/%{name} gmaven-runtime-1.7
%add_to_maven_depmap org.codehaus.gmaven.runtime gmaven-runtime-api %{namedversion} JPP/%{name} gmaven-runtime-api
%add_to_maven_depmap org.codehaus.gmaven.runtime gmaven-runtime-loader %{namedversion} JPP/%{name} gmaven-runtime-loader
%add_to_maven_depmap org.codehaus.gmaven.runtime gmaven-runtime-support %{namedversion} JPP/%{name} gmaven-runtime-support
%add_to_maven_depmap org.codehaus.gmaven.support filter-plugin %{namedversion} JPP/%{name} filter-plugin
%add_to_maven_depmap org.codehaus.gmaven.support gmaven-support %{namedversion} JPP/%{name} gmaven-support
%add_to_maven_depmap org.codehaus.mojo groovy-maven-plugin %{namedversion} JPP/%{name} groovy-maven-plugin

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
ln -s %{name}-%{namedversion} %{buildroot}%{_javadocdir}/%{name}

%if %with repolib
mkdir -p %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
pushd maven2-brew
cp -pr * %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew/
popd
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%dir %{_javadir}*/%{name}/
%exclude %dir %{_javadocdir}/%{name}/
#%{_javadir}*/%{name}/clean-maven-plugin-%{namedversion}.jar
#%{_javadir}*/%{name}/clean-maven-plugin.jar
%{_javadir}*/%{name}/filter-plugin-%{namedversion}.jar
%{_javadir}*/%{name}/filter-plugin.jar
#%{_javadir}*/%{name}/gmaven-%{namedversion}-site.xml
%{_javadir}*/%{name}/gmaven-archetype-basic-%{namedversion}.jar
#%{_javadir}*/%{name}/gmaven-archetype-basic-%{namedversion}.maven-archetype
%{_javadir}*/%{name}/gmaven-archetype-basic.jar
#%{_javadir}*/%{name}/gmaven-archetype-basic.maven-archetype
%{_javadir}*/%{name}/gmaven-archetype-mojo-%{namedversion}.jar
#%{_javadir}*/%{name}/gmaven-archetype-mojo-%{namedversion}.maven-archetype
%{_javadir}*/%{name}/gmaven-archetype-mojo.jar
#%{_javadir}*/%{name}/gmaven-archetype-mojo.maven-archetype
%{_javadir}*/%{name}/gmaven-feature-api-%{namedversion}.jar
%{_javadir}*/%{name}/gmaven-feature-api.jar
%{_javadir}*/%{name}/gmaven-feature-support-%{namedversion}.jar
%{_javadir}*/%{name}/gmaven-feature-support.jar
%{_javadir}*/%{name}/gmaven-mojo-%{namedversion}.jar
%{_javadir}*/%{name}/gmaven-mojo-support-%{namedversion}.jar
%{_javadir}*/%{name}/gmaven-mojo-support.jar
%{_javadir}*/%{name}/gmaven-mojo.jar
%{_javadir}*/%{name}/gmaven-packaging-%{namedversion}.jar
%{_javadir}*/%{name}/gmaven-packaging.jar
%{_javadir}*/%{name}/gmaven-plugin-%{namedversion}.jar
%{_javadir}*/%{name}/gmaven-plugin.jar
%{_javadir}*/%{name}/gmaven-runtime-api-%{namedversion}.jar
%{_javadir}*/%{name}/gmaven-runtime-api.jar
%{_javadir}*/%{name}/gmaven-runtime-loader-%{namedversion}.jar
%{_javadir}*/%{name}/gmaven-runtime-loader.jar
%{_javadir}*/%{name}/gmaven-runtime-support-%{namedversion}.jar
%{_javadir}*/%{name}/gmaven-runtime-support.jar
#%{_javadir}*/%{name}/gmaven-site.xml
%{_javadir}*/%{name}/gmaven-testsuite-%{namedversion}.jar
%{_javadir}*/%{name}/gmaven-testsuite.jar
%{_javadir}*/%{name}/groovy-maven-plugin-%{namedversion}.jar
%{_javadir}*/%{name}/groovy-maven-plugin.jar
#%{_javadir}*/%{name}/install-maven-plugin-%{namedversion}.jar
#%{_javadir}*/%{name}/install-maven-plugin.jar
#%{_datadir}/maven2/poms/JPP.%{name}-clean-maven-plugin.pom
%{_datadir}/maven2/poms/JPP.%{name}-filter-plugin.pom
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-archetype-basic.pom
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-archetype-mojo.pom
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-archetypes.pom
#%{_datadir}/maven2/poms/JPP.%{name}-gmaven-examples.pom
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-feature-api.pom
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-feature-support.pom
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-feature.pom
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-mojo-support.pom
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-mojo.pom
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-packaging.pom
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-plugin.pom
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-runtime-api.pom
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-runtime-loader.pom
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-runtime-support.pom
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-runtime.pom
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-support.pom
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-testsuite.pom
%{_datadir}/maven2/poms/JPP.%{name}-gmaven.pom
%{_datadir}/maven2/poms/JPP.%{name}-groovy-maven-plugin.pom
#%{_datadir}/maven2/poms/JPP.%{name}-install-maven-plugin.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*-%{version}.jar.*
%endif

%files runtime-1.5
%{_javadir}*/%{name}/gmaven-runtime-1.5-%{namedversion}.jar
%{_javadir}*/%{name}/gmaven-runtime-1.5.jar
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-runtime-1.5.pom

%files runtime-1.6
%{_javadir}*/%{name}/gmaven-runtime-1.6-%{namedversion}.jar
%{_javadir}*/%{name}/gmaven-runtime-1.6.jar
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-runtime-1.6.pom

%files runtime-1.7
%{_javadir}*/%{name}/gmaven-runtime-1.7-%{namedversion}.jar
%{_javadir}*/%{name}/gmaven-runtime-1.7.jar
%{_datadir}/maven2/poms/JPP.%{name}-gmaven-runtime-1.7.pom

%files javadoc
%{_javadocdir}/%{name}-%{namedversion}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}*/
%exclude %dir %{_javadocdir}/
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_3jpp6
- dropped plexus-maven-plugin (unused)

* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_3jpp6
- fixed build

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_3jpp6
- full version

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

