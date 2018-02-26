Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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

%bcond_with bootstrap

%define _with_repolib 1

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/jboss/messaging/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


%define reltag  SP3_CP01

Name:           jboss-messaging
Version:        1.4.0
Release:        alt1_1.SP3_CP01.5jpp5
Epoch:          0
Summary:        Enterprise Messaging for Java and the App Server
License:        LGPLv2+
Group:          Development/Java
URL:            http://labs.jboss.com/jbossmessaging/
# svn export http://anonsvn.jboss.org/repos/messaging/tags/JBossMessaging_1_4_0_SP3_CP01/ jboss-messaging
# tar czf jboss-messaging-1.4.0.SP3_CP01-src.tar.gz jboss-messaging
Source0:        jboss-messaging-1.4.0.SP3_CP01-src.tar.gz
Source1:	jboss-messaging-component-info.xml
Source2:        %{name}-libraries.ent
BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: ant-nodeps

BuildRequires: concurrent
BuildRequires: dom4j
BuildRequires: dtdparser
BuildRequires: ecj
BuildRequires: gnu-trove
BuildRequires: hsqldb
BuildRequires: jakarta-commons-el
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-modeler
BuildRequires: javacc3
BuildRequires: javassist
BuildRequires: jboss-aop
%if %with bootstrap
Requires: jboss4-j2ee
Requires: jboss4-jmx
Requires: jboss4-security
Requires: jboss4-system
Requires: jboss4-transaction
BuildRequires: jboss4-j2ee
BuildRequires: jboss4-jmx
BuildRequires: jboss4-security
BuildRequires: jboss4-system
BuildRequires: jboss4-transaction
%else
Requires: jbossas
BuildRequires: jbossas
%endif
BuildRequires: jboss-common
BuildRequires: jboss-profiler
BuildRequires: jboss-remoting
BuildRequires: jboss-serialization
#BuildRequires: jbossts
BuildRequires: jbossxb
BuildRequires: jgroups
BuildRequires: junit
BuildRequires: log4j
BuildRequires: qdox
BuildRequires: snmptrapappender
BuildRequires: tomcat5-admin-webapps
BuildRequires: tomcat5-common-lib
BuildRequires: tomcat5-jasper
BuildRequires: tomcat5-server-lib
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: xml-commons-resolver
BuildRequires: excalibur-avalon-framework
BuildRequires: batik
BuildRequires: fop
BuildRequires: saxon

Requires: jpackage-utils >= 0:1.6
Requires: concurrent
Requires: jboss-aop
Requires: jboss-common
Requires: jboss-remoting
Requires: jgroups


%description
JBoss Messaging is a high performance JMS provider in the JBoss Enterprise 
Middleware Stack (JEMS). It is a complete rewrite of JBossMQ, the legacy 
JBoss JMS provider.

%if %{with_repolib}
%package repolib
Summary:	 Artifacts to be uploaded to a repository library
Group:	         Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}

%package demo
Summary:        Usage examples for %{name}
Group:          Development/Documentation

%description demo
%{summary}

%prep
%setup -q -n %{name}
chmod -R go=u-w *

# FIXME: (dwalluck) These should be replaced (to build docs)
# FIXME: (dwalluck) jai is non-free
#find . -name '*.jar' | xargs -t %{__rm}
# ./tools/lib/jbossbuild.jar
rm ./lib/docbook-support/support/lib/avalon-framework-cvs-20020806.jar
# ./lib/docbook-support/support/lib/saxon-dbxsl-extensions.jar
# ./lib/docbook-support/support/lib/rowan-0.1.jar
rm ./lib/docbook-support/support/lib/batik.jar
# ./lib/docbook-support/support/lib/jai_codec.jar
rm ./lib/docbook-support/support/lib/fop.jar
rm ./lib/docbook-support/support/lib/saxon.jar
# ./lib/docbook-support/support/lib/jai_core.jar
%{__ln_s} $(build-classpath excalibur/avalon-framework) ./lib/docbook-support/support/lib/avalon-framework-cvs-20020806.jar
%{__ln_s} $(build-classpath batik) ./lib/docbook-support/support/lib/batik.jar
%{__ln_s} $(build-classpath fop) ./lib/docbook-support/support/lib/fop.jar
%{__ln_s} $(build-classpath saxon) ./lib/docbook-support/support/lib/saxon.jar

