BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define gcj_support 0

# If you don't want to build with maven, and use straight ant instead,
# give rpmbuild option '--without maven'

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}

# If you want to build with the TCKs
# give rpmbuild option '--with tck'

%define with_tck %{?_with_tck:1}%{!?_with_tck:0}
%define without_tck %{!?_with_tck:1}%{?_with_tck:0}



# To make the tarball:
# svn export -r 414701 http://svn.apache.org/repos/asf/db/jdo/trunk apache-jdo

Name:           apache-jdo
Summary:        Apache JDO specification.
Version:        2.0
Release:        alt6_5jpp6
Epoch:          0
URL:            http://db.apache.org/jdo
License:        Apache License, Version 2.0
Group:          Development/Java
Source:         %{name}-%{version}-src.tar.bz2
Source1:        maven2jpp-mapdeps.xsl
Source2:        apache-jdo-jpp-depmap.xml
Source3:        netbeans-btree.tar.gz
Source4:        apache-jdo-api11-build.xml
Source5:        apache-jdo-api20-build.xml
Source6:        apache-jdo-btree-build.xml
Source7:        apache-jdo-core20-build.xml
Source8:        apache-jdo-enhancer20-build.xml
Source9:        apache-jdo-fostore20-build.xml
Source10:       apache-jdo-query20-build.xml
Source11:       apache-jdo-ri11-build.xml
Source12:       apache-jdo-runtime20-build.xml
Source13:       apache-jdo-tck11-build.xml
Source14:       apache-jdo-tck20-build.xml
Source15:       apache-jdo-fostore20-build.properties
Source16:       apache-jdo-ri11-build.properties
Source17:       jdo2-api-2.0.pom
Source18:       jdo2-core-2.0.pom
Source19:       jdo2-enhancer-2.0.pom


Patch0:         apache-jdo-tck11-project_xml.patch
Patch1:         apache-jdo-ri11-maven_xml.patch
Patch2:         apache-jdo-fostore20-project_properties.patch
Patch3:         apache-jdo-ri11-project_properties.patch
Patch4:         apache-jdo-tck11-project_properties.patch
Patch5:         apache-jdo-tck20-project_properties.patch
Patch6:         apache-jdo-enhancer20-project_properties.patch
Patch7:         apache-jdo-btree-maven_xml.patch
Patch8:         apache-jdo-fostore20-maven_xml.patch
BuildRequires:  jpackage-utils >= 0:1.7.5
%if %{with_maven}
BuildRequires:  maven1 >= 1.1
BuildRequires:  maven1-plugins-base
BuildRequires:  maven1-plugin-license
BuildRequires:  maven1-plugin-multiproject
BuildRequires:  maven1-plugin-test
BuildRequires:  maven1-plugin-xdoc
BuildRequires:  saxon
BuildRequires:  saxon-scripts
%endif
BuildRequires:  junit
BuildRequires:  antlr
BuildRequires:  apache-commons-logging
BuildRequires:  geronimo-jta-1.0.1B-api
#BuildRequires:  xerces-j2 >= 2.7.1
#BuildRequires:  xml-commons-apis
%if %{with_tck}
BuildRequires:  spring-beans
BuildRequires:  spring-core
BuildRequires:  jpox-core
BuildRequires:  jpox-enhancer
BuildRequires:  jpox-c3p0
BuildRequires:  jpox-dbcp
%endif
%if %{gcj_support}
BuildRequires:  gnu-crypto
BuildRequires:          java-gcj-compat-devel
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Source44: import.info


%description
Java Data Objects (JDO) is a standard way to access persistent data 
in databases, using plain old Java objects (POJO) to represent 
persistent data.

%package 1.1-api
Group:          Development/Java
Summary:        JDO 1.1 API.
Requires:       jta_1_0_1B_api
Provides:       jdo = 0:1.1
Provides:       jdo11
Obsoletes:      jdo
%if %{gcj_support}
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif

%description 1.1-api
The standard definition of the JDO 1.1 API as originally 
defined by the JSR-12 standard (JDO 1.0) .

%package 1.1-api-javadoc
Group:          Development/Documentation
Summary:        Javadoc for JDO 1.1 api.

%description 1.1-api-javadoc
Javadoc for JDO 1.1 api.

%package 1.1-impl
Group:          Development/Java
Summary:        JDO 1.1 Implementation
Requires:       antlr
Requires:       %{name}-1.1-api = %{epoch}:%{version}-%{release}
Requires:       %{name}-btree = %{epoch}:%{version}-%{release}
Requires:       jakarta-commons-logging
Requires:       jta_1_0_1B_api
Requires:       xml-commons-apis
%if %{gcj_support}
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif

