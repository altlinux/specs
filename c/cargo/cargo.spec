Patch33: cargo-core-1.0-alt-maven3.patch 
BuildRequires: jetty6-servlet-2.5-api
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without maven
#def_with bootstrap
%bcond_with bootstrap

%define gcj_support 0

%define resversion  1.0
%define m2plversion  1.0

Name:           cargo
Version:        1.0
Release:        alt4_3jpp6
Epoch:          0
Summary:        Cargo container wrapper
License:        ASL 2.0
Group:          Development/Java
URL:            http://cargo.codehaus.org/
%if 0
svn -q export http://svn.codehaus.org/cargo/core/tags/cargo-core-1.0 && tar cjf cargo-core-1.0-src.tar.bz2 cargo-core-1.0
svn -q export http://svn.codehaus.org/cargo/extensions/tags/cargo-extensions-1.0 && tar cjf cargo-extensions-1.0-src.tar.bz2 cargo-extensions-1.0
svn -q export http://svn.codehaus.org/cargo/resources/tags/cargo-resources-1.0 && tar cjf cargo-resources-1.0-src.tar.bz2 cargo-resources-1.0
%endif
Source0:        cargo-core-1.0-src.tar.bz2
Source1:        cargo-extensions-1.0-src.tar.bz2
Source2:        cargo-resources-1.0-src.tar.bz2
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
Patch4:         cargo-core-containers-no-jonas.patch
Patch5:         cargo-samples-pom_xml.patch
Patch6:         cargo-core-api-pom_xml.patch
Patch7:         cargo-core-containers-pom_xml.patch
Patch8:         cargo-extensions-no-maven.patch
Patch9:         cargo-extensions-no-maven2-archetypes.patch
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires: ant >= 0:1.6
Requires: apache-commons-codec
Requires: apache-commons-vfs
Requires: javamail
Requires: jdom
Requires: jline
Requires: log4j
Requires: geronimo-j2ee-1.4-apis
Requires: geronimo-j2ee-deployment-1.1-api
Requires: gnu-trove
Requires: servlet_2_3_api
Requires: spring2-all
Requires: xalan-j2
Requires: xerces-j2
Requires: xml-commons-jaxp-1.3-apis
BuildRequires: ant
BuildRequires: bcel
BuildRequires: derby
BuildRequires: geronimo-genesis
BuildRequires: geronimo-ejb-2.1-api
BuildRequires: geronimo-j2ee-deployment-1.1-api
BuildRequires: geronimo-j2ee-1.4-apis
BuildRequires: geronimo-jta-1.0.1B-api
BuildRequires: geronimo-servlet-2.4-api
BuildRequires: gnu-trove
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: jetty6
BuildRequires: jetty6-core
BuildRequires: jmock
BuildRequires: junit
BuildRequires: apache-commons-parent
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-vfs
BuildRequires: jdom
BuildRequires: jline
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-dependency
BuildRequires: maven2-plugin-ear
BuildRequires: maven2-plugin-ejb
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-one
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-war
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-release
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: modello >= 0:1.0-0.a17
BuildRequires: modello-maven-plugin >= 0:1.0-0.a17
BuildRequires: plexus-container-default
BuildRequires: plexus-utils
BuildRequires: servlet_2_3_api
BuildRequires: spring2-all
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: xmlunit
BuildRequires: xpp3-minimal
BuildRequires: saxpath
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
Cargo is a thin wrapper around existing containers (e.g. J2EE 
containers). It provides different APIs to easily manipulate 
containers.
Cargo provides the following APIs:
* A Java API to start/stop/configure Java Containers and deploy 
  modules into them. We also offer Ant tasks, Maven 1, Maven 2, 
  Intellij IDEA and Netbeans plugins.
* A Java API to parse/create/merge J2EE Modules

%package maven-plugin
Summary:        Cargo Maven Plugin
Group:          Development/Java
Requires: maven >= 0:1.1
Requires: %{name} = %{epoch}:%{version}-%{release}