%if %{with_repolib}
sed -i 's/@VERSION@/%{version}.%{reltag}-brew/g' %{SOURCE1}
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{SOURCE1}
%endif

%if %with bootstrap
%{__rm} src/main/org/jboss/jms/server/recovery/MessagingXAResourceRecovery.java
%endif

%build
mkdir thirdparty

pushd thirdparty
mkdir -p apache-log4j/lib
ln -s $(build-classpath log4j) apache-log4j/lib/log4j.jar

mkdir -p apache-logging/lib
ln -s $(build-classpath commons-logging) apache-logging/lib/commons-logging.jar

mkdir -p apache-modeler/lib
ln -s $(build-classpath commons-modeler) apache-modeler/lib/commons-modeler.jar

mkdir -p apache-tomcat/lib
ln -s $(build-classpath tomcat5/catalina) apache-tomcat/lib/catalina.jar
ln -s $(build-classpath tomcat5/catalina-manager) apache-tomcat/lib/catalina-manager.jar
ln -s $(build-classpath tomcat5/catalina-optional) apache-tomcat/lib/catalina-optional.jar
ln -s $(build-classpath jasper5-compiler) apache-tomcat/lib/jasper-compiler.jar
ln -s $(build-classpath jdtcore) apache-tomcat/lib/jasper-compiler-jdt.jar
ln -s $(build-classpath jasper5-runtime) apache-tomcat/lib/jasper-runtime.ja
ln -s $(build-classpath tomcat5/naming-resources) apache-tomcat/lib/naming-resources.jar
ln -s $(build-classpath tomcat5/servlets-default) apache-tomcat/lib/servlets-default.jar
ln -s $(build-classpath tomcat5/servlets-invoker) apache-tomcat/lib/servlets-invoker.jar
ln -s $(build-classpath tomcat5/servlets-webdav) apache-tomcat/lib/servlets-webdav.jar
ln -s $(build-classpath tomcat5/tomcat-ajp) apache-tomcat/lib/tomcat-ajp.jar
ln -s $(build-classpath tomcat5/tomcat-apr) apache-tomcat/lib/tomcat-apr.jar
ln -s $(build-classpath tomcat5/tomcat-coyote) apache-tomcat/lib/tomcat-coyote.jar
ln -s $(build-classpath tomcat5/tomcat-http) apache-tomcat/lib/tomcat-http.jar
ln -s $(build-classpath tomcat5/tomcat-util) apache-tomcat/lib/tomcat-util.jar

mkdir -p apache-xerces/lib
ln -s $(build-classpath xerces-j2) apache-xerces/lib/xercesImpl.jar

mkdir -p apache-xml-commons/lib
ln -s $(build-classpath xml-commons-resolver) apache-xml-commons/lib/resolver.jar
ln -s $(build-classpath xml-commons-apis) apache-xml-commons/lib/xml-apis.jar

mkdir -p commons-el/lib
ln -s $(build-classpath commons-el) commons-el/lib/commons-el.jar

mkdir -p dom4j/lib
ln -s $(build-classpath dom4j) dom4j/lib/dom4j.jar

mkdir -p hsqldb/lib
ln -s $(build-classpath hsqldb) hsqldb/lib/hsqldb.jar

mkdir -p javassist/lib
ln -s $(build-classpath javassist) javassist/lib/javassist.jar
#javassist/lib/javassist-src.jar

mkdir -p jboss/aop/lib
#./jboss/aop/lib/common-softvaluehashmap.jar
ln -s $(build-classpath jboss-aop/jboss-aop) jboss/aop/lib/jboss-aop.jar
ln -s $(build-classpath jboss-aop/jboss-aop-jdk50-client) jboss/aop/lib/jboss-aop-jdk50-client.jar
ln -s $(build-classpath jboss-aop/jboss-aop-jdk50) jboss/aop/lib/jboss-aop-jdk50.jar
ln -s $(build-classpath jboss-aop/jdk14-pluggable-instrumentor) jboss/aop/lib/jdk14-pluggable-instrumentor.jar
ln -s $(build-classpath jboss-aop/jrockit-pluggable-instrumentor) jboss/aop/lib/jrockit-pluggable-instrumentor.jar
ln -s $(build-classpath jboss-aop/pluggable-instrumentor) jboss/aop/lib/pluggable-instrumentor.jar

