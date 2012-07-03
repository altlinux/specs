Patch34: cargo-core-0.9-alt-maven3.patch
BuildRequires: maven-dependency-plugin maven-ear-plugin
%define oldname cargo
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: checkstyle4-optional jakarta-commons-vfs maven-shared maven-shared-file-management
BuildRequires: geronimo-specs-poms
BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without          maven
%bcond_with             maven1
%bcond_without          bootstrap

%define gcj_support 0

%define resversion  0.9.1
%define m2plversion  0.3-SNAPSHOT

Name:           cargo0
Version:        0.9
Release:        alt9_5jpp5
Epoch:          0
Summary:        Cargo container wrapper
License:        ASL 2.0
Group:          Development/Java
URL:            http://cargo.codehaus.org/
# svn export http://svn.codehaus.org/cargo/core/tags/cargo-core-0.9
Source0:        cargo-core-0.9-src.tar.bz2
# svn export http://svn.codehaus.org/cargo/extensions/tags/cargo-extensions-0.9
Source1:        cargo-extensions-0.9-src.tar.bz2
# svn export http://svn.codehaus.org/cargo/resources/tags/cargo-resources-0.9.1
Source2:        cargo-resources-0.9.1-src.tar.bz2
Source3:        cargo-trunks-1.pom
Source4:        cargo-parent-2.pom
Source5:        cargo-settings.xml
Source6:        cargo-jpp-depmap.xml
Source7:        cargo.license
Source8:        cargo-ant-build-set.tar.bz2
Patch0:         cargo-core-pom_xml.patch
Patch1:         cargo-core-uberjar-pom_xml.patch
Patch2:         cargo-extensions-ant-pom_xml.patch
Patch3:         cargo-extensions-maven-pom_xml.patch
Patch4:         cargo-extensions-maven2-pom_xml.patch
Patch5:         cargo-samples-pom_xml.patch
Patch6:         cargo-core-api-pom_xml.patch
Patch7:         cargo-core-containers-pom_xml.patch
Patch8:         cargo-extensions-maven2-missing-uber-war.patch
%if %with bootstrap
BuildRequires: cargo
%endif
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-ear
BuildRequires: maven2-plugin-ejb
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-one
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-war
BuildRequires: maven-release
BuildRequires: maven-surefire-plugin
BuildRequires: modello-maven-plugin >= 0:1.0-0.a17
BuildRequires: plexus-container-default
BuildRequires: plexus-utils
BuildRequires: jetty5
BuildRequires: junit
BuildRequires: jmock
BuildRequires: xmlunit
BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant >= 0:1.6.5
BuildRequires: bcel
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-vfs
BuildRequires: jdom
BuildRequires: jline
BuildRequires: modello >= 0:1.0-0.a17
BuildRequires: geronimo-ejb-2.1-api
BuildRequires: geronimo-j2ee-deployment-1.1-api
BuildRequires: geronimo-j2ee-1.4-apis
BuildRequires: geronimo-jta-1.0.1B-api
BuildRequires: geronimo-servlet-2.4-api
BuildRequires: gnu-trove
BuildRequires: saxpath
BuildRequires: servlet_2_3_api
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: xpp3-minimal
Requires: ant >= 0:1.6
Requires: jakarta-commons-codec
Requires: jakarta-commons-vfs
Requires: jdom
Requires: jline
Requires: geronimo-j2ee-deployment-1.1-api
Requires: geronimo-j2ee-1.4-apis
Requires: gnu-trove
Requires: xalan-j2
Requires: xerces-j2
Requires: javamail
Requires: log4j
Requires: servlet_2_3_api
Requires: xml-commons-jaxp-1.3-apis
Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Patch33: cargo-0.9-alt-pom-add-ant-launcher-dependency.patch

%description
Cargo is a thin wrapper around existing containers (e.g. J2EE 
containers). It provides different APIs to easily manipulate 
containers.
Cargo provides the following APIs:
* A Java API to start/stop/configure Java Containers and deploy 
  modules into them. We also offer Ant tasks, Maven 1, Maven 2, 
  Intellij IDEA and Netbeans plugins.
