BuildRequires: cssparser
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

#def_with coreonly
%bcond_with coreonly
#def_with gcj_support
%bcond_with gcj_support
#def_with jsf_ri
%bcond_with jsf_ri

%if %with coreonly
#def_with apps
%bcond_with apps
#def_with manual
%bcond_with manual
#def_with zips
%bcond_with zips
%else
%bcond_with apps
%bcond_with manual
#def_with zips
%bcond_with zips
%endif

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           struts
Version:        1.3.10
Release:        alt2_2jpp6
Epoch:          0
Summary:        Web application framework
License:        ASL 2.0
Group:          Development/Java
URL:            http://struts.apache.org/
Source0:        http://archive.apache.org/dist/struts/source/struts-1.3.10-src.zip
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        http://svn.apache.org/repos/asf/struts/maven/tags/STRUTS_MASTER_4/pom.xml
Source4:        %{name}-checks.xml
Patch0:         struts-1.3.8-core-pom.patch
Patch1:         struts-1.3.10-Tomcat5xTestSetup.patch
Patch2:         struts-1.3.8-assembly-pom.patch
Patch3:         struts-1.3.10-taglib-pom.patch
Patch4:         struts-1.3.10-pom.patch
# Part of updating the syntax in site.xml for the new site plugin
Patch5:         struts-1.3.8-site.patch
Patch6:         struts-1.3.8-no-sign.patch
Patch7:         struts-1.3.8-no-versions.patch
Patch8:         struts-1.3.8-jsf-ri.patch
Patch9:         struts-1.3.8-no-apps.patch
Patch10:        struts-1.3.8-web-xml-version.patch
Patch11:        struts-1.3.8-apps-scripting-mailreader.patch
# This is due to <http://jira.codehaus.org/browse/MCHECKSTYLE-97>
Patch12:         struts-1.3.10-no-checkstyle.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-extras = %{epoch}:%{version}-%{release}
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: junit
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-checkstyle
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-dependency
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-gpg
BuildRequires: maven2-plugin-pmd
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven2-plugin-source
BuildRequires: maven2-plugin-war
BuildRequires: maven-jxr
BuildRequires: maven-surefire-plugin
BuildRequires: maven2-plugin-surefire-report
BuildRequires: maven-surefire-provider-junit
BuildRequires: cargo-maven2-plugin
BuildRequires: commons-parent
BuildRequires: dtddoc-maven2-plugin
BuildRequires: taglib-maven2-plugin
BuildRequires: bcel
BuildRequires: checkstyle4
BuildRequires: checkstyle4-optional
BuildRequires: jhighlight
BuildRequires: maven2-default-skin
BuildRequires: jakarta-taglibs-standard
BuildRequires: servlet_2_4_api
BuildRequires: jsp_2_0_api
%if %without jsf_ri
BuildRequires: myfaces
%else
BuildRequires: glassfish-jsf
%endif
BuildRequires: antlr
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-digester
BuildRequires: jakarta-commons-fileupload
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-validator
BuildRequires: jakarta-oro
BuildRequires: xpp3-minimal
# For compilation
BuildRequires: servletapi4
# For tests
BuildRequires: tomcat5-servlet-2.4-api
BuildRequires: tomcat6-el-2.1-api
BuildRequires: tomcat5-jsp-2.0-api
BuildRequires: tomcat6-jsp-2.1-api
%if %without coreonly
BuildRequires: bsf
BuildRequires: excalibur-avalon-framework
BuildRequires: excalibur-avalon-logkit
BuildRequires: groovy15
BuildRequires: jakarta-commons-chain
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-el
BuildRequires: jakarta-taglibs-standard
BuildRequires: log4j
# src/integration/apps-it/pom.xml:
BuildRequires: htmlunit >= 0:1.8
BuildRequires: cargo >= 0:0.8
%endif
Obsoletes:      struts-webapps-tomcat3 < %{epoch}:%{version}
Provides:       struts-webapps-tomcat3 = %{epoch}:%{version}-%{release}
Obsoletes:      struts-webapps-tomcat4 < %{epoch}:%{version}
Provides:       struts-webapps-tomcat4 = %{epoch}:%{version}-%{release}
Obsoletes:      struts-webapps-tomcat5 < %{epoch}:%{version}
Provides:       struts-webapps-tomcat5 = %{epoch}:%{version}-%{release}
Obsoletes:      struts-chain-webapps-tomcat3 < %{epoch}:%{version}
Provides:       struts-chain-webapps-tomcat3 = %{epoch}:%{version}-%{release}
Obsoletes:      struts-chain-webapps-tomcat4 < %{epoch}:%{version}
Provides:       struts-chain-webapps-tomcat4 = %{epoch}:%{version}-%{release}
Obsoletes:      struts-chain-webapps-tomcat5 < %{epoch}:%{version}
Provides:       struts-chain-webapps-tomcat5 = %{epoch}:%{version}-%{release}
Obsoletes:      struts-el-webapps-tomcat3 < %{epoch}:%{version}
Provides:       struts-el-webapps-tomcat3 = %{epoch}:%{version}-%{release}
Obsoletes:      struts-el-webapps-tomcat4 < %{epoch}:%{version}
Provides:       struts-el-webapps-tomcat4 = %{epoch}:%{version}-%{release}
Obsoletes:      struts-el-webapps-tomcat5 < %{epoch}:%{version}
Provides:       struts-el-webapps-tomcat5 = %{epoch}:%{version}-%{release}
Obsoletes:      struts-faces-webapps-tomcat3 < %{epoch}:%{version}
Provides:       struts-faces-webapps-tomcat3 = %{epoch}:%{version}-%{release}
Obsoletes:      struts-faces-webapps-tomcat4 < %{epoch}:%{version}
Provides:       struts-faces-webapps-tomcat4 = %{epoch}:%{version}-%{release}
Obsoletes:      struts-faces-webapps-tomcat5 < %{epoch}:%{version}
Provides:       struts-faces-webapps-tomcat5 = %{epoch}:%{version}-%{release}
Obsoletes:      struts-chain < %{epoch}:%{version}
Provides:       struts-chain = %{epoch}:%{version}-%{release}
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
Welcome to the Struts Framework! The goal of this project is to provide
an open source framework useful in building web applications with Java
Servlet and JavaServer Pages (JSP) technology. Struts encourages
application architectures based on the Model-View-Controller (MVC)
design paradigm, colloquially known as Model 2 in discussions on various
servlet and JSP related mailing lists.

