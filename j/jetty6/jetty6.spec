Patch33: jetty6-maven3-alt.patch
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%def_without cometd
%def_without wadi
%def_without jboss
%def_without grizzly
%def_without terracotta
%def_without xbean
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 6.1.26
%define name jetty6
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without jdk6
%bcond_without native
%bcond_without api
%bcond_with cometd
%bcond_without plus
%bcond_with wadi
%bcond_with xbean

%if %without plus
#def_with wadi
%bcond_with wadi
#def_with xbean
%bcond_with xbean
%endif

%define jtuid       90
%define username    jetty
%define jboss_home  %{_javadir}/jbossas
%define jettyname   jetty
%define servletspec 2.5
%define jspspec     2.1

# FHS 2.3 compliant tree structure - http://www.pathname.com/fhs/
%define appdir /var/lib/jetty6/webapps
%define ctxdir /var/lib/jetty6/contexts
%define confdir %{_sysconfdir}/%{name}
%define apphomedir %{_datadir}/%{name}
%define libdir %{_javadir}/%{name}
%define logdir %{_var}/log/%{name}
%define vardir %{_var}/lib/%{name}
%define tempdir %{_var}/tmp/%{name}
%define rundir  %{_var}/run/%{name}

#%%define workdir %{_var}/cache/%{name}

Name:           jetty6
Version:        6.1.26
Release:        alt5_1jpp6
Epoch:          0
Summary:        Webserver and Servlet Container
Group:          Development/Java
License:        ASL 2.0
URL:            http://www.mortbay.org/
Source0:        http://dist.codehaus.org/jetty/jetty-6.1.26/jetty-6.1.26-src.zip
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-start.config
Source4:        %{name}-jetty.conf
Source5:        %{name}.sysconfig
Source6:        djetty.script
Source7:        jetty.init
Source8:        jetty.logrotate
Source9:        http://repo1.maven.org/maven2/org/mortbay/jetty/jetty-parent/10/jetty-parent-10.pom
Source10:       http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-parent/14/jetty-parent-14.pom
Source11:       http://repo1.maven.org/maven2/org/mortbay/jetty/jetty-parent/8/jetty-parent-8.pom
Patch1:         %{name}-pom.patch
Patch3:         %{name}-extras-xbean-pom_xml.patch
Patch4:         %{name}-jsp-2.1-pom.patch
Patch5:         %{name}-dependency-plugin.patch
Patch6:         %{name}-jspc-plugin.patch
Patch7:         %{name}-maven-plugin-disable-site.patch
Patch8:         %{name}-plus-pom.patch
Patch9:         %{name}-ldap-jaas-pom.patch
Patch10:        %{name}-TerracottaSessionManager.patch
Patch11:        %{name}-spring-ebj3-demo-pom.patch
Patch13:        %{name}-cometd-ContinuationBayeux.patch
Patch15:        %{name}-contrib-wadi-WadiCluster.patch
Patch16:        %{name}-contrib-wadi-pom.patch
Patch17:        %{name}-ChannelEndPoint.patch

Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
Requires(preun): /sbin/chkconfig
Requires(post):  /sbin/chkconfig
Requires(post):  jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
BuildRequires:  jetty-jsp-2.1
BuildRequires:  servlet_2_5_api
BuildRequires:  jsp_2_1_api
#
BuildRequires:  ant >= 0:1.7
BuildRequires:  ant-junit
%if %with cometd
BuildRequires:  cometd-java-api
%endif
BuildRequires:  derby
BuildRequires:  ecj
#BuildRequires:  felix-maven2
BuildRequires:  maven-plugin-bundle
BuildRequires:  geronimo-annotation-1.0-api
BuildRequires:  geronimo-ejb-3.0-api
BuildRequires:  geronimo-jta-1.0.1B-api
BuildRequires:  geronimo-j2ee-management-1.0-api
BuildRequires:  jakarta-commons-el
BuildRequires:  jakarta-commons-parent >= 0:9
BuildRequires:  jakarta-slide-webdavclient
BuildRequires:  javamail_1_4_api
BuildRequires:  jaf_1_1_api
BuildRequires:  jmock
BuildRequires:  junit >= 0:3.8.1
BuildRequires:  maven2 >= 2.0.7
BuildRequires:  maven2-default-skin
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-dependency
BuildRequires:  maven2-plugin-enforcer
BuildRequires:  maven2-plugin-help
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven2-plugin-project-info-reports
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-site
BuildRequires:  maven2-plugin-source
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven2-plugin-war
BuildRequires:  maven-enforcer-api
BuildRequires:  maven-jxr
BuildRequires:  maven-release
BuildRequires:  maven-shared-enforcer-rule-api
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  mojo-maven2-plugin-build-helper
BuildRequires:  mojo-maven2-plugin-exec
#BuildRequires:  mojo-maven2-plugin-jboss-packaging
#BuildRequires:  mojo-maven2-natives
BuildRequires:  mojo-parent
BuildRequires:  geronimo-genesis
BuildRequires:  jetty-build-support
#BuildRequires:  mx4j
BuildRequires:  qdox
BuildRequires:  slf4j
BuildRequires:  spring-all
BuildRequires:  testng
BuildRequires:  tomcat5-jasper
BuildRequires:  tomcat6
BuildRequires:  tomcat6-lib
%if %with wadi
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-httpclient
BuildRequires:  backport-util-concurrent
BuildRequires:  cglib
BuildRequires:  concurrent
BuildRequires:  gmaven-runtime-1.6
BuildRequires:  regexp
BuildRequires:  wadi2
%endif
%if %with xbean
BuildRequires:  xbean
%endif
BuildRequires:  xpp3
BuildRequires:  xpp3-minimal
BuildArch:      noarch
Source44: import.info

%description
Jetty is a 100%% Java HTTP Server and Servlet Container.

%if %with api
%package -n %{jettyname}6-jsp-%{jspspec}

Summary:        JSP 2.1 impl from %{name}
Group:          Development/Java
Requires(post): alternatives
Requires(postun): alternatives
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jetty-jsp-2.1
Requires:       jsp_2_1_api
Requires:       servlet_2_5_api
Requires:       ant

%description -n %{jettyname}6-jsp-%{jspspec}
%{summary}.

%package -n %{jettyname}6-jsp-2.0
Summary:        JSP 2.0 impl from %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       servlet_2_5_api
Requires:       jsp_2_0_api
Requires:       ant
Requires:       jakarta-commons-el
Requires:       slf4j
Requires:       tomcat5-jasper
Provides:       jsp_impl
Provides:       jsp_2_0_impl

%description -n %{jettyname}6-jsp-2.0
%{summary}.
%endif

%package -n %{jettyname}6-core
Summary:        Core libraries for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       servlet_2_5_api
Requires:       slf4j

%description -n %{jettyname}6-core
%{summary}.


%package -n %{jettyname}6-ext
Summary:        Extension libraries for %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-plus = %{epoch}:%{version}-%{release}
Requires:       %{name}-util5 = %{epoch}:%{version}-%{release}

%description -n %{jettyname}6-ext
%{summary}.


%package -n %{jettyname}6-plus
Summary:        JavaEE style services for %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-naming = %{epoch}:%{version}-%{release}
Requires:       jta_api

%description -n %{jettyname}6-plus
%{summary}.


%package -n %{jettyname}6-annotations
Summary:        Servlet Annotations for %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-plus = %{epoch}:%{version}-%{release}
Requires:       %{name}-naming = %{epoch}:%{version}-%{release}
Requires:       annotation_1_0_api

%description -n %{jettyname}6-annotations
%{summary}.


%package -n %{jettyname}6-management
Summary:        JMX for %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
#Requires:       mx4j >= 0:3.0.1

%description -n %{jettyname}6-management
%{summary}.


%package -n %{jettyname}6-naming
Summary:        JNDI for %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       jaf_1_1_api
Requires:       javamail_1_4_api

%description -n %{jettyname}6-naming
%{summary}.


%package -n %{jettyname}6-spring
Summary:        Spring for %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-plus = %{epoch}:%{version}-%{release}
Requires:       spring

%description -n %{jettyname}6-spring
%{summary}.

%if %with xbean
%package -n %{jettyname}6-xbean
Summary:        XBean for %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-plus = %{epoch}:%{version}-%{release}
Requires:       qdox
Requires:       spring
Requires:       xbean

%description -n %{jettyname}6-xbean
%{summary}.
%endif

%package -n %{jettyname}6-maven2-plugins
Summary:        Maven2 plugins for %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-management = %{epoch}:%{version}-%{release}
Requires:       %{name}-naming = %{epoch}:%{version}-%{release}
Requires:       %{name}-plus = %{epoch}:%{version}-%{release}
Requires:       maven2
Requires:       tomcat5-jasper

%description -n %{jettyname}6-maven2-plugins
%{summary}.

%if %with cometd
%if_with cometd
%package -n %{jettyname}6-cometd
Summary:        Contributed Cometd for %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-ext = %{epoch}:%{version}-%{release}
Requires:       servlet_2_5_api
Requires:       cometd-java-api
%endif #cometd

%if_with cometd
%description -n %{jettyname}6-cometd
%{summary}.
%endif
%endif #cometd

