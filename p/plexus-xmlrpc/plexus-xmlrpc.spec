BuildRequires: xmlrpc2
BuildRequires: /proc
BuildRequires: jpackage-compat
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

# If you don't want to build with maven, and use straight ant instead,
# give rpmbuild option '--without maven'
%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}

%define parent plexus
%define subname appserver

Name:           plexus-xmlrpc
Version:        1.0
Release:        alt7_0.2.b4.2.16jpp6
Epoch:          0
Summary:        Plexus XML RPC Component
License:        ASL 1.1 and MIT
Group:          Development/Java
URL:            http://plexus.codehaus.org/
# svn export svn://svn.plexus.codehaus.org/plexus/tags/plexus-xmlrpc-1.0-beta-4/
# tar czf plexus-xmlrpc-1.0-beta-4-src.tar.gz plexus-xmlrpc-1.0-beta-4/
Source0:        plexus-xmlrpc-1.0-beta-4-src.tar.gz
Source1:        %{name}-1.0-build.xml
Source2:        %{name}-jpp-depmap.xml

Patch0:         %{name}-add-codec-dep.patch


%if ! %{gcj_support}
BuildArch:      noarch
%else
ExcludeArch:    ppc64
%endif

BuildRequires: jpackage-utils >= 0:1.7.2
BuildRequires: ant >= 0:1.6
BuildRequires: ant-nodeps
%if %{with_maven}
BuildRequires: maven2 >= 2.0.4-9
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-doxia
BuildRequires: maven-doxia-sitetools
#BuildRequires: plexus-containers-component-metadata
BuildRequires: maven-release

%endif
BuildRequires: classworlds >= 0:1.1
BuildRequires: commons-codec
BuildRequires: plexus-container-default
BuildRequires: plexus-utils
BuildRequires: xmlrpc

Requires: commons-codec
Requires: classworlds >= 0:1.1
Requires: plexus-container-default
Requires: plexus-utils
Requires: xmlrpc

Requires(post): jpackage-utils >= 0:1.7.2
Requires(postun): jpackage-utils >= 0:1.7.2

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
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
%setup -q -n plexus-xmlrpc-1.0-beta-4
cp %{SOURCE1} build.xml

%patch0 -b .sav

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

%if %{with_maven}
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        install javadoc:javadoc
%else
mkdir -p target/lib
build-jar-repository -s -p target/lib \
classworlds \
commons-codec \
plexus/container-default \
plexus/utils \
xmlrpc \

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  jar javadoc
%endif

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/plexus
install -pm 644 target/plexus-xmlrpc-%{version}-beta-4.jar \
  $RPM_BUILD_ROOT%{_javadir}/plexus/xmlrpc-%{version}.jar
%add_to_maven_depmap org.codehaus.plexus plexus-xmlrpc 1.0-beta-4 JPP/plexus xmlrpc
(cd $RPM_BUILD_ROOT%{_javadir}/plexus && for jar in *-%{version}*; \
  do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

#poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.plexus-xmlrpc.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}
%{_datadir}/maven2
%doc LICENSE.txt
%config(noreplace)  %{_mavendepmapfragdir}/plexus-xmlrpc

%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/xmlrpc-1.0.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/*

%changelog
* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.2.b4.2.16jpp6
- dropped unused plexus-maven-plugin dependencies

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6_0.2.b4.2.16jpp6
- build w/o plexus-maven-plugin

* Wed Mar 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.2.b4.2.16jpp6
- fixed build with maven3

* Sun Feb 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.2.b4.2.16jpp6
- new version

* Thu Jan 06 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.2.b4.2.16jpp6
- jpp 6 releases

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.2.b4.2.16jpp6
- new jpp release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b4.6jpp5
- new jpackage release

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b4.5jpp1.7
- updated to new jpackage release

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b4.4jpp1.7
- converted from JPackage by jppimport script

