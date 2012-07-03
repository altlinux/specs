BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 1.3.5
%define name plexus-maven-plugin
# Copyright (c) 2000-2005, JPackage Project
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

%define gcj_support 0

%define parent plexus
%define subname maven-plugin

%define maven_settings_file %{_builddir}/%{name}/settings.xml

Name:           %{parent}-%{subname}
Version:        1.3.5
Release:        alt3_7jpp6
Epoch:          1
Summary:        Plexus Maven plugin
License:        Apache Software License
Group:          Development/Java
URL:            http://plexus.codehaus.org/
# svn export http://svn.codehaus.org/plexus/plexus-maven-plugin/tags/plexus-maven-plugin-1.3.5
# tar czf plexus-maven-plugin-src.tar.gz plexus-maven-plugin-1.3.5
Source0:        %{name}-src.tar.gz
Source1:        %{name}-jpp-depmap.xml

Patch0:         %{name}-maven-doxia.patch
Patch1:         %{name}-add-jdom-dep.patch


%if ! %{gcj_support}
BuildArch: noarch
%endif

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: maven2 >= 2.0.8
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-doxia
BuildRequires: maven-doxia-sitetools
BuildRequires: maven2-common-poms >= 1.0
BuildRequires: maven2-plugin-release
BuildRequires: plexus-appserver >= 1.0-0.a5.3
BuildRequires: plexus-cdc >= 1.0-0.3.a10
BuildRequires: plexus-containers
BuildRequires: plexus-containers-container-default
BuildRequires: plexus-runtime-builder >= 1.0-0.a9.2
BuildRequires: apache-commons-parent
BuildRequires: qdox

Requires: maven2 >= 2.0.8
Requires: maven2-common-poms >= 1.0
Requires: plexus-appserver >= 1.0-0.a5.3
Requires: plexus-cdc >= 1.0
Requires: plexus-containers-container-default
Requires: plexus-runtime-builder >= 1.0-0.a9.2

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Source44: import.info

%description
Plexus Maven Plugin helps create plexus component descriptions
from within Maven.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch0 -b .sav
%patch1 -b .sav

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/plexus
install -pm 644 target/*.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{parent}/%{subname}-%{version}.jar
%add_to_maven_depmap org.codehaus.plexus %{name} 1.2 JPP/%{parent} %{subname}
(cd $RPM_BUILD_ROOT%{_javadir}/%{parent} && for jar in *-%{version}*; \
  do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-%{subname}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

cp -pr target/site/apidocs/* \
        $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/

ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/plexus
%{_datadir}/maven2
%{_mavendepmapfragdir}

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/maven-plugin-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/*

%changelog
* Sat Feb 25 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.3.5-alt3_7jpp6
- fixed build

* Mon Jan 31 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.3.5-alt2_7jpp6
- set target 5

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.3.5-alt1_7jpp6
- fixed build

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.6-alt1_1jpp5
- new version

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.5-alt2_2jpp5
- converted from JPackage by jppimport script

* Wed Oct 01 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.5-alt1_2jpp5
- converted from JPackage by jppimport script

* Thu Nov 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_2jpp1.7
- converted from JPackage by jppimport script

