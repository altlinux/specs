# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# Copyright (c) 2000-2011, JPackage Project
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

# If you want to build with hibernate2 support
# give rpmbuild option '--with hibernate2'

%define with_hibernate2 %{?_with_hibernate2:1}%{!?_with_hibernate2:0}
%define without_hibernate2 %{!?_with_hibernate2:1}%{?_with_hibernate2:0}



Name:           spring
Summary:        Spring J2EE Framework
Url:            http://www.springframework.org/
Version:        1.2.9
Release:        alt11_4jpp6
Epoch:          0
License:        Apache Software License 2.0
Group:          Development/Java
Source0:        %{name}-framework-%{version}.zip
Source1:        http://repo1.maven.org/maven2/org/springframework/spring/1.2.9/spring-1.2.9.pom
Source2:        http://repo1.maven.org/maven2/org/springframework/spring-aop/1.2.9/spring-aop-1.2.9.pom
Source3:        http://repo1.maven.org/maven2/org/springframework/spring-beans/1.2.9/spring-beans-1.2.9.pom
Source4:        http://repo1.maven.org/maven2/org/springframework/spring-context/1.2.9/spring-context-1.2.9.pom
Source5:        http://repo1.maven.org/maven2/org/springframework/spring-core/1.2.9/spring-core-1.2.9.pom
Source6:        http://repo1.maven.org/maven2/org/springframework/spring-dao/1.2.9/spring-dao-1.2.9.pom
Source7:        spring-full-1.2.9.pom
Source8:        http://repo1.maven.org/maven2/org/springframework/spring-hibernate/1.2.9/spring-hibernate-1.2.9.pom
Source9:        http://repo1.maven.org/maven2/org/springframework/spring-jdbc/1.2.9/spring-jdbc-1.2.9.pom
Source10:       http://repo1.maven.org/maven2/org/springframework/spring-mock/1.2.9/spring-mock-1.2.9.pom
Source11:       http://repo1.maven.org/maven2/org/springframework/spring-orm/1.2.9/spring-orm-1.2.9.pom
Source12:       spring-parent-1.2.9.pom
Source13:       http://repo1.maven.org/maven2/org/springframework/spring-remoting/1.2.9/spring-remoting-1.2.9.pom
Source14:       http://repo1.maven.org/maven2/org/springframework/spring-support/1.2.9/spring-support-1.2.9.pom
Source15:       http://repo1.maven.org/maven2/org/springframework/spring-web/1.2.9/spring-web-1.2.9.pom
Source16:       http://repo1.maven.org/maven2/org/springframework/spring-webmvc/1.2.9/spring-webmvc-1.2.9.pom

Patch0:         spring-1.2.7-FilterDefinitionFactoryBean.patch
Patch1:         spring-1.2.7-HibernateTemplate.patch
Patch2:         spring-1.2.7-IdTransferringMergeEventListener.patch
Patch3:         spring-1.2.7-LocalSessionFactoryBeanTests.patch
Patch4:         spring-1.2.7-SessionBrokerFactoryTests.patch
Patch5:         spring-1.2.7-PathMatchingResourcePatternResolverTests.patch
Patch6:         spring-1.2.7-HibernateTemplateTests.patch
Patch7:         spring-1.2.7-MBeanClientInterceptorTests.patch
Patch8:         spring-1.2.7-RemoteMBeanClientInterceptorTests.patch
Patch9:         spring-1.2.7-ConnectorServerFactoryBean.patch
Patch10:        spring-1.2.7-ConnectorServerFactoryBeanTests.patch
#Patch11:        spring-1.2.7-MBeanServerConnectionFactoryBeanTests.patch
Patch12:        spring-1.2.7-JdbcTemplate.patch
Patch13:        spring-1.2.7-DefaultJdoDialect.patch
Patch14:        spring-1.2.7-JdoTemplateTests.patch

