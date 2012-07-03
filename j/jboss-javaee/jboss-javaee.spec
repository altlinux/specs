Packager: Igor Vlasenko <viy@altlinux.ru>
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

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/jboss/jboss-javaee/%{javaee_namedversion}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define gcj_support 0

%define javaee_namedversion      5.0.1.GA
%define ejb_namedversion         3.0.0.GA
%define jacc_namedversion        1.1.0.GA
%define jad_namedversion         1.2.0.GA
%define jaspi_namedversion       1.0.0.GA
%define jaxr_namedversion        1.0.0.GA
%define jca_namedversion         1.5.0.GA
%define jms_namedversion         1.1.0.GA
%define transaction_namedversion 1.0.1.GA

Name:           jboss-javaee
Version:        5.0.1
Release:        alt2_2jpp6
Epoch:          0
Summary:        JBoss JavaEE 5.0 Aggregate
License:        LGPLv2+
URL:            http://www.jboss.org/
Group:          Development/Java
# svn -q export http://anonsvn.jboss.org/repos/jbossas/projects/javaee/tags/5.0.1.GA/ jboss-javaee-5.0.1 && tar cjf jboss-javaee-5.0.1.tar.bz2 jboss-javaee-5.0.1
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-component-info.xml
Source4:        %{name}-org-jboss-javaee-component-info.xml
Source5:        %{name}-jboss-jboss-jaspi-api-component-info.xml
Requires: %{name}-poms = %{epoch}:%{version}-%{release}
BuildRequires: jboss-common-core >= 0:2.2.8
BuildRequires: jboss-common-logging-spi >= 0:2.0.5
BuildRequires: jboss-parent
BuildRequires: jbossweb
# FIXME: (dwalluck): 3.0.4.GA listed in POM
BuildRequires: jbossws-native >= 0:3.0.1
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: junit
BuildRequires: maven-jboss-deploy-plugin
BuildRequires: maven-release
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-default-skin
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-site
BuildRequires: maven2-plugin-source
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-report-maven-plugin
BuildRequires: mojo-maven2-plugin-taglist
BuildArch:      noarch

%description
The JBoss JavaEE API classes.

%package poms
Summary:        POM files for jboss-javaee
Group:          Development/Java
Requires(post): jpackage-utils >= 1.7.5
Requires(postun): jpackage-utils >= 1.7.5

%description poms
The Project Object Model files for the jboss-javaee modules.

%package -n jboss-ejb-3.0-api
Summary:        JBoss EJB 3.0 API
Group:          Development/Java
Requires: %{name}-poms = %{epoch}:%{version}-%{release}
Requires: jboss-transaction-1.0.1-api
Requires(preun): alternatives >= 0:0.4
Requires(post): alternatives >= 0:0.4
Provides:       ejb = 0:3.0
Provides:       ejb_3_0_api
Provides:       ejb_api = 0:3.0

%description -n jboss-ejb-3.0-api
The Java EJB 3.0 API classes.

%package -n jboss-jacc-1.1-api
Summary:        JBoss JACC 1.1 API
Group:          Development/Java
Requires: %{name}-poms = %{epoch}:%{version}-%{release}
Requires: jbossweb2-servlet-2.5-api
Requires(preun): alternatives >= 0:0.4
Requires(post): alternatives >= 0:0.4
Provides:       jacc_1_1_api
Provides:       jacc_api = 0:1.1

%description -n jboss-jacc-1.1-api
The Java Authorization Contract for Containers 1.1 API classes.

%package -n jboss-jad-1.2-api
Summary:        JBoss JAD 1.2 API
Group:          Development/Java
Requires: %{name}-poms = %{epoch}:%{version}-%{release}
Requires(preun): alternatives >= 0:0.4
Requires(post): alternatives >= 0:0.4
Provides:       jad_1_2_api
Provides:       jad_api = 0:1.2

%description -n jboss-jad-1.2-api
The JavaEE Application Deployment 1.2 API classes.

%package -n jboss-jaspi-1.0-api
Summary:        JBoss JASPI 1.0 API
Group:          Development/Java
Requires: %{name}-poms = %{epoch}:%{version}-%{release}
Requires(preun): alternatives >= 0:0.4
Requires(post): alternatives >= 0:0.4
Provides:       jaspi_1_0_api
Provides:       jaspi_api = 0:1.0

