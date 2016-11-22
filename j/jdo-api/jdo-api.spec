Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jdo-api
%define version 3.1
%global namedreltag -rc1
%global namedversion %{version}%{?namedreltag}
Name:          jdo-api
Version:       3.1
Release:       alt1_0.8.rc1jpp8
Summary:       JDO 3.1 API
License:       ASL 2.0
URL:           http://db.apache.org/jdo/
# svn export http://svn.apache.org/repos/asf/db/jdo/tags/3.1-rc1/ jdo-api-3.1-rc1
# find jdo-api-3.1-rc1/ -name "*.jar" -delete
# find jdo-api-3.1-rc1/ -name "*.class" -delete
# tar cJf jdo-api-3.1-rc1.tar.xz jdo-api-3.1-rc1
Source0:       %{name}-%{namedversion}.tar.xz


BuildRequires: mvn(javax.transaction:jta)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components:pom:)

%if 0
# copy-jdori-jars module deps
BuildRequires: mvn(com.mchange:c3p0)
BuildRequires: mvn(log4j:log4j)
# Circular deps
BuildRequires: mvn(org.datanucleus:datanucleus-api-jdo)
BuildRequires: mvn(org.datanucleus:datanucleus-api-jpa)
BuildRequires: mvn(org.datanucleus:datanucleus-core)
BuildRequires: mvn(org.datanucleus:datanucleus-rdbms)
# jdo-exectck module deps
BuildRequires: mvn(commons-collections:commons-collections)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.derby:derby)
BuildRequires: mvn(org.apache.derby:derbytools)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.springframework:spring-beans)
# jdo-tck module deps
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(org.hibernate.javax.persistence:hibernate-jpa-2.0-api)
%endif

# Test deps
BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: maven-remote-resources-plugin
BuildRequires: maven-site-plugin

BuildArch:     noarch
Source44: import.info

%description
The Java Data Objects (JDO) API is a standard interface
based Java model abstraction of persistence, developed as
Java Specification Requests (JSR 12 and 243) under the
auspices of the Java Community Process.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'javax.transaction' ]/pom:artifactId" jta parent-pom
%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'javax.transaction' ]/pom:artifactId" jta api
%pom_remove_plugin :maven-source-plugin api

%if 0
%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'javax.transaction' ]/pom:artifactId" jta tck
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'c3p0' ]/pom:groupId" com.mchange copyjdorijars
%pom_change_dep org.apache.geronimo.specs:geronimo-jpa_2.0_spec org.hibernate.javax.persistence:hibernate-jpa-2.0-api tck
%pom_change_dep org.apache.geronimo.specs:geronimo-jpa_2.0_spec org.hibernate.javax.persistence:hibernate-jpa-2.0-api exectck
%endif

%pom_disable_module copyjdorijars
%pom_disable_module exectck
%pom_disable_module tck

# unavailable test resources
rm -r api/test/java/javax/jdo/EnhancerTest.java \
 api/test/java/javax/jdo/PMFMapMapTest.java

%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.html
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_0.8.rc1jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_0.7.rc1jpp8
- unbootsrap build

