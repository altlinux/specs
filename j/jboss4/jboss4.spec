#define _with_basiconly 1
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: jbossretro spring-all
BuildRequires: /proc
BuildRequires: jpackage-1.5.0-core
%define version 4.0.4
%define name jboss4
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

# If you want only core modules to be built, 
# give rpmbuild option '--with coreonly'

%define with_coreonly %{?_with_coreonly:1}%{!?_with_coreonly:0}
%define without_coreonly %{!?_with_coreonly:1}%{?_with_coreonly:0}

# If you want only core and basic modules to be built, 
# give rpmbuild option '--with basiconly'

%define with_basiconly %{?_with_basiconly:1}%{!?_with_basiconly:0}
%define without_basiconly %{!?_with_basiconly:1}%{?_with_basiconly:0}

# If you want only modules to be built, 
# give rpmbuild option '--with modulesonly'

%define with_modulesonly %{?_with_modulesonly:1}%{!?_with_modulesonly:0}
%define without_modulesonly %{!?_with_modulesonly:1}%{?_with_modulesonly:0}

# If you don't want the hibernate module to be built, 
# give rpmbuild option '--without hibernate'

%define with_hibernate %{!?_without_hibernate:1}%{?_without_hibernate:0}
%define without_hibernate %{?_without_hibernate:1}%{!?_without_hibernate:0}

%define jbossdir %{_var}/lib/%{name}
%define logdir   %{_var}/log
%define tmpdir   %{_var}/cache
%define jbver    4.0.4.GA

Summary:        JBoss J2EE Application Server
Name:           jboss4
Version:        4.0.4
Release:        alt16_5jpp5
Epoch:          0
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
Source0:        http://download.sourceforge.net/jboss/jboss-4.0.4.GA-src.tar.gz
Source1:        %{name}.init
# Not in use, but let's keep this around.
Source2:        %{name}.logrotate
Source3:        %{name}.conf
Source4:        %{name}.catalog
Source5:        %{name}-all.properties
Source6:        %{name}-default.properties
Source7:        %{name}-minimal.properties
Source8:        %{name}-modules-tests.ent
Source9:        %{name}-jboss-minimal-tests.sh
Source10:       %{name}-jboss-all-config-tests.sh
Source11:	%{name}-jboss-tests-aop-scoped.sh
Source12:	%{name}-jboss-tests-compatibility.sh
Source13:	%{name}-jboss-tests-jacc-security-external.sh
Source14:	%{name}-jboss-tests-jacc-securitymgr.sh
Source15:	%{name}-jboss-tests-report-html.sh
Source16:	%{name}-jboss-tests-security-manager.sh
Source98:       %{name}-%{version}-testsuite-server-config.xml
Source99:       %{name}-jboss-tests.sh
Source100:	jboss-common-xb-src.tar.gz
#
Patch0:         %{name}-%{version}-build_xml.patch
Patch1:         %{name}-%{version}-SunConfigParser.patch
#404#Patch2:         %{name}-%{version}-util-Classes.patch
#404#Patch3:		%{name}-%{version}-ECVMonitorService.patch
Patch4:		%{name}-%{version}-jpp-libraries_xml.patch
Patch5:		%{name}-%{version}-jpp-libraries_ent.patch
Patch6:		%{name}-%{version}-jpp-thirdparty-libraries_ent.patch
#404#Patch7:         %{name}-%{version}-JspServletOptions.patch
Patch8:         %{name}-%{version}-tomcat-build_xml.patch
Patch9:         %{name}-%{version}-GraphMBeanAttributeAction.patch
#404#Patch10:        %{name}-%{version}-ManageSnapshotServlet.patch
Patch11:        %{name}-%{version}-jms-build_xml.patch
Patch12:        %{name}-%{version}-jmx-remoting-build_xml.patch
Patch13:        %{name}-%{version}-JMXSubsystemInvocationHandler.patch
Patch14:        %{name}-%{version}-MBeanServerClientInvokerProxy.patch
Patch15:	%{name}-%{version}-ManageSnapshotServlet.patch
Patch16:        %{name}-%{version}-testsuite-build_xml.patch
Patch17:        %{name}-%{version}-HttpSessionReplicationTestCase.patch
Patch18:        %{name}-%{version}-BaseTest.patch
Patch19:        %{name}-%{version}-spring-int-build_xml.patch
#notneededanylonger#Patch20:        %{name}-%{version}-common-build_xml.patch
Patch21:        %{name}-%{version}-JBossNotificationFilterSupport.patch
Patch22:        %{name}-%{version}-DeploymentInfoNotificationFilterFactory.patch
Patch23:        %{name}-%{version}-docbook-formal_xsl.patch
Patch24:        %{name}-%{version}-docbook-support_xml.patch
Patch25:	%{name}-%{version}-MultispacedUnitTestCase.patch
Patch26:	%{name}-%{version}-MappingTestCase.patch
Patch27:	%{name}-%{version}-JvmRouteURLRewritingTestCase.patch
Patch28:	%{name}-%{version}-testsuite-classloader_xml.patch
Patch29:	%{name}-%{version}-ResourceTest.patch
Patch30:	%{name}-%{version}-TestEntityBean.patch
Patch31:	%{name}-%{version}-server_policy.patch
Patch32:	%{name}-%{version}-server-config_xml.patch
Patch77:	jboss4-4.0.4-alt-tomcat5.5.31.patch

BuildArch:      noarch
# force install of jboss4-default configuration
Requires: bcel
Requires: sun-jaf
Requires: concurrent
Requires: dom4j
Requires: dtdparser
Requires: excalibur-avalon-framework-api
Requires: excalibur-avalon-framework-impl
Requires: gnu-getopt
Requires: gnu-regexp
Requires: gnu-trove
Requires: jacorb-jboss4
Requires: jakarta-commons-codec
Requires: jakarta-commons-httpclient
Requires: jakarta-commons-logging
Requires: jakarta-slide-webdavclient
Requires: jaxen
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-connector = 0:%{version}-%{release}
Requires: jboss4-config-default = 0:%{version}-%{release}
Requires: jboss4-deployment = 0:%{version}-%{release}
Requires: jboss4-iiop = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: jboss4-security = 0:%{version}-%{release}
Requires: jboss4-server = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}
Requires: jgroups24
Requires: log4j
Requires: tomcat5-server-lib
Requires: tomcat5-servlet-2.4-api
Requires: xalan-j2
Requires: xerces-j2
Requires: xml-commons-jaxp-1.3-apis
Requires: xml-commons-resolver12
# general requires
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant17 >= 0:1.6
BuildRequires: ant17-nodeps
BuildRequires: ant17-javamail
BuildRequires: ant17-junit
BuildRequires: ant17-trax
BuildRequires: eclipse-ecj
BuildRequires: excalibur-avalon-framework-api
BuildRequires: excalibur-avalon-framework-impl
BuildRequires: excalibur-avalon-logkit
BuildRequires: batik
BuildRequires: bsf
BuildRequires: fop
#BuildRequires:  jai			# NON-FREE
BuildRequires: jboss4-buildmagic-tasks
BuildRequires: junit
BuildRequires: saxon
BuildRequires: xalan-j2
BuildRequires: xdoclet-jboss4
BuildRequires: xerces-j2
BuildRequires: xjavadoc
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: xml-commons-resolver12
# core requires
BuildRequires: bcel
BuildRequires: concurrent
#404#BuildRequires:  crimson
BuildRequires: dom4j
BuildRequires: dtdparser
BuildRequires: gnu-getopt
BuildRequires: gnu-regexp
BuildRequires: jacorb-jboss4
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-digester
BuildRequires: jakarta-commons-el
BuildRequires: jakarta-commons-fileupload
BuildRequires: jakarta-commons-httpclient
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-modeler
BuildRequires: jakarta-commons-pool
BuildRequires: jakarta-taglibs-standard
BuildRequires: jakarta-slide-webdavclient
BuildRequires: jaxen
#BuildRequires:  jmx				# NON-FREE
BuildRequires: mx4j
			# REPLACEMENT
BuildRequires: log4j
BuildRequires: regexp
BuildRequires: snmptrapappender
BuildRequires: ws-jaxme
%if %{without_coreonly}
# noncore requires
BuildRequires: gjt-jpl-pattern
BuildRequires: gjt-jpl-util
#BuildRequires:  jaf				# NON-FREE
BuildRequires: jboss-j2se
BuildRequires: sun-jaf
			# REPLACEMENT
BuildRequires: jboss-remoting >= 0:1.4.3
BuildRequires: javacc40
BuildRequires: wsdl4j-jboss4

%if %{without_basiconly}
BuildRequires: jboss-cache
# nonbasic requires
BuildRequires: axis
BuildRequires: berkeleydb
#rap not needed?#BuildRequires:  bouncycastle-jdk1.4
BuildRequires: bsh
BuildRequires: gnu-trove
BuildRequires: hsqldb
BuildRequires: jakarta-commons-discovery
#BuildRequires:  javamail			# NON-FREE
BuildRequires: classpathx-mail
			# REPLACEMENT
#BuildRequires:  javamail-monolithic		# NON-FREE
BuildRequires: classpathx-mail
			# REPLACEMENT
BuildRequires: jboss-aop >= 0:1.5
BuildRequires: jboss-container
BuildRequires: jboss-dependency
BuildRequires: jboss-microcontainer
#BuildRequires: jbossws = 1:1.0.0
BuildRequires: jcommon
BuildRequires: jfreechart0
BuildRequires: jgroups24
#BuildRequires:  jmf			# NON-FREE
			# NO REPLACEMENT
BuildRequires: joesnmp
BuildRequires: javassist
BuildRequires: juddi
BuildRequires: junitejb
BuildRequires: myfaces
BuildRequires: opensaml
BuildRequires: qdox
BuildRequires: quartz >= 0:1.5.2
BuildRequires: tomcat5 >= 0:5.5.17
BuildRequires: tomcat5-admin-webapps
BuildRequires: tomcat5-common-lib
BuildRequires: tomcat5-server-lib
BuildRequires: tomcat5-jasper
BuildRequires: tomcat5-servlet-2.4-api
BuildRequires: tomcat5-jsp-2.0-api
BuildRequires: velocity
BuildRequires: ws-fx-addressing
BuildRequires: ws-scout
BuildRequires: wss4j
BuildRequires: xml-security
%if %{with_hibernate}
# hibernate3 requires
BuildRequires: hibernate32 >= 0:3.2
BuildRequires: hibernate3-annotations >= 0:3.2
BuildRequires: hibernate3-entitymanager >= 0:3.2
BuildRequires: hibernate3-ejb-persistence-3.0-api
BuildRequires: antlr
BuildRequires: asm
BuildRequires: cglib
BuildRequires: odmg
%endif
%endif
%endif
Patch33: jboss-4.0.3SP1-alt-ant17support.patch
Patch34: jboss4-4.0.3.1-alt-force-jdk14-only.patch

%description
JBoss Application Server is the most widely used Java application 
server on the market. A J2EE certified platform for developing and 
deploying enterprise Java applications, Web applications, and 
Portals, JBoss Application Server provides the full range of 
J2EE 1.4 features as well as extended enterprise services including 
clustering, caching, and persistence.

%if %{without_coreonly}
%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildRequires: java-javadoc
BuildArch: noarch

%description    javadoc
%{summary}.
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{without_modulesonly}
%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    manual
%{summary}.
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{without_modulesonly}
%package        config-all
Summary:        All configuration for %{name}
Group:          Development/Java
Provides:       %{name}-all 
Obsoletes:      %{name}-all
#Requires: ant17
Requires: antlr
Requires: asm
Requires: excalibur-avalon-framework-api
Requires: excalibur-avalon-framework-impl
Requires: backport-util-concurrent
Requires: bcel
Requires: bsf
Requires: bsh
Requires: cglib
Requires: eclipse-ecj
Requires: gjt-jpl-pattern
Requires: gjt-jpl-util
Requires: gnu-trove
Requires: hibernate32 >= 0:3.2
Requires: hsqldb
Requires: jacorb-jboss4
#Requires:       jaf				# NON-FREE
Requires: sun-jaf
			# REPLACEMENT
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-codec
Requires: jakarta-commons-collections
Requires: jakarta-commons-digester
Requires: jakarta-commons-discovery
Requires: jakarta-commons-el
Requires: jakarta-commons-logging
Requires: jakarta-commons-modeler
Requires: jakarta-taglibs-standard
#Requires:       javamail				# NON-FREE
Requires: classpathx-mail
			# REPLACEMENT
Requires: javassist
Requires: jboss4 = 0:%{version}-%{release}
Requires: jboss-aop >= 0:1.5
Requires: jboss4-aspects
Requires: jboss-cache >= 0:1.3.0
Requires: jboss4-cluster = 0:%{version}-%{release}
Requires: jboss4-connector = 0:%{version}-%{release}
Requires: jboss-container
Requires: jboss4-console = 0:%{version}-%{release}
Requires: jboss-dependency
Requires: jboss4-deployment
Requires: jboss4-hibernate-int = 0:%{version}-%{release}
Requires: jboss4-iiop = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jaxrpc = 0:%{version}-%{release}
Requires: jboss4-management = 0:%{version}-%{release}
Requires: jboss4-messaging = 0:%{version}-%{release}
Requires: jboss-microcontainer
Requires: jboss4-naming = 0:%{version}-%{release}
Requires: jboss-remoting >= 0:1.4.3
Requires: jboss4-remoting-int = 0:%{version}-%{release}
Requires: jboss4-security = 0:%{version}-%{release}
Requires: jboss-serialization
Requires: jboss4-server = 0:%{version}-%{release}
Requires: jboss4-transaction = 0:%{version}-%{release}
Requires: jboss4-varia = 0:%{version}-%{release}
Requires: jboss4-webservice = 0:%{version}-%{release}
Requires: jbossretro
#Requires: jbossws
Requires: jcommon
Requires: jfreechart0
Requires: jgroups24
Requires: juddi
Requires: log4j
Requires: myfaces
Requires: odmg
Requires: regexp
Requires: tomcat5 >= 0:5.5.17
Requires: tomcat5-admin-webapps
Requires: tomcat5-common-lib
Requires: tomcat5-server-lib
Requires: tomcat5-jasper
Requires: tomcat5-servlet-2.4-api
Requires: tomcat5-jsp-2.0-api
Requires: ws-scout
Requires: wsdl4j-jboss4
Requires: xml-security

%description    config-all
%{summary}.
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{without_modulesonly}
%package        config-default
Summary:        Default configuration for %{name}
Group:          Development/Java
Provides:       %{name}-default
Obsoletes:      %{name}-default
#Requires: ant
Requires: antlr
Requires: asm
Requires: backport-util-concurrent
Requires: bcel
Requires: bsf
Requires: bsh
Requires: cglib
Requires: eclipse-ecj
Requires: gjt-jpl-pattern
Requires: gjt-jpl-util
Requires: gnu-trove
Requires: hibernate32 >= 0:3.2
Requires: hsqldb
#Requires:       jaf				# NON-FREE
Requires: sun-jaf
			# REPLACEMENT
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-codec
Requires: jakarta-commons-collections
Requires: jakarta-commons-digester
Requires: jakarta-commons-discovery
Requires: jakarta-commons-httpclient
Requires: jakarta-commons-el
Requires: jakarta-commons-logging
Requires: jakarta-commons-modeler
Requires: jakarta-taglibs-standard
#Requires:       javamail				# NON-FREE
Requires: classpathx-mail
			# REPLACEMENT
Requires: javassist
Requires: jboss4 = 0:%{version}-%{release}
Requires: jboss-aop >= 0:1.5
Requires: jboss4-aspects
Requires: jboss4-connector = 0:%{version}-%{release}
Requires: jboss4-console = 0:%{version}-%{release}
Requires: jboss-container
Requires: jboss-dependency
Requires: jboss4-deployment = 0:%{version}-%{release}
Requires: jboss4-hibernate-int = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jaxrpc = 0:%{version}-%{release}
Requires: jboss4-management = 0:%{version}-%{release}
Requires: jboss4-messaging = 0:%{version}-%{release}
Requires: jboss-microcontainer
Requires: jboss4-naming = 0:%{version}-%{release}
Requires: jboss-remoting
Requires: jboss4-remoting-int = 0:%{version}-%{release}
Requires: jboss4-security = 0:%{version}-%{release}
Requires: jboss-serialization
Requires: jboss4-server = 0:%{version}-%{release}
Requires: jboss4-transaction = 0:%{version}-%{release}
Requires: jboss4-varia = 0:%{version}-%{release}
Requires: jboss4-webservice = 0:%{version}-%{release}
Requires: jbossretro
#Requires: jbossws
Requires: jcommon
Requires: jfreechart0
Requires: log4j
Requires: myfaces
Requires: odmg
Requires: regexp
Requires: tomcat5 >= 0:5.5.17
Requires: tomcat5-admin-webapps
Requires: tomcat5-common-lib
Requires: tomcat5-server-lib
Requires: tomcat5-jasper
Requires: tomcat5-servlet-2.4-api
Requires: tomcat5-jsp-2.0-api
Requires: wsdl4j-jboss4
Requires: xml-security

%description    config-default
%{summary}.
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{without_modulesonly}
%package        config-minimal
Summary:        Minimal configuration for %{name}
Group:          Development/Java
Provides:       %{name}-minimal
Obsoletes:      %{name}-minimal
Requires: jboss4 = 0:%{version}-%{release}
Requires: jboss4-management = 0:%{version}-%{release}
Requires: jboss4-naming = 0:%{version}-%{release}
Requires: jboss4-server = 0:%{version}-%{release}
Requires: log4j

%description    config-minimal
%{summary}.
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{without_modulesonly}
%package        client
Summary:        Client libraries for %{name}
Group:          Development/Java
Requires: excalibur-avalon-framework-api
Requires: excalibur-avalon-framework-impl
Requires: excalibur-avalon-logkit
Requires: concurrent
Requires: gnu-getopt
Requires: jacorb-jboss4
#Requires:       jaf				# NON-FREE
Requires: sun-jaf
			# REPLACEMENT
Requires: jakarta-commons-discovery
Requires: jakarta-commons-logging
#Requires:       javamail				# NON-FREE
Requires: classpathx-mail
			# REPLACEMENT
