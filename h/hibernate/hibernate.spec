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
%define version 5.0.10
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

# Conditionals to help breaking hibernate <-> infinispan dependency cycle
%if 0%{?fedora}
%bcond_with infinispan
# Use geolatte-geom 1.0.1 but 1.x series is no compatible with the 0.1x
%bcond_with spatial
%endif

%global pom_url http://repo1.maven.org/maven2/org/hibernate

Name:          hibernate
Version:       5.0.10
Release:       alt1_4jpp8
Summary:       Relational persistence and query service
License:       LGPLv2+ and ASL 2.0
URL:           http://www.hibernate.org/
Source0:       https://github.com/hibernate/hibernate-orm/archive/%{version}/%{name}-%{namedversion}.tar.gz

Source1:       %{pom_url}/hibernate-c3p0/%{namedversion}/hibernate-c3p0-%{namedversion}.pom
Source2:       %{pom_url}/hibernate-core/%{namedversion}/hibernate-core-%{namedversion}.pom
Source3:       %{pom_url}/hibernate-ehcache/%{namedversion}/hibernate-ehcache-%{namedversion}.pom
Source4:       %{pom_url}/hibernate-entitymanager/%{namedversion}/hibernate-entitymanager-%{namedversion}.pom
Source5:       %{pom_url}/hibernate-envers/%{namedversion}/hibernate-envers-%{namedversion}.pom
Source6:       %{pom_url}/hibernate-hikaricp/%{namedversion}/hibernate-hikaricp-%{namedversion}.pom
Source7:       %{pom_url}/hibernate-infinispan/%{namedversion}/hibernate-infinispan-%{namedversion}.pom
Source8:       %{pom_url}/hibernate-java8/%{namedversion}/hibernate-java8-%{namedversion}.pom
Source9:       %{pom_url}/hibernate-osgi/%{namedversion}/hibernate-osgi-%{namedversion}.pom
Source10:      %{pom_url}/hibernate-proxool/%{namedversion}/hibernate-proxool-%{namedversion}.pom
Source11:      %{pom_url}/hibernate-spatial/%{namedversion}/hibernate-spatial-%{namedversion}.pom
Source12:      %{pom_url}/hibernate-testing/%{namedversion}/hibernate-testing-%{namedversion}.pom

# http://repo1.maven.org/maven2/org/hibernate/hibernate-jpamodelgen/5.0.10.Final/hibernate-jpamodelgen-5.0.10.Final.pom

# Custom hibernate-parent POM
Source50:      hibernate-parent-%{namedversion}.pom

# hibernate package don't include ASL license file
Source60:      http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: maven-local
BuildRequires: mvn(antlr:antlr)
BuildRequires: mvn(com.experlog:xapool)
BuildRequires: mvn(com.fasterxml:classmate)
BuildRequires: mvn(com.mchange:c3p0)
BuildRequires: mvn(com.zaxxer:HikariCP)
BuildRequires: mvn(dom4j:dom4j)
BuildRequires: mvn(java_cup:java_cup)
BuildRequires: mvn(javax.enterprise:cdi-api)
BuildRequires: mvn(javax.validation:validation-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.sf.ehcache:ehcache-core)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jta_1.1_spec)
BuildRequires: mvn(org.apache.geronimo.specs:specs-parent:pom:)
BuildRequires: mvn(org.bsc.maven:maven-processor-plugin)
BuildRequires: mvn(org.codehaus.mojo:antlr-maven-plugin)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi)
%if %{with spatial}
BuildRequires: mvn(org.geolatte:geolatte-geom)
BuildRequires: mvn(postgresql:postgresql)
%endif
BuildRequires: mvn(org.hibernate.common:hibernate-commons-annotations)
BuildRequires: mvn(org.hibernate.javax.persistence:hibernate-jpa-2.1-api)
%if %{without infinispan}
BuildRequires: mvn(org.infinispan:infinispan-core) >= 7.2.1
%endif
BuildRequires: mvn(org.javassist:javassist)
BuildRequires: mvn(org.jboss:jandex)
BuildRequires: mvn(org.jboss.byteman:byteman)
BuildRequires: mvn(org.jboss.byteman:byteman-bmunit)
BuildRequires: mvn(org.jboss.byteman:byteman-install)
BuildRequires: mvn(org.jboss.logging:jboss-logging)
BuildRequires: mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires: mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires: mvn(org.jboss.narayana.jta:jta)
BuildRequires: mvn(org.jboss.spec.javax.security.jacc:jboss-jacc-api_1.4_spec)
BuildRequires: mvn(org.jvnet.jaxb2.maven2:maven-jaxb22-plugin)
BuildRequires: mvn(org.jvnet.jaxb2_commons:jaxb2-basics)
BuildRequires: mvn(org.rhq.helpers:rhq-pluginAnnotations)
BuildRequires: mvn(proxool:proxool)

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