%description -n jboss-jaspi-1.0-api
The Java Authentication SPI for Containers 1.0-PR API classes.

%package -n jboss-jaxr-1.0-api
Summary:        JBoss JAXR 1.0 API
Group:          Development/Java
Requires: %{name}-poms = %{epoch}:%{version}-%{release}
Requires: jaf_1_0_2_api
Requires(preun): alternatives >= 0:0.4
Requires(post): alternatives >= 0:0.4
Provides:       jaxr = 0:1.0
Provides:       jaxr_1_0_api
Provides:       jaxr_api = 0:1.0

%description -n jboss-jaxr-1.0-api
The Java API for XML Registries 1.0 API classes.

%package -n jboss-jca-1.5-api
Summary:        JBoss JCA 1.5 API
Group:          Development/Java
Requires: %{name}-poms = %{epoch}:%{version}-%{release}
Requires(preun): alternatives >= 0:0.4
Requires(post): alternatives >= 0:0.4
Provides:       j2ee-connector = 0:1.5
Provides:       j2ee_connector_1_5_api
Provides:       j2ee_connector_api = 0:1.5
Provides:       jca_1_5_api
Provides:       jca_api = 0:1.5

%description -n jboss-jca-1.5-api
The J2EE Connector Architecture 1.5 API classes.

%package -n jboss-jms-1.1-api
Summary:        JBoss JMS 1.1 API
Group:          Development/Java
Requires: %{name}-poms = %{epoch}:%{version}-%{release}
Requires(preun): alternatives >= 0:0.4
Requires(post): alternatives >= 0:0.4
Provides:       jms = 0:1.1
Provides:       jms_1_1_api
Provides:       jms_api = 0:1.1

%description -n jboss-jms-1.1-api
The Java Messaging Service 1.1 API classes.

%package -n jboss-transaction-1.0.1-api
Summary:        JBoss Transaction 1.0.1 API
Group:          Development/Java
Requires: %{name}-poms = %{epoch}:%{version}-%{release}
Requires(preun): alternatives >= 0:0.4
Requires(post): alternatives >= 0:0.4
Provides:       jta = 0:1.0.1B
Provides:       jta_1_0_1B_api
Provides:       jta_api = 0:1.0.1B

%description -n jboss-transaction-1.0.1-api
The Java Transaction 1.0.1 API classes.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
Requires: %{name}-javadoc = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description manual
%{summary}.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q 
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

cp %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%build
export LANG=en_US.ISO8859-1

export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
export M2_SETTINGS=$(pwd)/settings.xml
mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $M2_SETTINGS \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Daggregate=true \
        install javadoc:javadoc 
#	site


%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

%add_to_maven_depmap org.jboss.javaee jboss-javaee-parent %{javaee_namedversion} JPP jboss-javaee-parent
install -m 644 build/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jboss-javaee-parent.pom

%add_to_maven_depmap org.jboss.javaee jboss-javaee %{javaee_namedversion} JPP jboss-javaee
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jboss-javaee.pom
install -m 644 target/jboss-javaee.jar \
           $RPM_BUILD_ROOT%{_javadir}/jboss-javaee-5-apis-%{version}.jar
ln -s jboss-javaee-5-apis-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jboss-javaee-%{version}.jar

%add_to_maven_depmap org.jboss.javaee jboss-ejb-api %{ejb_namedversion} JPP jboss-ejb-api
install -m 644 jboss-ejb-api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jboss-ejb-api.pom
install -m 644 jboss-ejb-api/target/jboss-ejb-api.jar \
           $RPM_BUILD_ROOT%{_javadir}/jboss-ejb-3.0-api-%{version}.jar
ln -s jboss-ejb-3.0-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jboss-ejb-api-%{version}.jar
touch $RPM_BUILD_ROOT%{_javadir}/ejb.jar
touch $RPM_BUILD_ROOT%{_javadir}/ejb_api.jar
touch $RPM_BUILD_ROOT%{_javadir}/ejb_3_0_api.jar

%add_to_maven_depmap org.jboss.javaee jboss-jacc-api %{jacc_namedversion} JPP jboss-jacc-api
install -m 644 jboss-jacc-api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jboss-jacc-api.pom
install -m 644 jboss-jacc-api/target/jboss-jacc-api.jar \
           $RPM_BUILD_ROOT%{_javadir}/jboss-jacc-1.1-api-%{version}.jar
