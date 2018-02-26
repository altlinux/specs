Source33: plexus-container-default-1.0-alt-depmap.xml
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 1.0
%define name plexus-bsh-factory
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

%bcond_without          maven

%define gcj_support 0


%define parent plexus
%define subname bsh-factory

%define maven_settings_file %{_builddir}/%{name}/settings.xml

Name:           %{parent}-%{subname}
Version:        1.0
Release:        alt3_0.a7s.5jpp6
Epoch:          0
Summary:        Plexus Bsh Factory
License:        ASL 2.0
Group:          Development/Java
URL:            http://plexus.codehaus.org/
# svn export svn://svn.plexus.codehaus.org/plexus/tags/plexus-bsh-factory-1.0-alpha-7-SNAPSHOT plexus-bsh-factory
Source0:        %{name}-src.tar.gz
Source1:        %{name}-jpp-depmap.xml
Source2:        %{name}-build.xml
Patch0:         %{name}-encodingfix.patch
Requires: bsh
Requires: classworlds
Requires: plexus-container-default
Requires: plexus-utils
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
BuildRequires: jpackage-utils >= 0:1.7.5
%if %{with_maven}
BuildRequires: maven2 >= 2.0.8
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-common-poms >= 1.0-2
BuildRequires: maven-release
BuildRequires: maven-surefire-maven-plugin
BuildRequires: apache-commons-parent
%else
BuildRequires: ant
%endif
BuildRequires: bsh
BuildRequires: classworlds
BuildRequires: plexus-container-default
BuildRequires: plexus-utils
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}
%patch0 -p0

%if %without maven
cp -p %{SOURCE2} build.xml
%endif

%build
%if %with maven
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
	-Dmaven.local.depmap.file=%{S:33} \
	-Dmaven.repo.local=$MAVEN_REPO_LOCAL install javadoc:javadoc
%else
export CLASSPATH=
export OPT_JAR_LIST=:
mkdir -p lib
build-jar-repository -s -p lib bsh classworlds  plexus/container-default plexus/utils
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dmaven.mode.offline=true package javadoc
%endif

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/plexus
install -m 644 target/*.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/%{subname}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{parent} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
%add_to_maven_depmap org.codehaus.plexus %{name} 1.0-alpha-7 JPP/%{parent} %{subname}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-%{subname}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%dir %{_javadir}/plexus
%{_javadir}/plexus/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{with_maven}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/bsh-factory-1.0.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%endif

%changelog
* Fri Apr 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a7s.5jpp6
- fixed build with new plexus-containers

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a7s.5jpp6
- new jpp release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a7s.4jpp5
- new jpackage release

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a7s.2jpp1.7
- build with maven2

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a7s.2jpp1.7
- converted from JPackage by jppimport script

