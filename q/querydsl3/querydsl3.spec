BuildRequires: apache-parent
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 26
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 3.7.2
%global _version %( echo %{version} | tr . _ )

%if 0%{?fedora}
# lucene:4.2.1
#def_with lucene4
%bcond_with lucene4
# https://bugzilla.redhat.com/show_bug.cgi?id=1213455
#def_with postgis
%bcond_with postgis
%endif

Name:          querydsl3
Version:       3.7.2
Release:       alt2_6jpp8
Summary:       Type safe queries for Java
License:       ASL 2.0
URL:           http://www.querydsl.com
Source0:       https://github.com/querydsl/querydsl/archive/QUERYDSL_%{_version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(cglib:cglib)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.infradna.tool:bridge-method-annotation)
BuildRequires: mvn(com.infradna.tool:bridge-method-injector)
BuildRequires: mvn(com.mysema.codegen:codegen)
BuildRequires: mvn(com.mysema.commons:mysema-commons-lang)
BuildRequires: mvn(com.thoughtworks.proxytoys:proxytoys)
BuildRequires: mvn(com.vividsolutions:jts)
BuildRequires: mvn(jakarta-regexp:jakarta-regexp)
BuildRequires: mvn(javassist:javassist)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(javax.jdo:jdo-api)
BuildRequires: mvn(javax.jdo:jdo2-api)
BuildRequires: mvn(javax.validation:validation-api)
BuildRequires: mvn(joda-time:joda-time)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
# lucene3 :3.6.2
BuildRequires: mvn(org.apache.lucene:lucene-core:3)
BuildRequires: mvn(org.apache.lucene:lucene-queries:3)
%if %{with lucene4}
BuildRequires: mvn(org.apache.lucene:lucene-analyzers-common:4.2.1)
BuildRequires: mvn(org.apache.lucene:lucene-core:4.2.1)
BuildRequires: mvn(org.apache.lucene:lucene-queries:4.2.1)
BuildRequires: mvn(org.apache.lucene:lucene-queryparser:4.2.1)
%endif
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.eclipse.persistence:eclipselink)
BuildRequires: mvn(org.geolatte:geolatte-geom)
BuildRequires: mvn(org.hamcrest:hamcrest-core)
BuildRequires: mvn(org.hibernate:hibernate-core:4)
BuildRequires: mvn(org.hibernate:hibernate-entitymanager:4)
BuildRequires: mvn(org.hibernate:hibernate-search-orm)
BuildRequires: mvn(org.hibernate:hibernate-validator)
BuildRequires: mvn(org.hibernate.javax.persistence:hibernate-jpa-2.0-api)
BuildRequires: mvn(org.hibernate.javax.persistence:hibernate-jpa-2.1-api)
BuildRequires: mvn(org.jenkins-ci:annotation-indexer)
BuildRequires: mvn(org.mongodb:mongo-java-driver:2)
BuildRequires: mvn(org.mongodb.morphia:morphia)
%if %{with postgis}
BuildRequires: mvn(org.postgis:postgis-jdbc)
%endif
BuildRequires: mvn(org.reflections:reflections)
BuildRequires: mvn(org.scala-lang:scala-library)
BuildRequires: mvn(org.scala-lang:scala-compiler)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(org.sonatype.plexus:plexus-build-api)
BuildRequires: mvn(org.springframework:spring-jdbc)

