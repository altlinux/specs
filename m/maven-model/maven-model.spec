BuildRequires: google-collections
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2010, JPackage Project
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

# If you want to build with maven, 
# give rpmbuild option '--with maven'

%define with_maven %{?_with_maven:1}%{!?_with_maven:0}
%define without_maven %{!?_with_maven:1}%{?_with_maven:0}


Name:           maven-model
Version:        3.0.2
Release:        alt8_7jpp6
Epoch:          0
Summary:        Maven Model
License:        Apache Software License 2.0
Group:          Development/Java
URL:            http://maven.apache.org/

# svn export http://svn.apache.org/repos/asf/maven/components/tags/maven-model-3.0.2
Source0:        maven-model-3.0.2-src.tar.gz
Source1:        nomaven-model-3.0.2-build.xml
Source2:        maven-model-3.0.2.pom
Patch0:         maven-model-3.0.2-pom.patch

BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
%if %{with_maven}
BuildRequires:  maven2 >= 0:2.0.8
BuildRequires:  maven2-default-skin
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-project-info-reports
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-site
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  modello-maven-plugin
%endif
BuildRequires:  stax_1_0_api
BuildRequires:  classworlds >= 0:1.1
BuildRequires:  dom4j
BuildRequires:  jdom
BuildRequires:  modello >= 0:1.3
BuildRequires:  plexus-build-api
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-containers-container-default
BuildRequires:  plexus-utils
BuildRequires:  stax-utils

Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5

Requires:  plexus-utils
Requires:  stax-utils >= 0:0.0-0.20060502
Source44: import.info

%description
Maven's model for Java project.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if %{with_maven}
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.
%endif

%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1} build.xml

%patch0 -b .sav0

%build
%if %{with_maven}
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}
export MAVEN_OPTS="-Dmaven2.jpp.mode=true -Dmaven.repo.local=${MAVEN_REPO_LOCAL}"
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        install
cp target/%{name}-%{version}.jar .
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -P all-models \
        -s $(pwd)/settings.xml \
        install javadoc:javadoc site
cp %{name}-%{version}.jar target

%else

export CLASSPATH=$(build-classpath \
stax_1_0_api \
classworlds \
dom4j \
jdom \
modello/core \
modello/plugin-dom4j \
modello/plugin-java \
modello/plugin-jdom \
modello/plugin-stax \
modello/plugin-xml \
modello/plugin-xpp3 \
modello/plugin-xsd \
plexus/plexus-build-api \
plexus/classworlds \
plexus/containers-container-default \
plexus/utils \
stax-utils \
google-collections \
xbean/xbean-reflect \
)

java org.codehaus.modello.ModelloCli src/main/mdo/maven.mdo java target/generated-sources 4.0.0 false true
java org.codehaus.modello.ModelloCli src/main/mdo/maven.mdo xsd  target/generated-sources 4.0.0 false true
java org.codehaus.modello.ModelloCli src/main/mdo/maven.mdo jdom-writer target/generated-sources 4.0.0 false true
#
java org.codehaus.modello.ModelloCli src/main/mdo/maven.mdo xpp3-reader target/generated-sources 4.0.0 false true
java org.codehaus.modello.ModelloCli src/main/mdo/maven.mdo xpp3-writer target/generated-sources 4.0.0 false true
#
java org.codehaus.modello.ModelloCli src/main/mdo/maven.mdo dom4j-reader target/generated-sources 4.0.0 false true
java org.codehaus.modello.ModelloCli src/main/mdo/maven.mdo dom4j-writer target/generated-sources 4.0.0 false true
#
java org.codehaus.modello.ModelloCli src/main/mdo/maven.mdo stax-reader target/generated-sources 4.0.0 false true
java org.codehaus.modello.ModelloCli src/main/mdo/maven.mdo stax-writer target/generated-sources 4.0.0 false true
#
java org.codehaus.modello.ModelloCli src/main/mdo/maven.mdo java target/generated-sources 3.0.0 true true
java org.codehaus.modello.ModelloCli src/main/mdo/maven.mdo xsd  target/generated-sources 3.0.0 true true
java org.codehaus.modello.ModelloCli src/main/mdo/maven.mdo jdom-writer  target/generated-sources 3.0.0 true true
#
java org.codehaus.modello.ModelloCli src/main/mdo/maven.mdo xpp3-reader target/generated-sources 3.0.0 true true
java org.codehaus.modello.ModelloCli src/main/mdo/maven.mdo xpp3-writer target/generated-sources 3.0.0 true true
#
java org.codehaus.modello.ModelloCli src/main/mdo/maven.mdo dom4j-reader target/generated-sources 3.0.0 true true
java org.codehaus.modello.ModelloCli src/main/mdo/maven.mdo dom4j-writer target/generated-sources 3.0.0 true true
#
java org.codehaus.modello.ModelloCli src/main/mdo/maven.mdo stax-reader target/generated-sources 3.0.0 true true
java org.codehaus.modello.ModelloCli src/main/mdo/maven.mdo stax-writer target/generated-sources 3.0.0 true true



