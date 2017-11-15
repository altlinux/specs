Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.8.4
%global namedreltag .RELEASE
%global namedversion %{version}%{?namedreltag}
%global oname spring-data-commons

Name:          springframework-data-commons
Version:       1.8.4
Release:       alt1_9jpp8
Summary:       Interfaces between relational and non-relational data stores
License:       ASL 2.0
URL:           http://projects.spring.io/spring-data/
# Newer release require springframework >= 4.0.7.RELEASE
Source0:       https://github.com/spring-projects/spring-data-commons/archive/%{namedversion}.tar.gz


BuildRequires: maven-local
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.mysema.querydsl:querydsl-apt)
BuildRequires: mvn(com.mysema.querydsl:querydsl-core)
BuildRequires: mvn(javax.annotation:jsr250-api)
BuildRequires: mvn(javax.ejb:ejb-api)
BuildRequires: mvn(javax.enterprise:cdi-api)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(joda-time:joda-time)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.springframework:spring-expression)
BuildRequires: mvn(org.springframework:spring-oxm)
BuildRequires: mvn(org.springframework:spring-tx)
BuildRequires: mvn(org.springframework:spring-web)
BuildRequires: mvn(org.springframework:spring-webmvc)
BuildRequires: mvn(org.springframework.hateoas:spring-hateoas)

%if 0
# Test deps
# https://bugzilla.redhat.com/show_bug.cgi?id=1217162
BuildRequires: mvn(com.mysema.maven:apt-maven-plugin)
BuildRequires: mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires: mvn(javax.el:javax.el-api)
BuildRequires: mvn(org.apache.openwebbeans.test:cditest-owb)
BuildRequires: mvn(org.codehaus.groovy:groovy-all:1.8.6)
BuildRequires: mvn(xmlunit:xmlunit)
%endif

BuildArch:     noarch
Source44: import.info

%description
Spring Data Commons is part of the umbrella Spring Data project that
provides shared infrastructure across the Spring Data projects. Most
importantly at the moment it contains technology neutral repository
interfaces as well as a meta-data model for persisting Java classes.

Features:
A. Powerful Repository and custom object-mapping abstractions
A. Support for cross-store persistence
A. Dynamic query generation from query method names
A. Implementation domain base classes providing basic properties
A. Support for transparent auditing (created, last changed)
A. Possibility to integrate custom repository code
A. Easy Spring integration with custom name-space

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{namedversion}

cp -p src/main/resources/*.txt .
sed -i 's/\r//' *.txt

# https://github.com/spring-projects/spring-data-build
%pom_remove_parent
# Remove unavailable plugins
%pom_remove_plugin :apt-maven-plugin
%pom_remove_plugin :wagon-maven-plugin
# Remove unwanted plugin
%pom_remove_plugin :maven-assembly-plugin

# Set dependecies version (available in parent pom)
%pom_xpath_set "pom:dependency[pom:groupId='com.fasterxml.jackson.core']/pom:version" 2.5.0
%pom_xpath_set "pom:dependency[pom:groupId='javax.enterprise']/pom:version" 1.1
%pom_xpath_set "pom:dependency[pom:groupId='joda-time']/pom:version" 2.3
%pom_xpath_set "pom:dependency[pom:groupId='org.apache.openwebbeans.test']/pom:version" 1.2.0
%pom_xpath_set "pom:dependency[pom:groupId='com.mysema.querydsl']/pom:version" 3.6.4

# Force EL 3.0 apis
%pom_xpath_set "pom:dependency[pom:groupId='javax.el']/pom:artifactId" javax.el-api
%pom_xpath_set "pom:dependency[pom:groupId='javax.el']/pom:version" 3.0.0
# Force servlet 3.1 apis
%pom_xpath_set "pom:dependency[pom:groupId='javax.servlet']/pom:artifactId" javax.servlet-api
%pom_xpath_set "pom:dependency[pom:groupId='javax.servlet']/pom:version" 3.1.0

# Use jvm apis (java.util.Optional)
%pom_remove_dep org.springframework.data.build:spring-data-java8-stub

# Add OSGi support
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
%pom_add_plugin org.apache.felix:maven-bundle-plugin . '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>org.springframework.data.core</Bundle-SymbolicName>
    <Bundle-Name>${project.name}</Bundle-Name>
    <Bundle-Vendor>Pivotal Software, Inc.</Bundle-Vendor>
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

%mvn_file : %{oname}

%build

# Unavailable test deps
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc changelog.txt readme.*
%doc license.txt notice.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.txt

%changelog
* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt1_9jpp8
- fc update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt1_8jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt1_7jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt1_6jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt1_5jpp8
- new version