Struts includes the following primary areas of functionality:
A controller servlet that dispatches requests to appropriate Action
classes provided by the application developer.
JSP custom tag libraries, and associated support in the controller
servlet, that assists developers in creating interactive form-based
applications.

Utility classes to support XML parsing, automatic population of
JavaBeans properties based on the Java reflection APIs, and
internationalization of prompts and messages.
Struts is part of the Jakarta Project, sponsored by the Apache Software
Foundation. The official Struts home page is at
http://jakarta.apache.org/struts.

%if %with manual
%package manual
Summary:        Manual for %{name}
Group:          Development/Documentation
Requires: %{name}-javadoc = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description manual
Documentation for %{name}.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package core
Summary:        Core for %{name}
Group:          Development/Java
Requires: antlr >= 0:2.7.2
Requires: jakarta-commons-beanutils >= 0:1.8.0
Requires: jakarta-commons-chain >= 0:1.2
Requires: jakarta-commons-digester >= 0:1.8
Requires: jakarta-commons-logging >= 0:1.0.4
Requires: jakarta-commons-validator >= 0:1.3.1
Requires: jakarta-oro >= 0:2.0.8
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: commons-parent >= 0:7

%description core
%{summary}.

%if %without coreonly
%package el
Summary:        EL extension for %{name}
Group:          Development/Java
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-taglib = %{epoch}:%{version}-%{release}
Requires: %{name}-tiles = %{epoch}:%{version}-%{release}
Requires: jakarta-taglibs-standard >= 0:1.0.6
#Provided:      servlet_2_3_api

%description el
%{summary}.

%package extras
Summary:        Extras for %{name}
Group:          Development/Java
Requires: %{name}-core = %{epoch}:%{version}-%{release}
#Provided:      servlet_2_3_api

%description extras
%{summary}.

%package faces
Summary:        Integration library for %{name}-faces
Group:          Development/Java
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-taglib = %{epoch}:%{version}-%{release}
Requires: %{name}-tiles = %{epoch}:%{version}-%{release}
%if %without jsf_ri
#Provided:      myfaces >= 0:1.0.9
%else
#Provided:      glassfish-jsf
%endif
#Provided:      jsp_2_0_api
#Provided:      servlet_2_3_api

%description faces
%{summary}.

%package mailreader-dao
Summary:        %{name} mailreader-dao library
Group:          Development/Java
Requires: jakarta-commons-digester >= 0:1.8
Requires: jakarta-commons-logging >= 0:1.0.4

%description mailreader-dao
%{summary}.

%package scripting
Summary:        %{name} scripting library
Group:          Development/Java
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: bsf >= 0:2.3
#Provided:      servlet_2_3_api

%description scripting
%{summary}.

%package taglib
Summary:        %{name} taglib library
Group:          Development/Java
Requires: %{name}-core = %{epoch}:%{version}-%{release}
#Provided:      servlet_2_3_api

%description taglib
%{summary}.

%package tiles
Summary:        %{name} tiles library
Group:          Development/Java
Requires: %{name}-core = %{epoch}:%{version}-%{release}
#Provided:      servlet_2_3_api

%description tiles
%{summary}.
%endif # coreonly

%if %with apps
%package webapp-blank
Summary:        Sample %{name} blank webapp
Group:          Development/Java
Requires: %{name}-taglib = %{epoch}:%{version}-%{release}
Requires: %{name}-tiles = %{epoch}:%{version}-%{release}
#Provided:      servlet_2_3_api

%description webapp-blank
%{summary}.

%package webapp-cookbook
Summary:        Sample %{name} cookbook webapp
Group:          Development/Java
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-taglib = %{epoch}:%{version}-%{release}
#Provided:      servlet_2_3_api

%description webapp-cookbook
%{summary}.

%package webapp-el-example
Summary:        Sample %{name} EL webapp
Group:          Development/Java
Requires: antlr
Requires: excalibur-avalon-framework
Requires: excalibur-avalon-logkit
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-chain
Requires: jakarta-commons-digester
Requires: jakarta-commons-logging
Requires: jakarta-commons-validator
Requires: jakarta-taglibs-standard
Requires: log4j
Requires: jakarta-oro
Requires: %{name}-el = %{epoch}:%{version}-%{release}
#Provided:      servlet_2_3_api

%description webapp-el-example
%{summary}.

%package webapp-examples
Summary:        Sample %{name} webapp
Group:          Development/Java
Requires: %{name}-extras = %{epoch}:%{version}-%{release}
Requires: %{name}-taglib = %{epoch}:%{version}-%{release}
#Provided:      servlet_2_3_api
Requires: jakarta-taglibs-standard >= 0:1.0.6
Requires: jakarta-commons-fileupload >= 0:1.1.1

%description webapp-examples
%{summary}.

%package webapps-faces
Summary:        Sample %{name} faces webapps
Group:          Development/Java
%if %with jsf_ri
#Optional:      myfaces >= 0:1.0.9
%else
#Optional:      glassfish-jsf
%endif
Requires: jakarta-commons-codec >= 0:1.2
Requires: jakarta-commons-el >= 0:1.0
Requires: jakarta-taglibs-standard >= 0:1.0.6
Requires: %{name}-faces = %{epoch}:%{version}-%{release}
Requires: %{name}-tiles = %{epoch}:%{version}-%{release}
#Provided:      servlet_2_3_api

%description webapps-faces
%{summary}.

%package webapp-mailreader
Summary:        Sample %{name} mailreader webapp
Group:          Development/Java
Requires: %{name}-extras = %{epoch}:%{version}-%{release}
Requires: %{name}-mailreader-dao = %{epoch}:%{version}-%{release}
Requires: %{name}-taglib = %{epoch}:%{version}-%{release}
#Provided:      servlet_2_3_api

%description webapp-mailreader
%{summary}.

