BuildRequires: maven-assembly-plugin
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 5.5.4
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          hibernate-search
Version:       5.5.4
Release:       alt2_2jpp8
Summary:       Hibernate Search
License:       LGPLv2+
URL:           http://hibernate.org/search/
Source0:       https://github.com/hibernate/hibernate-search/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.puppycrawl.tools:checkstyle)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(java_cup:java_cup)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:12)
BuildRequires: mvn(org.apache.avro:avro)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.lucene:lucene-analyzers-common)
BuildRequires: mvn(org.apache.lucene:lucene-analyzers-phonetic)
BuildRequires: mvn(org.apache.lucene:lucene-backward-codecs)
BuildRequires: mvn(org.apache.lucene:lucene-core) >= 5.3.1
BuildRequires: mvn(org.apache.lucene:lucene-facet)
BuildRequires: mvn(org.apache.lucene:lucene-misc)
BuildRequires: mvn(org.apache.lucene:lucene-queryparser)
BuildRequires: mvn(org.apache.maven.plugins:maven-checkstyle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.pdfbox:pdfbox)
BuildRequires: mvn(org.apache.tika:tika-core)
BuildRequires: mvn(org.bsc.maven:maven-processor-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.hibernate:hibernate-core) >= 5.0.7
BuildRequires: mvn(org.hibernate:hibernate-entitymanager)
BuildRequires: mvn(org.hibernate:hibernate-envers)
BuildRequires: mvn(org.hibernate:hibernate-testing)
BuildRequires: mvn(org.hibernate.common:hibernate-commons-annotations) >= 5.0.1
BuildRequires: mvn(org.hibernate.javax.persistence:hibernate-jpa-2.1-api)
BuildRequires: mvn(org.jboss.byteman:byteman)
BuildRequires: mvn(org.jboss.byteman:byteman-bmunit)
BuildRequires: mvn(org.jboss.byteman:byteman-install)
BuildRequires: mvn(org.jboss.logging:jboss-logging)
BuildRequires: mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires: mvn(org.jboss.maven.plugins:maven-injection-plugin)
BuildRequires: mvn(org.jboss.spec.javax.jms:jboss-jms-api_2.0_spec)
BuildRequires: mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.2_spec)
BuildRequires: mvn(org.jgroups:jgroups) >= 3.6.6
BuildRequires: mvn(simple-jndi:simple-jndi)
BuildRequires: xmvn

BuildArch:     noarch
Source44: import.info

%description
Full text search engines like Apache Lucene are very powerful technologies to
add efficient free text search capabilities to applications. However, Lucene
suffers several mismatches when dealing with object domain models. Amongst
other things indexes have to be kept up to date and mismatches between index
structure and domain model as well as query mismatches have to be avoided.

Hibernate Search addresses these shortcomings - it indexes your domain model
with the help of a few annotations, takes care of database/index
synchronization and brings back regular managed objects from free text queries.

Hibernate Search is using Apache Lucene under the cover.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
rm -rf orm/src/test/resources/org/hibernate/search/test/bridge/tika/

%pom_disable_module integrationtest/jms
%pom_disable_module integrationtest/narayana
%pom_disable_module integrationtest/spring
%pom_disable_module integrationtest/wildfly
%pom_disable_module integrationtest/performance
%pom_disable_module integrationtest/osgi/karaf-features
%pom_disable_module integrationtest/osgi/karaf-it
%pom_disable_module integrationtest/sandbox
%pom_disable_module integrationtest/engine-performance
%pom_disable_module distribution
%pom_disable_module documentation
# This component is now owned and maintained by the Infinispan team:
# org.infinispan:infinispan-directory-provider:8.0.1.Final
%pom_disable_module infinispan
%pom_disable_module legacy

# hibernate-search-engine, hibernate-search-orm
%pom_xpath_remove "pom:dependency[pom:type = 'test-jar']" testing

%pom_remove_plugin ":maven-enforcer-plugin"
# de.thetaphi:forbiddenapis:1.8
%pom_remove_plugin -r :forbiddenapis

%pom_remove_dep org.apache.tika:tika-core
%pom_change_dep -r "org.apache.tika:tika-parsers" "org.apache.tika:tika-core"
%pom_change_dep -r :log4j ::12

# org.easytesting:fest-assert:1.4
%pom_remove_dep -r :fest-assert
# org.unitils:unitils-easymock:3.3
%pom_remove_dep -r :unitils-easymock

%mvn_alias :hibernate-search-orm :hibernate-search

%build
# NO test deps see above
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc changelog.txt README.md
%doc lgpl.txt

%files javadoc -f .mfiles-javadoc
%doc lgpl.txt

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 5.5.4-alt2_2jpp8
- added BR: maven-assembly-plugin for javapackages 5

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 5.5.4-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 4.5.1-alt1_6jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 4.5.1-alt1_5jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 4.5.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