# Patch15 sets mx4j logging to debug
Patch15:        spring-1.2.9-build_xml.patch
Patch16:        spring-1.2.7-set-debug-logging-for-tests.patch
Patch17:        spring-1.2.7-autodetectLazyMBeans_xml.patch

Patch19:        spring-1.2.9-JmxTestBean.patch
Patch20:        spring-java6-DriverManagerDataSource.patch
Patch21:        spring-java6-LazyConnectionDataSourceProxy.patch
Patch22:        spring-java6-TransactionAwareDataSourceProxy.patch
Patch23:        spring-java6-UserCredentialsDataSourceAdapter.patch
Patch24:        spring-java6-OracleLobHandler.patch
Patch25:        spring-LocalTransactionManagerLookup.patch
Patch26:        spring-TilesViewTests.patch
Patch27:        spring-SQLErrorCodesFactoryTests.patch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-junit
BuildRequires:  junit
BuildRequires:  antlr
BuildRequires:  aopalliance
BuildRequires:  asm
BuildRequires:  axis
BuildRequires:  burlap >= 0:3.0.8
BuildRequires:  c3p0 >= 0:0.9.0
BuildRequires:  cglib
BuildRequires:  apache-commons-attributes
BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-dbcp
BuildRequires:  apache-commons-digester
BuildRequires:  apache-commons-discovery
BuildRequires:  apache-commons-fileupload
BuildRequires:  apache-commons-httpclient
BuildRequires:  apache-commons-lang
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-pool
BuildRequires:  apache-commons-validator
BuildRequires:  jakarta-taglibs-standard
BuildRequires:  db-ojb
BuildRequires:  dom4j
BuildRequires:  easymock
BuildRequires:  easymock-classextension
BuildRequires:  ehcache
BuildRequires:  ejb
BuildRequires:  freemarker
BuildRequires:  hessian >= 0:3.0.8
%if %{with_hibernate2}
BuildRequires:  hibernate2
%endif
BuildRequires:  hibernate3
BuildRequires:  hibernate3-annotations
BuildRequires:  hsqldb
BuildRequires:  itext
BuildRequires:  j2ee-connector
BuildRequires:  jaf
BuildRequires:  jamonapi
BuildRequires:  jasperreports2
BuildRequires:  javamail-monolithic
BuildRequires:  jaxen
BuildRequires:  jboss4-connector
BuildRequires:  apache-jdo-2.0-api
BuildRequires:  jetty5
BuildRequires:  jexcelapi
BuildRequires:  jms
BuildRequires:  mx4j >= 0:3.0.1-2jpp
BuildRequires:  jotm
BuildRequires:  myfaces
BuildRequires:  jsp_2_0_api
BuildRequires:  jta
BuildRequires:  jakarta-poi >= 0:2.5.1
BuildRequires:  log4j
BuildRequires:  oro
BuildRequires:  qdox161
BuildRequires:  quartz
BuildRequires:  servlet_2_4_api
BuildRequires:  struts
BuildRequires:  struts-tiles
BuildRequires:  velocity14
BuildRequires:  velocity-tools12
BuildRequires:  xapool
BuildRequires:  xjavadoc


Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
%if %{gcj_support}
BuildRequires:    gnu-crypto
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info

%description
Spring is a layered Java/J2EE application framework, 
based on code published in Expert One-on-One J2EE 
Design and Development by Rod Johnson (Wrox, 2002). 

%package core
Summary:        Spring core
Group:          Development/Java
Requires:       %{name} = 0:%{version}-%{release}
Requires:       apache-commons-logging

%description core
Spring bean container, core utilities
Optionals: log4j

%package aop
Summary:        Spring aop
Group:          Development/Java
Requires:       %{name} = 0:%{version}-%{release}
Requires:       %{name}-core = 0:%{version}-%{release}
Requires:       aopalliance

%description aop
Spring AOP framework, source level metadata support
Optionals: cglib, apache-commons-attributes

%package beans
Summary:        Spring beans
Group:          Development/Java
Requires:       %{name} = 0:%{version}-%{release}
Requires:       %{name}-core = 0:%{version}-%{release}
Requires:       cglib