Requires: jboss4 = 0:%{version}-%{release}
Requires: jboss4-cluster = 0:%{version}-%{release}
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-connector = 0:%{version}-%{release}
Requires: jboss4-deployment = 0:%{version}-%{release}
Requires: jboss4-iiop = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jaxrpc = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: jboss4-management = 0:%{version}-%{release}
Requires: jboss4-messaging = 0:%{version}-%{release}
Requires: jboss4-security = 0:%{version}-%{release}
Requires: jboss4-server = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}
Requires: jboss4-transaction = 0:%{version}-%{release}
Requires: jboss4-varia = 0:%{version}-%{release}
Requires: jboss4-webservice = 0:%{version}-%{release}
Requires: log4j
Requires: wsdl4j-jboss4

%description    client
%{summary}.
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%package        aspects
Summary:        Aspects Library for %{name}
Group:          Development/Java
Requires: bsh
Requires: concurrent
Requires: jakarta-commons-logging
Requires: javassist
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-transaction = 0:%{version}-%{release}
Requires: jboss-remoting >= 0:1.4.3
Requires: jboss4-server = 0:%{version}-%{release}
Requires: gnu-trove
Requires: qdox

%description    aspects
%{summary}.
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%package        cluster
Summary:        Cluster Module for %{name}
Group:          Development/Java
Requires: concurrent
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: jboss4-naming = 0:%{version}-%{release}
Requires: jboss4-server = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}
Requires: jgroups24
Requires: xml-commons-jaxp-1.3-apis

%description    cluster
%{summary}.
%endif
%endif

%package        common
Summary:        Common Module for %{name}
Group:          Development/Java
Requires: concurrent
Requires: dom4j
Requires: dtdparser
Requires: gnu-regexp
Requires: jakarta-commons-httpclient
Requires: jakarta-slide-webdavclient
Requires: jboss4-system = 0:%{version}-%{release}
Requires: ws-jaxme
Requires: xerces-j2
Requires: xml-commons-jaxp-1.3-apis

%description    common
%{summary}.

%if %{without_coreonly}
%if %{without_basiconly}
%package        connector
Summary:        Connector Module for %{name}
Group:          Development/Java
Requires: concurrent
#Requires:       javamail				# NON-FREE
Requires: classpathx-mail
			# REPLACEMENT
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: jboss4-security = 0:%{version}-%{release}
Requires: jboss4-server = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}
Requires: jboss4-transaction = 0:%{version}-%{release}
Requires: xml-commons-jaxp-1.3-apis

%description    connector
%{summary}.
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%package        console
Summary:        Console Module for %{name}
Group:          Development/Java
Requires: bsh
Requires: concurrent
Requires: dom4j
Requires: gnu-getopt
Requires: gnu-regexp
Requires: gnu-trove
Requires: jakarta-commons-httpclient
Requires: jboss-aop >= 0:1.5
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: jboss4-management = 0:%{version}-%{release}
Requires: jboss4-server = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}
Requires: jboss4-varia = 0:%{version}-%{release}
Requires: jfreechart0 >= 0:0.9.21
Requires: tomcat5-servlet-2.4-api
Requires: xerces-j2
Requires: xml-commons-jaxp-1.3-apis

%description    console
%{summary}.
%endif
%endif

%if %{without_coreonly}
%package        deployment
Summary:        Deployment Module for %{name}
Group:          Development/Java
Requires: dom4j
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}

%description    deployment
%{summary}.
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{with_hibernate}
%package        hibernate-int
Summary:        Hibernate Module for %{name}
Group:          Development/Java
Obsoletes:      %{name}-hibernate
Provides:       %{name}-hibernate
Requires: asm
Requires: cglib
Requires: hibernate32 >= 0:3.2
Requires: odmg
Requires: jboss-cache >= 0:1.3.0
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: jboss4-server = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}
Requires: jboss4-transaction = 0:%{version}-%{release}

%description    hibernate-int
%{summary}.
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{with_hibernate}
%package        ejb3
Summary:        EJB3 Module for %{name}
Group:          Development/Java
Requires: concurrent
Requires: hibernate32
Requires: hibernate3-entitymanager
Requires: jakarta-commons-logging
Requires: javassist
Requires: jboss-aop
Requires: jboss-cache
Requires: jboss-remoting >= 0:1.4.3
Requires: jboss-serialization
Requires: jboss4-cluster = 0:%{version}-%{release}
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-deployment = 0:%{version}-%{release}
Requires: jboss4-ejb3x = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: jboss4-naming = 0:%{version}-%{release}
Requires: jboss4-security = 0:%{version}-%{release}
Requires: jboss4-server = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}
Requires: jboss4-transaction = 0:%{version}-%{release}
Requires: xml-commons-jaxp-1.3-apis
Requires: hibernate3-ejb-persistence-3.0-api

%description    ejb3
%{summary}.
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{with_hibernate}
%package        ejb3x
Summary:        EJB3X Module for %{name}
Group:          Development/Java

%description    ejb3x
%{summary}.
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%package        iiop
Summary:        IIOP Module for %{name}
Group:          Development/Java
Requires: excalibur-avalon-framework-api
Requires: excalibur-avalon-framework-impl
Requires: jacorb-jboss4
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: jboss4-naming = 0:%{version}-%{release}
Requires: jboss4-security = 0:%{version}-%{release}
Requires: jboss4-server = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}
Requires: jboss4-transaction = 0:%{version}-%{release}

%description    iiop
%{summary}.
%endif
%endif

%if %{without_coreonly}
%package        j2ee
Summary:        J2EE Module for %{name}
Group:          Development/Java
Requires: concurrent
Requires: dom4j
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: tomcat5-servlet-2.4-api

%description    j2ee
%{summary}.
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%package        jaxrpc
Summary:        JAXRPC Module for %{name}
Group:          Development/Java
#Requires:       jaf				# NON-FREE
Requires: sun-jaf
			# REPLACEMENT
Requires: jakarta-commons-discovery
Requires: jakarta-commons-logging
#Requires:       javamail				# NON-FREE
Requires: classpathx-mail
			# REPLACEMENT
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: tomcat5-servlet-2.4-api
Requires: wsdl4j-jboss4
Requires: xml-commons-jaxp-1.3-apis

%description    jaxrpc
%{summary}.
%endif
%endif

# dropped from JB404
%if 0
%if %{without_coreonly}
%if %{without_basiconly}
%package        jboss.net
Summary:        Net Module for %{name}
Group:          Development/Java
Requires: dom4j
#Requires:       jaf				# NON-FREE
Requires: sun-jaf
			# REPLACEMENT
Requires: jakarta-commons-discovery
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jaxrpc = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: jboss4-security = 0:%{version}-%{release}
Requires: jboss4-server = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}
Requires: tomcat5-servlet-2.4-api
Requires: wsdl4j-jboss4
Requires: xdoclet-jboss4
Requires: xml-commons-jaxp-1.3-apis

%description    jboss.net
%{summary}.
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%package        jms
Summary:        JMS Module for %{name}
Group:          Development/Java
Requires: concurrent
Requires: jboss-aop >= 0:1.5
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss-remoting >= 0:1.4.3
Requires: jgroups24

%description    jms
%{summary}.
%endif
%endif

%package        jmx
Summary:        JMX Module for %{name}
Group:          Development/Java
Requires: bcel
Requires: concurrent
Requires: dom4j
Requires: gnu-regexp
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}
Requires: xml-commons-jaxp-1.3-apis

%description    jmx
%{summary}.

%package        test
Summary:        Test Module for %{name}
Group:          Development/Java
#Requires: ant
Requires: jboss4-common = 0:%{version}-%{release}
Requires: junit
Requires: log4j

%description    test
%{summary}.

%if %{without_coreonly}
%if %{without_basiconly}
%package        jmx-remoting
Summary:        JMX Remoting Module for %{name}
Group:          Development/Java
Requires: concurrent
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}

%description    jmx-remoting
%{summary}.
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%package        management
Summary:        Management Module for %{name}
Group:          Development/Java
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-cluster = 0:%{version}-%{release}
Requires: jboss4-connector = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: jboss4-server = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}
Requires: xml-commons-jaxp-1.3-apis

%description    management
%{summary}.
%endif
%endif

%if 0
%package        media
Summary:        Media Module for %{name}
Group:          Development/Java
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: jboss4-server = 0:%{version}-%{release}
Requires: xml-commons-jaxp-1.3-apis
Requires: jmf
# Omitted because of non-free jmf (B)R

%description    media
%{summary}.
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%package        messaging
Summary:        Messaging Module for %{name}
Group:          Development/Java
Requires: concurrent
Requires: gnu-regexp
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: jboss4-security = 0:%{version}-%{release}
Requires: jboss4-server = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}
Requires: xml-commons-jaxp-1.3-apis

%description    messaging
%{summary}.
%endif
%endif

%package        naming
Summary:        Naming Module for %{name}
Group:          Development/Java
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}

%description    naming
%{summary}.

%if %{without_coreonly}
%if %{without_basiconly}
%package        remoting-int
Summary:        Remoting Integration Module for %{name}
Group:          Development/Java
Obsoletes:      %{name}-remoting
Provides:       %{name}-remoting
Requires: junit
Requires: log4j
Requires: jboss-aop
Requires: jboss-remoting >= 0:1.4.3
Requires: jboss4-aspects = 0:%{version}-%{release}
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-security = 0:%{version}-%{release}

%description    remoting-int
%{summary}.
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%package        security
Summary:        Security Module for %{name}
Group:          Development/Java
Requires: concurrent
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: jboss4-naming = 0:%{version}-%{release}
Requires: jboss4-server = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}
Requires: xml-commons-jaxp-1.3-apis

%description    security
%{summary}.
%endif
%endif

%if %{without_coreonly}
%package        server
Summary:        Server Module for %{name}
Group:          Development/Java
Requires: concurrent
Requires: gjt-jpl-util
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: jboss4-naming = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}
Requires: jboss4-transaction = 0:%{version}-%{release}

%description    server
%{summary}.
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{with_hibernate}
%package        spring-int
Summary:        Spring Module for %{name}
Group:          Development/Java
Obsoletes:      %{name}-spring
Provides:       %{name}-spring
Requires: jboss-aop
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-deployment = 0:%{version}-%{release}
Requires: jboss4-naming = 0:%{version}-%{release}
Requires: jboss4-naming = 0:%{version}-%{release}
Requires: spring

%description    spring-int
%{summary}.
%endif
%endif
%endif

%package        system
Summary:        System Module for %{name}
Group:          Development/Java
Requires: concurrent
Requires: gnu-getopt
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: xml-commons-jaxp-1.3-apis

%description    system
%{summary}.

%if %{without_coreonly}
%package        transaction
Summary:        Transaction Module for %{name}
Group:          Development/Java
Requires: concurrent
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}

%description    transaction
%{summary}.
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%package        varia
Summary:        Varia Module for %{name}
Group:          Development/Java
#Requires: ant
Requires: bsh
Requires: concurrent
Requires: gnu-regexp
#Requires:       jaf				# NON-FREE
Requires: sun-jaf
			# REPLACEMENT
Requires: jakarta-commons-logging
#Requires:       javamail				# NON-FREE
Requires: classpathx-mail
			# REPLACEMENT
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-cluster = 0:%{version}-%{release}
Requires: jboss4-console = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: jboss4-security = 0:%{version}-%{release}
Requires: jboss4-server = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}
Requires: jboss4-transaction = 0:%{version}-%{release}
Requires: joesnmp
Requires: junit
Requires: tomcat5-servlet-2.4-api
Requires: velocity
Requires: xalan-j2
Requires: xerces-j2
Requires: xml-commons-jaxp-1.3-apis
Requires: xmlrpc

%description    varia
%{summary}.
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%package        webservice
Summary:        Web Service Module for %{name}
Group:          Development/Java
Requires: dom4j
#Requires:       jaf				# NON-FREE
Requires: sun-jaf
			# REPLACEMENT
Requires: jboss4-common = 0:%{version}-%{release}
Requires: jboss4-j2ee = 0:%{version}-%{release}
Requires: jboss4-jaxrpc = 0:%{version}-%{release}
Requires: jboss4-jmx = 0:%{version}-%{release}
Requires: jboss4-security = 0:%{version}-%{release}
Requires: jboss4-server = 0:%{version}-%{release}
Requires: jboss4-system = 0:%{version}-%{release}
Requires: tomcat5-servlet-2.4-api
Requires: wsdl4j-jboss4
Requires: xmlbeans
Requires: xml-commons-jaxp-1.3-apis
Requires: xmlrpc

%description    webservice
%{summary}.
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{without_modulesonly}
%package        testsuite
Summary:        Testsuite for %{name}
Group:          Development/Java
Requires: jboss4-config-all = 0:%{version}-%{release}

%description    testsuite
%{summary}.
%endif
%endif
%endif

%prep
cat <<EOT

		If you want only core modules to be built, 
		give rpmbuild option '--with coreonly'

		If you want only core and basic modules to be built, 
		give rpmbuild option '--with basiconly'

		If you want only modules to be built, 
		give rpmbuild option '--with modulesonly'

		If you do not want the hibernate module to be built, 
		give rpmbuild option '--without hibernate'

EOT
%setup -q -n jboss-%{jbver}-src
%setup -q -n jboss-%{jbver}-src -T -D -a 100
for f in $(find . -name "*.jar"); do
	mv $f $f.no
done

%patch0 -b .sav
%patch1 -b .sav
#404#%patch2 -b .sav
#404#%patch3 -b .sav
%patch4 -b .sav
%patch5 -b .sav
%patch6 -b .sav
#404#%patch7 -b .sav
%patch8 -b .sav
%patch9 -b .sav
#404#%patch10 -b .sav
%patch11 -b .sav
%patch12 -b .sav
%patch13 -b .sav
%patch14 -b .sav
%patch15 -b .sav
%patch16 -b .sav
%patch17 -b .sav
%patch18 -b .sav
%patch19 -b .sav
#%patch20 -b .sav
%patch21 -b .sav
%patch22 -b .sav
%patch23 -b .sav
%patch24 -b .sav
%patch25 -b .sav
%patch26 -b .sav
%patch27 -b .sav
%patch28 -b .sav
%patch29 -b .sav
%patch30 -b .sav
%patch31 -b .sav
%patch32 -b .sav
%patch77 -b .sav -p1

# ant 1.8 support hack
for i in `find . -name buildmagic.ent`; do sed -i 's,fail unless="buildmagic.ant.compatible",fail if="never",' $i; done


pushd thirdparty

# additional for spring-int

mkdir -p spring/lib
pushd spring/lib
ln -sf $(build-classpath spring) .
popd

# NEW, link in unconditionally for now

#temp##jboss/backport-concurrent/lib/jboss-backport-concurrent.jar.no
#temp#pushd jboss/backport-concurrent/lib
#temp#mv jboss-backport-concurrent.jar.no jboss-backport-concurrent.jar
#temp##ln -sf $(build-classpath backport-util-concurrent) jboss-backport-concurrent.jar
#temp#popd
#temp##jboss/jbossretro-rt/lib/jbossretro-rt.jar.no
#temp#pushd jboss/jbossretro-rt/lib
#temp#mv jbossretro-rt.jar.no jbossretro-rt.jar
#temp#popd
#temp##jboss/jbossws/lib/jbossws-client.jar.no
#temp##jboss/jbossws/lib/jbossws.sar
#temp#pushd jboss/jbossws/lib
#temp#mv jbossws-client.jar.no jbossws-client.jar
#temp#popd
#temp##jboss/jbossws14/lib/jbossws14-client.jar.no
#temp##jboss/jbossws14/lib/jbossws14.sar
#temp#pushd jboss/jbossws14/lib
#temp#mv jbossws14-client.jar.no jbossws14-client.jar
#temp#popd

###404# jbossxb is needed in coreonly phase
###404# build this jar in an preliminary stage, before starting real build

###jboss/jbossxb/lib/jboss-xml-binding.jar.no
##pushd jboss/jbossxb/lib
##mv jboss-xml-binding.jar.no jboss-xml-binding.jar
##popd