# Test deps
%if 0
BuildRequires: mvn(com.h2database:h2)
# https://bugzilla.redhat.com/show_bug.cgi?id=1217563
BuildRequires: mvn(com.jolbox:bonecp:0.7.1.RELEASE)
BuildRequires: mvn(com.mysema.maven:apt-maven-plugin)
BuildRequires: mvn(com.oracle:ojdbc6)
BuildRequires: mvn(cubrid:cubrid-jdbc:9.3.1.0005)
BuildRequires: mvn(jdepend:jdepend)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(mysql:mysql-connector-java)
BuildRequires: mvn(net.sourceforge.jtds:jtds)
BuildRequires: mvn(org.apache.derby:derby)
# https://gil.fedorapeople.org/batoo-jpa-2.0.1.2-1.fc20.src.rpm
BuildRequires: mvn(org.batoo.jpa:batoo-jpa)
BuildRequires: mvn(org.datanucleus:datanucleus-api-jdo)
BuildRequires: mvn(org.datanucleus:datanucleus-core)
BuildRequires: mvn(org.datanucleus:datanucleus-maven-plugin)
BuildRequires: mvn(org.datanucleus:datanucleus-rdbms)
BuildRequires: mvn(org.easymock:easymock)
BuildRequires: mvn(org.eclipse.jdt.core.compiler:ecj)
# https://gil.fedorapeople.org/jaybird-2.2.7-1.fc20.src.rpm
BuildRequires: mvn(org.firebirdsql.jdbc:jaybird-jdk16)
BuildRequires: mvn(org.hibernate:hibernate-annotations)
BuildRequires: mvn(org.hibernate:hibernate-envers)
BuildRequires: mvn(org.hsqldb:hsqldb)
# https://gil.fedorapeople.org/joda-money-0.10.0-1.fc20.src.rpm
BuildRequires: mvn(org.joda:joda-money)
# https://gil.fedorapeople.org/geodb-0.8-1.fc20.src.rpm
BuildRequires: mvn(org.opengeo:geodb)
# https://bugzilla.redhat.com/show_bug.cgi?id=1217395
BuildRequires: mvn(org.postgresql:postgresql:9.3-1101-jdbc41)
BuildRequires: mvn(org.xerial:sqlite-jdbc)
%endif

Obsoletes:     %{name}-scala <= %{version}-4
BuildArch:     noarch
Source44: import.info

%description
Querydsl is a framework which enables the
construction of type safe SQL-like queries
for multiple backends including JPA, JDO and
SQL in Java.

Instead of writing queries as inline strings
or externalizing them into XML files they
are constructed via a fluent API.

%package apt
Group: Development/Java
Summary:       Querydsl - APT support

%description apt
Annotation Processing Tool based
Source code generation for Querydsl.

%package codegen
Group: Development/Java
Summary:       Querydsl - Codegen module

%description codegen
Codegen module for Querydsl.

%package collections
Group: Development/Java
Summary:       Querydsl - Collections support

%description collections
Collections support for Querydsl.

%package hibernate-search
Group: Development/Java
Summary:       Querydsl - Hibernate Search support

%description hibernate-search
Hibernate Search support for Querydsl.

%package jdo
Group: Development/Java
Summary:       Querydsl - JDO support

%description jdo
Java Data Objects support for Querydsl.

%package jpa
Group: Development/Java
Summary:       Querydsl - JPA support

%description jpa
Java Persistence API support for Querydsl.

%package jpa-codegen
Group: Development/Java
Summary:       Querydsl - JPA Codegen support

%description jpa-codegen
Java Persistence API Codegen support for Querydsl.

%package lucene3
Group: Development/Java
Summary:       Querydsl - Lucene 3 support

%description lucene3
Lucene 3 support for Querydsl.

%package maven-plugin
Group: Development/Java
Summary:       Querydsl - Maven plugin

%description maven-plugin
Querydsl Maven plugin.

%package mongodb
Group: Development/Java
Summary:       Querydsl - Mongodb support

%description mongodb
Mongodb support for Querydsl.

%package root
Group: Development/Java
Summary:       Querydsl - Parent POM

%description root
Parent POM project for Querydsl modules.

%package scala
Group: Development/Java
Summary:       Querydsl - Scala support

%description scala
Querydsl - Scala support.

%package spatial
Group: Development/Java
Summary:       Querydsl - Spatial module

%description spatial
Core module for Querydsl.

%package sql
Group: Development/Java
Summary:       Querydsl - SQL support

%description sql
SQL support for Querydsl.

%package sql-codegen
Group: Development/Java
Summary:       Querydsl - SQL Codegen support

%description sql-codegen
SQL Codegen support for Querydsl.

%package sql-spring
Group: Development/Java
Summary:       Querydsl - SQL Spring support

%description sql-spring
SQL Spring Framework support for Querydsl.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n querydsl-QUERYDSL_%{_version}
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

