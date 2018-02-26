Patch33: portals-pluto-1.2.0-G602095-alt-maven3.patch
BuildRequires: jmock
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat maven-surefire-provider-junit4
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

%define gcj_support 0

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}

%define bname    pluto
%define namedversion 1.2.0-286-SNAPSHOT

Name:           portals-%{bname}12
Version:        1.2.0
Release:        alt4_0.G602095.1jpp5
Epoch:          0
Summary:        Portlet 1.0 Reference Implementation
License:        Apache Software License 2.0
Url:            http://portals.apache.org/pluto/
Group:          Development/Java
Source0:        portals-pluto-1.2.0-G602095.tar.gz
# svn export -r 601061 https://svn.apache.org/repos/asf/portals/pluto/trunk pluto
Source1:        portals-pluto-1.2.0-G602095-settings.xml
Source2:        portals-pluto-1.2.0-G602095-jpp-depmap.xml
Source3:        apache-jar-resource-bundle-1.3.jar
Source4:        http://mirrors.dotsrc.org/maven2/javax/ccpp/ccpp/1.0/ccpp-1.0.jar

Patch0:         portals-pluto-1.2.0-G602095-partial-pom.patch
Patch1:         portals-pluto-1.2.0-G602095-PortletURLProviderImpl.patch
Patch2:         portals-pluto-1.2.0-G602095-PublicRenderParamDD.patch
Patch3:         portals-pluto-1.2.0-G602095-EventDefinitionReferenceDD.patch
Patch4:         portals-pluto-1.2.0-G602095-pluto-util-pom.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.6.5
BuildRequires: junit
%if %{with_maven}
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-ant
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-dependency
BuildRequires: maven2-plugin-enforcer
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-remote-resources
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven2-plugin-source
BuildRequires: maven2-plugin-war
BuildRequires: maven2-default-skin
BuildRequires: maven-surefire-plugin
%endif
BuildRequires: castor
BuildRequires: jakarta-commons-io
BuildRequires: jakarta-taglibs-standard
BuildRequires: servlet_2_4_api
BuildRequires: spring2-beans
BuildRequires: spring2-core
BuildRequires: spring2-web
BuildRequires: stax_1_0_api
BuildRequires: sun-jaxb-2.1-api
BuildRequires: sun-jaxb-2.1-impl
BuildRequires: xmlunit
BuildRequires: xpp3-minimal

Requires: %{name}-portlet-2.0-api = %{epoch}:%{version}-%{release}
Requires: castor
Requires: jakarta-commons-io
Requires: jakarta-taglibs-standard
Requires: servlet_2_4_api
Requires: spring2-beans
Requires: spring2-core
Requires: spring2-web
Requires: stax_1_0_api
Requires: sun-jaxb-2.1-api
Requires: sun-jaxb-2.1-impl
Requires: xpp3-minimal

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
Pluto is the Reference Implementation of the Java Portlet 
Specfication. 
Portlets are designed to run in the context of a portal. 
They are written to the Portlet API which are similar to 
the Servlet API.
A portlet container provides a runtime environment for 
portlets implemented according to the Portlet API. In 
this environment portlets can be instantiated, used and 
finally destroyed. The portlet container is not a 
stand-alone container like the servlet container; instead 
it is implemented as a thin layer on top of the servlet 
container and reuses the functionality provided by the 
servlet container. 
Pluto serves as portlet container that implements the 
Portlet API and offers developers a working example 
platform from which they can test their portlets. 


%package portlet-2.0-api
Summary:        Portlet 1.0 API from %{name}
Group:          Development/Java
Provides:       portlet_2_0_api
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description portlet-2.0-api
%{summary}.

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
%setup -q -n %{bname}
# remove all binary libs
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4

sed -i 's, collapsed="true",,' pluto-site/src/site/site.xml
%patch33

