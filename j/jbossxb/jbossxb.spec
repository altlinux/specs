Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 1.0.0
%define name jbossxb
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

%define reltag SP3
%define repodir %{_javadir}/repository.jboss.com/jboss/jbossxb/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define gcj_support 0


%define maven_settings_file %{_builddir}/%{name}/settings.xml

Name:           jbossxb
Version:        1.0.0
Release:	alt3_3.SP3.9jpp5
Epoch:          1
Summary:        JBoss XB
License:        LGPLv2+
Group:          Development/Java
URL:            http://anonsvn.jboss.org/repos/common/jbossxb
Source0:        %{name}-%{version}.SP3-src.tar.gz
# svn export http://anonsvn.jboss.org/repos/common/jbossxb/tags/1.0.0.SP3/ jbossxb
# tar czf jbossxb-1.0.0.SP3-src.tar.gz jbossxb
Source1:        %{name}-jpp-depmap.xml
Source2:	jbossxb-component-info.xml
Source3:        jbossxb-1.0.0.pom
Patch0:         %{name}-pom-xml.patch


%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRequires: jpackage-utils >= 0:1.7.2
BuildRequires: concurrent
BuildRequires: dtdparser
BuildRequires: maven2 >= 0:2.0.4-10
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-release
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin
BuildRequires: maven2-plugin-surefire-report
BuildRequires: maven2-common-poms >= 0:1.0
BuildRequires: jakarta-slide-webdavclient
BuildRequires: jboss-common
#BuildRequires:  jboss-test >= 0:1.0.0
BuildRequires: junit
BuildRequires: log4j
BuildRequires: plexus-utils
BuildRequires: xerces-j2
BuildRequires: jaf_1_1_api
Requires: concurrent
Requires: dtdparser
Requires: xerces-j2
Requires(post): jpackage-utils >= 0:1.7.2
Requires(postun): jpackage-utils >= 0:1.7.2
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%endif

%description
The JBoss Xml Bindings

%if %{with_repolib}
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n %{name}
%patch0 -p0

mkdir external_repo
ln -s %{_javadir} external_repo/JPP 

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        -Dmaven.test.skip=true \
        install

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/jboss
install -pm 644 target/jboss-xml-binding.jar $RPM_BUILD_ROOT%{_javadir}/jboss/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jboss/jboss-xml-binding-%{version}.jar
install -pm 644 target/jboss-xml-binding-sources.jar $RPM_BUILD_ROOT%{_javadir}/jboss/%{name}-sources-%{version}.jar
ln -s %{name}-sources-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jboss/jboss-xml-binding-sources-%{version}.jar
(cd %{buildroot}%{_javadir}/jboss && for jar in *-%{version}.jar; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# pom
%add_to_maven_depmap jboss.xb %{name} %{version}.%{reltag} JPP/jboss %{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%if 0
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jboss.%{name}.pom
%else
install -pm 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.jboss.%{name}.pom
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %{with_repolib}
	install -d -m 755 $RPM_BUILD_ROOT%{repodir}
	install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
	install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{repodir}/component-info.xml
        sed -i "s/@VERSION@/%{version}.%{reltag}-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
        tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
        sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
	install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
	install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
	cp -p $RPM_BUILD_ROOT%{_javadir}/jboss/jboss-xml-binding.jar $RPM_BUILD_ROOT%{repodirlib}
	cp -p $RPM_BUILD_ROOT%{_javadir}/jboss/jboss-xml-binding-sources.jar $RPM_BUILD_ROOT%{repodirlib}
%endif

%files
%{_javadir}/jboss
%{_datadir}/maven2/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/jboss-xml-binding-1.0.0.jar.*
%endif

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.0.0-alt3_3.SP3.9jpp5
- updated repolib

* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.0.0-alt2_3.SP3.9jpp5
- rebuild with new xerces repolib

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.0.0-alt1_3.SP3.9jpp5
- new jpp release