%description 1.1-impl
The reference implementation of the JDO 1.1 API as originally 
defined by the JSR-12 standard (JDO 1.0) .

%package 1.1-impl-javadoc
Group:          Development/Documentation
Summary:        Javadoc for JDO 1.1 implementation.

%description 1.1-impl-javadoc
Javadoc for JDO 1.1 implementation.

%if %{with_tck}
%package 1.1-tck
Group:          Development/Java
Summary:        JDO 1.1 TCK
Requires:       %{name}-1.1-api = %{epoch}:%{version}-%{release}
Requires:       %{name}-1.1-impl = %{epoch}:%{version}-%{release}
Requires:       jakarta-commons-logging
Requires:       junit
Requires:       spring-beans
Requires:       spring-core
%if %{gcj_support}
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif

%description 1.1-tck
The technology compatibility kit for the JDO 1.1 API as originally 
defined by the JSR-12 standard (JDO 1.0) .

%package 1.1-tck-javadoc
Group:          Development/Documentation
Summary:        Javadoc for JDO 1.1 TCK

%description 1.1-tck-javadoc
Javadoc for JDO 1.1 TCK
%endif

%package 2.0-api
Group:          Development/Java
Summary:        JDO 2.0 API.
Requires:       jta_1_0_1B_api
Provides:       jdo = 0:2.0
Provides:       jdo20
%if %{gcj_support}
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif
Requires(post):    jpackage-utils >= 0:1.7.2
Requires(postun):  jpackage-utils >= 0:1.7.2

%description 2.0-api
The standard definition of the JDO 2.0 API as defined by the 
JSR-243 standard.

%package 2.0-api-javadoc
Group:          Development/Documentation
Summary:        Javadoc for JDO 2.0 api.

%description 2.0-api-javadoc
Javadoc for JDO 2.0 api.

%package 2.0-core
Group:          Development/Java
Summary:        JDO 2.0 core implementation.
Requires:       %{name}-2.0-api = %{epoch}:%{version}-%{release}
Requires:       jakarta-commons-logging
Requires:       xml-commons-apis
%if %{gcj_support}
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif
Requires(post):    jpackage-utils >= 0:1.7.2
Requires(postun):  jpackage-utils >= 0:1.7.2

%description 2.0-core
An implementation of the core functionality for the 
JDO 2.0 API as defined by the JSR-243 standard.

%package 2.0-core-javadoc
Group:          Development/Documentation
Summary:        Javadoc for JDO 2.0 core implementation.

%description 2.0-core-javadoc
Javadoc for JDO 2.0 core implementation.

%package 2.0-runtime
Group:          Development/Java
Summary:        JDO 2.0 runtime implementation.
Requires:       %{name}-2.0-api = %{epoch}:%{version}-%{release}
Requires:       %{name}-2.0-core = %{epoch}:%{version}-%{release}
Requires:       jakarta-commons-logging
Requires:       jta_1_0_1B_api
%if %{gcj_support}
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif

%description 2.0-runtime
An implementation of the runtime functionality for the 
JDO 2.0 API as defined by the JSR-243 standard.

%package 2.0-runtime-javadoc
Group:          Development/Documentation
Summary:        Javadoc for JDO 2.0 runtime implementation.

%description 2.0-runtime-javadoc
Javadoc for JDO 2.0 runtime implementation.

%package 2.0-enhancer
Group:          Development/Java
Summary:        JDO 2.0 enhancer implementation.
Requires:       %{name}-2.0-core = %{epoch}:%{version}-%{release}
%if %{gcj_support}
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif
Requires(post):    jpackage-utils >= 0:1.7.2
Requires(postun):  jpackage-utils >= 0:1.7.2

%description 2.0-enhancer
An implementation of the enhancer functionality for the 
JDO 2.0 API as defined by the JSR-243 standard.

%package 2.0-enhancer-javadoc
Group:          Development/Documentation
Summary:        Javadoc for JDO 2.0 enhancer implementation.

%description 2.0-enhancer-javadoc
Javadoc for JDO 2.0 enhancer implementation.

%package 2.0-query
Group:          Development/Java
Summary:        JDO 2.0 query implementation.
Requires:       antlr
Requires:       %{name}-2.0-api = %{epoch}:%{version}-%{release}
Requires:       %{name}-2.0-core = %{epoch}:%{version}-%{release}
Requires:       jakarta-commons-logging
%if %{gcj_support}
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif

%description 2.0-query
An implementation of the query functionality for the 
JDO 2.0 API as defined by the JSR-243 standard.

%package 2.0-query-javadoc
Group:          Development/Documentation
Summary:        Javadoc for JDO 2.0 query implementation.

%description 2.0-query-javadoc
Javadoc for JDO 2.0 query implementation.

%package 2.0-fostore
Group:          Development/Java
Summary:        JDO 2.0 FOStore implementation.
Requires:       %{name}-2.0-api = %{epoch}:%{version}-%{release}
Requires:       %{name}-2.0-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-btree = %{epoch}:%{version}-%{release}
Requires:       jakarta-commons-logging
%if %{gcj_support}
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif

%description 2.0-fostore
An implementation of the FOStore functionality for the 
JDO 2.0 API as defined by the JSR-243 standard.

%package 2.0-fostore-javadoc
Group:          Development/Documentation
Summary:        Javadoc for JDO 2.0 FOStore implementation.

%description 2.0-fostore-javadoc
Javadoc for JDO 2.0 FOStore implementation.

%package btree
Group:          Development/Java
Summary:        Binary Tree for JDO 2.0 FOStore implementation.
%if %{gcj_support}
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif

%description btree
Netbeans mdr btree implementation provided as a library.

%package btree-javadoc
Group:          Development/Documentation
Summary:        Javadoc for JDO 2.0 FOStore binary tree.

%description btree-javadoc
Javadoc for JDO 2.0 FOStore binary tree.

%if %{with_tck}
%package 2.0-tck
Group:          Development/Java
Summary:        JDO 2.0 TCK
%if %{gcj_support}
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif

%description 2.0-tck
The technology compatibility kit for the JDO 2.0 API as 
defined by the JSR-243 standard.

%package 2.0-tck-javadoc
Group:          Development/Documentation
Summary:        Javadoc for JDO 2.0 TCK

%description 2.0-tck-javadoc
Javadoc for JDO 2.0 TCK
%endif

%prep
%setup -q -n %{name}
%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav
%patch4 -b .sav
%patch5 -b .sav
%patch6 -b .sav
%patch7 -b .sav
%patch8 -b .sav
pushd btree
       gzip -dc %{SOURCE3} | tar xf -
popd
%if ! %{with_maven}
cp %{SOURCE4}   api11/build.xml
cp %{SOURCE5}   api20/build.xml
cp %{SOURCE6}   btree/build.xml
cp %{SOURCE7}   core20/build.xml
cp %{SOURCE8}   enhancer20/build.xml
cp %{SOURCE9}   fostore20/build.xml
cp %{SOURCE10}  query20/build.xml
cp %{SOURCE11}  ri11/build.xml
cp %{SOURCE12}  runtime20/build.xml
cp %{SOURCE13}  tck11/build.xml
cp %{SOURCE14}  tck20/build.xml
cp %{SOURCE15}  fostore20/build.properties
cp %{SOURCE16}  ri11/build.properties
%endif

%build

# for PermGen error, running out of memory
export MAVEN_OPTS=-XX:MaxPermSize=512m
    unset CLASSPATH
mkdir -p fostore20/target/test-classes

%if %{with_maven}
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE1} map=%{SOURCE2}
    popd
done
export MAVEN_OPTS="-XX:MaxPermSize=256m"
export MAVEN_HOME_LOCAL=$(pwd)/.maven
%if %{with_tck}
maven -Dmaven.compile.target=1.4 -Dmaven.javadoc.source=1.4  -e \
    -Dmaven.home.local=$MAVEN_HOME_LOCAL \
    -Dmaven.repo.remote=file:/usr/share/maven1/repository \
    -Dgoal=jar:install,javadoc,test:test multiproject:goal
pushd tck11
maven -Dmaven.compile.target=1.4 -Dmaven.javadoc.source=1.4  \
    -Dmaven.home.local=$MAVEN_HOME_LOCAL \
    -Dmaven.repo.remote=file:/usr/share/maven1/repository \
    runtck
popd
%else
maven -Dmaven.compile.target=1.4 -Dmaven.javadoc.source=1.4  \
    -Dmaven.home.local=$MAVEN_HOME_LOCAL \
    -Dmaven.repo.remote=file:/usr/share/maven1/repository \
    -Dmaven.test.failure.ignore=true \
    -Dmaven.multiproject.excludes=tck20/project.xml,tck11/project.xml \
    -Dgoal=jar:install,javadoc,test:test multiproject:goal
