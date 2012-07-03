Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 1.0.1
%define name jettison
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_with          maven

%define gcj_support 0

%define _with_repolib 1

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define namedver    %{version}

%define version_full %{namedver}

%define repodir_root repository.jboss.com
%define repodir_release codehaus-%{name}/%{version_full}
%define repodir %{_javadir}/%{repodir_root}/%{repodir_release}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

Name:           jettison
Version:        1.0.1
Release:        alt1_2jpp5
Epoch:          0
Summary:        JSON StAX Implementation
License:        ASL 2.0
Group:          Development/Java
URL:            http://jettison.codehaus.org
# svn export http://svn.codehaus.org/jettison/tags/jettison-1.0.1/ jettison-1.0.1
# tar cjf jettison-1.0.1.tar.bz2 jettison-1.0.1
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-build.xml
Source4:        %{name}-component-info.xml
Patch0:         %{name}-BadgerFishXMLStreamWriterTest.patch
Requires: jakarta-slide-webdavclient
Requires: jetty5
Requires: jpackage-utils >= 0:1.7.2
Requires: servletapi5
Requires: stax_1_0_api
Requires: xml-commons-jaxp-1.3-apis
BuildRequires: ant >= 0:1.6
BuildRequires: jpackage-utils >= 0:1.7.2
BuildRequires: junit >= 0:3.8.2
%if %with maven
BuildRequires: maven2 >= 2.0.4-10jpp
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-plugin
%endif
Requires(post): jpackage-utils >= 0:1.7.2
Requires(postun): jpackage-utils >= 0:1.7.2
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
BuildRequires: jakarta-slide-webdavclient
BuildRequires: jetty5
BuildRequires: servletapi5
BuildRequires: stax_1_0_api
BuildRequires: xml-commons-jaxp-1.3-apis

%description
Jettison is a collection of StAX parsers and writers which 
read and write JSON. This allows nearly transparent 
enablement of JSON based web services in services 
frameworks like CXF.
There are currently two included conventions for mapping 
JSON to XML. The first, is BadgerFish which implements the 
full XML infoset in JSON using various techniques. 
The second, is called the "mapped" convention. It allows 
you to manually map XML namespaces to JSON element prefixes.
Jettison was developed for usage in XFire and CXF to enable 
JSON based services.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if %{with_repolib}
%package repolib
Summary:     Artifacts to be uploaded to a repository library
Group:       Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q
cp -p %{SOURCE1} settings.xml
cp -p %{SOURCE3} build.xml
%patch0 -p0

%build
%if %with maven
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

mvn-jpp \
        -e \
        -s $(pwd)/settings.xml \
        -Dmaven2.jpp.mode=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc
%else
export CLASSPATH=$(build-classpath stax_1_0_api jetty5/jetty5 servletapi5):target/classes:target/test-classes
export OPT_JAR_LIST="junit ant/ant-junit"
ant -Dbuild.sysclasspath=only jar javadoc
%endif

pushd src/main/java
%{jar} cf ../../../target/%{name}-src-%{namedver}.jar org
pushd ../resources
%{jar} uf ../../../target/%{name}-src-%{namedver}.jar META-INF
popd
popd

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap org.codehaus.jettison %{name} %{namedver} JPP %{name}

# create unprefixed and unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{with_repolib}
    install -d -m 755 $RPM_BUILD_ROOT%{repodir}
    install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
    install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
    install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}

    cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/%{name}.jar
    cp -p target/%{name}-src-%{namedver}.jar $RPM_BUILD_ROOT%{repodirlib}/%{name}-src.jar

    cp -p %{SOURCE4} $RPM_BUILD_ROOT%{repodir}/component-info.xml
    sed -i 's/@VERSION@/%{version_full}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
    tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
    sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-*%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %{with_repolib}
%files repolib
%{_javadir}/%{repodir_root}
%endif
%dir %_javadir/repository.jboss.com/codehaus-jettison

%changelog
* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_2jpp5
- use default jpp profile

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.rc2.1jpp5
- jpp5 build

* Mon Dec 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.rc1.1jpp1.7
- added dependency on new excalibur

* Thu Nov 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.rc1.1jpp1.7
- converted from JPackage by jppimport script

