Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.5.0-compat
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

## If you don't want to build with maven, and use straight ant instead,
## give rpmbuild option '--without maven'

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}


%define ucname         JPOX

Name:           jpox
Summary:        Java Persistent Objects
Version:        1.1.1
Release:        alt5_2jpp5
Epoch:          0
URL:            http://www.jpox.org
License:        Apache License, Version 2.0
Group:          Development/Java
Source0:        JPOX-1.1.1.tar.gz
# cvs -d:pserver:anonymous@jpox.cvs.sourceforge.net:/cvsroot/jpox login
# cvs -z3 -d:pserver:anonymous@jpox.cvs.sourceforge.net:/cvsroot/jpox export -r JPOX-1_1_1 JPOX
# mv JPOX/ JPOX-1.1.1
# tar cf JPOX-1.1.1.tar JPOX-1.1.1/
# gzip JPOX-1.1.1.tar
Source1:        maven2jpp-mapdeps.xsl
Source2:        JPOX-1.1.1-jpp-depmap.xml

Source3:        JPOX-1.1.1-Plugins-C3P0-build.xml
Source4:        JPOX-1.1.1-Plugins-DBCP-build.xml
Source5:        JPOX-1.1.1-Plugins-Ehcache-build.xml
Source6:        JPOX-1.1.1-Plugins-Java5-build.xml
Source7:        JPOX-1.1.1-Plugins-JPOXTest-build.xml
Source8:        JPOX-1.1.1-Plugins-Maven1-build.xml
Source9:        JPOX-1.1.1-Plugins-Maven1-FAQ-build.xml
Source10:       JPOX-1.1.1-Plugins-Maven2-build.xml
Source11:       JPOX-1.1.1-Plugins-OSCache-build.xml
Source12:       JPOX-1.1.1-Plugins-Spatial-build.xml
Source13:       JPOX-1.1.1-Plugins-SpatialOracle-build.xml
Source14:       JPOX-1.1.1-Plugins-SpringFramework-build.xml
Source15:       JPOX-1.1.1-Plugins-SwarmCache-build.xml
Source16:       JPOX-1.1.1-Plugins-TangosolCache-build.xml
Source17:       JPOX-1.1.1-Plugins-ThirdParty-build.xml
Source18:       JPOX-1.1.1-Plugins-XMLTypeOracle-build.xml
Source19:       JPOX-1.1.1-Enhancer-build.xml
Source20:       http://repo1.maven.org/maven2/jpox/jpox/1.1.1/jpox-1.1.1.pom
Source21:       http://repo1.maven.org/maven2/jpox/jpox-c3p0/1.1.1/jpox-c3p0-1.1.1.pom
Source22:       http://repo1.maven.org/maven2/jpox/jpox-dbcp/1.1.1/jpox-dbcp-1.1.1.pom
Source23:       http://repo1.maven.org/maven2/jpox/jpox-ehcache/1.1.1/jpox-ehcache-1.1.1.pom
Source24:       http://repo1.maven.org/maven2/jpox/jpox-enhancer/1.1.1/jpox-enhancer-1.1.1.pom
Source25:       http://repo1.maven.org/maven2/jpox/jpox-java5/1.1.1/jpox-java5-1.1.1.pom
Source26:       http://repo1.maven.org/maven2/jpox/jpox-oscache/1.1.1/jpox-oscache-1.1.1.pom
Source27:       http://repo1.maven.org/maven2/jpox/jpox-parent/1.1.1/jpox-parent-1.1.1.pom
Source28:       http://repo1.maven.org/maven2/jpox/jpox-proxool/1.1.1/jpox-proxool-1.1.1.pom
Source29:       http://repo1.maven.org/maven2/jpox/jpox-shell/1.1.1/jpox-shell-1.1.1.pom
Source30:       http://repo1.maven.org/maven2/jpox/jpox-spatial/1.1.1/jpox-spatial-1.1.1.pom
Source31:       http://repo1.maven.org/maven2/jpox/jpox-spatialoracle/1.1.1/jpox-spatialoracle-1.1.1.pom
Source32:       http://repo1.maven.org/maven2/jpox/jpox-springframework/1.1.1/jpox-springframework-1.1.1.pom
Source33:       http://repo1.maven.org/maven2/jpox/jpox-swarmcache/1.1.1/jpox-swarmcache-1.1.1.pom
Source34:       http://repo1.maven.org/maven2/jpox/jpox-tangosol/1.1.1/jpox-tangosol-1.1.1.pom
Source35:       http://repo1.maven.org/maven2/jpox/jpox-xmltypeoracle/1.1.1/jpox-xmltypeoracle-1.1.1.pom


