BuildRequires: java-1.5.0-devel
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
%define version 2.5.1
%define name jboss-remoting
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

%define repodir %{_javadir}/repository.jboss.com/jboss/remoting/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%bcond_without repolib


Name:           jboss-remoting
Version:        2.5.1
Release:	alt2_4jpp6
Epoch:          0
Summary:        JBoss Remoting
Group:          Development/Java
License:        LGPLv2+
URL:            http://www.jboss.org
# -q svn export http://anonsvn.jboss.org/repos/jbossremoting/remoting2/tags/2.5.1/ jboss-remoting-2.5.1
Source0:        jboss-remoting-2.5.1.tar.gz
Source1:        http://repository.jboss.com/maven2/org/jboss/remoting/jboss-remoting/2.5.1/jboss-remoting-2.5.1.pom
Source2:        jboss-remoting-component-info.xml


BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  jboss-jrunit
BuildRequires:  junit

BuildRequires:  aopalliance
BuildRequires:  concurrent
BuildRequires:  dom4j
BuildRequires:  gnu-trove
BuildRequires:  hessian
BuildRequires:  jakarta-commons-logging
BuildRequires:  jboss-common-core
BuildRequires:  jboss-common-logging-log4j
BuildRequires:  jboss-common-logging-spi
BuildRequires:  jboss-j2se
BuildRequires:  jboss-naming
BuildRequires:  jboss-serialization
BuildRequires:  jbossweb >= 0:2.1.3
BuildRequires:  jcommon
BuildRequires:  jfreechart
BuildRequires:  jgroups
BuildRequires:  log4j
BuildRequires:  jbossweb2-servlet-2.5-api
BuildRequires:  spring
BuildRequires:  spring-aop
BuildRequires:  spring-beans
BuildRequires:  spring-context
BuildRequires:  spring-core
BuildRequires:  spring-remoting
BuildRequires:  spring-web
BuildRequires:  spring-webmvc

