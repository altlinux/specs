Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 1.2.0
%define name jboss-jaxr
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

%define _with_repolib 1
# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/jboss/jaxr/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define gcj_support 0


%define reltag SP1

%define maven_settings_file %{_builddir}/%{name}/settings.xml

Name:           jboss-jaxr
Version:        1.2.0
Release:        alt1_1.SP1.4jpp5
Epoch:          0
Summary:        JBoss JAXR
License:        LGPLv2+
Group:          Development/Java
URL:            http://wiki.jboss.org/wiki/en/Jbossesb/JAXR
# svn export http://anonsvn.jboss.org/repos/jbossas/projects/jaxr/tags/jaxr-1.2.0.SP1
# mv jaxr-1.2.0.SP1 jboss-jaxr
# tar czvf jboss-jaxr-1.2.0.SP1-src.tar.gz jboss-jaxr/
Source0:        %{name}-%{version}.%{reltag}-src.tar.gz
Source1:        %{name}-jpp-depmap.xml
Source2:        %{name}-component-info.xml
#Patch0:        %{name}-pom-xml.patch
Requires(post): jpackage-utils >= 0:1.7.2
Requires(postun): jpackage-utils >= 0:1.7.2
Requires: jboss-common
%if 0
# FIXME: (dwalluck): juddi and ws-scout0 are bundled, not symlinked
Requires: juddi
Requires: ws-scout0
%endif
BuildRequires: jpackage-utils >= 0:1.7.2
BuildRequires: maven2 >= 0:2.0.4-10
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven-release
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-report-plugin
BuildRequires: maven2-common-poms >= 0:1.0
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-antrun
BuildRequires: jboss-common >= 0:1.0.4
BuildRequires: jbossas >= 0:4.2.3
BuildRequires: juddi >= 0:0.9
BuildRequires: juddi-repolib >= 0:0.9
BuildRequires: servlet24
BuildRequires: ws-scout0 >= 0:0.7
BuildRequires: ws-scout0-repolib >= 0:0.7
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif

%description
The JBoss Xml Registries.

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
%setup -q -n %{name}
#%%patch0 -p0

mkdir external_repo
ln -s %{_javadir} external_repo/JPP 

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mvn-jpp \
        -e \
        -Djboss.repository=file://%{_javadir}/repository.jboss.com \
        -Dapache-scout=0.7rc2-brew \
        -Djuddi=0.9RC4-brew \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/jboss-jaxr
install -pm 644 target/%{name}.jar \
          $RPM_BUILD_ROOT%{_javadir}/jboss-jaxr/%{name}-%{version}.jar
install -pm 644 target/juddi-saaj.jar \
          $RPM_BUILD_ROOT%{_javadir}/jboss-jaxr/juddi-saaj-%{version}.jar
install -pm 644 target/juddi-service.sar \
          $RPM_BUILD_ROOT%{_javadir}/jboss-jaxr/juddi-service-%{version}.sar
%add_to_maven_depmap jboss.jaxr %{name} %{version}-%{reltag} JPP/jboss-jaxr %{name}

(cd $RPM_BUILD_ROOT%{_javadir}/jboss-jaxr && ln -sf %{name}-%{version}.jar %{name}.jar)
(cd $RPM_BUILD_ROOT%{_javadir}/jboss-jaxr && ln -sf juddi-saaj-%{version}.jar juddi-saaj.jar)
(cd $RPM_BUILD_ROOT%{_javadir}/jboss-jaxr && ln -sf juddi-service-%{version}.sar juddi-service.sar)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}.pom

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %{with_repolib}
        install -d -m 755 $RPM_BUILD_ROOT%{repodir}
        install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
        install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{repodir}/component-info.xml
        install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
        install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
        cp -p $RPM_BUILD_ROOT%{_javadir}/jboss-jaxr/juddi-saaj.jar $RPM_BUILD_ROOT%{repodirlib}
        cp -p $RPM_BUILD_ROOT%{_javadir}/jboss-jaxr/juddi-service.sar $RPM_BUILD_ROOT%{repodirlib}
        # replace @VERSION@ @TAG@ in component-info.xml
        sed -i 's/@VERSION@/%{version}.%{reltag}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
        tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
        sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
%endif

%files
%dir %{_javadir}/jboss-jaxr
%{_javadir}/jboss-jaxr/%{name}-%{version}.jar
%{_javadir}/jboss-jaxr/%{name}.jar
%{_javadir}/jboss-jaxr/juddi-saaj-%{version}.jar
%{_javadir}/jboss-jaxr/juddi-saaj.jar
%{_javadir}/jboss-jaxr/juddi-service-%{version}.sar
%{_javadir}/jboss-jaxr/juddi-service.sar
%{_datadir}/maven2/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_1.SP1.4jpp5
- full version

* Sun Aug 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt0.1jpp
bootstrap; see deps.notes for details

