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
#

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without          maven

%define gcj_support 0


%define parent plexus
%define subname interactivity

Name:           plexus-interactivity
Version:        1.0
Release:        alt3_0.a6.1jpp6
Epoch:          0
Summary:        Plexus Interactivity Handler Component
License:        ASL 2.0
Group:          Development/Java
URL:            http://plexus.codehaus.org/
# svn export http://svn.codehaus.org/plexus/plexus-components/tags/plexus-interactivity-1.0-alpha-6/
Source0:        plexus-interactivity-1.0-alpha-6-src.tar.gz
Source1:        plexus-interactivity-1.0-api-build.xml
Source2:        plexus-interactivity-1.0-api-project.xml
Source3:        plexus-interactivity-1.0-jline-build.xml
Source4:        plexus-interactivity-1.0-jline-project.xml
Source5:        plexus-interactivity-settings.xml
Source6:        plexus-interactivity-1.0-jpp-depmap.xml
Requires: plexus-container-default
Requires: plexus-utils
Requires: jline
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
%if %with maven
BuildRequires: maven2 >= 2.0.8
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven-release
BuildRequires: maven-surefire-maven-plugin
BuildRequires: apache-commons-parent
%endif
BuildRequires: jline
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
%setup -q -n plexus-interactivity-1.0-alpha-6
cp %{SOURCE1} plexus-interactivity-api/build.xml
cp %{SOURCE2} plexus-interactivity-api/project.xml
cp %{SOURCE3} plexus-interactivity-jline/build.xml
cp %{SOURCE4} plexus-interactivity-jline/project.xml
cp %{SOURCE5} settings.xml

%build
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mkdir external_repo
ln -sf %{_javadir} external_repo/JPP

%if %with maven
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s $(pwd)/settings.xml \
        -Dmaven2.jpp.depmap.file=%{SOURCE6} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc
%else
export CLASSPATH=
export OPT_JAR_LIST=:
pushd plexus-interactivity-api
mkdir -p target/lib
build-jar-repository -s -p target/lib plexus/container-default plexus/utils
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadoc
popd

pushd plexus-interactivity-jline
mkdir -p target/lib
cp ../plexus-interactivity-api/target/plexus-interactivity-api-1.0-alpha-5.jar target/lib
build-jar-repository -s -p target/lib jline plexus/container-default
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadoc
popd
%endif

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/plexus
install -m 644 plexus-interactivity-api/target/%{name}-api-%{version}-alpha-6.jar $RPM_BUILD_ROOT%{_javadir}/plexus/interactivity-api-%{version}.jar
install -m 644 plexus-interactivity-jline/target/%{name}-jline-%{version}-alpha-6.jar $RPM_BUILD_ROOT%{_javadir}/plexus/interactivity-jline-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/plexus && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
%add_to_maven_depmap org.codehaus.plexus %{name}-api %{version} JPP/%{parent} %{subname}-api
%add_to_maven_depmap org.codehaus.plexus %{name}-jline %{version} JPP/%{parent} %{subname}-jline

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/default_poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-%{subname}.pom
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/default_poms/org.codehaus.plexus-%{parent}-%{subname}.pom

install -m 644 plexus-interactivity-api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-%{subname}-api.pom
install -m 644 plexus-interactivity-jline/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-%{subname}-jline.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/api
cp -pr plexus-interactivity-api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/api
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jline
cp -pr plexus-interactivity-jline/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jline
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/%{parent}/*
%{_datadir}/maven2/poms/*
%{_datadir}/maven2/default_poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{subname}*-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a6.1jpp6
- new version

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a5.6jpp5
- fixed build

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a5.6jpp5
- new jpackage release

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a5.5jpp1.7
- build with maven2

* Wed Jun 13 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a5.5jpp1.7
- updated to new jpackage release

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a5.4jpp1.7
- converted from JPackage by jppimport script

* Sun Dec 04 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt0.1.alpha5
- Rebuild for ALTLinux Sisyphus
- spec cleanup

* Mon Nov 07 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.a5.1jpp
- First JPackage build