%package -n %{jettyname}6-ant
Summary:        Contributed Ant module for %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-plus = %{epoch}:%{version}-%{release}
Requires:       %{name}-naming = %{epoch}:%{version}-%{release}
Requires:       ant >= 0:1.7.1
Requires:       servlet_2_5_api

%description -n %{jettyname}6-ant
%{summary}.

%package -n %{jettyname}6-embedded
Summary:        Embedded Jetty example from %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-ext = %{epoch}:%{version}-%{release}
Requires:       jsp_2_1_api

%description -n %{jettyname}6-embedded
%{summary}.

%if %with wadi
%if_with wadi
%package -n %{jettyname}6-wadi
Summary:        WADI session manager from %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       apache-commons-codec
Requires:       apache-commons-httpclient
Requires:       backport-util-concurrent
Requires:       cglib
Requires:       concurrent
Requires:       regexp
Requires:       wadi2
Requires:       tomcat6-lib
%endif #wadi

%if_with wadi
%description -n %{jettyname}6-wadi
%{summary}.

%endif
%endif #wadi

%package -n %{jettyname}6-extratests
Summary:        extratests module from %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       jetty-jsp-2.1

%description -n %{jettyname}6-extratests
%{summary}.

%if_with grizzly
%package -n %{jettyname}6-grizzly
Summary:        grizzly module from %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-plus = %{epoch}:%{version}-%{release}
Requires:       grizzly17
BuildRequires:  grizzly17
%endif #grizzly

%if_with grizzly
%description -n %{jettyname}6-grizzly
%{summary}.
%endif #grizzly

%package -n %{jettyname}6-j2se6
Summary:        j2se6 module from %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}

%description -n %{jettyname}6-j2se6
%{summary}.

%package -n %{jettyname}6-start-daemon
Summary:        start-daemon module from %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       apache-commons-daemon

%description -n %{jettyname}6-start-daemon
%{summary}.

%package -n %{jettyname}6-sweeper
Summary:        sweeper module from %{name}
Group:          Development/Java

%description -n %{jettyname}6-sweeper
%{summary}.

%if_with terracotta
%package -n %{jettyname}6-terracotta
Summary:        terracotta module from %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-ext = %{epoch}:%{version}-%{release}
Requires:       terracotta-dso
Requires:       tc-maven-plugin
BuildRequires:  terracotta-dso
BuildRequires:  tc-maven-plugin
BuildRequires:  h2database
BuildRequires:  cargo-maven2-plugin
BuildRequires:  berkeleydb-je4

%description -n %{jettyname}6-terracotta
%{summary}.
%endif

%package -n %{jettyname}6-util5
Summary:        util5 module from %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}

%description -n %{jettyname}6-util5
%{summary}.

%package webapps
Summary:        Example webapps for %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-ext = %{epoch}:%{version}-%{release}
Requires:       jsp_2_1_api
Requires:       ejb_3_0_api
Requires:       interceptor_3_0_api
BuildRequires:  cometd-javascript

%description webapps
%{summary}.

%if_with jboss
%package jboss
Summary:        jboss sar for %{name}
Group:          Development/Java
Requires:       %{name}-core = %{epoch}:%{version}-%{release}
Requires:       %{name}-ext = %{epoch}:%{version}-%{release}
Requires:       %{name}-management = %{epoch}:%{version}-%{release}
Requires:       jetty-jsp-2.1
Requires:       jsp_2_1_api
Requires:       slf4j
BuildRequires:       jboss4-common
BuildRequires:       jboss4-j2ee
BuildRequires:       jboss4-jmx
BuildRequires:       jboss4-security
BuildRequires:       jboss4-server
BuildRequires:       jboss4-system
%endif #jboss

%if_with jboss
%description jboss
%{summary}.
%endif #jboss

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

%prep
%setup -q -n %{jettyname}-%{version}
%patch1 -b .sav1
%patch3 -b .sav3
%patch5 -b .sav5
%patch6 -b .sav6
%patch7 -b .sav7
%patch8 -b .sav8
%patch9 -b .sav9
%patch10 -b .sav10
%patch11 -b .sav11
%patch13 -b .sav13
%patch15 -b .sav15
%patch16 -b .sav16
%patch17 -b .sav17

%if %with cometd
perl -pi -e 's|<!--<module>contrib/cometd</module>-->|<module>contrib/cometd</module>|;' pom.xml
%endif
%if %with plus
perl -pi -e 's|<!--<module>modules/annotations</module>-->|<module>modules/annotations</module>|;' pom.xml
perl -pi -e 's|<!--<module>modules/plus</module>-->|<module>modules/plus</module>|;' pom.xml
%endif
%if %without xbean
perl -pi -e 's|<module>extras/xbean</module>|<!--<module>extras/xbean</module>-->|;' pom.xml
%endif

cp -p %{SOURCE1} settings.xml
cp -p %{SOURCE3} etc/start.config
cp -p %{SOURCE4} etc/jetty.conf

sed -i "s|# look for JETTY_HOME|export JETTY_HOME=%{_datadir}/%{name}|g" bin/jetty-xinetd.sh

# test fails with spring 1.2.9
rm extras/xbean/src/test/java/org/mortbay/jetty/xbean/XBeanTest.java

# location referenced by ${user.dir}
mkdir -p src/test/resources
cp -p extras/sslengine/src/test/resources/keystore src/test/resources/

for j in $(find . -name "*.java" -exec grep -l localhost {} \; | grep /test/); do
    sed -i -e 's/localhost/127.0.0.1/g' $j
done

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

 sed -i -e '/<module>contrib\/jboss<\/module>/d' pom.xml
 sed -i -e '/<module>contrib\/cometd<\/module>/d' pom.xml
 sed -i -e '/<module>contrib\/grizzly<\/module>/d' pom.xml
 sed -i -e '/<module>contrib\/wadi<\/module>/d' pom.xml
 sed -i -e '/<module>contrib\/terracotta<\/module>/d' pom.xml

 sed -i -e '/<module>modules\/native<\/module>/d' extras/setuid/pom.xml

%patch33

%build
export LANG=en_US.ISO8859-1
export SETTINGS=$(pwd)/settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}
mkdir -p ${MAVEN_REPO_LOCAL}/org/mortbay/jetty/jetty-parent/10
cp -p %{SOURCE9} ${MAVEN_REPO_LOCAL}/org/mortbay/jetty/jetty-parent/10/jetty-parent-10.pom
mkdir -p ${MAVEN_REPO_LOCAL}/org/eclipse/jetty/jetty-parent/14
cp -p %{SOURCE10} ${MAVEN_REPO_LOCAL}/org/eclipse/jetty/jetty-parent/14/jetty-parent-14.pom
mkdir -p ${MAVEN_REPO_LOCAL}/org/mortbay/jetty/jetty-parent/8
cp -p %{SOURCE11} ${MAVEN_REPO_LOCAL}/org/mortbay/jetty/jetty-parent/8/jetty-parent-8.pom
mkdir -p ${MAVEN_REPO_LOCAL}/org/mortbay/jetty/jetty-parent/9
cp -p %{SOURCE9} ${MAVEN_REPO_LOCAL}/org/mortbay/jetty/jetty-parent/9/jetty-parent-9.pom
mkdir -p $MAVEN_REPO_LOCAL/org/hyperic/libsigar-x86-linux/1.6.4/
if [ -e %{_libdir}/libsigar-x86-linux.so ]; then 
   ln -s %{_libdir}/libsigar-x86-linux.so $MAVEN_REPO_LOCAL/org/hyperic/libsigar-x86-linux/1.6.4/libsigar-x86-linux-1.6.4.so
else
   ln -s /dev/null $MAVEN_REPO_LOCAL/org/hyperic/libsigar-x86-linux/1.6.4/libsigar-x86-linux-1.6.4.so
fi
mkdir -p $MAVEN_REPO_LOCAL/org/hyperic/libsigar-amd64-linux/1.6.4/
if [ -e %{_libdir}/libsigar-amd64-linux.so ]; then 
   ln -s %{_libdir}/libsigar-amd64-linux.so $MAVEN_REPO_LOCAL/org/hyperic/libsigar-amd64-linux/1.6.4/libsigar-amd64-linux-1.6.4.so
else
   ln -s /dev/null $MAVEN_REPO_LOCAL/org/hyperic/libsigar-amd64-linux/1.6.4/libsigar-amd64-linux-1.6.4.so
