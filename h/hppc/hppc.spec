Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          hppc
Version:       0.6.1
Release:       alt1_3jpp8
Summary:       High Performance Primitive Collections for Java
License:       ASL 2.0
URL:           http://labs.carrotsearch.com/hppc.html
Source0:       https://github.com/carrotsearch/hppc/archive/%{version}.tar.gz

BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-junit)
BuildRequires: mvn(org.apache.velocity:velocity)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

%if 0
# hppc-benchmarks deps
# http://gil.fedorapeople.org/caliper-1.0-0.1.20120909SNAPSHOT.fc16.src.rpm
BuildRequires: mvn(com.google.caliper:caliper:0.5-rc1)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(com.h2database:h2)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(it.unimi.dsi:fastutil)
# http://gil.fedorapeople.org/trove-3.0.3-1.fc16.src.rpm
BuildRequires: mvn(net.sf.trove4j:trove4j:3.0.3)
BuildRequires: mvn(org.apache.mahout:mahout-collections)

# test deps
BuildRequires: mvn(com.carrotsearch:junit-benchmarks)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(com.carrotsearch.randomizedtesting:junit4-maven-plugin)
BuildRequires: mvn(com.carrotsearch.randomizedtesting:randomizedtesting-runner)
%endif

BuildRequires: maven-local
BuildRequires: maven-antrun-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-build-helper

BuildArch:     noarch
Source44: import.info

%description
Fundamental data structures (maps, sets, lists, stacks, queues) generated for
combinations of object and primitive types to conserve JVM memory and speed
up execution.

%package templateprocessor
Group: Development/Java
Summary:       HPPC Template Processor

%description templateprocessor
Template Processor and Code Generation for HPPC.

%package javadoc
Group: Development/Java
Summary:       Javadoc for HPPC
BuildArch: noarch

%description javadoc
This package contains javadoc for HPPC.

%prep
%setup -q
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

# remove ant-trax and ant-nodeps, fix jdk tools JAR location
%pom_xpath_remove "pom:project/pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId = 'maven-antrun-plugin']/pom:dependencies/pom:dependency[pom:groupId = 'org.apache.ant']"
%pom_xpath_inject "pom:project/pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId = 'maven-antrun-plugin']/pom:dependencies" "
<dependency>
  <groupId>org.apache.ant</groupId>
  <artifactId>ant</artifactId>
  <version>1.8.0</version>
</dependency>
<dependency>
  <groupId>org.apache.ant</groupId>
  <artifactId>ant-junit</artifactId>
  <version>1.8.0</version>
</dependency>
<dependency>
  <groupId>com.sun</groupId>
  <artifactId>tools</artifactId>
  <version>1.7.0</version>
</dependency>"

# Unavailable deps
%pom_disable_module %{name}-benchmarks
%pom_disable_module %{name}-examples

%pom_remove_plugin :findbugs-maven-plugin

%pom_remove_plugin :junit4-maven-plugin %{name}-core

sed -i 's/\r//' CHANGES

%mvn_file :%{name} %{name}
%mvn_file :%{name}-templateprocessor %{name}-templateprocessor
%mvn_package :%{name}-templateprocessor %{name}-templateprocessor

%build

# Disable test for now. Unavailable test deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc CHANGES README
%doc LICENSE

%files templateprocessor -f .mfiles-%{name}-templateprocessor
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_3jpp8
- java 8 mass update