Requires:  concurrent
Requires:  jbossweb
Requires:  jboss-common-core
Requires:  jboss-common-logging-spi
Requires:  jboss-j2se
Requires:  jboss-naming
Requires:  jboss-serialization
Requires:  log4j
Requires:  servlet_2_5_api

Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
JBoss remoting.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
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
%{_bindir}/find . -name "*.jar" | %{_bindir}/xargs -t %{__rm}
#BUILD/jboss-remoting-2.5.1/lib/oswego-concurrent/lib/concurrent.jar.no
ln -sf $(build-classpath concurrent) lib/oswego-concurrent/lib/
#BUILD/jboss-remoting-2.5.1/lib/jboss/jboss-logging-spi.jar.no
ln -sf $(build-classpath jboss-common-logging-spi) lib/jboss/jboss-logging-spi.jar
#BUILD/jboss-remoting-2.5.1/lib/jboss/jboss-logging-log4j.jar.no
ln -sf $(build-classpath jboss-common-logging-log4j) lib/jboss/jboss-logging-log4j.jar
#BUILD/jboss-remoting-2.5.1/lib/jboss/jboss-common-core.jar.no
ln -sf $(build-classpath jboss-common-core) lib/jboss/
#BUILD/jboss-remoting-2.5.1/lib/jboss/jnpserver.jar.no
ln -sf $(build-classpath jboss-naming/jnpserver) lib/jboss/
#BUILD/jboss-remoting-2.5.1/lib/sun-servlet/lib/servlet-api.jar.no
ln -sf $(build-classpath servlet_2_5_api) lib/sun-servlet/lib/servlet-api.jar
#BUILD/jboss-remoting-2.5.1/lib/jboss/jboss-j2se.jar.no
ln -sf $(build-classpath jboss-j2se/jboss-j2se) lib/jboss/
#BUILD/jboss-remoting-2.5.1/lib/jboss/jboss-serialization.jar.no
ln -sf $(build-classpath jboss-serialization) lib/jboss/
#BUILD/jboss-remoting-2.5.1/lib/jbossweb/jbossweb.jar.no
ln -sf $(build-classpath jbossweb/jbossweb) lib/jbossweb/jbossweb.jar
#BUILD/jboss-remoting-2.5.1/lib/jboss/jrunit.jar.no
ln -sf $(build-classpath jboss-jrunit) lib/jboss/
#BUILD/jboss-remoting-2.5.1/lib/junit/lib/junit.jar.no
ln -sf $(build-classpath junit) lib/junit/lib
#BUILD/jboss-remoting-2.5.1/lib/spring/spring-beans.jar.no
ln -sf $(build-classpath spring/beans) lib/spring/spring-beans.jar
#BUILD/jboss-remoting-2.5.1/lib/spring/spring-context.jar.no
ln -sf $(build-classpath spring/context) lib/spring/spring-context.jar
#BUILD/jboss-remoting-2.5.1/lib/spring/caucho/hessian-2.1.12.jar.no
ln -sf $(build-classpath hessian) lib/spring/caucho/hessian-2.1.12.jar
#BUILD/jboss-remoting-2.5.1/lib/spring/spring-webmvc.jar.no
ln -sf $(build-classpath spring/webmvc) lib/spring/spring-webmvc.jar
#BUILD/jboss-remoting-2.5.1/lib/spring/spring-aop.jar.no
ln -sf $(build-classpath spring/aop) lib/spring/spring-aop.jar
#BUILD/jboss-remoting-2.5.1/lib/spring/spring-core.jar.no
ln -sf $(build-classpath spring/core) lib/spring/spring-core.jar
#BUILD/jboss-remoting-2.5.1/lib/spring/spring-web.jar.no
ln -sf $(build-classpath spring/web) lib/spring/spring-web.jar
#BUILD/jboss-remoting-2.5.1/lib/spring/spring-remoting.jar.no
ln -sf $(build-classpath spring/remoting) lib/spring/spring-remoting.jar
#BUILD/jboss-remoting-2.5.1/lib/spring/spring.jar.no
ln -sf $(build-classpath spring) lib/spring/spring.jar
#BUILD/jboss-remoting-2.5.1/lib/spring/aopalliance/aopalliance.jar.no
ln -sf $(build-classpath aopalliance) lib/spring/aopalliance/
#BUILD/jboss-remoting-2.5.1/lib/dom4j/lib/dom4j.jar.no
ln -sf $(build-classpath dom4j) lib/dom4j/lib/
#BUILD/jboss-remoting-2.5.1/lib/apache-commons/lib/commons-logging.jar.no
ln -sf $(build-classpath commons-logging) lib/apache-commons/lib/
#BUILD/jboss-remoting-2.5.1/lib/apache-log4j/lib/log4j.jar.no
ln -sf $(build-classpath log4j) lib/apache-log4j/lib/log4j.jar
#BUILD/jboss-remoting-2.5.1/lib/jgroups/lib/jgroups-all.jar.no
ln -sf $(build-classpath jgroups) lib/jgroups/lib/jgroups-all.jar
#BUILD/jboss-remoting-2.5.1/lib/jrunit-libs/lib/jcommon-1.0.0-rc1.jar.no
ln -sf $(build-classpath jcommon) lib/jrunit-libs/lib/jcommon-1.0.0-rc1.jar
#BUILD/jboss-remoting-2.5.1/lib/jrunit-libs/lib/jfreechart-1.0.0-rc1.jar.no
ln -sf $(build-classpath jfreechart) lib/jrunit-libs/lib/jfreechart-1.0.0-rc1.jar
#BUILD/jboss-remoting-2.5.1/lib/trove/lib/trove.jar.no
ln -sf $(build-classpath gnu-trove) lib/trove/lib/trove.jar

# hack; disabled jdk6 support
sed -i 's,<condition property="isJDK6">,<condition property="isJDK5">,' build.xml

%build
export JAVA_HOME=/usr/lib/jvm/java-1.5.0
export CLASSPATH=$(build-classpath ant/ant-junit)
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jars tests.jars javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 output/lib/jboss-remoting.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 output/lib/jboss-remoting-src.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-src-%{version}.jar
install -m 644 output/lib/jboss-remoting-tests.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tests-%{version}.jar
install -m 644 output/lib/jboss-remoting-loading-tests.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-loading-tests-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr output/lib/servlet-invoker.war $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr output/etc $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.jboss.remoting %{name} %{version} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/jboss-remoting.jar
%endif

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-src-%{version}.jar
%{_javadir}/%{name}-src.jar
%{_javadir}/%{name}-tests-%{version}.jar
%{_javadir}/%{name}-tests.jar
%{_javadir}/%{name}-loading-tests-%{version}.jar
%{_javadir}/%{name}-loading-tests.jar
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/etc
%{_datadir}/%{name}-%{version}/servlet-invoker.war
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt2_4jpp6
- hack: built w/o jdk6 support for jboss/jbossas 4 support

* Sat Jan 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_4jpp6
- converted from JPackage by jppimport script

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2.2-alt1_3.SP8.1jpp5
- new version

* Fri Mar 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2.2-alt0.1jpp
- bootstrap for jbossas

