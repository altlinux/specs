# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java rpm-macros-fedora-compat
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: eclipse-equinox-osgi felix-osgi-foundation xpp3-minimal maven-antrun-plugin eclipse-jdt
BuildRequires: jetty-orbit-maven-depmap
Requires: jetty-orbit-maven-depmap
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jetty
%define version 8.1.5
# Copyright (c) 2000-2007, JPackage Project
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

%global jettyname   jetty
%global jtuid       110
%global username    %{name}
%global confdir     %{_sysconfdir}/%{name}
%global logdir      %{_var}/log/%{name}
%global apphomedir     %{_datadir}/%{name}
%global jettycachedir %{_var}/cache/%{name}
%global tempdir     %{jettycachedir}/temp
%global rundir      %{_var}/run/%{name}
%global jettylibdir %{_var}/lib/%{name}
%global appdir      %{jettylibdir}/webapps

%global addver v20120716

Name:           jetty
Version:        8.1.5
Release:        alt2_6jpp7
Summary:        Java Webserver and Servlet Container

Group:          Networking/WWW
# Jetty is dual licensed under both ASL 2.0 and EPL 1.0, see NOTICE.txt
License:        ASL 2.0 or EPL
URL:            http://jetty.mortbay.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.project.git/snapshot/jetty-%{version}.%{addver}.tar.bz2
Source1:        djetty.script
Source3:        jetty.logrotate
Source4:        %{name}-depmap.xml
Source5:        %{name}.service
Patch0:         %{name}-create-work-dir.patch
Patch4:         0004-Modify-dependencies.patch

BuildRequires:  geronimo-annotation
BuildRequires:  geronimo-jaspic-spec
BuildRequires:  geronimo-jta
BuildRequires:  glassfish-jsp
BuildRequires:  glassfish-jsp-api
BuildRequires:  jakarta-taglibs-standard
BuildRequires:  jpackage-utils
BuildRequires:  jvnet-parent
BuildRequires:  maven
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-war-plugin
BuildRequires:  objectweb-asm
BuildRequires:  slf4j
BuildRequires:  tomcat-el-2.2-api
BuildRequires:  tomcat-jsp-2.2-api
BuildRequires:  tomcat-lib
BuildRequires:  tomcat-servlet-3.0-api

%if 0%{?rhel} <= 0
BuildRequires:  eclipse-platform
BuildRequires:  eclipse-rcp
BuildRequires:  mongo-java-driver >= 2.6.5-4
%endif

# we want javamail not classpathx-javamail
BuildRequires:  %{_javadir}/javamail/mail.jar
BuildRequires:  jetty-parent
BuildRequires:  jetty-distribution-remote-resources
BuildRequires:  jetty-build-support
BuildRequires:  jetty-version-maven-plugin
BuildRequires:  jetty-toolchain
BuildRequires:  jetty-assembly-descriptors
BuildRequires:  jetty-test-policy
BuildRequires:  jetty-artifact-remote-resources


BuildArch:      noarch

Requires:       jpackage-utils
Requires:       jetty-ajp = %{version}-%{release}
Requires:       jetty-annotations = %{version}-%{release}
Requires:       jetty-client = %{version}-%{release}
Requires:       jetty-continuation = %{version}-%{release}
Requires:       jetty-deploy = %{version}-%{release}
Requires:       jetty-http = %{version}-%{release}
Requires:       jetty-io = %{version}-%{release}
Requires:       jetty-jmx = %{version}-%{release}
Requires:       jetty-jndi = %{version}-%{release}
Requires:       jetty-overlay-deployer = %{version}-%{release}
Requires:       jetty-plus = %{version}-%{release}
Requires:       jetty-policy = %{version}-%{release}
Requires:       jetty-rewrite = %{version}-%{release}
Requires:       jetty-security = %{version}-%{release}
Requires:       jetty-server = %{version}-%{release}
Requires:       jetty-servlet = %{version}-%{release}
Requires:       jetty-servlets = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       jetty-webapp = %{version}-%{release}
Requires:       jetty-websocket = %{version}-%{release}
Requires:       jetty-xml = %{version}-%{release}
# These are not required by main jetty server so we don't require them
# in RPM. Install as necessary:
#  * jetty-http-spi
#  * jetty-jaspi
#  * jetty-nested
#  * jetty-nosql
#  * jetty-osgi