fi
mkdir -p $MAVEN_REPO_LOCAL/org/hyperic/libsigar-universal64-macosx/1.6.4/
ln -s /dev/null $MAVEN_REPO_LOCAL/org/hyperic/libsigar-universal64-macosx/1.6.4/libsigar-universal64-macosx-1.6.4.dylib
mkdir -p $MAVEN_REPO_LOCAL/org/hyperic/libsigar-universal-macosx/1.6.4/
ln -s /dev/null $MAVEN_REPO_LOCAL/org/hyperic/libsigar-universal-macosx/1.6.4/libsigar-universal-macosx-1.6.4.dylib
mkdir -p $MAVEN_REPO_LOCAL/org/hyperic/sigar-x86-winnt/1.6.4/
ln -s /dev/null $MAVEN_REPO_LOCAL/org/hyperic/sigar-x86-winnt/1.6.4/sigar-x86-winnt-1.6.4.lib
mkdir -p $MAVEN_REPO_LOCAL/org/hyperic/sigar-x86-winnt/1.6.4/
ln -s /dev/null $MAVEN_REPO_LOCAL/org/hyperic/sigar-x86-winnt/1.6.4/sigar-x86-winnt-1.6.4.dll
mkdir -p $MAVEN_REPO_LOCAL/org/hyperic/sigar-amd64-winnt/1.6.4/
ln -s /dev/null $MAVEN_REPO_LOCAL/org/hyperic/sigar-amd64-winnt/1.6.4/sigar-amd64-winnt-1.6.4.dll
mkdir -p $MAVEN_REPO_LOCAL/org/hyperic/libsigar-x86-solaris/1.6.4/
ln -s /dev/null $MAVEN_REPO_LOCAL/org/hyperic/libsigar-x86-solaris/1.6.4/libsigar-x86-solaris-1.6.4.so
mkdir -p $MAVEN_REPO_LOCAL/org/hyperic/libsigar-sparc-solaris/1.6.4/
ln -s /dev/null $MAVEN_REPO_LOCAL/org/hyperic/libsigar-sparc-solaris/1.6.4/libsigar-sparc-solaris-1.6.4.so
mkdir -p $MAVEN_REPO_LOCAL/org/hyperic/libsigar-amd64-solaris/1.6.4/
ln -s /dev/null $MAVEN_REPO_LOCAL/org/hyperic/libsigar-amd64-solaris/1.6.4/libsigar-amd64-solaris-1.6.4.so
mkdir -p $MAVEN_REPO_LOCAL/JPP/
ln -s $(build-classpath testng) $MAVEN_REPO_LOCAL/JPP/testng-jdk15.jar

mkdir -p $MAVEN_REPO_LOCAL/org/cometd/javascript/cometd-examples-dojo/1.0.0rc0/
ln -sf %{_javadir}/cometd-javascript/examples-dojo.war $MAVEN_REPO_LOCAL/org/cometd/javascript/cometd-examples-dojo/1.0.0rc0/cometd-examples-dojo-1.0.0rc0.war
mkdir -p $MAVEN_REPO_LOCAL/org/cometd/javascript/cometd-javascript-jquery/1.0.0rc0/
ln -sf %{_javadir}/cometd-javascript/jquery.war $MAVEN_REPO_LOCAL/org/cometd/javascript/cometd-javascript-jquery/1.0.0rc0/cometd-javascript-jquery-1.0.0rc0.war
mkdir -p $MAVEN_REPO_LOCAL/org/cometd/javascript/cometd-examples-jquery/1.0.0rc0/
ln -sf %{_javadir}/cometd-javascript/examples-jquery.war $MAVEN_REPO_LOCAL/org/cometd/javascript/cometd-examples-jquery/1.0.0rc0/cometd-examples-jquery-1.0.0rc0.war
mkdir -p $MAVEN_REPO_LOCAL/org/cometd/javascript/cometd-javascript-dojo/1.0.0rc0/
ln -sf %{_javadir}/cometd-javascript/dojo.war $MAVEN_REPO_LOCAL/org/cometd/javascript/cometd-javascript-dojo/1.0.0rc0/cometd-javascript-dojo-1.0.0rc0.war


export MAVEN_OPTS="-Djava.awt.headless=true"
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -Djboss.home=%{jboss_home} \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.test.skip=true \
        install 

%if %with native
pushd extras/setuid
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven.test.skip=true \
        install 
popd
%endif

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -Djboss.home=%{jboss_home} \
        -Daggregate=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
	-Dproject.build.sourceEncoding=ISO-8859-1 \
        javadoc:javadoc

%if %without bootstrap
pushd modules/maven-plugin
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        plugin:xdoc 
popd
%endif

pushd modules/jspc-maven-plugin
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        plugin:xdoc 
popd

%if 0
pushd project-website
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        install 
popd
%endif

%if %with wadi
pushd contrib/wadi
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven.test.failure.ignore=true \
        install 
popd
%endif

%install

# ************* INSTALL Files To Fake RPM File Structure *******************

install -d -m 755 %{buildroot}%{_javadir}/%{name}

install -m 644 start.jar %{buildroot}%{_javadir}/%{name}/start-%{version}.jar
ln -s %{_javadir}/servlet_2_5_api.jar %{buildroot}%{_javadir}/%{name}/

%if %with api

# ================= Start of JSP 2.1 subpackage install
# create folder
install -d -m 755 %{buildroot}%{_javadir}/%{name}/jsp-2.1

# install jar files
install -m 644 lib/jsp-2.1/jsp-2.1-jetty-%{version}.jar %{buildroot}%{_javadir}/%{name}/jsp-2.1/jsp-2.1-jetty-%{version}.jar
ln -s %{_javadir}/jetty-jsp-2.1-api-glassfish.jar %{buildroot}%{_javadir}/%{name}/jsp-2.1/jsp-2.1-api-glassfish.jar
ln -s %{_javadir}/jetty-jsp-2.1-glassfish.jar %{buildroot}%{_javadir}/%{name}/jsp-2.1/jsp-2.1-glassfish.jar
pushd %{buildroot}%{_javadir}/%{name}/jsp-2.1
    ln -s $(build-classpath ant)
    ln -s $(build-classpath ecj)
popd
# ================= End of JSP 2.1 subpackage install


# ================= Start of JSP 2.0 subpackage install
# create folder
install -d -m 755 %{buildroot}%{_javadir}/%{name}/jsp-2.0

# install jar files
install -m 644 lib/jsp-2.0/jsp-api-2.0.jar %{buildroot}%{_javadir}/%{name}/jsp-2.0/jsp-api-2.0-%{version}.jar
pushd %{buildroot}%{_javadir}/%{name}/jsp-2.0
    ln -s $(build-classpath ant)
    ln -s $(build-classpath commons-el)
    ln -s $(build-classpath ecj)
    ln -s $(build-classpath jasper5-compiler)
    ln -s $(build-classpath jasper5-runtime)
    ln -s $(build-classpath slf4j/jcl-over-slf4j) jcl104-over-slf4j.jar
    ln -s $(build-classpath slf4j/slf4j-api) slf4j-api.jar
    ln -s $(build-classpath slf4j/slf4j-simple) slf4j-simple.jar
    ln -s $(build-classpath xerces-j2)
    ln -s $(build-classpath xml-commons-jaxp-1.3-apis)
popd
# ================= End of JSP 2.0 subpackage install
%endif

# ================= Start of Jetty-Core subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/core
install -m 644 lib/jetty-%{version}.jar %{buildroot}%{_javadir}/%{name}/core/%{name}-%{version}.jar
install -m 644 lib/jetty-util-%{version}.jar %{buildroot}%{_javadir}/%{name}/core/%{name}-util-%{version}.jar
install -m 644 lib/ext/jetty-html-%{version}.jar %{buildroot}%{_javadir}/%{name}/core/%{name}-html-%{version}.jar

# compat symlinks
pushd %{buildroot}%{_javadir}/%{name}
    ln -s core/%{name}-%{version}.jar
    ln -s core/%{name}-util-%{version}.jar
    ln -s core/%{name}-html-%{version}.jar
popd
# ================= End of Jetty-Core subpackage install

# ================= Start of Jetty-Ext subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/ext
install -m 644 extras/ajp/target/jetty-ajp-%{version}.jar %{buildroot}%{_javadir}/%{name}/ext/%{name}-ajp-%{version}.jar
install -m 644 lib/ext/jetty-client-%{version}.jar %{buildroot}%{_javadir}/%{name}/ext/%{name}-client-%{version}.jar
install -m 644 lib/ext/jetty-java5-threadpool-%{version}.jar %{buildroot}%{_javadir}/%{name}/ext/%{name}-java5-threadpool-%{version}.jar
install -m 644 lib/ext/jetty-servlet-tester-%{version}.jar %{buildroot}%{_javadir}/%{name}/ext/%{name}-servlet-tester-%{version}.jar
install -m 644 lib/ext/jetty-sslengine-%{version}.jar %{buildroot}%{_javadir}/%{name}/ext/%{name}-sslengine-%{version}.jar
# ================= End of Jetty-Ext subpackage install

%if %with plus
# ================= Start of Jetty-Plus subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/plus
install -m 644 lib/plus/jetty-plus-%{version}.jar %{buildroot}%{_javadir}/%{name}/plus/%{name}-plus-%{version}.jar
# compat symlinks
pushd %{buildroot}%{_javadir}/%{name}
    ln -s plus/%{name}-plus-%{version}.jar
popd
# ================= End of Jetty-Plus subpackage install
%endif

%if %with plus
# ================= Start of Jetty-Annotations subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/annotations
install -m 644 lib/annotations/jetty-annotations-%{version}.jar %{buildroot}%{_javadir}/%{name}/annotations/%{name}-annotations-%{version}.jar
pushd %{buildroot}%{_javadir}/%{name}/annotations
    ln -s $(build-classpath geronimo-annotation-1.0-api)
popd
# ================= End of Jetty-Annotations subpackage install
%endif