Patch0:         JPOX-1.1.1-project_xml.patch
Patch1:         JPOX-1.1.1-Core-project_xml.patch
Patch2:         JPOX-1.1.1-Core-maven_xml.patch
Patch3:         JPOX-1.1.1-Enhancer-project_xml.patch
Patch4:         JPOX-1.1.1-Core-build_properties.patch


BuildRequires: jpackage-utils >= 0:1.7.4
%if %{with_maven}
BuildRequires: maven1 >= 1.1
BuildRequires: maven1-plugins-base
BuildRequires: maven1-plugin-multiproject
BuildRequires: maven1-plugin-changelog
BuildRequires: maven1-plugin-changes
BuildRequires: maven1-plugin-checkstyle
BuildRequires: maven1-plugin-developer-activity
BuildRequires: maven1-plugin-faq
BuildRequires: maven1-plugin-file-activity
BuildRequires: maven1-plugin-javadoc
BuildRequires: maven1-plugin-jdepend
BuildRequires: maven1-plugin-jxr
BuildRequires: maven1-plugin-license
BuildRequires: maven1-plugin-linkcheck
BuildRequires: maven1-plugin-pmd
BuildRequires: maven1-plugin-tasklist
BuildRequires: maven1-plugin-test
BuildRequires: maven1-plugin-xdoc
BuildRequires: saxon
BuildRequires: saxon-scripts
%endif
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-nodeps
BuildRequires: ant-junit
BuildRequires: junit >= 0:3.8.1
BuildRequires: jakarta-commons-collections >= 0:3.1
BuildRequires: jakarta-commons-dbcp >= 0:1.2
BuildRequires: jakarta-commons-pool >= 0:1.2
BuildRequires: log4j >= 0:1.2.8
BuildRequires: geronimo-j2ee-connector-1.5-api
BuildRequires: geronimo-jta-1.0.1B-api
BuildRequires: bcel >= 0:5.1
BuildRequires: c3p0
BuildRequires: ehcache
BuildRequires: apache-jdo-2.0-api
BuildRequires: jakarta-commons-jelly-tags-xml
BuildRequires: dom4j
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: xerces-j2
BuildRequires: oscache
BuildRequires: swarmcache
BuildRequires: spring-all

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%if ! %{gcj_support}
BuildArch:      noarch
%endif
Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4
Patch33: JPOX-1.1.1-alt-jpp5.patch

%description
JPOX is a heterogenous persistence solution for Java. It 
allows you and your team to take your Java data model objects
and persist them to a datastore without having to spend large
amounts of time defining how they will be persisted.
This means that you can concentrate your application
development time on adding business logic rather than the
routine task of storing/retrieval of your objects. 

JPOX is designed to comply with all pertinent standards in
the persistence domain. It is a fully compliant implementation
of the JDO1/JDO2 specifications, and is planned to comply with
the JPA1 specification in its next release. This means that by
choosing JPOX you have persistence behaviour that you can trust
and is defined in Java standards specifications. In addition
JPOX is extensible utilising the OSGi standard plugin mechanism
and providing many extension points where you can enhance your
persistence capabilities even further.


%package core
Group:          Development/Java
Summary:        JPOX Core
Requires: ant
Requires: jdo20
Requires: jta_1_0_1B_api
Requires: j2ee-connector
Requires: log4j

%description core
%{summary}.

%package enhancer
Group:          Development/Java
Summary:        JPOX Enhancer
Requires: %{name}-core = %{version}-%{release}
Requires: ant
Requires: bcel
Requires: jdo20
Requires: log4j

%description enhancer
%{summary}.

%package c3p0
Group:          Development/Java
Summary:        JPOX C3P0 Plugin
Requires: %{name}-core = %{version}-%{release}
Requires: c3p0
Requires: jdo20
Requires: log4j

%description c3p0
%{summary}.

