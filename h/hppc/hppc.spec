Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          hppc
Version:       0.7.1
Release:       alt1_3jpp8
Summary:       High Performance Primitive Collections for Java
License:       ASL 2.0
URL:           http://labs.carrotsearch.com/hppc.html
Source0:       https://github.com/carrotsearch/hppc/archive/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-junit)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.velocity:velocity)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(org.antlr:antlr4)
BuildRequires: mvn(org.antlr:antlr4-maven-plugin)

%if 0
# hppc-benchmarks deps
BuildRequires: mvn(it.unimi.dsi:fastutil)
BuildRequires: mvn(net.openhft:koloboke-impl-jdk6-7:0.6.6)
BuildRequires: mvn(org.openjdk.jmh:jmh-core)
BuildRequires: mvn(org.openjdk.jmh:jmh-generator-annprocess)

# test deps
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(com.carrotsearch.randomizedtesting:junit4-maven-plugin)
BuildRequires: mvn(com.carrotsearch.randomizedtesting:randomizedtesting-runner)
BuildRequires: mvn(org.assertj:assertj-core)
%endif

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

# Unavailable deps
%pom_disable_module %{name}-benchmarks
%pom_remove_plugin :junit4-maven-plugin
%pom_remove_plugin :forbiddenapis
%pom_remove_plugin :junit4-maven-plugin hppc
# Unneeded task
%pom_remove_plugin -r :maven-assembly-plugin

# Convert from dos to unix line ending
for file in CHANGES.txt; do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm $file.orig
done

%mvn_file :%{name} %{name}
%mvn_package :%{name}::esoteric:
%mvn_file :%{name}-template-processor %{name}-templateprocessor
%mvn_package :%{name}-template-processor %{name}-templateprocessor

%build

# Disable test for now. Unavailable test deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.txt README.txt
%doc LICENSE.txt NOTICE.txt

%files templateprocessor -f .mfiles-%{name}-templateprocessor
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_3jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_3jpp8
- java 8 mass update