# ================= Start of Jetty-Management subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/management/mx4j
install -m 644 lib/management/jetty-management-%{version}.jar %{buildroot}%{_javadir}/%{name}/management/%{name}-management-%{version}.jar
#pushd %{buildroot}%{_javadir}/%{name}/management
#    pushd mx4j
#        ln -s $(build-classpath mx4j/mx4j)
#        ln -s $(build-classpath mx4j/mx4j-tools)
#    popd
#popd
# compat symlink
pushd %{buildroot}%{_javadir}/%{name}
    ln -s management/%{name}-management-%{version}.jar
popd
# ================= End of Jetty-Management subpackage install

# ================= Start of Jetty-Naming subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/naming
install -m 644 lib/naming/jetty-naming-%{version}.jar %{buildroot}%{_javadir}/%{name}/naming/%{name}-naming-%{version}.jar
pushd %{buildroot}%{_javadir}/%{name}/naming
    ln -s $(build-classpath jaf_1_1_api)
    ln -s $(build-classpath javamail_1_4_api)
popd
# compat symlink
pushd %{buildroot}%{_javadir}/%{name}
    ln -s naming/%{name}-naming-%{version}.jar
popd
# ================= End of Jetty-Naming subpackage install

%if %with xbean
# ================= Start of Jetty-XBean subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/xbean
install -m 644 lib/xbean/jetty-xbean-%{version}.jar %{buildroot}%{_javadir}/%{name}/xbean/%{name}-xbean-%{version}.jar
# ================= End of Jetty-XBean subpackage install
%endif

%if %with cometd
# ================= Start of Jetty-Cometd subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/cometd
install -m 644 contrib/cometd/server/target/cometd-server-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}/cometd/
install -m 644 contrib/cometd/client/target/cometd-client-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}/cometd/
install -m 644 contrib/cometd/client/target/cometd-client-%{version}-tests.jar \
  %{buildroot}%{_javadir}/%{name}/cometd/cometd-client-tests-%{version}.jar
install -m 644 contrib/cometd/oort/target/cometd-oort-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}/cometd/
pushd %{buildroot}%{_javadir}/%{name}/cometd
    ln -s $(build-classpath cometd-api) cometd-api.jar
popd
# ================= End of Jetty-Cometd subpackage install
%endif

# ================= Start of Jetty-Ant subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/ant
install -m 644 contrib/jetty-ant/target/jetty-ant-%{version}.jar %{buildroot}%{_javadir}/%{name}/ant/%{name}-ant-%{version}.jar
# ================= End of Jetty-Ant subpackage install

%if %with wadi
# ================= Start of Jetty-Wadi subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/wadi
install -m 644 contrib/wadi/target/jetty-wadi-session-manager-%{version}.jar %{buildroot}%{_javadir}/%{name}/wadi/%{name}-wadi-session-manager-%{version}.jar
# ================= End of Jetty-Wadi subpackage install
%endif

# ================= Start of Jetty-Embedded subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/embedded
install -m 644 examples/embedded/target/jetty-embedded-%{version}.jar %{buildroot}%{_javadir}/%{name}/embedded/%{name}-embedded-%{version}.jar
# ================= End of Jetty-Embedded subpackage install

# ================= Start of Jetty-Spring subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/spring
install -m 644 extras/spring/target/jetty-spring-%{version}.jar %{buildroot}%{_javadir}/%{name}/spring/%{name}-spring-%{version}.jar
# ================= End of Jetty-Spring subpackage install

install -d -m 755 %{buildroot}%{_datadir}/maven2/plugins
# ================= Start of Jetty Maven2-Plugins subpackages install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/maven2
install -m 644 modules/jspc-maven-plugin/target/maven-jetty-jspc-plugin-%{version}.jar %{buildroot}%{_javadir}/%{name}/maven2/jetty6-jspc-maven-plugin-%{version}.jar
install -m 644 modules/maven-plugin/target/maven-jetty-plugin-%{version}.jar %{buildroot}%{_javadir}/%{name}/maven2/jetty6-maven-plugin-%{version}.jar
pushd %{buildroot}%{_datadir}/maven2/plugins
    ln -s %{_javadir}/%{name}/maven2/jetty6-jspc-maven-plugin-%{version}.jar jetty-jspc-maven-plugin-%{version}.jar
    ln -s %{_javadir}/%{name}/maven2/jetty6-maven-plugin-%{version}.jar jetty-maven-plugin-%{version}.jar

popd
# ================= End of Jetty Maven2-Plugin subpackages install

%if_with grizzly
# ================= Start of Jetty-Grizzly subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/grizzly
install -m 644 contrib/grizzly/target/jetty-grizzly-%{version}.jar %{buildroot}%{_javadir}/%{name}/grizzly/%{name}-grizzly-%{version}.jar
# ================= End of Jetty-Grizzly subpackage install
%endif

# ================= Start of Jetty-J2se6 subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/j2se6
install -m 644 contrib/j2se6/target/jetty-j2se6-%{version}.jar %{buildroot}%{_javadir}/%{name}/j2se6/%{name}-j2se6-%{version}.jar
# ================= End of Jetty-J2se6 subpackage install

# ================= Start of Jetty-Ldap-Jaas subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/ext
install -m 644 contrib/jetty-ldap-jaas/target/jetty-ldap-jaas-%{version}.jar %{buildroot}%{_javadir}/%{name}/ext/%{name}-ldap-jaas-%{version}.jar
# ================= End of Jetty-Ldap-Jaas subpackage install

# ================= Start of Jetty-Rewrite-Handler subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/ext
install -m 644 contrib/jetty-rewrite-handler/target/jetty-rewrite-handler-%{version}.jar %{buildroot}%{_javadir}/%{name}/ext/%{name}-rewrite-handler-%{version}.jar
# ================= End of Jetty-Rewrite-Handler subpackage install

#BUILD/jetty-6.1.22/contrib/maven-beanshell-plugin/target/maven-beanshell-plugin-1.0-SNAPSHOT.jar MISSING

# ================= Start of Jetty-Start-Daemon subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/start-daemon
install -m 644 contrib/start-daemon/target/start-daemon-%{version}.jar %{buildroot}%{_javadir}/%{name}/start-daemon/%{name}-start-daemon-%{version}.jar
# ================= End of Jetty-Start-Daemon subpackage install

# ================= Start of Jetty-Sweeper subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/sweeper
install -m 644 contrib/sweeper/target/sweeper-%{version}.jar %{buildroot}%{_javadir}/%{name}/sweeper/%{name}-sweeper-%{version}.jar
# ================= End of Jetty-Sweeper subpackage install

%if_with terracotta
# ================= Start of Jetty-Terracotta subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/terracotta
install -m 644 contrib/terracotta/target/jetty-terracotta-sessions-%{version}.jar %{buildroot}%{_javadir}/%{name}/terracotta/%{name}-terracotta-sessions-%{version}.jar
# ================= End of Jetty-Terracotta subpackage install
%endif

# ================= Start of Jetty-Extratests subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/extratests
install -m 644 examples/tests/target/extratests-%{version}.jar %{buildroot}%{_javadir}/%{name}/extratests/%{name}-extratests-%{version}.jar
# ================= End of Jetty-Extratests subpackage install

# ================= Start of Jetty-Java5-Stats subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/ext
install -m 644 extras/jetty-java5-stats/target/jetty-java5-stats-%{version}.jar %{buildroot}%{_javadir}/%{name}/ext/%{name}-java5-stats-%{version}.jar
# ================= End of Jetty-Java5-Stats subpackage install

# ================= Start of Jetty-Setuid subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/ext
install -m 644 extras/setuid/target/jetty-setuid-%{version}.jar %{buildroot}%{_javadir}/%{name}/ext/%{name}-setuid-%{version}.jar
# ================= End of Jetty-Setuid subpackage install

# ================= Start of Jetty-Util5 subpackage install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/jre1.5
install -m 644 modules/util5/target/jetty-util5-%{version}.jar %{buildroot}%{_javadir}/%{name}/jre1.5/%{name}-util5-%{version}.jar
# ================= End of Jetty-Util5 subpackage install

# build initial path structure
%{__install} -d -m 0755 %{buildroot}%{apphomedir}
%{__install} -d -m 0755 %{buildroot}%{apphomedir}/bin
%{__install} -d -m 0755 %{buildroot}%{appdir}
%{__install} -d -m 0755 %{buildroot}%{vardir}
%{__install} -d -m 0755 %{buildroot}%{_bindir}
%{__install} -d -m 0755 %{buildroot}%{_sbindir}
%{__install} -d -m 0755 %{buildroot}%{ctxdir}
%{__install} -d -m 0755 %{buildroot}%{confdir}
%{__install} -d -m 0755 %{buildroot}%{logdir}
%{__install} -d -m 0755 %{buildroot}%{rundir}
%{__install} -d -m 0755 %{buildroot}%{_initrddir}
%{__install} -d -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d
%{__install} -d -m 0755 %{buildroot}%{_sysconfdir}/sysconfig