#    <!-- Need the original package as well -->
#    <ant:copy tofile="target/maven.mdo.m1" file="maven.mdo" />
#    <ant:replace file="target/maven.mdo.m1" token="org.apache.maven.model" value="org.apache.maven.project" />
sed -e 's/org\.apache\.maven\.model/org.apache.maven.project/' src/main/mdo/maven.mdo > target/maven.mdo.m1
#    <modello:generate model="target/maven.mdo.m1" type="java" packageWithVersion="false" version="3.0.0" targetDirectory="target/generated-sources" />
java org.codehaus.modello.ModelloCli target/maven.mdo.m1 java target/generated-sources 3.0.0 false true
#    <modello:generate model="target/maven.mdo.m1" type="xpp3-reader" packageWithVersion="false" version="3.0.0" targetDirectory="target/generated-sources" />
java org.codehaus.modello.ModelloCli target/maven.mdo.m1 xpp3-reader target/generated-sources 3.0.0 false true
#    <modello:generate model="target/maven.mdo.m1" type="xpp3-writer" packageWithVersion="false" version="3.0.0" targetDirectory="target/generated-sources" />
java org.codehaus.modello.ModelloCli target/maven.mdo.m1 xpp3-writer target/generated-sources 3.0.0 false true
#
java org.codehaus.modello.ModelloCli target/maven.mdo.m1 dom4j-reader target/generated-sources 3.0.0 false true
java org.codehaus.modello.ModelloCli target/maven.mdo.m1 dom4j-writer target/generated-sources 3.0.0 false true
java org.codehaus.modello.ModelloCli target/maven.mdo.m1 stax-reader target/generated-sources 3.0.0 false true
java org.codehaus.modello.ModelloCli target/maven.mdo.m1 stax-writer target/generated-sources 3.0.0 false true

ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc

%endif


%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 target/%{name}-%{version}-all.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-all-%{version}.jar
%add_to_maven_depmap maven %{name} %{version} JPP %{name}
%add_to_maven_depmap maven %{name}-all %{version} JPP %{name}-all
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)


# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{with_maven}
# manual
rm -rf target/site/apidocs 
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif

%files
%{_javadir}/*
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%if %{with_maven}
%files manual
%doc %{_docdir}/%{name}-%{version}
%endif

%changelog
* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.2-alt8_7jpp6
- fixed build with new testng and xbean

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.2-alt7_7jpp6
- fixed build

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.2-alt6_7jpp6
- built with org/apache/maven/project/io/stax

* Tue Feb 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.2-alt5_7jpp6
- fixed build

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.0.2-alt4_7jpp6
- new version

* Fri Sep 24 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.0.2-alt4_6jpp6
- added maven.report

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.0.2-alt3_6jpp6
- build w/3.0 API

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.0.2-alt3_3jpp5
- new jpp release

* Thu Mar 19 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.0.2-alt2jpp
modello-plexus bootstrap