Requires(pre):    shadow-utils

Provides:       group(%username) = %jtuid
Provides:       user(%username) = %jtuid

Obsoletes: %{name}-manual < %{version}-%{release}
Source44: import.info
Source45: jetty.init

%description
%%global desc \
Jetty is a 100%% Java HTTP Server and Servlet Container. This means that you\
do not need to configure and run a separate web server (like Apache) in order\
to use Java, servlets and JSPs to generate dynamic content. Jetty is a fully\
featured web server for static and dynamic content. Unlike separate\
server/container solutions, this means that your web server and web\
application run in the same process, without interconnection overheads\
and complications. Furthermore, as a pure java component, Jetty can be simply\
included in your application for demonstration, distribution or deployment.\
Jetty is available on all Java supported platforms.
%%{desc}
%%global extdesc %%{desc}\
\
This package contains

%package        project
Summary:        POM files for Jetty
Group:          Development/Java
Requires:       jpackage-utils
Requires:       jetty-parent

%description    project
%%{extdesc} %%{summary}.

%package        ajp
Group: Networking/WWW
Summary:        ajp module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-http = %{version}-%{release}
Requires:       jetty-io = %{version}-%{release}
Requires:       jetty-server = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       tomcat-servlet-3.0-api
%description    ajp
%%{extdesc} %%{summary}.

%package        annotations
Group: Networking/WWW
Summary:        annotations module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-plus = %{version}-%{release}
Requires:       jetty-security = %{version}-%{release}
Requires:       jetty-server = %{version}-%{release}
Requires:       jetty-servlet = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       jetty-webapp = %{version}-%{release}
Requires:       objectweb-asm
Requires:       geronimo-annotation
Requires:       tomcat-lib
%description    annotations
%%{extdesc} %%{summary}.

%package        client
Group: Networking/WWW
Summary:        client module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-http = %{version}-%{release}
Requires:       jetty-io = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}

%description    client
%%{extdesc} %%{summary}.

%package        continuation
Group: Networking/WWW
Summary:        continuation module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       tomcat-servlet-3.0-api
%description    continuation
%%{extdesc} %%{summary}.

%package        deploy
Group: Networking/WWW
Summary:        deploy module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-jmx = %{version}-%{release}
Requires:       jetty-server = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       jetty-webapp = %{version}-%{release}
Requires:       jetty-xml = %{version}-%{release}

%description    deploy
%%{extdesc} %%{summary}.

%package        http
Group: Networking/WWW
Summary:        http module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-io = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       tomcat-servlet-3.0-api
%description    http
%%{extdesc} %%{summary}.

%package        http-spi
Group: Networking/WWW
Summary:        http-spi module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-server = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       tomcat-servlet-3.0-api

%description    http-spi
%%{extdesc} %%{summary}.

%package        io
Group: Networking/WWW
Summary:        io module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}

%description    io
%%{extdesc} %%{summary}.

%package        jaspi
Group: Networking/WWW
Summary:        jaspi module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-security = %{version}-%{release}
Requires:       jetty-server = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       geronimo-jaspic-spec
Requires:       tomcat-servlet-3.0-api

%description    jaspi
%%{extdesc} %%{summary}.

%package        jmx
Group: Networking/WWW
Summary:        jmx module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}

%description    jmx
%%{extdesc} %%{summary}.

%package        jndi
Group: Networking/WWW
Summary:        jndi module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-server = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       jetty-webapp = %{version}-%{release}
Requires:       %{_javadir}/javamail/mail.jar

%description    jndi
%%{extdesc} %%{summary}.

%package        monitor
Group: Networking/WWW
Summary:        monitor module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-client = %{version}-%{release}
Requires:       jetty-io = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       jetty-xml = %{version}-%{release}

%description    monitor
%%{extdesc} %%{summary}.

%package        nested
Group: Networking/WWW
Summary:        nested module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-http = %{version}-%{release}
Requires:       jetty-io = %{version}-%{release}
Requires:       jetty-server = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       tomcat-servlet-3.0-api

%description    nested
%%{extdesc} %%{summary}.