ln -s jboss-jacc-1.1-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jboss-jacc-api-%{version}.jar
touch $RPM_BUILD_ROOT%{_javadir}/jacc_api.jar
touch $RPM_BUILD_ROOT%{_javadir}/jacc_1_1_api.jar

%add_to_maven_depmap org.jboss.javaee jboss-jad-api %{jad_namedversion} JPP jboss-jad-api
install -m 644 jboss-jad-api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jboss-jad-api.pom
install -m 644 jboss-jad-api/target/jboss-jad-api.jar \
           $RPM_BUILD_ROOT%{_javadir}/jboss-jad-1.2-api-%{version}.jar
ln -s jboss-jad-1.2-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jboss-jad-api-%{version}.jar
touch $RPM_BUILD_ROOT%{_javadir}/jad_api.jar
touch $RPM_BUILD_ROOT%{_javadir}/jad_1_2_api.jar

%add_to_maven_depmap org.jboss.javaee jboss-jaspi-api %{jaspi_namedversion} JPP jboss-jaspi-api
install -m 644 jboss-jaspi-api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jboss-jaspi-api.pom
install -m 644 jboss-jaspi-api/target/jboss-jaspi-api.jar \
           $RPM_BUILD_ROOT%{_javadir}/jboss-jaspi-1.0-api-%{version}.jar
ln -s jboss-jaspi-1.0-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jboss-jaspi-api-%{version}.jar
touch $RPM_BUILD_ROOT%{_javadir}/jaspi_api.jar
touch $RPM_BUILD_ROOT%{_javadir}/jaspi_1_0_api.jar

%add_to_maven_depmap org.jboss.javaee jboss-jaxr-api %{jaxr_namedversion} JPP jboss-jaxr-api
install -m 644 jboss-jaxr-api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jboss-jaxr-api.pom
install -m 644 jboss-jaxr-api/target/jboss-jaxr-api.jar \
           $RPM_BUILD_ROOT%{_javadir}/jboss-jaxr-1.0-api-%{version}.jar
ln -s jboss-jaxr-1.0-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jboss-jaxr-api-%{version}.jar
touch $RPM_BUILD_ROOT%{_javadir}/jaxr.jar
touch $RPM_BUILD_ROOT%{_javadir}/jaxr_api.jar
touch $RPM_BUILD_ROOT%{_javadir}/jaxr_1_0_api.jar

%add_to_maven_depmap org.jboss.javaee jboss-jca-api %{jca_namedversion} JPP jboss-jca-api
install -m 644 jboss-jca-api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jboss-jca-api.pom
install -m 644 jboss-jca-api/target/jboss-jca-api.jar \
           $RPM_BUILD_ROOT%{_javadir}/jboss-jca-1.5-api-%{version}.jar
ln -s jboss-jca-1.5-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jboss-jca-api-%{version}.jar
touch $RPM_BUILD_ROOT%{_javadir}/j2ee-connector.jar
touch $RPM_BUILD_ROOT%{_javadir}/j2ee_connector_api.jar
touch $RPM_BUILD_ROOT%{_javadir}/j2ee_connector_1_5_api.jar
touch $RPM_BUILD_ROOT%{_javadir}/jca_1_5_api.jar
touch $RPM_BUILD_ROOT%{_javadir}/jca_api.jar

%add_to_maven_depmap org.jboss.javaee jboss-jms-api %{jms_namedversion} JPP jboss-jms-api
install -m 644 jboss-jms-api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jboss-jms-api.pom
install -m 644 jboss-jms-api/target/jboss-jms-api.jar \
           $RPM_BUILD_ROOT%{_javadir}/jboss-jms-1.1-api-%{version}.jar
ln -s jboss-jms-1.1-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jboss-jms-api-%{version}.jar
touch $RPM_BUILD_ROOT%{_javadir}/jms.jar
touch $RPM_BUILD_ROOT%{_javadir}/jms_api.jar
touch $RPM_BUILD_ROOT%{_javadir}/jms_1_1_api.jar

%add_to_maven_depmap org.jboss.javaee jboss-transaction-api %{transaction_namedversion} JPP jboss-transaction-api
install -m 644 jboss-transaction-api/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-jboss-transaction-api.pom
install -m 644 jboss-transaction-api/target/jboss-transaction-api.jar \
           $RPM_BUILD_ROOT%{_javadir}/jboss-transaction-1.0.1-api-%{version}.jar
