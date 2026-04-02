Name:           log4j
Version:        2.20.0
Release:        alt1.1

Summary:        Java logging package
License:        Apache-2.0
Group:          Development/Java
URL:            https://logging.apache.org/%name
VCS:            https://github.com/apache/logging-log4j2

Source0:        %name-%version.tar

Patch0:         logging-log4j-Remove-unsupported-EventDataConverter.patch
Patch1:         0002-Remove-usage-of-toolchains.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(com.lmax:disruptor)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(jakarta.mail:jakarta.mail-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.jctools:jctools-core)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)

BuildArch:      noarch

%description
Log4j is a tool to help the programmer output log statements to a
variety of output targets.

%javadoc_package

%package slf4j
Group:          Development/Java
Summary:        Binding between LOG4J 2 API and SLF4J

%description slf4j
Binding between LOG4J 2 API and SLF4J.

%package jcl
Group:          Development/Java
Summary:        Apache Log4j Commons Logging Bridge

%description jcl
Apache Log4j Commons Logging Bridge.

%package web
Group:          Development/Java
Summary:        Apache Log4j Web
 
%description web
Support for Log4j in a web servlet container.

%package bom
Group:          Development/Java
Summary:        Apache Log4j BOM
 
%description bom
Apache Log4j 2 Bill of Material

%prep
%setup
%autopatch -p1

%pom_remove_parent
%pom_remove_parent log4j-bom

%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-toolchains-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r com.diffplug.spotless:spotless-maven-plugin
%pom_remove_plugin -r org.apache.logging.log4j:log4j-changelog-maven-plugin
%pom_remove_plugin -r org.codehaus.mojo:xml-maven-plugin
 
find -name '*.jar' -o -name '*.class' -delete
rm -rf docs/api
 
%pom_disable_module %name-distribution
%pom_disable_module %name-samples
%pom_disable_module %name-flume-ng
%pom_disable_module %name-perf
 
%pom_remove_dep -r org.codehaus.groovy:groovy-bom
%pom_remove_dep -r com.fasterxml.jackson:jackson-bom
%pom_remove_dep -r jakarta.platform:jakarta.jakartaee-bom
%pom_remove_dep -r org.eclipse.jetty:jetty-bom
%pom_remove_dep -r org.junit:junit-bom
%pom_remove_dep -r io.fabric8:kubernetes-client-bom
%pom_remove_dep -r io.netty:netty-bom
%pom_remove_dep -r org.springframework:spring-framework-bom
 
rm log4j-core/src/main/java/org/apache/logging/log4j/core/async/DisruptorBlockingQueueFactory.java
%pom_remove_dep -r com.conversantmedia:disruptor
 
rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/appender/mom/kafka
%pom_remove_dep -r :kafka-clients
 
%pom_remove_dep -r javax.jms:javax.jms-api
 
%pom_disable_module %name-jdbc-dbcp2
 
%pom_disable_module %name-mongodb3
%pom_disable_module %name-mongodb4
 
%pom_remove_dep :jconsole %name-jmx-gui
%pom_add_dep sun.jdk:jconsole %name-jmx-gui
 
%pom_change_dep -r org.osgi:org.osgi.core org.osgi:osgi.core
 
%pom_remove_plugin :maven-failsafe-plugin
 
%pom_remove_dep -r :slf4j-ext
 
# Make compiled code compatible with OpenJDK 8
%pom_xpath_inject 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration' "<release>8</release>"
 
%pom_disable_module %name-api-test
%pom_disable_module %name-core-test
%pom_disable_module %name-layout-template-json-test
%pom_disable_module %name-slf4j2-impl
%pom_disable_module %name-taglib
%pom_disable_module %name-jmx-gui
%pom_disable_module %name-jakarta-web
%pom_disable_module %name-iostreams
%pom_disable_module %name-jul
%pom_disable_module %name-core-its
%pom_disable_module %name-jpa
%pom_disable_module %name-couchdb
%pom_disable_module %name-cassandra
%pom_disable_module %name-appserver
%pom_disable_module %name-spring-cloud-config
%pom_disable_module %name-spring-boot
%pom_disable_module %name-docker
%pom_disable_module %name-kubernetes
%pom_disable_module %name-layout-template-json
 
%pom_remove_dep -r :jackson-core
%pom_remove_dep -r :jackson-databind
%pom_remove_dep -r :jackson-dataformat-yaml
%pom_remove_dep -r :jackson-dataformat-xml
%pom_remove_dep -r :woodstox-core
%pom_remove_dep -r :jeromq
%pom_remove_dep -r :commons-csv
 
rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/{jackson,config/yaml,config/json,parser}
rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/appender/{db,mom,nosql}
rm log4j-core/src/main/java/org/apache/logging/log4j/core/layout/*{Csv,Jackson,Xml,Yaml,Json,Gelf}*.java
rm log4j-1.2-api/src/main/java/org/apache/log4j/builders/layout/*Xml*.java
rm log4j-api/src/main/java/org/apache/logging/log4j/util/Activator.java
rm -r log4j-1.2-api/src/main/java/org/apache/log4j/or/jms

%mvn_alias :%name-1.2-api %name:%name
%mvn_file ':{%name-1.2-api}' %name/@1 %name
 
%mvn_package :%name-slf4j-impl slf4j
%mvn_package :%name-to-slf4j slf4j
%mvn_package :%name-taglib taglib
%mvn_package :%name-jcl jcl
%mvn_package :%name-jmx-gui jmx-gui
%mvn_package :%name-web web
%mvn_package :%name-bom bom
%mvn_package :%name-cassandra nosql
%mvn_package :%name-couchdb nosql
 
%mvn_package :log4j-core-its __noinstall
 
%mvn_package ::zip: __noinstall
 
%pom_remove_dep com.sun.mail:javax.mail log4j-core
%pom_remove_dep javax.mail:javax.mail-api log4j-core
%pom_remove_dep javax.activation:javax.activation-api log4j-core
rm log4j-core/src/main/java/org/apache/logging/log4j/core/net/MimeMessageBuilder.java
rm log4j-core/src/main/java/org/apache/logging/log4j/core/net/SmtpManager.java
rm log4j-core/src/main/java/org/apache/logging/log4j/core/appender/SmtpAppender.java
rm log4j-core/src/main/java/org/apache/logging/log4j/core/filter/MutableThreadContextMapFilter.java
 
%pom_remove_dep org.eclipse.angus:angus-activation log4j-jakarta-smtp
%pom_remove_dep org.eclipse.angus:jakarta.mail log4j-jakarta-smtp
 
%pom_remove_plugin -r org.apache.maven.plugins:maven-failsafe-plugin
%pom_remove_plugin -r org.ops4j.pax.exam:exam-maven-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files slf4j -f .mfiles-slf4j
%files jcl -f .mfiles-jcl
%files web -f .mfiles-web
%files bom -f .mfiles-bom

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 2.20.0-alt1.1
- Cosmetic fixes.

* Thu Jan 29 2026 Evgeniy Serov <scala@altlinux.org> 2.20.0-alt1
- Updated to 2.20.0.

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

