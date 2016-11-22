Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name hibernate
%define version 4.3.5
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          hibernate
Version:       4.3.5
Release:       alt1_7jpp8
Summary:       Relational persistence and query service
License:       LGPLv2+ and ASL 2.0
URL:           http://www.hibernate.org/
Source0:       https://github.com/hibernate/hibernate-orm/archive/%{namedversion}.tar.gz

Source1:       http://repo1.maven.org/maven2/org/hibernate/hibernate-c3p0/%{namedversion}/hibernate-c3p0-%{namedversion}.pom
Source2:       http://repo1.maven.org/maven2/org/hibernate/hibernate-core/%{namedversion}/hibernate-core-%{namedversion}.pom
Source3:       http://repo1.maven.org/maven2/org/hibernate/hibernate-ehcache/%{namedversion}/hibernate-ehcache-%{namedversion}.pom
Source4:       http://repo1.maven.org/maven2/org/hibernate/hibernate-entitymanager/%{namedversion}/hibernate-entitymanager-%{namedversion}.pom
Source5:       http://repo1.maven.org/maven2/org/hibernate/hibernate-envers/%{namedversion}/hibernate-envers-%{namedversion}.pom
Source6:       http://repo1.maven.org/maven2/org/hibernate/hibernate-infinispan/%{namedversion}/hibernate-infinispan-%{namedversion}.pom
Source7:       http://repo1.maven.org/maven2/org/hibernate/hibernate-proxool/%{namedversion}/hibernate-proxool-%{namedversion}.pom
Source8:       http://repo1.maven.org/maven2/org/hibernate/hibernate-testing/%{namedversion}/hibernate-testing-%{namedversion}.pom
Source9:       http://repo1.maven.org/maven2/org/hibernate/hibernate-osgi/%{namedversion}/hibernate-osgi-%{namedversion}.pom

# Custom hibernate-parent POM
Source50:      hibernate-parent-%{namedversion}.pom

# hibernate package don't include ASL license file
Source60:      http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: maven-local

BuildRequires: ant
BuildRequires: antlr-tool
BuildRequires: bean-validation-api
BuildRequires: byteman
BuildRequires: c3p0
BuildRequires: cdi-api
BuildRequires: classmate
BuildRequires: dom4j
BuildRequires: ehcache-core
BuildRequires: h2
BuildRequires: hibernate-commons-annotations
BuildRequires: hibernate-jpa-2.0-api
BuildRequires: hibernate-validator
BuildRequires: infinispan
BuildRequires: jandex
BuildRequires: javassist
BuildRequires: jboss-common-core
BuildRequires: jboss-jacc-1.4-api
BuildRequires: narayana
BuildRequires: jboss-logging
BuildRequires: jboss-naming
BuildRequires: jboss-transaction-1.1-api
BuildRequires: junit
BuildRequires: log4j
BuildRequires: mchange-commons
BuildRequires: mockito
BuildRequires: proxool
BuildRequires: rhq-plugin-annotations
BuildRequires: shrinkwrap
BuildRequires: slf4j
BuildRequires: xapool
BuildRequires: annox
BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-logging
BuildRequires: codemodel
BuildRequires: glassfish-jaxb
BuildRequires: glassfish-jaxb-api
BuildRequires: hibernate-jpamodelgen
BuildRequires: jaxb2-common-basics
BuildRequires: jboss-logging-tools

BuildRequires:  mvn(org.jvnet.jaxb2_commons:jaxb2-basics-runtime)
BuildRequires:  mvn(org.jvnet.jaxb2.maven2:maven-jaxb22-plugin)
BuildRequires:  mvn(org.eclipse.osgi:org.eclipse.osgi)
BuildRequires:  mvn(org.bsc.maven:maven-processor-plugin)
BuildRequires:  antlr-maven-plugin

BuildRequires:  maven-jaxb2-plugin
BuildRequires:  hibernate-hql

BuildArch:     noarch
Source44: import.info

%description
Hibernate is a powerful, ultra-high performance
object/relational persistence and query service
for Java. Hibernate lets you develop persistent
objects following common Java idiom - including
association, inheritance, polymorphism, composition
and the Java collections framework. Extremely
fine-grained, richly typed object models are
possible. The Hibernate Query Language, designed
as a "minimal" object-oriented extension to SQL,
provides an elegant bridge between the object and
relational worlds. Hibernate is now the most
popular ORM solution for Java.

%package core
Group: Development/Java
Summary:       Hibernate Core

%description core
Core Hibernate O/RM functionality

%package c3p0
Group: Development/Java
Summary:       Hibernate C3P0 ConnectionProvider

%description c3p0
C3P0-based implementation of the Hibernate ConnectionProvder contract.

%package ehcache
Group: Development/Java
Summary:       Hibernate Ehcache Integration

%description ehcache
Integration of Hibernate with Ehcache.

%package entitymanager
Group: Development/Java
Summary:       Hibernate Entity Manager

%description entitymanager
Hibernate Entity Manager.