ln -s jboss-transaction-1.0.1-api-%{version}.jar  $RPM_BUILD_ROOT%{_javadir}/jboss-transaction-api-%{version}.jar
touch $RPM_BUILD_ROOT%{_javadir}/jta.jar
touch $RPM_BUILD_ROOT%{_javadir}/jta_api.jar
touch $RPM_BUILD_ROOT%{_javadir}/jta_1_0_1B_api.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
# FIXME: breaks -bi --short-circuit
rm -rf target/site/apidocs
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

## manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#cp target/site/license.html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#cp -prv target/site $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#(cd $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} && ln -s %{_javadocdir}/%{name}-%{version} apidocs)
#for spec in ejb jacc jad jaspi jaxr jca jms transaction; do
#    install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/${spec}-api
#    cp -pr jboss-${spec}-api/target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/${spec}-api
#done

%if %with repolib
%{__install} -d -m 755 %{buildroot}%{repodir}
%{__install} -d -m 755 %{buildroot}%{repodirlib}
%{__install} -p -m 644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{javaee_namedversion}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 755 %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE2} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/jboss-javaee.jar

%define repodir %{_javadir}/repository.jboss.com/org/jboss/javaee/%{ejb_namedversion}-brew
%{__install} -d -m 755 %{buildroot}%{repodir}
%{__install} -d -m 755 %{buildroot}%{repodirlib}
%{__install} -p -m 644 %{SOURCE4} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{ejb_namedversion}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 755 %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE2} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/jboss-ejb-3.0-api-%{version}.jar %{buildroot}%{repodirlib}/jboss-ejb-api.jar
%{__cp} -p %{buildroot}%{_javadir}/jboss-transaction-1.0.1-api-%{version}.jar %{buildroot}%{repodirlib}/jboss-transaction-api.jar
%{__cp} -p %{buildroot}%{_javadir}/jboss-jms-1.1-api-%{version}.jar %{buildroot}%{repodirlib}/jboss-jms-api.jar
%{__cp} -p %{buildroot}%{_javadir}/jboss-jca-1.5-api-%{version}.jar %{buildroot}%{repodirlib}/jboss-jca-api.jar
%{__cp} -p %{buildroot}%{_javadir}/jboss-jacc-1.1-api-%{version}.jar %{buildroot}%{repodirlib}/jboss-jacc-api.jar
%{__cp} -p %{buildroot}%{_javadir}/jboss-jad-1.2-api-%{version}.jar %{buildroot}%{repodirlib}/jboss-jad-api.jar

