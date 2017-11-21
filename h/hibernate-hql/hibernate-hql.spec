Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.3.0
%global namedreltag .Alpha2
%global namedversion %{version}%{?namedreltag}

Name:             hibernate-hql
Version:          1.3.0
Release:          alt2_0.2.Alpha2jpp8
Summary:          Hibernate Query Parser
License:          LGPLv2 and ASL 2.0
Url:              https://github.com/hibernate/hibernate-hql-parser
Source0:          https://github.com/hibernate/hibernate-hql-parser/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

Source1:          https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/hibernate/hql/%{name}-parser/%{namedversion}/%{name}-parser-%{namedversion}.pom
Source2:          https://repository.jboss.org/nexus/service/local/repositories/releases/content/org/hibernate/hql/%{name}-lucene/%{namedversion}/%{name}-lucene-%{namedversion}.pom

BuildRequires:    maven-local
BuildRequires:    mvn(org.antlr:antlr-runtime) >= 3.4
BuildRequires:    mvn(org.antlr:antlr3-maven-plugin)
BuildRequires:    mvn(org.antlr:stringtemplate)
BuildRequires:    mvn(org.apache.lucene:lucene-core:4)
BuildRequires:    mvn(org.apache.lucene:lucene-analyzers:4)
BuildRequires:    mvn(org.apache.lucene:lucene-facet:4)
BuildRequires:    mvn(org.bsc.maven:maven-processor-plugin)
BuildRequires:    mvn(org.hibernate:hibernate-search-engine) >= 5.3.0
BuildRequires:    mvn(org.hibernate.javax.persistence:hibernate-jpa-2.1-api)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor) >= 1.2.0

BuildArch:        noarch
Source44: import.info

%description
Experimental new parser for HQL and JP-QL queries, to convert these into SQL
and other different targets such as Lucene queries, Map/Reduce queries for
NoSQL stores, make it possible to perform more sophisticated SQL
transformations.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-parser-%{namedversion}

find . -name '*.jar' -delete
find . -name '*.class' -delete

sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," license.txt

cp %{SOURCE1} parser/pom.xml
cp %{SOURCE2} lucene/pom.xml
# This is a dummy POM added just to ease building in the RPM platforms
cat > pom.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">

    <modelVersion>4.0.0</modelVersion>
    <groupId>org.hibernate.hql</groupId>
    <artifactId>hibernate-hql-parent</artifactId>
    <version>%{namedversion}</version>
    <packaging>pom</packaging>
    <name>Hibernate HQL/JP-QL Parent</name>
    <description>Hibernate HQL/JP-QL</description>

    <modules>
      <module>parser</module>
      <module>lucene</module>
    </modules>
  
</project>
EOF

%pom_add_plugin "org.bsc.maven:maven-processor-plugin:2.0.2 " parser '
<configuration>
    <defaultOutputDirectory>${project.build.directory}/generated-sources/logging</defaultOutputDirectory>
    <processors>
        <processor>org.jboss.logging.processor.apt.LoggingToolsProcessor</processor>
    </processors>
    <compilerArguments>
      -nowarn -proc:only -encoding UTF-8 
      -source 1.6 -target 1.6 
      -sourcepath ${project.build.directory}/generated-sources/antlr3 
      -Adebug=true -AskipTranslations=true
    </compilerArguments>
</configuration>
<executions>
    <execution>
        <id>process</id>
        <phase>generate-sources</phase>
        <goals>
            <goal>process</goal>
        </goals>
    </execution>
</executions>
<dependencies>
    <dependency>
        <groupId>org.jboss.logging</groupId>
        <artifactId>jboss-logging-processor</artifactId>
        <version>1.2.0.Final</version>
    </dependency>
</dependencies>'

%pom_add_plugin "org.antlr:antlr3-maven-plugin:3.4" parser " 
<executions>
  <execution>
   <phase>generate-sources</phase>
   <goals>
    <goal>antlr</goal>
   </goals>
   <configuration>
    <sourceDirectory>src/main/antlr</sourceDirectory>
   </configuration>
 </execution>
</executions>"

# package org.antlr.stringtemplate does not exist
%pom_add_dep org.antlr:stringtemplate:3.3-SNAPSHOT:provided parser
%pom_add_dep org.apache.lucene:lucene-core:4:provided lucene
%pom_add_dep org.apache.lucene:lucene-analyzers:4:provided lucene
%pom_add_dep org.apache.lucene:lucene-facet:4:provided lucene

%mvn_package :hibernate-hql-parent __noinstall

%build
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc copyright.txt license.txt

%files javadoc -f .mfiles-javadoc
%doc copyright.txt license.txt

%changelog
* Tue Nov 21 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_0.2.Alpha2jpp8
- build with lucene4

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_0.2.Alpha2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.7.Alpha6jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.6.Alpha6jpp8
- full build

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

