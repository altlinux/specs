Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 1.0.2
%define name jbossws-spi
# Copyright (c) 2000-2008, JPackage Project
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

# XXX: (dwalluck): 1.0.4.GA switched to mvn (commented out)

%define _with_repolib 1
 
# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir_root repository.jboss.com
%define repodir_release jboss/%{name}/%{version_full}
%define repodir %{_javadir}/%{repodir_root}/%{repodir_release}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define version_maj 1
%define version_min 0
%define version_rev 2
%define version_tag GA
%define version_full %{version_maj}.%{version_min}.%{version_rev}.%{version_tag}

Name:           jbossws-spi
Version:        %{version_maj}.%{version_min}.%{version_rev}
Release:        alt1_2jpp5
Epoch:          0
Summary:        JBoss Web Services (SPI)
License:        LGPLv2+
Group:          Development/Java
URL:            http://labs.jboss.com/jbossws/
# svn export http://anonsvn.jboss.org/repos/jbossws/spi/tags/jbossws-spi-1.0.4.GA/ jbossws-spi-1.0.4.GA
# tar cjf jbossws-spi-1.0.4.GA.tar.bz2 jbossws-spi-1.0.4.GA
Source0:        %{name}-%{version_full}.tar.bz2
Source1:        %{name}.pom
Source2:        %{name}-component-info.xml
Source3:        %{name}-jpp-depmap.xml
Patch0:         jbossws-spi-1.0.2.GA-build-thirdparty.patch
Patch1:         jbossws-spi-no-classpath-in-manifest.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildRequires: ant
BuildRequires: dom4j >= 0:1.6.1
BuildRequires: gnu-getopt
BuildRequires: jboss-common
BuildRequires: jboss-microcontainer
BuildRequires: jbossws-parent
BuildRequires: jbossxb >= 0:1.0.0
BuildRequires: junit >= 0:3.8.1
BuildRequires: maven2
BuildRequires: maven2-plugin-antrun
# FIXME: (dwalluck): we need packages containing maven2 poms
#BuildRequires: ejb_3_0_api
BuildRequires: geronimo-ejb-3.0-api
#BuildRequires: servlet25
BuildRequires: geronimo-j2ee-1.4-apis
#BuildRequires: jaxb_2_1_api
BuildRequires: glassfish-jaxb >= 0:2.1
#BuildRequires: jaxws_2_1_api
BuildRequires: glassfish-jaxws >= 0:2.1
BuildArch:      noarch

%description
JBossWS SPI.

%if 0
%package javadoc
Summary:         Javadoc for %{name}
Group:           Development/Documentation

%description javadoc
Javadoc for %{name}.
%endif

%if %{with_repolib}
%package repolib
Summary:         Artifacts to be uploaded to a repository library
Group:           Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n %{name}-%{version_full}
%patch0 -p1
%patch1 -p1
%{__cp} -a ant.properties.example ant.properties
%{__mkdir_p} repository

%{__mkdir_p} thirdparty
pushd thirdparty
%{__ln_s} $(build-classpath dom4j) dom4j.jar
%{__ln_s} $(build-classpath gnu-getopt) getopt.jar
%{__ln_s} $(build-classpath sun-jaxb/jaxb-api) jaxb-api.jar
%{__ln_s} $(build-classpath sun-jaxws/jaxws-api) jaxws-api.jar
%{__ln_s} $(build-classpath jboss-common/jboss-common) jboss-common-core.jar
%{__ln_s} $(build-classpath jboss-microcontainer/jboss-microcontainer) jboss-microcontainer.jar
%{__ln_s} $(build-classpath jboss/jbossxb) jboss-xml-binding.jar
%{__ln_s} $(build-classpath junit) junit.jar
%{__ln_s} $(build-classpath geronimo-j2ee-1.4-apis) servlet-api.jar
popd

%build
%if 0
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
%{__mkdir_p} $MAVEN_REPO_LOCAL

%{_bindir}/mvn-jpp \
    -Djboss.local.repository=$(pwd)/repository \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.test.failure.ignore=false \
    -Dmaven2.jpp.depmap.file=%{SOURCE3} \
    install javadoc:javadoc
%else
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant}
%endif

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%if 0
%{__cp} -a target/%{name}-%{version_full}.jar %{buildroot}%{_javadir}/%{name}-%{version_full}.jar
%{__cp} -a target/%{name}-%{version_full}-sources.jar %{buildroot}%{_javadir}/%{name}-sources-%{version_full}.jar
%else
%{__cp} -a output/lib/jbossws-spi.jar %{buildroot}%{_javadir}/%{name}-%{version_full}.jar
%{__cp} -a output/lib/jbossws-spi-src.zip %{buildroot}%{_javadir}/%{name}-sources-%{version_full}.jar
%endif
(cd %{buildroot}%{_javadir} && for jar in *-%{version_full}.jar; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version_full}||g"`; done)

# javadoc
%if 0
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -a target/site/apidocs/*  %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%endif

# poms
%add_to_maven_depmap org.jboss.ws jbossws-spi %{version_full} JPP %{name}
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -a %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

%if %{with_repolib}
    %{__mkdir_p} %{buildroot}%{repodir}
    %{__mkdir_p} %{buildroot}%{repodirlib}
    %{__mkdir_p} %{buildroot}%{repodirsrc}
    %{__cp} -a %{SOURCE0} %{buildroot}%{repodirsrc}
%if 0
    %{__cp} -a repository/jboss/*/*/* %{buildroot}%{repodir}
%else
    %{__cp} -a %{buildroot}%{_javadir}/%{name}-%{version_full}.jar %{buildroot}%{repodirlib}/jbossws-spi.jar
    %{__cp} -a %{buildroot}%{_javadir}/%{name}-sources-%{version_full}.jar %{buildroot}%{repodirlib}/jbossws-spi-sources.jar
    %{__cp} -a %{SOURCE0} %{buildroot}%{repodirsrc}
    %{__cp} -a %{PATCH0} %{buildroot}%{repodirsrc}
    %{__cp} -a %{PATCH1} %{buildroot}%{repodirsrc}
%endif
    %{__cp} -a %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
    %{__sed} -i 's/@VERSION@/%{version_full}-brew/g' %{buildroot}%{repodir}/component-info.xml
    tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
    %{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%endif

%files
%{_javadir}/%{name}-%{version_full}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-sources-%{version_full}.jar
%{_javadir}/%{name}-sources.jar
%{_datadir}/maven2/*
%{_mavendepmapfragdir}/*

%if 0
%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%endif

%if %{with_repolib}
%files repolib
%{_javadir}/%{repodir_root}
%endif

%changelog
* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_2jpp5
- new jpp release