%description beans
%{summary}.

%package context
Summary:        Spring context
Group:          Development/Java
Requires:       %{name} = 0:%{version}-%{release}
Requires:       %{name}-core = 0:%{version}-%{release}

%description context
Spring application context, validation, UI support, mail,
JNDI, JMS, EJB, remoting, scheduling, caching
Optionals: velocity, freemarker, javamail, jms, ejb, axis,
hessian, burlap, quartz, ehcache

%package dao
Summary:        Spring dao
Group:          Development/Java
Requires:       %{name} = 0:%{version}-%{release}
Requires:       %{name}-core = 0:%{version}-%{release}

%description dao
Spring DAO support, transaction infrastructure, JDBC support
Optionals: spring-aop, jta

%package hibernate
Summary:        Spring hibernate
Group:          Development/Java
Requires:       %{name} = 0:%{version}-%{release}
Requires:       %{name}-core = 0:%{version}-%{release}
Requires:       hibernate3

%description hibernate
%{summary}.

%package jdbc
Summary:        Spring jdbc
Group:          Development/Java
Requires:       %{name} = 0:%{version}-%{release}
Requires:       %{name}-core = 0:%{version}-%{release}
Requires:       apache-commons-dbcp

%description jdbc
%{summary}.

%package orm
Summary:        Spring orm
Group:          Development/Java
Requires:       %{name} = 0:%{version}-%{release}
Requires:       %{name}-dao = 0:%{version}-%{release}

%description orm
Spring Hibernate support, JDO support, Apache OJB, iBATIS SQL Maps
Optionals: hibernate2, hibernate3, hibernate3-annotations, 
apache-jdo-2.0-api, db-ojb, j2ee-connector

%package remoting
Summary:        Spring remoting
Group:          Development/Java
Requires:       %{name} = 0:%{version}-%{release}
Requires:       %{name}-core = 0:%{version}-%{release}

%description remoting
%{summary}.

%package support
Summary:        Spring support
Group:          Development/Java
Requires:       %{name} = 0:%{version}-%{release}
Requires:       %{name}-core = 0:%{version}-%{release}

%description support
%{summary}.

%package web
Summary:        Spring web
Group:          Development/Java
Requires:       %{name} = 0:%{version}-%{release}
Requires:       %{name}-context = 0:%{version}-%{release}
Requires:       servlet_2_4_api

%description web
Spring web application support, multipart resolver, struts support,
web utilities
Optionals: jsp_2_0_api, jakarta-taglibs-standard, apache-commons-fileupload,
struts, struts-tiles

%package webmvc
Summary:        Spring webmvc
Group:          Development/Java
Requires:       %{name} = 0:%{version}-%{release}
Requires:       %{name}-web = 0:%{version}-%{release}

%description webmvc
Spring framework servlets, web MVC framework, web controllers, web views
Optionals: tiles, itext, poi

%package all
Summary:        Spring all except mocks
Group:          Development/Java
Requires:       %{name} = 0:%{version}-%{release}
Requires:       apache-commons-logging
Requires:       aopalliance
Requires:       servlet_2_4_api

%description all
Spring everything except mocks
Optionals: log4j, cglib, apache-commons-attributes
velocity, freemarker, javamail, jms, ejb, axis, hessian, 
burlap, quartz, ehcache, jta, hibernate2, hibernate3, 
hibernate3-annotations, apache-jdo-2.0-api, ojb, 
jsp_2_0_api, jakarta-taglibs-standard, apache-commons-fileupload,
tiles, itest, poi

%package mock
Summary:        Spring mock
Group:          Development/Java
Requires:       %{name} = 0:%{version}-%{release}
Requires:       %{name}-core = 0:%{version}-%{release}

%description mock
Spring JNDI mocks, Servlet API mocks

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%package demo
Summary:        Samples for %{name}
Group:          Development/Documentation
Requires:       %{name} = 0:%{version}-%{release}
Requires:       antlr
Requires:       axis
Requires:       dom4j
Requires:       jaxen
Requires:       ehcache
Requires:       hsqldb