%build
export LANG=en_US.ISO8859-1
%if %{with_maven}
cp %{SOURCE1} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository
mkdir -p $MAVEN_REPO_LOCAL/org.apache
cp %{SOURCE3} $MAVEN_REPO_LOCAL/org.apache/apache-jar-resource-bundle.jar
mkdir -p $MAVEN_REPO_LOCAL/javax.ccpp
cp %{SOURCE4} $MAVEN_REPO_LOCAL/javax.ccpp/ccpp.jar
# 208 hacks
install -Dm644 %{SOURCE3} $MAVEN_REPO_LOCAL/org/apache/apache-jar-resource-bundle/1.2/apache-jar-resource-bundle-1.2.jar
install -Dm644 %{SOURCE4} $MAVEN_REPO_LOCAL/javax/ccpp/ccpp/1.0/ccpp-1.0.jar
# end 2008 hacks

mkdir -p pluto-container/src/main/java/org/apache/pluto/driver/core/
cp pluto-portal-driver/src/main/java/org/apache/pluto/driver/core/PortletWindowImpl.java pluto-container/src/main/java/org/apache/pluto/driver/core
cp pluto-portal-driver/src/main/java/org/apache/pluto/driver/core/PortletWindowIDImpl.java pluto-container/src/main/java/org/apache/pluto/driver/core
mkdir -p pluto-container/src/main/java/org/apache/pluto/driver/services/portal/
cp pluto-portal-driver/src/main/java/org/apache/pluto/driver/services/portal/PortletWindowConfig.java pluto-container/src/main/java/org/apache/pluto/driver/services/portal
cp pluto-portal-driver/src/main/java/org/apache/pluto/driver/services/portal/PageConfig.java pluto-container/src/main/java/org/apache/pluto/driver/services/portal
mkdir -p pluto-container/src/main/java/org/apache/pluto/driver/url/
cp pluto-portal-driver/src/main/java/org/apache/pluto/driver/url/PortalURL.java pluto-container/src/main/java/org/apache/pluto/driver/url
cp pluto-portal-driver/src/main/java/org/apache/pluto/driver/url/PortalURLParameter.java pluto-container/src/main/java/org/apache/pluto/driver/url

mv pluto-container/src/main/java/org/apache/pluto/core/PortletContainerImpl.java PortletContainerImpl.java.sav
mv pluto-container/src/main/java/org/apache/pluto/PortletContainerFactory.java PortletContainerFactory.java.sav

mv pluto-container/src/test pluto-container-src-test

mv pluto-portal-driver/src/main/java/org/apache/pluto/driver/PortalStartupListener.java PortalStartupListener.java.sav

mv pluto-portal-driver/src/test pluto-portal-driver-src-test

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
	-Dmaven.test.skip=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        install

cp pom.xml.sav0 pom.xml

mv pluto-portal-driver-src-test pluto-portal-driver/src/test

mv PortalStartupListener.java.sav pluto-portal-driver/src/main/java/org/apache/pluto/driver/PortalStartupListener.java

mv pluto-container-src-test pluto-container/src/test

mv PortletContainerFactory.java.sav pluto-container/src/main/java/org/apache/pluto/PortletContainerFactory.java
mv PortletContainerImpl.java.sav pluto-container/src/main/java/org/apache/pluto/core/PortletContainerImpl.java

rm -rf pluto-container/src/main/java/org/apache/pluto/driver
rm -rf pluto-container/target/classes/org/apache/pluto/driver

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
	-Dmaven.test.skip=true \
        ant:ant install

mkdir -p $MAVEN_REPO_LOCAL/org.apache.pluto
cp pluto-site-skin/target/pluto-site-skin-%{namedversion}.jar $MAVEN_REPO_LOCAL/org.apache.pluto/pluto-site-skin.jar

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Daggregate=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        javadoc:javadoc 

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Daggregate=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        site ||:


%else
#[INFO] Reactor build order:
#[INFO]   Apache Pluto
#[INFO]   Portlet 2.0 API
#[INFO]   Pluto Descriptor Service API
#[INFO]   Pluto Descriptor Service Implementation
#[INFO]   Pluto Portlet Container
#[INFO]   Pluto Portlet Tag Library
#[INFO]   Pluto Portal Driver
#[INFO]   Pluto Portal Driver Implementation Classes
#[INFO]   Pluto Portal
#[INFO]   Pluto Utilities
#[INFO]   Maven Pluto Installer Plugin
#[INFO]   Pluto Testsuite Portlet
#[INFO]   Pluto Ant Tasks
#[INFO]   Pluto Website Documentation
#[INFO]   Pluto Website Skin

export CLASSPATH=
pushd portlet2-api
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd
blurb
export CLASSPATH=$(build-classpath \
servletapi4 \
)
CLASSPATH=$CLASSPATH:$(pwd)/api/target/portlet-api-1.0.jar
pushd container
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd
export CLASSPATH=$(build-classpath \
castor0 \
servletapi4 \
xerces-j2 \
)
pushd descriptors
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd
export CLASSPATH=$(build-classpath \
xerces-j2 \
)
CLASSPATH=$CLASSPATH:$(pwd)/descriptors/target/pluto-descriptors-1.0.1.jar
pushd deploy
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd
export CLASSPATH=$(build-classpath \
castor0 \
commons-fileupload \
servletapi4 \
xerces-j2 \
)
CLASSPATH=$CLASSPATH:$(pwd)/api/target/portlet-api-1.0.jar
CLASSPATH=$CLASSPATH:$(pwd)/container/target/pluto-1.0.1.jar
CLASSPATH=$CLASSPATH:$(pwd)/descriptors/target/pluto-descriptors-1.0.1.jar
pushd portal
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd
export CLASSPATH=$(build-classpath \
commons-digester \
servletapi4 \
xerces-j2 \
)
CLASSPATH=$CLASSPATH:$(pwd)/api/target/portlet-api-1.0.jar
pushd testsuite
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd
%endif

%install
# jars/poms
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms


%add_to_maven_depmap org.apache.pluto pluto %{namedversion} JPP/%{name} pluto
install -m 644 pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-pluto.pom

install -m 644 portlet2-api/target/portlet-api-2.0-r26.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-portlet-2.0-api-%{version}.jar
%add_to_maven_depmap javax.portlet portlet-api 2.0 JPP portlet_1_0_api
%add_to_maven_depmap portlet-api portlet-api 2.0 JPP %{name}-portlet-2.0-api
install -m 644 portlet2-api/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-%{name}-portlet-2.0-api.pom

install -m 644 pluto-ant-tasks/target/pluto-ant-tasks-%{namedversion}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/pluto-ant-tasks-%{version}.jar
%add_to_maven_depmap org.apache.pluto pluto-ant-tasks %{namedversion} JPP/%{name} pluto-ant-tasks
install -m 644 pluto-ant-tasks/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-pluto-ant-tasks.pom

install -m 644 pluto-container/target/pluto-container-%{namedversion}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/pluto-container-%{version}.jar
%add_to_maven_depmap org.apache.pluto pluto-container %{namedversion} JPP/%{name} pluto-container
install -m 644 pluto-container/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-pluto-container.pom

install -m 644 pluto-descriptor-api/target/pluto-descriptor-api-%{namedversion}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/pluto-descriptor-api-%{version}.jar
%add_to_maven_depmap org.apache.pluto pluto-descriptor-api %{namedversion} JPP/%{name} pluto-descriptor-api
install -m 644 pluto-descriptor-api/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-pluto-descriptor-api.pom

install -m 644 pluto-descriptor-impl/target/pluto-descriptor-impl-%{namedversion}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/pluto-descriptor-impl-%{version}.jar
%add_to_maven_depmap org.apache.pluto pluto-descriptor-impl %{namedversion} JPP/%{name} pluto-descriptor-impl
install -m 644 pluto-descriptor-impl/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-pluto-descriptor-impl.pom