* A Java API to parse/create/merge J2EE Modules

%if 0
%package maven1-plugin
Summary:        Cargo Maven Plugin
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: %{name} = %{epoch}:%{version}-%{release}

%description maven1-plugin
%{summary}.
%endif

%package maven2-plugin
Summary:        Cargo Maven2 Plugin
Group:          Development/Java
Requires: maven2 >= 0:2.0.7
Requires: %{name} = %{epoch}:%{version}-%{release}

%description maven2-plugin
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -c
%if 0
gzip -dc %{SOURCE1} | tar -xf -
gzip -dc %{SOURCE2} | tar -xf -
%endif
%setup -q -T -D -a 1
%setup -q -T -D -a 2
cp -p %{SOURCE7} LICENSE
perl -pi -e 's/\r$//g' LICENSE
mv cargo-core-0.9 core
mv cargo-extensions-0.9 extensions
mv cargo-resources-0.9.1 resources
# remove all binary libs
for j in $(find . -name "*.jar" | grep -v test/resources); do
    mv $j $j.no
done
cp -p %{SOURCE3} pom.xml
mkdir -p pom
cp -p %{SOURCE4} pom/pom.xml
mkdir -p .m2/repository/JPP/maven2/default_poms/
cp -p %{SOURCE4} \
    .m2/repository/JPP/maven2/default_poms/org.codehaus.cargo-cargo-parent.pom
cp -p %{SOURCE5} settings.xml
%if %without maven
%setup -q -T -D -a 8
%patch1 -p0
%endif

%patch0 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p1
%patch33 -p1
%patch34

rm ./core/api/generic/src/test/java/org/codehaus/cargo/generic/deployable/DefaultDeployableFactoryTest.java
find ./core/samples/java/src/test/java -name '*.java' -delete


%build
export LANG=en_US.ISO8859-1

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export SETTINGS=$(pwd)/settings.xml

%if %with maven

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        -Dmaven2.jpp.mode=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install:install-file -DgroupId=xpp3 -DartifactId=xpp3_min \
        -Dversion=1.1.4c -Dpackaging=jar -Dfile=$(build-classpath xpp3)

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $SETTINGS \
        -Dcargo.containers= \
        -Dcargo.core.version=0.9 \
        -Dmaven2.jpp.mode=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE6} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc
%else
export CLASSPATH=$(build-classpath geronimo-ejb-2.1-api geronimo-servlet-2.4-api junit commons-vfs commons-logging xalan-j2 jmock commons-codec plexus/container-default plexus/utils)
export CLASSPATH=${CLASSPATH}:`pwd`/core/api/util/target/classes:`pwd`/core/api/util/target/test-classes
export CLASSPATH=${CLASSPATH}:`pwd`/core/api/module/target/classes:`pwd`/core/api/module/target/test-classes
export CLASSPATH=${CLASSPATH}:`pwd`/core/api/container/target/classes:`pwd`/core/api/container/target/test-classes
export CLASSPATH=${CLASSPATH}:`pwd`/core/api/generic/target/classes:`pwd`/core/api/generic/target/test-classes
export CLASSPATH=${CLASSPATH}:`pwd`/resources/testdata/simple-ejb/target/classes
for container in geronimo jboss jetty jo orion resin tomcat weblogic; do
export CLASSPATH=${CLASSPATH}:`pwd`/core/containers/${container}/target/classes:`pwd`/core/containers/${container}/target/test-classes
done
export CLASSPATH=${CLASSPATH}:$(echo %{_datadir}/maven2/lib/maven-plugin-api-[0-9]*.jar)::$(echo %{_datadir}/maven2/lib/maven-artifact-[0-9]*.jar):$(echo %{_datadir}/maven2/lib/maven-project-[0-9]*.jar):$(echo %{_datadir}/maven2/lib/maven-model-[0-9]*.jar)
export CLASSPATH=${CLASSPATH}:`pwd`/classes/org/codehaus/cargo/module/webapp
export OPT_JAR_LIST="junit ant/ant-junit"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dcargo.containers= -Dcargo.core.version=0.9 -Dmaven.junit.fork=true -Dmaven.test.skip=true -Dbuild.sysclasspath=first -Dmaven.mode.offline=true -Dmaven.repo.local=$MAVEN_REPO_LOCAL package javadoc
%if %with bootstrap
pushd core/uberjar
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $SETTINGS \
        -Dcargo.core.version=0.9 \
        -Dmaven2.jpp.mode=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE6} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        assembly:assembly