%pom_remove_parent
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin -r :maven-pmd-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r org.eluder.coveralls:coveralls-maven-plugin
%pom_remove_plugin -r :jacoco-maven-plugin
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:outputDirectory"
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:reportOutputDirectory"
# Use org.semver:enforcer-rule
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-source-plugin querydsl-sql-codegen
%pom_remove_plugin com.mysema.maven:apt-maven-plugin

%if %{without lucene4}
%pom_disable_module querydsl-lucene4
%endif

%pom_remove_plugin com.mysema.maven:apt-maven-plugin querydsl-lucene4

%pom_remove_plugin :maven-source-plugin querydsl-core
%pom_xpath_set "pom:dependency[pom:artifactId='annotation-indexer']/pom:groupId" org.jenkins-ci querydsl-core

%pom_remove_plugin :maven-source-plugin querydsl-codegen
%pom_remove_plugin :maven-source-plugin querydsl-spatial
%pom_remove_plugin com.mysema.maven:apt-maven-plugin querydsl-spatial

%pom_remove_plugin com.mysema.maven:apt-maven-plugin querydsl-apt
%pom_remove_plugin :maven-assembly-plugin querydsl-apt
# org.springframework.roo:org.springframework.roo.annotations:1.2.3.RELEASE
# https://gil.fedorapeople.org/springframework-roo-1.2.5-1.fc20.src.rpm
%pom_remove_dep org.springframework.roo:org.springframework.roo.annotations querydsl-apt
rm -r querydsl-apt/src/apt/roo
rm -r querydsl-apt/src/main/java/com/mysema/query/apt/roo

%pom_remove_plugin com.mysema.maven:apt-maven-plugin querydsl-collections

%pom_remove_plugin :maven-source-plugin querydsl-sql
%pom_xpath_set "pom:dependency[pom:artifactId='annotation-indexer']/pom:groupId" org.jenkins-ci querydsl-sql
%pom_change_dep :org.apache.servicemix.bundles.javax-inject javax.inject:javax.inject:1 querydsl-sql

%pom_remove_dep com.oracle:ojdbc6 querydsl-sql
%pom_remove_dep oracle:sdoapi querydsl-sql
rm -r querydsl-sql/src/main/java/com/mysema/query/sql/spatial/JGeometryConverter.java \
 querydsl-sql/src/main/java/com/mysema/query/sql/spatial/JGeometryType.java \
 querydsl-sql/src/main/java/com/mysema/query/sql/spatial/OracleSpatialTemplates.java

%if %{without postgis}
%pom_remove_dep org.postgis:postgis-jdbc querydsl-sql
rm -r querydsl-sql/src/main/java/com/mysema/query/sql/spatial/PGgeometryConverter.java \
 querydsl-sql/src/main/java/com/mysema/query/sql/spatial/PGgeometryType.java \
 querydsl-sql/src/main/java/com/mysema/query/sql/spatial/PostGISTemplates.java
%endif

%pom_xpath_set "pom:properties/pom:mvn.version" 3.1.1 querydsl-maven-plugin
%pom_change_dep :maven-project :maven-core:'${mvn.version}' querydsl-maven-plugin

%pom_remove_plugin :maven-source-plugin querydsl-jpa
%pom_remove_plugin :maven-assembly-plugin querydsl-jpa
%pom_remove_plugin com.mysema.maven:apt-maven-plugin querydsl-jpa

%pom_remove_plugin com.mysema.maven:apt-maven-plugin querydsl-jdo
%pom_remove_plugin :maven-assembly-plugin querydsl-jdo
%pom_remove_plugin org.datanucleus:datanucleus-maven-plugin querydsl-jdo

%pom_remove_plugin com.mysema.maven:apt-maven-plugin querydsl-lucene3
%pom_xpath_set "pom:properties/pom:lucene.version" 3 querydsl-lucene3
%pom_xpath_set "pom:properties/pom:lucene.version" 3 querydsl-hibernate-search

%pom_change_dep :hibernate-search :hibernate-search-orm querydsl-hibernate-search