%endif
%else
export ANT_OPTS="-XX:MaxPermSize=128m"
pushd api11
export CLASSPATH=$(build-classpath geronimo-jta-1.0.1B-api):target/classes:target/test-classes
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 -Dbuild.sysclasspath=only jar javadoc
popd
pushd btree
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 -Dbuild.sysclasspath=only jar javadoc
popd
pushd ri11
export CLASSPATH=$(build-classpath antlr geronimo-jta-1.0.1B-api):../api11/target/jdo1-api-SNAPSHOT.jar:../btree/target/jdo-btree-1.1.jar:target/classes:target/test-classes:test/conf
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 -Dbuild.sysclasspath=only compile compile-tests
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 -Dbuild.sysclasspath=only jar javadoc
popd
export CLASSPATH=
pushd api20
export CLASSPATH=$(build-classpath geronimo-jta-1.0.1B-api):target/classes:target/test-classes
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 -Dbuild.sysclasspath=only jar javadoc
popd
export CLASSPATH=
pushd core20
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 -Dbuild.sysclasspath=only jar javadoc
popd
export CLASSPATH=
pushd runtime20
rm -rf src/java/org/apache/jdo/impl/model/java/runtime/jdk5
export CLASSPATH=$(build-classpath geronimo-jta-1.0.1B-api):../api20/target/jdo2-api-SNAPSHOT.jar:../core20/target/jdo2-core-SNAPSHOT.jar
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 -Dbuild.sysclasspath=only jar javadoc
popd
export CLASSPATH=
pushd query20
export CLASSPATH=$(build-classpath antlr geronimo-jta-1.0.1B-api):../api20/target/jdo2-api-SNAPSHOT.jar:../core20/target/jdo2-core-SNAPSHOT.jar:../runtime20/target/jdo2-runtime-SNAPSHOT.jar:target/classes:target/test-classes:test/conf
pushd src/java/org/apache/jdo/impl/jdoql/jdoqlc
java antlr.Tool JDOQL.g
java antlr.Tool Semantic.g
java antlr.Tool Optimizer.g
popd
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 -Dbuild.sysclasspath=only jar javadoc
popd
export CLASSPATH=
pushd enhancer20
export CLASSPATH=../api20/target/jdo2-api-SNAPSHOT.jar:../core20/target/jdo2-core-SNAPSHOT.jar:target/classes:target/test-classes
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 -Dbuild.sysclasspath=only jar javadoc
popd
export CLASSPATH=
pushd fostore20
export CLASSPATH=$(build-classpath geronimo-jta-1.0.1B-api):../api20/target/jdo2-api-SNAPSHOT.jar:../btree/target/jdo-btree-1.1.jar:../core20/target/jdo2-core-SNAPSHOT.jar:../runtime20/target/jdo2-runtime-SNAPSHOT.jar:../query20/target/jdo2-query-SNAPSHOT.jar:../enhancer20/target/jdo2-enhancer-SNAPSHOT.jar:target/classes:target/test-classes:test/jdo:test/conf
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 -Dbuild.sysclasspath=only jar javadoc
popd
%endif

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
install -m 644 api11/target/jdo1-api-SNAPSHOT.jar \
    $RPM_BUILD_ROOT%{_javadir}/apache-jdo-1.1-api-%{version}.jar
install -m 644 ri11/target/jdo1-ri-SNAPSHOT.jar \
    $RPM_BUILD_ROOT%{_javadir}/apache-jdo-1.1-impl-%{version}.jar
install -m 644 api20/target/jdo2-api-SNAPSHOT.jar \
    $RPM_BUILD_ROOT%{_javadir}/apache-jdo-2.0-api-%{version}.jar
install -m 644 btree/target/jdo-btree-1.1.jar \
    $RPM_BUILD_ROOT%{_javadir}/apache-jdo-btree-%{version}.jar
install -m 644 core20/target/jdo2-core-SNAPSHOT.jar \
    $RPM_BUILD_ROOT%{_javadir}/apache-jdo-2.0-core-%{version}.jar
install -m 644 enhancer20/target/jdo2-enhancer-SNAPSHOT.jar \
    $RPM_BUILD_ROOT%{_javadir}/apache-jdo-2.0-enhancer-%{version}.jar
install -m 644 fostore20/target/jdo2-fostore-SNAPSHOT.jar \
    $RPM_BUILD_ROOT%{_javadir}/apache-jdo-2.0-fostore-%{version}.jar
