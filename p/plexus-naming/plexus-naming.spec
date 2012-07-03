Patch33: plexus-naming-migration-to-component-metadata.patch
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2007, JPackage Project
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

%define namedversion 1.0-alpha-3

%define parent plexus
%define subname naming

Name:           plexus-naming
Version:        1.0
Release:        alt6_0.a3.4jpp6
Epoch:          0
Summary:        Plexus Naming Component
License:        Apache Software License 2.0
Group:          Development/Java
URL:            http://plexus.codehaus.org/

#http://mirrors.dotsrc.org/jpackage/5.0/generic/SRPMS.free/plexus-naming-1.0-0.a3.1jpp.src.rpm
Source0:        %{name}-%{namedversion}.tar.gz
Source1:        plexus-naming-1.0-build.xml
Source3:        plexus-naming-1.0-jpp-depmap.xml
Source4:        plexus-naming-components.xml

Patch0:         plexus-naming-1.0-pom.patch


%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: junit
BuildRequires: hsqldb
BuildRequires: jakarta-commons-logging
%if %{with_maven}
BuildRequires: maven2 >= 2.0.4-10jpp
BuildRequires: maven2-common-poms
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-release
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-doxia
BuildRequires: maven-doxia-sitetools
BuildRequires: plexus-containers-component-metadata
BuildRequires: qdox >= 1.5
BuildRequires: tomcat5
BuildRequires: tomcat5-servlet-2.4-api
BuildRequires: excalibur-avalon-logkit
BuildRequires: excalibur-avalon-framework

%endif
BuildRequires: directory-naming
BuildRequires: avalon-framework
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-dbcp
BuildRequires: jakarta-commons-digester
BuildRequires: jakarta-commons-pool
BuildRequires: plexus-cdc
BuildRequires: plexus-classworlds
BuildRequires: plexus-containers-container-default
BuildRequires: plexus-utils

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

Requires: directory-naming
Requires: jakarta-commons-pool
Requires: plexus-classworlds
Requires: plexus-container-default
Requires: plexus-utils
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
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
%setup -q -n %{name}-%{namedversion}
cp %{SOURCE1} build.xml
mkdir -p target/classes/META-INF/plexus/
cp %{SOURCE4} target/classes/META-INF/plexus/components.xml
%patch0 -b .sav0

%patch33

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

%if %{with_maven}
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -Dmaven.test.failure.ignore=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE3} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc

%else
export CLASSPATH=$(build-classpath \
commons-collections \
commons-logging \
commons-dbcp \
commons-pool \
directory-naming/naming-config \
directory-naming/naming-core \
directory-naming/naming-factory \
directory-naming/naming-java \
hsqldb \
plexus/classworlds \
plexus/containers-container-default \
plexus/utils \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.sysclasspath=only jar javadoc
%endif

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/plexus
install -pm 644 target/%{name}-%{namedversion}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{parent}/%{subname}-%{version}.jar
%add_to_maven_depmap org.codehaus.plexus %{name} %{version} JPP/%{parent} %{subname}

(cd $RPM_BUILD_ROOT%{_javadir}/plexus && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-%{subname}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/%{parent}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{subname}*-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6_0.a3.4jpp6
- dropped unused plexus-maven-plugin dependencies

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.a3.4jpp6
- build w/o plexus-maven-plugin

* Sun Feb 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.a3.4jpp6
- new version

* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a3.4jpp6
- rebuild w/o BR: maven2-plugins

* Sat Dec 25 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a3.4jpp6
- jpp 6.0 build

* Sat Feb 21 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a3.1jpp5
- fixed build with maven 2.0.7

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a3.1jpp5
- converted from JPackage by jppimport script