%package webapp-scripting-mailreader
Summary:        Sample %{name} scripting mailreader webapp
Group:          Development/Java
Requires: groovy15
Requires: %{name}-extras = %{epoch}:%{version}-%{release}
Requires: %{name}-mailreader-dao = %{epoch}:%{version}-%{release}
Requires: %{name}-scripting = %{epoch}:%{version}-%{release}
Requires: %{name}-taglib = %{epoch}:%{version}-%{release}
#Provided:      servlet_2_3_api

%description webapp-scripting-mailreader
%{summary}.
%endif # apps

%if %with zips
%package zip
Summary:     Container for the zipped distribution of %{name}
Group:       Development/Java

%description zip
Container for the zipped distribution of %{name}.

%package src-zip
Summary:     Container for the sources of %{name}
Group:       Development/Java

%description src-zip
Container for the sources of %{name}.
%endif # zips

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%if %with jsf_ri
%patch8
%endif
%if %without apps
%patch9
%endif
%patch10
%patch11
%patch12

# Finish updating the syntax in site.xml for the new site plugin
for j in $(find . -name "site.xml"); do
    perl -p -i -e 's/\$\{reports\}/\<menu ref=\"reports\" \/\>/' $j
done

%if %without jsf_ri
perl -pi -e 's/^MYFACES_BEGIN.*\n$//g;' \
         -e 's/^MYFACES_END.*\n$//g;' \
%else
perl -pi -e 's/^MYFACES_BEGIN.*\n$/<!--\r\n/g;' \
         -e 's/^MYFACES_END.*\n$/-->\r\n/g;' \
%endif
    src/apps/faces-example1/src/main/webapp/WEB-INF/web.xml \
    src/apps/faces-example2/src/main/webapp/WEB-INF/web.xml