install -m 644 query20/target/jdo2-query-SNAPSHOT.jar \
    $RPM_BUILD_ROOT%{_javadir}/apache-jdo-2.0-query-%{version}.jar
install -m 644 runtime20/target/jdo2-runtime-SNAPSHOT.jar \
    $RPM_BUILD_ROOT%{_javadir}/apache-jdo-2.0-runtime-%{version}.jar
%if %{with_tck}
install -m 644 tck11/target/jdo1-tck-SNAPSHOT.jar \
    $RPM_BUILD_ROOT%{_javadir}/apache-jdo-1.1-tck-%{version}.jar
install -m 644 tck20/target/jdo2-tck-SNAPSHOT.jar \
    $RPM_BUILD_ROOT%{_javadir}/apache-jdo-2.0-tck-%{version}.jar
%endif

pushd $RPM_BUILD_ROOT%{_javadir}
for jar in *-%{version}.jar; do
    ln -sf ${jar} `echo $jar| sed "s|-%{version}\.jar|.jar|g"`;
done
ln -sf apache-jdo-1.1-api.jar jdo11.jar
ln -sf apache-jdo-2.0-api.jar jdo20.jar
ln -sf apache-jdo-2.0-api.jar jdo.jar
popd

%add_to_maven_depmap javax.jdo jdo2-api %{version} JPP apache-jdo-2.0-api
%add_to_maven_depmap org.apache.jdo jdo2-core %{version} JPP apache-jdo-2.0-core
%add_to_maven_depmap org.apache.jdo jdo2-enhancer %{version} JPP apache-jdo-2.0-enhancer

# poms
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 0644 %{SOURCE17} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-apache-jdo-2.0-api.pom
install -m 0644 %{SOURCE18} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-apache-jdo-2.0-core.pom
install -m 0644 %{SOURCE19} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-apache-jdo-2.0-enhancer.pom

# Javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-1.1-api
ln -s %{name}-%{version}-1.1-api $RPM_BUILD_ROOT%{_javadocdir}/%{name}-1.1-api
cp -pr api11/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-1.1-api
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-1.1-impl
ln -s %{name}-%{version}-1.1-impl $RPM_BUILD_ROOT%{_javadocdir}/%{name}-1.1-impl
cp -pr ri11/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-1.1-impl
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-2.0-api
ln -s %{name}-%{version}-2.0-api $RPM_BUILD_ROOT%{_javadocdir}/%{name}-2.0-api
cp -pr api20/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-2.0-api
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-2.0-core
ln -s %{name}-%{version}-2.0-core $RPM_BUILD_ROOT%{_javadocdir}/%{name}-2.0-core
cp -pr core20/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-2.0-core
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-2.0-runtime
ln -s %{name}-%{version}-2.0-runtime $RPM_BUILD_ROOT%{_javadocdir}/%{name}-2.0-runtime
cp -pr runtime20/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-2.0-runtime
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-2.0-enhancer
ln -s %{name}-%{version}-2.0-enhancer $RPM_BUILD_ROOT%{_javadocdir}/%{name}-2.0-enhancer
cp -pr enhancer20/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-2.0-enhancer
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-2.0-query
ln -s %{name}-%{version}-2.0-query $RPM_BUILD_ROOT%{_javadocdir}/%{name}-2.0-query
cp -pr query20/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-2.0-query
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-2.0-fostore
ln -s %{name}-%{version}-2.0-fostore $RPM_BUILD_ROOT%{_javadocdir}/%{name}-2.0-fostore
cp -pr fostore20/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-2.0-fostore
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-btree
ln -s %{name}-%{version}-btree $RPM_BUILD_ROOT%{_javadocdir}/%{name}-btree
cp -pr btree/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-btree
%if %{with_tck}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-1.1-tck
ln -s %{name}-%{version}-1.1-tck $RPM_BUILD_ROOT%{_javadocdir}/%{name}-1.1-tck
cp -pr tck11/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-1.1-tck
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-2.0-tck
ln -s %{name}-%{version}-2.0-tck $RPM_BUILD_ROOT%{_javadocdir}/%{name}-2.0-tck
cp -pr tck20/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}-2.0-tck
%endif

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jdo_apache-jdo-1.1-api<<EOF
%{_javadir}/jdo.jar	%{_javadir}/apache-jdo-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jdo11_apache-jdo-1.1-api<<EOF
%{_javadir}/jdo11.jar	%{_javadir}/apache-jdo-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jdo_apache-jdo-2.0-api<<EOF
%{_javadir}/jdo.jar	%{_javadir}/apache-jdo-2.0-api.jar	20000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jdo20_apache-jdo-2.0-api<<EOF
%{_javadir}/jdo20.jar	%{_javadir}/apache-jdo-2.0-api.jar	20000
EOF