%description demo
%{summary}.
Optionals: antlr, axis, dom4j, jaxen, ehcache, hsqldb

%prep
%setup -q -n %{name}-framework-%{version}
chmod -R go=u-w *
#find . -name "*.jar" -exec rm {} \;
for f in $(find . -name "*.jar"); do
    mv $f $f.no
done
rm src/org/springframework/jdbc/core/SqlRowSetResultSetExtractor.java
rm -rf src/org/springframework/orm/ibatis/
rm -rf test/org/springframework/orm/ibatis/

# patches related to compile against hibernate-3.1.X in src
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%if %{with_hibernate2}
# patches related to compile against hibernate-2.1.6 in test
%patch3 -b .sav3
%endif
## patches related to compile against toplink-10.1.3.0.0 in test
#%patch4 -b .sav4
# patches related to run against aopalliance-1.0 in test
%patch5 -b .sav5
# patches related to run against hibernate-3.1.X in test
%patch6 -b .sav6
# patches related to run against mx4j-3.0.1 in test
%patch7 -b .sav7
%patch8 -b .sav8
%patch9 -b .sav9
%patch10 -b .sav10
# patches related to runtime issues (race conditions) in test
#%patch11 -b .sav11
# patches related to rowsets unavailable
%patch12 -b .sav12
# patches related to apache-jdo-2.0
%patch13 -b .sav13
%patch14 -b .sav14
# temporary patches 
# may be also used to patch mx4j.log.priority in tests
# drop java option -XX:MaxPermSize=, will not work with other than sun
%patch15 -b .sav15
# patch tests mx4j log level to debug
#%patch16 -b .sav16
%patch17 -b .sav17

%patch19 -b .sav19
%patch20 -b .sav20
%patch21 -b .sav21
%patch22 -b .sav22
%patch23 -b .sav23
%patch24 -b .sav24
%patch25 -b .sav25
%patch26 -b .sav26
%patch27 -b .sav27

# optionally remove sources requiring hibernate2
%if %{without_hibernate2}
rm -rf src/org/springframework/orm/hibernate
rm -rf test/org/springframework/orm/hibernate
%endif
# remove sources requiring non-free stuff
rm -rf src/org/springframework/orm/toplink
rm -rf test/org/springframework/orm/toplink
rm -rf src/org/springframework/mail/cos
rm -rf src/org/springframework/web/multipart/cos
rm test/org/springframework/web/multipart/cos/CosMultipartResolverTests.java
rm test/org/springframework/mail/SimpleMailMessageTests.java
# directory foo expected by one test
mkdir foo

%build

mkdir -p lib
pushd lib

mkdir -p jetty
pushd jetty
ln -sf $(build-classpath jetty5/jetty5) .
popd

mkdir -p antlr
pushd antlr
ln -sf $(build-classpath antlr) .
popd

mkdir -p aopalliance
pushd aopalliance
ln -sf $(build-classpath aopalliance) .
popd

mkdir -p axis
pushd axis
ln -sf $(build-classpath axis/axis) .
ln -sf $(build-classpath axis/saaj) .
ln -sf $(build-classpath wsdl4j) .
popd

mkdir -p c3p0
pushd c3p0
ln -sf $(build-classpath c3p0) .
popd

mkdir -p caucho
pushd caucho
ln -sf $(build-classpath burlap) .
ln -sf $(build-classpath hessian) .
#
ln -sf $(build-classpath caucho-services) .
popd

mkdir -p cglib
pushd cglib
ln -sf $(build-classpath cglib) cglib-nodep-2.1_2.jar
ln -sf $(build-classpath asm/asm) .
popd

mkdir -p dom4j
pushd dom4j
ln -sf $(build-classpath dom4j) .
ln -sf $(build-classpath jaxen) .
popd