%if %with zips
# Create src-zip
mkdir -p dist/%{name}-%{version}
cd dist/%{name}-%{version}
cp -R ../../src .
cp -R ../../*.txt .
zip -q -r ../%{name}-%{version}-src.zip * -x \*.sav*
rm -Rf src
cd ../../
%endif

cp -p %{SOURCE3} pom.xml

cp -p %{SOURCE1} maven2-settings.xml
CHECK_XML_LOCATION=$(pwd)/struts_checks.xml
cp -p %{SOURCE4} $CHECK_XML_LOCATION

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<configLocation>__STRUTS_CHECKS__</configLocation>|<configLocation>file://$CHECK_XML_LOCATION</configLocation>|g" src/pom.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

find -type f -name site.xml | xargs -t perl -pi -e 's|\$\{modules\}||g;' -e 's|\$\{reports\}||g;'

%build
export LANG=en_US.ISO8859-1
export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository
mkdir -p $MAVEN_REPO_LOCAL/JPP/maven2/default_poms
cp -p %{SOURCE3} $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/org.apache.struts-struts-master.pom
#cp -p %{SOURCE3} $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/JPP-struts-master.pom

export MAVEN_OPTS="-Xmx256M -Djava.awt.headless=true"

pushd src/
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dcargo.tomcat5x.home=%{_datadir}/tomcat5 \
        -Dmaven.test.failure.ignore=true \
        install -P apps,itest,pre-assembly

#mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
#        -s ${M2SETTINGS} \
#        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
#        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
#        -Daggregate=true \
#        site -P apps,itest,pre-assembly
popd

#pushd src/assembly/
#mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
#        -s ${M2SETTINGS} \
#        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
#        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
#    assembly:assembly
#popd

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 0644 src/core/target/%{name}-core-%{version}.jar %{buildroot}%{_javadir}/%{name}-core-%{version}.jar
ln -s %{name}-core-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%if %without coreonly
install -p -m 0644 src/el/target/%{name}-el-%{version}.jar %{buildroot}%{_javadir}/%{name}-el-%{version}.jar
install -p -m 0644 src/extras/target/%{name}-extras-%{version}.jar %{buildroot}%{_javadir}/%{name}-extras-%{version}.jar
install -p -m 0644 src/faces/target/%{name}-faces-%{version}.jar %{buildroot}%{_javadir}/%{name}-faces-%{version}.jar
install -p -m 0644 src/mailreader-dao/target/%{name}-mailreader-dao-%{version}.jar %{buildroot}%{_javadir}/%{name}-mailreader-dao-%{version}.jar
install -p -m 0644 src/scripting/target/%{name}-scripting-%{version}.jar %{buildroot}%{_javadir}/%{name}-scripting-%{version}.jar
install -p -m 0644 src/taglib/target/%{name}-taglib-%{version}.jar %{buildroot}%{_javadir}/%{name}-taglib-%{version}.jar
install -p -m 0644 src/tiles/target/%{name}-tiles-%{version}.jar %{buildroot}%{_javadir}/%{name}-tiles-%{version}.jar
%endif
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} ${jar/-%{version}/}; done)
%if %with apps
pushd %{buildroot}%{_javadir}
ln -s %{_datadir}/%{name}/apps %{name}-apps
popd
%endif

# poms and depmap frags
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
%if %with apps
install -p -m 0644 src/apps/blank/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-apps-blank.pom
%add_to_maven_depmap org.apache.struts struts-blank %{version} JPP/%{name}-apps blank
install -p -m 0644 src/apps/cookbook/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-apps-cookbook.pom
%add_to_maven_depmap org.apache.struts struts-cookbook %{version} JPP/%{name}-apps cookbook
install -p -m 0644 src/apps/el-example/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-apps-el-example.pom
%add_to_maven_depmap org.apache.struts struts-el %{version} JPP/%{name}-apps el-example
install -p -m 0644 src/apps/examples/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-apps-examples.pom
%add_to_maven_depmap org.apache.struts struts-examples %{version} JPP/%{name}-apps examples
install -p -m 0644 src/apps/faces-example1/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-apps-faces-example1.pom
%add_to_maven_depmap org.apache.struts struts-faces-example1 %{version} JPP/%{name}-apps faces-example1
install -p -m 0644 src/apps/faces-example2/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-apps-faces-example2.pom
%add_to_maven_depmap org.apache.struts struts-faces-example2 %{version} JPP/%{name}-apps faces-example2
install -p -m 0644 src/apps/mailreader/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-apps-mailreader.pom
%add_to_maven_depmap org.apache.struts struts-mailreader %{version} JPP/%{name}-apps mailreader
install -p -m 0644 src/apps/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-apps.pom
%add_to_maven_depmap org.apache.struts struts-apps %{version} JPP %{name}-apps
install -p -m 0644 src/apps/scripting-mailreader/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-apps-scripting-mailreader.pom
%add_to_maven_depmap org.apache.struts struts-scripting-mailreader %{version} JPP/%{name}-apps scripting-mailreader
%endif
install -p -m 0644 src/assembly/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-assembly.pom
%add_to_maven_depmap org.apache.struts struts-assembly %{version} JPP %{name}-assembly
install -p -m 0644 src/core/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache.struts struts-core %{version} JPP %{name}
install -p -m 0644 src/integration/apps-it/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-it-apps.pom
%add_to_maven_depmap org.apache.struts struts-it-apps %{version} JPP %{name}-it-apps
install -p -m 0644 src/integration/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-it.pom
%add_to_maven_depmap org.apache.struts struts-it %{version} JPP %{name}-it
%if %without coreonly
install -p -m 0644 src/el/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-el.pom
%add_to_maven_depmap org.apache.struts struts-el %{version} JPP %{name}-el
install -p -m 0644 src/extras/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-extras.pom
%add_to_maven_depmap org.apache.struts struts-extras %{version} JPP %{name}-extras
install -p -m 0644 src/faces/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-faces.pom
%add_to_maven_depmap org.apache.struts struts-faces %{version} JPP %{name}-faces
install -p -m 0644 src/mailreader-dao/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-mailreader-dao.pom
%add_to_maven_depmap org.apache.struts struts-mailreader-dao %{version} JPP %{name}-mailreader-dao
install -p -m 0644 src/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
%add_to_maven_depmap org.apache.struts struts-parent %{version} JPP %{name}-parent
install -p -m 0644 src/scripting/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-scripting.pom
%add_to_maven_depmap org.apache.struts struts-scripting %{version} JPP %{name}-scripting
install -p -m 0644 src/taglib/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-taglib.pom
%add_to_maven_depmap org.apache.struts struts-taglib %{version} JPP %{name}-taglib
install -p -m 0644 src/tiles/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-tiles.pom
%add_to_maven_depmap org.apache.struts struts-tiles %{version} JPP %{name}-tiles
%endif
install -p -m 0644 pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-master.pom
%add_to_maven_depmap org.apache.struts struts-master %{version} JPP %{name}-master

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
#cp -pr src/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
#rm -rf src/target/site/apidocs

# data
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -p -m 0644 src/el/src/main/resources/META-INF/tld/*.tld %{buildroot}%{_datadir}/%{name}
install -p -m 0644 src/faces/src/main/resources/META-INF/tld/*.tld %{buildroot}%{_datadir}/%{name}
install -p -m 0644 src/taglib/src/main/resources/META-INF/tld/*.tld %{buildroot}%{_datadir}/%{name}
install -p -m 0644 src/tiles/src/main/resources/META-INF/tld/*.tld %{buildroot}%{_datadir}/%{name}
#install -p -m 0644 src/target/site/dtds/*.dtd %{buildroot}%{_datadir}/%{name}
install -p -m 0644 src/core/src/main/resources/org/apache/struts/validator/vali*.xml %{buildroot}%{_datadir}/%{name}

%if %with apps
install -d -m 755 %{buildroot}%{_datadir}/%{name}/apps
pushd %{buildroot}%{_datadir}/%{name}/apps
mkdir blank.war
pushd blank.war
unzip -qq $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-blank*.war
rm -v WEB-INF/lib/*
#WEB-INF/lib/antlr-2.7.2.jar
ln -s $(build-classpath antlr) .
#WEB-INF/lib/avalon-framework-4.1.3.jar
ln -s $(build-classpath excalibur/avalon-framework) .
#WEB-INF/lib/commons-beanutils-1.8.0.jar
ln -s $(build-classpath commons-beanutils) .
#WEB-INF/lib/commons-chain-1.2.jar
ln -s $(build-classpath commons-chain) .
#WEB-INF/lib/commons-collections-3.1.jar
ln -s $(build-classpath commons-collections) .
#WEB-INF/lib/commons-digester-1.8.jar
ln -s $(build-classpath commons-digester) .
#WEB-INF/lib/commons-logging-1.0.4.jar
ln -s $(build-classpath commons-logging) .
#WEB-INF/lib/commons-validator-1.3.1.jar
ln -s $(build-classpath commons-validator) .
#WEB-INF/lib/log4j-1.2.12.jar
ln -s $(build-classpath log4j) .
#WEB-INF/lib/logkit-1.0.1.jar
ln -s $(build-classpath excalibur/avalon-logkit) .
#WEB-INF/lib/mail-1.4.jar
ln -s $(build-classpath javamail_1_4_api) .
#WEB-INF/lib/oro-2.0.8.jar
ln -s $(build-classpath jakarta-oro) .
#WEB-INF/lib/struts-core-1.3.10.jar
ln -s %{_javadir}/struts-core.jar .
#WEB-INF/lib/struts-taglib-1.3.10.jar
ln -s %{_javadir}/struts-taglib.jar .
#WEB-INF/lib/struts-tiles-1.3.10.jar
ln -s %{_javadir}/struts-tiles.jar .
rm $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-blank*.war
zip -q -r $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-blank.war .
popd
mkdir cookbook.war
pushd cookbook.war
unzip -qq $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-cookbook*.war
rm -v WEB-INF/lib/*
#WEB-INF/lib/antlr-2.7.2.jar
ln -s $(build-classpath antlr) .
#WEB-INF/lib/avalon-framework-4.1.3.jar
ln -s $(build-classpath excalibur/avalon-framework) .
#WEB-INF/lib/commons-beanutils-1.8.0.jar
ln -s $(build-classpath commons-beanutils) .
#WEB-INF/lib/commons-chain-1.2.jar
ln -s $(build-classpath commons-chain) .
#WEB-INF/lib/commons-collections-3.1.jar
ln -s $(build-classpath commons-collections) .
#WEB-INF/lib/commons-digester-1.8.jar
ln -s $(build-classpath commons-digester) .
#WEB-INF/lib/commons-logging-1.0.4.jar
ln -s $(build-classpath commons-logging) .
#WEB-INF/lib/commons-validator-1.3.1.jar
ln -s $(build-classpath commons-validator) .
#WEB-INF/lib/log4j-1.2.12.jar
ln -s $(build-classpath log4j) .
#WEB-INF/lib/logkit-1.0.1.jar
ln -s $(build-classpath excalibur/avalon-logkit) .
#WEB-INF/lib/mail-1.4.jar
ln -s $(build-classpath javamail_1_4_api) .
#WEB-INF/lib/oro-2.0.8.jar
ln -s $(build-classpath jakarta-oro) 
#WEB-INF/lib/struts-core-1.3.10.jar
ln -s %{_javadir}/struts-core.jar .
#WEB-INF/lib/struts-taglib-1.3.10.jar
ln -s %{_javadir}/struts-taglib.jar .
rm $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-cookbook*.war
zip -q -r $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-cookbook.war .
popd
mkdir el-example.war
pushd el-example.war
unzip -qq $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-el-example*.war
rm -v WEB-INF/lib/*
#WEB-INF/lib/antlr-2.7.2.jar
ln -s $(build-classpath antlr) .
#WEB-INF/lib/avalon-framework-4.1.3.jar
ln -s $(build-classpath excalibur/avalon-framework) .
#WEB-INF/lib/commons-beanutils-1.8.0.jar
ln -s $(build-classpath commons-beanutils) .
#WEB-INF/lib/commons-chain-1.2.jar
ln -s $(build-classpath commons-chain) .
#WEB-INF/lib/commons-collections-3.1.jar
ln -s $(build-classpath commons-collections) .
#WEB-INF/lib/commons-digester-1.8.jar
ln -s $(build-classpath commons-digester) .
#WEB-INF/lib/commons-logging-1.0.4.jar
ln -s $(build-classpath commons-logging) .
#WEB-INF/lib/commons-validator-1.3.1.jar
ln -s $(build-classpath commons-validator) .
#WEB-INF/lib/jstl-1.0.2.jar
ln -s $(build-classpath jakarta-taglibs-core) .
#WEB-INF/lib/log4j-1.2.12.jar
ln -s $(build-classpath log4j) .
#WEB-INF/lib/logkit-1.0.1.jar
ln -s $(build-classpath excalibur/avalon-logkit) .
#WEB-INF/lib/mail-1.4.jar
ln -s $(build-classpath javamail_1_4_api) .
#WEB-INF/lib/oro-2.0.8.jar
ln -s $(build-classpath jakarta-oro) .
#WEB-INF/lib/standard-1.0.6.jar
ln -s $(build-classpath jakarta-taglibs-standard) .
#WEB-INF/lib/struts-core-1.3.10.jar
ln -s %{_javadir}/struts-core.jar .
#WEB-INF/lib/struts-el-1.3.10.jar
ln -s %{_javadir}/struts-el.jar .
#WEB-INF/lib/struts-taglib-1.3.10.jar
ln -s %{_javadir}/struts-taglib.jar .
rm $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-el-example*.war
zip -q -r $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-el-example.war .
popd
mkdir examples.war
pushd examples.war
unzip -qq $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-examples*.war
rm -v WEB-INF/lib/*
#WEB-INF/lib/antlr-2.7.2.jar
ln -s $(build-classpath antlr) .
#WEB-INF/lib/avalon-framework-4.1.3.jar
ln -s $(build-classpath excalibur/avalon-framework) .
#WEB-INF/lib/commons-beanutils-1.8.0.jar
ln -s $(build-classpath commons-beanutils) .
#WEB-INF/lib/commons-chain-1.2.jar
ln -s $(build-classpath commons-chain) .
#WEB-INF/lib/commons-collections-3.1.jar
ln -s $(build-classpath commons-collections) .
#WEB-INF/lib/commons-digester-1.8.jar
ln -s $(build-classpath commons-digester) .
#WEB-INF/lib/commons-fileupload-1.1.1.jar
ln -s $(build-classpath commons-fileupload) .
#WEB-INF/lib/commons-logging-1.0.4.jar
ln -s $(build-classpath commons-logging) .
#WEB-INF/lib/commons-validator-1.3.1.jar
ln -s $(build-classpath commons-validator) .
#WEB-INF/lib/jstl-1.0.6.jar
ln -s $(build-classpath jakarta-taglibs-core) .
#WEB-INF/lib/log4j-1.2.12.jar
ln -s $(build-classpath log4j) .
#WEB-INF/lib/logkit-1.0.1.jar
ln -s $(build-classpath excalibur/avalon-logkit) .
#WEB-INF/lib/mail-1.4.jar
ln -s $(build-classpath javamail_1_4_api) .
#WEB-INF/lib/oro-2.0.8.jar
ln -s $(build-classpath jakarta-oro) .
#WEB-INF/lib/standard-1.0.6.jar
ln -s $(build-classpath jakarta-taglibs-standard) .
#WEB-INF/lib/struts-core-1.3.10.jar
ln -s %{_javadir}/struts-core.jar .
#WEB-INF/lib/struts-extras-1.3.10.jar
ln -s %{_javadir}/struts-extras.jar .
#WEB-INF/lib/struts-taglib-1.3.10.jar
ln -s %{_javadir}/struts-taglib.jar .
rm $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-examples*.war
zip -q -r $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-examples.war .
popd
mkdir faces-example1.war
pushd faces-example1.war
unzip -qq $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-faces-example1*.war
rm -v WEB-INF/lib/*
#WEB-INF/lib/antlr-2.7.2.jar
ln -s $(build-classpath antlr) .
#WEB-INF/lib/avalon-framework-4.1.3.jar
ln -s $(build-classpath excalibur/avalon-framework) .
#WEB-INF/lib/commons-beanutils-1.8.0.jar
ln -s $(build-classpath commons-beanutils) .
#WEB-INF/lib/commons-chain-1.2.jar
ln -s $(build-classpath commons-chain) .
#WEB-INF/lib/commons-codec-1.2.jar
ln -s $(build-classpath commons-codec) .
#WEB-INF/lib/commons-collections-3.1.jar
ln -s $(build-classpath commons-collections) .
#WEB-INF/lib/commons-digester-1.8.jar
ln -s $(build-classpath commons-digester) .
#WEB-INF/lib/commons-el-1.0.jar
ln -s $(build-classpath commons-el) .
#WEB-INF/lib/commons-logging-1.0.4.jar
ln -s $(build-classpath commons-logging) .
#WEB-INF/lib/commons-validator-1.3.1.jar
ln -s $(build-classpath commons-validator) .
#WEB-INF/lib/jstl-1.0.2.jar
ln -s $(build-classpath jakarta-taglibs-core) .
#WEB-INF/lib/log4j-1.2.12.jar
ln -s $(build-classpath log4j) .
#WEB-INF/lib/logkit-1.0.1.jar
ln -s $(build-classpath excalibur/avalon-logkit) .
#WEB-INF/lib/mail-1.4.jar
ln -s $(build-classpath javamail_1_4_api) .
#WEB-INF/lib/myfaces-extensions-1.0.9.jar
ln -s $(build-classpath myfaces/myfaces-all) .
#WEB-INF/lib/myfaces-impl-1.0.9.jar
ln -s $(build-classpath myfaces/myfaces-impl) .
#WEB-INF/lib/myfaces-jsf-api-1.0.9.jar
ln -s $(build-classpath myfaces/myfaces-jsf-api) .
#WEB-INF/lib/oro-2.0.8.jar
ln -s $(build-classpath jakarta-oro) .
#WEB-INF/lib/standard-1.0.6.jar
ln -s $(build-classpath jakarta-taglibs-standard) .
#WEB-INF/lib/struts-core-1.3.10.jar
ln -s %{_javadir}/struts-core.jar .
#WEB-INF/lib/struts-faces-1.3.10.jar
ln -s %{_javadir}/struts-faces.jar .
#WEB-INF/lib/struts-taglib-1.3.10.jar
ln -s %{_javadir}/struts-taglib.jar .
#WEB-INF/lib/struts-tiles-1.3.10.jar
ln -s %{_javadir}/struts-tiles.jar .
rm $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-faces-example1*.war
zip -q -r $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-faces-example1.war .
popd
mkdir faces-example2.war
pushd faces-example2.war
unzip -qq $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-faces-example2*.war
rm -v WEB-INF/lib/*
#WEB-INF/lib/antlr-2.7.2.jar
ln -s $(build-classpath antlr) .
#WEB-INF/lib/avalon-framework-4.1.3.jar
ln -s $(build-classpath excalibur/avalon-framework) .
#WEB-INF/lib/commons-beanutils-1.8.0.jar
ln -s $(build-classpath commons-beanutils) .
#WEB-INF/lib/commons-chain-1.2.jar
ln -s $(build-classpath commons-chain) .
#WEB-INF/lib/commons-codec-1.2.jar
ln -s $(build-classpath commons-codec) .
#WEB-INF/lib/commons-collections-3.1.jar
ln -s $(build-classpath commons-collections) .
#WEB-INF/lib/commons-digester-1.8.jar
ln -s $(build-classpath commons-digester) .
#WEB-INF/lib/commons-el-1.0.jar
ln -s $(build-classpath commons-el) .
#WEB-INF/lib/commons-logging-1.0.4.jar
ln -s $(build-classpath commons-logging) .
#WEB-INF/lib/commons-validator-1.3.1.jar
ln -s $(build-classpath commons-validator) .
#WEB-INF/lib/jstl-1.0.2.jar
ln -s $(build-classpath jakarta-taglibs-core) .
#WEB-INF/lib/log4j-1.2.12.jar
ln -s $(build-classpath log4j) .
#WEB-INF/lib/logkit-1.0.1.jar
ln -s $(build-classpath excalibur/avalon-logkit) .
#WEB-INF/lib/mail-1.4.jar
ln -s $(build-classpath javamail_1_4_api) .
#WEB-INF/lib/myfaces-extensions-1.0.9.jar
ln -s $(build-classpath myfaces/myfaces-all) .
#WEB-INF/lib/myfaces-impl-1.0.9.jar
ln -s $(build-classpath myfaces/myfaces-impl) .
#WEB-INF/lib/myfaces-jsf-api-1.0.9.jar
ln -s $(build-classpath myfaces/myfaces-jsf-api) .
#WEB-INF/lib/oro-2.0.8.jar
ln -s $(build-classpath jakarta-oro) .
#WEB-INF/lib/standard-1.0.6.jar
ln -s $(build-classpath jakarta-taglibs-standard) .
#WEB-INF/lib/struts-core-1.3.10.jar
ln -s %{_javadir}/struts-core.jar .
#WEB-INF/lib/struts-faces-1.3.10.jar
ln -s %{_javadir}/struts-faces.jar .
#WEB-INF/lib/struts-taglib-1.3.10.jar
ln -s %{_javadir}/struts-taglib.jar .
#WEB-INF/lib/struts-tiles-1.3.10.jar
ln -s %{_javadir}/struts-tiles.jar .
rm $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-faces-example2*.war
zip -q -r $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-faces-example2.war .
popd
mkdir mailreader.war
pushd mailreader.war
unzip -qq $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-mailreader*.war
rm -v WEB-INF/lib/*
#WEB-INF/lib/antlr-2.7.2.jar
ln -s $(build-classpath antlr) .
#WEB-INF/lib/avalon-framework-4.1.3.jar
ln -s $(build-classpath excalibur/avalon-framework) .
#WEB-INF/lib/commons-beanutils-1.8.0.jar
ln -s $(build-classpath commons-beanutils) .
#WEB-INF/lib/commons-chain-1.2.jar
ln -s $(build-classpath commons-chain) .
#WEB-INF/lib/commons-collections-3.1.jar
ln -s $(build-classpath commons-collections) .
#WEB-INF/lib/commons-digester-1.8.jar
ln -s $(build-classpath commons-digester) .
#WEB-INF/lib/commons-logging-1.0.4.jar
ln -s $(build-classpath commons-logging) .
#WEB-INF/lib/commons-validator-1.3.1.jar
ln -s $(build-classpath commons-validator) .
#WEB-INF/lib/log4j-1.2.12.jar
ln -s $(build-classpath log4j) .
#WEB-INF/lib/logkit-1.0.1.jar
ln -s $(build-classpath excalibur/avalon-logkit) .
#WEB-INF/lib/mail-1.4.jar
ln -s $(build-classpath javamail_1_4_api) .
#WEB-INF/lib/oro-2.0.8.jar
ln -s $(build-classpath jakarta-oro) .
#WEB-INF/lib/struts-core-1.3.10.jar
ln -s %{_javadir}/struts-core.jar .
#WEB-INF/lib/struts-extras-1.3.10.jar
ln -s %{_javadir}/struts-extras.jar .
#WEB-INF/lib/struts-mailreader-dao-1.3.10.jar
ln -s %{_javadir}/struts-mailreader-dao.jar .
#WEB-INF/lib/struts-taglib-1.3.10.jar
ln -s %{_javadir}/struts-taglib.jar .
rm $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-mailreader*.war
zip -q -r $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-mailreader.war .
popd
mkdir scripting-mailreader.war
pushd scripting-mailreader.war
unzip -qq $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-scripting-mailreader*.war
rm -v WEB-INF/lib/*
#WEB-INF/lib/ant-1.7.0.jar
ln -s $(build-classpath ant) .
#WEB-INF/lib/ant-launcher-1.7.0.jar
ln -s $(build-classpath ant-launcher) .
#WEB-INF/lib/antlr-2.7.2.jar
ln -s $(build-classpath antlr) .
#WEB-INF/lib/avalon-framework-4.1.3.jar
ln -s $(build-classpath excalibur/avalon-framework) .
#WEB-INF/lib/bsf-2.3.0.jar
ln -s $(build-classpath bsf) .
#WEB-INF/lib/commons-beanutils-1.8.0.jar
ln -s $(build-classpath commons-beanutils) .
#WEB-INF/lib/commons-chain-1.2.jar
ln -s $(build-classpath commons-chain) .
#WEB-INF/lib/commons-collections-3.1.jar
ln -s $(build-classpath commons-collections) .
#WEB-INF/lib/commons-digester-1.8.jar
ln -s $(build-classpath commons-digester) .
#WEB-INF/lib/commons-logging-1.0.4.jar
ln -s $(build-classpath commons-logging) .
#WEB-INF/lib/commons-validator-1.3.1.jar
ln -s $(build-classpath commons-validator) .
#WEB-INF/lib/groovy-all-1.0-jsr-04.jar
ln -s $(build-classpath groovy15) .
#WEB-INF/lib/jline-0.9.94.jar
ln -s $(build-classpath jline) .
#WEB-INF/lib/log4j-1.2.12.jar
ln -s $(build-classpath log4j) .
#WEB-INF/lib/logkit-1.0.1.jar
ln -s $(build-classpath excalibur/avalon-logkit) .
#WEB-INF/lib/mail-1.4.jar
ln -s $(build-classpath javamail_1_4_api) .
#WEB-INF/lib/oro-2.0.8.jar
ln -s $(build-classpath jakarta-oro) .
#WEB-INF/lib/struts-core-1.3.10.jar
ln -s %{_javadir}/struts-core.jar .
#WEB-INF/lib/struts-extras-1.3.10.jar
ln -s %{_javadir}/struts-extras.jar .
#WEB-INF/lib/struts-mailreader-dao-1.3.10.jar
ln -s %{_javadir}/struts-mailreader-dao.jar .
#WEB-INF/lib/struts-scripting-1.3.10.jar
ln -s %{_javadir}/struts-scripting.jar .
#WEB-INF/lib/struts-taglib-1.3.10.jar
ln -s %{_javadir}/struts-taglib.jar .
rm $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-scripting-mailreader*.war
zip -q -r $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/struts-scripting-mailreader.war .
popd
popd
rm -rf struts-%{version}/apps
mkdir -p struts-%{version}/apps
cp -p $RPM_BUILD_DIR/%{name}-%{version}/src/assembly/target/apps/*.war struts-%{version}/apps/
rm src/assembly/target/assembly/out/struts-%{version}-apps.zip
zip -q -r src/assembly/target/assembly/out/struts-%{version}-apps.zip struts-%{version}/apps/
%endif # apps

%if %with zips
install -dm 755 %{buildroot}/%{_javadir}/jbossas-fordev/
%{__install} -p -m 0644 src/assembly/target/assembly/out/struts-%{version}-all.zip %{buildroot}%{_javadir}/jbossas-fordev/%{name}-%{version}-all.zip
%{__install} -p -m 0644 src/assembly/target/assembly/out/struts-%{version}-lib.zip %{buildroot}%{_javadir}/jbossas-fordev/%{name}-%{version}-lib.zip
%if %with apps
%{__install} -p -m 0644 src/assembly/target/assembly/out/struts-%{version}-apps.zip %{buildroot}%{_javadir}/jbossas-fordev/%{name}-%{version}-apps.zip
%endif
%{__install} -p -m 0644 src/assembly/target/assembly/out/struts-%{version}-src.zip %{buildroot}%{_javadir}/jbossas-fordev/%{name}-%{version}-src.zip
%{__install} -p -m 0644 src/assembly/target/assembly/out/struts-%{version}-docs.zip %{buildroot}%{_javadir}/jbossas-fordev/%{name}-%{version}-docs.zip
%endif

%if %with manual
rm -rf docs-tmp/
mkdir docs-tmp/
unzip -qq src/assembly/target/assembly/out/struts-%{version}-docs.zip -d docs-tmp/
install -dm 755 %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr docs-tmp/struts-%{version}/* %{buildroot}%{_docdir}/%{name}-%{version}
rm -Rf %{buildroot}%{_docdir}/%{name}-%{version}/docs/apidocs
pushd %{buildroot}%{_docdir}/%{name}-%{version}/docs/
ln -s %{_javadocdir}/%{name} apidocs
popd
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif
rm -rf $RPM_BUILD_ROOT/var/lib/tomcat?/webapps/struts-documentation/download.cgi

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%dir %{_datadir}/%{name}
#%{_datadir}/%{name}/struts-config_1_0.dtd
#%{_datadir}/%{name}/struts-config_1_1.dtd
#%{_datadir}/%{name}/struts-config_1_2.dtd
#%{_datadir}/%{name}/struts-config_1_3.dtd
#%{_datadir}/%{name}/tiles-config_1_1.dtd
#%{_datadir}/%{name}/tiles-config_1_3.dtd
%{_datadir}/%{name}/struts-bean-el.tld
%{_datadir}/%{name}/struts-bean.tld
%{_datadir}/%{name}/struts-faces.tld
%{_datadir}/%{name}/struts-html-el.tld
%{_datadir}/%{name}/struts-html.tld
%{_datadir}/%{name}/struts-logic-el.tld
%{_datadir}/%{name}/struts-logic.tld
%{_datadir}/%{name}/struts-nested.tld
%{_datadir}/%{name}/struts-tiles-el.tld
%{_datadir}/%{name}/struts-tiles.tld
%{_datadir}/%{name}/validator-rules-compressed.xml
%{_datadir}/%{name}/validator-rules.xml
#%{_datadir}/%{name}/web-app_2_3.dtd
%if %with apps
%dir %{_datadir}/%{name}/apps
%dir %{_javadir}/%{name}-apps
%{_datadir}/maven2/poms/JPP-%{name}-apps.pom
%endif
%{_datadir}/maven2/poms/JPP-%{name}-assembly.pom
%{_datadir}/maven2/poms/JPP-%{name}-it-apps.pom
%{_datadir}/maven2/poms/JPP-%{name}-it.pom
%{_datadir}/maven2/poms/JPP-%{name}-master.pom
%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%if %with manual
%files manual
%doc %{_docdir}/%{name}-%{version}
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files core
%{_javadir}/%{name}-core-%{version}.jar
%{_javadir}/%{name}-core.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-core-%{version}.jar.*
%endif

%if %without coreonly
%files el
%{_javadir}/%{name}-el-%{version}.jar
%{_javadir}/%{name}-el.jar
%{_datadir}/maven2/poms/JPP-%{name}-el.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-el-%{version}.jar.*
%endif

%files extras
%{_javadir}/%{name}-extras-%{version}.jar
%{_javadir}/%{name}-extras.jar
%{_datadir}/maven2/poms/JPP-%{name}-extras.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-extras-%{version}.jar.*
%endif

%files faces
%{_javadir}/%{name}-faces-%{version}.jar
%{_javadir}/%{name}-faces.jar
%{_datadir}/maven2/poms/JPP-%{name}-faces.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-faces-%{version}.jar.*
%endif

%files mailreader-dao
%{_javadir}/%{name}-mailreader-dao-%{version}.jar
%{_javadir}/%{name}-mailreader-dao.jar
%{_datadir}/maven2/poms/JPP-%{name}-mailreader-dao.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-mailreader-dao-%{version}.jar.*
%endif

%files scripting
%{_javadir}/%{name}-scripting-%{version}.jar
%{_javadir}/%{name}-scripting.jar
%{_datadir}/maven2/poms/JPP-%{name}-scripting.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-scripting-%{version}.jar.*
%endif

%files taglib
%{_javadir}/%{name}-taglib-%{version}.jar
%{_javadir}/%{name}-taglib.jar
%{_datadir}/maven2/poms/JPP-%{name}-taglib.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-taglib-%{version}.jar.*
%endif

%files tiles
%{_javadir}/%{name}-tiles-%{version}.jar
%{_javadir}/%{name}-tiles.jar
%{_datadir}/maven2/poms/JPP-%{name}-tiles.pom
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-tiles-%{version}.jar.*
%endif
%endif # coreonly

%if %with apps
%files webapp-blank
%{_datadir}/%{name}/apps/blank.war
%{_datadir}/maven2/poms/JPP.%{name}-apps-blank.pom

%files webapp-cookbook
%{_datadir}/%{name}/apps/cookbook.war
%{_datadir}/maven2/poms/JPP.%{name}-apps-cookbook.pom

%files webapp-el-example
%{_datadir}/%{name}/apps/el-example.war
%{_datadir}/maven2/poms/JPP.%{name}-apps-el-example.pom

%files webapp-examples
%{_datadir}/%{name}/apps/examples.war
%{_datadir}/maven2/poms/JPP.%{name}-apps-examples.pom

%files webapps-faces
%{_datadir}/%{name}/apps/faces-example1.war
%{_datadir}/%{name}/apps/faces-example2.war
%{_datadir}/maven2/poms/JPP.%{name}-apps-faces-example1.pom
%{_datadir}/maven2/poms/JPP.%{name}-apps-faces-example2.pom

%files webapp-mailreader
%{_datadir}/%{name}/apps/mailreader.war
%{_datadir}/maven2/poms/JPP.%{name}-apps-mailreader.pom

%files webapp-scripting-mailreader
%{_datadir}/%{name}/apps/scripting-mailreader.war
%{_datadir}/maven2/poms/JPP.%{name}-apps-scripting-mailreader.pom
%endif # apps

%if %with zips
%files zip
%defattr(0644,jboss,jboss,0755)
%dir %{_javadir}/jbossas-fordev
%{_javadir}/jbossas-fordev/%{name}-%{version}-all.zip
%{_javadir}/jbossas-fordev/%{name}-%{version}-lib.zip
%if %with apps
%{_javadir}/jbossas-fordev/%{name}-%{version}-apps.zip
%endif
%{_javadir}/jbossas-fordev/%{name}-%{version}-docs.zip

%files src-zip
%defattr(0644,jboss,jboss,0755)
%dir %{_javadir}/jbossas-fordev
%{_javadir}/jbossas-fordev/%{name}-%{version}-src.zip
%endif

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.10-alt2_2jpp6
- fixed build with java 7

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3.10-alt1_2jpp6
- new version

* Fri Mar 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.8-alt2_2jpp5
- build with checkstyle4

* Sun Mar 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3.8-alt1_2jpp5
- fixed repocop warnings

* Fri Mar 14 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt4_5jpp1.7
- disabled struts-tomcat4

* Wed Sep 12 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt3_5jpp1.7
- rebuild to remove duplicate struts

* Sat Aug 11 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt2_5jpp1.7
- converted from JPackage by jppimport script

* Fri Aug 10 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt1_5jpp1.7
- new version

* Thu Apr 19 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.2.6-alt4
- Built with explicit java-1.5.0

* Wed Mar 22 2006 Vladimir Lettiev <crux@altlinux.ru> 1.2.6-alt3
- Fix build with j2se-1.5

* Wed Apr 06 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2.6-alt2
- packaged webapps for tomcats

* Tue Apr 05 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Tue Apr 05 2005 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt1
- Initial build for ALT Linux Sisyphus

