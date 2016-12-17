Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          morphia
Version:       1.0.1
Release:       alt1_4jpp8
Summary:       A type-safe Java library for MongoDB
License:       ASL 2.0
URL:           https://github.com/mongodb/morphia
Source0:       https://github.com/mongodb/morphia/archive/r%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(cglib:cglib)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.inject:guice)
BuildRequires: mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires: mvn(com.thoughtworks.proxytoys:proxytoys)
BuildRequires: mvn(commons-collections:commons-collections)
BuildRequires: mvn(javax.validation:validation-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires: mvn(org.mongodb:mongo-java-driver:2)
BuildRequires: mvn(org.reflections:reflections)
BuildRequires: mvn(org.scannotation:scannotation)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-jdk14)
BuildRequires: mvn(org.slf4j:slf4j-simple)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(dom4j:dom4j)
%if 0
# Test deps
BuildRequires: mvn(org.hibernate:hibernate-validator:4.1.0.Final)
%endif

BuildArch:     noarch
Source44: import.info

%description
Morphia is a lightweight type-safe library for mapping Java
objects to/from MongoDB. Morphia provides a type-safe, and
fluent Query API support with (run-time) validation. Morphia
uses annotations so there are no XML files to manage or update.
Morphia should feel very comfortable for any developer
with JPA experience.

%package entityscanner-plug
Group: Development/Java
Summary:       EntityScanner Plugin

%description entityscanner-plug
Morphia EntityScanner Plugin.

%package guice-plug
Group: Development/Java
Summary:       Guice Plugin

%description guice-plug
Morphia Guice Plugin.

%package logging-slf4j
Group: Development/Java
Summary:       Logging via SLF4J

%description logging-slf4j
Morphia Logging via SLF4J.

%package parent
Group: Development/Java
Summary:       Morphia Parent POM

%description parent
Build Project for Morphia.

%package validation
Group: Development/Java
Summary:       JSR303 Validation

%description validation
Morphia JSR303 Validation.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-r%{version}
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

rm -r %{name}/src/main/java/relocated
%pom_add_dep commons-collections:commons-collections:3.2.1
sed -i "s|relocated.morphia.||" $(find %{name} -name "*.java")

%pom_remove_plugin :gwt-maven-plugin
%pom_remove_plugin :maven-license-plugin
%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-javadoc-plugin']/pom:executions"

%pom_disable_module no-proxy-deps-tests

%pom_xpath_set "pom:project/pom:version" %{version}
%pom_xpath_set "pom:parent/pom:version" %{version} entityscanner-plug
%pom_xpath_set "pom:parent/pom:version" %{version} guice-plug
%pom_xpath_set "pom:parent/pom:version" %{version} logging-slf4j
%pom_xpath_set "pom:parent/pom:version" %{version} %{name}
%pom_xpath_set "pom:parent/pom:version" %{version} validation

%pom_xpath_set "pom:project/pom:properties/pom:java-driver.version" 2

%pom_change_dep cglib: :cglib %{name}
%pom_change_dep :scannotation org.scannotation: entityscanner-plug
%pom_change_dep com.google.collections:google-collections com.google.guava:guava:18.0 entityscanner-plug

%pom_remove_plugin :maven-shade-plugin entityscanner-plug

# Add OSGi manifest
for p in entityscanner-plug guice-plug logging-slf4j validation; do
  %pom_xpath_set "pom:packaging" bundle ${p}
  %pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 ${p} '
    <extensions>true</extensions>
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

%build

# Tests require web access
%mvn_build -sf

%install
%mvn_install

%files -f .mfiles-%{name}
%doc CONTRIBUTING.md README.md
%doc %{name}/LICENSE.txt

%files entityscanner-plug -f .mfiles-%{name}-entityscanner-plug
%doc LICENSE

%files guice-plug -f .mfiles-%{name}-guice-plug
%doc LICENSE

%files logging-slf4j -f .mfiles-%{name}-logging-slf4j
%doc LICENSE

%files parent -f .mfiles-%{name}-parent
%doc LICENSE

%files validation -f .mfiles-%{name}-validation
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc %{name}/LICENSE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_4jpp8
- new fc release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1jpp8
- new version

