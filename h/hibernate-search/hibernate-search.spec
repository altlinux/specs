Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name hibernate-search
%define version 4.5.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

# Use this switch to rebuild without infinispan
# This is useful to break the hibernate-search circular dependency
%define with_infinispan 1

Name:             hibernate-search
Version:          4.5.1
Release:          alt1_6jpp8
Summary:          Hibernate Search
License:          LGPLv2+
Url:              http://search.hibernate.org

# wget https://github.com/hibernate/hibernate-search/archive/4.5.1.Final.tar.gz
# tar -xf 4.5.1.Final.tar.gz
# rm -rf hibernate-search-4.5.1.Final/orm/src/test/resources/org/hibernate/search/test/bridge/tika/
# tar -cvjf hibernate-search-4.5.1.Final-CLEAN.tar.gz hibernate-search-4.5.1.Final/
Source0:          hibernate-search-%{namedversion}-CLEAN.tar.gz

BuildRequires:    maven-local
BuildRequires:    jboss-logging
BuildRequires:    jboss-logging-tools
BuildRequires:    avro
BuildRequires:    jgroups
BuildRequires:    slf4j
BuildRequires:    jboss-transaction-1.1-api

%if 0%{?fedora} >= 21
BuildRequires:    lucene3
BuildRequires:    lucene3-contrib
%else
BuildRequires:    lucene
BuildRequires:    lucene-contrib
%endif

BuildRequires:    solr3

BuildRequires:    h2
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-processor-plugin
BuildRequires:    maven-injection-plugin
BuildRequires:    byteman
BuildRequires:    hibernate-commons-annotations
BuildRequires:    hibernate-jpa-2.1-api
BuildRequires:    hibernate-core >= 4.3.1
BuildRequires:    geronimo-jta
BuildRequires:    junit
BuildRequires:    tika

%if %{with_infinispan}
BuildRequires:    infinispan
%endif

BuildArch:        noarch
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
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n hibernate-search-%{namedversion}

%pom_disable_module integrationtest/wildfly
%pom_disable_module integrationtest/spring
%pom_disable_module integrationtest/narayana
%pom_disable_module testing
%pom_disable_module modules
%pom_disable_module legacy

%if !%{with_infinispan}
%pom_disable_module infinispan
%endif

%pom_remove_plugin ":maven-enforcer-plugin"

%pom_remove_dep "org.apache.tika:tika-parsers" engine/pom.xml
%pom_add_dep "org.apache.tika:tika-core" engine/pom.xml

sed -i "s|luceneVersion>3.6.2</luceneVersion|luceneVersion>3</luceneVersion|" pom.xml

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc lgpl.txt README.md

%files javadoc -f .mfiles-javadoc
%doc lgpl.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 4.5.1-alt1_6jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 4.5.1-alt1_5jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 4.5.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

