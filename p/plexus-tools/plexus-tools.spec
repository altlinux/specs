BuildRequires: /proc
BuildRequires: jpackage-compat
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

%global parent plexus
%global subname tools
%global cdc_version 1.0.10
%global cli_version 1.4


Name:           plexus-tools
Version:        1.0.10
Release:        alt8.a13_5jpp6
Epoch:          0
Summary:        Plexus Tools
License:        ASL 2.0
Group:          Development/Java
URL:            http://plexus.codehaus.org/
Source0:        %{name}-%{version}.tar.gz
## http://svn.codehaus.org/plexus/archive/plexus-tools/tags/plexus-tools-1.0.11/
# svn export http://svn.codehaus.org/plexus/plexus-tools/tags/plexus-tools-1.0.10/

Source1:        %{name}-jpp-depmap.xml
Patch0:         plexus-tools-cdc-DefaultComponentDescriptorWriterTest.patch
#Patch1:         plexus-tools-cli-pom.patch
#Patch2:         plexus-tools-pom.patch
Patch3:         plexus-tools-cdc-anno-pom.patch
#Patch4:         plexus-tools-javadoc-pom.patch
Patch5:         plexus-tools-build.patch
%if 0
Provides:       plexus-cdc
Obsoletes:      plexus-cdc
Provides:       plexus-cli
Obsoletes:      plexus-cli
%endif
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       apache-commons-cli
Requires:       jdom
Requires:       plexus-classworlds
Requires:       plexus-component-annotations
Requires:       plexus-containers-container-default
Requires:       plexus-utils
Requires:       qdox
Requires:       slf4j
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  maven2 >= 0:2.0.8
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-release
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven2-common-poms >= 0:1.0
BuildRequires:  jdom
BuildRequires:  apache-commons-parent
BuildRequires:  apache-commons-cli
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-component-annotations
BuildRequires:  plexus-containers-container-default
BuildRequires:  plexus-utils
BuildRequires:  qdox
BuildRequires:  slf4j
BuildArch:      noarch
Source44: import.info

#Provides: plexus-cdc = %version
#Obsoletes: plexus-cdc < %version
#Obsoletes: plexus-cli
Requires: plexus-cdc

%package        -n plexus-cdc
Version:        1.0
Epoch:          0
Summary:        Plexus Component Descriptor Creator
License:        Apache Software License
Group:          Development/Java
URL:            http://plexus.codehaus.org/

%description -n plexus-cdc
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%package        -n plexus-cli14
Summary:        Command Line Interface facilitator for Plexus
Group:          Development/Java

%description -n plexus-cli14
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.


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
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
%patch0 -p0 -b .sav0
#patch1 -p0 -b .sav1
#patch2 -p0 -b .sav2
%patch3 -p0 -b .sav3
#patch4 -p0 -b .sav4
pushd plexus-cdc
%patch5 -p0 -b .sav5
rm -rf src/test/java
ln -s src/test/resources src/test/java
popd

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:aggregate


%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/plexus
cp -p plexus-cdc-anno/target/*.jar \
          $RPM_BUILD_ROOT%{_javadir}/%{parent}/tools-cdc-anno-%{version}.jar
%add_to_maven_depmap_at plexus-cdc org.codehaus.plexus plexus-cdc-anno 1.0-alpha-3 JPP/%{parent} tools-cdc-anno
cp -p plexus-cdc/target/*.jar \
          $RPM_BUILD_ROOT%{_javadir}/%{parent}/tools-cdc-%{version}.jar
%add_to_maven_depmap_at plexus-cdc org.codehaus.plexus plexus-cdc 1.0-alpha-13 JPP/%{parent} tools-cdc
cp -p plexus-cli/target/*.jar \
          $RPM_BUILD_ROOT%{_javadir}/%{parent}/tools-cli-1.4.jar
%add_to_maven_depmap_at plexus-cli14 org.codehaus.plexus plexus-cli 1.4 JPP/%{parent} tools-cli

(cd $RPM_BUILD_ROOT%{_javadir}/%{parent} && for jar in *-%{cdc_version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{cdc_version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{parent} && for jar in *-%{cli_version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{cli_version}||g"`; done)
ln -s tools-cdc.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/cdc.jar
ln -s tools-cli.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/cli.jar

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
cp -p plexus-cdc-anno/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-tools-cdc-anno.pom
cp -p plexus-cdc/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-tools-cdc.pom
cp -p plexus-cli/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-tools-cli.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

ln -s tools-cdc-1.0.jar %buildroot/usr/share/java/plexus/tools-cdc.jar


%files
%{_javadir}/plexus/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%exclude %{_mavendepmapfragdir}/plexus-cdc
%exclude /usr/share/java/plexus/cdc.jar
%exclude /usr/share/java/plexus/tools-cdc*
%exclude /usr/share/maven2/poms/JPP.plexus-tools-cdc*

%exclude %{_mavendepmapfragdir}/plexus-cli14
%exclude /usr/share/java/plexus/cli.jar
%exclude /usr/share/java/plexus/tools-cli*
%exclude /usr/share/maven2/poms/JPP.plexus-tools-cli*

%files -n plexus-cdc
%{_mavendepmapfragdir}/plexus-cdc
/usr/share/java/plexus/cdc.jar
/usr/share/java/plexus/tools-cdc*jar
/usr/share/maven2/poms/JPP.plexus-tools-cdc*

%files -n plexus-cli14
%{_mavendepmapfragdir}/plexus-cli14
/usr/share/java/plexus/cli.jar
/usr/share/java/plexus/tools-cli*jar
/usr/share/maven2/poms/JPP.plexus-tools-cli*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Apr 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.10-alt8.a13_5jpp6
- fixed build with new plexus-containers

* Wed Mar 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.10-alt7.a13_5jpp6
- fixed build with maven3
- plexus-cli14 moved to subpackage

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.10-alt6.a13_5jpp6
- separated plexus-cdc a13

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.10-alt2_5jpp6
- obsolete plexus-cdc

* Mon Feb 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.10-alt1_5jpp6
- new jpp relase

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.10-alt1_3jpp6
- new jpp release

* Thu Jun 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.10-alt1_2jpp5
- new jpp release