mkdir -p easymock
pushd easymock
ln -sf $(build-classpath easymock) .
ln -sf $(build-classpath easymock-classextension) .
popd

mkdir -p ehcache
pushd ehcache
ln -sf $(build-classpath ehcache) ehcache-1.1.jar
popd

mkdir -p freemarker
pushd freemarker
ln -sf $(build-classpath freemarker) .
popd

mkdir -p hibernate
pushd hibernate
ln -sf $(build-classpath hibernate3-core) hibernate3.jar
%if %{with_hibernate2}
ln -sf $(build-classpath hibernate2) hibernate2.jar
%endif
ln -sf $(build-classpath hibernate3-annotations) hibernate-annotations.jar
popd

mkdir -p hsqldb
pushd hsqldb
ln -sf $(build-classpath hsqldb) .
popd

mkdir -p itext
pushd itext
ln -sf $(build-classpath itext) itext-1.3.jar
popd
mkdir -p j2ee
pushd j2ee
ln -sf $(build-classpath jaf) activation.jar
ln -sf $(build-classpath j2ee-connector) connector.jar
ln -sf $(build-classpath ejb) .
ln -sf $(build-classpath axis/jaxrpc) .
ln -sf $(build-classpath jms) .
ln -sf $(build-classpath jsp_2_0_api) jspapi.jar
ln -sf $(build-classpath taglibs-core) jstl-core.jar
ln -sf $(build-classpath taglibs-standard) jstl.jar
ln -sf $(build-classpath jta) .
ln -sf $(build-classpath javamail) mail.jar
ln -sf $(build-classpath servlet_2_4_api) servlet-api.jar
#ln -sf $(build-classpath xml-commons-apis) xml-apis.jar
popd
mkdir -p endorsed
pushd endorsed
ln -sf $(build-classpath xerces-j2) xerces.jar
ln -sf $(build-classpath xml-commons-apis) xml-apis.jar
popd

mkdir -p jakarta-commons
pushd jakarta-commons
ln -sf $(build-classpath commons-attributes-api) .
ln -sf $(build-classpath commons-attributes-compiler) .
ln -sf $(build-classpath commons-beanutils) .
ln -sf $(build-classpath commons-codec) .
ln -sf $(build-classpath commons-collections) .
ln -sf $(build-classpath commons-dbcp) .
ln -sf $(build-classpath commons-digester) .
ln -sf $(build-classpath commons-discovery) .
ln -sf $(build-classpath commons-fileupload) .
ln -sf $(build-classpath commons-httpclient) .
ln -sf $(build-classpath commons-lang) .
ln -sf $(build-classpath commons-logging) .
ln -sf $(build-classpath commons-pool) .
ln -sf $(build-classpath commons-validator) .
ln -sf $(build-classpath qdox161) .
popd

mkdir -p jakarta-taglibs
pushd jakarta-taglibs
ln -sf $(build-classpath taglibs-standard) standard.jar
popd

mkdir -p jamon
pushd jamon
ln -sf $(build-classpath jamonapi) JAMon.jar
popd

mkdir -p jasperreports
pushd jasperreports
ln -sf $(build-classpath jasperreports2) jasperreports-1.0.3.jar
popd

mkdir -p jboss
pushd jboss
ln -sf $(build-classpath jboss4/jboss-common-jdbc-wrapper) .
popd

mkdir -p jdo
pushd jdo
ln -sf $(build-classpath apache-jdo-2.0-api) jdo2.jar
popd

mkdir -p jexcelapi
pushd jexcelapi
ln -sf $(build-classpath jexcelapi/jxl) jxl.jar
popd

mkdir -p jmx
pushd jmx
ln -sf $(build-classpath mx4j/mx4j)
ln -sf $(build-classpath mx4j/mx4j-impl)
ln -sf $(build-classpath mx4j/mx4j-jmx)
ln -sf $(build-classpath mx4j/mx4j-remote)
ln -sf $(build-classpath mx4j/mx4j-rimpl)
ln -sf $(build-classpath mx4j/mx4j-rjmx)
ln -sf $(build-classpath mx4j/mx4j-tools)
ln -sf $(build-classpath mx4j/mx4j-tools-extra)
popd