( cat << EO_RC
JAVA_HOME=%{java_home}
JAVA_OPTIONS=
JETTY_HOME=%{apphomedir}
JETTY_CONSOLE=%{logdir}/jetty-console.log
JETTY_PORT=8080
JETTY_RUN=%{_var}/run/%{name}
JETTY_PID=\$JETTY_RUN/jetty.pid
EO_RC
) > %{buildroot}%{apphomedir}/.jettyrc

# install etc files <jetty-root>/etc
install -m 644 etc/start.config %{buildroot}%{confdir}/start.config
install -m 644 etc/jetty.conf %{buildroot}%{confdir}/jetty.conf
install -m 644 etc/jetty.xml %{buildroot}%{confdir}/jetty.xml
install -m 644 etc/jetty-ajp.xml %{buildroot}%{confdir}/jetty-ajp.xml
install -m 644 etc/jetty-bio.xml %{buildroot}%{confdir}/jetty-bio.xml
%if_with grizzly
install -m 644 etc/jetty-grizzly.xml %{buildroot}%{confdir}/jetty-grizzly.xml
%endif
install -m 644 etc/jetty-jmx.xml %{buildroot}%{confdir}/jetty-jmx.xml
install -m 644 etc/jetty-logging.xml %{buildroot}%{confdir}/jetty-logging.xml
%if %with plus
install -m 644 etc/jetty-plus.xml %{buildroot}%{confdir}/jetty-plus.xml
%endif
install -m 644 etc/jetty-rewrite.xml %{buildroot}%{confdir}/jetty-rewrite.xml
install -m 644 etc/jetty-setuid.xml %{buildroot}%{confdir}/jetty-setuid.xml
install -m 644 etc/jetty-ssl.xml %{buildroot}%{confdir}/jetty-ssl.xml
install -m 644 etc/jetty-sslengine.xml %{buildroot}%{confdir}/jetty-sslengine.xml
install -m 644 etc/jetty-stats.xml %{buildroot}%{confdir}/jetty-stats.xml
install -m 644 etc/jetty-xinetd.xml %{buildroot}%{confdir}/jetty-xinetd.xml
install -m 644 etc/webdefault.xml %{buildroot}%{confdir}/webdefault.xml
install -m 644 etc/realm.properties %{buildroot}%{confdir}/realm.properties
install -m 644 etc/jdbcRealm.properties %{buildroot}%{confdir}/jdbcRealm.properties
install -m 644 etc/jetty-jaas.xml %{buildroot}%{confdir}/jetty-jaas.xml
install -m 644 etc/keystore %{buildroot}%{confdir}/keystore
install -m 644 etc/login.conf %{buildroot}%{confdir}/login.conf
install -m 644 etc/login.properties %{buildroot}%{confdir}/login.properties

# install bin files <jetty-root>/bin
install -m 644 bin/jetty-xinetd.sh %{buildroot}%{apphomedir}/bin/jetty-xinetd.sh
chmod +x %{buildroot}%{apphomedir}/bin/jetty-xinetd.sh
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -m 644 %{SOURCE6} %{buildroot}%{_sbindir}/d%{name}
install -m 644 bin/jetty.sh %{buildroot}%{apphomedir}/bin/jetty.sh
ln -s %{apphomedir}/bin/jetty.sh %{buildroot}%{_bindir}/%{name}
install -m 755 %{SOURCE7} %{buildroot}%{_initrddir}/%{name}
install -m 755 %{SOURCE8} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# FHS Symlink for Jetty Home
pushd %{buildroot}%{apphomedir}
    %{__ln_s} %{appdir} webapps
    %{__ln_s} %{ctxdir} contexts
    %{__ln_s} %{confdir} etc
    %{__ln_s} %{logdir} logs
    %{__ln_s} %{vardir} lib
popd

(
cd %{buildroot}%{_javadir}/%{name} 
for jar in *-%{version}.jar; do
	n=$(/bin/echo ${jar} | %{__sed} "s|-%{version}||g")
	ln -s ${jar} ${n}
	ln -s %{_javadir}/%{name}/${n} %{buildroot}%{vardir}
done
)

for module in annotations ant cometd core embedded ext extratests grizzly j2se6 java5-stats jsp-2.0 jsp-2.1 ldap-jaas management naming plus rewrite-handler setuid spring start-daemon sweeper terracotta jre1.5 wadi xbean maven2; do
    if [ -d %{buildroot}%{_javadir}/%{name}/${module} ]; then
        (
	cd %{buildroot}%{_javadir}/%{name}/${module} 
	for jar in *-%{version}.jar; do
		n=$(/bin/echo ${jar} | %{__sed} "s|-%{version}||g")
		ln -s ${jar} ${n}
		mkdir -p %{buildroot}%{vardir}/${module}
		ln -s %{_javadir}/%{name}/${module}/${n} %{buildroot}%{vardir}/${module}
	done
	)
    fi
done

%if_with jboss
# ================= Start of Jetty-JBoss subpackage install
%{__install} -d -m 0755 %{buildroot}%{_datadir}/%{name}
%{__install} -m 0644 contrib/jboss/target/jetty-%{version}-jboss-4.2.3.GA-jsp-2.1.jboss-sar \
			%{buildroot}%{_datadir}/%{name}/jetty-%{version}-jboss4-jsp-2.1.sar
# ================= End of Jetty-JBoss subpackage install
%endif

# ================= Start of Jetty-Webapps subpackage install
LOC=$(pwd)
mkdir -p %{buildroot}%{appdir}/spring-ebj3-demo
pushd %{buildroot}%{appdir}/spring-ebj3-demo
jar xf ${LOC}/examples/spring-ebj3-demo/target/spring-ejb3-demo-%{version}.war 
popd
mkdir -p %{buildroot}%{appdir}/spring-ebj3-demo/WEB-INF/lib
ln -s $(build-classpath ejb_3_0_api) %{buildroot}%{appdir}/spring-ebj3-demo/WEB-INF/lib
ln -s $(build-classpath interceptor_3_0_api) %{buildroot}%{appdir}/spring-ebj3-demo/WEB-INF/lib

mkdir -p %{buildroot}%{appdir}/test-jaas
pushd %{buildroot}%{appdir}/test-jaas
jar xf ${LOC}/examples/test-jaas-webapp/target/jetty-test-jaas-%{version}.war 
popd

mkdir -p %{buildroot}%{appdir}/test-jndi
pushd %{buildroot}%{appdir}/test-jndi
jar xf ${LOC}/examples/test-jndi-webapp/target/jetty-test-jndi-%{version}.war
popd

mkdir -p %{buildroot}%{appdir}/test
pushd %{buildroot}%{appdir}/test
jar xf ${LOC}/examples/test-webapp/target/jetty-test-%{version}.war
popd

mkdir -p %{buildroot}%{appdir}/cometd
%if_with cometd
pushd %{buildroot}%{appdir}/cometd
jar xf ${LOC}/contrib/cometd/demo/target/cometd-demo-%{version}.war
popd
rm %{buildroot}%{appdir}/cometd/WEB-INF/lib/cometd-api-1.1.1.jar
ln -s $(build-classpath cometd-api) %{buildroot}%{appdir}/cometd/WEB-INF/lib/
rm %{buildroot}%{appdir}/cometd/WEB-INF/lib/cometd-server-%{version}.jar
ln -s %{_javadir}/jetty6/cometd/cometd-server.jar %{buildroot}%{appdir}/cometd/WEB-INF/lib/
rm %{buildroot}%{appdir}/cometd/WEB-INF/lib/jetty-util5-%{version}.jar
ln -s %{_javadir}/jetty6/jre1.5/jetty6-util5.jar %{buildroot}%{appdir}/cometd/WEB-INF/lib/
rm %{buildroot}%{appdir}/cometd/WEB-INF/lib/jetty-util-%{version}.jar
ln -s %{_javadir}/jetty6/jetty6-util.jar %{buildroot}%{appdir}/cometd/WEB-INF/lib/
rm %{buildroot}%{appdir}/cometd/WEB-INF/lib/servlet-api-2.5.jar
ln -s %{_javadir}/servlet_2_5_api.jar %{buildroot}%{appdir}/cometd/WEB-INF/lib/
%endif

install -m 644 contexts/README-test-jndi.txt \
     %{buildroot}%{ctxdir}
install -m 644 contexts/README.TXT \
     %{buildroot}%{ctxdir}
cp -pr contexts/test.d %{buildroot}%{ctxdir}
cp -pr contexts/test-jndi.d %{buildroot}%{ctxdir}
install -m 644 contexts/test-jndi.xml \
     %{buildroot}%{ctxdir}
install -m 644 contexts/test.xml \
     %{buildroot}%{ctxdir}
%if_with wadi
install -m 644 contexts/wadi.xml \
     %{buildroot}%{ctxdir}
%endif
%if_with cometd
install -m 644 contrib/cometd/demo/etc/cometd.xml \
     %{buildroot}%{ctxdir}
%endif

# ================= End of Jetty-Webapps subpackage install

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms

%add_to_maven_depmap org.mortbay.jetty jetty-parent 8 JPP/%{name}/org.mortbay.jetty %{name}-parent
install -m 644 %{SOURCE9} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}.org.mortbay.jetty-%{name}-parent.pom