%package envers
Group: Development/Java
Summary:       Hibernate Envers

%description envers
Support for entity auditing.

%package infinispan
Group: Development/Java
Summary:       Hibernate Infinispan Integration

%description infinispan
Integration of Hibernate with Infinispan.

%package proxool
Group: Development/Java
Summary:       Hibernate Proxool ConnectionProvider

%description proxool
Proxool-based implementation of the Hibernate ConnectionProvder contract.

%package osgi
Group: Development/Java
Summary:       Hibernate OSGi Support

%description osgi
Support for running Hibernate O/RM in OSGi environments.

%package testing
Group: Development/Java
Summary:       Hibernate Testing

%description testing
Hibernate JUnit test utilities.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n hibernate-orm-%{namedversion}

find .  -name "*.jar" -delete
find .  -name "*.class" -delete
rm -r documentation/*

# Copy poms
cp %{SOURCE50} pom.xml
cp %{SOURCE1} hibernate-c3p0/pom.xml
cp %{SOURCE2} hibernate-core/pom.xml
cp %{SOURCE3} hibernate-ehcache/pom.xml
cp %{SOURCE4} hibernate-entitymanager/pom.xml
cp %{SOURCE5} hibernate-envers/pom.xml
cp %{SOURCE6} hibernate-infinispan/pom.xml
cp %{SOURCE7} hibernate-proxool/pom.xml
cp %{SOURCE8} hibernate-testing/pom.xml
cp %{SOURCE9} hibernate-osgi/pom.xml

cp -p %{SOURCE60} .
sed -i 's/\r//' LICENSE-2.0.txt

for m in entitymanager envers core; do
%pom_add_plugin org.bsc.maven:maven-processor-plugin hibernate-${m} "
<configuration>
    <defaultOutputDirectory>\${project.build.directory}/generated-sources/logging</defaultOutputDirectory>
    <processors>
        <processor>org.jboss.logging.processor.apt.LoggingToolsProcessor</processor>
    </processors>
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
        <version>1.2.0.Beta1</version>
    </dependency>
</dependencies>"
done

pushd hibernate-core

%pom_add_plugin "org.jvnet.jaxb2.maven2:maven-jaxb22-plugin" . "
<executions>
  <execution>
    <id>hibernate-configuration</id>
    <goals>
      <goal>generate</goal>
    </goals>
    <configuration>
      <schemaIncludes>
        <include>hibernate-configuration-4.0.xsd</include>
      </schemaIncludes>
      <bindingIncludes>
        <include>hbm-configuration-bindings.xjb</include>
      </bindingIncludes>
      <generatePackage>org.hibernate.internal.jaxb.cfg</generatePackage>
      <generateDirectory>\${project.build.directory}/generated-sources/hibernate-configuration</generateDirectory>
    </configuration>
  </execution>
  <execution>
    <id>hibernate-mapping</id>
    <goals>
      <goal>generate</goal>
    </goals>
    <configuration>
      <schemaIncludes>
        <include>hibernate-mapping-4.0.xsd</include>
      </schemaIncludes>
      <bindingIncludes>
        <include>hbm-mapping-bindings.xjb</include>
      </bindingIncludes>
      <generatePackage>org.hibernate.internal.jaxb.mapping.hbm</generatePackage>
      <generateDirectory>\${project.build.directory}/generated-sources/hibernate-mapping</generateDirectory>
    </configuration>
  </execution>
  <execution>
    <id>hibernate-orm</id>
    <goals>
      <goal>generate</goal>
    </goals>
    <configuration>
      <schemaIncludes>
        <include>jpa/orm_2_0.xsd</include>
      </schemaIncludes>
      <bindingIncludes>
        <include>orm-bindings.xjb</include>
      </bindingIncludes>
      <generatePackage>org.hibernate.internal.jaxb.mapping.orm</generatePackage>
      <generateDirectory>\${project.build.directory}/generated-sources/hibernate-orm</generateDirectory>
    </configuration>
  </execution>
</executions>
<configuration>
  <schemaDirectory>src/main/resources/org/hibernate</schemaDirectory>
  <bindingDirectory>src/main/xjb</bindingDirectory>
  <extension>true</extension>
  <plugins>
    <plugin>
      <groupId>org.jvnet.jaxb2_commons</groupId>
      <artifactId>jaxb2-basics</artifactId>
      <version>0.6.3</version>
    </plugin>
  </plugins>
  <args>
    <arg>-Xinheritance</arg>
  </args>
</configuration>"


%pom_add_plugin "org.codehaus.mojo:antlr-maven-plugin" . "
<configuration>
  <grammars>*</grammars>
</configuration>
<executions>
  <execution>
    <goals>
      <goal>generate</goal>
    </goals>
  </execution>
</executions>"

%pom_add_plugin "org.apache.maven.plugins:maven-compiler-plugin" . "
<configuration>
  <source>1.5</source>
  <target>1.5</target>
</configuration>
<inherited>true</inherited>"

%pom_add_plugin org.apache.felix:maven-bundle-plugin . "
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-Description>hibernate core</Bundle-Description>
    <Bundle-SymbolicName>org.hibernate.core</Bundle-SymbolicName>
    <Bundle-Name>hibernate-core</Bundle-Name>
    <Bundle-Vendor>Hibernate.org</Bundle-Vendor>
    <Bundle-Version>\${project.version}</Bundle-Version>
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
</executions>"

%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin . "
<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
    <manifest>
      <addClasspath>false</addClasspath>
      <mainClass>org.hibernate.Version</mainClass>
    </manifest>
    <manifestEntries>
      <Implementation-Url>http://hibernate.org</Implementation-Url>
      <Implementation-Vendor>Hibernate.org</Implementation-Vendor>
      <Implementation-Vendor-Id>org.hibernate</Implementation-Vendor-Id>
      <Implementation-Version>\${project.version}</Implementation-Version>
    </manifestEntries>
  </archive>
</configuration>"

popd

for m in c3p0 ehcache entitymanager envers infinispan osgi proxool testing; do
%pom_add_plugin org.apache.felix:maven-bundle-plugin hibernate-${m} "
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-Description>hibernate ${m}</Bundle-Description>
    <Bundle-SymbolicName>org.hibernate.${m}</Bundle-SymbolicName>
    <Bundle-Name>hibernate-${m}</Bundle-Name>
    <Bundle-Vendor>Hibernate.org</Bundle-Vendor>
    <Bundle-Version>\${project.version}</Bundle-Version>
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
</executions>"

%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin hibernate-${m} "
<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
    <manifestEntries>
      <Implementation-Url>http://hibernate.org</Implementation-Url>
      <Implementation-Vendor>Hibernate.org</Implementation-Vendor>
      <Implementation-Vendor-Id>org.hibernate</Implementation-Vendor-Id>
      <Implementation-Version>\${project.version}</Implementation-Version>
    </manifestEntries>
  </archive>
</configuration>"

done

# Add missing deps
%pom_add_dep "com.fasterxml:classmate" hibernate-core/pom.xml
%pom_add_dep "org.jboss.spec.javax.security.jacc:jboss-jacc-api_1.4_spec" hibernate-core/pom.xml
%pom_add_dep "org.apache.ant:ant:1.9.4:provided" hibernate-core/pom.xml
%pom_add_dep "javax.validation:validation-api" hibernate-core/pom.xml
%pom_add_dep "junit:junit:4:test" hibernate-core/pom.xml
%pom_add_dep "org.hibernate:hibernate-testing:%{namedversion}:test" hibernate-core/pom.xml
%pom_add_dep "javax.enterprise:cdi-api" hibernate-entitymanager/pom.xml
%pom_add_dep "org.eclipse.osgi:org.eclipse.osgi" hibernate-osgi/pom.xml

# Use narayana instead of old jboss-jts
%pom_remove_dep "org.jboss.jbossts:jbossjta" hibernate-testing/pom.xml
%pom_add_dep "org.jboss.narayana.jta:jta" hibernate-testing/pom.xml

# fix non ASCII chars
for f in $(grep -e 'Pedersen\|Lichtmaier\|Chanfreau\|Benke\|Carlos\|CREATE\ SCHEMA' --include *.java -r -l | sort | uniq); do
  native2ascii -encoding UTF8 ${f} ${f}
done

sed -i.jandex1.2.2 "s|classDotName, superName, access_flag, interfaces, map|classDotName, superName, access_flag, interfaces, map, true|" \
 hibernate-core/src/main/java/org/hibernate/metamodel/source/annotations/xml/mocker/IndexBuilder.java

%build
# Disabled beacuse of cyclic dep between core and testing modules
%mvn_build -s -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles-hibernate-parent
%doc changelog.txt README.md
%doc lgpl.txt LICENSE-2.0.txt

%files core -f .mfiles-hibernate-core
%doc changelog.txt lgpl.txt LICENSE-2.0.txt README.md

%files c3p0 -f .mfiles-hibernate-c3p0
%doc lgpl.txt

%files ehcache -f .mfiles-hibernate-ehcache
%doc lgpl.txt LICENSE-2.0.txt

%files entitymanager -f .mfiles-hibernate-entitymanager
%doc lgpl.txt

%files envers -f .mfiles-hibernate-envers
%doc lgpl.txt LICENSE-2.0.txt

%files infinispan -f .mfiles-hibernate-infinispan
%doc lgpl.txt LICENSE-2.0.txt

%files proxool -f .mfiles-hibernate-proxool
%doc lgpl.txt LICENSE-2.0.txt

%files testing -f .mfiles-hibernate-testing
%doc lgpl.txt LICENSE-2.0.txt

%files osgi -f .mfiles-hibernate-osgi
%doc lgpl.txt

%files javadoc -f .mfiles-javadoc
%doc lgpl.txt LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 4.3.5-alt1_7jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 4.3.5-alt1_6jpp8
- unbootstrap build

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 4.3.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.7-alt1_6jpp7
- new version