mkdir -p jbossas/core-libs/lib
ln -s $(build-classpath jboss-common/jboss-common) jbossas/core-libs/lib/jboss-common.jar
ln -s $(build-classpath jboss/jboss-xml-binding) jbossas/core-libs/lib/jboss-xml-binding.jar
%if %with bootstrap
ln -s $(build-classpath jboss4/jboss-common-jdbc-wrapper) jbossas/core-libs/lib/jboss-common-jdbc-wrapper.jar
ln -s $(build-classpath jboss4/jbosscx-client) jbossas/core-libs/lib/jbosscx-client.jar
ln -s $(build-classpath jboss4/jboss-j2ee) jbossas/core-libs/lib/jboss-j2ee.jar
ln -s $(build-classpath jboss4/jboss) jbossas/core-libs/lib/jboss.jar
ln -s $(build-classpath jboss4/jboss-jca) jbossas/core-libs/lib/jboss-jca.jar
ln -s $(build-classpath jboss4/jboss-jmx) ./jbossas/core-libs/lib/jboss-jmx.jar
#./jbossas/core-libs/lib/jboss-local-jdbc.jar
ln -s $(build-classpath jboss4/jbosssx-client) jbossas/core-libs/lib/jbosssx-client.jar
ln -s $(build-classpath jboss4/jboss-system) jbossas/core-libs/lib/jboss-system.jar
ln -s $(build-classpath jboss4/jboss-transaction-client) jbossas/core-libs/lib/jboss-transaction-client.jar
#./jbossas/core-libs/lib/jms-ra.jar
ln -s $(build-classpath jboss4/jnp-client) jbossas/core-libs/lib/jnp-client.jar
%else
ln -s $(build-classpath jbossas/jboss-common-jdbc-wrapper) jbossas/core-libs/lib/jboss-common-jdbc-wrapper.jar
ln -s $(build-classpath jbossas/jbosscx-client) jbossas/core-libs/lib/jbosscx-client.jar
ln -s $(build-classpath jbossas/jboss-j2ee) jbossas/core-libs/lib/jboss-j2ee.jar
ln -s $(build-classpath jbossas/jboss) jbossas/core-libs/lib/jboss.jar
ln -s $(build-classpath jbossas/jboss-jca) jbossas/core-libs/lib/jboss-jca.jar
ln -s $(build-classpath jbossas/jboss-jmx) ./jbossas/core-libs/lib/jboss-jmx.jar
#./jbossas/core-libs/lib/jboss-local-jdbc.jar
ln -s $(build-classpath jbossas/jbosssx-client) jbossas/core-libs/lib/jbosssx-client.jar
ln -s $(build-classpath jbossas/jboss-system) jbossas/core-libs/lib/jboss-system.jar
ln -s $(build-classpath jbossas/jboss-transaction-client) jbossas/core-libs/lib/jboss-transaction-client.jar
#./jbossas/core-libs/lib/jms-ra.jar
ln -s $(build-classpath jbossas/jnp-client) jbossas/core-libs/lib/jnp-client.jar
%endif

mkdir -p jboss/common/lib
ln -s $(build-classpath jboss-common/jboss-common-client) jboss/common/lib/jboss-common-client.jar
ln -s $(build-classpath jboss-common/jboss-common) jboss/common/lib/jboss-common.jar
#./jboss/common/lib/jboss-common-sources.jar
ln -s $(build-classpath jboss-common/namespace) jboss/common/lib/namespace.jar

%if %without bootstrap
mkdir -p jboss/jbossts14/lib
ln -s $(build-classpath jbossts/jbossjta-integration) jboss/jbossts14/lib/jbossjta-integration.jar
ln -s $(build-classpath jbossts/jbossjta) jboss/jbossts14/lib/jbossjta.jar
ln -s $(build-classpath jbossts/jbossts-common) jboss/jbossts14/lib/jbossts-common.jar
%endif

