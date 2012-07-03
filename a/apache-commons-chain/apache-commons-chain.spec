%define _without_maven 1
BuildRequires: mojo-maven2-plugin-jdepend mojo-maven2-plugin-rat
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

%bcond_without maven
#def_with gcj_support
%bcond_with gcj_support
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/apache-%{base_name}/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirres %{repodir}/resources
%define repodirsrc %{repodir}/src

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define base_name chain
%define short_name commons-%{base_name}

Name:           apache-commons-chain
Version:        1.3
Release:        alt2_0.r831527.5jpp6
Epoch:          0
Summary:        Apache Commons Chain
License:        ASL 2.0
Group:          Development/Java
URL:            http://commons.apache.org/chain/
Source0:        commons-chain-1.3-src.tar.gz
# svn export -r 831527 http://svn.apache.org/repos/asf/commons/proper/chain/trunk/ commons-chain-1.3-src
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-component-info.xml
Source4:        http://repo2.maven.org/maven2/org/apache/myfaces/myfaces/5/myfaces-5.pom
Patch0:         apache-commons-chain-pom.patch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7
BuildRequires: junit
BuildRequires: fonts-ttf-liberation
%if %with maven
BuildRequires: apache-commons-parent >= 0:12
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-checkstyle
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-idea
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-default-skin
BuildRequires: mojo-maven2-plugin-clirr
BuildRequires: clirr
%endif
BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-digester
BuildRequires: jakarta-commons-logging
BuildRequires: jstl
BuildRequires: myfaces-core11-api
BuildRequires: portlet_1_0_api
BuildRequires: servlet_2_4_api
BuildRequires: struts
Requires: apache-commons-beanutils
Requires: apache-commons-collections
Requires: apache-commons-digester
Requires: jakarta-commons-logging
Requires: jsf_1_1_api
Requires: jstl
Requires: portlet_1_0_api
Requires: servlet
Requires: struts
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Provides:       jakarta-%{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{epoch}:%{version}-%{release}
Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name} < %{epoch}:%{version}-%{release}
Source44: import.info

%description
A popular technique for organizing the execution of complex 
processing flows is the "Chain of Responsibility" pattern, as 
described (among many other places) in the classic "Gang of Four" 
design patterns book. Although the fundamental API contracts 
required to implement this design patten are extremely simple, 
it is useful to have a base API that facilitates using the pattern, 
and (more importantly) encouraging composition of command 
implementations from multiple diverse sources.
Towards that end, the Chain API models a computation as a series 
of "commands" that can be combined into a "chain". The API for a 
command consists of a single method (execute()), which is passed 
a "context" parameter containing the dynamic state of the 
computation, and whose return value is a boolean that determines 
whether or not processing for the current chain has been completed 
(true), or whether processing should be delegated to the next 
command in the chain (false).

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java
Provides:       jakarta-%{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-repolib < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-repolib < %{epoch}:%{version}-%{release}

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       jakarta-%{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-javadoc < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%if %with maven
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
Provides:       jakarta-%{short_name}-manual = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-manual < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-manual = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-manual < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description manual
%{summary}.
%endif

%prep
%setup -q -n %{short_name}-%{version}-src
%{__perl} -pi \
    -e 's/\r$//g;' \
  PROPOSAL.html LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%patch0 -b .sav0
%if %with maven
cp -p %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP
%endif

%build
%if %with maven
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}
mkdir -p ${MAVEN_REPO_LOCAL}/org/apache/myfaces/myfaces/5/
cp %{SOURCE4} ${MAVEN_REPO_LOCAL}/org/apache/myfaces/myfaces/5/myfaces-5.pom
export MAVEN_OPTS="-Dmaven2.jpp.mode=true -Dmaven2.jpp.depmap.file=%{SOURCE2} -Dmaven.repo.local=${MAVEN_REPO_LOCAL}"
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e -X \
       install javadoc:javadoc site

%else
export CLASSPATH=
export OPT_JAR_LIST=:
mkdir -p target/lib
pushd target/lib
ln -sf $(build-classpath commons-beanutils)
ln -sf $(build-classpath commons-collections)
ln -sf $(build-classpath commons-digester)
ln -sf $(build-classpath commons-logging)
ln -sf $(build-classpath junit)
ln -sf $(build-classpath jsf_1_1_api)
ln -sf $(build-classpath portlet_1_0_api)
ln -sf $(build-classpath servlet_2_4_api)
ln -sf $(build-classpath struts)
popd
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dnoget compile jar javadoc
%endif

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{short_name}-%{version}-SNAPSHOT.jar \
           $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

%add_to_maven_depmap %{short_name} %{short_name} %{version} JPP %{name}

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in apache-*; do ln -sf ${jar} $(echo $jar | sed -e 's/apache-/jakarta-/'); done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in apache-*; do ln -sf ${jar} $(echo $jar | sed -e 's/apache-//'); done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} $(echo $jar | sed -e 's/-%{version}//'); done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %with maven
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
rm -rf target/site/apidocs
%else
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

## manual
%if %with maven
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_docdir}/jakarta-%{short_name}-%{version}
%endif

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__install} -m 0644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__install} -m 0644 %{PATCH0} %{buildroot}%{repodirsrc}/
%{__install} -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}/
%{__install} -m 0644 %{SOURCE1} %{buildroot}%{repodirsrc}/
%{__install} -m 0644 %{SOURCE2} %{buildroot}%{repodirsrc}/
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/%{short_name}.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-*%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/*

%if %with maven
%files manual
%doc %{_docdir}/*
%endif

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_0.r831527.5jpp6
- fixed build with maven3

* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_0.r831527.5jpp6
- new version

