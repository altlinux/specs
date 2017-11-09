Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.2.7
%global namedreltag .RELEASE
%global namedversion %{version}%{?namedreltag}
%global oname spring-batch

%if 0%{?fedora}
# Unavailable deps
# https://bugzilla.redhat.com/show_bug.cgi?id=1240475
%bcond_with vpp
%endif

Name:          springframework-batch
Version:       2.2.7
Release:       alt1_5jpp8
Summary:       Tools for enterprise batch or bulk processing
License:       ASL 2.0
URL:           http://www.springsource.org/spring-batch
# lastest release require springframework >= 4
Source0:       https://github.com/spring-projects/spring-batch/archive/%{namedversion}.tar.gz
Patch0:        %{name}-2.2.7-spring-retry1.1.0.patch

BuildRequires: maven-local
BuildRequires: mvn(cglib:cglib)
BuildRequires: mvn(com.h2database:h2)
BuildRequires: mvn(com.thoughtworks.xstream:xstream)
BuildRequires: mvn(commons-collections:commons-collections)
BuildRequires: mvn(commons-dbcp:commons-dbcp)
BuildRequires: mvn(commons-io:commons-io)
%if %{with vpp}
# antrun-plugin deps
BuildRequires: mvn(foundrylogic.vpp:vpp)
%endif
BuildRequires: mvn(javax.mail:mail)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(net.java.dev.jets3t:jets3t)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-apache-regexp)
BuildRequires: mvn(org.apache.derby:derby)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.felix:org.osgi.core)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jta_1.1_spec)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.aspectj:aspectjweaver)
BuildRequires: mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires: mvn(org.codehaus.jettison:jettison)
BuildRequires: mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires: mvn(org.eclipse.gemini.blueprint:gemini-blueprint-core)
BuildRequires: mvn(org.hibernate:hibernate-core)
BuildRequires: mvn(org.hibernate:hibernate-entitymanager)
BuildRequires: mvn(org.hibernate:hibernate-validator)
BuildRequires: mvn(org.hsqldb:hsqldb)
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
BuildRequires: mvn(org.springframework:spring-aop)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-context-support)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.springframework:spring-jdbc)
BuildRequires: mvn(org.springframework:spring-jms)
BuildRequires: mvn(org.springframework:spring-orm)
BuildRequires: mvn(org.springframework:spring-oxm)
BuildRequires: mvn(org.springframework:spring-test)
BuildRequires: mvn(org.springframework:spring-tx)
BuildRequires: mvn(org.springframework.amqp:spring-amqp)
BuildRequires: mvn(org.springframework.amqp:spring-rabbit)
BuildRequires: mvn(org.springframework.data:spring-data-commons)
BuildRequires: mvn(org.springframework.data:spring-data-mongodb)
BuildRequires: mvn(org.springframework.data:spring-data-redis)
BuildRequires: mvn(org.springframework.retry:spring-retry)

BuildArch:     noarch
Source44: import.info

%description
Spring Batch provides tools for enterprise batch or bulk processing. It
can be used to wire up jobs, and track their execution, or simply as an
optimization for repetitive processing in a transactional environment.
Spring Batch is part of the Spring Portfolio.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{namedversion}
%patch0 -p1