# UNCONDITIONAL
#apache-avalon/lib/avalon-framework.jar.no
pushd apache-avalon/lib
ln -sf $(build-classpath excalibur/avalon-framework-api) .
ln -sf $(build-classpath excalibur/avalon-framework-impl) .
ln -sf $(build-classpath excalibur/avalon-logkit) .
popd
#apache-avalon-logkit/lib/logkit.jar.no
pushd apache-avalon-logkit/lib
ln -sf $(build-classpath excalibur/avalon-logkit) .
popd
#apache-bcel/lib/bcel.jar.no
pushd apache-bcel/lib
ln -sf $(build-classpath bcel) .
popd
#apache-beanutils/lib/commons-beanutils.jar.no
pushd apache-beanutils/lib
ln -sf $(build-classpath commons-beanutils-core) .
ln -sf $(build-classpath commons-beanutils) .
popd
#apache-bsf/lib/bsf.jar.no
pushd apache-bsf/lib
ln -sf $(build-classpath bsf) .
popd
#apache-codec/lib/commons-codec-1.2.jar.no
pushd apache-codec/lib
ln -sf $(build-classpath commons-codec) .
popd
#apache-collections/lib/commons-collections.jar.no
pushd apache-collections/lib
ln -sf $(build-classpath commons-collections) .
popd
#404##apache-crimson/lib/crimson.jar.no
#404#pushd apache-crimson/lib
#404#ln -sf $(build-classpath crimson) .
#404#popd
#apache-digester/lib/commons-digester-1.6.jar.no
#apache-digester/lib/commons-digester.jar.no
pushd apache-digester/lib
ln -sf $(build-classpath commons-digester) .
popd
#apache-discovery/lib/commons-discovery.jar.no
pushd apache-discovery/lib
ln -sf $(build-classpath commons-discovery) .
popd
#apache-fileupload/lib/commons-fileupload.jar.no
pushd apache-fileupload/lib
ln -sf $(build-classpath commons-fileupload) .
popd
#apache-httpclient/lib/commons-httpclient.jar.no
pushd apache-httpclient/lib
ln -sf $(build-classpath commons-httpclient) .
popd
#apache-jaxme/lib/jaxmexs.jar.no
pushd apache-jaxme/lib
ln -sf $(build-classpath jaxme/ws-jaxmexs) jaxmexs.jar
popd
#apache-lang/lib/commons-lang-1.0.jar.no
pushd apache-lang/lib
ln -sf $(build-classpath commons-lang) commons-lang-1.0.jar
popd
#apache-log4j/lib/log4j.jar.no
#apache-log4j/lib/snmpTrapAppender.jar.no
pushd apache-log4j/lib
ln -sf $(build-classpath log4j) .
ln -sf $(build-classpath snmptrapappender) snmpTrapAppender.jar
popd
#apache-logging/lib/commons-logging.jar.no
pushd apache-logging/lib
ln -sf $(build-classpath commons-logging) .
popd
#apache-modeler/lib/commons-modeler.jar.no
pushd apache-modeler/lib
ln -sf $(build-classpath commons-modeler) .
popd
#apache-myfaces/lib/jstl.jar.no
#apache-myfaces/lib/myfaces-api.jar.no
#apache-myfaces/lib/myfaces-impl.jar.no
pushd apache-myfaces/lib
ln -sf $(build-classpath taglibs-core) jstl.jar
ln -sf $(build-classpath myfaces/myfaces-jsf-api) myfaces-api.jar
ln -sf $(build-classpath myfaces/myfaces-impl) .
popd
#apache-pool/lib/commons-pool.jar.no
pushd apache-pool/lib
ln -sf $(build-classpath commons-pool) .
popd
#apache-slide/lib/webdavlib.jar.no
pushd apache-slide/lib
ln -sf $(build-classpath slide/slide-webdavclient-webdavlib) webdavlib.jar
popd
#apache-xalan/lib/xalan.jar.no
pushd apache-xalan/lib
ln -sf $(build-classpath xalan-j2) xalan.jar
ln -sf $(build-classpath xalan-j2-serializer) xalan-serializer.jar
popd
#apache-xerces/lib/resolver.jar.no
#apache-xerces/lib/xercesImpl.jar.no
#apache-xerces/lib/xml-apis.jar.no
pushd apache-xerces/lib
ln -sf $(build-classpath xml-commons-resolver12) resolver.jar
ln -sf $(build-classpath xerces-j2) xercesImpl.jar
ln -sf $(build-classpath xml-commons-jaxp-1.3-apis) xml-apis.jar
popd
#dom4j/lib/dom4j.jar.no
pushd dom4j/lib
ln -sf $(build-classpath dom4j) .
popd
#gnu-getopt/lib/getopt.jar.no
pushd gnu-getopt/lib
ln -sf $(build-classpath gnu-getopt) getopt.jar
popd
#404##gnu-regexp/lib/gnu-regexp.jar.no
#404#pushd gnu-regexp/lib
#404#ln -sf $(build-classpath gnu-regexp) gnu-regexp.jar
#404#popd
#jacorb/lib/idl_g.jar.no
#jacorb/lib/idl.jar.no
#jacorb/lib/jacorb_g.jar.no
#jacorb/lib/jacorb.jar.no
pushd jacorb/lib
ln -sf $(build-classpath jacorb-jboss4/idl) idl.jar
ln -sf $(build-classpath jacorb-jboss4/jacorb-jboss4) jacorb.jar
popd
#jaxen/lib/jaxen-1.1-beta-4.jar.no
#jaxen/lib/jaxen.jar.no
pushd jaxen/lib
ln -sf $(build-classpath jaxen) .
popd
#junit/lib/junit.jar.no
pushd junit/lib
ln -sf $(build-classpath junit) .
popd
#oswego-concurrent/lib/concurrent.jar.no
pushd oswego-concurrent/lib
ln -sf $(build-classpath concurrent) .
popd
#wutka-dtdparser/lib/dtdparser121.jar.no
pushd wutka-dtdparser/lib
ln -sf $(build-classpath dtdparser) dtdparser121.jar
popd
#xdoclet/lib/xdoclet-bea-module-jb4.jar.no
#xdoclet/lib/xdoclet-ejb-module-jb4.jar.no
#xdoclet/lib/xdoclet-java-module-jb4.jar.no
#xdoclet/lib/xdoclet-jb4.jar.no
#xdoclet/lib/xdoclet-jboss-module-jb4.jar.no
#xdoclet/lib/xdoclet-jdo-module-jb4.jar.no
#xdoclet/lib/xdoclet-jmx-module-jb4.jar.no
#xdoclet/lib/xdoclet-web-module-jb4.jar.no
#xdoclet/lib/xdoclet-xdoclet-module-jb4.jar.no
#xdoclet/lib/xdoclet-xjavadoc-jb4.jar.no
pushd xdoclet/lib
ln -sf $(build-classpath xdoclet-jboss4/xdoclet-bea-module) xdoclet-bea-module-jb4.jar
ln -sf $(build-classpath xdoclet-jboss4/xdoclet-ejb-module) xdoclet-ejb-module-jb4.jar
ln -sf $(build-classpath xdoclet-jboss4/xdoclet-java-module) xdoclet-java-module-jb4.jar
ln -sf $(build-classpath xdoclet-jboss4/xdoclet-jboss-module) xdoclet-jboss-module-jb4.jar
ln -sf $(build-classpath xdoclet-jboss4/xdoclet) xdoclet-jb4.jar
ln -sf $(build-classpath xdoclet-jboss4/xdoclet-jdo-module) xdoclet-jdo-module-jb4.jar
ln -sf $(build-classpath xdoclet-jboss4/xdoclet-jmx-module) xdoclet-jmx-module-jb4.jar
ln -sf $(build-classpath xdoclet-jboss4/xdoclet-web-module) xdoclet-web-module-jb4.jar
ln -sf $(build-classpath xdoclet-jboss4/xdoclet-xdoclet-module) xdoclet-xdoclet-module-jb4.jar
ln -sf $(build-classpath xjavadoc) xdoclet-xjavadoc-jb4.jar
popd
#xml-sax/lib/sax2-ext.jar.no
#xml-sax/lib/sax2.jar.no
pushd xml-sax/lib
ln -sf $(build-classpath sax2) sax2.jar
ln -sf $(build-classpath sax2) sax2-ext.jar
popd
#sun-jaf/lib/activation.jar.no
pushd sun-jaf/lib
ln -sf $(build-classpath sun-jaf) activation.jar
popd



%if %{without_coreonly}
#jboss/serialization/lib/jboss-serialization.jar.no
pushd jboss/serialization/lib
ln -sf $(build-classpath jboss-serialization) .
popd

#gjt-jpl-util/lib/jpl-pattern.jar.no
#gjt-jpl-util/lib/jpl-util.jar.no
pushd gjt-jpl-util/lib
ln -sf $(build-classpath gjt-jpl-util) jpl-util.jar
ln -sf $(build-classpath gjt-jpl-pattern) jpl-pattern.jar
popd
#jboss/remoting/lib/jboss-remoting.jar.no
pushd jboss/remoting/lib
ln -sf $(build-classpath jboss-remoting) .
popd
#sun-servlet/lib/jsp-api.jar.no
#sun-servlet/lib/servlet-api.jar.no
pushd sun-servlet/lib
ln -sf $(build-classpath jspapi) jsp-api.jar
ln -sf $(build-classpath servletapi5) servlet-api.jar
popd
#sun-javacc/lib/javacc.jar.no
pushd sun-javacc/lib
ln -sf $(build-classpath javacc) .
popd
#ibm-wsdl4j/lib/wsdl4j.jar.no
pushd ibm-wsdl4j/lib
ln -sf $(build-classpath wsdl4j-jboss4) wsdl4j.jar
popd
#javassist/lib/javassist.jar.no
pushd javassist/lib
ln -sf $(build-classpath javassist) javassist.jar
popd

%if %{without_basiconly}
#quartz/lib/quartz-all-1.5.2.jar.no
pushd quartz/lib
ln -sf $(build-classpath quartz) quartz-all-1.5.2.jar
popd

#jboss/cache/lib/jboss-cache.jar.no
pushd jboss/cache/lib
ln -sf $(build-classpath jboss-cache) .
popd
#apache-addressing/lib/addressing-1.0.jar.no
pushd apache-addressing/lib
ln -sf $(build-classpath ws-fx-addressing) .
popd
#apache-scout/lib/scout.jar.no
pushd apache-scout/lib
ln -sf $(build-classpath ws-scout/scout) scout.jar
popd
#apache-velocity/lib/velocity.jar.no
pushd apache-velocity/lib
ln -sf $(build-classpath velocity) .
popd
#apache-wss4j/lib/wss4j.jar.no
pushd apache-wss4j/lib
ln -sf $(build-classpath wss4j) wss4j.jar
popd
#apache-xmlsec/lib/xmlsec.jar.no
pushd apache-xmlsec/lib
ln -sf $(build-classpath xml-security) xmlsec.jar
popd
#404##asm/lib/asm-attrs.jar.no
#404##asm/lib/asm.jar.no
#404#pushd asm/lib
#404#ln -sf $(build-classpath asm/asm) .
#404#ln -sf $(build-classpath asm/asm-attrs) .
#404#popd
#beanshell/lib/bsh-1.3.0.jar.no
pushd beanshell/lib
ln -sf $(build-classpath bsh) bsh-1.3.0.jar
popd
#cglib/lib/cglib-2.1_2jboss.jar.no
pushd cglib/lib
ln -sf $(build-classpath cglib-nodep) cglib.jar
popd
#commons-el/lib/commons-el.jar.no
pushd commons-el/lib
ln -sf $(build-classpath commons-el) .
popd
#hsqldb/lib/hsqldb.jar.no
pushd hsqldb/lib
ln -sf $(build-classpath hsqldb) hsqldb.jar
popd
#jboss/aop/lib/jboss-aop.jar.no
#jboss/aop/lib/jboss-aop-jdk50-client.jar.no
#jboss/aop/lib/jboss-aop-jdk50.jar.no
#jboss/aop/lib/jdk14-pluggable-instrumentor.jar.no
#jboss/aop/lib/jrockit-pluggable-instrumentor.jar.no
#jboss/aop/lib/pluggable-instrumentor.jar.no
pushd jboss/aop/lib
#ln -sf $(build-classpath jboss-aop/jboss-aop) .
#ln -sf $(build-classpath jboss-aop/jdk14-pluggable-instrumentor) .
##
#ln -sf $(build-classpath jboss-aop/jboss-aop-jdk50) .
#ln -sf $(build-classpath jboss-aop/jboss-aop-jdk50-client) .
##ln -sf $(build-classpath jboss-aop/jrockit-pluggable-instrumentor) .
#ln -sf $(build-classpath jboss-aop/pluggable-instrumentor) .
for i in *.no; do mv $i `echo $i| sed -e 's,.no,,'`; done
popd
#jboss/microcontainer/lib/jboss-container.jar.no
#jboss/microcontainer/lib/jboss-dependency.jar.no
#jboss/microcontainer/lib/jboss-microcontainer.jar.no
pushd jboss/microcontainer/lib
ln -sf $(build-classpath jboss-container) .
ln -sf $(build-classpath jboss-dependency) .
ln -sf $(build-classpath jboss-microcontainer/jboss-microcontainer) .
popd
#jfreechart/lib/jcommon.jar.no
#jfreechart/lib/jfreechart.jar.no
pushd jfreechart/lib
ln -sf $(build-classpath jcommon) .
ln -sf $(build-classpath jfreechart0) jfreechart.jar
popd
#jgroups/lib/jgroups.jar.no
pushd jgroups/lib
ln -sf $(build-classpath jgroups24) jgroups.jar
popd
#joesnmp/lib/joesnmp.jar.no
pushd joesnmp/lib
ln -sf $(build-classpath joesnmp) .
popd
#juddi/lib/juddi.jar.no
pushd juddi/lib
ln -sf $(build-classpath juddi/juddi) .
popd
#junitejb/lib/junitejb.jar.no
pushd junitejb/lib
ln -sf $(build-classpath junitejb) .
popd
#qdox/lib/qdox.jar.no
pushd qdox/lib
#ln -sf $(build-classpath qdox) .
popd
# move to the end
mv qdox/lib/qdox.jar.no qdox/lib/qdox.jar
#sleepycat/lib/je.jar.no
pushd sleepycat/lib
ln -sf $(build-classpath berkeleydb) je.jar
popd
#sun-javamail/lib/mail.jar.no
pushd sun-javamail/lib
ln -sf $(build-classpath javamail) mail.jar
popd
#trove/lib/trove.jar.no
pushd trove/lib
ln -sf $(build-classpath gnu-trove) trove.jar
popd

#jboss/backport-concurrent/lib/jboss-backport-concurrent.jar.no
pushd jboss/backport-concurrent/lib
#mv jboss-backport-concurrent.jar.no jboss-backport-concurrent.jar
ln -sf $(build-classpath backport-util-concurrent) jboss-backport-concurrent.jar
popd
#jboss/jbossretro-rt/lib/jbossretro-rt.jar.no
pushd jboss/jbossretro-rt/lib
#mv jbossretro-rt.jar.no jbossretro-rt.jar
ln -sf $(build-classpath jbossretro-rt) .
popd
#jboss/jbossws/lib/jbossws-client.jar.no
pushd jboss/jbossws/lib
mv jbossws-client.jar.no jbossws-client.jar
#ln -sf $(build-classpath jbossws/jbossws-client) .
popd
#jboss/jbossws14/lib/jbossws14-client.jar.no
pushd jboss/jbossws14/lib
mv jbossws14-client.jar.no jbossws14-client.jar
#ln -sf $(build-classpath jbossws/jbossws14-client) .
popd

%if %{with_hibernate}
mkdir -p jboss/j2se/lib
pushd jboss/j2se/lib
ln -sf $(build-classpath jboss-j2se/jboss-j2se) .
popd

#antlr/lib/antlr-2.7.5H3.jar.no
pushd antlr/lib
ln -sf $(build-classpath antlr) .
popd

#hibernate-annotations/lib/hibernate-annotations.jar.no
###
#hibernate-entitymanager/lib/ejb3-persistence.jar.no
#hibernate-entitymanager/lib/hibernate-entitymanager.jar.no
###
#hibernate/lib/hibernate3.jar.no
pushd hibernate/lib
ln -sf $(build-classpath hibernate32) hibernate3.jar
popd
pushd hibernate-entitymanager/lib
ln -sf $(build-classpath hibernate3-entitymanager) hibernate-entitymanager.jar
#mv ejb3-persistence.jar.no ejb3-persistence.jar
ln -sf $(build-classpath hibernate3-ejb-persistence-3.0-api) ejb3-persistence.jar
popd
pushd hibernate-annotations/lib
ln -sf $(build-classpath hibernate3-annotations) hibernate-annotations.jar
popd

#odmg/lib/odmg-3.0.jar.no
pushd odmg/lib
ln -sf $(build-classpath odmg-3.0) .
popd
%endif

pushd apache-tomcat/lib
#apache-tomcat/lib/catalina.jar.no
ln -sf $(build-classpath tomcat5/catalina) .
#apache-tomcat/lib/catalina-manager.jar.no
ln -sf $(build-classpath tomcat5/catalina-manager) .
#apache-tomcat/lib/catalina-optional.jar.no
ln -sf $(build-classpath tomcat5/catalina-optional) .
#apache-tomcat/lib/jasper-compiler.jar.no
ln -sf $(build-classpath jasper5-compiler) jasper-compiler.jar
#apache-tomcat/lib/jasper-compiler-jdt.jar.no
ln -sf $(build-classpath jdtcore) jasper-compiler-jdt.jar
#apache-tomcat/lib/jasper-runtime.jar.no
ln -sf $(build-classpath jasper5-runtime) jasper-runtime.jar
#apache-tomcat/lib/naming-resources.jar.no
ln -sf $(build-classpath tomcat5/naming-resources) .
#apache-tomcat/lib/servlets-default.jar.no
ln -sf $(build-classpath tomcat5/servlets-default) .
#apache-tomcat/lib/servlets-invoker.jar.no
ln -sf $(build-classpath tomcat5/servlets-invoker) .
#apache-tomcat/lib/servlets-webdav.jar.no
ln -sf $(build-classpath tomcat5/servlets-webdav) .
#apache-tomcat/lib/tomcat-ajp.jar.no
ln -sf $(build-classpath tomcat5/tomcat-ajp) .
#apache-tomcat/lib/tomcat-apr.jar.no
ln -sf $(build-classpath tomcat5/tomcat-apr) .
#apache-tomcat/lib/tomcat-coyote.jar.no
ln -sf $(build-classpath tomcat5/tomcat-coyote) .
#apache-tomcat/lib/tomcat-http.jar.no
ln -sf $(build-classpath tomcat5/tomcat-http) .
#apache-tomcat/lib/tomcat-util.jar.no
ln -sf $(build-classpath tomcat5/tomcat-util) .
popd


%endif
%endif

popd

pushd docbook-support/support/lib
ln -sf $(build-classpath fop) fop.jar
build-jar-repository -s -p . batik
#build-jar-repository -s -p . jai/jai_codec jai/jai_core
ln -sf $(build-classpath excalibur/avalon-framework-api) .
ln -sf $(build-classpath excalibur/avalon-framework-impl) .
ln -sf $(build-classpath saxon) saxon.jar
#ln -sf $(build-classpath saxon-dbxsl-extensions) saxon-dbxsl-extensions.jar
#ln -sf $(build-classpath rowan) rowan-0.1.jar
#aux#mv avalon-framework-cvs-20020806.jar.no avalon-framework-cvs-20020806.jar
#aux#mv batik.jar.no batik.jar
#aux#mv fop.jar.no fop.jar
#aux#mv jai_codec.jar.no jai_codec.jar
#aux#mv jai_core.jar.no jai_core.jar
#aux#mv rowan-0.1.jar.no rowan-0.1.jar
#aux#mv saxon-dbxsl-extensions.jar.no saxon-dbxsl-extensions.jar
#aux#mv saxon.jar.no saxon.jar
popd

# FIXME: these tests have unresolved imports
rm testsuite/src/main/org/jboss/test/jms/JBossASJMSTestAdmin.java
rm -rf testsuite/src/main/org/jboss/test/jbossmq

mv testsuite/src/resources/jmx/mbeanlocaldir/local-directory/sub-directory/examplejar.jar.no testsuite/src/resources/jmx/mbeanlocaldir/local-directory/sub-directory/examplejar.jar
mv testsuite/src/resources/classloader/scoping/override/log4j113/log4j-core.jar.no testsuite/src/resources/classloader/scoping/override/log4j113/log4j-core.jar
mv testsuite/src/resources/classloader/scoping/override/xml/xerces.jar.no testsuite/src/resources/classloader/scoping/override/xml/xerces.jar