%package hikaricp
Group: Development/Java
Summary:       Hibernate HikariCP Integration

%description hikaricp
Integration of Hibernate with HikariCP.

%package infinispan
Group: Development/Java
Summary:       Hibernate Infinispan Integration

%description infinispan
Integration of Hibernate with Infinispan.

%package java8
Group: Development/Java
Summary:       Hibernate Java8-specific functionality

%description java8
Support for Java8-specific features - mainly Java8 Date/Time (JSR 310).

%package osgi
Group: Development/Java
Summary:       Hibernate OSGi Support

%description osgi
Support for running Hibernate O/RM in OSGi environments.

%package parent
Group: Development/Java
Summary:       Hibernate Parent POM

%description parent
Hibernate Parent POM.

%package proxool
Group: Development/Java
Summary:       Hibernate Proxool ConnectionProvider

%description proxool
Proxool-based implementation of the Hibernate ConnectionProvder contract.

%package spatial
Group: Development/Java
Summary:       Hibernate Spatial/GIS Integration

%description spatial
Integrate support for Spatial/GIS data into Hibernate.

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
%setup -q -n %{name}-orm-%{version}
find .  -name "*.jar" -delete
find .  -name "*.class" -delete
rm -r documentation/*

cp -p %{SOURCE1} hibernate-c3p0/pom.xml
cp -p %{SOURCE2} hibernate-core/pom.xml
cp -p %{SOURCE3} hibernate-ehcache/pom.xml
cp -p %{SOURCE4} hibernate-entitymanager/pom.xml
cp -p %{SOURCE5} hibernate-envers/pom.xml
cp -p %{SOURCE6} hibernate-hikaricp/pom.xml
cp -p %{SOURCE7} hibernate-infinispan/pom.xml
cp -p %{SOURCE8} hibernate-java8/pom.xml
cp -p %{SOURCE9} hibernate-osgi/pom.xml
cp -p %{SOURCE10} hibernate-proxool/pom.xml
cp -p %{SOURCE11} hibernate-spatial/pom.xml
cp -p %{SOURCE12} hibernate-testing/pom.xml

cp -p %{SOURCE50} pom.xml

cp -p %{SOURCE60} .
sed -i 's/\r//' LICENSE-2.0.txt

for m in entitymanager envers core; do
%pom_add_plugin org.bsc.maven:maven-processor-plugin:2.2.4 hibernate-${m} "
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
        <version>2.0.1.Final</version>
    </dependency>
</dependencies>"
done

pushd hibernate-core

%pom_add_plugin "org.jvnet.jaxb2.maven2:maven-jaxb22-plugin:0.12.3" . "
<executions>
  <execution>
    <id>hibernate-configuration</id>
    <goals>
      <goal>generate</goal>
    </goals>
    <configuration>
      <schemaIncludes>
        <include>cfg/legacy-configuration-4.0.xsd</include>
      </schemaIncludes>
      <bindingIncludes>
        <include>hbm-configuration-bindings.xjb</include>
      </bindingIncludes>
      <generatePackage>org.hibernate.boot.jaxb.cfg.spi</generatePackage>
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
        <include>mapping/legacy-mapping-4.0.xsd</include>
      </schemaIncludes>
      <bindingIncludes>
        <include>hbm-mapping-bindings.xjb</include>
      </bindingIncludes>
      <generatePackage>org.hibernate.boot.jaxb.hbm.spi</generatePackage>
      <generateDirectory>\${project.build.directory}/generated-sources/hibernate-mapping</generateDirectory>
      <args>
        <arg>-Xinheritance</arg>
        <arg>-Xsimplify</arg>
      </args>
    </configuration>
  </execution>
</executions>
<configuration>
  <schemaDirectory>src/main/resources/org/hibernate/xsd</schemaDirectory>
  <bindingDirectory>src/main/xjb</bindingDirectory>
  <extension>true</extension>
  <plugins>
    <plugin>
      <groupId>org.jvnet.jaxb2_commons</groupId>
      <artifactId>jaxb2-basics</artifactId>
      <version>0.6.3</version>
    </plugin>
  </plugins>
</configuration>"

%pom_add_plugin "org.codehaus.mojo:antlr-maven-plugin:2.2" . "
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

%pom_add_plugin "org.apache.maven.plugins:maven-compiler-plugin:3.3" . "
<configuration>
  <source>1.6</source>
  <target>1.6</target>
</configuration>
<inherited>true</inherited>"

%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.5.4 . "
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

%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin:2.6 . "
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

# Add missing deps
%pom_add_dep "com.fasterxml:classmate:1.1.0"
%pom_add_dep "javax.validation:validation-api:1.1.0.Final"
%pom_add_dep "org.apache.ant:ant:1.9.4:provided"
#%% pom_add_dep "org.jboss.spec.javax.security.jacc:jboss-jacc-api_1.5_spec:1.0.0.Final"
%pom_add_dep "org.jboss.spec.javax.security.jacc:jboss-jacc-api_1.4_spec:1.0.2.Final"

%pom_add_dep "junit:junit:4.12:test"
%pom_add_dep "org.hibernate:hibernate-testing:%{namedversion}:test"

popd

%pom_add_dep "javax.enterprise:cdi-api:1.2" hibernate-entitymanager

# Fix HikariCP aId
%pom_change_dep "com.zaxxer:HikariCP-java6" "com.zaxxer:HikariCP:2.4.0" hibernate-hikaricp

# Use eclipse apis only
%pom_change_dep "org.osgi:org.osgi.core" "org.eclipse.osgi:org.eclipse.osgi:3.10.102.v20160416-2200" hibernate-osgi
%pom_remove_dep "org.osgi:org.osgi.compendium" hibernate-osgi

# Use narayana instead of old jboss-jts
%pom_change_dep "org.jboss.jbossts:jbossjta" "org.jboss.narayana.jta:jta" hibernate-testing

for m in c3p0 ehcache entitymanager envers hikaricp infinispan java8 osgi proxool spatial testing; do
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.5.4 hibernate-${m} "
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

%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin:2.6 hibernate-${m} "
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

# fix non ASCII chars
for f in $(grep -e 'Pedersen\|Lichtmaier\|Chanfreau\|Benke\|Carlos\|CREATE\ SCHEMA' --include *.java -r -l | sort | uniq); do
  native2ascii -encoding UTF8 ${f} ${f}
done

%if %{with infinispan}
%pom_disable_module hibernate-infinispan
%endif

%if %{without spatial}
%pom_disable_module hibernate-spatial
%endif

%build

# Disabled beacuse of cyclic dep between core and testing modules
%mvn_build -s -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files core -f .mfiles-hibernate-core
%doc changelog.txt README.md migration-guide.adoc
%doc --no-dereference lgpl.txt LICENSE-2.0.txt

%files c3p0 -f .mfiles-hibernate-c3p0
%files ehcache -f .mfiles-hibernate-ehcache
%files entitymanager -f .mfiles-hibernate-entitymanager
%files envers -f .mfiles-hibernate-envers
%files hikaricp -f .mfiles-hibernate-hikaricp
%if %{without infinispan}
%files infinispan -f .mfiles-hibernate-infinispan
%endif
%files java8 -f .mfiles-hibernate-java8
%files osgi -f .mfiles-hibernate-osgi
%doc hibernate-osgi/README.md

%files parent -f .mfiles-hibernate-parent
%doc --no-dereference lgpl.txt LICENSE-2.0.txt

%files proxool -f .mfiles-hibernate-proxool

%if %{with spatial}
%files spatial -f .mfiles-hibernate-spatial
%doc --no-dereference hibernate-spatial/COPYRIGHT
%endif

%files testing -f .mfiles-hibernate-testing

%files javadoc -f .mfiles-javadoc
%doc --no-dereference lgpl.txt LICENSE-2.0.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.10-alt1_4jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 5.0.10-alt1_3jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 4.3.5-alt1_7jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 4.3.5-alt1_6jpp8
- unbootstrap build

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 4.3.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.7-alt1_6jpp7
- new version