mkdir -p jotm
pushd jotm
ln -sf $(build-classpath jotm/jotm) .
ln -sf $(build-classpath xapool) .
popd

mkdir -p jsf
pushd jsf
ln -sf $(build-classpath myfaces/myfaces-jsf-api) jsf.jar
popd

mkdir -p log4j
pushd log4j
ln -sf $(build-classpath log4j) log4j-1.2.14.jar
popd

mkdir -p ojb
pushd ojb
ln -sf $(build-classpath db-ojb/db-ojb) db-ojb-1.0.4.jar
popd

mkdir -p oro
pushd oro
ln -sf $(build-classpath oro) jakarta-oro-2.0.8.jar
popd

mkdir -p poi
pushd poi
ln -sf $(build-classpath poi/poi) poi-2.5.1.jar
popd

mkdir -p quartz
pushd quartz
ln -sf $(build-classpath quartz) .
popd

mkdir -p struts
pushd struts
ln -sf $(build-classpath struts) .
ln -sf $(build-classpath struts-extras) .
ln -sf $(build-classpath struts-tiles) .
popd

mkdir -p velocity
pushd velocity
ln -sf $(build-classpath velocity-tools12-generic) velocity-tools-generic-1.1.jar
ln -sf $(build-classpath velocity-tools12-view) velocity-tools-view-1.1.jar
ln -sf $(build-classpath velocity14) velocity-1.4.jar
popd

mkdir -p xdoclet
pushd xdoclet
ln -sf $(build-classpath xjavadoc) xjavadoc-1.1.jar
popd
popd

export OPT_JAR_LIST="ant-launcher ant/ant-junit junit xjavadoc commons-collections commons-attributes-compiler qdox161"
#export ANT_OPTS="-Dmx4j.log.priority=debug"

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
    -Djava.endorsed.dir=lib/endorsed \
    alljars tests


%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

install -m 644 dist/%{name}-aop.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}/aop-%{version}.jar
install -m 644 dist/%{name}-beans.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}/beans-%{version}.jar
install -m 644 dist/%{name}-context.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}/context-%{version}.jar
install -m 644 dist/%{name}-core.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}/core-%{version}.jar
install -m 644 dist/%{name}-dao.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}/dao-%{version}.jar
install -m 644 dist/%{name}-hibernate.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}/hibernate-%{version}.jar
install -m 644 dist/%{name}-jdbc.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}/jdbc-%{version}.jar
install -m 644 dist/%{name}-mock.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}/mock-%{version}.jar
install -m 644 dist/%{name}-orm.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}/orm-%{version}.jar
install -m 644 dist/%{name}-remoting.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}/remoting-%{version}.jar
install -m 644 dist/%{name}-support.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}/support-%{version}.jar
install -m 644 dist/%{name}-web.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}/web-%{version}.jar
install -m 644 dist/%{name}-webmvc.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}/webmvc-%{version}.jar
install -m 644 dist/%{name}.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

