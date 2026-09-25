Name:           log4j
Version:        2.25.4
Release:        alt1

Summary:        Java logging package
License:        Apache-2.0
Group:          Development/Java
URL:            https://logging.apache.org/%name
VCS:            https://github.com/apache/logging-log4j2

Source0:        %name-%version.tar

Patch0:         0001-Remove-InlineMe-annotations.patch

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.apache.logging:logging-parent:pom:)
BuildRequires:  mvn(biz.aQute.bnd:biz.aQute.bnd.annotation)
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires:  mvn(com.lmax:disruptor)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.jctools:jctools-core)
BuildRequires:  mvn(org.jspecify:jspecify)
BuildRequires:  mvn(org.osgi:osgi.annotation)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)

BuildArch:      noarch

%description
Log4j is a tool to help the programmer output log statements to a
variety of output targets.

%package        slf4j
Group:          Development/Java
Summary:        Binding between LOG4J 2 API and SLF4J

%description    slf4j
Binding between LOG4J 2 API and SLF4J.

%package        jcl
Group:          Development/Java
Summary:        Apache Log4j Commons Logging Bridge

%description    jcl
Apache Log4j Commons Logging Bridge.

%package        web
Group:          Development/Java
Summary:        Apache Log4j Web

%description    web
Support for Log4j in a web servlet container.

%package        bom
Group:          Development/Java
Summary:        Apache Log4j BOM

%description    bom
Apache Log4j Bill of Materials.

%prep
%setup
%autopatch -p1

%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r com.diffplug.spotless:spotless-maven-plugin
%pom_remove_plugin -r org.ops4j.pax.exam:exam-maven-plugin
%pom_remove_plugin org.gradlex:gradle-module-metadata-maven-plugin log4j-parent
%pom_remove_plugin org.codehaus.gmavenplus:gmavenplus-plugin log4j-parent

%pom_remove_plugin :maven-clean-plugin log4j-parent

%pom_remove_plugin org.apache.logging.log4j:log4j-docgen-maven-plugin
%pom_xpath_remove 'pom:path[pom:artifactId="log4j-docgen"]' log4j-parent
%pom_xpath_remove 'pom:processor[text()="org.apache.logging.log4j.docgen.processor.DescriptorGenerator"]' log4j-parent
%pom_xpath_remove 'pom:compilerArgs/pom:arg[starts-with(text(), "-Alog4j.docgen.")]' log4j-parent
%pom_xpath_remove 'pom:execution[pom:id="define-log4jDocgenDescriptorFilepath"]' log4j-parent

%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-resources-plugin"]/pom:dependencies'
rm -rf docs/api

%pom_remove_dep -r com.fasterxml.jackson:jackson-bom
%pom_remove_dep -r jakarta.platform:jakarta.jakartaee-bom
%pom_remove_dep -r org.junit:junit-bom
%pom_remove_dep -r org.springframework:spring-framework-bom
%pom_remove_dep org.apache.groovy:groovy-bom log4j-parent
%pom_remove_dep org.mockito:mockito-bom log4j-parent

%pom_change_dep -r org.osgi:org.osgi.core org.osgi:osgi.core
%pom_change_dep -r org.osgi:org.osgi.annotation.bundle org.osgi:osgi.annotation
%pom_remove_dep -r org.osgi:org.osgi.annotation.versioning

# with patch0
%pom_remove_dep com.google.errorprone:error_prone_annotations log4j-parent

%pom_xpath_set 'pom:properties/pom:bnd-jpms-module-info' \
    '$[bnd-module-name];access=0;modules="biz.aQute.bnd.annotation,osgi.annotation"' \
    log4j-parent

rm log4j-core/src/main/java/org/apache/logging/log4j/core/async/DisruptorBlockingQueueFactory.java
%pom_remove_dep -r com.conversantmedia:disruptor
%pom_remove_dep -r :kafka-clients
%pom_remove_dep -r javax.jms:javax.jms-api