%define repodir %{_javadir}/repository.jboss.com/jboss/jboss-jaspi-api/%{jaspi_namedversion}-brew
%{__install} -d -m 755 %{buildroot}%{repodir}
%{__install} -d -m 755 %{buildroot}%{repodirlib}
%{__install} -p -m 644 %{SOURCE5} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{jaspi_namedversion}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 755 %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE2} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/jboss-jaspi-1.0-api-%{version}.jar %{buildroot}%{repodirlib}/jboss-jaspi-api.jar
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ejb_jboss-ejb-3.0-api<<EOF
%{_javadir}/ejb.jar	%{_javadir}/jboss-ejb-3.0-api.jar	30000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ejb_3_0_api_jboss-ejb-3.0-api<<EOF
%{_javadir}/ejb_3_0_api.jar	%{_javadir}/jboss-ejb-3.0-api.jar	30000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ejb_api_jboss-ejb-3.0-api<<EOF
%{_javadir}/ejb_api.jar	%{_javadir}/jboss-ejb-3.0-api.jar	30000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jacc_1_1_api_jboss-jacc-1.1-api<<EOF
%{_javadir}/jacc_1_1_api.jar	%{_javadir}/jboss-jacc-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jacc_api_jboss-jacc-1.1-api<<EOF
%{_javadir}/jacc_api.jar	%{_javadir}/jboss-jacc-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jad_1_2_api_jboss-jad-1.2-api<<EOF
%{_javadir}/jad_1_2_api.jar	%{_javadir}/jboss-jad-1.2-api.jar	10200
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jad_api_jboss-jad-1.2-api<<EOF
%{_javadir}/jad_api.jar	%{_javadir}/jboss-jad-1.2-api.jar	10200
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaspi_1_0_api_jboss-jaspi-1.0-api<<EOF
%{_javadir}/jaspi_1_0_api.jar	%{_javadir}/jboss-jaspi-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaspi_api_jboss-jaspi-1.0-api<<EOF
%{_javadir}/jaspi_api.jar	%{_javadir}/jboss-jaspi-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxr_1_0_api_jboss-jaxr-1.0-api<<EOF
%{_javadir}/jaxr_1_0_api.jar	%{_javadir}/jboss-jaxr-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxr_api_jboss-jaxr-1.0-api<<EOF
%{_javadir}/jaxr_api.jar	%{_javadir}/jboss-jaxr-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxr_jboss-jaxr-1.0-api<<EOF
%{_javadir}/jaxr.jar	%{_javadir}/jboss-jaxr-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jca_1_5_api_jboss-jca-1.5-api<<EOF
%{_javadir}/jca_1_5_api.jar	%{_javadir}/jboss-jca-1.5-api.jar	10500
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jca_api_jboss-jca-1.5-api<<EOF
%{_javadir}/jca_api.jar	%{_javadir}/jboss-jca-1.5-api.jar	10500
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee-connector_jboss-jca-1.5-api<<EOF
%{_javadir}/j2ee-connector.jar	%{_javadir}/jboss-jca-1.5-api.jar	10500
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee_connector_api_jboss-jca-1.5-api<<EOF
%{_javadir}/j2ee_connector_api.jar	%{_javadir}/jboss-jca-1.5-api.jar	10500
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/j2ee_connector_1_5_api_jboss-jca-1.5-api<<EOF
%{_javadir}/j2ee_connector_1_5_api.jar	%{_javadir}/jboss-jca-1.5-api.jar	10500
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jms_1_1_api_jboss-jms-1.1-api<<EOF
%{_javadir}/jms_1_1_api.jar	%{_javadir}/jboss-jms-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jms_api_jboss-jms-1.1-api<<EOF
%{_javadir}/jms_api.jar	%{_javadir}/jboss-jms-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jms_jboss-jms-1.1-api<<EOF
%{_javadir}/jms.jar	%{_javadir}/jboss-jms-1.1-api.jar	10100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jta_1_0_1_api_jboss-transaction-1.0.1-api<<EOF
%{_javadir}/jta_2_5_api.jar	%{_javadir}/jboss-transaction-1.0.1-api.jar	10001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jta_api_jboss-transaction-1.0.1-api<<EOF
%{_javadir}/jta_1_0_1B_api.jar	%{_javadir}/jboss-transaction-1.0.1-api.jar	10001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jta_api_jboss-transaction-1.0.1-api<<EOF
%{_javadir}/jta_api.jar	%{_javadir}/jboss-transaction-1.0.1-api.jar	10001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jta_jboss-transaction-1.0.1-api<<EOF
%{_javadir}/jta.jar	%{_javadir}/jboss-transaction-1.0.1-api.jar	10001
EOF

%files
#%{_docdir}/%{name}-%{version}/license.html
%{_javadir}/jboss-javaee-%{version}.jar
%{_javadir}/jboss-javaee.jar
%{_javadir}/jboss-javaee-5-apis-%{version}.jar
%{_javadir}/jboss-javaee-5-apis.jar
# hack; explicitly added docdir if not owned
#%doc %dir %{_docdir}/%{name}-%{version}

%files poms
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files -n jboss-ejb-3.0-api
%_altdir/ejb_api_jboss-ejb-3.0-api
%_altdir/ejb_3_0_api_jboss-ejb-3.0-api
%_altdir/ejb_jboss-ejb-3.0-api
%{_javadir}/jboss-ejb-3.0-api-%{version}.jar
%{_javadir}/jboss-ejb-3.0-api.jar
%{_javadir}/jboss-ejb-api-%{version}.jar
%{_javadir}/jboss-ejb-api.jar
%exclude %{_javadir}/ejb.jar
%exclude %{_javadir}/ejb_api.jar
%exclude %{_javadir}/ejb_3_0_api.jar

%files -n jboss-jacc-1.1-api
%_altdir/jacc_api_jboss-jacc-1.1-api
%_altdir/jacc_1_1_api_jboss-jacc-1.1-api
%{_javadir}/jboss-jacc-1.1-api-%{version}.jar
%{_javadir}/jboss-jacc-1.1-api.jar
%{_javadir}/jboss-jacc-api-%{version}.jar
%{_javadir}/jboss-jacc-api.jar
%exclude %{_javadir}/jacc_api.jar
%exclude %{_javadir}/jacc_1_1_api.jar