%description maven-plugin
%{summary}.

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
%setup -q -T -D -a 1
%setup -q -T -D -a 2
cp -p %{SOURCE7} LICENSE
perl -pi -e 's/\r$//g' LICENSE
mv cargo-core-%{version} core
mv cargo-extensions-%{version} extensions
mv cargo-resources-%{version} resources
# remove all binary libs
for j in $(find . -name "*.jar" | grep -v test/resources); do
    mv $j $j.no
done

cp -p %{SOURCE3} pom.xml
mkdir -p pom
cp -p %{SOURCE4} pom/pom.xml
mkdir -p .m2/repository/org/codehaus/cargo/cargo-parent/2/
cp -p %{SOURCE4} \
    .m2/repository/org/codehaus/cargo/cargo-parent/2/cargo-parent-2.pom
mkdir -p .m2/repository/org/codehaus/cargo/cargo-parent/4.1/
cp -p %{SOURCE4} \
    .m2/repository/org/codehaus/cargo/cargo-parent/4.1/cargo-parent-4.1.pom
cp -p %{SOURCE5} settings.xml

%if %without maven
%setup -q -T -D -a 8
%patch1 -b .sav1
%endif
%patch0 -b .sav0
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5
%patch6 -b .sav6
%patch7 -b .sav7
%patch8 -b .sav8
#%patch9 -b .sav9

%if %with maven
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP
%endif

%patch33

%build
export LANG=en_US.ISO8859-1
export MAVEN_OPTS="-Xmx256m"
%if %with maven
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}
export SETTINGS=$(pwd)/settings.xml
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $SETTINGS \
        -Dcargo.containers= \
        -Dcargo.core.version=%{version} \
        -Dmaven2.jpp.depmap.file=%{SOURCE6} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven.test.failure.ignore=true \
        install javadoc:javadoc
%else
export CLASSPATH=$(build-classpath geronimo-ejb-2.1-api geronimo-servlet-2.4-api junit commons-vfs commons-logging xalan-j2 jmock commons-codec plexus/container-default plexus/utils)
export CLASSPATH=${CLASSPATH}:`pwd`/core/api/util/target/classes:`pwd`/core/api/util/target/test-classes
export CLASSPATH=${CLASSPATH}:`pwd`/core/api/module/target/classes:`pwd`/core/api/module/target/test-classes
export CLASSPATH=${CLASSPATH}:`pwd`/core/api/container/target/classes:`pwd`/core/api/container/target/test-classes
export CLASSPATH=${CLASSPATH}:`pwd`/core/api/generic/target/classes:`pwd`/core/api/generic/target/test-classes
export CLASSPATH=${CLASSPATH}:`pwd`/resources/testdata/simple-ejb/target/classes
for container in geronimo jboss jetty jo jrun orion resin tomcat weblogic; do
export CLASSPATH=${CLASSPATH}:`pwd`/core/containers/${container}/target/classes:`pwd`/core/containers/${container}/target/test-classes
done
export CLASSPATH=${CLASSPATH}:$(echo %{_datadir}/maven2/lib/maven-plugin-api-[0-9]*.jar)::$(echo %{_datadir}/maven2/lib/maven-artifact-[0-9]*.jar):$(echo %{_datadir}/maven2/lib/maven-project-[0-9]*.jar):$(echo %{_datadir}/maven2/lib/maven-model-[0-9]*.jar)
export CLASSPATH=${CLASSPATH}:`pwd`/classes/org/codehaus/cargo/module/webapp
export OPT_JAR_LIST=`cat %{_sysconfdir}/ant.d/junit`
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dcargo.containers= -Dcargo.core.version=%{version} -Dmaven.junit.fork=true -Dmaven.test.skip=true -Dbuild.sysclasspath=first -Dmaven.mode.offline=true -Dmaven.repo.local=$MAVEN_REPO_LOCAL package javadoc
%if %with bootstrap
pushd core/uberjar
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $SETTINGS \
        -Dcargo.core.version=%{version} \
        -Dmaven2.jpp.mode=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE6} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        assembly:assembly
popd
%endif
%endif

%install