%files 1.1-api
%_altdir/jdo11_apache-jdo-1.1-api
%_altdir/jdo_apache-jdo-1.1-api
%{_javadir}/%{name}-1.1-api*.jar
%exclude %{_javadir}/jdo.jar
%exclude %{_javadir}/jdo11.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-1.1-api*.jar.*
%endif

%files 1.1-api-javadoc
%{_javadocdir}/%{name}-%{version}-1.1-api
%doc %{_javadocdir}/%{name}-1.1-api

%files 1.1-impl
%{_javadir}/%{name}-1.1-impl*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-1.1-impl*.jar.*
%endif

%files 1.1-impl-javadoc
%{_javadocdir}/%{name}-%{version}-1.1-impl
%doc %{_javadocdir}/%{name}-1.1-impl

%if %{with_tck}
%files 1.1-tck
%{_javadir}/%{name}-1.1-tck*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-1.1-tck*.jar.*
%endif

%files 1.1-tck-javadoc
%{_javadocdir}/%{name}-%{version}-1.1-tck
%doc %{_javadocdir}/%{name}-1.1-tck
%endif

%files 2.0-api
%_altdir/jdo20_apache-jdo-2.0-api
%_altdir/jdo_apache-jdo-2.0-api
%{_javadir}/%{name}-2.0-api*.jar
%exclude %{_javadir}/jdo.jar
%exclude %{_javadir}/jdo20.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-2.0-api*.jar.*
%endif

%files 2.0-api-javadoc
%{_javadocdir}/%{name}-%{version}-2.0-api
%doc %{_javadocdir}/%{name}-2.0-api

%files 2.0-core
%{_javadir}/%{name}-2.0-core*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-2.0-core*.jar.*
%endif

%files 2.0-core-javadoc
%{_javadocdir}/%{name}-%{version}-2.0-core
%doc %{_javadocdir}/%{name}-2.0-core

%files 2.0-runtime
%{_javadir}/%{name}-2.0-runtime*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-2.0-runtime*.jar.*
%endif

%files 2.0-runtime-javadoc
%{_javadocdir}/%{name}-%{version}-2.0-runtime
%doc %{_javadocdir}/%{name}-2.0-runtime

%files 2.0-enhancer
%{_javadir}/%{name}-2.0-enhancer*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-2.0-enhancer*.jar.*
%endif

%files 2.0-enhancer-javadoc
%{_javadocdir}/%{name}-%{version}-2.0-enhancer
%doc %{_javadocdir}/%{name}-2.0-enhancer

%files 2.0-query
%{_javadir}/%{name}-2.0-query*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-2.0-query*.jar.*
%endif

%files 2.0-query-javadoc
%{_javadocdir}/%{name}-%{version}-2.0-query
%doc %{_javadocdir}/%{name}-2.0-query

%files 2.0-fostore
%{_javadir}/%{name}-2.0-fostore*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-2.0-fostore*.jar.*
%endif

%files 2.0-fostore-javadoc
%{_javadocdir}/%{name}-%{version}-2.0-fostore
%doc %{_javadocdir}/%{name}-2.0-fostore

%files btree
%{_javadir}/%{name}-btree*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-btree*.jar.*
%endif

%files btree-javadoc
%{_javadocdir}/%{name}-%{version}-btree
%doc %{_javadocdir}/%{name}-btree

%if %{with_tck}
%files 2.0-tck
%{_javadir}/%{name}-2.0-tck*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-2.0-tck*.jar.*
%endif

%files 2.0-tck-javadoc
%{_javadocdir}/%{name}-%{version}-2.0-tck
%doc %{_javadocdir}/%{name}-2.0-tck
%endif

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt6_5jpp6
- fixed build with moved maven1

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt5_5jpp6
- new jpp relase

* Fri Sep 16 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt5_4jpp5
- fixed build

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt4_4jpp5
- use maven1

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt3_4jpp5
- alternatives 0.4

* Sun Oct 19 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_4jpp5
- build with java 5

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_3jpp1.7
- updated to new jpackage release

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_2jpp1.7
- converted from JPackage by jppimport script

