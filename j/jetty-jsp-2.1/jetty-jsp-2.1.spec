BuildRequires: maven-release maven-plugin-bundle
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# Copyright (c) 2000-2012, JPackage Project
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


Name:           jetty-jsp-2.1
Version:        20091210
Release:        alt3_2jpp6
Epoch:          0
Summary:        Jetty JSP-2.1 Modules
License:        CDDL
Url:            http://jetty.codehaus.org/jetty/
Group:          Development/Java
Source0:        jetty-jsp-2.1.v20091210.tgz
# svn export http://svn.codehaus.org/jetty/jsp/tags/jetty-jsp-2.1.v20091210/
# tar czf jetty-jsp-2.1.v20091210.tgz jetty-jsp-2.1.v20091210/
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        jsp-2.1-glassfish-src-prefetched.tgz
# pushd jsp-2.1-glassfish
# ant -Dglassfish.tag=SJSAS-2_1_1-B31G-19_Oct_2009 -f checkout.xml extract-src
# popd
# tar czf jsp-2.1-glassfish-src-prefetched.tgz jsp-2.1-glassfish/target/
Source4:        jsp-api-2.1-glassfish-src-prefetched.tgz
# pushd jsp-api-2.1-glassfish/
# ant -Dglassfish.tag=SJSAS-2_1_1-B31G-19_Oct_2009 -f checkout.xml extract-src
# popd
# tar czf jsp-api-2.1-glassfish-src-prefetched.tgz jsp-api-2.1-glassfish/target/
Source5:        jsr199-glassfish-src-prefetched.tgz
# pushd jsr199/
# ant -Dglassfish.tag=SJSAS-2_1_1-B31G-19_Oct_2009 -f checkout.xml extract-src
# popd
# tar czf jsr199-glassfish-src-prefetched.tgz jsr199/target/
Source6:        jetty-parent-8.pom
Source7:        jetty-parent-9.pom

Patch0:         jetty-jsp-2.1-glassfish-pom.patch
Patch1:         jetty-jsp-api-2.1-glassfish-pom.patch
Patch2:         jetty-jsp-taglibs-DataSourceWrapper.patch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  maven2 >= 0:2.0.8
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven-doxia
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  mojo-maven2-plugin-build-helper
BuildRequires:  mojo-parent
BuildRequires:  ecj3

BuildArch:      noarch


Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info


%description
JSP-2.1 modules from Glassfish for Jetty.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n jetty-jsp-2.1.v20091210
tar xzf %{SOURCE3}
tar xzf %{SOURCE4}
tar xzf %{SOURCE5}
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2

%build
cp %{SOURCE1} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository
mkdir -p $MAVEN_REPO_LOCAL/org/mortbay/jetty/jetty-parent/8/
cp %{SOURCE6} $MAVEN_REPO_LOCAL/org/mortbay/jetty/jetty-parent/8/jetty-parent-8.pom
mkdir -p $MAVEN_REPO_LOCAL/org/eclipse/jetty/jetty-parent/9/
cp %{SOURCE7} $MAVEN_REPO_LOCAL/org/eclipse/jetty/jetty-parent/9/jetty-parent-9.pom
mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Daggregate=true \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        install javadoc:javadoc


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 jsp-api-2.1-glassfish/target/jsp-api-2.1-glassfish-2.1.v%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-api-glassfish-%{version}.jar
install -m 644 jsp-api-2.1-glassfish/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-api-glassfish.pom
%add_to_maven_depmap org.mortbay.jetty jsp-api-2.1-glassfish 2.1v%{version} JPP %{name}-api-glassfish
install -m 644 jsp-2.1-glassfish/target/jsp-2.1-glassfish-2.1.v%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-glassfish-%{version}.jar
install -m 644 jsp-2.1-glassfish/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-glassfish.pom
%add_to_maven_depmap org.mortbay.jetty jsp-2.1-glassfish 2.1v%{version} JPP %{name}-glassfish
install -m 644 pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.mortbay.jetty jetty-jsp 2.1v%{version} JPP %{name}


(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink


%files 
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:20091210-alt3_2jpp6
- fixed build with maven3

* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:20091210-alt2_2jpp6
- new jpp release

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:20091210-alt2_1jpp6
- fixed build

* Sun Oct 17 2010 Igor Vlasenko <viy@altlinux.ru> 0:20091210-alt1_1jpp6
- fixed init script