# jars
mkdir -p %{buildroot}%{_javadir}/%{name}

cp -p \
   core/api/container/target/cargo-core-api-container-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-core-api-container-%{version}.jar
cp -p \
   core/api/generic/target/cargo-core-api-generic-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-core-api-generic-%{version}.jar
cp -p \
   core/api/module/target/cargo-core-api-module-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-core-api-module-%{version}.jar
cp -p \
   core/api/util/target/cargo-core-api-util-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-core-api-util-%{version}.jar
cp -p \
   core/containers/geronimo/target/cargo-core-container-geronimo-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-core-container-geronimo-%{version}.jar
cp -p \
   core/containers/jboss/target/cargo-core-container-jboss-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-core-container-jboss-%{version}.jar
cp -p \
   core/containers/jetty/target/cargo-core-container-jetty-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-core-container-jetty-%{version}.jar
cp -p \
   core/containers/jo/target/cargo-core-container-jo-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-core-container-jo-%{version}.jar
cp -p \
   core/containers/jrun/target/cargo-core-container-jrun-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-core-container-jrun-%{version}.jar
cp -p \
   core/containers/orion/target/cargo-core-container-orion-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-core-container-orion-%{version}.jar
cp -p \
   core/containers/resin/target/cargo-core-container-resin-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-core-container-resin-%{version}.jar
cp -p \
   core/containers/tomcat/target/cargo-core-container-tomcat-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-core-container-tomcat-%{version}.jar
cp -p \
   core/containers/weblogic/target/cargo-core-container-weblogic-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-core-container-weblogic-%{version}.jar
cp -p \
   core/documentation/target/cargo-documentation-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-documentation-%{version}.jar
cp -p \
   core/samples/java/target/cargo-sample-java-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-sample-java-%{version}.jar
cp -p \
   core/uberjar/target/cargo-core-uberjar-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-core-uberjar-%{version}.jar
cp -p \
   extensions/ant/target/cargo-ant-%{version}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-ant-%{version}.jar
cp -p \
   resources/build-tools/target/cargo-build-tools-%{resversion}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-build-tools-%{resversion}.jar

%if %with maven
cp -p extensions/maven2/plugin/target/cargo-maven2-plugin-%{m2plversion}.jar \
   %{buildroot}%{_javadir}/%{name}/%{name}-maven2-plugin-%{m2plversion}.jar
%endif

# create unversioned symlinks
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{m2plversion}.jar; do ln -sf ${jar} ${jar/-%{m2plversion}/}; done)
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{resversion}.jar; do ln -sf ${jar} ${jar/-%{resversion}/}; done)
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} ${jar/-%{version}/}; done)

%if %with maven
%if 0
mkdir -p %{buildroot}%{_datadir}/maven/plugins
cp -p extensions/maven/plugin/target/cargo-maven-plugin-%{version}.jar \
 %{buildroot}%{_datadir}/maven/plugins/maven-%{name}-plugin-%{version}.jar
mkdir -p %{buildroot}%{_javadir}/maven-plugins
pushd %{buildroot}%{_javadir}/maven-plugins
ln -sf %{_datadir}/maven/plugins/maven-%{name}-plugin-%{version}.jar \
        maven-%{name}-plugin.jar
popd
%endif
%endif

# poms
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p core/api/container/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-api-container.pom
cp -p core/api/generic/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-api-generic.pom
cp -p core/api/module/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-api-module.pom
cp -p core/api/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-api.pom
cp -p core/api/util/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-api-util.pom
cp -p core/containers/geronimo/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-container-geronimo.pom
cp -p core/containers/jboss/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-container-jboss.pom
cp -p core/containers/jetty/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-container-jetty.pom
cp -p core/containers/jo/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-container-jo.pom
cp -p core/containers/jrun/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-container-jrun.pom
cp -p core/containers/orion/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-container-orion.pom
cp -p core/containers/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-containers.pom
cp -p core/containers/resin/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-container-resin.pom
cp -p core/containers/tomcat/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-container-tomcat.pom
cp -p core/containers/weblogic/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-container-weblogic.pom
cp -p core/documentation/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-documentation.pom
cp -p core/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core.pom
cp -p core/samples/java/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-samples-java.pom
cp -p core/samples/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-samples.pom
cp -p core/uberjar/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-core-uberjar.pom
cp -p extensions/ant/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-ant.pom
cp -p extensions/maven2/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-maven2-plugin.pom
cp -p extensions/maven/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-maven-plugin.pom
cp -p extensions/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-extensions.pom
cp -p pom/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-parent.pom
cp -p pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-trunks.pom
cp -p resources/build-tools/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-build-tools.pom
cp -p resources/pom.xml \
   %{buildroot}%{_datadir}/maven2/poms/JPP.cargo-cargo-resources.pom

