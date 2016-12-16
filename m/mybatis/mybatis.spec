Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# Started: Wed, 06 Jul 2016 13:50:35 UTC
# Terminated: Thu, 07 Jul 2016 06:37:46 UTC
#def_with test
%bcond_with test

Name:          mybatis
Version:       3.2.8
Release:       alt1_5jpp8
Summary:       SQL Mapping Framework for Java
License:       ASL 2.0
# http://code.google.com/p/mybatis/
URL:           http://www.mybatis.org/
Source0:       https://github.com/mybatis/mybatis-3/archive/%{name}-%{version}.tar.gz
# thanks to jhernand
# replace ognl ognl with apache-commons-ognl
Patch0:        %{name}-%{version}-commons-ognl.patch

BuildRequires: maven-local
BuildRequires: mvn(cglib:cglib)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.commons:commons-ognl)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.logging.log4j:log4j-core)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-site-plugin)
BuildRequires: mvn(org.javassist:javassist)
BuildRequires: mvn(org.mybatis:mybatis-parent:pom:)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)

%if %{with test}
# test deps
BuildRequires: mvn(commons-dbcp:commons-dbcp)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.derby:derby)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jta_1.1_spec)
BuildRequires: mvn(org.apache.geronimo.specs:specs:pom:)
BuildRequires: mvn(org.apache.velocity:velocity)
BuildRequires: mvn(org.hsqldb:hsqldb)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(postgresql:postgresql)
%endif

BuildArch:     noarch
Source44: import.info

%description
The MyBatis data mapper framework makes it easier
to use a relational database with object-oriented
applications. MyBatis couples objects with stored
procedures or SQL statements using a XML descriptor
or annotations. Simplicity is the biggest advantage
of the MyBatis data mapper over object relational
mapping tools.

To use the MyBatis data mapper, you rely on your
own objects, XML, and SQL. There is little to
learn that you don't already know. With the
MyBatis data mapper, you have the full power of
both SQL and stored procedures at your fingertips. 

The MyBatis project is developed and maintained by
a team that includes the original creators of the
"iBATIS" data mapper. The Apache project was retired
and continued here.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-3-%{name}-%{version}

%patch0 -p1
%pom_remove_plugin :maven-pdf-plugin
%pom_remove_plugin :jarjar-maven-plugin
%pom_remove_plugin :cobertura-maven-plugin

sed -i 's/\r//' LICENSE NOTICE

%if %{with test}
%pom_remove_dep javax.transaction:transaction-api
%pom_add_dep org.apache.geronimo.specs:geronimo-jta_1.1_spec::test

# Fails on java8
rm src/test/java/org/apache/ibatis/parsing/GenericTokenParserTest.java

rm src/test/java/org/apache/ibatis/submitted/multipleresultsetswithassociation/MultipleResultSetTest.java \
 src/test/java/org/apache/ibatis/submitted/includes/IncludeTest.java \
 src/test/java/org/apache/ibatis/submitted/resultmapwithassociationstest/ResultMapWithAssociationsTest.java \
 src/test/java/org/apache/ibatis/submitted/nestedresulthandler_association/NestedResultHandlerAssociationTest.java

rm src/test/java/org/apache/ibatis/logging/LogFactoryTest.java
%endif

%mvn_file :%{name} %{name}

%build
# Test suite skipped

%if %{without test}
opts="-f"
%endif
%mvn_build $opts -- -Dproject.build.sourceEncoding=UTF-8
 
%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt1_5jpp8
- new fc release

* Mon Nov 28 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt1_4jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt1_3jpp8
- java 8 mass update

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

