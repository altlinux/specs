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

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define _with_repolib 1

%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/hibernate-search/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirres %{repodir}/resources
%define repodirsrc %{repodir}/src


%define reltag GA
%define hname hibernate-search
%define namedversion %{version}.%{reltag}

Name:           hibernate3-search
Version:        3.1.1
Release:        alt2_1jpp6
Epoch:          0
Summary:        Hibernate integration with Lucene for indexing and querying data
License:        LGPLv2+
URL:            http://search.hibernate.org/
Group:          Databases
# svn -q export http://anonsvn.jboss.org/repos/hibernate/search/tags/v3_1_1_GA/ hibernate-search-3.1.1 && tar cjf hibernate-search-3.1.1.tar.bz2 hibernate-search-3.1.1
Source0:        hibernate-search-3.1.1.tar.bz2
Source2:        %{hname}-component-info.xml
Source3:        %{hname}-jpp-depmap.xml
Source4:        %{hname}-settings.xml
Source6:        solr-1.3.0.tar.gz
Source7:        activemq-5.2.0.tar.gz
Patch0:         %{hname}-pom.xml.patch

# The following are required to build %{hname}.jar
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: java-javadoc >= 1.5.0
BuildRequires: maven2
BuildRequires: maven2-plugin-source
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-release
BuildRequires: maven-release
BuildRequires: maven-surefire
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-doxia-sitetools
BuildRequires: jboss-parent
BuildRequires: jboss-javaee
BuildRequires: jboss-transaction-1.0.1-api
BuildRequires: junit >= 3.8.2
BuildRequires: hibernate3 >= 0:3.3.2
BuildRequires: hibernate3-commons-annotations >= 0:3.1.0
BuildRequires: hibernate3-annotations >= 0:3.4.0
BuildRequires: hibernate3-ejb-persistence-3.0-api >= 0:3.4.0
BuildRequires: hibernate3-entitymanager >= 0:3.4.0
BuildRequires: slf4j >= 1.5.6
BuildRequires: lucene >= 0:2.4.1
BuildRequires: lucene-contrib >= 0:2.4.1
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: hsqldb

Requires: hibernate3 >= 0:3.3.2
Requires: hibernate3-ejb-persistence-3.0-api >= 0:3.4.0
Requires: hibernate3-commons-annotations >= 0:3.1.0
Requires: hibernate3-annotations >= 0:3.4.0
Requires: hibernate3-entitymanager >= 0:3.4.0
Requires: jakarta-commons-codec >= 1.3
Requires: jakarta-commons-io >= 1.3.2

BuildArch:      noarch
Source44: import.info

%description
Hibernate, like all other object/relational mapping tools, 
requires metadata that governs the transformation of data 
from one representation to the other (and vice versa). In 
Hibernate 2.x, mapping metadata is most of the time declared 
in XML text files. Another option is XDoclet, utilizing 
Javadoc source code annotations and a preprocessor at compile 
time.
Hibernate Search brings the power of full text search engines
to the persistence domain model and Hibernate experience,
through transparent configuration (Hibernate Annotations)
and a common API.

%if %with repolib
%package         repolib
Summary:         Artifacts to be uploaded to a repository library
Group:        Development/Java

%description         repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{hname}-%{version}
%patch0 -b .sav
sed -i 's|__DOCS_DIR_PLACEHOLDER__|%{_javadocdir}/java|g' ./pom.xml
cp -p %{SOURCE4} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

#FIXME: Remove this stuff when solr and activemq are BRs
tar xzf %{SOURCE6}
tar xzf %{SOURCE7}

cp %{SOURCE2} .
sed -i 's/@VERSION@/%{version}.%{reltag}-brew/g' %{hname}-component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{hname}-component-info.xml

export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository

mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -Dmaven.repo.local=$MAVEN_REPO_LOCAL -Dmaven2.jpp.depmap.file=%{SOURCE3} install:install-file -DgroupId=org.apache.solr -DartifactId=solr-common -Dversion=1.3.0 -Dpackaging=jar -Dfile=${PWD}/org/apache/solr/solr-common/1.3.0/solr-common-1.3.0.jar
mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -Dmaven.repo.local=$MAVEN_REPO_LOCAL -Dmaven2.jpp.depmap.file=%{SOURCE3} install:install-file -DgroupId=org.apache.solr -DartifactId=solr-core -Dversion=1.3.0 -Dpackaging=jar -Dfile=${PWD}/org/apache/solr/solr-core/1.3.0/solr-core-1.3.0.jar

mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -Dmaven.repo.local=$MAVEN_REPO_LOCAL -Dmaven2.jpp.depmap.file=%{SOURCE3} install:install-file -DgroupId=org.apache.activemq -DartifactId=activemq-core -Dversion=5.2.0 -Dpackaging=jar -Dfile=${PWD}/org/apache/activemq/activemq-core/5.2.0/activemq-core-5.2.0.jar

%build
export LANG=en_US.ISO8859-1

export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository

mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE3} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.test.skip=true \
        -P with-optional-jars,hsqldb \
        install javadoc:javadoc

### ***  FIXME ***
## tests are skipped for now because of the following error:
## org.apache.maven.lifecycle.LifecycleExecutionException: Unable to instantiate POJO 'class org.hibernate.search.test.reader.functionality.TestableSharingBufferReaderProvider$MockIndexReader'; nested exception is java.lang.InstantiationException: org.hibernate.search.test.reader.functionality.TestableSharingBufferReaderProvider$MockIndexReader; nested exception is org.apache.maven.surefire.testset.TestSetFailedException: Unable to instantiate POJO 'class org.hibernate.search.test.reader.functionality.TestableSharingBufferReaderProvider$MockIndexReader'; nested exception is java.lang.InstantiationException: org.hibernate.search.test.reader.functionality.TestableSharingBufferReaderProvider$MockIndexReader

##FIXME: removed junit test target, should be added back in when 
## issues are resolved.
## This failures are expected in the junit target:
## org.hibernate.search.test.jms.slave.JMSSlaveTest
## In addition, for junitinstrument task is broken so it is not included

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}

cp -p target/%{hname}-%{version}.%{reltag}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
cp -p target/%{hname}-%{version}.%{reltag}-sources.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-sources-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|%{name}|%{hname}|g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

## javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
(cd $RPM_BUILD_ROOT%{_javadocdir} && for doc in *-%{version}; do ln -sf ${doc} `echo $doc| sed "s|%{name}|%{hname}|g"`; done)
(cd $RPM_BUILD_ROOT%{_javadocdir} && for doc in *-%{version}; do ln -sf ${doc} `echo $doc| sed "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%add_to_maven_depmap org.hibernate %{hname} %{namedversion} JPP %{name}
install -p -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -m 755 %{hname}-component-info.xml $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -m 755 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}

install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{repodirsrc}
install -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{repodirsrc}
install -m 755 %{SOURCE4} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{hname}.jar $RPM_BUILD_ROOT%{repodirlib}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{hname}-sources.jar $RPM_BUILD_ROOT%{repodirlib}
%endif

%files
%doc lgpl.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{hname}-%{version}.jar
%{_javadir}/%{hname}.jar
%{_javadir}/%{hname}-sources-%{version}.jar
%{_javadir}/%{hname}-sources.jar
%{_javadir}/%{name}-sources-%{version}.jar
%{_javadir}/%{name}-sources.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{_javadocdir}/%{hname}-%{version}
%{_javadocdir}/%{hname}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1.1-alt2_1jpp6
- fixed build with java 7

* Fri Feb 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.1.1-alt1_1jpp6
- new version