# depmap frags
%add_to_maven_depmap org.codehaus.cargo cargo-core-api-container %{version} JPP/cargo cargo-core-api-container
%add_to_maven_depmap org.codehaus.cargo cargo-core-api-generic %{version} JPP/cargo cargo-core-api-generic
%add_to_maven_depmap org.codehaus.cargo cargo-core-api-module %{version} JPP/cargo cargo-core-api-module
%add_to_maven_depmap org.codehaus.cargo cargo-core-api %{version} JPP/cargo cargo-core-api
%add_to_maven_depmap org.codehaus.cargo cargo-core-api-util %{version} JPP/cargo cargo-core-api-util
%add_to_maven_depmap org.codehaus.cargo cargo-core-container-geronimo %{version} JPP/cargo cargo-core-container-geronimo
%add_to_maven_depmap org.codehaus.cargo cargo-core-container-jboss %{version} JPP/cargo cargo-core-container-jboss
%add_to_maven_depmap org.codehaus.cargo cargo-core-container-jetty %{version} JPP/cargo cargo-core-container-jetty
%add_to_maven_depmap org.codehaus.cargo cargo-core-container-jo %{version} JPP/cargo cargo-core-container-jo
%add_to_maven_depmap org.codehaus.cargo cargo-core-container-jrun %{version} JPP/cargo cargo-core-container-jrun
%add_to_maven_depmap org.codehaus.cargo cargo-core-container-orion %{version} JPP/cargo cargo-core-container-orion
%add_to_maven_depmap org.codehaus.cargo cargo-core-containers %{version} JPP/cargo cargo-core-containers
%add_to_maven_depmap org.codehaus.cargo cargo-core-container-resin %{version} JPP/cargo cargo-core-container-resin
%add_to_maven_depmap org.codehaus.cargo cargo-core-container-tomcat %{version} JPP/cargo cargo-core-container-tomcat
%add_to_maven_depmap org.codehaus.cargo cargo-core-container-weblogic %{version} JPP/cargo cargo-core-container-weblogic
%add_to_maven_depmap org.codehaus.cargo cargo-core-documentation %{version} JPP/cargo cargo-core-documentation
%add_to_maven_depmap org.codehaus.cargo cargo-core %{version} JPP/cargo cargo-core
%add_to_maven_depmap org.codehaus.cargo cargo-core-samples-java %{version} JPP/cargo cargo-core-samples-java
%add_to_maven_depmap org.codehaus.cargo cargo-core-samples %{version} JPP/cargo cargo-core-samples
%add_to_maven_depmap org.codehaus.cargo cargo-core-uberjar %{version} JPP/cargo cargo-core-uberjar
%add_to_maven_depmap org.codehaus.cargo cargo-ant %{version} JPP/cargo cargo-ant
%add_to_maven_depmap org.codehaus.cargo cargo-maven2-plugin %{m2plversion} JPP/cargo cargo-maven2-plugin
%add_to_maven_depmap org.codehaus.cargo cargo-maven-plugin %{version} JPP/cargo cargo-maven-plugin
%add_to_maven_depmap org.codehaus.cargo cargo-extensions %{version} JPP/cargo cargo-extensions
%add_to_maven_depmap org.codehaus.cargo cargo-parent %{version} JPP/cargo cargo-parent
%add_to_maven_depmap org.codehaus.cargo cargo-trunks %{version} JPP/cargo cargo-trunks
%add_to_maven_depmap org.codehaus.cargo cargo-build-tools %{resversion} JPP/cargo cargo-build-tools
%add_to_maven_depmap org.codehaus.cargo cargo-resources %{resversion} JPP/cargo cargo-resources

