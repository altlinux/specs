Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 0.16.0
%global namedreltag .RELEASE
%global namedversion %{version}%{?namedreltag}
%global oname spring-hateoas
Name:          springframework-hateoas
Version:       0.16.0
Release:       alt1_7jpp8
Summary:       Representations for hyper-text driven REST web services
License:       ASL 2.0
URL:           http://github.com/SpringSource/spring-hateoas
# Newer release require springframework >= 4.0.9.RELEASE
Source0:       https://github.com/spring-projects/spring-hateoas/archive/%{namedversion}.tar.gz
Patch0:        springframework-hateoas-0.16.0-jackson2.7.patch

BuildRequires: maven-local
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.jayway.jsonpath:json-path)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(javax.ws.rs:jsr311-api)
BuildRequires: mvn(net.sf.cglib:cglib)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.atteo:evo-inflector)
BuildRequires: mvn(org.objenesis:objenesis)
# BuildRequires: mvn(org.projectlombok:lombok:1.14.4) @  https://github.com/rzwitserloot/lombok/
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.springframework:spring-aop)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.springframework:spring-web)
BuildRequires: mvn(org.springframework:spring-webmvc)
BuildRequires: mvn(org.springframework.plugin:spring-plugin-core)
%if 0
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(joda-time:joda-time)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.jadler:jadler-all)
BuildRequires: mvn(org.hamcrest:hamcrest-library)
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
BuildRequires: mvn(org.springframework:spring-test)
BuildRequires: mvn(xmlunit:xmlunit)
%endif

BuildArch:     noarch
Source44: import.info

%description
This project provides some APIs to ease creating REST representations that
follow the HATEOAS principle when working with Spring and especially Spring
MVC. The core problem it tries to address is link creation and representation
assembly.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{namedversion}

cp -p src/main/resources/changelog.txt .
cp -p src/main/resources/license.txt .
cp -p src/main/resources/notice.txt .
sed -i 's/\r//' *.txt readme.md

%patch0 -p1

%pom_remove_plugin :com.springsource.bundlor.maven
%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"

%pom_change_dep :servlet-api javax.servlet:javax.servlet-api:3.1.0

find ./ -name "*.java" -exec sed -i "s/org.springframework.cglib/net.sf.cglib/g" {} +
%pom_add_dep net.sf.cglib:cglib

%pom_remove_plugin :maven-jar-plugin
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
%pom_add_plugin org.apache.felix:maven-bundle-plugin . '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>org.springframework.hateoas</Bundle-SymbolicName>
    <Bundle-Name>Spring HATEOAS</Bundle-Name>
    <Bundle-Vendor>SpringSource</Bundle-Vendor>
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

# org.projectlombok:lombok:jar:1.14.4
%pom_remove_dep org.projectlombok:lombok
rm -r src/main/java/org/springframework/hateoas/alps/Alps.java \
 src/main/java/org/springframework/hateoas/alps/Descriptor.java \
 src/main/java/org/springframework/hateoas/alps/Doc.java \
 src/main/java/org/springframework/hateoas/alps/Ext.java

%mvn_file : %{oname}

%build

# Unavailable test deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc changelog.txt readme.md
%doc license.txt notice.txt 

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_6jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_5jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_3jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_2jpp8
- new version