%package        overlay-deployer
Group: Networking/WWW
Summary:        overlay-deployer module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-deploy = %{version}-%{release}
Requires:       jetty-http = %{version}-%{release}
Requires:       jetty-jndi = %{version}-%{release}
Requires:       jetty-server = %{version}-%{release}
Requires:       jetty-servlet = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       jetty-webapp = %{version}-%{release}
Requires:       jetty-xml = %{version}-%{release}
Requires:       geronimo-jta
Requires:       tomcat-servlet-3.0-api

%description    overlay-deployer
%%{extdesc} %%{summary}.

%package        plus
Group: Networking/WWW
Summary:        plus module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-jndi = %{version}-%{release}
Requires:       jetty-security = %{version}-%{release}
Requires:       jetty-server = %{version}-%{release}
Requires:       jetty-servlet = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       jetty-webapp = %{version}-%{release}
Requires:       jetty-xml = %{version}-%{release}
Requires:       tomcat-servlet-3.0-api

%description    plus
%%{extdesc} %%{summary}.

%package        policy
Group: Networking/WWW
Summary:        policy module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}

%description    policy
%%{extdesc} %%{summary}.

%package        rewrite
Group: Networking/WWW
Summary:        rewrite module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-client = %{version}-%{release}
Requires:       jetty-http = %{version}-%{release}
Requires:       jetty-io = %{version}-%{release}
Requires:       jetty-server = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       tomcat-servlet-3.0-api

%description    rewrite
%%{extdesc} %%{summary}.

%package        security
Group: Networking/WWW
Summary:        security module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-http = %{version}-%{release}
Requires:       jetty-server = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       tomcat-servlet-3.0-api

%description    security
%%{extdesc} %%{summary}.

%package        server
Group: Networking/WWW
Summary:        server module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-continuation = %{version}-%{release}
Requires:       jetty-http = %{version}-%{release}
Requires:       jetty-io = %{version}-%{release}
Requires:       jetty-jmx = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       tomcat-servlet-3.0-api

%description    server
%%{extdesc} %%{summary}.

%package        servlet
Group: Networking/WWW
Summary:        servlet module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-continuation = %{version}-%{release}
Requires:       jetty-http = %{version}-%{release}
Requires:       jetty-io = %{version}-%{release}
Requires:       jetty-jmx = %{version}-%{release}
Requires:       jetty-security = %{version}-%{release}
Requires:       jetty-server = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       tomcat-servlet-3.0-api

%description    servlet
%%{extdesc} %%{summary}.

%package        servlets
Group: Networking/WWW
Summary:        servlets module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-client = %{version}-%{release}
Requires:       jetty-continuation = %{version}-%{release}
Requires:       jetty-http = %{version}-%{release}
Requires:       jetty-io = %{version}-%{release}
Requires:       jetty-server = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       jetty-webapp = %{version}-%{release}
Requires:       tomcat-servlet-3.0-api

%description    servlets
%%{extdesc} %%{summary}.

%package        util
Group: Networking/WWW
Summary:        util module for Jetty
# Utf8Appendable.java is additionally under MIT license
License:        (ASL 2.0 or EPL) and MIT
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       tomcat-servlet-3.0-api
Requires:       slf4j

%description    util
%%{extdesc} %%{summary}.

%package        webapp
Group: Networking/WWW
Summary:        webapp module for Jetty
License:        ASL 2.0 or EPL
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-http = %{version}-%{release}
Requires:       jetty-io = %{version}-%{release}
Requires:       jetty-security = %{version}-%{release}
Requires:       jetty-server = %{version}-%{release}
Requires:       jetty-servlet = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       jetty-xml = %{version}-%{release}
Requires:       glassfish-jsp
Requires:       glassfish-jsp-api
Requires:       jakarta-taglibs-standard
Requires:       tomcat-servlet-3.0-api

%description    webapp
%%{extdesc} %%{summary}.

%package        websocket
Group: Networking/WWW
Summary:        websocket module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-http = %{version}-%{release}
Requires:       jetty-io = %{version}-%{release}
Requires:       jetty-server = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       tomcat-servlet-3.0-api

%description    websocket
%%{extdesc} %%{summary}.

%package        xml
Group: Networking/WWW
Summary:        xml module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}

%description    xml
%%{extdesc} %%{summary}.