%add_to_maven_depmap org.springframework %{name} %{version} JPP %{name}
%add_to_maven_depmap org.springframework %{name}-aop %{version} JPP/%{name} aop
%add_to_maven_depmap org.springframework %{name}-beans %{version} JPP/%{name} beans
%add_to_maven_depmap org.springframework %{name}-context %{version} JPP/%{name} context
%add_to_maven_depmap org.springframework %{name}-core %{version} JPP/%{name} core
%add_to_maven_depmap org.springframework %{name}-dao %{version} JPP/%{name} dao
# next is a dependency list
%add_to_maven_depmap org.springframework %{name}-full %{version} JPP/%{name} full
#
%add_to_maven_depmap org.springframework %{name}-hibernate %{version} JPP/%{name} hibernate
%add_to_maven_depmap org.springframework %{name}-jdbc %{version} JPP/%{name} jdbc
%add_to_maven_depmap org.springframework %{name}-mock %{version} JPP/%{name} mock
%add_to_maven_depmap org.springframework %{name}-orm %{version} JPP/%{name} orm
# next is the project parent
%add_to_maven_depmap org.springframework %{name}-parent %{version} JPP/%{name} parent
#
%add_to_maven_depmap org.springframework %{name}-remoting %{version} JPP/%{name} remoting
%add_to_maven_depmap org.springframework %{name}-support %{version} JPP/%{name} support
%add_to_maven_depmap org.springframework %{name}-web %{version} JPP/%{name} web
%add_to_maven_depmap org.springframework %{name}-webmvc %{version} JPP/%{name} webmvc

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}.pom
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-aop.pom
install -pm 644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-beans.pom
install -pm 644 %{SOURCE4} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-context.pom
install -pm 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-core.pom
install -pm 644 %{SOURCE6} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-dao.pom
# next is a dependency list
install -pm 644 %{SOURCE7} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-full.pom
#
install -pm 644 %{SOURCE8} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-hibernate.pom
install -pm 644 %{SOURCE9} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jdbc.pom
install -pm 644 %{SOURCE10} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-mock.pom
install -pm 644 %{SOURCE11} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-orm.pom
# next is the project parent
install -pm 644 %{SOURCE12} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-parent.pom
#
install -pm 644 %{SOURCE13} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-remoting.pom
install -pm 644 %{SOURCE14} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-support.pom
install -pm 644 %{SOURCE15} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-web.pom
install -pm 644 %{SOURCE16} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-webmvc.pom

# definitions
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc
install -m 644 dist/%{name}-beans.dtd \
       $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{name}-beans.dtd
install -m 644 dist/%{name}.ftl \
       $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{name}.ftl
install -m 644 dist/%{name}.tld \
       $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{name}.tld
install -m 644 dist/%{name}.vm \
       $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc/%{name}.vm

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf docs/api

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p license.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/samples
cp -pr samples/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/samples

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%dir %{_datadir}/%{name}-%{version}
%dir %{_datadir}/%{name}-%{version}/etc
%{_datadir}/%{name}-%{version}/etc/*
%{_docdir}/%{name}-%{version}/license.txt
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-*%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files core
%{_javadir}/%{name}/core*.jar

%files aop
%{_javadir}/%{name}/aop*.jar

%files beans
%{_javadir}/%{name}/beans*.jar

%files context
%{_javadir}/%{name}/context*.jar

%files dao
%{_javadir}/%{name}/dao*.jar

%files hibernate
%{_javadir}/%{name}/hibernate*.jar

%files jdbc
%{_javadir}/%{name}/jdbc*.jar

%files orm
%{_javadir}/%{name}/orm*.jar

%files remoting
%{_javadir}/%{name}/remoting*.jar

%files support
%{_javadir}/%{name}/support*.jar

%files web
%{_javadir}/%{name}/web-*.jar
%{_javadir}/%{name}/web.jar

%files webmvc
%{_javadir}/%{name}/webmvc*.jar

%files all
%{_javadir}/%{name}*.jar

%files mock
%{_javadir}/%{name}/mock*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/mock-*%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%files demo
%{_datadir}/%{name}-%{version}/samples

%changelog
* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt11_4jpp6
- fixed build

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt10_4jpp6
- built with java 6 due to abstract getParentLogger

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt9_4jpp6
- built with jasperreports2

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt8_4jpp6
- converted from JPackage by jppimport script

* Sun Feb 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt8_3jpp5
- fixed build

* Mon Feb 07 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt7_3jpp5
- build with hibernate32

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt6_3jpp5
- explicit selection of java5 compiler

* Thu May 21 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt5_3jpp5
- fixed build

* Sun Feb 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt4_3jpp5
- fixed build with maven 2.0.7

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt3_3jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt2_3jpp5
- fixed docdir ownership

* Tue Oct 21 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.9-alt1_3jpp5
- jpackage 5.0