%add_to_maven_depmap org.eclipse.jetty jetty-parent 9 JPP/%{name}/org.eclipse.jetty %{name}-parent
install -m 644 %{SOURCE10} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}.org.eclipse.jetty-%{name}-parent.pom

%add_to_maven_depmap org.mortbay.jetty project %{version} JPP/%{name} project
install -m 644 pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-project.pom

%add_to_maven_depmap org.mortbay.jetty jetty %{version} JPP/%{name}/core jetty6
install -m 644 modules/jetty/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.core-jetty6.pom

%add_to_maven_depmap org.mortbay.jetty jetty-html %{version} JPP/%{name}/core %{name}-html
install -m 644 modules/html/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.core-%{name}-html.pom

%add_to_maven_depmap org.mortbay.jetty jetty-util %{version} JPP/%{name}/core %{name}-util
install -m 644 modules/util/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.core-%{name}-util.pom

%if %with plus
%add_to_maven_depmap org.mortbay.jetty jetty-annotations %{version} JPP/%{name}/annotations %{name}-annotations
install -m 644 modules/annotations/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.annotations-%{name}-annotations.pom
%endif

%add_to_maven_depmap org.mortbay.jetty jetty-naming %{version} JPP/%{name}/naming %{name}-naming
install -m 644 modules/naming/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.naming-%{name}-naming.pom

%add_to_maven_depmap org.mortbay.jetty jetty-management %{version} JPP/%{name}/management %{name}-management
install -m 644 modules/management/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.management-%{name}-management.pom

%if %with plus
%add_to_maven_depmap org.mortbay.jetty jetty-plus %{version} JPP/%{name}/plus %{name}-plus
install -m 644 modules/plus/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.plus-%{name}-plus.pom
%endif

%if %with api

%add_to_maven_depmap org.mortbay.jetty jsp-2.1 %{version} JPP/%{name}/jsp-2.1 jsp-2.1
install -m 644 modules/jsp-2.1/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.jsp-2.1-jsp-2.1.pom

%add_to_maven_depmap org.mortbay.jetty jsp-api-2.0 %{version} JPP/%{name}/jsp-2.0 jsp-2.0-api
install -m 644 modules/jsp-api-2.0/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.jsp-2.0-jsp-2.0-api.pom

%add_to_maven_depmap org.mortbay.jetty jsp-2.0 %{version} JPP/%{name}/jsp-2.0 jsp-2.0
install -m 644 modules/jsp-2.0/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.jsp-2.0-jsp-2.0.pom
%endif

%add_to_maven_depmap org.mortbay.jetty jetty-ajp %{version} JPP/%{name}/ext %{name}-ajp
install -m 644 extras/ajp/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-ajp.pom

%add_to_maven_depmap org.mortbay.jetty jetty-client %{version} JPP/%{name}/ext %{name}-client
install -m 644 extras/client/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-client.pom

%add_to_maven_depmap org.mortbay.jetty jetty-java5-threadpool %{version} JPP/%{name}/ext %{name}-java5-threadpool
install -m 644 extras/threadpool/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-java5-threadpool.pom

%add_to_maven_depmap org.mortbay.jetty jetty-servlet-tester %{version} JPP/%{name}/ext %{name}-servlet-tester
install -m 644 extras/servlet-tester/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-servlet-tester.pom

%add_to_maven_depmap org.mortbay.jetty jetty-sslengine %{version} JPP/%{name}/ext %{name}-sslengine
install -m 644 extras/sslengine/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-sslengine.pom

%add_to_maven_depmap org.mortbay.jetty jetty-spring %{version} JPP/%{name}/spring %{name}-spring
install -m 644 extras/spring/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.spring-%{name}-spring.pom

%if %with xbean
%add_to_maven_depmap org.mortbay.jetty jetty-xbean %{version} JPP/%{name}/xbean %{name}-xbean
install -m 644 extras/xbean/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.xbean-%{name}-xbean.pom
%endif

%add_to_maven_depmap org.mortbay.jetty maven-jetty-jspc-plugin %{version} JPP/%{name}/maven2 jetty6-jspc-maven-plugin
install -m 644 modules/jspc-maven-plugin/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}.maven2-jetty6-jspc-maven-plugin.pom
 
%add_to_maven_depmap org.mortbay.jetty maven-jetty-plugin %{version} JPP/%{name}/maven2 jetty6-maven-plugin
install -m 644 modules/maven-plugin/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}.maven2-jetty6-maven-plugin.pom

%if %with cometd
%add_to_maven_depmap org.mortbay.jetty cometd-project %{version} JPP/%{name}/cometd project
install -m 644 contrib/cometd/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.cometd-project.pom
%add_to_maven_depmap org.mortbay.jetty cometd-server %{version} JPP/%{name}/cometd cometd-server
install -m 644 contrib/cometd/server/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.cometd-cometd-server.pom
%add_to_maven_depmap org.mortbay.jetty cometd-client %{version} JPP/%{name}/cometd cometd-client
install -m 644 contrib/cometd/client/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.cometd-cometd-client.pom
%add_to_maven_depmap org.mortbay.jetty cometd-oort %{version} JPP/%{name}/cometd cometd-oort
install -m 644 contrib/cometd/oort/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.cometd-cometd-oort.pom
%endif

%add_to_maven_depmap org.mortbay.jetty jetty-ant %{version} JPP/%{name}/ant %{name}-ant
install -m 644 contrib/jetty-ant/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.ant-%{name}-ant.pom

%if %with wadi
%add_to_maven_depmap org.mortbay.jetty jetty-wadi-session-manager %{version} JPP/%{name}/wadi %{name}-wadi-session-manager
install -m 644 contrib/wadi/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.wadi-%{name}-wadi-session-manager.pom
%endif

%add_to_maven_depmap org.mortbay.jetty jetty-embedded %{version} JPP/%{name}/embedded %{name}-embedded
install -m 644 examples/embedded/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.embedded-%{name}-embedded.pom

%add_to_maven_depmap org.mortbay.jetty jetty-extratests %{version} JPP/%{name}/extratests %{name}-extratests
install -m 644 examples/tests/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.extratests-%{name}-extratests.pom

%add_to_maven_depmap org.mortbay.jetty jetty-grizzly %{version} JPP/%{name}/grizzly %{name}-grizzly
install -m 644 contrib/grizzly/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.grizzly-%{name}-grizzly.pom

%add_to_maven_depmap org.mortbay.jetty jetty-j2se6 %{version} JPP/%{name}/j2se6 %{name}-j2se6
install -m 644 contrib/j2se6/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.j2se6-%{name}-j2se6.pom

%add_to_maven_depmap org.mortbay.jetty jetty-java5-stats %{version} JPP/%{name}/ext %{name}-java5-stats
install -m 644 extras/jetty-java5-stats/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-java5-stats.pom

%add_to_maven_depmap org.mortbay.jetty jetty-ldap-jaas %{version} JPP/%{name}/ext %{name}-ldap-jaas
install -m 644 contrib/jetty-ldap-jaas/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-ldap-jaas.pom

%add_to_maven_depmap org.mortbay.jetty jetty-rewrite-handler %{version} JPP/%{name}/ext %{name}-rewrite-handler
install -m 644 contrib/jetty-rewrite-handler/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-rewrite-handler.pom

%add_to_maven_depmap org.mortbay.jetty jetty-setuid %{version} JPP/%{name}/ext %{name}-setuid
install -m 644 extras/setuid/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-setuid.pom

%add_to_maven_depmap org.mortbay.jetty jetty-setuid-java %{version} JPP/%{name}/ext %{name}-setuid-java
install -m 644 extras/setuid/modules/java/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-setuid-java.pom

%add_to_maven_depmap org.mortbay.jetty libsetuid %{version} JPP/%{name}/ext %{name}-libsetuid
install -m 644 extras/setuid/modules/native/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-libsetuid.pom

%add_to_maven_depmap org.mortbay.jetty jetty-start-daemon %{version} JPP/%{name}/start-daemon %{name}-start-daemon
install -m 644 contrib/start-daemon/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.start-daemon-%{name}-start-daemon.pom

%add_to_maven_depmap org.mortbay.jetty jetty-sweeper %{version} JPP/%{name}/sweeper %{name}-sweeper
install -m 644 contrib/sweeper/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.sweeper-%{name}-sweeper.pom

%if_with terracotta
%add_to_maven_depmap org.mortbay.jetty jetty-terracotta-sessions %{version} JPP/%{name}/terracotta %{name}-terracotta-sessions
install -m 644 contrib/terracotta/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.terracotta-%{name}-terracotta-sessions.pom
%endif

%add_to_maven_depmap org.mortbay.jetty jetty-util5 %{version} JPP/%{name}/jre1.5 %{name}-util5
install -m 644 modules/util5/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.jetty6.jre1.5-%{name}-util5.pom

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
ln -s %{_javadocdir}/%{name} %{buildroot}%{apphomedir}/javadoc
install -m 644 contexts/javadoc.xml %{buildroot}%{ctxdir}

