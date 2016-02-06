Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          randomizedtesting
Version:       2.1.3
Release:       alt1_3jpp8
Summary:       Java Testing Framework
License:       ASL 2.0
URL:           http://labs.carrotsearch.com/randomizedtesting.html
Source0:       https://github.com/carrotsearch/randomizedtesting/archive/release/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(asm:asm)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(dom4j:dom4j)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires: mvn(org.hamcrest:hamcrest-core)
BuildRequires: mvn(org.simpleframework:simple-xml)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(stax:stax-api)
%if 0
# junit4-ant build tools
BuildRequires: mvn(net.sf.proguard:proguard)
BuildRequires: proguard-maven-plugin
# Test deps
BuildRequires: mvn(org.easytesting:fest-assert-core) >= 2.0M6
%endif

Requires:      maven-local
BuildArch:     noarch
Source44: import.info

%description
Foundation classes and rules for applying the
principles of Randomized Testing.

%package junit4-ant
Group: Development/Java
Summary:       RandomizedTesting JUnit4 ANT Task
Requires:      %{name} = %{version}

%description junit4-ant
RandomizedTesting JUnit4 ANT Task.

%package junit4-maven-plugin
Group: Development/Java
Summary:       RandomizedTesting JUnit4 Maven Plugin
Requires:      %{name} = %{version}

%description junit4-maven-plugin
RandomizedTesting JUnit4 Maven Plugin.

%package runner
Group: Development/Java
Summary:       RandomizedTesting Randomized Runner
Requires:      %{name} = %{version}

%description runner
RandomizedRunner is a JUnit runner, so it is capable of
running @Test-annotated test cases.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-release-%{version}
find . -name "*.class" -delete
find . -name "*.jar" -delete
find . -name "*.dll" -delete
find . -name "*.dylib" -delete
find . -name "*.so" -delete

# Remove bundled JavaScript libraries
find . -name "*.js" -print -delete
sed -i '/jquery/d' \
 junit4-ant/src/main/resources/com/carrotsearch/ant/tasks/junit4/templates/json/index.html \
 junit4-ant/src/main/java/com/carrotsearch/ant/tasks/junit4/listeners/json/JsonReport.java
sed -i '/script.js/d' \
 junit4-ant/src/main/resources/com/carrotsearch/ant/tasks/junit4/templates/json/index.html \
 junit4-ant/src/main/java/com/carrotsearch/ant/tasks/junit4/listeners/json/JsonReport.java

%pom_remove_dep org.easytesting:fest-assert-core randomized-runner

%pom_disable_module examples/maven
%pom_disable_module examples/ant
%pom_disable_module packaging
%pom_disable_module junit4-maven-plugin-tests
# Disable repackaged and shaded deps
%pom_remove_plugin com.pyx4me:proguard-maven-plugin junit4-ant
%pom_remove_plugin org.codehaus.mojo:exec-maven-plugin junit4-ant
%pom_remove_plugin :maven-dependency-plugin junit4-ant
# Fix deps scope
%pom_xpath_remove "pom:scope[text()='provided']" junit4-ant
sed -i 's/\r//' README randomized-runner/README

# package org.hamcrest does not exist
%pom_add_dep org.hamcrest:hamcrest-core randomized-runner

%pom_remove_plugin :maven-plugin-plugin
%pom_xpath_inject "pom:plugin[pom:artifactId = 'maven-plugin-plugin']" \
  "<configuration>
    <skipErrorNoDescriptorsFound>true</skipErrorNoDescriptorsFound>
  </configuration>" junit4-maven-plugin


%mvn_package :%{name}-parent %{name}-runner

%build

# Requires org.easytesting:fest-assert-core >= 2.0M6
%mvn_build -f -s

%install
%mvn_install

%files
%dir %{_javadir}/%{name}
%doc README
%doc LICENSE

%files junit4-ant -f .mfiles-junit4-ant

%files junit4-maven-plugin -f .mfiles-junit4-maven-plugin

%files runner -f .mfiles-%{name}-runner
%doc randomized-runner/README

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.3-alt1_3jpp8
- java 8 mass update