sed -i 's/\r//' src/assembly/*.txt
cp -p src/assembly/license.txt .
cp -p src/assembly/notice.txt .

%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin com.agilejava.docbkx:docbkx-maven-plugin
%pom_remove_plugin org.codehaus.mojo:jdepend-maven-plugin
%pom_remove_plugin -r :com.springsource.bundlor.maven
# require com.springsource.bundlor:com.springsource.bundlor.maven
%pom_remove_plugin org.eclipse.m2e:lifecycle-mapping spring-batch-parent
# org.springframework.build.aws org.springframework.build.aws.maven
%pom_xpath_remove -r pom:build/pom:extensions

sed -i 's|${pom.version}|${project.version}|' pom.xml spring-batch-parent/pom.xml spring-batch-core/pom.xml

# antrun-plugin deps
%pom_remove_dep org.springframework.build:
%pom_remove_dep :ant-trax spring-batch-parent
# hibernate-annotations apis are available in hibernate-core
%pom_remove_dep -r :hibernate-annotations

# Fix cglib aId
%pom_xpath_set -r "pom:dependency[pom:groupId = 'cglib']/pom:artifactId" cglib

# Fix org.osgi.core gId aId
%pom_change_dep -r :osgi_R4_core org.apache.felix:org.osgi.core

%pom_xpath_set "pom:dependency[pom:groupId = 'org.aspectj']/pom:artifactId" aspectjweaver  spring-batch-test
%pom_remove_dep -r :aspectjrt

%pom_xpath_set "pom:dependency[pom:groupId = 'log4j']/pom:version" 1.2.17 spring-batch-parent

# Use newer org.springframework.osgi
%pom_change_dep -r :spring-osgi-core org.eclipse.gemini.blueprint:gemini-blueprint-core:1.0.2.RELEASE
sed -i "s|org.springframework.osgi|org.eclipse.gemini.blueprint|" spring-batch-core/src/main/java/org/springframework/batch/core/configuration/support/OsgiBundleXmlApplicationContextFactory.java
  
# Unavailable deps.
# require: 2.3.4.726 < ibatis-sqlmap > 2.3.0
%pom_remove_dep org.apache.ibatis:ibatis-sqlmap spring-batch-infrastructure
rm -r spring-batch-infrastructure/src/main/java/org/springframework/batch/item/database/Ibatis*.java \
  spring-batch-infrastructure/src/test/java/org/springframework/batch/item/database/Ibatis*.java

# AGPLv3
%pom_remove_dep org.springframework.data:spring-data-neo4j spring-batch-infrastructure
rm -r spring-batch-infrastructure/src/main/java/org/springframework/batch/item/data/Neo4jItemReader.java \
 spring-batch-infrastructure/src/main/java/org/springframework/batch/item/data/Neo4jItemWriter.java \
 spring-batch-infrastructure/src/test/java/org/springframework/batch/item/data/Neo4jItemReaderTests.java \
 spring-batch-infrastructure/src/test/java/org/springframework/batch/item/data/Neo4jItemWriterTests.java

# NON free
%pom_remove_dep org.springframework.data:spring-data-gemfire spring-batch-infrastructure
rm -r spring-batch-infrastructure/src/main/java/org/springframework/batch/item/data/GemfireItemWriter.java \
 spring-batch-infrastructure/src/main/java/org/springframework/batch/item/data/SpELMappingGemfireItemWriter.java \
 spring-batch-infrastructure/src/test/java/org/springframework/batch/item/data/GemfireItemWriterTests.java

# require foundrylogic.vpp vpp 2.2.1 for generate sql resources
%if %{with vpp}
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-antrun-plugin']" \
"<dependencies>
  <dependency>
    <groupId>foundrylogic.vpp</groupId>
    <artifactId>vpp</artifactId>
    <version>2.2.1</version>
  </dependency>
</dependencies>" spring-batch-core
# regenerate resources.
rm -r spring-batch-core/src/main/resources/org/springframework/batch/core/*.sql
# Fix resources location
sed -i 's|${basedir}/target/generated-resources|${basedir}/target/generated-resources/org/springframework/batch/core|' spring-batch-core/pom.xml
%pom_xpath_inject "pom:project/pom:build" '
<resources>
  <resource>
    <directory>${basedir}/src/main/resources</directory>
    <includes>
      <include>**/*</include>
    </includes>
  </resource>
  <resource>
    <directory>${basedir}/target/generated-resources</directory>
    <includes>
      <include>**/*</include>
    </includes>
  </resource>
</resources>' spring-batch-core
%else
%pom_remove_plugin org.apache.maven.plugins:maven-antrun-plugin spring-batch-core
%pom_remove_plugin org.apache.maven.plugins:maven-antrun-plugin spring-batch-parent
%endif

%pom_xpath_inject pom:properties '
  <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>' spring-batch-parent

# add OSGi support and FIX Bundle-SymbolicName
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 spring-batch-infrastructure '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>org.springframework.batch.infrastructure</Bundle-SymbolicName>
    <Bundle-Name>Spring Batch Infrastructure</Bundle-Name>
    <Bundle-Vendor>Spring</Bundle-Vendor>
    <Bundle-Version>${project.version}</Bundle-Version>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 spring-batch-core '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>org.springframework.batch.core</Bundle-SymbolicName>
    <Bundle-Name>Spring Batch Core</Bundle-Name>
    <Bundle-Vendor>Spring</Bundle-Vendor>
    <Bundle-Version>${project.version}</Bundle-Version>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 spring-batch-test '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>org.springframework.batch.test</Bundle-SymbolicName>
    <Bundle-Name>Spring Batch Test</Bundle-Name>
    <Bundle-Vendor>Spring</Bundle-Vendor>
    <Bundle-Version>${project.version}</Bundle-Version>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

%build
# Test disabled, because:
# due to the incompatibility of jettison 1.2+ with xstream
# com.thoughtworks.xstream.converters.ConversionException: Cannot construct java.util.Map$Entry as it does not have a no-args constructor : Cannot construct java.util.Map$Entry as it does not have a no-args constructor
# ---- Debugging information ----
# message             : Cannot construct java.util.Map$Entry as it does not have a no-args constructor
# cause-exception     : com.thoughtworks.xstream.converters.reflection.ObjectAccessException
# cause-message       : Cannot construct java.util.Map$Entry as it does not have a no-args constructor
# class               : java.util.HashMap
# required-type       : java.util.Map$Entry
# path                : /map/map/entry
# line number         : -1
# -------------------------------
# unavailable test deps: package org.springframework.orm.hibernate4 does not exist
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc license.txt notice.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt1_3jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.7-alt1_2jpp8
- java 8 mass update

