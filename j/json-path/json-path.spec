Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          json-path
Version:       2.1.0
Release:       alt1_4jpp8
Summary:       Java JsonPath implementation
# Some files in src/main/java/com/jayway/jsonassert/impl/matcher/ are licensed under BSD
License:       ASL 2.0 and BSD
URL:           https://github.com/jayway/JsonPath
Source0:       https://github.com/jayway/JsonPath/archive/%{name}-%{version}.tar.gz
# Too many unavailable plugins for use gradle
Source1:       http://central.maven.org/maven2/com/jayway/jsonpath/json-path/%{version}/json-path-%{version}.pom
Source2:       http://central.maven.org/maven2/com/jayway/jsonpath/json-path-assert/%{version}/json-path-assert-%{version}.pom
# Remove json.org support
Patch0:        %{name}-2.1.0-JsonOrg.patch

BuildRequires: maven-local
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.minidev:json-smart)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.hamcrest:hamcrest-library)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-simple)

BuildArch:     noarch
Source44: import.info

%description
Java DSL for reading and testing JSON documents.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n JsonPath-%{name}-%{version}
find -type f -name *.jar -print -delete
find -type f -name *.class -print -delete

cp -p %{SOURCE1} %{name}/pom.xml
cp -p %{SOURCE2} %{name}-assert/pom.xml

%patch0 -p1
rm -rf %{name}/src/main/java/com/jayway/jsonpath/spi/json/JsonOrg*.java \
 %{name}/src/main/java/com/jayway/jsonpath/spi/mapper/JsonOrg*.java \
 %{name}/src/test/java/com/jayway/jsonpath/JsonOrg*.java
%pom_remove_dep org.json:json %{name}

# This is a dummy POM added just to ease building in the RPM platforms
cat > pom.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<project
  xmlns="http://maven.apache.org/POM/4.0.0"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <modelVersion>4.0.0</modelVersion>
  <groupId>com.jayway.jsonpath</groupId>
  <artifactId>%{name}-parent</artifactId>
  <version>%{version}</version>
  <packaging>pom</packaging>
  <name>Java JsonPath implementation</name>
  <modules>
    <module>%{name}</module>
    <module>%{name}-assert</module>
  </modules>
</project>
EOF
# Add OSGi support
for p in %{name} %{name}-assert ;do
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>" ${p}
%pom_add_plugin "org.apache.maven.plugins:maven-jar-plugin:2.4" ${p} "
<configuration>
  <archive>
    <manifest>
      <addDefaultImplementationEntries>true</addDefaultImplementationEntries>
    </manifest>
  </archive>
</configuration>"
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 ${p} '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>${project.groupId}.${project.artifactId}</Bundle-SymbolicName>
    <Bundle-Name>${project.name}</Bundle-Name>
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
done

# Fix test deps
%pom_add_dep junit:junit:4.12:test %{name}
%pom_add_dep org.assertj:assertj-core:2.1.0:test %{name}
%pom_add_dep org.hamcrest:hamcrest-library:1.3:test %{name}
%pom_add_dep junit:junit:4.12:test %{name}-assert

# fix non ASCII chars
for s in %{name}/src/test/java/com/jayway/jsonpath/old/internal/ScanPathTokenTest.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

%mvn_file :%{name} %{name}
%mvn_file :%{name}-assert %{name}-assert
%mvn_package :%{name}-parent __noinstall

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_8jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_6jpp8
- unbootsrap build