%pom_remove_plugin com.mysema.maven:apt-maven-plugin querydsl-mongodb
%pom_remove_plugin :maven-assembly-plugin querydsl-mongodb

# A fatal error has been detected by the Java Runtime Environment:
#
#  Internal Error (assembler_aarch32.hpp:215), pid=9324, tid=0xb50d8470
#  guarantee(val < (1U << nbits)) failed: Field too big for insn
#
# JRE version: OpenJDK Runtime Environment (8.0_102) (build 1.8.0_102-160812)
# Java VM: OpenJDK Client VM (25.102-b160812 mixed mode linux-aarch32 )
# Failed to write core dump. Core dumps have been disabled. To enable core dumping, try "ulimit -c unlimited" before starting Java again
%if 0
%pom_remove_plugin net.alchim31.maven:scala-maven-plugin querydsl-scala
%pom_add_plugin org.apache.maven.plugins:maven-antrun-plugin:1.7 querydsl-scala '
<executions>
  <execution>
    <id>compile</id>
    <phase>process-sources</phase>
    <configuration>
      <tasks>
        <property name="build.compiler" value="extJavac"/>
        <taskdef resource="scala/tools/ant/antlib.xml" classpathref="maven.compile.classpath"/>
        <mkdir dir="target/classes"/>
        <scalac srcdir="src/main" destdir="target/classes" classpathref="maven.compile.classpath" encoding="UTF-8">
          <include name="**/*.*"/>
        </scalac>
      </tasks>
    </configuration>
      <goals>
        <goal>run</goal>
      </goals>
  </execution>
</executions>
<dependencies>
  <dependency>
      <groupId>org.scala-lang</groupId>
      <artifactId>scala-compiler</artifactId>
      <version>${scala.full.version}</version>
  </dependency>
</dependencies>'
%endif

%pom_disable_module querydsl-scala

%pom_xpath_set "pom:properties/pom:mongodb.version" 2 querydsl-mongodb
%pom_xpath_set -r "pom:properties/pom:hibernate.version" 4 querydsl-apt querydsl-hibernate-search querydsl-jpa querydsl-jpa-codegen querydsl-examples/querydsl-example-jpa-guice

# fix build failure. 'useDefaultManifestFile' has been removed from the maven-jar-plugin >= 3.0.0
%pom_remove_plugin :maven-jar-plugin

%mvn_package :querydsl-jdo::apt: querydsl-jdo
%mvn_package :querydsl-jpa::apt: querydsl-jpa

%build

# Unavailable test deps
%mvn_build -sf

%install
%mvn_install

%files -f .mfiles-querydsl-core
%doc README.md
%doc LICENSE.txt

%files apt -f .mfiles-querydsl-apt
%files codegen -f .mfiles-querydsl-codegen

%files collections -f .mfiles-querydsl-collections
%doc querydsl-collections/README.md

%files hibernate-search -f .mfiles-querydsl-hibernate-search

%files jdo -f .mfiles-querydsl-jdo
%doc querydsl-jdo/README.md

%files jpa -f .mfiles-querydsl-jpa
%doc querydsl-jpa/README.md

%files jpa-codegen -f .mfiles-querydsl-jpa-codegen

%files lucene3 -f .mfiles-querydsl-lucene3
%doc querydsl-lucene3/README.md

%files maven-plugin -f .mfiles-querydsl-maven-plugin

%files mongodb -f .mfiles-querydsl-mongodb
%doc querydsl-mongodb/README.md

%files root -f .mfiles-querydsl-root
%doc LICENSE.txt

%if 0
%files scala -f .mfiles-querydsl-scala
%endif

%files spatial -f .mfiles-querydsl-spatial

%files sql -f .mfiles-querydsl-sql
%doc querydsl-sql/README.md

%files sql-codegen -f .mfiles-querydsl-sql-codegen
%files sql-spring -f .mfiles-querydsl-sql-spring

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 3.7.2-alt2_6jpp8
- added BR: apache-parent for javapackages 5

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 3.7.2-alt1_6jpp8
- new jpp release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 3.6.6-alt1_3jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 3.6.6-alt1_1jpp8
- new version

