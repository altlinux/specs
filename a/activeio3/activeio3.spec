BuildRequires: backport-util-concurrent
BuildRequires: /proc
BuildRequires: jpackage-1.6-compat
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

%define gcj_support 0

%define oname activeio

Name:           activeio3
Summary:        ActiveIO Protocol Implementation Framework
Url:            http://activeio.codehaus.org/
Version:        3.0.1
Release:        alt4_2jpp6
Epoch:          0
License:        Apache Software License 2.0
Group:          Development/Java
Source0:        activeio-3.0.1.tar.gz
# svn export http://svn.apache.org/repos/asf/activemq/activeio/tags/activeio-3.0.1/

Source1:        activeio3-settings.xml
Source2:        activeio3-jpp-depmap.xml
Source3:        apache-jar-resource-bundle-1.3.jar

Patch0:         activeio3-pom.patch
Patch1:         activeio3-HowlJournal.patch
Patch2:         activeio3-core-pom.patch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  junit
BuildRequires:  maven2 >= 0:2.0.8
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-eclipse
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-remote-resources
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-stage
BuildRequires:  maven-release
BuildRequires:  maven-surefire-plugin
BuildRequires:  mojo-maven2-plugin-rat
BuildRequires:  apache-commons-parent
BuildRequires:  apache-jar-resource-bundle >= 0:1.4
#BuildRequires:  felix-maven2
BuildRequires:  geronimo-genesis

BuildRequires:  geronimo-specs
BuildRequires:  geronimo-j2ee-management-1.0-api
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-logging
#BuildRequires:  geronimo11-base
BuildRequires:  howl-logger
BuildRequires:  log4j

Requires:  backport-util-concurrent
Requires:  howl-logger
Requires:  apache-commons-logging

Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%if %{gcj_support}
BuildRequires:    gnu-crypto
BuildRequires:          java-gcj-compat-devel
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info

%description
ActiveIO provides a high performance IO framework 
for implementing protocols.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{version}
chmod -R go=u-w *
for f in $(find . -name "*.jar"); do
  mv $f $f.no
done
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2

# needs geronimo10
rm activeio-core/src/main/java/org/apache/activeio/xnet/StandardServiceStackGBean.java


cp %{SOURCE1} settings.xml

%build
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL/org.apache
cp %{SOURCE3} $MAVEN_REPO_LOCAL/org.apache/apache-jar-resource-bundle.jar

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export SETTINGS=$(pwd)/settings.xml

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $SETTINGS \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache.activemq activeio-parent %{version} JPP %{name}

install -m 644 %{oname}-core/target/%{oname}-core-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-core-%{version}.jar
install -m 644 %{oname}-core/target/%{oname}-core-%{version}-tests.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-core-tests-%{version}.jar
install -m 644 activeio-core/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-core.pom
%add_to_maven_depmap org.apache.activemq activeio-core %{version} JPP %{name}-core

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr activeio-core/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt4_2jpp6
- converted from JPackage by jppimport script

* Sun Jan 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt4_1jpp5
- adapted for new aspectj

* Mon Jan 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt3_1jpp5
- fixed build

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt2_1jpp5
- fixed build with new maven 2.0.8

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt1_1jpp5
- first build

