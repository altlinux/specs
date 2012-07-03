BuildRequires: mojo-parent oss-parent
BuildRequires: portals-pluto10-portlet-1.0-api
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat testng maven-surefire-provider-testng
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

%define parent myfaces

Summary:        JSF 1.2 implementation
Name:           myfaces-core12-impl
Version:        1.2.3
Release:        alt8_1jpp5
Epoch:          0
License:        Apache Software License 2.0
URL:            http://myfaces.apache.org/
Group:          Development/Java
Source0:        myfaces-core-1.2.3.tar.gz
# svn export http://svn.apache.org/repos/asf/myfaces/core/tags/1_2_3/ myfaces-core-1.2.3

Source1:        myfaces-core12-impl-jpp-depmap.xml
Source2:        myfaces-core12-impl-settings.xml
Source3:        myfaces-master.pom

Patch0:         myfaces-core12-impl-api-pom.patch
Patch1:         myfaces-core12-impl-impl-pom.patch

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-checkstyle
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-dependency
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin
BuildRequires: mojo-maven2-plugin-build-helper
BuildRequires: mojo-maven2-plugin-cobertura
BuildRequires: myfaces-maven2-plugins

BuildRequires: cargo
BuildRequires: easymock-classextension2
BuildRequires: jakarta-cactus
BuildRequires: shale-test
BuildRequires: tomcat6-lib

BuildRequires: geronimo-annotation-1.0-api
BuildRequires: geronimo-ejb-3.0-api
BuildRequires: geronimo-jpa-3.0-api
BuildRequires: google-guice
BuildRequires: jakarta-commons-discovery
BuildRequires: myfaces-core12-api
BuildRequires: myfaces-shared12
BuildRequires: servlet_2_5_api
BuildRequires: wstx

Requires: geronimo-annotation-1.0-api
Requires: geronimo-ejb-3.0-api
Requires: geronimo-jpa-3.0-api
Requires: google-guice
Requires: jakarta-commons-discovery
Requires: myfaces-core12-api
Requires: myfaces-shared12
Requires: servlet_2_5_api
Requires: wstx
BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3


%description
JavaServer(tm) Faces is a new and upcoming web application framework 
that accomplishes the MVC paradigm. It is comparable to the 
well-known Struts Framework but has features and concepts that 
are beyond those of Struts; especially the component orientation. 
Look at Sun's JavaServer(tm) Page to learn more about the Java 
Specification Request 127  and to download the specification. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n myfaces-core-%{version}

%patch0 -b .sav0
%patch1 -b .sav1

# easymock 2.3; incompatible with easymock 2.5
rm api/src/test/java/javax/faces/component/_ValueExpressionToValueBindingTest.java
rm impl/src/test/java/org/apache/myfaces/el/convert/ValueExpressionToValueBindingTest.java

%build
export LANG=en_US.ISO8859-1
cp %{SOURCE2} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository
mkdir -p ${MAVEN_REPO_LOCAL}/JPP/maven2/default_poms/
cp %{SOURCE3} ${MAVEN_REPO_LOCAL}/JPP/maven2/default_poms/org.apache.myfaces-myfaces.pom
install -Dm644 %{SOURCE3} ${MAVEN_REPO_LOCAL}/org/apache/myfaces/myfaces/5/myfaces-5.pom
install -Dm644 %{SOURCE3} ${MAVEN_REPO_LOCAL}/org/apache/myfaces/myfaces/6/myfaces-6.pom

mvn-jpp -e \
	-Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5 \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install:install-file -DgroupId=org.testng -DartifactId=testng -Dversion=5.1 -Dclassifier=jdk15 -Dpackaging=jar -Dfile=/usr/share/java/testng.jar

mvn-jpp -e \
	-Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5 \
	-s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
	install:install-file -DgroupId=org.apache.myfaces.shared -DartifactId=myfaces-shared-impl -Dversion=3.0.3 -Dclassifier=sources -Dpackaging=jar -Dfile=/usr/share/java/myfaces/shared12-impl.jar


mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc


%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{parent}
install -m 644 impl/target/myfaces-impl-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{parent}/core12-impl-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{parent} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 impl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{parent}-core12-impl.pom
%add_to_maven_depmap org.apache.myfaces.core myfaces-impl %{version} JPP/%{parent} core12-impl

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr api/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc assembly/src/main/resources/LICENSE.txt
%{_javadir}/%{parent}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt8_1jpp5
- fixed build with new testng and xbean

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt7_1jpp5
- fixed build with java 7

* Sat Feb 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt6_1jpp5
- fixed build

* Sun Jan 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt5_1jpp5
- fixed build

* Tue Jan 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt4_1jpp5
- fixed build

* Tue Nov 02 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt3_1jpp5
- build with wstx 3.2.8

* Mon Sep 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt2_1jpp5
- fixed build with new maven 2.0.8

* Thu May 28 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt1_1jpp5
- new jpp release

