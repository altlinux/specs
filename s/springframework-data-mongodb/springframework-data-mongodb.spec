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
%define version 1.5.2
%global namedreltag .RELEASE
%global namedversion %{version}%{?namedreltag}
%global oname spring-data-mongodb

%if 0%{?fedora}
%bcond_with aspectj
# https://bugzilla.redhat.com/show_bug.cgi?id=1217162
%bcond_with test
%endif

Name:          springframework-data-mongodb
# Newer release require springframework >= 4.0.7.RELEASE
Version:       1.5.2
Release:       alt1_7jpp8
Summary:       MongoDB support for Spring Data
License:       ASL 2.0
URL:           http://projects.spring.io/spring-data-mongodb/
Source0:       https://github.com/spring-projects/spring-data-mongodb/archive/%{namedversion}.tar.gz

BuildRequires: maven-local
# https://jira.spring.io/browse/DATACMNS-670
BuildRequires: mvn(com.mysema.querydsl:querydsl-apt)
BuildRequires: mvn(com.mysema.querydsl:querydsl-mongodb)
BuildRequires: mvn(javax.annotation:jsr250-api)
BuildRequires: mvn(javax.enterprise:cdi-api)
BuildRequires: mvn(javax.validation:validation-api)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(net.sf.cglib:cglib)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.mongodb:mongo-java-driver:2)
BuildRequires: mvn(org.objenesis:objenesis)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.springframework:spring-expression)
BuildRequires: mvn(org.springframework:spring-tx)
BuildRequires: mvn(org.springframework.data:spring-data-commons)

# spring-data-mongodb-cross-store
%if %{with aspectj}
BuildRequires: mvn(org.aspectj:aspectjrt)
BuildRequires: mvn(org.aspectj:aspectjtools)
BuildRequires: mvn(org.codehaus.mojo:aspectj-maven-plugin)
BuildRequires: mvn(org.hibernate.javax.persistence:hibernate-jpa-2.0-api)
BuildRequires: mvn(org.springframework:spring-aspects)
BuildRequires: mvn(org.springframework:spring-orm)
%endif

# Test deps
%if %{with test}
BuildRequires: mvn(hsqldb:hsqldb:1)
BuildRequires: mvn(javax.el:el-api)
BuildRequires: mvn(javax.servlet:servlet-api)
BuildRequires: mvn(joda-time:joda-time)
BuildRequires: mvn(org.apache.openwebbeans.test:cditest-owb)
BuildRequires: mvn(org.hibernate:hibernate-entitymanager)
BuildRequires: mvn(org.hibernate:hibernate-validator)
# https://bugzilla.redhat.com/show_bug.cgi?id=1217162
BuildRequires: mvn(com.mysema.maven:apt-maven-plugin)
BuildRequires: mvn(org.slf4j:jul-to-slf4j)
%endif

BuildArch:     noarch
Source44: import.info

%description
The Spring Data MongoDB project provides integration with the
MongoDB document database. Key functional areas of Spring
Data MongoDB are a POJO centric model for interacting with a
MongoDB DBCollection and easily writing a Repository style
data access layer.

%package log4j
Group: Development/Java
Summary:       Spring Data MongoDB - Log4J Appender

%description log4j
Spring Data Mongo DB Log4J Appender.

%package parent
Group: Development/Java
Summary:       Spring Data MongoDB Parent POM

%description parent
Spring Data MongoDB Parent POM.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{namedversion}
sed -i 's/\r//' src/main/resources/*.txt
cp -p src/main/resources/*.txt .

# org.springframework.data.build:spring-data-parent:pom:1.4.2.RELEASE
%pom_remove_parent

%if %{without aspectj}
%pom_disable_module %{oname}-cross-store
%endif
%if %{without test}
%pom_remove_plugin com.mysema.maven:apt-maven-plugin %{oname}
%endif

%pom_disable_module %{oname}-distribution
%pom_remove_plugin :maven-assembly-plugin %{oname}-distribution
%pom_remove_plugin :wagon-maven-plugin %{oname}-distribution

# Fix version
%pom_xpath_set "pom:project/pom:properties/pom:mongo" 2
%pom_xpath_set "pom:project/pom:properties/pom:mongo.osgi" 2
%pom_xpath_set "pom:properties/pom:log4j" 1.2.17 %{oname}-log4j

%pom_change_dep :cdi-api ::1.0 %{oname}
%pom_change_dep :cditest-owb ::1.2.8 %{oname}
%pom_change_dep :querydsl-apt ::3.6.4 %{oname}
%pom_change_dep :querydsl-mongodb ::3.6.4 %{oname}
%pom_change_dep :el-api ::3.0.0 %{oname}
%pom_change_dep :joda-time ::2.8.1 %{oname}
%pom_change_dep :jul-to-slf4j ::1.7.12 %{oname}
%pom_change_dep :objenesis ::2.1 %{oname}
%pom_change_dep :validation-api ::1.1.0.Final %{oname}

# Remove internal cglib
find ./ -name "*.java" -exec sed -i "s/org.springframework.cglib/net.sf.cglib/g" {} +
%pom_add_dep net.sf.cglib:cglib


# Ass OSGi support
for p in %{oname} %{oname}-log4j; do
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>" ${p}
done

%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 %{oname} '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>org.springframework.data.mongodb</Bundle-SymbolicName>
    <Bundle-Name>Spring Data MongoDB Support</Bundle-Name>
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

%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 %{oname}-log4j '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>org.springframework.data.mongodb.log4j</Bundle-SymbolicName>
    <Bundle-Name>Spring Data Mongo DB Log4J Appender</Bundle-Name>
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

%build

%if %{without test}
opts="-f"
%endif
# Unavailable test deps
%mvn_build -s $opts -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles-%{oname}
%doc CONTRIBUTING.MD README.md changelog.txt
%doc license.txt notice.txt

%files log4j -f .mfiles-%{oname}-log4j
%doc %{oname}-log4j/README.md

%files parent -f .mfiles-%{oname}-parent
%doc license.txt notice.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_6jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_5jpp8
- new fc release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_3jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_1jpp8
- new version