install -m 644 pluto-portal-driver-impl/target/pluto-portal-driver-impl-%{namedversion}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/pluto-portal-driver-impl-%{version}.jar
%add_to_maven_depmap org.apache.pluto pluto-portal-driver-impl %{namedversion} JPP/%{name} pluto-portal-driver-impl
install -m 644 pluto-portal-driver-impl/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-pluto-portal-driver-impl.pom

install -m 644 pluto-portal-driver/target/pluto-portal-driver-%{namedversion}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/pluto-portal-driver-%{version}.jar
%add_to_maven_depmap org.apache.pluto pluto-portal-driver %{namedversion} JPP/%{name} pluto-portal-driver
install -m 644 pluto-portal-driver/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-pluto-portal-driver.pom

install -m 644 pluto-site-skin/target/pluto-site-skin-%{namedversion}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/pluto-site-skin-%{version}.jar
%add_to_maven_depmap org.apache.pluto pluto-site-skin %{namedversion} JPP/%{name} pluto-site-skin
install -m 644 pluto-site-skin/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-pluto-site-skin.pom

install -m 644 pluto-taglib/target/pluto-taglib-%{namedversion}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/pluto-taglib-%{version}.jar
%add_to_maven_depmap org.apache.pluto pluto-taglib %{namedversion} JPP/%{name} pluto-taglib
install -m 644 pluto-taglib/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-pluto-taglib.pom

install -m 644 pluto-util/target/pluto-util-%{namedversion}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/pluto-util-%{version}.jar
%add_to_maven_depmap org.apache.pluto pluto-util %{namedversion} JPP/%{name} pluto-util
install -m 644 pluto-util/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-pluto-util.pom

install -m 644 maven-pluto-plugin/target/maven-pluto-plugin-%{namedversion}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/maven-pluto-plugin-%{version}.jar
%add_to_maven_depmap org.apache.pluto maven-pluto-plugin %{namedversion} JPP/%{name} maven-pluto-plugin
install -m 644 maven-pluto-plugin/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-maven-pluto-plugin.pom
install -d -m 755 ${RPM_BUILD_ROOT}%{_datadir}/maven2/plugins
pushd ${RPM_BUILD_ROOT}%{_datadir}/maven2/plugins
    ln -sf %{_javadir}/%{name}/maven-pluto-plugin-%{version}.jar maven-pluto-plugin.jar
popd

# create unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/
%if %{with_maven}
cp -pr target/site/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/ ||:
%else
cp -pr api/dist/docs/api/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/api
cp -pr container/dist/docs/api/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/container
cp -pr deploy/dist/docs/api/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/deploy
cp -pr descriptors/dist/docs/api/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/descriptors
cp -pr portal/dist/docs/api/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/portal
cp -pr testsuite/dist/docs/api/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/testsuite
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 pluto-portal/target/pluto-portal.war $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 pluto-testsuite/target/pluto-testsuite.war $RPM_BUILD_ROOT%{_datadir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp LICENSE $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %{with_maven}
rm -rf target/site/apidocs
cp -pr target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/portlet_2_0_api_%{name}-portlet-2.0-api<<EOF
%{_javadir}/portlet_2_0_api.jar	%{_javadir}/%{name}-portlet-2.0-api.jar	20000
EOF

%files 
%doc %{_docdir}/%{name}-%{version}/LICENSE
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%{_datadir}/maven2/poms/*
%{_datadir}/maven2/plugins/*
%{_mavendepmapfragdir}/*
%{_datadir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files portlet-2.0-api
%_altdir/portlet_2_0_api_%{name}-portlet-2.0-api
%{_javadir}/*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{bname}-portlet-2.0-api-%{version}.jar.*
%endif

%if %{with_maven}
%files manual
%doc %{_docdir}/%{name}-%{version}
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt4_0.G602095.1jpp5
- fixed build with maven3

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt3_0.G602095.1jpp5
- fixed build

* Thu Sep 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt2_0.G602095.1jpp5
- fixed build with new maven 2.0.8

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_0.G602095.1jpp5
- new version