pushd tools/lib
ln -sf $(build-classpath ant17) ant.jar
ln -sf $(build-classpath ant17/ant17-javamail) ant-javamail.jar
ln -sf $(build-classpath ant17/ant17-junit) ant-junit.jar
ln -sf $(build-classpath ant17-launcher) ant-launcher.jar
ln -sf $(build-classpath ant17/ant17-nodeps) ant-nodeps.jar
ln -sf $(build-classpath ant17/ant17-trax) ant-trax.jar
#ln -sf $(build-classpath ant17/ant17-xalan2) ant-xalan2.jar
#ln -sf $(build-classpath ant17/ant17-xslp) ant-xslp.jar
ln -sf $(build-classpath bsf) bsf.jar
ln -sf $(build-classpath jboss4/jboss4-buildmagic-tasks) buildmagic-tasks.jar
#BUILD/jboss-4.0.1-src/tools/lib/jbossbuild.jar.no
ln -sf $(build-classpath junit) junit.jar
#BUILD/jboss-4.0.1-src/tools/lib/pretty.jar.no
ln -sf $(build-classpath xml-commons-resolver) resolver.jar
ln -sf $(build-classpath xalan-j2) xalan.jar
ln -sf $(build-classpath xerces-j2) xercesImpl.jar
ln -sf $(build-classpath xml-commons-jaxp-1.3-apis) xml-apis.jar
ln -sf $(build-classpath xdoclet-jboss4/xdoclet-jboss-module) .
popd