popd
%endif
%endif

# Fix for ugly bug in assembly-plugin ?
#mkdir uberdir
#pushd uberdir
#jar xf ../core/uberjar/target/%{oldname}-core-uberjar-%{version}.jar
#mkdir uberdir
#cp -pr cargo*/* uberdir
#pushd uberdir
#jar cf ../../core/uberjar/target/%{oldname}-core-uberjar-%{version}.jar *
#popd
#popd

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

install -m 644 \
   core/api/container/target/%{oldname}-core-api-container-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-core-api-container-%{version}.jar
install -m 644 \
   core/api/generic/target/%{oldname}-core-api-generic-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-core-api-generic-%{version}.jar
install -m 644 \
   core/api/module/target/%{oldname}-core-api-module-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-core-api-module-%{version}.jar
install -m 644 \
   core/api/util/target/%{oldname}-core-api-util-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-core-api-util-%{version}.jar
install -m 644 \
   core/containers/geronimo/target/%{oldname}-core-container-geronimo-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-core-container-geronimo-%{version}.jar
install -m 644 \
   core/containers/jboss/target/%{oldname}-core-container-jboss-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-core-container-jboss-%{version}.jar
install -m 644 \
   core/containers/jetty/target/%{oldname}-core-container-jetty-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-core-container-jetty-%{version}.jar
install -m 644 \
   core/containers/jo/target/%{oldname}-core-container-jo-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-core-container-jo-%{version}.jar
install -m 644 \
   core/containers/orion/target/%{oldname}-core-container-orion-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-core-container-orion-%{version}.jar
install -m 644 \
   core/containers/resin/target/%{oldname}-core-container-resin-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-core-container-resin-%{version}.jar
install -m 644 \
   core/containers/tomcat/target/%{oldname}-core-container-tomcat-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-core-container-tomcat-%{version}.jar
install -m 644 \
   core/containers/weblogic/target/%{oldname}-core-container-weblogic-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-core-container-weblogic-%{version}.jar
install -m 644 \
   core/documentation/target/%{oldname}-documentation-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-documentation-%{version}.jar
install -m 644 \
   core/samples/java/target/%{oldname}-sample-java-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-sample-java-%{version}.jar
%if %with bootstrap
install -m 644 \
   core/uberjar/target/%{oldname}-core-uberjar-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-core-uberjar-%{version}.jar
%endif
install -m 644 \
   extensions/ant/target/%{oldname}-ant-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-ant-%{version}.jar
install -m 644 \
   resources/build-tools/target/%{oldname}-build-tools-%{resversion}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-build-tools-%{resversion}.jar

%if %with maven
install -m 644 extensions/maven2/target/%{oldname}-maven2-plugin-%{m2plversion}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-maven2-plugin-%{m2plversion}.jar
%endif

# create unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{m2plversion}.jar; do ln -sf ${jar} ${jar/-%{m2plversion}/}; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{resversion}.jar; do ln -sf ${jar} ${jar/-%{resversion}/}; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} ${jar/-%{version}/}; done)

%if %with maven
#install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven/plugins
#install -m 644 extensions/maven/target/%{oldname}-maven-plugin-%{version}.jar \
# $RPM_BUILD_ROOT%{_datadir}/maven/plugins/maven-%{name}-plugin-%{version}.jar
#install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/maven-plugins
#pushd $RPM_BUILD_ROOT%{_javadir}/maven-plugins
#ln -sf %{_datadir}/maven/plugins/maven-%{name}-plugin-%{version}.jar \
#        maven-%{name}-plugin.jar
#popd
%endif