%package dbcp
Group:          Development/Java
Summary:        JPOX DBCP Plugin
Requires: %{name}-core = %{version}-%{release}
Requires: jakarta-commons-collections
Requires: jakarta-commons-dbcp
Requires: jakarta-commons-pool
Requires: jdo20
Requires: log4j

%description dbcp
%{summary}.

%package ehcache
Group:          Development/Java
Summary:        JPOX Ehcache Plugin
Requires: %{name}-core = %{version}-%{release}
Requires: ehcache
Requires: jdo20
Requires: log4j

%description ehcache
%{summary}.

%package java5
Group:          Development/Java
Summary:        JPOX Java5 Plugin
Requires: %{name}-core = %{version}-%{release}
Requires: jdo20
Requires: log4j

%description java5
%{summary}.

%package maven-plugin
Group:          Development/Java
Summary:        JPOX Maven1 Plugin
Requires: %{name}-core = %{version}-%{release}
Requires: maven1
Requires: jdo20

%description maven-plugin
%{summary}.

%package maven-faq-plugin
Group:          Development/Java
Summary:        JPOX Maven1 FAQ Plugin
Requires: %{name}-core = %{version}-%{release}
Requires: maven1
Requires: jdo20

%description maven-faq-plugin
%{summary}.

%package oscache
Group:          Development/Java
Summary:        JPOX OSCache Plugin
Requires: %{name}-core = %{version}-%{release}
Requires: oscache
Requires: jdo20

%description oscache
%{summary}.

%package spatial
Group:          Development/Java
Summary:        JPOX Spatial Plugin
Requires: %{name}-core = %{version}-%{release}
Requires: jdo20
Requires: log4j

%description spatial
%{summary}.

%package spring
Group:          Development/Java
Summary:        JPOX Spring Plugin
Requires: %{name}-core = %{version}-%{release}
Requires: jdo20
Requires: log4j
Requires: spring-core
Requires: spring-beans

%description spring
%{summary}.

%package swarmcache
Group:          Development/Java
Summary:        JPOX SwarmCache Plugin
Requires: %{name}-core = %{version}-%{release}
Requires: jdo20
Requires: swarmcache

%description swarmcache
%{summary}.

%package tangosol
Group:          Development/Java
Summary:        JPOX TangosolCache Plugin
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-thirdparty = %{version}-%{release}
Requires: jdo20
Requires: log4j

%description tangosol
%{summary}.

%package thirdparty
Group:          Development/Java
Summary:        JPOX ThirdParty Plugin
Requires: %{name}-core = %{version}-%{release}

%description thirdparty
%{summary}.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for JPOX
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{ucname}-%{version}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav
%patch4 -b .sav
cp %{SOURCE3}   Plugins/C3P0/build.xml
cp %{SOURCE4}   Plugins/DBCP/build.xml
cp %{SOURCE5}   Plugins/Ehcache/build.xml
cp %{SOURCE6}   Plugins/Java5/build.xml
cp %{SOURCE7}   Plugins/JPOXTest/build.xml
cp %{SOURCE8}   Plugins/Maven1/build.xml
cp %{SOURCE9}   Plugins/Maven1-FAQ/build.xml
cp %{SOURCE10}  Plugins/Maven2/build.xml
cp %{SOURCE11}  Plugins/OSCache/build.xml
cp %{SOURCE12}  Plugins/Spatial/build.xml
cp %{SOURCE13}  Plugins/SpatialOracle/build.xml
cp %{SOURCE14}  Plugins/SpringFramework/build.xml
cp %{SOURCE15}  Plugins/SwarmCache/build.xml
cp %{SOURCE16}  Plugins/TangosolCache/build.xml
cp %{SOURCE17}  Plugins/ThirdParty/build.xml
cp %{SOURCE18}  Plugins/XMLTypeOracle/build.xml
cp %{SOURCE19}  Enhancer/build.xml


%if %{with_maven}
find . -name build.properties -exec rm -f {} \;
%endif
%patch33 -p1

%build
unset CLASSPATH
rm -rf samples
%if %{with_maven}
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE1} map=%{SOURCE2}
    popd
done

export MAVEN_HOME_LOCAL=$(pwd)/.maven
mkdir -p $MAVEN_HOME_LOCAL/repository/javax.jdo/jars/
pushd $MAVEN_HOME_LOCAL/repository/javax.jdo/jars/
ln -sf $(build-classpath jdo20) jdo2-api-SNAPSHOT.jar
popd
mkdir -p $MAVEN_HOME_LOCAL/repository/jdbc/jars/
pushd $MAVEN_HOME_LOCAL/repository/jdbc/jars/
ln -sf $(build-classpath jdbc-stdext) jdbc-stdext-2.0.jar
popd

maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
-Dmaven.test.skip=true \        -Dmaven.home.local=$MAVEN_HOME_LOCAL \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.multiproject.includes=*/project.xml,Plugins/*/project.xml \
        -Dmaven.multiproject.excludes=Plugins/XMLTypeOracle/project.xml,Plugins/SpatialOracle/project.xml \
        -Dgoal=jar:install,javadoc \
        multiproject:goal

%else
pushd Enhancer/lib
ln -sf $(build-classpath bcel) bcel-5.1.jar
ln -sf $(build-classpath bcel) bcel-5.2.jar
popd
pushd Core
pushd lib
ln -sf $(build-classpath ant) ant-1.6.jar
ln -sf $(build-classpath commons-collections) commons-collections-3.1.jar
ln -sf $(build-classpath commons-dbcp) commons-dbcp-1.2.jar
ln -sf $(build-classpath commons-pool) commons-pool-1.2.jar
ln -sf $(build-classpath jaas) jaas-1.0.01.jar
ln -sf $(build-classpath geronimo-j2ee-connector-1.5-api) jca-1.0.jar
ln -sf $(build-classpath jdbc-stdext) jdbc2_0-stdext.jar
ln -sf $(build-classpath jdo20) jdo2-api-SNAPSHOT.jar
#jpa-1.0.jar
ln -sf $(build-classpath geronimo-jta-1.0.1B-api) jta-1.0.1B.jar
ln -sf $(build-classpath junit) junit-3.8.1.jar
ln -sf $(build-classpath log4j) log4j-1.2.8.jar
popd
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 rar javadoc
popd
pushd Enhancer
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djpox.jar=file://$(pwd)/../dist/%{name}-%{version}.jar \
    -Dlog4j.jar=file://$(build-classpath log4j) \
    -Djdo2-api.jar=file://$(build-classpath jdo20) \
    -Dbcel.jar=file://$(build-classpath bcel) \
    -Dant.jar=file://$(build-classpath ant) \
    -Djunit.jar=file://$(build-classpath junit) \
    dist
popd
pushd Plugins
pushd C3P0
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djpox.jar=file:$(pwd)/../../dist/%{name}-%{version}.jar \
    -Dlog4j.jar=file://$(build-classpath log4j) \
    -Djdbc-stdext.jar=file://$(build-classpath jdbc-stdext) \
    -Djdo2-api.jar=file://$(build-classpath jdo20) \
    -Dc3p0.jar=file://$(build-classpath c3p0) \
    -Djunit.jar=file://$(build-classpath junit) \
    dist
popd
pushd DBCP
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djpox.jar=file:$(pwd)/../../dist/%{name}-%{version}.jar \
    -Dlog4j.jar=file://$(build-classpath log4j) \
    -Djdbc-stdext.jar=file://$(build-classpath jdbc-stdext) \
    -Djdo2-api.jar=file://$(build-classpath jdo20) \
    -Dcommons-dbcp.jar=file://$(build-classpath commons-dbcp) \
    -Dcommons-pool.jar=file://$(build-classpath commons-pool) \
    -Dcommons-collections.jar=file://$(build-classpath commons-collections) \
    -Djunit.jar=file://$(build-classpath junit) \
    dist
popd
pushd Ehcache
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djpox.jar=file:$(pwd)/../../dist/%{name}-%{version}.jar \
    -Dehcache.jar=file://$(build-classpath ehcache) \
    -Djdo2-api.jar=file://$(build-classpath jdo20) \
    -Dlog4j.jar=file://$(build-classpath log4j) \
    -Djunit.jar=file://$(build-classpath junit) \
    dist
popd
pushd Java5
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djpox.jar=file:$(pwd)/../../dist/%{name}-%{version}.jar \
    -Djdo2-api.jar=file://$(build-classpath jdo20) \
    -Dlog4j.jar=file://$(build-classpath log4j) \
    -Djunit.jar=file://$(build-classpath junit) \
    dist
popd
pushd JPOXTest
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djpox.jar=file:$(pwd)/../../dist/%{name}-%{version}.jar \
    -Djpox-enhancer.jar=file:$(pwd)/../../dist/%{name}-enhancer-%{version}.jar \
    -Dbcel.jar=file://$(build-classpath bcel) \
    -Djunit.jar=file://$(build-classpath junit) \
    jar
popd
pushd Maven1
mkdir plugin-resources
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djpox.jar=file:$(pwd)/../../dist/%{name}-%{version}.jar \
    -Djpox-enhancer.jar=file:$(pwd)/../../dist/%{name}-enhancer-%{version}.jar \
    -Dbcel.jar=file://$(build-classpath bcel) \
    -Djdo2-api.jar=file://$(build-classpath jdo20) \
    -Dlog4j.jar=file://$(build-classpath log4j) \
    -Djunit.jar=file://$(build-classpath junit) \
    jar
popd
pushd Maven1-FAQ
mkdir plugin-resources
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djpox.jar=file:$(pwd)/../../dist/%{name}-%{version}.jar \
    -Dcommons-jelly-tags-xml.jar=file://$(build-classpath commons-jelly-tags-xml) \
    -Ddom4j.jar=file://$(build-classpath dom4j) \
    -Dxml-apis.jar=file://$(build-classpath xml-commons-jaxp-1.3-apis) \
    -Dxerces.jar=file://$(build-classpath xerces-j2) \
    -Djunit.jar=file://$(build-classpath junit) \
    jar
popd
#pushd Maven2
#ant -Djpox.jar=file:$(pwd)/../../dist/%{name}-%{version}.jar dist
#popd
pushd OSCache
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djpox.jar=file:$(pwd)/../../dist/%{name}-%{version}.jar \
    -Doscache.jar=file://$(build-classpath oscache) \
    -Djdo2-api.jar=file://$(build-classpath jdo20) \
    -Djunit.jar=file://$(build-classpath junit) \
    dist
popd
pushd Spatial
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djpox.jar=file:$(pwd)/../../dist/%{name}-%{version}.jar \
    -Djdo2-api.jar=file://$(build-classpath jdo20) \
    -Dlog4j.jar=file://$(build-classpath log4j) \
    -Djunit.jar=file://$(build-classpath junit) \
    dist
popd
#pushd SpatialOracle
#ant \
#   -Djpox-spatial.jar=file:$(pwd)/../Spatial/target/jpox-spatial-SNAPSHOT.jar \
#   -Djpox.jar=file:$(pwd)/../../dist/%{name}-%{version}.jar dist
#popd
pushd SpringFramework
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djpox.jar=file:$(pwd)/../../dist/%{name}-%{version}.jar \
    -Dspring.jar=file://$(build-classpath spring) \
    -Djdo2-api.jar=file://$(build-classpath jdo20) \
    -Dlog4j.jar=file://$(build-classpath log4j) \
    -Djunit.jar=file://$(build-classpath junit) \
    dist
popd
pushd SwarmCache
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djpox.jar=file:$(pwd)/../../dist/%{name}-%{version}.jar \
    -Dswarmcache.jar=file://$(build-classpath swarmcache) \
    -Djdo2-api.jar=file://$(build-classpath jdo20) \
    -Djunit.jar=file://$(build-classpath junit) \
    dist
popd
pushd ThirdParty
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djpox.jar=file:$(pwd)/../../dist/%{name}-%{version}.jar \
    -Djunit.jar=file://$(build-classpath junit) \
    dist
popd
pushd TangosolCache
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
   -Djpox-thirdparty.jar=file:$(pwd)/../ThirdParty/target/jpox-thirdparty-SNAPSHOT.jar \
   -Djpox.jar=file:$(pwd)/../../dist/%{name}-%{version}.jar \
    -Djdo2-api.jar=file://$(build-classpath jdo20) \
    -Dlog4j.jar=file://$(build-classpath log4j) \
    -Djunit.jar=file://$(build-classpath junit) \
    dist
popd
#pushd XMLTypeOracle
#ant -Djpox.jar=file:$(pwd)/../../dist/%{name}-%{version}.jar dist
#popd
popd
%endif

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}
# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

%add_to_maven_depmap %{name} %{name}-parent %{version} JPP/%{name} parent
install -m 644 %{SOURCE27} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-parent.pom

%if %{with_maven}
install -m 644 Core/target/jpox-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/core-%{version}.jar
install -m 644 Enhancer/target/jpox-enhancer-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/enhancer-%{version}.jar
%else
install -m 644 dist/%{name}-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/core-%{version}.jar
install -m 644 dist/%{name}-enhancer-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/enhancer-%{version}.jar
%endif
%add_to_maven_depmap %{name} %{name} %{version} JPP/%{name} core
install -m 644 %{SOURCE20} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-core.pom
%add_to_maven_depmap %{name} %{name}-enhancer %{version} JPP/%{name} enhancer
install -m 644 %{SOURCE24} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-enhancer.pom

#Source19:       http://repo1.maven.org/maven2/jpox/jpox/1.1.1/jpox-1.1.1.pom
#Source20:       http://repo1.maven.org/maven2/jpox/jpox-c3p0/1.1.1/jpox-c3p0-1.1.1.pom
#Source21:       http://repo1.maven.org/maven2/jpox/jpox-dbcp/1.1.1/jpox-dbcp-1.1.1.pom
#Source22:       http://repo1.maven.org/maven2/jpox/jpox-ehcache/1.1.1/jpox-ehcache-1.1.1.pom
#Source23:       http://repo1.maven.org/maven2/jpox/jpox-enhancer/1.1.1/jpox-enhancer-1.1.1.pom
#Source24:       http://repo1.maven.org/maven2/jpox/jpox-java5/1.1.1/jpox-java5-1.1.1.pom
#Source25:       http://repo1.maven.org/maven2/jpox/jpox-oscache/1.1.1/jpox-oscache-1.1.1.pom
#Source26:       http://repo1.maven.org/maven2/jpox/jpox-parent/1.1.1/jpox-parent-1.1.1.pom
#Source27:       http://repo1.maven.org/maven2/jpox/jpox-proxool/1.1.1/jpox-proxool-1.1.1.pom
#Source28:       http://repo1.maven.org/maven2/jpox/jpox-shell/1.1.1/jpox-shell-1.1.1.pom
#Source29:       http://repo1.maven.org/maven2/jpox/jpox-spatial/1.1.1/jpox-spatial-1.1.1.pom
#Source30:       http://repo1.maven.org/maven2/jpox/jpox-spatialoracle/1.1.1/jpox-spatialoracle-1.1.1.pom
#Source31:       http://repo1.maven.org/maven2/jpox/jpox-springframework/1.1.1/jpox-springframework-1.1.1.pom
#Source32:       http://repo1.maven.org/maven2/jpox/jpox-swarmcache/1.1.1/jpox-swarmcache-1.1.1.pom
#Source33:       http://repo1.maven.org/maven2/jpox/jpox-tangosol/1.1.1/jpox-tangosol-1.1.1.pom
#Source34:       http://repo1.maven.org/maven2/jpox/jpox-xmltypeoracle/1.1.1/jpox-xmltypeoracle-1.1.1.pom

install -m 644 Plugins/C3P0/target/jpox-c3p0-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/c3p0-%{version}.jar
%add_to_maven_depmap %{name} %{name}-c3p0 %{version} JPP/%{name} c3p0
install -m 644 %{SOURCE21} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-c3p0.pom

install -m 644 Plugins/DBCP/target/jpox-dbcp-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/dbcp-%{version}.jar
%add_to_maven_depmap %{name} %{name}-dbcp %{version} JPP/%{name} dbcp
install -m 644 %{SOURCE22} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-dbcp.pom

install -m 644 Plugins/Ehcache/target/jpox-ehcache-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/ehcache-%{version}.jar
%add_to_maven_depmap %{name} %{name}-ehcache %{version} JPP/%{name} ehcache
install -m 644 %{SOURCE23} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-ehcache.pom

install -m 644 Plugins/Java5/target/jpox-java5-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/java5-%{version}.jar
%add_to_maven_depmap %{name} %{name}-java5 %{version} JPP/%{name} java5
install -m 644 %{SOURCE25} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-java5.pom

install -m 644 Plugins/Maven1/target/maven-jpox-plugin-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/maven-plugin-%{version}.jar
install -m 644 Plugins/Maven1-FAQ/target/maven-faq-plugin-1.2jpox.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/maven-faq-plugin-%{version}.jar

install -m 644 Plugins/OSCache/target/jpox-oscache-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/oscache-%{version}.jar
%add_to_maven_depmap %{name} %{name}-oscache %{version} JPP/%{name} oscache
install -m 644 %{SOURCE26} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-oscache.pom

install -m 644 Plugins/Spatial/target/jpox-spatial-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/spatial-%{version}.jar
%add_to_maven_depmap %{name} %{name}-spatial %{version} JPP/%{name} spatial
install -m 644 %{SOURCE30} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-spatial.pom

install -m 644 Plugins/SpringFramework/target/jpox-springframework-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/spring-%{version}.jar
%add_to_maven_depmap %{name} %{name}-springframework %{version} JPP/%{name} springframework
install -m 644 %{SOURCE32} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-springframework.pom

install -m 644 Plugins/SwarmCache/target/jpox-swarmcache-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/swarmcache-%{version}.jar
%add_to_maven_depmap %{name} %{name}-swarmcache %{version} JPP/%{name} swarmcache
install -m 644 %{SOURCE33} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-swarmcache.pom

install -m 644 Plugins/TangosolCache/target/jpox-tangosol-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/tangosol-%{version}.jar
%add_to_maven_depmap %{name} %{name}-tangosol %{version} JPP/%{name} tangosol
install -m 644 %{SOURCE34} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-tangosol.pom

install -m 644 Plugins/ThirdParty/target/jpox-thirdparty-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/thirdparty-%{version}.jar

pushd $RPM_BUILD_ROOT%{_javadir}/%{name}
for jar in *-%{version}.jar; do
    ln -sf ${jar} `echo $jar| sed "s|-%{version}\.jar|.jar|g"`;
done
popd

# Javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/enhancer
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/c3p0
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/dbcp
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/ehcache
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/java5
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/oscache
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/spatial
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/spring
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/swarmcache
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/tangosol
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/thirdparty

%if %{with_maven}
cp -pr Core/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core
%else
cp -pr Core/doc/api/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core
%endif
cp -pr Enhancer/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/enhancer
cp -pr Plugins/C3P0/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/c3p0
cp -pr Plugins/DBCP/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/dbcp
cp -pr Plugins/Ehcache/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/ehcache
cp -pr Plugins/Java5/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/java5
cp -pr Plugins/OSCache/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/oscache
cp -pr Plugins/Spatial/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/spatial
cp -pr Plugins/SpringFramework/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/spring
cp -pr Plugins/SwarmCache/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/swarmcache
cp -pr Plugins/TangosolCache/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/tangosol

ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%files core
%{_javadir}/%{name}/core*.jar
%{_datadir}/maven2
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/core-%{version}.jar.*
%endif

%files enhancer
%{_javadir}/%{name}/enhancer*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/enhancer-%{version}.jar.*
%endif

%files c3p0
%{_javadir}/%{name}/c3p0*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/c3p0-%{version}.jar.*
%endif

%files dbcp
%{_javadir}/%{name}/dbcp*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/dbcp-%{version}.jar.*
%endif

%files ehcache
%{_javadir}/%{name}/ehcache*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/ehcache-%{version}.jar.*
%endif

%files java5
%{_javadir}/%{name}/java5*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/java5-%{version}.jar.*
%endif

%files maven-plugin
%{_javadir}/%{name}/maven-plugin*.jar

%files maven-faq-plugin
%{_javadir}/%{name}/maven-faq-plugin*.jar

%files oscache
%{_javadir}/%{name}/oscache*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/oscache-%{version}.jar.*
%endif

%files spatial
%{_javadir}/%{name}/spatial*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/spatial-%{version}.jar.*
%endif

%files spring
%{_javadir}/%{name}/spring*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/spring-%{version}.jar.*
%endif

%files swarmcache
%{_javadir}/%{name}/swarmcache*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/swarmcache-%{version}.jar.*
%endif

%files tangosol
%{_javadir}/%{name}/tangosol*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/tangosol-%{version}.jar.*
%endif

%files thirdparty
%{_javadir}/%{name}/thirdparty*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/thirdparty-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt5_2jpp5
- fixed build with moved maven1

* Mon Aug 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt4_2jpp5
- maven1 dependency translaton

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt3_2jpp5
- selected java5 compiler explicitly

* Fri Feb 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt2_2jpp5
- fixed build

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_2jpp5
- converted from JPackage by jppimport script

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