mv console/src/resources/webconsole.war/images/otherimages.jar.no console/src/resources/webconsole.war/images/otherimages.jar
mkdir -p server/output/docs/
cp -pr server/src/docs/* server/output/docs/
mkdir -p messaging/output/docs/
%patch33 -p1
%patch34 -p1

%build
BUILD_ID=`date -u +%Y%m%d%H%M`_%{version}-%{release}
#export JAVA_HOME=/usr/lib/jvm/java-1.5.0
export PATH="$JAVA_HOME/bin:$PATH"
export OPT_JAR_LIST="ant17/ant17-nodeps ant17/ant17-junit junit ant17/ant17-trax"
export CLASSPATH=$(build-classpath xml-commons-jaxp-1.3-apis jaxp_parser_impl \
ant17/ant17-nodeps \
)

ANT_GRL_OPTS="-Djavax.xml.parsers.DocumentBuilderFactory=org.apache.xerces.jaxp.DocumentBuilderFactoryImpl"
ANT_GRL_OPTS="$ANT_GRL_OPTS -Djavax.xml.parsers.SAXParserFactory=org.apache.xerces.jaxp.SAXParserFactoryImpl"
ANT_GRL_OPTS="$ANT_GRL_OPTS -Djava.protocol.handler.pkgs=org.jboss.net.protocol"
ANT_GRL_OPTS="$ANT_GRL_OPTS "-Dbuild.id=$BUILD_ID

rm -rf common
mv common-xb common
pushd common
ant17  
popd
cp common/output/lib/jboss-xml-binding.jar thirdparty/jboss/jbossxb/lib/jboss-xml-binding.jar


pushd build
###install -m 644 etc/local.properties-production local.properties
###echo "build.compiler=modern"   >> local.properties
#### The following applies to at least Java 1.3.x versions:
###echo "build.sysclasspath=last" >> local.properties
###echo "build.docs=build-docs" >> local.properties
export ANT_OPTS="-Xmx512m $ANT_GRL_OPTS"
%if %{without_coreonly}
 %if %{without_basiconly}
  %if %{with_modulesonly}
    %if %{without_hibernate}
ant17  -Dgroups=core,basic,standard modules-all
    %else
ant17  -Dgroups=core,basic,standard,jdk5,postpone modules-all
    %endif
  %else
    %if %{without_hibernate}
ant17  -Dgroups=core,basic,standard modules-all install
    %else
ant17  -Dgroups=core,basic,standard,jdk5,postpone modules-all install
    %endif
  %endif
 %else
ant17  -Dgroups=core,basic modules-all
 %endif
%else
ant17  -Dgroups=core modules-most
%endif
popd
%if %{without_coreonly}
%if %{without_basiconly}
pushd jms
export ANT_OPTS="-Xmx512m $ANT_GRL_OPTS"
ant17  
popd
pushd jmx-remoting
export ANT_OPTS="-Xmx512m $ANT_GRL_OPTS"
ant17  
popd
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{without_modulesonly}
pushd docbook-support/docs/guide
export ANT_OPTS="-Xmx512m $ANT_GRL_OPTS"
ant17  
popd
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{without_modulesonly}
pushd build/output/jboss-%{jbver}/lib
# no avalon-framework-*.jar in binary dist
#404#ln -sf $(build-classpath excalibur/avalon-framework-api) .
# no avalon-framework-*.jar in binary dist
#404#ln -sf $(build-classpath excalibur/avalon-framework-impl) .
#rap not needed?#ln -sf $(build-classpath commons-codec) .
pushd endorsed
# duplicated by xalan-serializer.jar
#404#ln -sf $(build-classpath xalan-j2-serializer) .
popd
popd
pushd build/output/jboss-%{jbver}/server/all/lib
ln -sf $(build-classpath excalibur/avalon-framework-api) .
ln -sf $(build-classpath excalibur/avalon-framework-impl) .
#rap not needed?#ln -sf $(build-classpath commons-codec) .
popd
pushd build/output/jboss-%{jbver}/server/default/lib
#rap not needed?#ln -sf $(build-classpath commons-codec) .
popd
pushd build/output/jboss-%{jbver}/server/minimal/lib
#rap not needed?#ln -sf $(build-classpath commons-codec) .
popd
pushd testsuite
export ANT_OPTS="-Xmx512m $ANT_GRL_OPTS"

#   build the testsuite
ant17  most

# You may want to change JVM here, or even for different test groups
# export JAVA_HOME=/usr/lib/jvm/java-1.4.2-ibm

#   Validate the minimal config
ant17  jboss-minimal-tests

#   The units tests which are run against the jboss all config
#ant jboss-all-config-tests

#   Tests targeting the deployment service
#ant deployment-service-tests

#   Tests run against a custom netboot configuration
#ant netboot-tests

#   Test that apache can be started/stopped from ant
#ant tests-apache

#   Execute clustering tests requiring an apache load balanced two TC nodes.
#ant tests-apache-tomcat-clustering

#   Execute clustering tests requiring two nodes.
#ant tests-clustering

#   Execute clustering tests requiring two nodes.
#ant tests-clustering-all-stacks

#   Checks compatibility on SerialUUID
#ant tests-compatibility

#   Execute deployment Tests
#ant tests-deployment

#   Execute ha tests.
#ant tests-ha

#   Tests run against a jboss server with JACC configured
#ant tests-jacc-security

#   Tests run against a jboss server with JACC configured + security manager
#ant tests-jacc-securitymgr

#   Test that two jboss cluster nodes can be started/stopped from ant
#ant tests-jboss-cluster

#   Execute JBoss.NET Tests
#ant tests-jbossnet

#   Executes only the version check compatibility suite. Use -Dmatrix-versions=[version container] for this task
#ant tests-matrix

#   Tests run against a jboss server with a security manager
#ant tests-security-manager

#   Execute all stress tests.
#ant tests-stress

#   Execute JBossWS Tests
#ant tests-webservice

#   Tomcat tests requiring an SSL connector
#ant tests-webservice-ssl

#   Tomcat tests requiring an SSL connector
#ant tomcat-ssl-tests

#   Tomcat tests requiring clustered SSO configured
#ant tomcat-sso-clustered-tests

#   Tomcat tests requiring SSO configured
#ant tomcat-sso-tests


popd
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{without_modulesonly}
# Copy DTD catalog into place
install -m 644 %{SOURCE4} build/output/jboss-%{jbver}/docs/dtd/catalog
%endif
%endif
%endif


%install

# Global configuration file
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}
cat > jboss4.conf << EOT
# System-wide configuration file for jboss4 services
# This will be sourced by jboss4 and any secondary service
# Values will be overridden by service-specific configuration
# files in /etc/sysconfig
# Use this one to change default values for all services
# Change the service specific ones to affect only one service
# (see, for instance, /etc/sysconfig/jboss4)
#
# To change a setting, uncomment the line and set the value for what you want
# The values in the comments are the default values, shown here for convenience
#
EOT
cat %{SOURCE3} >> jboss4.conf
install -m 644 jboss4.conf $RPM_BUILD_ROOT%{_sysconfdir}
rm jboss4.conf
# Service-specific configuration file
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
cat > jboss4 << EOT
# Service-specific configuration file for jboss4 services
# This will be sourced by the SysV service script after the global
# configuration file /etc/jboss4.conf, thus allowing values
# to be overridden on a per-service way
#
# NEVER change the init script itself:
# To change values for all services make your changes in
# /etc/jboss4.conf
# To change values for a specific service, change it here
# To create a new service, create a link from /etc/init.d/<you new service> to
# /etc/init.d/jboss4 (do not copy the init script) and make a copy of the
# /etc/sysconfig/jboss4 file to /etc/sysconfig/<you new service> and change
# the property values so the two services won't conflict
# Register the new service in the system as usual (see chkconfig and similars)
#
# To change a setting, uncomment the line and set the value for what you want
# The values in the comments are the default values, shown here for convenience
#
EOT
cat %{SOURCE3} >> jboss4
install -m 644 jboss4 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
rm jboss4

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

%if %{without_coreonly}
%if %{without_basiconly}
# install aspects
install -m 644 aspects/output/lib/jboss-aspect-library32.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-aspect-library32-%{version}.jar
install -m 644 aspects/output/lib/jboss-aspect-library.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-aspect-library-%{version}.jar
#install -m 644 aspects/output/lib/jboss-aspect-jdk50-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-aspect-jdk50-client-%{version}.jar
#install -m 644 aspects/output/lib/jboss-aspect-library-jdk50.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-aspect-library-jdk50-%{version}.jar
#install -m 644 aspects/output/lib/jboss-aspect-library-jdk50-jb32.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-aspect-library-jdk50-jb32-%{version}.jar
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
# install cluster
install -m 644 cluster/output/lib/jbossha.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jbossha-%{version}.jar
install -m 644 cluster/output/lib/jbossha-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jbossha-client-%{version}.jar
%endif
%endif

# install common
install -m 644 common/output/lib/jboss-common.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-common-%{version}.jar
install -m 644 common/output/lib/jboss-common-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-common-client-%{version}.jar
install -m 644 common/output/lib/namespace.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/namespace-%{version}.jar
install -m 644 common/output/lib/testsuite-support.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/common-testsuite-support-%{version}.jar
install -m 644 common/output/lib/jboss-xml-binding.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-xml-binding-%{version}.jar
#notneededanylonger#install -m 644 common/output/lib/jboss-xml-binding2.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-xml-binding2-%{version}.jar

# install test
install -m 644 test/output/lib/jboss-test.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-test-%{version}.jar

%if %{without_coreonly}
%if %{without_basiconly}
# install connector
install -m 644 connector/output/lib/jboss-common-jdbc-wrapper.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-common-jdbc-wrapper-%{version}.jar
install -m 644 connector/output/lib/jbosscx-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jbosscx-client-%{version}.jar
install -m 644 connector/output/lib/jboss-jca.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-jca-%{version}.jar
install -m 644 connector/output/lib/jboss-local-jdbc.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-local-jdbc-%{version}.jar
install -m 644 connector/output/lib/jboss-xa-jdbc.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-xa-jdbc-%{version}.jar
install -m 644 connector/output/lib/jboss-ha-xa-jdbc.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-ha-xa-jdbc-%{version}.jar
install -m 644 connector/output/lib/jms-ra.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jms-ra-%{version}.jar
install -m 644 connector/output/lib/mail-ra.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/mail-ra-%{version}.jar
install -m 644 connector/output/lib/quartz-ra.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/quartz-ra-%{version}.jar
install -m 644 connector/output/lib/jboss-ha-local-jdbc.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-ha-local-jdbc-%{version}.jar
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
# install console
install -m 644 console/output/lib/applet.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/applet-%{version}.jar
install -m 644 console/output/lib/console.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/console-%{version}.jar
install -m 644 console/output/lib/console-mgr-classes.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/console-mgr-classes-%{version}.jar
install -m 644 console/output/lib/jboss-console-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-console-client-%{version}.jar
install -m 644 console/output/lib/jboss-console.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-console-%{version}.jar
install -m 644 console/output/lib/snmp-support.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/snmp-support-%{version}.jar
install -m 644 console/output/lib/twiddle.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/twiddle-%{version}.jar
%endif
%endif

%if %{without_coreonly}
# install deployment
install -m 644 deployment/output/lib/jboss-deployment.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-deployment-%{version}.jar
install -m 644 deployment/output/lib/jboss-jsr88.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-jsr88-%{version}.jar
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{with_hibernate}
# install hibernate
install -m 644 hibernate-int/output/lib/jboss-hibernate.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-hibernate-%{version}.jar
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{with_hibernate}
%if 0
# install ejb3
install -m 644 ejb3/output/lib/hibernate-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/hibernate-client-%{version}.jar
install -m 644 ejb3/output/lib/jboss-annotations-ejb3.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-annotations-ejb3-%{version}.jar
install -m 644 ejb3/output/lib/jboss-ejb3-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-ejb3-client-%{version}.jar
install -m 644 ejb3/output/lib/jboss-ejb3.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-ejb3-%{version}.jar
%endif
%endif
%endif
%endif

# ejb3x/output/lib/jboss-ejb3x.jar
%if %{without_coreonly}
%if %{without_basiconly}
%if %{with_hibernate}
%if 0
# install ejb3x
install -m 644 ejb3x/output/lib/jboss-ejb3x.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-ejb3x-%{version}.jar
%endif
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
# install iiop
install -m 644 iiop/output/lib/jboss-iiop.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-iiop-%{version}.jar
install -m 644 iiop/output/lib/jboss-iiop-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-iiop-client-%{version}.jar
%endif
%endif

%if %{without_coreonly}
# install j2ee
install -m 644 j2ee/output/lib/jboss-j2ee.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-j2ee-%{version}.jar
install -m 644 j2ee/output/lib/jboss-jaxrpc.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-jaxrpc-%{version}.jar
install -m 644 j2ee/output/lib/jboss-saaj.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-saaj-%{version}.jar
%endif

%if %{without_coreonly}
%if %{without_basiconly}
# install jaxrpc
install -m 644 jaxrpc/output/lib/axis-ws4ee.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/axis-ws4ee-%{version}.jar
%endif
%endif

# dropped from JB404
%if 0
%if %{without_coreonly}
%if %{without_basiconly}
# install jboss.net
install -m 644 jboss.net/output/lib/jboss-net-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-net-client-%{version}.jar
install -m 644 jboss.net/output/lib/jboss-net.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-net-%{version}.jar
install -m 644 jboss.net/output/lib/jboss-net-taglib.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-net-taglib-%{version}.jar
install -m 644 jboss.net/output/lib/xdoclet-module-jboss-net.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xdoclet-module-jboss-net-%{version}.jar
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
# install jms
install -m 644 jms/output/lib/jboss-JMS.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-JMS-%{version}.jar
%endif
%endif

# install jmx
install -m 644 jmx/output/lib/jboss-jmx-core.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-jmx-core-%{version}.jar
install -m 644 jmx/output/lib/jboss-jmx.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-jmx-%{version}.jar
install -m 644 jmx/output/lib/jboss-jmx-services.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-jmx-services-%{version}.jar
install -m 644 jmx/output/lib/jboss-jmx-testsuite.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-jmx-testsuite-%{version}.jar

%if %{without_coreonly}
%if %{without_basiconly}
# install jmx-remoting
install -m 644 jmx-remoting/output/lib/jboss-jmx-remoting.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-jmx-remoting-%{version}.jar
install -m 644 jmx-remoting/output/lib/jboss-jmx-remoting-testsuite.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-jmx-remoting-testsuite-%{version}.jar
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
# install management
install -m 644 management/output/lib/ejb-management.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/ejb-management-%{version}.jar
install -m 644 management/output/lib/jboss-jsr77-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-jsr77-client-%{version}.jar
install -m 644 management/output/lib/jboss-jsr77.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-jsr77-%{version}.jar
install -m 644 management/output/lib/jboss-management.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-management-%{version}.jar
%endif
%endif

%if 0
# install media
install -m 644 media/output/lib/jboss-jsr86.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-jsr86-%{version}.jar
install -m 644 media/output/lib/jboss-media-entity-ejb.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-media-entity-ejb-%{version}.jar
install -m 644 media/output/lib/jboss-media.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-media-%{version}.jar
# Omitted because of non-free jmf (B)R
%endif

%if %{without_coreonly}
%if %{without_basiconly}
# install messaging
install -m 644 messaging/output/lib/jbossmq-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jbossmq-client-%{version}.jar
install -m 644 messaging/output/lib/jbossmq.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jbossmq-%{version}.jar
%endif
%endif

# install naming
install -m 644 naming/output/lib/jnp-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jnp-client-%{version}.jar
install -m 644 naming/output/lib/jnpserver.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jnpserver-%{version}.jar
install -m 644 naming/output/lib/jnp-tests.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jnp-tests-%{version}.jar

%if %{without_coreonly}
%if %{without_basiconly}
# install remoting-int
install -m 644 remoting-int/output/lib/jboss-remoting-int.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-remoting-int-%{version}.jar
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
# install security
install -m 644 security/output/lib/jbosssx-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jbosssx-client-%{version}.jar
install -m 644 security/output/lib/jbosssx.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jbosssx-%{version}.jar
%endif
%endif

%if %{without_coreonly}
# install server
install -m 644 server/output/lib/jboss-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-client-%{version}.jar
install -m 644 server/output/lib/jboss.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-%{version}.jar
install -m 644 server/output/lib/jboss-minimal.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-minimal-%{version}.jar
#404#install -m 644 server/output/lib/jboss-security.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-security-%{version}.jar
install -m 644 server/output/lib/jmx-adaptor-plugin.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jmx-adaptor-plugin-%{version}.jar
install -m 644 server/output/lib/jmx-invoker-adaptor-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jmx-invoker-adaptor-client-%{version}.jar
install -m 644 server/output/lib/shutdown.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/shutdown-%{version}.jar
install -m 644 server/output/lib/verifier.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/verifier-%{version}.jar
install -m 644 server/output/lib/testsuite-support.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/server-testsuite-support-%{version}.jar
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{with_hibernate}
# install spring-int
install -m 644 spring-int/output/lib/jboss-spring.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-spring-%{version}.jar
#install -m 644 spring-int/output/lib/jboss-spring-jdk5.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-spring-jdk5-%{version}.jar
%endif
%endif
%endif

# install system
install -m 644 system/output/lib/jboss-boot.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-boot-%{version}.jar
install -m 644 system/output/lib/jboss-system-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-system-client-%{version}.jar
install -m 644 system/output/lib/jboss-system.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-system-%{version}.jar
install -m 644 system/output/lib/log4j-boot.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/log4j-boot-%{version}.jar
install -m 644 system/output/lib/run.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/run-%{version}.jar
install -m 644 system/output/lib/testsuite-support.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/system-testsuite-support-%{version}.jar

%if %{without_coreonly}
# install transaction
install -m 644 transaction/output/lib/jboss-transaction-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-transaction-client-%{version}.jar
install -m 644 transaction/output/lib/jboss-transaction.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-transaction-%{version}.jar
install -m 644 transaction/output/lib/testsuite-support.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/transaction-testsuite-support-%{version}.jar
%endif

%if %{without_coreonly}
%if %{without_basiconly}
# install varia
install -m 644 varia/output/lib/autonumber-plugin.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/autonumber-plugin-%{version}.jar
install -m 644 varia/output/lib/bindingservice-plugin.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/bindingservice-plugin-%{version}.jar
install -m 644 varia/output/lib/bsh-deployer.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/bsh-deployer-%{version}.jar
install -m 644 varia/output/lib/counter-plugin.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/counter-plugin-%{version}.jar
install -m 644 varia/output/lib/deployment-service.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/deployment-service-%{version}.jar
install -m 644 varia/output/lib/derby-plugin.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/derby-plugin-%{version}.jar
install -m 644 varia/output/lib/hsqldb.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/hsqldb-%{version}.jar
install -m 644 varia/output/lib/hsqldb-plugin.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/hsqldb-plugin-%{version}.jar
install -m 644 varia/output/lib/jbossjmx-ant.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jbossjmx-ant-%{version}.jar
install -m 644 varia/output/lib/jboss-srp.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-srp-%{version}.jar
install -m 644 varia/output/lib/jboss-srp-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-srp-client-%{version}.jar
install -m 644 varia/output/lib/jboss-monitoring.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-monitoring-%{version}.jar
install -m 644 varia/output/lib/mail-plugin.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/mail-plugin-%{version}.jar
install -m 644 varia/output/lib/process-plugin.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/process-plugin-%{version}.jar
install -m 644 varia/output/lib/properties-plugin.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/properties-plugin-%{version}.jar
install -m 644 varia/output/lib/scheduler-plugin-example.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/scheduler-plugin-example-%{version}.jar
install -m 644 varia/output/lib/scheduler-plugin.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/scheduler-plugin-%{version}.jar
install -m 644 varia/output/lib/snmp-adaptor.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/snmp-adaptor-%{version}.jar
install -m 644 varia/output/lib/statscollector.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/statscollector-%{version}.jar
install -m 644 varia/output/lib/jboss-bean-deployer.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-bean-deployer-%{version}.jar
install -m 644 varia/output/lib/juddisaaj.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/juddisaaj-%{version}.jar
install -m 644 varia/output/lib/juddi-service.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/juddi-service-%{version}.jar
install -m 644 varia/output/lib/logging-monitor.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/logging-monitor-%{version}.jar
install -m 644 varia/output/lib/xmlentitymgr.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xmlentitymgr-%{version}.jar
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
# install webservice
install -m 644 webservice/output/lib/jboss-ws4ee-client.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-ws4ee-client-%{version}.jar
install -m 644 webservice/output/lib/jboss-ws4ee.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-ws4ee-%{version}.jar
%endif
%endif


# create all versionless symlinks
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

%if %{without_coreonly}
%if %{without_basiconly}
%if %{without_modulesonly}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}

# install testsuite
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite
cp -pr testsuite/output $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite
cp -pr testsuite/imports $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite
install -m 755 %{SOURCE9} $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite/jboss-minimal-tests.sh
install -m 755 %{SOURCE10} $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite/jboss-all-config-tests.sh
install -m 755 %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite/jboss-tests-aop-scoped.sh
install -m 755 %{SOURCE12} $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite/jboss-tests-compatibility.sh
install -m 755 %{SOURCE13} $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite/jboss-tests-jacc-security-external.sh
install -m 755 %{SOURCE14} $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite/jboss-tests-jacc-securitymgr.sh
install -m 755 %{SOURCE15} $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite/jboss-tests-report-html.sh
install -m 755 %{SOURCE16} $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite/jboss-tests-security-manager.sh
install -m 644 %{SOURCE98} $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite/imports/server-config.xml
install -m 755 %{SOURCE99} $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite/jboss-tests.sh
install -m 644 testsuite/build.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite
install -m 644 testsuite/build-integration.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite/src/main/org/jboss/test/classloader/scoping/singleton
install -m 644 \
	testsuite/src/main/org/jboss/test/classloader/scoping/singleton/MySingleton_V1.txt \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite/src/main/org/jboss/test/classloader/scoping/singleton
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite/src/main/org/jboss/test/cts/interfaces
install -m 644 \
	testsuite/src/main/org/jboss/test/cts/interfaces/CtsCmp2Local_V1.txt \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite/src/main/org/jboss/test/cts/interfaces
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite/src/stylesheets
install -m 644 testsuite/src/stylesheets/*.xsl $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite/src/stylesheets
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/tools/etc/buildmagic
install -m 644 tools/etc/buildmagic/version-info.xml \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/tools/etc/buildmagic
install -m 644 tools/etc/buildmagic/build-common.xml \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/tools/etc/buildmagic
install -m 644 tools/etc/buildmagic/task.properties \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/tools/etc/buildmagic
install -m 644 %{SOURCE8} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/tools/etc/buildmagic/modules.ent
cp -pr thirdparty $RPM_BUILD_ROOT%{_datadir}/%{name}
find $RPM_BUILD_ROOT%{_datadir}/%{name}/thirdparty -name "*.sav" -exec rm -f {} \;
find $RPM_BUILD_ROOT%{_datadir}/%{name}/thirdparty -name "*.jar.no" -exec rm -f {} \;
sed -e 's|@codebase@|${jboss.home}|' testsuite/src/resources/jmx/archivestest-service.xml > $RPM_BUILD_ROOT%{_datadir}/%{name}/testsuite/output/lib/archivestest-service.xml

# install jboss main package, servers and client
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/bin

cp -a build/output/jboss-%{jbver}/bin/* \
                  $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/{jboss_init_hpux.sh,jboss_init_suse.sh,jboss_init_redhat.sh,*.bat}

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -a build/output/jboss-%{jbver}/docs/* \
                  $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
pushd $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/examples/ws4ee/jboss-ws4ee.sar
rm axis-ws4ee.jar
ln -sf %{_javadir}/%{name}/axis-ws4ee.jar .
rm jboss-ws4ee.jar
ln -sf %{_javadir}/%{name}/jboss-ws4ee.jar .
rm commons-discovery.jar
ln -sf %{_javadir}/commons-discovery.jar .
popd
pushd $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/examples/jmx
rm ejb-management.jar
ln -sf %{_javadir}/%{name}/ejb-management.jar .
pushd logging-monitor/lib
rm logging-monitor.jar
ln -sf %{_javadir}/%{name}/logging-monitor.jar .
popd
popd
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/api
ln -sf %{_javadocdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/api

%if 0
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/examples/media/
cp media/output/lib/jboss-media-entity-ejb.jar \
                  $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/examples/media/
# Omitted because of non-free jmf (B)R
%endif

install -d -m 755 $RPM_BUILD_ROOT{%{jbossdir},%_initdir}
# %{_sysconfdir}/logrotate.d}

rm -rf build/output/jboss-%{jbver}/server/minimal/log/*
rm -rf build/output/jboss-%{jbver}/server/default/log/*
rm -rf build/output/jboss-%{jbver}/server/default/tmp/*
rm -rf build/output/jboss-%{jbver}/server/default/work/*
rm -rf build/output/jboss-%{jbver}/server/all/log/*
rm -rf build/output/jboss-%{jbver}/server/all/tmp/*
rm -rf build/output/jboss-%{jbver}/server/all/work/*
cp -a build/output/jboss-%{jbver}/{client,lib} $RPM_BUILD_ROOT%{jbossdir}/
install -d -m 755 $RPM_BUILD_ROOT%{jbossdir}/server
cp -a build/output/jboss-%{jbver}/server/{all,default,minimal} \
                                        $RPM_BUILD_ROOT%{jbossdir}/server/
mkdir -p $RPM_BUILD_ROOT%{jbossdir}/server/default/data
ln -s %{jbossdir}/client $RPM_BUILD_ROOT%{_datadir}/%{name}/client
ln -s %{jbossdir}/lib $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
ln -s %{jbossdir}/server $RPM_BUILD_ROOT%{_datadir}/%{name}/server
ln -s $RPM_DOC_DIR/%{name}-%{version} $RPM_BUILD_ROOT%{jbossdir}/docs
ln -s $RPM_DOC_DIR/%{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/%{name}/docs

for server in all default minimal; do
  install -d -m 755 $RPM_BUILD_ROOT%{logdir}/jboss4/$server
  install -d -m 755 $RPM_BUILD_ROOT%{tmpdir}/jboss4/$server
  install -d -m 755 $RPM_BUILD_ROOT%{jbossdir}/server/$server/db
  install -d -m 755 $RPM_BUILD_ROOT%{jbossdir}/server/$server/data
  ln -s %{logdir}/jboss4/$server \
    $RPM_BUILD_ROOT%{jbossdir}/server/$server/log
done

# no server.properties in binary dist
#404#sed -e 's;/var/cache/jboss;%{tmpdir}/jboss4;' < %{SOURCE5} \
#404#  > $RPM_BUILD_ROOT/%{jbossdir}/server/all/conf/server.properties
# no server.properties in binary dist
#404#sed -e 's;/var/cache/jboss;%{tmpdir}/jboss4;' < %{SOURCE6} \
#404#  > $RPM_BUILD_ROOT/%{jbossdir}/server/default/conf/server.properties
# no server.properties in binary dist
#404#sed -e 's;/var/cache/jboss;%{tmpdir}/jboss4;' < %{SOURCE7} \
#404#  > $RPM_BUILD_ROOT/%{jbossdir}/server/minimal/conf/server.properties

# @@@ TODO: use a find script to generate filelists for files section?

install -m 0755 %{SOURCE1}  $RPM_BUILD_ROOT%_initdir/jboss4
sed -e 's;__VAR__;%{_localstatedir};g' \
  -e 's;__INITDIR__;%_initdir;g' \
  -e 's;__ETC__;%{_sysconfdir};g' \
< %{SOURCE1} > $RPM_BUILD_ROOT%_initdir/jboss4
#install -m 0755 %{SOURCE1}  $RPM_BUILD_ROOT%_initdir/jboss4

#### sed -e 's;__JBOSS_HOME__;%{jbossdir};g' \
####   < %{SOURCE2} > $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/jboss

###sed -e 's;__JBOSS_HOME__;/usr/share/jboss4;g' \
###  -e 's;__ETC__;%{_sysconfdir};g' \
###  -e 's;__JAVA_FUNCTIONS__;%{_datadir}/java-utils/java-functions;g' \
###  < %{SOURCE3} > $RPM_BUILD_ROOT%{_sysconfdir}/jboss4.conf

pushd $RPM_BUILD_ROOT%{jbossdir}/lib
rm -f avalon-framework-api.jar
ln -sf $(build-classpath excalibur/avalon-framework-api)
rm -f avalon-framework-impl.jar
ln -sf $(build-classpath excalibur/avalon-framework-impl)
rm -f commons-httpclient.jar
ln -sf $(build-classpath commons-httpclient)
rm -f commons-logging.jar
ln -sf $(build-classpath commons-logging)
rm -f concurrent.jar
ln -sf $(build-classpath concurrent)
rm -f dom4j.jar
ln -sf $(build-classpath dom4j)
rm -f jaxen.jar
ln -sf $(build-classpath jaxen)
pushd endorsed
rm -f resolver.jar
ln -sf $(build-classpath xml-commons-resolver) resolver.jar
rm -f xalan.jar
ln -sf $(build-classpath xalan-j2) xalan.jar
rm -f xalan-j2-serializer.jar
ln -sf $(build-classpath xalan-j2-serializer) xalan-serializer.jar
rm -f xercesImpl.jar
ln -sf $(build-classpath xerces-j2) xercesImpl.jar
rm -f xml-apis.jar
ln -sf $(build-classpath xml-commons-jaxp-1.3-apis) xml-apis.jar
popd
rm -f getopt.jar
ln -sf $(build-classpath gnu-getopt) getopt.jar
# no gnu-regexp.jar in binary dist
rm -f gnu-regexp.jar
ln -sf $(build-classpath gnu-regexp)
rm -f webdavlib.jar
ln -sf $(build-classpath slide/slide-webdavclient-webdavlib) webdavlib.jar
### jboss module stuff
rm -f jboss-common.jar
ln -sf %{_javadir}/%{name}/jboss-common.jar
rm -f jboss-jmx.jar
ln -sf %{_javadir}/%{name}/jboss-jmx.jar
rm -f jboss-system.jar
ln -sf %{_javadir}/%{name}/jboss-system.jar
rm -f jboss-xml-binding.jar
ln -sf %{_javadir}/%{name}/jboss-xml-binding.jar
# Note: not replacing lib/log4j-boot.jar with our (full) one.
rm -f log4j-boot.jar
ln -sf %{_javadir}/%{name}/log4j-boot.jar
rm -f namespace.jar
ln -sf %{_javadir}/%{name}/namespace.jar
popd

pushd $RPM_BUILD_ROOT%{jbossdir}/client
rm -f activation.jar
ln -sf $(build-classpath sun-jaf) activation.jar
rm -f antlr.jar
ln -sf $(build-classpath antlr)
rm -f avalon-framework-api.jar
ln -sf $(build-classpath excalibur/avalon-framework-api)
rm -f avalon-framework-impl.jar
ln -sf $(build-classpath excalibur/avalon-framework-impl)
rm -f jboss-backport-concurrent.jar
ln -sf $(build-classpath backport-util-concurrent) jboss-backport-concurrent.jar
# commons-discovery.jar not in binary dist
#rm -f commons-discovery.jar
#ln -sf $(build-classpath commons-discovery) commons-discovery.jar
rm -f commons-httpclient.jar
ln -sf $(build-classpath commons-httpclient)
rm -f commons-logging.jar
ln -sf $(build-classpath commons-logging)
rm -f concurrent.jar
ln -sf $(build-classpath concurrent)
rm -f getopt.jar
ln -sf $(build-classpath gnu-getopt) getopt.jar
rm -f jacorb.jar
ln -sf $(build-classpath jacorb-jboss4/jacorb-jboss4) jacorb.jar
rm -f javassist.jar
ln -sf $(build-classpath javassist)
rm -f javax.servlet.jar
ln -sf $(build-classpath servletapi5) javax.servlet.jar
rm -f jboss-remoting.jar
ln -sf $(build-classpath jboss-remoting)
rm -f jbossretro-rt.jar
ln -sf $(build-classpath jbossretro-rt)
rm -f jboss-serialization.jar
ln -sf $(build-classpath jboss-serialization)
rm -f log4j.jar
ln -sf $(build-classpath log4j)
rm -f logkit.jar
ln -sf $(build-classpath excalibur/avalon-logkit) logkit.jar
rm -f mail.jar
ln -sf $(build-classpath javamail) mail.jar
rm -f wsdl4j.jar
ln -sf $(build-classpath wsdl4j-jboss4) wsdl4j.jar
rm -f scout.jar
ln -sf $(build-classpath ws-scout/scout)
rm -f xmlsec.jar
ln -sf $(build-classpath xml-security) xmlsec.jar
# jboss module stuff
# axis-ws4ee.jar not in binary dist
# Only needed for ws4ee webservice stack
#ln -sf %{_javadir}/%{name}/axis-ws4ee.jar
# Don't !!! This file isn't in %{_javadir}
#rm -f jbossall-client.jar
#ln -sf %{_javadir}/%{name}/jbossall-client.jar
rm -f jboss-client.jar
ln -sf %{_javadir}/%{name}/jboss-client.jar
rm -f jboss-common-client.jar
ln -sf %{_javadir}/%{name}/jboss-common-client.jar
rm -f jbosscx-client.jar
ln -sf %{_javadir}/%{name}/jbosscx-client.jar
rm -f jboss-deployment.jar
ln -sf %{_javadir}/%{name}/jboss-deployment.jar
rm -f jbossha-client.jar
ln -sf %{_javadir}/%{name}/jbossha-client.jar
rm -f jboss-iiop-client.jar
ln -sf %{_javadir}/%{name}/jboss-iiop-client.jar
rm -f jboss-j2ee.jar
ln -sf %{_javadir}/%{name}/jboss-j2ee.jar
rm -f jboss-jaxrpc.jar
ln -sf %{_javadir}/%{name}/jboss-jaxrpc.jar
rm -f jbossjmx-ant.jar
ln -sf %{_javadir}/%{name}/jbossjmx-ant.jar
rm -f jboss-jsr77-client.jar
ln -sf %{_javadir}/%{name}/jboss-jsr77-client.jar
rm -f jbossmq-client.jar
ln -sf %{_javadir}/%{name}/jbossmq-client.jar
rm -f jboss-saaj.jar
ln -sf %{_javadir}/%{name}/jboss-saaj.jar
rm -f jbosssx-client.jar
ln -sf %{_javadir}/%{name}/jbosssx-client.jar
rm -f jboss-srp-client.jar
ln -sf %{_javadir}/%{name}/jboss-srp-client.jar
rm -f jboss-system-client.jar
ln -sf %{_javadir}/%{name}/jboss-system-client.jar
#rm -f jbossws14-client.jar
#ln -sf %{_javadir}/jbossws/jbossws14-client.jar
rm -f jboss-xml-binding.jar
ln -sf %{_javadir}/%{name}/jboss-xml-binding.jar
rm -f jboss-transaction-client.jar
ln -sf %{_javadir}/%{name}/jboss-transaction-client.jar
# jboss-ws4ee-client.jar not in binary dist
# rm -f jboss-ws4ee-client.jar
# ln -sf %{_javadir}/%{name}/jboss-ws4ee-client.jar
ln -sf %{_javadir}/%{name}/jboss-jmx-core.jar jmx-client.jar
rm -f jmx-invoker-adaptor-client.jar
ln -sf %{_javadir}/%{name}/jmx-invoker-adaptor-client.jar
rm -f jnp-client.jar
ln -sf %{_javadir}/%{name}/jnp-client.jar
rm -f namespace.jar
ln -sf %{_javadir}/%{name}/namespace.jar
popd

pushd $RPM_BUILD_ROOT%{jbossdir}/server/all/lib
rm -f activation.jar
ln -sf $(build-classpath sun-jaf) activation.jar
rm -f antlr.jar
ln -sf $(build-classpath antlr)
rm -f avalon-framework-api.jar
ln -sf $(build-classpath excalibur/avalon-framework-api)
rm -f avalon-framework-impl.jar
ln -sf $(build-classpath excalibur/avalon-framework-impl)
rm -f jboss-backport-concurrent.jar
ln -sf $(build-classpath backport-util-concurrent) jboss-backport-concurrent.jar
rm -f bcel.jar
ln -sf $(build-classpath bcel)
rm -f bsf.jar
ln -sf $(build-classpath bsf)
rm -f bsh-1.3.0.jar
ln -sf $(build-classpath bsh) bsh-1.3.0.jar
rm -f cglib.jar
ln -sf $(build-classpath cglib-nodep) cglib.jar
rm -f commons-collections.jar
ln -sf $(build-classpath commons-collections)
rm -f commons-htpclient.jar
ln -sf $(build-classpath commons-httpclient)
rm -f commons-logging.jar
ln -sf $(build-classpath commons-logging)
rm -f hibernate3.jar
ln -sf $(build-classpath hibernate32) hibernate3.jar
rm -f hsqldb.jar
ln -sf $(build-classpath hsqldb)
rm -f jboss-cache.jar
ln -sf $(build-classpath jboss-cache)
rm -f jboss-remoting.jar
ln -sf $(build-classpath jboss-remoting)
rm -f jboss-serialization.jar
ln -sf $(build-classpath jboss-serialization)
rm -f jbossretro-rt.jar
ln -sf $(build-classpath jbossretro-rt)
rm -f javassist.jar
ln -sf $(build-classpath javassist)
rm -f jacorb.jar
ln -sf $(build-classpath jacorb-jboss4/jacorb-jboss4) jacorb.jar
rm -f javax.servlet.jar
ln -sf $(build-classpath tomcat5-servlet-2.4-api) javax.servlet.jar
rm -f javax.servlet.jsp.jar
ln -sf $(build-classpath tomcat5-jsp-2.0-api) javax.servlet.jsp.jar
rm -f jgroups.jar
ln -sf $(build-classpath jgroups24) jgroups.jar
rm -f jpl-pattern.jar
ln -sf $(build-classpath gjt-jpl-pattern) jpl-pattern.jar
rm -f jpl-util.jar
ln -sf $(build-classpath gjt-jpl-util) jpl-util.jar
rm -f log4j.jar
ln -sf $(build-classpath log4j)
rm -f mail.jar
ln -sf $(build-classpath javamail) mail.jar
rm -f wsdl4j.jar
ln -sf $(build-classpath wsdl4j-jboss4) wsdl4j.jar
#ln -sf $(build-classpath xml-security) xmlsec.jar
# jboss module stuff
rm -f autonumber-plugin.jar
ln -sf %{_javadir}/%{name}/autonumber-plugin.jar
rm -f bindingservice-plugin.jar
ln -sf %{_javadir}/%{name}/bindingservice-plugin.jar
rm -f bsh-deployer.jar
ln -sf %{_javadir}/%{name}/bsh-deployer.jar
rm -f hsqldb-plugin.jar
ln -sf %{_javadir}/%{name}/hsqldb-plugin.jar
rm -f jboss-common-jdbc-wrapper.jar
ln -sf %{_javadir}/%{name}/jboss-common-jdbc-wrapper.jar
rm -f jbossha.jar
ln -sf %{_javadir}/%{name}/jbossha.jar
rm -f jboss-hibernate.jar
ln -sf %{_javadir}/%{name}/jboss-hibernate.jar
rm -f jboss-iiop.jar
ln -sf %{_javadir}/%{name}/jboss-iiop.jar
rm -f jboss-j2ee.jar
ln -sf %{_javadir}/%{name}/jboss-j2ee.jar
rm -f jboss.jar
ln -sf %{_javadir}/%{name}/jboss.jar
rm -f jboss-jaxrpc.jar
ln -sf %{_javadir}/%{name}/jboss-jaxrpc.jar
rm -f jboss-jca.jar
ln -sf %{_javadir}/%{name}/jboss-jca.jar
rm -f jboss-jsr77.jar
ln -sf %{_javadir}/%{name}/jboss-jsr77.jar
rm -f jboss-jsr88.jar
ln -sf %{_javadir}/%{name}/jboss-jsr88.jar
rm -f jboss-management.jar
ln -sf %{_javadir}/%{name}/jboss-management.jar
rm -f jboss-monitoring.jar
ln -sf %{_javadir}/%{name}/jboss-monitoring.jar
rm -f jbossmq.jar
ln -sf %{_javadir}/%{name}/jbossmq.jar
rm -f jboss-remoting-int.jar
ln -sf %{_javadir}/%{name}/jboss-remoting-int.jar
rm -f jboss-saaj.jar
ln -sf %{_javadir}/%{name}/jboss-saaj.jar
rm -f jboss-srp.jar
ln -sf %{_javadir}/%{name}/jboss-srp.jar
rm -f jbosssx.jar
ln -sf %{_javadir}/%{name}/jbosssx.jar
rm -f jboss-transaction.jar
ln -sf %{_javadir}/%{name}/jboss-transaction.jar
rm -f jmx-adaptor-plugin.jar
ln -sf %{_javadir}/%{name}/jmx-adaptor-plugin.jar
rm -f jnpserver.jar
ln -sf %{_javadir}/%{name}/jnpserver.jar
rm -f mail-plugin.jar
ln -sf %{_javadir}/%{name}/mail-plugin.jar
rm -f properties-plugin.jar
ln -sf %{_javadir}/%{name}/properties-plugin.jar
rm -f scheduler-plugin-example.jar
ln -sf %{_javadir}/%{name}/scheduler-plugin-example.jar
rm -f scheduler-plugin.jar
ln -sf %{_javadir}/%{name}/scheduler-plugin.jar
# no snmp-adaptor.jar in binary dist
rm -f snmp-adaptor.jar
ln -sf %{_javadir}/%{name}/snmp-adaptor.jar
rm -f snmp-support.jar
ln -sf %{_javadir}/%{name}/snmp-support.jar
rm -f xmlentitymgr.jar
ln -sf %{_javadir}/%{name}/xmlentitymgr.jar
popd

pushd $RPM_BUILD_ROOT%{jbossdir}/server/default/lib
rm -f activation.jar
ln -sf $(build-classpath sun-jaf) activation.jar
rm -f antlr.jar
ln -sf $(build-classpath antlr)
rm -f jboss-backport-concurrent.jar
ln -sf $(build-classpath backport-util-concurrent) jboss-backport-concurrent.jar
rm -f bcel.jar
ln -sf $(build-classpath bcel)
rm -f bsf.jar
ln -sf $(build-classpath bsf)
rm -f bsh-1.3.0.jar
ln -sf $(build-classpath bsh) bsh-1.3.0.jar
rm -f cglib.jar
ln -sf $(build-classpath cglib-nodep) cglib.jar
rm -f commons-collections.jar
ln -sf $(build-classpath commons-collections)
rm -f commons-httpclient.jar
ln -sf $(build-classpath commons-httpclient)
rm -f commons-logging.jar
ln -sf $(build-classpath commons-logging)
rm -f hibernate3.jar
ln -sf $(build-classpath hibernate32) hibernate3.jar
rm -f hsqldb.jar
ln -sf $(build-classpath hsqldb)
rm -f javassist.jar
ln -sf $(build-classpath javassist)
rm -f jboss-remoting.jar
ln -sf $(build-classpath jboss-remoting)
rm -f jbossretro-rt.jar
ln -sf $(build-classpath jbossretro-rt)
rm -f jboss-serialization.jar
ln -sf $(build-classpath jboss-serialization)
rm -f javax.servlet.jar
ln -sf $(build-classpath tomcat5-servlet-2.4-api) javax.servlet.jar
rm -f javax.servlet.jsp.jar
ln -sf $(build-classpath tomcat5-jsp-2.0-api) javax.servlet.jsp.jar
rm -f jpl-pattern.jar
ln -sf $(build-classpath gjt-jpl-pattern) jpl-pattern.jar
rm -f jpl-util.jar
ln -sf $(build-classpath gjt-jpl-util) jpl-util.jar
rm -f log4j.jar
ln -sf $(build-classpath log4j) log4j.jar
rm -f mail.jar
ln -sf $(build-classpath javamail) mail.jar
rm -f wsdl4j.jar
ln -sf $(build-classpath wsdl4j-jboss4) wsdl4j.jar
# jboss module stuff
rm -f autonumber-plugin.jar
ln -sf %{_javadir}/%{name}/autonumber-plugin.jar
rm -f bindingservice-plugin.jar
ln -sf %{_javadir}/%{name}/bindingservice-plugin.jar
rm -f bsh-deployer.jar
ln -sf %{_javadir}/%{name}/bsh-deployer.jar
rm -f hsqldb-plugin.jar
ln -sf %{_javadir}/%{name}/hsqldb-plugin.jar
rm -f jboss-common-jdbc-wrapper.jar
ln -sf %{_javadir}/%{name}/jboss-common-jdbc-wrapper.jar
rm -f jboss-hibernate.jar
ln -sf %{_javadir}/%{name}/jboss-hibernate.jar
rm -f jboss-j2ee.jar
ln -sf %{_javadir}/%{name}/jboss-j2ee.jar
rm -f jboss.jar
ln -sf %{_javadir}/%{name}/jboss.jar
rm -f jboss-jaxrpc.jar
ln -sf %{_javadir}/%{name}/jboss-jaxrpc.jar
rm -f jboss-jca.jar
ln -sf %{_javadir}/%{name}/jboss-jca.jar
rm -f jboss-jsr77.jar
ln -sf %{_javadir}/%{name}/jboss-jsr77.jar
rm -f jboss-jsr88.jar
ln -sf %{_javadir}/%{name}/jboss-jsr88.jar
rm -f jboss-management.jar
ln -sf %{_javadir}/%{name}/jboss-management.jar
rm -f jboss-monitoring.jar
ln -sf %{_javadir}/%{name}/jboss-monitoring.jar
rm -f jbossmq.jar
ln -sf %{_javadir}/%{name}/jbossmq.jar
rm -f jboss-remoting-int.jar
ln -sf %{_javadir}/%{name}/jboss-remoting-int.jar
rm -f jboss-saaj.jar
ln -sf %{_javadir}/%{name}/jboss-saaj.jar
rm -f jboss-srp.jar
ln -sf %{_javadir}/%{name}/jboss-srp.jar
rm -f jbosssx.jar
ln -sf %{_javadir}/%{name}/jbosssx.jar
rm -f jboss-transaction.jar
ln -sf %{_javadir}/%{name}/jboss-transaction.jar
rm -f jmx-adaptor-plugin.jar
ln -sf %{_javadir}/%{name}/jmx-adaptor-plugin.jar
rm -f jnpserver.jar
ln -sf %{_javadir}/%{name}/jnpserver.jar
rm -f mail-plugin.jar
ln -sf %{_javadir}/%{name}/mail-plugin.jar
rm -f properties-plugin.jar
ln -sf %{_javadir}/%{name}/properties-plugin.jar
rm -f scheduler-plugin-example.jar
ln -sf %{_javadir}/%{name}/scheduler-plugin-example.jar
rm -f scheduler-plugin.jar
ln -sf %{_javadir}/%{name}/scheduler-plugin.jar
# no snmp-adaptor.jar in binary dist
#404#ln -sf %{_javadir}/%{name}/snmp-adaptor.jar
rm -f snmp-support.jar
ln -sf %{_javadir}/%{name}/snmp-support.jar
rm -f xmlentitymgr.jar
ln -sf %{_javadir}/%{name}/xmlentitymgr.jar
popd

pushd $RPM_BUILD_ROOT%{jbossdir}/server/minimal/lib
rm -f jboss-management.jar
ln -sf %{_javadir}/%{name}/jboss-management.jar
rm -f jboss-minimal.jar
ln -sf %{_javadir}/%{name}/jboss-minimal.jar
rm -f jnpserver.jar
ln -sf %{_javadir}/%{name}/jnpserver.jar
rm -f log4j.jar
ln -sf $(build-classpath log4j) log4j.jar
popd


pushd $RPM_BUILD_ROOT%{jbossdir}/server/all/deploy/jboss-aop.deployer
rm -f trove.jar
ln -sf $(build-classpath gnu-trove) trove.jar
# no javassist.jar in binary dist
rm -f javassist.jar
ln -sf $(build-classpath javassist)
rm -f jboss-aop.jar
ln -sf $(build-classpath jboss-aop/jboss-aop)
rm -f jboss-aspect-library.jar
ln -sf /usr/share/java/jboss4/jboss-aspect-library.jar
popd

pushd $RPM_BUILD_ROOT%{jbossdir}/server/all/deploy/jboss-bean.deployer
rm jboss-container.jar
ln -sf $(build-classpath jboss-container) .
rm jboss-dependency.jar
ln -sf $(build-classpath jboss-dependency) .
rm jboss-bean-deployer.jar
ln -sf %{_javadir}/%{name}/jboss-bean-deployer.jar
rm jboss-microcontainer.jar
ln -sf $(build-classpath jboss-microcontainer/jboss-microcontainer) .
popd

pushd $RPM_BUILD_ROOT%{jbossdir}/server/all/deploy/jbossweb-tomcat55.sar
rm -f catalina.jar
ln -sf $(build-classpath tomcat5/catalina) .
rm -f catalina-manager.jar
ln -sf $(build-classpath tomcat5/catalina-manager) .
rm -f catalina-optional.jar
ln -sf $(build-classpath tomcat5/catalina-optional) .
# no commons-beanutils.jar in binary dist
rm -f commons-beanutils.jar
ln -sf $(build-classpath commons-beanutils) commons-beanutils.jar
# no commons-collections.jar in binary dist
rm -f commons-collections.jar
ln -sf $(build-classpath commons-collections)
# no commons-digester.jar in binary dist
rm -f commons-digester.jar
ln -sf $(build-classpath commons-digester)
rm -f commons-el.jar
ln -sf $(build-classpath commons-el)
rm -f commons-modeler.jar
ln -sf $(build-classpath commons-modeler) commons-modeler.jar
rm -f jasper-compiler.jar
ln -sf $(build-classpath jasper5-compiler) jasper-compiler.jar
rm -f jasper-compiler-jdt.jar
ln -sf $(build-classpath jdtcore) jasper-compiler-jdt.jar
rm -f jasper-runtime.jar
ln -sf $(build-classpath jasper5-runtime) jasper-runtime.jar
rm -f naming-resources.jar
ln -sf $(build-classpath tomcat5/naming-resources) .
rm -f servlets-default.jar
ln -sf $(build-classpath tomcat5/servlets-default) .
rm -f servlets-invoker.jar
ln -sf $(build-classpath tomcat5/servlets-invoker) .
rm -f servlets-webdav.jar
ln -sf $(build-classpath tomcat5/servlets-webdav) .
rm -f tomcat-ajp.jar
ln -sf $(build-classpath tomcat5/tomcat-ajp) .
rm -f tomcat-apr.jar
ln -sf $(build-classpath tomcat5/tomcat-apr) .
rm -f tomcat-coyote.jar
ln -sf $(build-classpath tomcat5/tomcat-coyote) .
rm -f tomcat-http.jar
ln -sf $(build-classpath tomcat5/tomcat-http) .
rm -f tomcat-util.jar
ln -sf $(build-classpath tomcat5/tomcat-util) .
mkdir -p jsf-libs
pushd jsf-libs
rm -f commons-beanutils.jar
ln -sf $(build-classpath commons-beanutils)
rm -f commons-codec.jar
ln -sf $(build-classpath commons-codec)
rm -f commons-collections.jar
ln -sf $(build-classpath commons-collections)
rm -f commons-digester.jar
ln -sf $(build-classpath commons-digester)
rm -f jstl.jar
ln -sf $(build-classpath taglibs-core) jstl.jar
# no equivalent of myfaces-all.jar in binary dist
rm -f myfaces.jar
ln -sf $(build-classpath myfaces/myfaces-all) myfaces.jar
rm -f myfaces-impl.jar
ln -sf $(build-classpath myfaces/myfaces-impl)
rm -f myfaces-api.jar
ln -sf $(build-classpath myfaces/myfaces-jsf-api) myfaces-api.jar
rm -f myfaces-jsf-api.jar
ln -sf $(build-classpath myfaces/myfaces-jsf-api)
popd
### workaround for xml status, may be temporary
##pushd ROOT.war
##mkdir -p manager
##cp xform.xsl manager
##popd
popd

pushd $RPM_BUILD_ROOT%{jbossdir}/server/all/deploy/jbossws14.sar
#rm -f jbossws14.jar
#ln -sf $(build-classpath jbossws/jbossws14) jbossws14.jar
#ln -sf %{_datadir}/jbossws/jbossws.war .
rm -f wsdl4j.jar
ln -sf $(build-classpath wsdl4j-jboss4) wsdl4j.jar
ln -sf $(build-classpath xml-security) xmlsec.jar
popd

pushd $RPM_BUILD_ROOT%{jbossdir}/server/all/deploy/juddi-service.sar
pushd juddiws.war/WEB-INF/lib
rm -f juddi.jar
ln -sf $(build-classpath juddi/juddi)
popd
rm -f juddi-service.jar
ln -sf %{_javadir}/%{name}/juddi-service.jar
rm -f juddi.jar
ln -sf $(build-classpath juddi/juddi)
rm -f juddisaaj.jar
ln -sf %{_javadir}/%{name}/juddisaaj.jar
rm -f scout.jar
ln -sf $(build-classpath ws-scout/scout)
popd

pushd $RPM_BUILD_ROOT%{jbossdir}/server/all/deploy/management/console-mgr.sar
pushd web-console.war
rm -f applet.jar
ln -sf %{_javadir}/%{name}/applet.jar
popd
rm -f jcommon.jar
ln -sf $(build-classpath jcommon) jcommon.jar
rm -f jfreechart.jar
ln -sf $(build-classpath jfreechart0) jfreechart.jar
# jboss module stuff
rm -f console-mgr-classes.jar
ln -sf %{_javadir}/%{name}/console-mgr-classes.jar
popd

pushd $RPM_BUILD_ROOT%{jbossdir}/server/all/deploy/snmp-adaptor.sar
rm -f snmp-adaptor.jar
ln -sf %{_javadir}/%{name}/snmp-adaptor.jar
popd


pushd $RPM_BUILD_ROOT%{jbossdir}/server/default/deploy/jboss-aop.deployer
rm -f trove.jar
ln -sf $(build-classpath gnu-trove) trove.jar
# no javassist.jar in binary dist
rm -f javassist.jar
ln -sf $(build-classpath javassist) .
rm -f jboss-aop.jar
ln -sf $(build-classpath jboss-aop/jboss-aop) .
rm -f jboss-aspect-library.jar
ln -sf /usr/share/java/jboss4/jboss-aspect-library.jar .
popd

pushd $RPM_BUILD_ROOT%{jbossdir}/server/default/deploy/jboss-bean.deployer
rm -f jboss-container.jar
ln -sf $(build-classpath jboss-container)
rm -f jboss-dependency.jar
ln -sf $(build-classpath jboss-dependency)
rm -f jboss-bean-deployer.jar
ln -sf %{_javadir}/%{name}/jboss-bean-deployer.jar
rm -f jboss-microcontainer.jar
ln -sf $(build-classpath jboss-microcontainer/jboss-microcontainer)
popd

pushd $RPM_BUILD_ROOT%{jbossdir}/server/default/deploy/jbossweb-tomcat55.sar
rm -f catalina.jar
ln -sf $(build-classpath tomcat5/catalina) .
rm -f catalina-manager.jar
ln -sf $(build-classpath tomcat5/catalina-manager) .
rm -f catalina-optional.jar
ln -sf $(build-classpath tomcat5/catalina-optional) .
# no commons-beanutils in binary dist
rm -f commons-beanutils.jar
ln -sf $(build-classpath commons-beanutils)
# no commons-collections in binary dist
rm -f commons-collections.jar
ln -sf $(build-classpath commons-collections)
# no commons-digester in binary dist
rm -f commons-digester.jar
ln -sf $(build-classpath commons-digester)
rm -f commons-el.jar
ln -sf $(build-classpath commons-el)
rm -f commons-modeler.jar
ln -sf $(build-classpath commons-modeler)
rm -f jasper-compiler.jar
ln -sf $(build-classpath jasper5-compiler) jasper-compiler.jar
rm -f jasper-compiler-jdt.jar
ln -sf $(build-classpath jdtcore) jasper-compiler-jdt.jar
rm -f jasper-runtime.jar
ln -sf $(build-classpath jasper5-runtime) jasper-runtime.jar
rm -f naming-resources.jar
ln -sf $(build-classpath tomcat5/naming-resources) .
rm -f servlets-default.jar
ln -sf $(build-classpath tomcat5/servlets-default) .
rm -f servlets-invoker.jar
ln -sf $(build-classpath tomcat5/servlets-invoker) .
rm -f servlets-webdav.jar
ln -sf $(build-classpath tomcat5/servlets-webdav) .
rm -f tomcat-ajp.jar
ln -sf $(build-classpath tomcat5/tomcat-ajp) .
rm -f tomcat-apr.jar
ln -sf $(build-classpath tomcat5/tomcat-apr) .
rm -f tomcat-coyote.jar
ln -sf $(build-classpath tomcat5/tomcat-coyote) .
rm -f tomcat-http.jar
ln -sf $(build-classpath tomcat5/tomcat-http) .
rm -f tomcat-util.jar
ln -sf $(build-classpath tomcat5/tomcat-util) .
mkdir -p jsf-libs
pushd jsf-libs
rm -f commons-beanutils.jar
ln -sf $(build-classpath commons-beanutils)
rm -f commons-codec.jar
ln -sf $(build-classpath commons-codec)
rm -f commons-collections.jar
ln -sf $(build-classpath commons-collections)
rm -f commons-digester.jar
ln -sf $(build-classpath commons-digester)
rm -f jstl.jar
ln -sf $(build-classpath taglibs-core) jstl.jar
# no equivatent of myfaces-all.jar in binary dist
rm -f myfaces.jar
ln -sf $(build-classpath myfaces/myfaces-all) myfaces.jar
rm -f myfaces-impl.jar
ln -sf $(build-classpath myfaces/myfaces-impl) myfaces-impl.jar
rm -f myfaces-api.jar
ln -sf $(build-classpath myfaces/myfaces-jsf-api) myfaces-api.jar
rm -f myfaces-jsf-api.jar
ln -sf $(build-classpath myfaces/myfaces-jsf-api) myfaces-jsf-api.jar
popd
### workaround for xml status, may be temporary
##pushd ROOT.war
##mkdir -p manager
##cp xform.xsl manager
##popd
popd

pushd $RPM_BUILD_ROOT%{jbossdir}/server/default/deploy/jbossws14.sar
#rm -f jbossws14.jar
#ln -sf $(build-classpath jbossws/jbossws14) jbossws14.jar
#ln -sf %{_datadir}/jbossws/jbossws.war .
rm -f wsdl4j.jar
ln -sf $(build-classpath wsdl4j-jboss4) wsdl4j.jar
rm -f xmlsec.jar
ln -sf $(build-classpath xml-security) xmlsec.jar
popd


pushd $RPM_BUILD_ROOT%{jbossdir}/server/default/deploy/management/console-mgr.sar
pushd web-console.war
rm -f applet.jar
ln -sf %{_javadir}/%{name}/applet.jar
popd
rm -f jcommon.jar
ln -sf $(build-classpath jcommon) jcommon.jar
rm -f jfreechart.jar
ln -sf $(build-classpath jfreechart0) jfreechart.jar
# jboss module stuff
rm -f console-mgr-classes.jar
ln -sf %{_javadir}/%{name}/console-mgr-classes.jar
popd

%endif
%endif
%endif

# ---------------------------------------------------------------------------
%if %{without_coreonly}
# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/output/jboss-%{jbver}/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%endif

# ---------------------------------------------------------------------------
%if %{without_coreonly}
%if %{without_basiconly}
%if %{without_modulesonly}

%pre
JBOSS_SHELL=/bin/false
#[ -x /sbin/nologin ] && JBOSS_SHELL=/sbin/nologin
groupadd -r %{name} 2>/dev/null || :
TOMCAT_GROUP=$(stat -c '%G' /etc/tomcat5/tomcat-users.xml)
useradd -c JBoss -r -s $JBOSS_SHELL -d /usr/share/%{name} -g %{name} -G $TOMCAT_GROUP %{name} 2>/dev/null || :

%preun
if [ "$1" = 0 ]; then
  # on erase
  %_initdir/%{name} stop > /dev/null 2>&1 || :
  [ -x /sbin/chkconfig ] && chkconfig --del %{name}
fi

%post
[ -x /sbin/chkconfig ] && chkconfig --add %{name} || :
# Note that we're using versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --add \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/%{name}/docs/dtd/catalog > /dev/null || :
fi

%post config-all
# We need this because the server/log dirs are ghosts (which in turn
# we need for smooth upgrade experience from previous versions).
if [ ! -e %{jbossdir}/server/all/log ]; then
    ln -sf %{logdir}/%{name}/all %{jbossdir}/server/all/log
fi

%post config-default
# We need this because the server/log dirs are ghosts (which in turn
# we need for smooth upgrade experience from previous versions).
if [ ! -e %{jbossdir}/server/default/log ]; then
    ln -sf %{logdir}/%{name}/default %{jbossdir}/server/default/log
fi

%post config-minimal
# We need this because the server/log dirs are ghosts (which in turn
# we need for smooth upgrade experience from previous versions).
if [ ! -e %{jbossdir}/server/minimal/log ]; then
    ln -sf %{logdir}/%{name}/minimal %{jbossdir}/server/minimal/log
fi

%postun
if [ "$1" -ge 1 ]; then
  # on upgrade
  %_initdir/%{name} condrestart >/dev/null 2>&1
fi
if [ "$1" = 0 ]; then
  # on erase
  userdel %{name} > /dev/null 2>&1 || :
  groupdel %{name} > /dev/null 2>&1 || :
fi
# Note that we're using versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --remove \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/%{name}/docs/dtd/catalog > /dev/null || :
fi
%endif
%endif
%endif

# ---------------------------------------------------------------------------

%if %{without_coreonly}
%if %{without_basiconly}
%if %{without_modulesonly}
%files
%defattr(0644,%{name},%{name},0755)
%attr(0755,root,root) %_initdir/%{name}
%attr(-,%{name},%{name}) %dir %{_var}/cache/%{name}
%dir %{_var}/log/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %{_datadir}/%{name}
%dir %{_var}/lib/%{name}
%dir %{_datadir}/%{name}/bin
%{_datadir}/%{name}/bin/*.conf
%{_datadir}/%{name}/bin/*.jar
%{_datadir}/%{name}/client
%dir %{_var}/lib/%{name}/client
%{_var}/lib/%{name}/client/jbossall-client.jar
%attr(0755,root,root) %{_datadir}/%{name}/bin/*.sh
%{_datadir}/%{name}/lib
%{_var}/lib/%{name}/lib
%{_datadir}/%{name}/server
%dir %{_var}/lib/%{name}/server
%{_var}/lib/%{name}/docs
%{_datadir}/%{name}/docs
%dir %{_docdir}/%{name}-%{version}
%{_docdir}/%{name}-%{version}/api
%{_docdir}/%{name}-%{version}/dtd
%{_docdir}/%{name}-%{version}/schema
# hack; explicitly added docdir if not owned
%doc %dir %attr(0755,root,root) %{_docdir}/%{name}-%{version}
%endif
%endif
%endif


%if %{without_coreonly}
%if %{without_basiconly}
%if %{without_modulesonly}
%files client
%{_var}/lib/%{name}/client/activation.jar
%{_var}/lib/%{name}/client/avalon-framework-api.jar
%{_var}/lib/%{name}/client/avalon-framework-impl.jar
# Only needed for ws4ee webservice stack
#%{_var}/lib/%{name}/client/axis-ws4ee.jar
#%{_var}/lib/%{name}/client/commons-discovery.jar
%{_var}/lib/%{name}/client/commons-logging.jar
%{_var}/lib/%{name}/client/concurrent.jar
%{_var}/lib/%{name}/client/getopt.jar
%{_var}/lib/%{name}/client/jacorb.jar
%{_var}/lib/%{name}/client/log4j.jar
%{_var}/lib/%{name}/client/logkit.jar
%{_var}/lib/%{name}/client/mail.jar
%{_var}/lib/%{name}/client/namespace.jar
%{_var}/lib/%{name}/client/wsdl4j.jar
#
%{_var}/lib/%{name}/client/jboss-client.jar
%{_var}/lib/%{name}/client/jboss-common-client.jar
%{_var}/lib/%{name}/client/jbosscx-client.jar
%{_var}/lib/%{name}/client/jboss-deployment.jar
%{_var}/lib/%{name}/client/jbossha-client.jar
%{_var}/lib/%{name}/client/jboss-iiop-client.jar
%{_var}/lib/%{name}/client/jboss-j2ee.jar
%{_var}/lib/%{name}/client/jboss-jaxrpc.jar
%{_var}/lib/%{name}/client/jbossjmx-ant.jar
%{_var}/lib/%{name}/client/jboss-jsr77-client.jar
%{_var}/lib/%{name}/client/jbossmq-client.jar
%{_var}/lib/%{name}/client/jboss-saaj.jar
%{_var}/lib/%{name}/client/jbosssx-client.jar
%{_var}/lib/%{name}/client/jboss-system-client.jar
%{_var}/lib/%{name}/client/jboss-transaction-client.jar
# Don't, triggers use of ws4ee instead of jbossws
#%{_var}/lib/%{name}/client/jboss-ws4ee-client.jar
%{_var}/lib/%{name}/client/jmx-client.jar
%{_var}/lib/%{name}/client/jmx-invoker-adaptor-client.jar
%{_var}/lib/%{name}/client/jnp-client.jar
%{_var}/lib/%{name}/client/juddisaaj.jar
%{_var}/lib/%{name}/client/scout.jar
%{_var}/lib/%{name}/client/javax.servlet.jar
%{_var}/lib/%{name}/client/jboss-remoting.jar
%{_var}/lib/%{name}/client/antlr.jar
%{_var}/lib/%{name}/client/commons-httpclient.jar
%{_var}/lib/%{name}/client/javassist.jar
%{_var}/lib/%{name}/client/jboss-backport-concurrent.jar
%{_var}/lib/%{name}/client/jboss-serialization.jar
%{_var}/lib/%{name}/client/jboss-srp-client.jar
%{_var}/lib/%{name}/client/jboss-xml-binding.jar
%{_var}/lib/%{name}/client/jbossretro-rt.jar
%{_var}/lib/%{name}/client/jbossws14-client.jar
%{_var}/lib/%{name}/client/xmlsec.jar
%config(noreplace) %{_var}/lib/%{name}/client/*.conf
%endif
%endif
%endif


%if %{without_coreonly}
%if %{without_basiconly}
%if %{without_modulesonly}
%files config-all
%defattr(0644,%{name},%{name},0755)
%attr(-,%{name},%{name}) %{_var}/cache/%{name}/all
%attr(-,%{name},%{name}) %{_var}/log/%{name}/all
%attr(-,%{name},%{name}) %dir %{_var}/lib/%{name}/server/all
%config(noreplace) %{_var}/lib/%{name}/server/all/conf
# Need write access to this.  Listed twice (see above) but we don't care :)
%attr(-,%{name},%{name}) %{_var}/lib/%{name}/server/all/data
%dir %{_var}/lib/%{name}/server/all/deploy-hasingleton
%dir %{_var}/lib/%{name}/server/all/deploy-hasingleton/jms
%config(noreplace) %{_var}/lib/%{name}/server/all/deploy-hasingleton/jms/*.xml
%{_var}/lib/%{name}/server/all/deploy-hasingleton/jms/jbossmq-httpil.sar
%dir %{_var}/lib/%{name}/server/all/deploy
%config(noreplace) %{_var}/lib/%{name}/server/all/deploy/*.xml
%attr(-,%{name},%{name}) %ghost %{_var}/lib/%{name}/server/all/db
%attr(-,%{name},%{name}) %ghost %{_var}/lib/%{name}/server/all/log
%{_var}/lib/%{name}/server/all/deploy/deploy.last
%{_var}/lib/%{name}/server/all/deploy/*.rar
%{_var}/lib/%{name}/server/all/deploy/uuid-key-generator.sar
%{_var}/lib/%{name}/server/all/deploy/jms
%{_var}/lib/%{name}/server/all/deploy/httpha-invoker.sar
%{_var}/lib/%{name}/server/all/deploy/jboss-aop.deployer
%{_var}/lib/%{name}/server/all/deploy/jboss-bean.deployer
#%{_var}/lib/%{name}/server/all/deploy/jbossha-httpsession.sar
%{_var}/lib/%{name}/server/all/deploy/jbossweb-tomcat55.sar
%{_var}/lib/%{name}/server/all/deploy/jbossws14.sar
%{_var}/lib/%{name}/server/all/deploy/snmp-adaptor.sar
%{_var}/lib/%{name}/server/all/deploy/jmx-console.war
%{_var}/lib/%{name}/server/all/deploy/management
%{_var}/lib/%{name}/server/all/deploy/juddi-service.sar
%{_var}/lib/%{name}/server/all/deploy/tc5-cluster.sar
%{_var}/lib/%{name}/server/all/farm
%{_var}/lib/%{name}/server/all/lib
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{without_modulesonly}
%files config-default
%defattr(0644,%{name},%{name},0755)
%attr(-,%{name},%{name}) %{_var}/cache/%{name}/default
%attr(-,%{name},%{name}) %{_var}/log/%{name}/default
%attr(-,%{name},%{name}) %dir %{_var}/lib/%{name}/server/default
%config(noreplace) %{_var}/lib/%{name}/server/default/conf
%attr(-,%{name},%{name}) %{_var}/lib/%{name}/server/default/data
%dir %{_var}/lib/%{name}/server/default/deploy
%config(noreplace) %{_var}/lib/%{name}/server/default/deploy/*.xml
%attr(-,%{name},%{name}) %ghost %{_var}/lib/%{name}/server/default/db
%attr(-,%{name},%{name}) %ghost %{_var}/lib/%{name}/server/default/log
%{_var}/lib/%{name}/server/default/deploy/*.rar
%{_var}/lib/%{name}/server/default/deploy/uuid-key-generator.sar
%{_var}/lib/%{name}/server/default/deploy/http-invoker.sar
%{_var}/lib/%{name}/server/default/deploy/jms
%{_var}/lib/%{name}/server/default/deploy/jboss-aop.deployer
%{_var}/lib/%{name}/server/default/deploy/jboss-bean.deployer
%{_var}/lib/%{name}/server/default/deploy/jbossweb-tomcat55.sar
%{_var}/lib/%{name}/server/default/deploy/jbossws14.sar
%{_var}/lib/%{name}/server/default/deploy/jmx-console.war
%{_var}/lib/%{name}/server/default/deploy/management
%{_var}/lib/%{name}/server/default/lib
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{without_modulesonly}
%files config-minimal
%defattr(0644,%{name},%{name},0755)
%attr(-,%{name},%{name}) %{_var}/cache/%{name}/minimal
%attr(-,%{name},%{name}) %{_var}/log/%{name}/minimal
%attr(-,%{name},%{name}) %dir %{_var}/lib/%{name}/server/minimal
%config(noreplace) %{_var}/lib/%{name}/server/minimal/conf
%attr(-,%{name},%{name}) %dir %{_var}/lib/%{name}/server/minimal/deploy
%attr(-,%{name},%{name}) %ghost %{_var}/lib/%{name}/server/minimal/db
%attr(-,%{name},%{name}) %ghost %{_var}/lib/%{name}/server/minimal/log
%{_var}/lib/%{name}/server/minimal/lib
%endif
%endif
%endif


%if %{without_coreonly}
%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{without_modulesonly}
%files manual
%{_docdir}/%{name}-%{version}/examples
%{_docdir}/%{name}-%{version}/todo
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%files aspects
%{_javadir}/%{name}/jboss-aspect-library32-%{version}.jar
%{_javadir}/%{name}/jboss-aspect-library32.jar
%{_javadir}/%{name}/jboss-aspect-library-%{version}.jar
%{_javadir}/%{name}/jboss-aspect-library.jar
#%{_javadir}/%{name}/jboss-aspect-jdk50-client-%{version}.jar
#%{_javadir}/%{name}/jboss-aspect-jdk50-client.jar
#%{_javadir}/%{name}/jboss-aspect-library-jdk50-%{version}.jar
#%{_javadir}/%{name}/jboss-aspect-library-jdk50.jar
#%{_javadir}/%{name}/jboss-aspect-library-jdk50-jb32-%{version}.jar
#%{_javadir}/%{name}/jboss-aspect-library-jdk50-jb32.jar
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%files cluster
%{_javadir}/%{name}/jbossha-%{version}.jar
%{_javadir}/%{name}/jbossha.jar
%{_javadir}/%{name}/jbossha-client-%{version}.jar
%{_javadir}/%{name}/jbossha-client.jar
%endif
%endif

%files test
%{_javadir}/%{name}/jboss-test-%{version}.jar
%{_javadir}/%{name}/jboss-test.jar

%files common
%{_javadir}/%{name}/jboss-common-%{version}.jar
%{_javadir}/%{name}/jboss-common-client-%{version}.jar
%{_javadir}/%{name}/namespace-%{version}.jar
%{_javadir}/%{name}/common-testsuite-support-%{version}.jar
%{_javadir}/%{name}/jboss-xml-binding-%{version}.jar
#notneededanylonger#%{_javadir}/%{name}/jboss-xml-binding2-%{version}.jar
%{_javadir}/%{name}/jboss-common.jar
%{_javadir}/%{name}/jboss-common-client.jar
%{_javadir}/%{name}/namespace.jar
%{_javadir}/%{name}/common-testsuite-support.jar
%{_javadir}/%{name}/jboss-xml-binding.jar
#notneededanylonger#%{_javadir}/%{name}/jboss-xml-binding2.jar

%if %{without_coreonly}
%if %{without_basiconly}
%files connector
%{_javadir}/%{name}/jboss-common-jdbc-wrapper-%{version}.jar
%{_javadir}/%{name}/jbosscx-client-%{version}.jar
%{_javadir}/%{name}/jboss-jca-%{version}.jar
%{_javadir}/%{name}/jboss-local-jdbc-%{version}.jar
%{_javadir}/%{name}/jboss-ha-local-jdbc-%{version}.jar
%{_javadir}/%{name}/jboss-xa-jdbc-%{version}.jar
%{_javadir}/%{name}/jboss-ha-xa-jdbc-%{version}.jar
%{_javadir}/%{name}/jms-ra-%{version}.jar
%{_javadir}/%{name}/mail-ra-%{version}.jar
%{_javadir}/%{name}/quartz-ra-%{version}.jar
%{_javadir}/%{name}/jboss-common-jdbc-wrapper.jar
%{_javadir}/%{name}/jbosscx-client.jar
%{_javadir}/%{name}/jboss-jca.jar
%{_javadir}/%{name}/jboss-local-jdbc.jar
%{_javadir}/%{name}/jboss-ha-local-jdbc.jar
%{_javadir}/%{name}/jboss-ha-xa-jdbc.jar
%{_javadir}/%{name}/jboss-xa-jdbc.jar
%{_javadir}/%{name}/jms-ra.jar
%{_javadir}/%{name}/mail-ra.jar
%{_javadir}/%{name}/quartz-ra.jar
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%files console
%{_javadir}/%{name}/applet-%{version}.jar
%{_javadir}/%{name}/console-%{version}.jar
%{_javadir}/%{name}/console-mgr-classes-%{version}.jar
%{_javadir}/%{name}/jboss-console-client-%{version}.jar
%{_javadir}/%{name}/jboss-console-%{version}.jar
%{_javadir}/%{name}/snmp-support-%{version}.jar
%{_javadir}/%{name}/twiddle-%{version}.jar
%{_javadir}/%{name}/applet.jar
%{_javadir}/%{name}/console.jar
%{_javadir}/%{name}/console-mgr-classes.jar
%{_javadir}/%{name}/jboss-console-client.jar
%{_javadir}/%{name}/jboss-console.jar
%{_javadir}/%{name}/snmp-support.jar
%{_javadir}/%{name}/twiddle.jar
%endif
%endif

%if %{without_coreonly}
%files deployment
%{_javadir}/%{name}/jboss-deployment-%{version}.jar
%{_javadir}/%{name}/jboss-deployment.jar
%{_javadir}/%{name}/jboss-jsr88-%{version}.jar
%{_javadir}/%{name}/jboss-jsr88.jar
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{with_hibernate}
%files hibernate-int
%{_javadir}/%{name}/jboss-hibernate-%{version}.jar
%{_javadir}/%{name}/jboss-hibernate.jar
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{with_hibernate}
%if 0
%files ejb3
%{_javadir}/%{name}/hibernate-client-%{version}.jar
%{_javadir}/%{name}/jboss-annotations-ejb3-%{version}.jar
%{_javadir}/%{name}/jboss-ejb3-client-%{version}.jar
%{_javadir}/%{name}/jboss-ejb3-%{version}.jar
%{_javadir}/%{name}/hibernate-client.jar
%{_javadir}/%{name}/jboss-annotations-ejb3.jar
%{_javadir}/%{name}/jboss-ejb3-client.jar
%{_javadir}/%{name}/jboss-ejb3.jar
%endif
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{with_hibernate}
%if 0
%files ejb3x
%{_javadir}/%{name}/jboss-ejb3x-%{version}.jar
%{_javadir}/%{name}/jboss-ejb3x.jar
%endif
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%files iiop
%{_javadir}/%{name}/jboss-iiop-%{version}.jar
%{_javadir}/%{name}/jboss-iiop-client-%{version}.jar
%{_javadir}/%{name}/jboss-iiop.jar
%{_javadir}/%{name}/jboss-iiop-client.jar
%endif
%endif

%if %{without_coreonly}
%files j2ee
%{_javadir}/%{name}/jboss-j2ee-%{version}.jar
%{_javadir}/%{name}/jboss-jaxrpc-%{version}.jar
%{_javadir}/%{name}/jboss-saaj-%{version}.jar
%{_javadir}/%{name}/jboss-j2ee.jar
%{_javadir}/%{name}/jboss-jaxrpc.jar
%{_javadir}/%{name}/jboss-saaj.jar
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%files jaxrpc
%{_javadir}/%{name}/axis-ws4ee-%{version}.jar
%{_javadir}/%{name}/axis-ws4ee.jar
%endif
%endif

%if 0
%if %{without_coreonly}
%if %{without_basiconly}
%files jboss.net
%{_javadir}/%{name}/jboss-net-client-%{version}.jar
%{_javadir}/%{name}/jboss-net-%{version}.jar
%{_javadir}/%{name}/jboss-net-taglib-%{version}.jar
%{_javadir}/%{name}/xdoclet-module-jboss-net-%{version}.jar
%{_javadir}/%{name}/jboss-net-client.jar
%{_javadir}/%{name}/jboss-net.jar
%{_javadir}/%{name}/jboss-net-taglib.jar
%{_javadir}/%{name}/xdoclet-module-jboss-net.jar
%endif
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%files jms
%{_javadir}/%{name}/jboss-JMS-%{version}.jar
%{_javadir}/%{name}/jboss-JMS.jar
%endif
%endif

%files jmx
%{_javadir}/%{name}/jboss-jmx-core-%{version}.jar
%{_javadir}/%{name}/jboss-jmx-%{version}.jar
%{_javadir}/%{name}/jboss-jmx-services-%{version}.jar
%{_javadir}/%{name}/jboss-jmx-testsuite-%{version}.jar
%{_javadir}/%{name}/jboss-jmx-core.jar
%{_javadir}/%{name}/jboss-jmx.jar
%{_javadir}/%{name}/jboss-jmx-services.jar
%{_javadir}/%{name}/jboss-jmx-testsuite.jar

%if %{without_coreonly}
%if %{without_basiconly}
%files jmx-remoting
%{_javadir}/%{name}/jboss-jmx-remoting-%{version}.jar
%{_javadir}/%{name}/jboss-jmx-remoting-testsuite-%{version}.jar
%{_javadir}/%{name}/jboss-jmx-remoting.jar
%{_javadir}/%{name}/jboss-jmx-remoting-testsuite.jar
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%files management
%{_javadir}/%{name}/ejb-management-%{version}.jar
%{_javadir}/%{name}/jboss-jsr77-client-%{version}.jar
%{_javadir}/%{name}/jboss-jsr77-%{version}.jar
%{_javadir}/%{name}/jboss-management-%{version}.jar
%{_javadir}/%{name}/ejb-management.jar
%{_javadir}/%{name}/jboss-jsr77-client.jar
%{_javadir}/%{name}/jboss-jsr77.jar
%{_javadir}/%{name}/jboss-management.jar
%endif
%endif

%if 0
%files media
%{_javadir}/%{name}/jboss-jsr86-%{version}.jar
%{_javadir}/%{name}/jboss-media-entity-ejb-%{version}.jar
%{_javadir}/%{name}/jboss-media-%{version}.jar
%{_javadir}/%{name}/jboss-jsr86.jar
%{_javadir}/%{name}/jboss-media-entity-ejb.jar
%{_javadir}/%{name}/jboss-media.jar
# Omitted because of non-free jmf (B)R
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%files messaging
%{_javadir}/%{name}/jbossmq-client-%{version}.jar
%{_javadir}/%{name}/jbossmq-%{version}.jar
%{_javadir}/%{name}/jbossmq-client.jar
%{_javadir}/%{name}/jbossmq.jar
%endif
%endif

%files naming
%{_javadir}/%{name}/jnp-client-%{version}.jar
%{_javadir}/%{name}/jnpserver-%{version}.jar
%{_javadir}/%{name}/jnp-tests-%{version}.jar
%{_javadir}/%{name}/jnp-client.jar
%{_javadir}/%{name}/jnpserver.jar
%{_javadir}/%{name}/jnp-tests.jar

%if %{without_coreonly}
%if %{without_basiconly}
%files remoting-int
%{_javadir}/%{name}/jboss-remoting-int-%{version}.jar
%{_javadir}/%{name}/jboss-remoting-int.jar
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%files security
%{_javadir}/%{name}/jbosssx-client-%{version}.jar
%{_javadir}/%{name}/jbosssx-%{version}.jar
%{_javadir}/%{name}/jbosssx-client.jar
%{_javadir}/%{name}/jbosssx.jar
%endif
%endif

%if %{without_coreonly}
%files server
%{_javadir}/%{name}/jboss-client-%{version}.jar
%{_javadir}/%{name}/jboss-%{version}.jar
%{_javadir}/%{name}/jboss-minimal-%{version}.jar
#404#%{_javadir}/%{name}/jboss-security-%{version}.jar
%{_javadir}/%{name}/jmx-adaptor-plugin-%{version}.jar
%{_javadir}/%{name}/jmx-invoker-adaptor-client-%{version}.jar
%{_javadir}/%{name}/shutdown-%{version}.jar
%{_javadir}/%{name}/verifier-%{version}.jar
%{_javadir}/%{name}/server-testsuite-support-%{version}.jar
%{_javadir}/%{name}/jboss-client.jar
%{_javadir}/%{name}/jboss.jar
%{_javadir}/%{name}/jboss-minimal.jar
#404#%{_javadir}/%{name}/jboss-security.jar
%{_javadir}/%{name}/jmx-adaptor-plugin.jar
%{_javadir}/%{name}/jmx-invoker-adaptor-client.jar
%{_javadir}/%{name}/shutdown.jar
%{_javadir}/%{name}/verifier.jar
%{_javadir}/%{name}/server-testsuite-support.jar
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{with_hibernate}
%files spring-int
%{_javadir}/%{name}/jboss-spring-%{version}.jar
%{_javadir}/%{name}/jboss-spring.jar
#%{_javadir}/%{name}/jboss-spring-jdk5-%{version}.jar
#%{_javadir}/%{name}/jboss-spring-jdk5.jar
%endif
%endif
%endif

%files system
%{_javadir}/%{name}/jboss-boot-%{version}.jar
%{_javadir}/%{name}/jboss-system-client-%{version}.jar
%{_javadir}/%{name}/jboss-system-%{version}.jar
%{_javadir}/%{name}/log4j-boot-%{version}.jar
%{_javadir}/%{name}/run-%{version}.jar
%{_javadir}/%{name}/system-testsuite-support-%{version}.jar
%{_javadir}/%{name}/jboss-boot.jar
%{_javadir}/%{name}/jboss-system-client.jar
%{_javadir}/%{name}/jboss-system.jar
%{_javadir}/%{name}/log4j-boot.jar
%{_javadir}/%{name}/run.jar
%{_javadir}/%{name}/system-testsuite-support.jar

%if %{without_coreonly}
%files transaction
%{_javadir}/%{name}/jboss-transaction-client-%{version}.jar
%{_javadir}/%{name}/jboss-transaction-%{version}.jar
%{_javadir}/%{name}/transaction-testsuite-support-%{version}.jar
%{_javadir}/%{name}/jboss-transaction-client.jar
%{_javadir}/%{name}/jboss-transaction.jar
%{_javadir}/%{name}/transaction-testsuite-support.jar
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%files varia
%{_javadir}/%{name}/autonumber-plugin-%{version}.jar
%{_javadir}/%{name}/bindingservice-plugin-%{version}.jar
%{_javadir}/%{name}/bsh-deployer-%{version}.jar
%{_javadir}/%{name}/counter-plugin-%{version}.jar
%{_javadir}/%{name}/deployment-service-%{version}.jar
%{_javadir}/%{name}/derby-plugin-%{version}.jar
%{_javadir}/%{name}/hsqldb-%{version}.jar
%{_javadir}/%{name}/hsqldb-plugin-%{version}.jar
%{_javadir}/%{name}/jbossjmx-ant-%{version}.jar
%{_javadir}/%{name}/jboss-bean-deployer-%{version}.jar
%{_javadir}/%{name}/jboss-monitoring-%{version}.jar
%{_javadir}/%{name}/jboss-srp-%{version}.jar
%{_javadir}/%{name}/jboss-srp-client-%{version}.jar
%{_javadir}/%{name}/juddisaaj-%{version}.jar
%{_javadir}/%{name}/juddi-service-%{version}.jar
%{_javadir}/%{name}/logging-monitor-%{version}.jar
%{_javadir}/%{name}/mail-plugin-%{version}.jar
%{_javadir}/%{name}/process-plugin-%{version}.jar
%{_javadir}/%{name}/properties-plugin-%{version}.jar
%{_javadir}/%{name}/scheduler-plugin-example-%{version}.jar
%{_javadir}/%{name}/scheduler-plugin-%{version}.jar
%{_javadir}/%{name}/snmp-adaptor-%{version}.jar
%{_javadir}/%{name}/statscollector-%{version}.jar
%{_javadir}/%{name}/xmlentitymgr-%{version}.jar
%{_javadir}/%{name}/autonumber-plugin.jar
%{_javadir}/%{name}/bindingservice-plugin.jar
%{_javadir}/%{name}/bsh-deployer.jar
%{_javadir}/%{name}/counter-plugin.jar
%{_javadir}/%{name}/deployment-service.jar
%{_javadir}/%{name}/derby-plugin.jar
%{_javadir}/%{name}/hsqldb.jar
%{_javadir}/%{name}/hsqldb-plugin.jar
%{_javadir}/%{name}/jbossjmx-ant.jar
%{_javadir}/%{name}/jboss-bean-deployer.jar
%{_javadir}/%{name}/jboss-monitoring.jar
%{_javadir}/%{name}/jboss-srp.jar
%{_javadir}/%{name}/jboss-srp-client.jar
%{_javadir}/%{name}/juddisaaj.jar
%{_javadir}/%{name}/logging-monitor.jar
%{_javadir}/%{name}/juddi-service.jar
%{_javadir}/%{name}/mail-plugin.jar
%{_javadir}/%{name}/process-plugin.jar
%{_javadir}/%{name}/properties-plugin.jar
%{_javadir}/%{name}/scheduler-plugin-example.jar
%{_javadir}/%{name}/scheduler-plugin.jar
%{_javadir}/%{name}/snmp-adaptor.jar
%{_javadir}/%{name}/statscollector.jar
%{_javadir}/%{name}/xmlentitymgr.jar
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%files webservice
%{_javadir}/%{name}/jboss-ws4ee-client-%{version}.jar
%{_javadir}/%{name}/jboss-ws4ee-%{version}.jar
%{_javadir}/%{name}/jboss-ws4ee-client.jar
%{_javadir}/%{name}/jboss-ws4ee.jar
%endif
%endif

%if %{without_coreonly}
%if %{without_basiconly}
%if %{without_modulesonly}
%files testsuite
%defattr(0644,jboss4,jboss4,0755)
%dir %{_datadir}/%{name}/testsuite
%{_datadir}/%{name}/testsuite/imports
%{_datadir}/%{name}/testsuite/output
%{_datadir}/%{name}/testsuite/src
%attr(755,jboss4,jboss4) %{_datadir}/%{name}/testsuite/*.sh
%{_datadir}/%{name}/testsuite/build.xml
%{_datadir}/%{name}/testsuite/build-integration.xml
%{_datadir}/%{name}/thirdparty
%{_datadir}/%{name}/tools
%endif
%endif
%endif

# -----------------------------------------------------------------------------

%changelog
* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt16_5jpp5
- build with ant17

* Mon Feb 07 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt15_5jpp5
- fixed synmlink

* Mon Feb 07 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt14_5jpp5
- build with hibernate32

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt13_5jpp5
- fixed build when with_basiconly

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt12_5jpp5
- build with jgroups24

* Mon Jan 31 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt11_5jpp5
- fixed build with new tomcat5

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt10_5jpp5
- fixed build; fixed init script (closes: #24280).

* Sat Sep 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt9_5jpp5
- ant 1.8 support

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt8_5jpp5
- explicit selection of java5 compiler

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt7_5jpp5
- rebuild with jboss-remoting 2.2.2

* Fri Mar 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt6_5jpp5
- use jboss-remoting1 compat lib (note: jboss-remoting.jar is not renamed)

* Thu Feb 25 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt5_5jpp5
- fixed jfreechart symlinks

* Thu Jan 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt4_5jpp5
- hack: temporarily fixed docdir defattr clash with jboss4-manual

* Mon Aug 31 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt3_5jpp5
- full build

* Sat Aug 08 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt2_5jpp5
- removed dep on jakarta-crimson

* Fri Aug 07 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.0.4-alt1_5jpp5
- fixed build

* Tue Dec 09 2008 Igor Vlasenko <viy@altlinux.ru> 0:4.0.3.1-alt4_5jpp5
- fixed build in jpp 5.0

* Fri Feb 22 2008 Igor Vlasenko <viy@altlinux.ru> 0:4.0.3.1-alt3_5jpp5.0
- rebuild to get rid of strange autodependency

* Wed Feb 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:4.0.3.1-alt2_5jpp5.0
- finally: complete build with all subpackages

* Thu Oct 25 2007 Igor Vlasenko <viy@altlinux.ru> 0:4.0.3.1-alt2_4jpp1.7
- basic build (was: core build)

* Tue Oct 23 2007 Igor Vlasenko <viy@altlinux.ru> 0:4.0.3.1-alt1_4jpp1.7
- converted from JPackage by jppimport script