# javadocs
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/core
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/core/api
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/core/api/container
cp -pr core/api/container/target/site/apidocs/* \
   %{buildroot}%{_javadocdir}/%{name}-%{version}/core/api/container
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/core/api/generic
cp -pr core/api/generic/target/site/apidocs/* \
   %{buildroot}%{_javadocdir}/%{name}-%{version}/core/api/generic
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/core/api/module
cp -pr core/api/module/target/site/apidocs/* \
   %{buildroot}%{_javadocdir}/%{name}-%{version}/core/api/module
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/core/api/util
cp -pr core/api/util/target/site/apidocs/* \
   %{buildroot}%{_javadocdir}/%{name}-%{version}/core/api/util
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/core/containers/geronimo
cp -pr core/containers/geronimo/target/site/apidocs/* \
   %{buildroot}%{_javadocdir}/%{name}-%{version}/core/containers/geronimo
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/core/containers/jboss
cp -pr core/containers/jboss/target/site/apidocs/* \
   %{buildroot}%{_javadocdir}/%{name}-%{version}/core/containers/jboss
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/core/containers/jetty
cp -pr core/containers/jetty/target/site/apidocs/* \
   %{buildroot}%{_javadocdir}/%{name}-%{version}/core/containers/jetty
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/core/containers/jo
cp -pr core/containers/jo/target/site/apidocs/* \
   %{buildroot}%{_javadocdir}/%{name}-%{version}/core/containers/jo
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/core/containers/jrun
cp -pr core/containers/jrun/target/site/apidocs/* \
   %{buildroot}%{_javadocdir}/%{name}-%{version}/core/containers/jrun
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/core/containers/orion
cp -pr core/containers/orion/target/site/apidocs/* \
   %{buildroot}%{_javadocdir}/%{name}-%{version}/core/containers/orion
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/core/containers/resin
cp -pr core/containers/resin/target/site/apidocs/* \
   %{buildroot}%{_javadocdir}/%{name}-%{version}/core/containers/resin
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/core/containers/tomcat
cp -pr core/containers/tomcat/target/site/apidocs/* \
   %{buildroot}%{_javadocdir}/%{name}-%{version}/core/containers/tomcat
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/core/containers/weblogic
cp -pr core/containers/weblogic/target/site/apidocs/* \
   %{buildroot}%{_javadocdir}/%{name}-%{version}/core/containers/weblogic
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/core/documentation
cp -pr core/documentation/target/site/apidocs/* \
   %{buildroot}%{_javadocdir}/%{name}-%{version}/core/documentation
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/core/samples
cp -pr core/samples/java/target/site/apidocs/* \
   %{buildroot}%{_javadocdir}/%{name}-%{version}/core/samples
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/extensions/ant
cp -pr extensions/ant/target/site/apidocs/* \
   %{buildroot}%{_javadocdir}/%{name}-%{version}/extensions/ant
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}/extensions/maven2
%if %with maven
cp -pr extensions/maven2/plugin/target/site/apidocs/* \
   %{buildroot}%{_javadocdir}/%{name}-%{version}/extensions/maven2
%endif

ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

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

%if %with maven
%if 0
%files maven-plugin
%{_datadir}/maven/plugins/maven-%{name}-plugin*.jar
%{_javadir}/maven-plugins/maven-%{name}-plugin.jar
%endif

%files maven2-plugin
%{_javadir}/%{name}/%{name}-maven2-plugin*.jar
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_3jpp6
- fixed build with maven3

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_3jpp6
- new jpp release

* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp6
- fixed build

* Wed Nov 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_2jpp6
- added BR: jetty6-servlet-2.5-api

* Thu Oct 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp6
- new version

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