%files -n jboss-jad-1.2-api
%_altdir/jad_api_jboss-jad-1.2-api
%_altdir/jad_1_2_api_jboss-jad-1.2-api
%{_javadir}/jboss-jad-1.2-api-%{version}.jar
%{_javadir}/jboss-jad-1.2-api.jar
%{_javadir}/jboss-jad-api-%{version}.jar
%{_javadir}/jboss-jad-api.jar
%exclude %{_javadir}/jad_api.jar
%exclude %{_javadir}/jad_1_2_api.jar

%files -n jboss-jaspi-1.0-api
%_altdir/jaspi_api_jboss-jaspi-1.0-api
%_altdir/jaspi_1_0_api_jboss-jaspi-1.0-api
%{_javadir}/jboss-jaspi-1.0-api-%{version}.jar
%{_javadir}/jboss-jaspi-1.0-api.jar
%{_javadir}/jboss-jaspi-api-%{version}.jar
%{_javadir}/jboss-jaspi-api.jar
%exclude %{_javadir}/jaspi_api.jar
%exclude %{_javadir}/jaspi_1_0_api.jar

%files -n jboss-jaxr-1.0-api
%_altdir/jaxr_jboss-jaxr-1.0-api
%_altdir/jaxr_api_jboss-jaxr-1.0-api
%_altdir/jaxr_1_0_api_jboss-jaxr-1.0-api
%{_javadir}/jboss-jaxr-1.0-api-%{version}.jar
%{_javadir}/jboss-jaxr-1.0-api.jar
%{_javadir}/jboss-jaxr-api-%{version}.jar
%{_javadir}/jboss-jaxr-api.jar
%exclude %{_javadir}/jaxr.jar
%exclude %{_javadir}/jaxr_1_0_api.jar
%exclude %{_javadir}/jaxr_api.jar

%files -n jboss-jca-1.5-api
%_altdir/j2ee_connector_1_5_api_jboss-jca-1.5-api
%_altdir/j2ee_connector_api_jboss-jca-1.5-api
%_altdir/j2ee-connector_jboss-jca-1.5-api
%_altdir/jca_api_jboss-jca-1.5-api
%_altdir/jca_1_5_api_jboss-jca-1.5-api
%{_javadir}/jboss-jca-1.5-api-%{version}.jar
%{_javadir}/jboss-jca-1.5-api.jar
%{_javadir}/jboss-jca-api-%{version}.jar
%{_javadir}/jboss-jca-api.jar
%exclude %{_javadir}/j2ee-connector.jar
%exclude %{_javadir}/j2ee_connector_1_5_api.jar
%exclude %{_javadir}/j2ee_connector_api.jar
%exclude %{_javadir}/jca_1_5_api.jar
%exclude %{_javadir}/jca_api.jar

%files -n jboss-jms-1.1-api
%_altdir/jms_jboss-jms-1.1-api
%_altdir/jms_api_jboss-jms-1.1-api
%_altdir/jms_1_1_api_jboss-jms-1.1-api
%{_javadir}/jboss-jms-1.1-api-%{version}.jar
%{_javadir}/jboss-jms-1.1-api.jar
%{_javadir}/jboss-jms-api-%{version}.jar
%{_javadir}/jboss-jms-api.jar
%exclude %{_javadir}/jms.jar
%exclude %{_javadir}/jms_1_1_api.jar
%exclude %{_javadir}/jms_api.jar

%files -n jboss-transaction-1.0.1-api
%_altdir/jta_jboss-transaction-1.0.1-api
%_altdir/jta_api_jboss-transaction-1.0.1-api
%_altdir/jta_api_jboss-transaction-1.0.1-api
%_altdir/jta_1_0_1_api_jboss-transaction-1.0.1-api
%{_javadir}/jboss-transaction-1.0.1-api-%{version}.jar
%{_javadir}/jboss-transaction-1.0.1-api.jar
%{_javadir}/jboss-transaction-api-%{version}.jar
%{_javadir}/jboss-transaction-api.jar
%exclude %{_javadir}/jta.jar
%exclude %{_javadir}/jta_1_0_1B_api.jar
%exclude %{_javadir}/jta_api.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

#%files manual
#%doc %{_docdir}/%{name}-%{version}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt2_2jpp6
- built with patched assembly plugin

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt1_2jpp6
- new version

