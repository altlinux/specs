BuildRequires: maven-dependency-plugin
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# Copyright (c) 2000-2009, JPackage Project
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


Name:           geronimo-txmanager
Summary:        Geronimo Genesis
Url:            http://geronimo.apache.org/
Version:        2.1.1
Release:        alt2_2jpp5
Epoch:          0
License:        Apache 2.0 License
Group:          Development/Java
Source0:        %{name}-%{version}.tar.gz
# Steps to reproduce
# svn export http://svn.apache.org/repos/asf/geronimo/components/txmanager/tags/geronimo-txmanager-parent-2.1.1/ geronimo-txmanager-2.1.1

Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        apache-jar-resource-bundle-1.3.jar
Patch0:         geronimo-txmanager-pom.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: maven2
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-enforcer
BuildRequires: maven2-plugin-idea
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-release
BuildRequires: maven2-plugin-remote-resources
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-plugin
BuildRequires: mojo-maven2-support

BuildRequires: geronimo-genesis
BuildRequires: geronimo-jta-1.1-api
BuildRequires: geronimo-j2ee-connector-1.5-api
BuildRequires: jakarta-commons-jexl >= 0:1.1
BuildRequires: howl-logger >= 0:1.0.2


Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires: geronimo-genesis
Requires: jta_1_1_api
Requires: j2ee_connector_1_5_api
Requires: howl-logger >= 0:1.0.2

BuildArch:      noarch

%description
TxManager.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
chmod -R go=u-w *
for f in $(find . -name "*.jar"); do
  mv $f $f.no
done
cp %{SOURCE1} settings.xml
%patch0 -b .sav0

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

mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $SETTINGS \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

%add_to_maven_depmap org.apache.geronimo.components geronimo-txmanager-parent %{version} JPP %{name}
install -m 644 pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

%add_to_maven_depmap org.apache.geronimo.components geronimo-connector %{version} JPP geronimo-connector
install -m 644 geronimo-connector/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-geronimo-connector.pom
install -m 644 geronimo-connector/target/geronimo-connector-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/geronimo-connector-%{version}.jar
install -m 644 geronimo-connector/target/geronimo-connector-%{version}-tests.jar \
   $RPM_BUILD_ROOT%{_javadir}/geronimo-connector-tests-%{version}.jar
%add_to_maven_depmap org.apache.geronimo.components geronimo-connector-tests %{version} JPP geronimo-connector-tests

%add_to_maven_depmap org.apache.geronimo.components geronimo-transaction %{version} JPP geronimo-transaction
install -m 644 geronimo-transaction/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-geronimo-transaction.pom
install -m 644 geronimo-transaction/target/geronimo-transaction-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/geronimo-transaction-%{version}.jar
install -m 644 geronimo-transaction/target/geronimo-transaction-%{version}-tests.jar \
   $RPM_BUILD_ROOT%{_javadir}/geronimo-transaction-tests-%{version}.jar
%add_to_maven_depmap org.apache.geronimo.components geronimo-transaction-tests %{version} JPP geronimo-transaction-tests

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/geronimo-connector
cp -pr geronimo-connector/target/site/apidocs/* \
       $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/geronimo-connector
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/geronimo-transaction
cp -pr geronimo-transaction/target/site/apidocs/* \
       $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/geronimo-transaction
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%doc geronimo-connector/LICENSE.txt

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_2jpp5
- fixed build with maven3

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_2jpp5
- new version