%if 0%{?rhel} <= 0
%package        nosql
Group: Networking/WWW
Summary:        nosql module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-server = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       mongo-java-driver >= 2.6.5-4
Requires:       tomcat-servlet-3.0-api

%description    nosql
%%{extdesc} %%{summary}.

%package        osgi
Group: Networking/WWW
Summary:        OSGi module for Jetty
Requires:       jpackage-utils
Requires:       jetty-project = %{version}-%{release}
Requires:       jetty-annotations = %{version}-%{release}
Requires:       jetty-deploy = %{version}-%{release}
Requires:       jetty-nested = %{version}-%{release}
Requires:       jetty-server = %{version}-%{release}
Requires:       jetty-servlet = %{version}-%{release}
Requires:       jetty-util = %{version}-%{release}
Requires:       jetty-webapp = %{version}-%{release}
Requires:       jetty-xml = %{version}-%{release}
Requires:       eclipse-platform
Requires:       eclipse-rcp
Requires:       glassfish-jsp
Requires:       glassfish-jsp-api
Requires:       tomcat-servlet-3.0-api
Requires:       tomcat-el-2.2-api
Requires:       tomcat-jsp-2.2-api
Requires:       tomcat-lib

%description    osgi
%%{extdesc} %%{summary}.
%endif

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
# some MIT-licensed code (from Utf8Appendable) is used to generate javadoc
License:        (ASL 2.0 or EPL) and MIT
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
%%{summary}.

%prep
%setup -q -n %{jettyname}-%{version}.%{addver}
for f in $(find . -name "*.?ar"); do rm $f; done
find . -name "*.class" -exec rm {} \;

%patch0 -p2 -b .sav
%patch4 -p1 -b .sav

# Remove javadoc execution
# We generate javadoc as a separate step
%pom_remove_plugin :maven-javadoc-plugin jetty-aggregate/jetty-all
%pom_remove_dep :jetty-all jetty-distribution

# Disable test artifacts
# they need more dependencies then we have time for right now :-)
%pom_disable_module tests
%pom_disable_module test-continuation
%pom_disable_module test-jetty-nested
%pom_disable_module test-jetty-servlet
%pom_disable_module test-jetty-osgi jetty-osgi

# Change servelt groupId to javax.servlet
%pom_xpath_inject "pom:project/pom:properties" "
    <servlet.spec.groupId>javax.servlet</servlet.spec.groupId>
    <servlet.spec.artifactId>servlet-api</servlet.spec.artifactId>
    <servlet.spec.version>3.0.20100224</servlet.spec.version>"

# Prevents problem with "Reporting mojo's can only be called from
# ReportDocumentRender". Investigate proper fix some other time?
%pom_remove_plugin :maven-pmd-plugin

# Remove unpack-config-deps from distribution
#
# This is needed because original code used classifiers to select subset
# of artifacts. Unfortunately there seems to be a weird bug affecting even
# upstream maven when this goes outside of reactor resolver. Or perhaps
# this is a weird feature.
#
# Our resolver obviously can't handle this so we have to unpack these
# manually before building distribution
%pom_xpath_remove "pom:execution[pom:id[text()='unpack-config-deps']]" jetty-distribution

# Disable SPDY for now as there are missing dependencies
# (like some TLS extensions for OpenJDK)
%pom_disable_module jetty-spdy
%pom_remove_dep org.eclipse.jetty.spdy: jetty-distribution
%pom_xpath_remove "pom:execution[pom:id[text()='copy-spdy']]" jetty-distribution

%if 0%{?rhel} > 0
# Disable OSGi
%pom_disable_module jetty-osgi
%pom_xpath_remove "pom:profile[pom:id[text()='osgi']]"

# Disable NoSQL
%pom_disable_module jetty-nosql
%endif

# Use Glassfish JSP
%pom_remove_dep :org.eclipse.jdt.core jetty-jsp
%pom_xpath_inject "pom:project/pom:dependencies" "
    <dependency>
      <groupId>org.glassfish.web</groupId>
      <artifactId>javax.servlet.jsp</artifactId>
      <version>any</version>
    </dependency>" jetty-jsp

cp %{SOURCE1} djetty