%pom_disable_module %name-api-test
%pom_disable_module %name-core-test
%pom_disable_module %name-layout-template-json-test
%pom_disable_module %name-fuzz-test
%pom_disable_module %name-core-fuzz-test
%pom_disable_module %name-layout-template-json-fuzz-test
%pom_disable_module %name-slf4j2-impl-fuzz-test
%pom_disable_module %name-osgi-test
%pom_disable_module %name-perf-test
%pom_disable_module %name-core-its
%pom_disable_module %name-slf4j2-impl
%pom_disable_module %name-taglib
%pom_disable_module %name-jakarta-web
%pom_disable_module %name-jakarta-jms
%pom_disable_module %name-jakarta-smtp
%pom_disable_module %name-iostreams
%pom_disable_module %name-jul
%pom_disable_module %name-jpa
%pom_disable_module %name-jdbc-dbcp2
%pom_disable_module %name-couchdb
%pom_disable_module %name-cassandra
%pom_disable_module %name-mongodb
%pom_disable_module %name-mongodb4
%pom_disable_module %name-appserver
%pom_disable_module %name-spring-boot
%pom_disable_module %name-spring-cloud-config-client
%pom_disable_module %name-docker
%pom_disable_module %name-layout-template-json

%pom_remove_dep -r :jackson-core
%pom_remove_dep -r :jackson-databind
%pom_remove_dep -r :jackson-dataformat-yaml
%pom_remove_dep -r :jackson-dataformat-xml
%pom_remove_dep :jackson-annotations log4j-core-java9
%pom_remove_dep org.codehaus.woodstox:stax2-api log4j-core
%pom_remove_dep -r :jeromq
%pom_remove_dep -r :commons-csv

rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/{jackson,config/yaml,config/json,parser}
rm -r log4j-core/src/main/java/org/apache/logging/log4j/core/appender/{db,mom,nosql}
rm log4j-core/src/main/java/org/apache/logging/log4j/core/layout/*{Csv,Jackson,Xml,Yaml,Json,Gelf}*.java
rm -r log4j-core-java9/src/main/java/org/apache/logging/log4j/core/jackson
rm log4j-1.2-api/src/main/java/org/apache/log4j/builders/layout/*Xml*.java
rm -r log4j-1.2-api/src/main/java/org/apache/log4j/or/jms

%pom_remove_dep com.sun.mail:javax.mail log4j-core
%pom_remove_dep javax.mail:javax.mail-api log4j-core
%pom_remove_dep javax.activation:javax.activation-api log4j-core
rm log4j-core/src/main/java/org/apache/logging/log4j/core/net/MimeMessageBuilder.java
rm log4j-core/src/main/java/org/apache/logging/log4j/core/net/SmtpManager.java
rm log4j-core/src/main/java/org/apache/logging/log4j/core/appender/SmtpAppender.java
rm log4j-core/src/main/java/org/apache/logging/log4j/core/filter/MutableThreadContextMapFilter.java

%pom_xpath_remove -r 'pom:dependencies/pom:dependency[pom:scope="test"]'

%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin . '
<configuration>
  <annotationProcessorPaths combine.self="override"/>
  <compilerArgs combine.self="override">
    <arg>-Xlint:all</arg>
  </compilerArgs>
</configuration>'

%mvn_alias :%name-1.2-api %name:%name
%mvn_file ':{%name-1.2-api}' %name/@1 %name
%mvn_package :%name-slf4j-impl slf4j
%mvn_package :%name-to-slf4j slf4j
%mvn_package :%name-jcl jcl
%mvn_package :%name-web web
%mvn_package :%name-bom bom
%mvn_package ::zip: __noinstall

%build
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files slf4j -f .mfiles-slf4j
%files jcl -f .mfiles-jcl
%files web -f .mfiles-web
%files bom -f .mfiles-bom

%changelog
* Thu Sep 24 2026 Evgeniy Serov <scala@altlinux.org> 2.25.4-alt1
- Updated to 2.25.4.
- Disabled javadoc.

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

