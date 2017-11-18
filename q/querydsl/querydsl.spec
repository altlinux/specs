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
%define version 4.0.4
%global _version %( echo %{version} | tr . _ )

%if 0%{?fedora}
# lucene:4.2.1
#def_with lucene4
%bcond_with lucene4
# lucene:5.1.0
#def_with lucene5
%bcond_with lucene5
# https://bugzilla.redhat.com/show_bug.cgi?id=1213455
#def_with postgis
%bcond_with postgis
%endif

Name:          querydsl
# NOTE: newer release use hibernate-core:4.3.11.Final
Version:       4.0.4
Release:       alt2_6jpp8
Summary:       Type-safe queries for Java
License:       LGPLv2+
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
%if %{with lucene5}
BuildRequires: mvn(org.apache.lucene:lucene-analyzers-common:5.1.0)
BuildRequires: mvn(org.apache.lucene:lucene-core:5.1.0)
BuildRequires: mvn(org.apache.lucene:lucene-queries:5.1.0)
BuildRequires: mvn(org.apache.lucene:lucene-queryparser:5.1.0)
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
# https://bugzilla.redhat.com/show_bug.cgi?id=1196043
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

Obsoletes:     %{name}-scala =< %{version}-4
BuildArch:     noarch
Source44: import.info

%description
Querydsl is a framework which enables the
construction of type-safe SQL-like queries
for multiple backends including JPA, JDO and
SQL in Java.

Instead of writing queries as inline strings
or externalizing them into XML files they
are constructed via a fluent API.

%package apt
Group: Development/Java
Summary:       Querydsl - APT support

%description apt
APT based Source code generation for Querydsl.

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
JDO support for Querydsl.

%package jpa
Group: Development/Java
Summary:       Querydsl - JPA support

%description jpa
JPA support for Querydsl.

%package jpa-codegen
Group: Development/Java
Summary:       Querydsl - JPA Codegen support

%description jpa-codegen
JPA Codegen support for Querydsl.

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

%package sql-spatial
Group: Development/Java
Summary:       Querydsl - SQL Spatial support

%description sql-spatial
SQL Spatial support for Querydsl.

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
%setup -q -n %{name}-QUERYDSL_%{_version}
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

%pom_remove_parent
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin -r :maven-pmd-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-version-plugin
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:outputDirectory"
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:reportOutputDirectory"
%pom_remove_plugin :maven-checkstyle-plugin
# Use unavailable org.semver:enforcer-rule
%pom_remove_plugin :maven-enforcer-plugin

%pom_remove_plugin :maven-source-plugin %{name}-sql-codegen
%pom_remove_plugin :maven-source-plugin %{name}-sql-spatial

%if %{without lucene4}
%pom_disable_module %{name}-lucene4
%endif
%if %{without lucene5}
%pom_disable_module %{name}-lucene5
%endif
%pom_remove_plugin com.mysema.maven:apt-maven-plugin
%pom_remove_plugin com.mysema.maven:apt-maven-plugin %{name}-lucene4
%pom_remove_plugin com.mysema.maven:apt-maven-plugin %{name}-lucene5

%pom_remove_plugin :maven-source-plugin %{name}-core
%pom_xpath_set "pom:dependency[pom:artifactId='annotation-indexer']/pom:groupId" org.jenkins-ci %{name}-core

%pom_remove_plugin :maven-source-plugin %{name}-codegen
%pom_remove_plugin :maven-source-plugin %{name}-spatial
%pom_remove_plugin com.mysema.maven:apt-maven-plugin %{name}-spatial

%pom_remove_plugin com.mysema.maven:apt-maven-plugin %{name}-apt
%pom_remove_plugin :maven-assembly-plugin %{name}-apt
# org.springframework.roo:org.springframework.roo.annotations:1.2.3.RELEASE
# https://gil.fedorapeople.org/springframework-roo-1.2.5-1.fc20.src.rpm
%pom_remove_dep org.springframework.roo:org.springframework.roo.annotations %{name}-apt
rm -r %{name}-apt/src/apt/roo
rm -r %{name}-apt/src/main/java/com/querydsl/apt/roo

%pom_remove_plugin com.mysema.maven:apt-maven-plugin %{name}-collections

%pom_remove_plugin :maven-source-plugin %{name}-sql
%pom_xpath_set "pom:dependency[pom:artifactId='annotation-indexer']/pom:groupId" org.jenkins-ci %{name}-sql
%pom_xpath_set "pom:dependency[pom:artifactId='annotation-indexer']/pom:groupId" org.jenkins-ci %{name}-sql-spatial
%pom_change_dep :org.apache.servicemix.bundles.javax-inject javax.inject:javax.inject:1 %{name}-sql

%pom_remove_dep com.oracle:ojdbc6 %{name}-sql
%pom_remove_dep oracle:sdoapi %{name}-sql
%pom_remove_dep com.oracle:ojdbc6 %{name}-sql-spatial
%pom_remove_dep oracle:sdoapi %{name}-sql-spatial
rm -r %{name}-sql-spatial/src/main/java/com/querydsl/sql/spatial/JGeometryConverter.java \
 %{name}-sql-spatial/src/main/java/com/querydsl/sql/spatial/JGeometryType.java \
 %{name}-sql-spatial/src/main/java/com/querydsl/sql/spatial/OracleSpatialTemplates.java

