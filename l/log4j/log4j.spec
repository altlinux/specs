Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without  jp_minimal

Name:           log4j
Version:        2.17.2
Release:        alt1_3jpp11
Summary:        Java logging package
BuildArch:      noarch
License:        ASL 2.0

URL:            https://logging.apache.org/%{name}
Source0:        https://www.apache.org/dist/logging/%{name}/%{version}/apache-%{name}-%{version}-src.tar.gz
Source1:        https://www.apache.org/dist/logging/%{name}/%{version}/apache-%{name}-%{version}-src.tar.gz.asc
Source2:        https://www.apache.org/dist/logging/KEYS

Patch2:         logging-log4j-Remove-unsupported-EventDataConverter.patch

BuildRequires:  gnupg2

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.lmax:disruptor)
BuildRequires:  mvn(com.sun.activation:jakarta.activation)
BuildRequires:  mvn(com.sun.mail:javax.mail)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.jctools:jctools-core)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(jakarta.servlet:jakarta.servlet-api)

%if %{without jp_minimal}
BuildRequires:  mvn(com.datastax.cassandra:cassandra-driver-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires:  mvn(com.fasterxml.woodstox:woodstox-core)
BuildRequires:  mvn(com.lmax:disruptor)
BuildRequires:  mvn(com.sun.mail:javax.mail)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(javax.servlet.jsp:jsp-api)
BuildRequires:  mvn(org.apache.commons:commons-csv)
BuildRequires:  mvn(org.apache.logging:logging-parent:pom:)
BuildRequires:  mvn(org.apache.tomcat:tomcat-catalina)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty:jetty-util)
BuildRequires:  mvn(org.eclipse.persistence:javax.persistence)
BuildRequires:  mvn(org.fusesource.jansi:jansi:1)
BuildRequires:  mvn(org.jboss.spec.javax.jms:jboss-jms-api_1.1_spec)
BuildRequires:  mvn(org.jctools:jctools-core)
BuildRequires:  mvn(org.lightcouch:lightcouch)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-ext)
BuildRequires:  mvn(org.zeromq:jeromq)
BuildRequires:  mvn(sun.jdk:jconsole)
# Explicit requires for javapackages-tools since log4j-jmx script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools

# Also needs:
# - Various Spring dependencies
# - javax.jms
# - io.fabric8.kubernetes-client
%endif
Source44: import.info

%description
Log4j is a tool to help the programmer output log statements to a
variety of output targets.

%package slf4j
Group: Development/Java
Summary:        Binding between LOG4J 2 API and SLF4J

%description slf4j
Binding between LOG4J 2 API and SLF4J.

%package jcl
Group: Development/Java
Summary:        Apache Log4j Commons Logging Bridge

%description jcl
Apache Log4j Commons Logging Bridge.

%if %{without jp_minimal}
%package osgi
Group: Development/Java
Summary:        Apache Log4J Core OSGi Bundles

%description osgi
Apache Log4J Core OSGi Bundles.

%package taglib
Group: Development/Java
Summary:        Apache Log4j Tag Library

%description taglib
Apache Log4j Tag Library for Web Applications.

%package jmx-gui
Group: Development/Java
Summary:        Apache Log4j JMX GUI

%description jmx-gui
Swing-based client for remotely editing the log4j configuration and remotely
monitoring StatusLogger output. Includes a JConsole plug-in.

%package web
Group: Development/Java
Summary:        Apache Log4j Web

%description web
Support for Log4j in a web servlet container.

%package bom
Group: Development/Java
Summary:        Apache Log4j BOM

%description bom
Apache Log4j 2 Bill of Material


%package nosql
Group: Development/Java
Summary:        Apache Log4j NoSql

%description nosql
Use NoSQL databases such as MongoDB and CouchDB to append log messages.

%endif

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}

%description    javadoc
%{summary}.

%prep
%setup -q -n apache-%{name}-%{version}-src
%patch2 -p1


