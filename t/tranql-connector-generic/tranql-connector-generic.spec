BuildRequires:  maven-plugin-bundle geronimo-jta-1.0.1B-api geronimo-j2ee-connector-1.5-api
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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


Name:           tranql-connector-generic
Summary:        TranQL generic connector
Url:            http://tranql.codehaus.org
Version:        1.7
Release:        alt2_1jpp6
Epoch:          0
License:        Apache 2.0 License
Group:          Development/Java
Source0:        tranql-connector-generic-1.7.tgz
# svn export http://svn.codehaus.org/tranql/ra/tags/tranql-connector-generic-1.7/
# tar czf tranql-connector-generic-1.7.tgz tranql-connector-generic-1.7/

Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        tranql-connector-parent-1.8.pom
Source4:        http://mirrors.ibiblio.org/pub/mirrors/maven2/org/tranql/tranql-jar-resource-bundle/1.0/tranql-jar-resource-bundle-1.0.jar

Patch0:         tranql-connector-generic-ConnectionHandle-java6.patch
Patch1:         tranql-connector-generic-ConnectionWrapper-java6.patch
Patch2:         tranql-connector-generic-PreparedStatementHandle-java6.patch
Patch3:         tranql-connector-generic-PreparedStatementWrapper-java6.patch
Patch4:         tranql-connector-generic-StatementHandle-java6.patch
Patch5:         tranql-connector-generic-CallableStatementHandle-java6.patch
Patch6:         tranql-connector-generic-ResultSetHandle-java6.patch
Patch7:         tranql-connector-generic-DatabaseMetaDataHandle-java6.patch
Patch8:         tranql-connector-generic-DataSourceTest-java6.patch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  maven2 >= 0:2.0.8
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-idea
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven2-plugin-rar
BuildRequires:  maven2-plugin-remote-resources
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven-release
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  apache-commons-parent
BuildRequires:  geronimo-genesis
BuildRequires:  apache-commons-primitives
BuildRequires:  axion
BuildRequires:  javacc3

Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Requires:  apache-commons-primitives
Obsoletes: tranql-connector <= 0:1.2-alt3
Provides:  tranql-connector = %{epoch}:%{version}-%{release}

BuildArch:      noarch
Source44: import.info

%description
TranQL is a library for supporting access to data using 
different declarative query-based languages. For example, 
access to data could be provided using both SQL and EJBQL.

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
%patch0 -b .java6_0
%patch1 -b .java6_1
%patch2 -b .java6_2
%patch3 -b .java6_3
%patch4 -b .java6_4
%patch5 -b .java6_5
%patch6 -b .java6_6
%patch7 -b .java6_7
%patch8 -b .java6_8

%build
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL/

mkdir -p $MAVEN_REPO_LOCAL/org/tranql/tranql-connector-parent/1.8/
cp %{SOURCE3} $MAVEN_REPO_LOCAL/org/tranql/tranql-connector-parent/1.8/tranql-connector-parent-1.8.pom
mkdir -p $MAVEN_REPO_LOCAL/org/tranql/tranql-jar-resource-bundle/1.0/
cp %{SOURCE4} $MAVEN_REPO_LOCAL/org/tranql/tranql-jar-resource-bundle/1.0/tranql-jar-resource-bundle-1.0.jar

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export SETTINGS=$(pwd)/settings.xml

mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $SETTINGS \
        -Daggregate=true \
        -Dmaven.test.failure.ignore=false \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

%add_to_maven_depmap org.tranql tranql-connector-parent %{version} JPP tranql-connector-parent
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-tranql-connector-parent.pom

%add_to_maven_depmap org.tranql tranql-connector-generic %{version} JPP %{name}
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

%add_to_maven_depmap org.tranql tranql-connector %{version} JPP tranql-connector
install -m 644 tranql-connector/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-tranql-connector.pom
install -m 644 tranql-connector/target/tranql-connector-%{version}.jar $RPM_BUILD_ROOT%{_javadir}

%add_to_maven_depmap org.tranql tranql-connector-ra %{version} JPP tranql-connector-ra
install -m 644 tranql-connector-ra/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-tranql-connector-ra.pom
install -m 644 tranql-connector-ra/target/tranql-connector-ra-%{version}.rar $RPM_BUILD_ROOT%{_javadir}

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.?ar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/*.?ar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%doc LICENSE

%files javadoc
%doc %{_javadocdir}/*

%changelog
* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt2_1jpp6
- fixed build with maven3

* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_1jpp6
- converted from JPackage by jppimport script