# poms 

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 core/api/container/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core-api-container.pom
install -m 644 core/api/generic/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core-api-generic.pom
install -m 644 core/api/module/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core-api-module.pom
install -m 644 core/api/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core-api.pom
install -m 644 core/api/util/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core-api-util.pom
install -m 644 core/containers/geronimo/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core-container-geronimo.pom
install -m 644 core/containers/jboss/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core-container-jboss.pom
install -m 644 core/containers/jetty/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core-container-jetty.pom
install -m 644 core/containers/jo/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core-container-jo.pom
install -m 644 core/containers/orion/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core-container-orion.pom
install -m 644 core/containers/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core-containers.pom
install -m 644 core/containers/resin/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core-container-resin.pom
install -m 644 core/containers/tomcat/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core-container-tomcat.pom
install -m 644 core/containers/weblogic/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core-container-weblogic.pom
install -m 644 core/documentation/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core-documentation.pom
install -m 644 core/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core.pom
install -m 644 core/samples/java/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core-samples-java.pom
install -m 644 core/samples/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core-samples.pom
install -m 644 core/uberjar/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-core-uberjar.pom
install -m 644 extensions/ant/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-ant.pom
install -m 644 extensions/maven2/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-maven2-plugin.pom
install -m 644 extensions/maven/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-maven-plugin.pom
install -m 644 extensions/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-extensions.pom
install -m 644 pom/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-parent.pom
install -m 644 pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-trunks.pom
install -m 644 resources/build-tools/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-build-tools.pom
install -m 644 resources/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.cargo0-cargo0-resources.pom

# depmap frags
%add_to_maven_depmap org.codehaus.cargo cargo-core-api-container %{version} JPP/cargo0 cargo0-core-api-container
%add_to_maven_depmap org.codehaus.cargo cargo-core-api-generic %{version} JPP/cargo0 cargo0-core-api-generic
%add_to_maven_depmap org.codehaus.cargo cargo-core-api-module %{version} JPP/cargo0 cargo0-core-api-module
%add_to_maven_depmap org.codehaus.cargo cargo-core-api %{version} JPP/cargo0 cargo0-core-api
%add_to_maven_depmap org.codehaus.cargo cargo-core-api-util %{version} JPP/cargo0 cargo0-core-api-util
%add_to_maven_depmap org.codehaus.cargo cargo-core-container-geronimo %{version} JPP/cargo0 cargo0-core-container-geronimo
%add_to_maven_depmap org.codehaus.cargo cargo-core-container-jboss %{version} JPP/cargo0 cargo0-core-container-jboss
%add_to_maven_depmap org.codehaus.cargo cargo-core-container-jetty %{version} JPP/cargo0 cargo0-core-container-jetty
%add_to_maven_depmap org.codehaus.cargo cargo-core-container-jo %{version} JPP/cargo0 cargo0-core-container-jo
%add_to_maven_depmap org.codehaus.cargo cargo-core-container-orion %{version} JPP/cargo0 cargo0-core-container-orion
%add_to_maven_depmap org.codehaus.cargo cargo-core-containers %{version} JPP/cargo0 cargo0-core-containers
%add_to_maven_depmap org.codehaus.cargo cargo-core-container-resin %{version} JPP/cargo0 cargo0-core-container-resin
%add_to_maven_depmap org.codehaus.cargo cargo-core-container-tomcat %{version} JPP/cargo0 cargo0-core-container-tomcat
%add_to_maven_depmap org.codehaus.cargo cargo-core-container-weblogic %{version} JPP/cargo0 cargo0-core-container-weblogic
%add_to_maven_depmap org.codehaus.cargo cargo-core-documentation %{version} JPP/cargo0 cargo0-core-documentation
%add_to_maven_depmap org.codehaus.cargo cargo-core %{version} JPP/cargo0 cargo0-core
%add_to_maven_depmap org.codehaus.cargo cargo-core-samples-java %{version} JPP/cargo0 cargo0-core-samples-java
%add_to_maven_depmap org.codehaus.cargo cargo-core-samples %{version} JPP/cargo0 cargo0-core-samples
%add_to_maven_depmap org.codehaus.cargo cargo-core-uberjar %{version} JPP/cargo0 cargo0-core-uberjar
%add_to_maven_depmap org.codehaus.cargo cargo-ant %{version} JPP/cargo0 cargo0-ant
%add_to_maven_depmap org.codehaus.cargo cargo-maven2-plugin %{m2plversion} JPP/cargo0 cargo0-maven2-plugin
%add_to_maven_depmap org.codehaus.cargo cargo-maven-plugin %{version} JPP/cargo0 cargo0-maven-plugin
%add_to_maven_depmap org.codehaus.cargo cargo-extensions %{version} JPP/cargo0 cargo0-extensions
%add_to_maven_depmap org.codehaus.cargo cargo-parent %{version} JPP/cargo0 cargo0-parent
%add_to_maven_depmap org.codehaus.cargo cargo-trunks %{version} JPP/cargo0 cargo0-trunks
%add_to_maven_depmap org.codehaus.cargo cargo-build-tools %{resversion} JPP/cargo0 cargo0-build-tools
%add_to_maven_depmap org.codehaus.cargo cargo-resources %{resversion} JPP/cargo0 cargo0-resources