%if %{without postgis}
%pom_remove_dep org.postgis:postgis-jdbc %{name}-sql
%pom_remove_dep org.postgis:postgis-jdbc %{name}-sql-spatial
rm -r %{name}-sql-spatial/src/main/java/com/querydsl/sql/spatial/PGgeometryConverter.java \
 %{name}-sql-spatial/src/main/java/com/querydsl/sql/spatial/PGgeometryType.java \
 %{name}-sql-spatial/src/main/java/com/querydsl/sql/spatial/PostGISTemplates.java
%endif

%pom_xpath_set "pom:properties/pom:mvn.version" 3.1.1 %{name}-maven-plugin
%pom_change_dep :maven-project :maven-core:'${mvn.version}' %{name}-maven-plugin

%pom_remove_plugin :maven-source-plugin %{name}-jpa
%pom_remove_plugin :maven-assembly-plugin %{name}-jpa
%pom_remove_plugin com.mysema.maven:apt-maven-plugin %{name}-jpa

%pom_remove_plugin com.mysema.maven:apt-maven-plugin %{name}-jdo
%pom_remove_plugin :maven-assembly-plugin %{name}-jdo
%pom_remove_plugin org.datanucleus:datanucleus-maven-plugin %{name}-jdo

%pom_remove_plugin com.mysema.maven:apt-maven-plugin %{name}-lucene3
%pom_xpath_set "pom:properties/pom:lucene.version" 3 %{name}-lucene3

%pom_change_dep :hibernate-search :hibernate-search-orm %{name}-hibernate-search

%pom_remove_plugin com.mysema.maven:apt-maven-plugin %{name}-mongodb
%pom_remove_plugin :maven-assembly-plugin %{name}-mongodb


# A fatal error has been detected by the Java Runtime Environment:
#
#  Internal Error (assembler_aarch32.hpp:215), pid=27932, tid=0xb5198470
#  guarantee(val < (1U << nbits)) failed: Field too big for insn
#
# JRE version: OpenJDK Runtime Environment (8.0_102) (build 1.8.0_102-160812)
# Java VM: OpenJDK Client VM (25.102-b160812 mixed mode linux-aarch32 )
# Core dump written. Default location: /builddir/build/BUILD/querydsl-QUERYDSL_4_0_4/core or core.27932
%if 0
%pom_remove_plugin net.alchim31.maven:scala-maven-plugin %{name}-scala
%pom_add_plugin org.apache.maven.plugins:maven-antrun-plugin:1.7 %{name}-scala '
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
%pom_disable_module %{name}-scala

%pom_remove_dep -r org.codehaus.mojo:animal-sniffer-annotations
rm -r querydsl-sql/src/main/java/com/querydsl/sql/types/JSR310InstantType.java \
 querydsl-sql/src/main/java/com/querydsl/sql/types/AbstractJSR310DateTimeType.java \
 querydsl-sql/src/main/java/com/querydsl/sql/types/JSR310LocalDateTimeType.java \
 querydsl-sql/src/main/java/com/querydsl/sql/types/JSR310OffsetTimeType.java \
 querydsl-sql/src/main/java/com/querydsl/sql/types/JSR310ZonedDateTimeType.java \
 querydsl-sql/src/main/java/com/querydsl/sql/types/JSR310LocalTimeType.java \
 querydsl-sql/src/main/java/com/querydsl/sql/types/JSR310LocalDateType.java \
 querydsl-sql/src/main/java/com/querydsl/sql/types/JSR310OffsetDateTimeType.java

%pom_xpath_set "pom:properties/pom:mongodb.version" 2 querydsl-mongodb
%pom_xpath_set -r "pom:properties/pom:hibernate.version" 4 querydsl-apt querydsl-hibernate-search querydsl-jpa querydsl-jpa-codegen querydsl-examples/querydsl-example-jpa-guice

# fix build failure. 'useDefaultManifestFile' has been removed from the maven-jar-plugin >= 3.0.0
%pom_remove_plugin :maven-jar-plugin

%mvn_package :%{name}-jdo::apt: %{name}-jdo
%mvn_package :%{name}-jpa::apt: %{name}-jpa

%build

# Unavailable test deps
%mvn_build -sf

%install
%mvn_install

%files -f .mfiles-%{name}-core
%doc README.md
%doc LICENSE.txt

%files apt -f .mfiles-%{name}-apt
%files codegen -f .mfiles-%{name}-codegen

%files collections -f .mfiles-%{name}-collections
%doc %{name}-collections/README.md

%files hibernate-search -f .mfiles-%{name}-hibernate-search

%files jdo -f .mfiles-%{name}-jdo
%doc %{name}-jdo/README.md

%files jpa -f .mfiles-%{name}-jpa
%doc %{name}-jpa/README.md

%files jpa-codegen -f .mfiles-%{name}-jpa-codegen

%files lucene3 -f .mfiles-%{name}-lucene3
%doc %{name}-lucene3/README.md

%files maven-plugin -f .mfiles-%{name}-maven-plugin

%files mongodb -f .mfiles-%{name}-mongodb
%doc %{name}-mongodb/README.md

%files root -f .mfiles-%{name}-root
%doc LICENSE.txt

%if 0
%files scala -f .mfiles-%{name}-scala
%endif

%files spatial -f .mfiles-%{name}-spatial

%files sql -f .mfiles-%{name}-sql
%doc %{name}-sql/README.md

%files sql-codegen -f .mfiles-%{name}-sql-codegen
%files sql-spatial -f .mfiles-%{name}-sql-spatial
%files sql-spring -f .mfiles-%{name}-sql-spring

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt2_6jpp8
- added BR: apache-parent for javapackages 5

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt1_6jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt1_3jpp8
- new version

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.3-alt1_3jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.3-alt1_1jpp8
- new version