%if 0
install -dm 755 %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr project-website/project-site/target/site/* %{buildroot}%{_docdir}/%{name}-%{version}
rm -rf %{buildroot}%{_docdir}/%{name}-%{version}/apidocs
ln -s %{_javadocdir}/%{name} %{buildroot}%{_docdir}/%{name}-%{version}/apidocs
%endif

mkdir -p $RPM_BUILD_ROOT`dirname /etc/default/%{name}`
touch $RPM_BUILD_ROOT/etc/default/%{name}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/default/jetty`
touch $RPM_BUILD_ROOT/etc/default/jetty

# ********************* CLEAN SECTION **************************
%pre
%{_sbindir}/groupadd -r -r %{username} &>/dev/null || :
# Use /bin/sh so init script will start properly.
%{_sbindir}/useradd -r -s /bin/sh -d %{apphomedir} -M          \
                    -r %{username} &>/dev/null || :

%preun
if [ $1 = 0 ]; then
    [ -f /var/lock/subsys/%{name} ] && %{_initrddir}/%{name} stop || :
    [ -f %{_initrddir}/%{name} -a -x /sbin/chkconfig ] && /sbin/chkconfig --del %{name} || :

    %{_sbindir}/userdel jetty >> /dev/null 2>&1 || :
fi

# Post-Install
%post
[ -x /sbin/chkconfig ] && /sbin/chkconfig --add %{name} || :

# Post-Uninstall
%files
%attr(0755,root,root) %{_sbindir}/d%{name}
%attr(0755,root,root) %{_bindir}/%{name}
%{_sysconfdir}/logrotate.d/%{name}
%{_sysconfdir}/sysconfig/%{name}
%dir %{appdir}
%dir %{ctxdir}
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%dir %{vardir}
%{vardir}/start.jar
%{vardir}/%{name}.jar
%{vardir}/%{name}-html.jar
%{vardir}/%{name}-util.jar
%attr(755,root,root) %{_initrddir}/%{name}
%dir %{confdir}
%config(noreplace) %{confdir}/start.config
%config(noreplace) %{confdir}/jetty.conf
%config(noreplace) %{confdir}/jetty.xml
%config(noreplace) %{confdir}/jetty-bio.xml
%config(noreplace) %{confdir}/jetty-logging.xml
%config(noreplace) %{confdir}/jetty-ssl.xml
%config(noreplace) %{confdir}/jetty-stats.xml
%config(noreplace) %{confdir}/jetty-xinetd.xml
%config(noreplace) %{confdir}/jdbcRealm.properties
%config(noreplace) %{confdir}/realm.properties
%config(noreplace) %{confdir}/keystore
%config(noreplace) %{confdir}/webdefault.xml
%{apphomedir}
%{_mavendepmapfragdir}/%{name}
%{_datadir}/maven2/poms/JPP.%{name}.org.eclipse.jetty-%{name}-parent.pom                                                                             
%{_datadir}/maven2/poms/JPP.%{name}.org.mortbay.jetty-%{name}-parent.pom
%doc *.txt
%doc LICENSES/LICENSE*.txt
%attr(0755,jetty,jetty) %dir %{logdir}
%attr(0755,jetty,jetty) %dir %{rundir}
%dir %{_datadir}/%{name}
%config(noreplace,missingok) /etc/default/%{name}
%config(noreplace,missingok) /etc/default/jetty

# ========= End of Jetty package Files

%if %with api

# ========= Start of JSP 2.1 Subpackage Files
%files -n %{jettyname}6-jsp-%{jspspec}
%dir %{_javadir}/%{name}/jsp-2.1
%{_javadir}/%{name}/jsp-2.1/*.jar
%dir %{vardir}/jsp-2.1
%{vardir}/jsp-2.1/*.jar
%{_datadir}/maven2/poms/JPP.jetty6.jsp-2.1-jsp-2.1.pom
%doc LICENSES/LICENSE*.txt
# ========= End of JSP 2.1 Subpackage Files

# ========= Start of JSP 2.0 Subpackage Files
%files -n %{jettyname}6-jsp-2.0
%dir %{_javadir}/%{name}/jsp-2.0
%{_javadir}/%{name}/jsp-2.0/*.jar
%dir %{vardir}/jsp-2.0
%{vardir}/jsp-2.0/*.jar
%{_datadir}/maven2/poms/JPP.jetty6.jsp-2.0-jsp-2.0-api.pom
%{_datadir}/maven2/poms/JPP.jetty6.jsp-2.0-jsp-2.0.pom
%doc LICENSES/LICENSE*.txt
# ========= End of JSP 2.0 Subpackage Files

%endif

# ========= Start of Jetty core Subpackage Files
%files -n %{jettyname}6-core
%dir %{_javadir}/%{name}/core
%{_javadir}/%{name}/core/*.jar
%{_javadir}/%{name}/%{name}.jar
%{_javadir}/%{name}/%{name}-html.jar
%{_javadir}/%{name}/%{name}-util.jar
%dir %{vardir}/core
%{vardir}/core/%{name}.jar
%{vardir}/core/%{name}-html.jar
%{vardir}/core/%{name}-util.jar
%{_datadir}/maven2/poms/JPP.%{name}-project.pom
%{_datadir}/maven2/poms/JPP.jetty6.core-jetty6.pom
%{_datadir}/maven2/poms/JPP.jetty6.core-%{name}-util.pom
%{_datadir}/maven2/poms/JPP.jetty6.core-%{name}-html.pom
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty core  Subpackage Files

# ========= Start of Jetty ext Subpackage Files
%files -n %{jettyname}6-ext
%dir %{_javadir}/%{name}/ext
%{_javadir}/%{name}/ext/*.jar
%config(noreplace) %{confdir}/jetty-ajp.xml
%config(noreplace) %{confdir}/jetty-rewrite.xml
%config(noreplace) %{confdir}/jetty-setuid.xml
%config(noreplace) %{confdir}/jetty-sslengine.xml
%dir %{vardir}/ext
%{vardir}/ext/%{name}-ajp.jar
%{vardir}/ext/%{name}-client.jar
%{vardir}/ext/%{name}-java5-stats.jar
%{vardir}/ext/%{name}-java5-threadpool.jar
%{vardir}/ext/%{name}-ldap-jaas.jar
%{vardir}/ext/%{name}-rewrite-handler.jar
%{vardir}/ext/%{name}-servlet-tester.jar
%{vardir}/ext/%{name}-setuid.jar
%{vardir}/ext/%{name}-sslengine.jar
%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-ajp.pom
%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-client.pom
%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-java5-threadpool.pom
%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-servlet-tester.pom
%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-sslengine.pom
%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-java5-stats.pom
%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-ldap-jaas.pom
%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-rewrite-handler.pom
%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-setuid.pom
%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-libsetuid.pom
%{_datadir}/maven2/poms/JPP.jetty6.ext-%{name}-setuid-java.pom
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty ext  Subpackage Files

%if %with plus
# ========= Start of Jetty plus Subpackage Files
%files -n %{jettyname}6-plus
%dir %{_javadir}/%{name}/plus
%{_javadir}/%{name}/plus/*.jar
%{_javadir}/%{name}/%{name}-plus.jar
%dir %{vardir}/plus
%{vardir}/plus/%{name}-plus.jar
%{vardir}/%{name}-plus.jar
%config(noreplace) %{confdir}/jetty-plus.xml
%{_datadir}/maven2/poms/JPP.jetty6.plus-%{name}-plus.pom
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty plus  Subpackage Files
%endif

%if %with plus
# ========= Start of Jetty annotations Subpackage Files
%files -n %{jettyname}6-annotations
%dir %{_javadir}/%{name}/annotations
%dir %{vardir}/annotations
%{vardir}/annotations/%{name}-annotations.jar
%{_javadir}/%{name}/annotations/*.jar
%{_datadir}/maven2/poms/JPP.jetty6.annotations-%{name}-annotations.pom
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty annotations  Subpackage Files
%endif

# ========= Start of Jetty management Subpackage Files
%files -n %{jettyname}6-management
%dir %{_javadir}/%{name}/management
%{_javadir}/%{name}/management/*.jar
#%{_javadir}/%{name}/management/mx4j
%{_javadir}/%{name}/%{name}-management.jar
%dir %{vardir}/management
%{vardir}/management/%{name}-management.jar
%{vardir}/%{name}-management.jar
%config(noreplace) %{confdir}/jetty-jmx.xml
%{_datadir}/maven2/poms/JPP.jetty6.management-%{name}-management.pom
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty management  Subpackage Files

# ========= Start of Jetty naming Subpackage Files
%files -n %{jettyname}6-naming
%dir %{_javadir}/%{name}/naming
%{_javadir}/%{name}/naming/*.jar
%{_javadir}/%{name}/%{name}-naming.jar
%dir %{vardir}/naming
%{vardir}/naming/%{name}-naming.jar
%{vardir}/%{name}-naming.jar
%{_datadir}/maven2/poms/JPP.jetty6.naming-%{name}-naming.pom
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty naming  Subpackage Files

# ========= Start of Jetty spring Subpackage Files
%files -n %{jettyname}6-spring
%dir %{_javadir}/%{name}/spring
%{_javadir}/%{name}/spring/*.jar
%dir %{vardir}/spring
%{vardir}/spring/%{name}-spring.jar
%{_datadir}/maven2/poms/JPP.jetty6.spring-%{name}-spring.pom
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty spring  Subpackage Files

%if %with xbean
# ========= Start of Jetty xbean Subpackage Files
%files -n %{jettyname}6-xbean
%dir %{_javadir}/%{name}/xbean
%{_javadir}/%{name}/xbean/*.jar
%dir %{vardir}/xbean
%{vardir}/xbean/%{name}-xbean.jar
%{_datadir}/maven2/poms/JPP.jetty6.xbean-%{name}-xbean.pom
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty xbean  Subpackage Files
%endif

%if %with cometd
# ========= Start of Jetty cometd Subpackage Files
%if_with cometd
%files -n %{jettyname}6-cometd
%dir %{_javadir}/%{name}/cometd
%{_javadir}/%{name}/cometd/*.jar
%dir %{vardir}/cometd
%{vardir}/cometd/cometd-client.jar
%{vardir}/cometd/cometd-client-tests.jar
%{vardir}/cometd/cometd-oort.jar
%{vardir}/cometd/cometd-server.jar
%{_datadir}/maven2/poms/JPP.jetty6.cometd-cometd-oort.pom
%{_datadir}/maven2/poms/JPP.jetty6.cometd-cometd-client.pom
%{_datadir}/maven2/poms/JPP.jetty6.cometd-cometd-server.pom
%{_datadir}/maven2/poms/JPP.jetty6.cometd-project.pom
%{ctxdir}/cometd.xml
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty cometd  Subpackage Files
%endif
%endif #cometd

# ========= Start of Jetty ant Subpackage Files
%files -n %{jettyname}6-ant
%dir %{_javadir}/%{name}/ant
%{_javadir}/%{name}/ant/*.jar
%dir %{vardir}/ant
%{vardir}/ant/%{name}-ant.jar
%{_datadir}/maven2/poms/JPP.jetty6.ant-%{name}-ant.pom
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty ant  Subpackage Files

%if %with wadi
# ========= Start of Jetty wadi Subpackage Files
%if_with wadi
%files -n %{jettyname}6-wadi
%dir %{_javadir}/%{name}/wadi
%{_javadir}/%{name}/wadi/*.jar
%dir %{vardir}/wadi
%{vardir}/wadi/%{name}-wadi-session-manager.jar
%{_datadir}/maven2/poms/JPP.jetty6.wadi-%{name}-wadi-session-manager.pom
%{ctxdir}/wadi.xml
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty wadi  Subpackage Files
%endif
%endif #wadi

# ========= Start of Jetty embedded Subpackage Files
%files -n %{jettyname}6-embedded
%dir %{_javadir}/%{name}/embedded
%{_javadir}/%{name}/embedded/*.jar
%dir %{vardir}/embedded
%{vardir}/embedded/%{name}-embedded.jar
%{_datadir}/maven2/poms/JPP.jetty6.embedded-%{name}-embedded.pom
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty embedded  Subpackage Files

# ========= Start of Jetty extratests Subpackage Files
%files -n %{jettyname}6-extratests
%dir %{_javadir}/%{name}/extratests
%{_javadir}/%{name}/extratests/*.jar
%dir %{vardir}/extratests
%{vardir}/extratests/%{name}-extratests.jar
%{_datadir}/maven2/poms/JPP.jetty6.extratests-%{name}-extratests.pom
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty extratests  Subpackage Files

# ========= Start of Jetty grizzly Subpackage Files
%if_with grizzly
%files -n %{jettyname}6-grizzly
%dir %{_javadir}/%{name}/grizzly
%{_javadir}/%{name}/grizzly/*.jar
%dir %{vardir}/grizzly
%{vardir}/grizzly/%{name}-grizzly.jar
%config(noreplace) %{confdir}/jetty-grizzly.xml
%{_datadir}/maven2/poms/JPP.jetty6.grizzly-%{name}-grizzly.pom
%doc *.txt
%doc LICENSES/LICENSE*.txt
%endif #grizzly
# ========= End of Jetty grizzly  Subpackage Files

# ========= Start of Jetty j2se6 Subpackage Files
%files -n %{jettyname}6-j2se6
%dir %{_javadir}/%{name}/j2se6
%{_javadir}/%{name}/j2se6/*.jar
%dir %{vardir}/j2se6
%{vardir}/j2se6/%{name}-j2se6.jar
%{_datadir}/maven2/poms/JPP.jetty6.j2se6-%{name}-j2se6.pom
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty j2se6  Subpackage Files

# ========= Start of Jetty start-daemon Subpackage Files
%files -n %{jettyname}6-start-daemon
%dir %{_javadir}/%{name}/start-daemon
%{_javadir}/%{name}/start-daemon/*.jar
%dir %{vardir}/start-daemon
%{vardir}/start-daemon/%{name}-start-daemon.jar
%{_datadir}/maven2/poms/JPP.jetty6.start-daemon-%{name}-start-daemon.pom
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty start-daemon  Subpackage Files

# ========= Start of Jetty sweeper Subpackage Files
%files -n %{jettyname}6-sweeper
%dir %{_javadir}/%{name}/sweeper
%{_javadir}/%{name}/sweeper/*.jar
%dir %{vardir}/sweeper
%{vardir}/sweeper/%{name}-sweeper.jar
%{_datadir}/maven2/poms/JPP.jetty6.sweeper-%{name}-sweeper.pom
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty sweeper  Subpackage Files

%if_with terracotta
# ========= Start of Jetty terracotta Subpackage Files
%files -n %{jettyname}6-terracotta
%dir %{_javadir}/%{name}/terracotta
%{_javadir}/%{name}/terracotta/*.jar
%dir %{vardir}/terracotta
%{vardir}/terracotta/%{name}-terracotta-sessions.jar
%{_datadir}/maven2/poms/JPP.jetty6.terracotta-%{name}-terracotta-sessions.pom
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty terracotta  Subpackage Files
%endif

# ========= Start of Jetty util5 Subpackage Files
%files -n %{jettyname}6-util5
%dir %{_javadir}/%{name}/jre1.5
%{_javadir}/%{name}/jre1.5/*.jar
%dir %{vardir}/jre1.5
%{vardir}/jre1.5/%{name}-util5.jar
%{_datadir}/maven2/poms/JPP.jetty6.jre1.5-%{name}-util5.pom
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty util5  Subpackage Files

# ========= Start of Jetty Maven Plugins Subpackage Files
%files -n %{jettyname}6-maven2-plugins
%dir %{_javadir}/%{name}/maven2
%{_javadir}/%{name}/maven2/*.jar
%dir %{vardir}/maven2
%{vardir}/maven2/*.jar
%{_datadir}/maven2/poms/JPP.%{name}.maven2-jetty6-jspc-maven-plugin.pom
%{_datadir}/maven2/poms/JPP.%{name}.maven2-jetty6-maven-plugin.pom
%{_datadir}/maven2/plugins/*
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty Maven Plugin Subpackage Files

# ========= Start of Jetty Javadoc Subpackage Files
%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{ctxdir}/javadoc.xml
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty Javadoc Subpackage Files

# ========= Start of Jetty JBoss Subpackage Files
%if_with jboss
%files jboss
%{_datadir}/%{name}/*.sar
%doc *.txt
%doc LICENSES/LICENSE*.txt
%endif #jboss
# ========= End of Jetty Webapps Subpackage Files

# ========= Start of Jetty Webapps Subpackage Files
%files webapps
%{appdir}/*
%{ctxdir}/README*
%{ctxdir}/test*
%config(noreplace) %{confdir}/jetty-jaas.xml
%config(noreplace) %{confdir}/login.conf
%config(noreplace) %{confdir}/login.properties
%doc *.txt
%doc LICENSES/LICENSE*.txt
# ========= End of Jetty Webapps Subpackage Files

%changelog
* Sun Jun 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:6.1.26-alt5_1jpp6
- build with maven-enforcer-api

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:6.1.26-alt4_1jpp6
- fixed build with new testng and xbean

* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:6.1.26-alt3_1jpp6
- fixed build with maven3

* Sun Feb 26 2012 Igor Vlasenko <viy@altlinux.ru> 0:6.1.26-alt2_1jpp6
- fixed build

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:6.1.26-alt1_1jpp6
- new version

* Tue Apr 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:6.1.22-alt5_2jpp6
- fixed build

* Mon Jan 31 2011 Igor Vlasenko <viy@altlinux.ru> 0:6.1.22-alt4_2jpp6
- fixed build

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:6.1.22-alt3_2jpp6
- fixed user/group creation (closes: #24688)

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0:6.1.22-alt2_2jpp6
- added OSGi manifest

* Fri Oct 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:6.1.22-alt1_2jpp6
- fixed build; added api subpackages; 
- full build w/o example webapps (and cometd as dependency)

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:6.1.22-alt1_1jpp6
- new version (closes: #19914)

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:6.1.14-alt2_1jpp5
- explicit selection of java5 compiler

* Thu Jun 11 2009 Igor Vlasenko <viy@altlinux.ru> 0:6.1.14-alt1_1jpp5
- new version

* Tue Feb 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:6.1.7-alt1_4jpp5
- new version (disabled jetty6-wadi)