#javadocs

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/api
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/api/container
cp -pr core/api/container/target/site/apidocs/* \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/api/container
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/api/generic
cp -pr core/api/generic/target/site/apidocs/* \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/api/generic
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/api/module
cp -pr core/api/module/target/site/apidocs/* \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/api/module
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/api/util
cp -pr core/api/util/target/site/apidocs/* \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/api/util
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/containers/geronimo
cp -pr core/containers/geronimo/target/site/apidocs/* \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/containers/geronimo
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/containers/jboss
cp -pr core/containers/jboss/target/site/apidocs/* \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/containers/jboss
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/containers/jetty
cp -pr core/containers/jetty/target/site/apidocs/* \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/containers/jetty
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/containers/jo
cp -pr core/containers/jo/target/site/apidocs/* \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/containers/jo
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/containers/orion
cp -pr core/containers/orion/target/site/apidocs/* \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/containers/orion
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/containers/resin
cp -pr core/containers/resin/target/site/apidocs/* \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/containers/resin
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/containers/tomcat
cp -pr core/containers/tomcat/target/site/apidocs/* \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/containers/tomcat
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/containers/weblogic
cp -pr core/containers/weblogic/target/site/apidocs/* \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/containers/weblogic
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/documentation
cp -pr core/documentation/target/site/apidocs/* \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/documentation
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/samples
cp -pr core/samples/java/target/site/apidocs/* \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/core/samples
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/extensions/ant
cp -pr extensions/ant/target/site/apidocs/* \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/extensions/ant
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/extensions/maven2
%if %with maven
cp -pr extensions/maven2/target/site/apidocs/* \
   $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/extensions/maven2
%endif

ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files 
%doc LICENSE
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-core*.jar
%{_javadir}/%{name}/%{name}-documentation*.jar
%{_javadir}/%{name}/%{name}-sample-java*.jar
%{_javadir}/%{name}/%{name}-ant*.jar
%{_javadir}/%{name}/%{name}-build-tools*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-*.jar.*
%endif

%if %with maven1
%files maven1-plugin
%{_datadir}/maven/plugins/maven-%{name}-plugin*.jar
%{_javadir}/maven-plugins/maven-%{name}-plugin.jar
%endif

%if %with maven
%files maven2-plugin
%{_javadir}/%{name}/%{name}-maven2-plugin*.jar
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt9_5jpp5
- fixed build with maven3

* Mon Aug 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt8_5jpp5
- dropped maven1 plugin

* Sun Aug 28 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt7_5jpp5
- renamed maven1 plugin

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt6_5jpp5
- fixed modello plugin dependency

* Mon Nov 01 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt5_5jpp5
- fixed pom names 

* Thu Oct 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt4_5jpp5
- compat build for jakarta cactus 1.7

* Fri Mar 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt3_5jpp5
- build with checkstyle4

* Thu Apr 02 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt2_5jpp5
- new jpp release

* Mon Mar 02 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt2_4jpp5
- fixed uberjar

* Tue Feb 17 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt1_4jpp5
- fixed build after maven 2.0.7

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt1_2jpp5
- converted from JPackage by jppimport script

* Sat Nov 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt1_1jpp1.7
- converted from JPackage by jppimport script