# this needs jetty6 things, so just remove it
# shouldn't cause any trouble since it handled only in loadClass elsewhere
rm jetty-continuation/src/main/java/org/eclipse/jetty/continuation/Jetty6Continuation.java

iconv -f iso-8859-1 -t utf-8 LICENSE-CONTRIBUTOR/CDDLv1.0.txt > \
      LICENSE-CONTRIBUTOR/CDDLv1.0.txt.con
mv LICENSE-CONTRIBUTOR/CDDLv1.0.txt{.con,}

%build
: rm -rf ./*
: ln -sf ~/temp/jetty/jetty-8.1.0.%{addver}.copy/* .
: exit 0
# remove previous lines!
sed -i -e "s|/usr/share|%{_datadir}|g" djetty

mvn-rpmbuild  -e \
    -Dmaven.local.depmap.file=%{SOURCE4} \
    -Dmaven.test.skip=true \
    install javadoc:aggregate
cd jetty-distribution
rm -rf target/distribution
mkdir -p target/distribution
find .. -ipath '*target/*config.jar' | ( while read; do
  unzip $REPLY -x 'META-INF/*' -d target/distribution
done)

mvn-rpmbuild \
    -Dmaven.repo.local=$(pwd)/../.m2 \
    -Dmaven.local.depmap.file=%{SOURCE4} \
    -Dmaven.test.skip=true \
    install javadoc:aggregate

%install
# dirs
install -dm 755 %{buildroot}%{_bindir}
install -dm 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -dm 755 %{buildroot}%{_javadir}/%{name}


install -dm 755 %{buildroot}%{_javadocdir}/%{name}
install -dm 755 %{buildroot}%{confdir}
install -dm 755 %{buildroot}%{apphomedir}
install -dm 755 %{buildroot}%{logdir}
install -dm 755 %{buildroot}%{rundir}
install -dm 755 %{buildroot}%{tempdir}
install -dm 755 %{buildroot}%{appdir}
install -dm 755 %{buildroot}%{_unitdir}

# systemd unit file
cp %{SOURCE5} %{buildroot}%{_unitdir}/

# main pkg
tar xvf jetty-distribution/target/%{name}-distribution-%{version}.%{addver}.tar.gz -C %{buildroot}%{apphomedir}
mv %{buildroot}%{apphomedir}/%{name}-distribution-%{version}.%{addver}/* %{buildroot}%{apphomedir}/
rm -rf %{buildroot}%{apphomedir}/%{name}-distribution-%{version}.%{addver}
rm -f %{buildroot}%{apphomedir}/bin/*cygwin*

chmod +x %{buildroot}%{apphomedir}/bin/jetty-xinetd.sh
chmod +x djetty
mv djetty %{buildroot}%{_bindir}/djetty
ln -s %{apphomedir}/bin/jetty.sh %{buildroot}%{_bindir}/%{name}
install -pm 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
echo '# Placeholder configuration file.  No default is provided.' > \
     %{buildroot}%{confdir}/jetty.conf

# make sure jetty knows where to look for jars
sed -i "1{s:^:lib=%{apphomedir}/lib\n:}" %{buildroot}%{apphomedir}/start.ini
mv %{buildroot}%{apphomedir}/start.ini %{buildroot}%{confdir}
ln -s %{confdir}/start.ini %{buildroot}%{apphomedir}


install -dm 755 %{buildroot}%{_mavenpomdir}
for module in jetty-ajp jetty-annotations jetty-client jetty-continuation \
           jetty-deploy jetty-http jetty-io jetty-jmx jetty-jndi \
           jetty-overlay-deployer jetty-plus jetty-policy \
           jetty-rewrite jetty-security jetty-server jetty-servlet \
           jetty-servlets jetty-util jetty-webapp jetty-websocket \
           jetty-xml; do
    mv %{buildroot}%{apphomedir}/lib/$module-*.jar \
           %{buildroot}%{_javadir}/%{name}/$module.jar
    ln -s  %{_javadir}/%{name}/$module.jar \
           %{buildroot}%{apphomedir}/lib/$module-%{version}.%{addver}.jar
    install -pm 644 $module/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-$module.pom
    %add_maven_depmap JPP.%{name}-$module.pom %{name}/$module.jar -f $module
done

# modules used during build and other jars not included in the
# distribution tarball
for module in jetty-http-spi jetty-jaspi jetty-nested; do
    install -m 644 $module/target/$module-%{version}.%{addver}.jar \
           %{buildroot}%{_javadir}/%{name}/$module.jar
    install -pm 644 $module/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-$module.pom
    %add_maven_depmap JPP.%{name}-$module.pom %{name}/$module.jar -f $module
done

%if 0%{?rhel} <= 0
install -m 644 jetty-nosql/target/jetty-nosql-%{version}.%{addver}.jar \
        %{buildroot}%{_javadir}/%{name}/jetty-nosql.jar
install -pm 644 jetty-nosql/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-jetty-nosql.pom
%add_maven_depmap JPP.%{name}-jetty-nosql.pom %{name}/jetty-nosql.jar -f jetty-nosql

pushd jetty-osgi
    install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-jetty-osgi.pom
    %add_maven_depmap JPP.%{name}-jetty-osgi.pom -f jetty-osgi
    for submod in boot boot-jsp boot-warurl;do
        module=jetty-osgi-$submod
        install -m 644 $module/target/$module-%{version}.%{addver}.jar \
           %{buildroot}%{_javadir}/%{name}/$module.jar
        install -pm 644 $module/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-$module.pom
        %add_maven_depmap JPP.%{name}-$module.pom %{name}/$module.jar -f jetty-osgi
    done

    #httpservice is a bit special (for no good reason)
    module=jetty-httpservice
    install -m 644 jetty-osgi-httpservice/target/$module-%{version}.%{addver}.jar \
        %{buildroot}%{_javadir}/%{name}/$module.jar
    install -pm 644 jetty-osgi-httpservice/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-$module.pom
    %add_maven_depmap JPP.%{name}-$module.pom %{name}/$module.jar -f jetty-osgi

popd
%endif

install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-project.pom
%add_maven_depmap JPP.%{name}-project.pom -f project

# purge bundled jars
rm %{buildroot}%{apphomedir}/lib/{annotations,jndi,jsp,jta}/*

# recreat tarball structure in lib
ln -sf $(build-classpath tomcat-servlet-3.0-api) \
       %{buildroot}%{apphomedir}/lib/servlet-api-3.0.jar

build-jar-repository %{buildroot}%{apphomedir}/lib/annotations \
                     objectweb-asm/asm-all geronimo-annotation

build-jar-repository %{buildroot}%{apphomedir}/lib/jndi javamail/mail

build-jar-repository %{buildroot}%{apphomedir}/lib/jsp tomcat-el-2.2-api \
           taglibs-core taglibs-standard glassfish-jsp \
           glassfish-jsp-api  tomcat/jasper tomcat/jasper-el tomcat/tomcat-api \
           tomcat/tomcat-juli tomcat/tomcat-jsp-2.2-api


ln -sf $(build-classpath geronimo-jta) \
       %{buildroot}%{apphomedir}/lib/jta/

mv %{buildroot}%{apphomedir}/lib/monitor/jetty-monitor-%{version}.%{addver}.jar \
   %{buildroot}%{_javadir}/%{name}/jetty-monitor.jar
ln -s %{_javadir}/%{name}/jetty-monitor.jar \
      %{buildroot}%{apphomedir}/lib/monitor/jetty-monitor-%{version}.%{addver}.jar
install -pm 644 jetty-monitor/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-jetty-monitor.pom
%add_maven_depmap JPP.%{name}-jetty-monitor.pom %{name}/jetty-monitor.jar -f jetty-monitor

mv %{buildroot}%{apphomedir}/start.jar \
   %{buildroot}%{_javadir}/%{name}/jetty-start.jar
ln -s %{_javadir}/%{name}/jetty-start.jar \
      %{buildroot}%{apphomedir}/start.jar
install -pm 644 jetty-start/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-jetty-start.pom
%add_maven_depmap JPP.%{name}-jetty-start.pom %{name}/jetty-start.jar


( cat << EO_RC
JAVA_HOME=/usr/lib/jvm/java
JAVA_OPTIONS=
JETTY_HOME=%{apphomedir}
JETTY_CONSOLE=%{logdir}/jetty-console.log
JETTY_PORT=8080
JETTY_RUN=%{_var}/run/%{name}
JETTY_PID=\$JETTY_RUN/jetty.pid
EO_RC
) > %{buildroot}%{apphomedir}/.jettyrc

mkdir -p %{buildroot}%{_sysconfdir}/tmpfiles.d
( cat << EOF
D /var/run/%{name} 0755 %username %{username} -
EOF
) > %{buildroot}%{_sysconfdir}/tmpfiles.d/%{name}.conf

rm -fr %{buildroot}%{apphomedir}/logs
ln -s %{logdir} %{buildroot}%{apphomedir}/logs

mv %{buildroot}%{apphomedir}/etc/* %{buildroot}/%{confdir}
rm -fr %{buildroot}%{apphomedir}/etc
ln -s %{confdir} %{buildroot}%{apphomedir}/etc

mv %{buildroot}%{apphomedir}/webapps/* %{buildroot}/%{appdir}
rm -fr %{buildroot}%{apphomedir}/webapps
ln -s %{appdir} %{buildroot}%{apphomedir}/webapps

rm %{buildroot}%{apphomedir}/*.txt  %{buildroot}%{apphomedir}/*.html

# Here jetty is going to put its runtime data.
# See: https://bugzilla.redhat.com/show_bug.cgi?id=845993
ln -sf %{rundir} %{buildroot}%{apphomedir}/work

# following seem like config directories
for cdir in overlays;do
   mv %{buildroot}%{apphomedir}/$cdir %{buildroot}/%{confdir}/$cdir
   ln -s %{confdir}/$cdir %{buildroot}%{apphomedir}/$cdir
done

# this should be symlinked the other way around but rpm doesn't let us
# do that! BAD BAD rpm
# https://bugzilla.redhat.com/show_bug.cgi?id=447156
for cdir in contexts contexts-available resources;do
    ln -sf %{apphomedir}/$cdir %{buildroot}/%{confdir}/$cdir
done

# javadocs
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

mkdir -p $RPM_BUILD_ROOT`dirname /etc/default/jetty8`
touch $RPM_BUILD_ROOT/etc/default/jetty8
install -D -m 755 %{S:45} %buildroot%_initdir/%name


%pre
getent group  %username &>/dev/null || groupadd -r  %username || :
getent passwd %username &>/dev/null || useradd  -r  -g %username \
                             -d %apphomedir -M -s /bin/sh %username || :

%post
%systemd_post jetty.service

%preun
%systemd_preun jetty.service

%postun
%systemd_postun_with_restart jetty.service


%files
%config(noreplace) %{_sysconfdir}/tmpfiles.d/%{name}.conf
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/logrotate.d/%{name}
%{_bindir}/*
%config(noreplace) %{confdir}
%dir %{jettylibdir}
%dir %{jettycachedir}
%{apphomedir}
%attr(755, jetty, jetty) %{logdir}
%attr(755, jetty, jetty) %{tempdir}
%ghost %dir %attr(755, jetty, jetty) %{rundir}
%{appdir}
%{_unitdir}/%{name}.service
%{_javadir}/%{name}/%{name}-start.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-start.pom
%{_mavendepmapfragdir}/%{name}
%config(noreplace,missingok) /etc/default/jetty8
%_initdir/%name

%files project
%doc NOTICE.txt README.txt VERSION.txt LICENSE*
%dir %{_javadir}/%{name}
%{_mavenpomdir}/JPP.%{name}-project.pom
%{_mavendepmapfragdir}/%{name}-project

%files ajp
%{_javadir}/%{name}/%{name}-ajp.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-ajp.pom
%{_mavendepmapfragdir}/%{name}-%{name}-ajp

%files annotations
%{_javadir}/%{name}/%{name}-annotations.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-annotations.pom
%{_mavendepmapfragdir}/%{name}-%{name}-annotations

%files client
%{_javadir}/%{name}/%{name}-client.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-client.pom
%{_mavendepmapfragdir}/%{name}-%{name}-client

%files continuation
%{_javadir}/%{name}/%{name}-continuation.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-continuation.pom
%{_mavendepmapfragdir}/%{name}-%{name}-continuation

%files deploy
%{_javadir}/%{name}/%{name}-deploy.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-deploy.pom
%{_mavendepmapfragdir}/%{name}-%{name}-deploy

%files http
%{_javadir}/%{name}/%{name}-http.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-http.pom
%{_mavendepmapfragdir}/%{name}-%{name}-http

%files http-spi
%{_javadir}/%{name}/%{name}-http-spi.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-http-spi.pom
%{_mavendepmapfragdir}/%{name}-%{name}-http-spi

%files io
%{_javadir}/%{name}/%{name}-io.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-io.pom
%{_mavendepmapfragdir}/%{name}-%{name}-io

%files jaspi
%{_javadir}/%{name}/%{name}-jaspi.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-jaspi.pom
%{_mavendepmapfragdir}/%{name}-%{name}-jaspi

%files jmx
%{_javadir}/%{name}/%{name}-jmx.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-jmx.pom
%{_mavendepmapfragdir}/%{name}-%{name}-jmx

%files jndi
%{_javadir}/%{name}/%{name}-jndi.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-jndi.pom
%{_mavendepmapfragdir}/%{name}-%{name}-jndi

%files monitor
%{_javadir}/%{name}/%{name}-monitor.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-monitor.pom
%{_mavendepmapfragdir}/%{name}-%{name}-monitor

%files nested
%{_javadir}/%{name}/%{name}-nested.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-nested.pom
%{_mavendepmapfragdir}/%{name}-%{name}-nested

%files overlay-deployer
%{_javadir}/%{name}/%{name}-overlay-deployer.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-overlay-deployer.pom
%{_mavendepmapfragdir}/%{name}-%{name}-overlay-deployer

%files plus
%{_javadir}/%{name}/%{name}-plus.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-plus.pom
%{_mavendepmapfragdir}/%{name}-%{name}-plus

%files policy
%{_javadir}/%{name}/%{name}-policy.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-policy.pom
%{_mavendepmapfragdir}/%{name}-%{name}-policy

%files rewrite
%{_javadir}/%{name}/%{name}-rewrite.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-rewrite.pom
%{_mavendepmapfragdir}/%{name}-%{name}-rewrite

%files security
%{_javadir}/%{name}/%{name}-security.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-security.pom
%{_mavendepmapfragdir}/%{name}-%{name}-security

%files server
%{_javadir}/%{name}/%{name}-server.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-server.pom
%{_mavendepmapfragdir}/%{name}-%{name}-server

%files servlet
%{_javadir}/%{name}/%{name}-servlet.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-servlet.pom
%{_mavendepmapfragdir}/%{name}-%{name}-servlet

%files servlets
%{_javadir}/%{name}/%{name}-servlets.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-servlets.pom
%{_mavendepmapfragdir}/%{name}-%{name}-servlets

%files util
%{_javadir}/%{name}/%{name}-util.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-util.pom
%{_mavendepmapfragdir}/%{name}-%{name}-util

%files webapp
%{_javadir}/%{name}/%{name}-webapp.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-webapp.pom
%{_mavendepmapfragdir}/%{name}-%{name}-webapp

%files websocket
%{_javadir}/%{name}/%{name}-websocket.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-websocket.pom
%{_mavendepmapfragdir}/%{name}-%{name}-websocket

%files xml
%{_javadir}/%{name}/%{name}-xml.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-xml.pom
%{_mavendepmapfragdir}/%{name}-%{name}-xml

%if 0%{?rhel} <= 0
%files nosql
%{_javadir}/%{name}/%{name}-nosql.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-nosql.pom
%{_mavendepmapfragdir}/%{name}-%{name}-nosql

%files osgi
%{_javadir}/%{name}/%{name}-osgi*.jar
%{_javadir}/%{name}/%{name}-httpservice.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-osgi*.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-httpservice.pom
%{_mavendepmapfragdir}/%{name}-%{name}-osgi
%endif

%files javadoc
%doc NOTICE.txt LICENSE*
%doc %{_javadocdir}/%{name}

%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 8.1.5-alt2_6jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 8.1.5-alt1_6jpp7
- fc update

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.5-alt1_5jpp7
- new version (closes: #27671)

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.5-alt1_2jpp7
- prebuild using manual depmap 

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.0-alt4_4jpp7
- fixed build

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.0-alt3_4jpp7
- rebuild

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.0-alt2_4jpp7
- fixed %pre

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.0-alt1_4jpp7
- full version