mkdir -p jboss/jbossxb/lib
ln -s $(build-classpath jboss/jboss-xml-binding) jboss/jbossxb/lib/jboss-xml-binding.jar
#./jboss/jbossxb/lib/jboss-xml-binding-sources.jar

mkdir -p jboss/profiler/jvmti/lib
ln -s $(build-classpath jboss-profiler/jboss-profiler-jvmti) jboss/profiler/jvmti/lib/jboss-profiler-jvmti.jar

mkdir -p jboss/remoting/lib
ln -s $(build-classpath jboss-remoting) jboss/remoting/lib/jboss-remoting.jar

mkdir -p jboss/serialization/lib
ln -s $(build-classpath jboss-serialization) jboss/serialization/lib/jboss-serialization.jar

mkdir -p jgroups/lib
ln -s $(build-classpath jgroups) jgroups/lib/jgroups.jar

mkdir -p junit/lib
ln -s $(build-classpath junit) junit/lib/junit.jar

mkdir -p oswego-concurrent/lib
ln -s $(build-classpath concurrent) oswego-concurrent/lib/concurrent.jar

mkdir -p qdox/lib
ln -s $(build-classpath qdox) qdox/lib/qdox.jar

mkdir -p snmptrapappender/lib
ln -s $(build-classpath snmpTrapAppender) snmptrapappender/lib/snmpTrapAppender.jar

mkdir -p sun-javacc/lib
ln -s $(build-classpath javacc3) sun-javacc/lib/javacc.jar

mkdir -p trove/lib
ln -s $(build-classpath trove) trove/lib/trove.jar

mkdir -p wutka-dtdparser/lib
ln -s $(build-classpath dtdparser) wutka-dtdparser/lib/dtdparser.jar

popd

cp %{SOURCE2} thirdparty/libraries.ent

export CLASSPATH=
export OPT_JAR_LIST="ant/ant-nodeps"
ant release-bundle

mkdir temp
pushd temp
tar xzf %{SOURCE0}
jar cf ../%{name}-src.jar *
popd temp
rm -rf temp

%install

# jar
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 0644 output/lib/jboss-messaging.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# FIXME: (dwalluck) W: class-path-in-manifest /usr/share/jboss-messaging-1.4.0/jboss-messaging-client.jar

# client and sar
install -dm 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -pm 0644 output/lib/jboss-messaging-client.jar $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -pm 0644 output/lib/jboss-messaging.sar $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr output/etc $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# manual
install -d -m 0755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#cp -pr output/docs/userguide/en/pdf  $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr output/docs/userguide/en/html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%{__perl} -pi -e 's/\r$//g' %{buildroot}%{_docdir}/%{name}-%{version}/html/css/html.css

%if %{with_repolib}
	install -d -m 755 $RPM_BUILD_ROOT%{repodir}
	install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
	install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
	install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
	install -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
	cp -p $RPM_BUILD_ROOT%{_javadir}/jboss-messaging.jar $RPM_BUILD_ROOT%{repodirlib}
	cp -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/jboss-messaging-client.jar $RPM_BUILD_ROOT%{repodirlib}
        # Add the source again for some eclipse jboss project use
	install -m 644 %{name}-src.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-messaging-src.jar
        # Add resources
        install -d -m 755 $RPM_BUILD_ROOT%{repodir}/resources
        cp -p output/etc/server/default/deploy/*.xml $RPM_BUILD_ROOT%{repodir}/resources
        rm $RPM_BUILD_ROOT%{repodir}/resources/multiplexer*
        rm $RPM_BUILD_ROOT%{repodir}/resources/jboss*
        cp -p output/etc/remoting/*.xml $RPM_BUILD_ROOT%{repodir}/resources
%endif

%files
%{_javadir}/*jar
%{_datadir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%if %{with_repolib}
%files repolib
%{repodir}
%endif

%changelog
* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt1_1.SP3_CP01.5jpp5
- new version

