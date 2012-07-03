Patch33: geronimo-genesis-2.0-alt-maven3hack.patch
BuildRequires: maven-plugin-descriptor
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


Name:           geronimo-genesis2
Summary:        Geronimo Genesis
Url:            http://geronimo.apache.org/
Version:        2.0
Release:        alt2_1jpp6
Epoch:          0
License:        Apache 2.0 License
Group:          Development/Java
Source0:        geronimo-genesis-%{version}.tgz
# Steps to reproduce
# svn export http://svn.apache.org/repos/asf/geronimo/genesis/tags/genesis-2.0/ geronimo-genesis-2.0
# tar czf geronimo-genesis-2.0.tgz geronimo-genesis-2.0/


Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Patch0:         geronimo-genesis2-gmaven.patch
Patch1:         genesis-default-flava-pom.patch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  maven2 >= 0:2.0.8
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-idea
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven2-plugin-release
BuildRequires:  maven2-plugin-remote-resources
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  gmaven >= 0:1.3
BuildRequires:  gmaven-runtime-1.6

BuildRequires:  apache-jar-resource-bundle
BuildRequires:  apache-commons-parent
BuildRequires:  apache-commons-lang
BuildRequires:  gmaven

Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Requires:          ant >= 0:1.7.1
Requires:          apache-commons-lang
Requires:          gmaven >= 0:1.3
Requires:          plexus-utils

BuildArch:      noarch
Source44: import.info

%description
Genesis

%prep
%setup -q -n geronimo-genesis-%{version}
chmod -R go=u-w *
for f in $(find . -name "*.jar"); do
  mv $f $f.no
done
cp %{SOURCE1} settings.xml

%patch0 -b .gmaven
%patch1 -b .sav1
%patch33

%build
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL/org.apache
#cp %{SOURCE3} $MAVEN_REPO_LOCAL/org.apache/apache-jar-resource-bundle.jar

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export SETTINGS=$(pwd)/settings.xml

mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $SETTINGS \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/plugins

%add_to_maven_depmap org.apache.geronimo.genesis genesis %{version} JPP/%{name} genesis
install -m 644 pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-genesis.pom

%add_to_maven_depmap org.apache.geronimo.genesis apache-source-release-assembly-descriptor %{version} JPP/%{name} apache-source-release-assembly-descriptor
install -m 644 apache-source-release-assembly-descriptor/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-apache-source-release-assembly-descriptor.pom
install -m 644 apache-source-release-assembly-descriptor/target/apache-source-release-assembly-descriptor-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/apache-source-release-assembly-descriptor-%{version}.jar

%add_to_maven_depmap org.apache.geronimo.genesis genesis-maven-plugin %{version} JPP/%{name} genesis-maven-plugin
install -m 644 genesis-maven-plugin/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-genesis-maven-plugin.pom
install -m 644 genesis-maven-plugin/target/genesis-maven-plugin-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/genesis-maven-plugin-%{version}.jar

%add_to_maven_depmap org.apache.geronimo.genesis genesis-packaging %{version} JPP/%{name} genesis-packaging
install -m 644 genesis-packaging/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-genesis-packaging.pom
install -m 644 genesis-packaging/target/genesis-packaging-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/genesis-packaging-%{version}.jar

%add_to_maven_depmap org.apache.geronimo.genesis genesis-default-flava %{version} JPP/%{name} genesis-default-flava
install -m 644 genesis-default-flava/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-genesis-default-flava.pom

%add_to_maven_depmap org.apache.geronimo.genesis genesis-java6-flava %{version} JPP/%{name} genesis-java6-flava
install -m 644 genesis-default-flava/genesis-java6-flava/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-genesis-java6-flava.pom

%add_to_maven_depmap org.apache.geronimo.genesis genesis-java5-flava %{version} JPP/%{name} genesis-java5-flava
install -m 644 genesis-default-flava/genesis-java5-flava/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-genesis-java5-flava.pom

%add_to_maven_depmap org.apache.geronimo.genesis genesis-java1.4-flava %{version} JPP/%{name} genesis-java1.4-flava
install -m 644 genesis-default-flava/genesis-java1.4-flava/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-genesis-java1.4-flava.pom

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

%files
%{_javadir}/%{name}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%doc LICENSE

%changelog
* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_1jpp6
- fixed build with maven3

* Mon Jan 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_1jpp6
- new release