%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-remote-resources-plugin
%pom_remove_plugin -r :maven-doap-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-toolchains-plugin
%pom_remove_plugin -r :revapi-maven-plugin

# remove all the stuff we'll build ourselves
find -name "*.jar" -o -name "*.class" -delete
rm -rf docs/api

%pom_disable_module %{name}-distribution
%pom_disable_module %{name}-samples

# Apache Flume is not in Fedora yet
%pom_disable_module %{name}-flume-ng

# artifact for upstream testing of log4j itself, shouldn't be distributed
%pom_disable_module %{name}-perf

# add dependency for javax.activation package (no longer part of OpenJDK)
%pom_add_dep com.sun.activation:jakarta.activation

# unavailable com.conversantmedia:disruptor
rm log4j-core/src/main/java/org/apache/logging/log4j/core/async/DisruptorBlockingQueueFactory.java
%pom_remove_dep -r com.conversantmedia:disruptor

# kafka not available
rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/appender/mom/kafka
%pom_remove_dep -r :kafka-clients

# not compatible with fedora's version
%pom_disable_module %{name}-liquibase

# we don't have slf4j 1.8 yet
%pom_disable_module %{name}-slf4j18-impl

# we don't have commons-dbcp2
%pom_disable_module %{name}-jdbc-dbcp2

# We don't have mmongo-java
%pom_disable_module %{name}-mongodb3
%pom_disable_module %{name}-mongodb4

# System scoped dep provided by JDK
%pom_remove_dep :jconsole %{name}-jmx-gui
%pom_add_dep sun.jdk:jconsole %{name}-jmx-gui

# old AID is provided by felix, we want osgi-core
%pom_change_dep -r org.osgi:org.osgi.core org.osgi:osgi.core

# BOM package shouldn't require Apache RAT
%pom_remove_plugin :apache-rat-plugin %{name}-bom

# tests are disabled
%pom_remove_plugin :maven-failsafe-plugin

# Remove deps on slf4j-ext, it is no longer available in Fedora 35
%pom_remove_dep -r :slf4j-ext
%pom_remove_parent

# Make compiled code compatible with OpenJDK 8
%pom_xpath_inject 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration' "<release>8</release>"

%if %{with jp_minimal}
%pom_disable_module %{name}-taglib
%pom_disable_module %{name}-jmx-gui
%pom_disable_module %{name}-bom
%pom_disable_module %{name}-web
%pom_disable_module %{name}-iostreams
%pom_disable_module %{name}-jul
%pom_disable_module %{name}-core-its
%pom_disable_module %{name}-jpa
%pom_disable_module %{name}-couchdb
%pom_disable_module %{name}-cassandra
%pom_disable_module %{name}-appserver
%pom_disable_module %{name}-spring-cloud-config
%pom_disable_module %{name}-spring-boot
%pom_disable_module %{name}-kubernetes
%pom_disable_module %{name}-layout-template-json

%pom_remove_dep -r :jackson-dataformat-yaml
%pom_remove_dep -r :jackson-dataformat-xml
%pom_remove_dep -r :woodstox-core
%pom_remove_dep -r :javax.persistence
%pom_remove_dep -r :jboss-jms-api_1.1_spec
%pom_remove_dep -r :jeromq
%pom_remove_dep -r :commons-csv

rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/{jackson,config/yaml,parser}
rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/appender/{db,mom,nosql}
rm log4j-core/src/main/java/org/apache/logging/log4j/core/layout/*{Csv,Jackson,Xml,Yaml,Json,Gelf}*.java
rm log4j-1.2-api/src/main/java/org/apache/log4j/builders/layout/*Xml*.java
rm log4j-api/src/main/java/org/apache/logging/log4j/util/Activator.java
rm -r log4j-1.2-api/src/main/java/org/apache/log4j/or/jms
%endif

%mvn_alias :%{name}-1.2-api %{name}:%{name}

# Note that packages using the compatibility layer still need to have log4j-core
# on the classpath to run. This is there to prevent build-classpath from putting
# whole dir on the classpath which results in loading incorrect provider
%mvn_file ':{%{name}-1.2-api}' %{name}/@1 %{name}

%mvn_package ':%{name}-slf4j-impl' slf4j
%mvn_package ':%{name}-to-slf4j' slf4j
%mvn_package ':%{name}-taglib' taglib
%mvn_package ':%{name}-jcl' jcl
%mvn_package ':%{name}-jmx-gui' jmx-gui
%mvn_package ':%{name}-web' web
%mvn_package ':%{name}-bom' bom
%mvn_package ':%{name}-cassandra' nosql
%mvn_package ':%{name}-couchdb' nosql

%mvn_package :log4j-core-its __noinstall

%build
# missing test deps (mockejb)
%mvn_build -f -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%if %{without jp_minimal}
%jpackage_script org.apache.logging.log4j.jmx.gui.ClientGUI '' '' %{name}/%{name}-jmx-gui:%{name}/%{name}-core %{name}-jmx false
%endif

mkdir -p $RPM_BUILD_ROOT`dirname /etc/chainsaw.conf`
touch $RPM_BUILD_ROOT/etc/chainsaw.conf

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE.txt NOTICE.txt
%config(noreplace,missingok) /etc/chainsaw.conf

%files slf4j -f .mfiles-slf4j
%files jcl -f .mfiles-jcl
%if %{without jp_minimal}
%files taglib -f .mfiles-taglib
%files web -f .mfiles-web
%files bom -f .mfiles-bom
%files nosql -f .mfiles-nosql
%files jmx-gui -f .mfiles-jmx-gui
%{_bindir}/%{name}-jmx
%endif

#%%files javadoc -f .mfiles-javadoc
#%%doc LICENSE.txt NOTICE.txt


%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:2.17.2-alt1_3jpp11
- update

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:2.17.2-alt1_1jpp11
- new version

* Sun Dec 19 2021 Andrey Cherepanov <cas@altlinux.org> 0:2.17.0-alt1_1jpp11
- new version (fixes CVE-2021-45105)

* Wed Dec 15 2021 Andrey Cherepanov <cas@altlinux.org> 0:2.16.0-alt1_1jpp11
- new version
- security fix for CVE-2021-45046

* Mon Dec 13 2021 Andrey Cherepanov <cas@altlinux.org> 0:2.15.0-alt1_1jpp11
- new version
- security fix for CVE-2021-44228
- fix License tag according to SPDX

* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 0:2.14.1-alt1_1jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:2.13.3-alt1_3jpp11
- fc34 update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:2.13.3-alt1_1jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 0:2.13.0-alt1_3jpp8
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.11.1-alt1_5jpp8
- update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.11.1-alt1_3jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt1_4jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt1_2jpp8
- new version

* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.8.2-alt1_2jpp8
- new version

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt1_4jpp8
- new version

* Thu Sep 28 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_5jpp8
- CVE-2017-5645

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_4jpp8
- new fc release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_2jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_2jpp8
- unbootsrap build

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.17-alt4_14jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.17-alt4_10jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.17-alt4_3jpp7
- rebuild with maven-local

* Tue Jul 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.17-alt3_3jpp7
- osgi fix

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2.17-alt2_3jpp7
- applied repocop patches

* Sun Sep 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.17-alt1_3jpp7
- fc release

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.15-alt2_7jpp6
- fixed repolib

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.15-alt1_7jpp6
- new version

* Sun Mar 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.14-alt8_15jpp5
- fixed missing org.apache.log4j.jmx

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.14-alt7_15jpp5
- new version

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.14-alt7_4jpp5
- fixed missing org.apache.log4j.jmx

* Mon Nov 17 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.14-alt6_4jpp5
- removed obsolete update_menus

