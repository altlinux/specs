Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global oname mustache.java
Name:          mustache-java
Version:       0.9.1
Release:       alt1_2jpp8
Summary:       Implementation of mustache.js for Java
License:       ASL 2.0
URL:           https://github.com/spullara/mustache.java/
Source0:       https://github.com/spullara/mustache.java/archive/%{oname}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.github.spullara.cli-parser:cli-parser)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires: mvn(org.eclipse.jetty:jetty-server)
BuildRequires: mvn(org.openjdk.jmh:jmh-core)
BuildRequires: mvn(org.openjdk.jmh:jmh-generator-annprocess)
BuildRequires: mvn(org.ow2.asm:asm-commons)
BuildRequires: mvn(org.ow2.asm:asm-util)

%if 0
BuildRequires: mvn(com.twitter:util-core_2.10:6.25.0)
BuildRequires: mvn(org.scala-lang:scala-library:2.10.4)
BuildRequires: mvn(com.twitter:util-core_2.11:6.23.0)
BuildRequires: mvn(org.scala-lang:scala-library:2.11.4)
BuildRequires: mvn(org.scala-tools:maven-scala-plugin:2.14.1)
%endif

BuildArch:     noarch
Source44: import.info

%description
Implementation of the Mustache language in Java.
Mustache.java is a derivative of mustache.js.

%package benchmarks
Group: Development/Java
Summary:       Benchmarks for Mustache.java

%description benchmarks
A development module for performance benchmarks of
Mustache.java classes.

%package maven-plugin
Group: Development/Java
Summary:       Mustache Maven Mojo

%description maven-plugin
A maven plugin to process mustache templates in a maven build.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{oname}-%{version}
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

%pom_disable_module scala-extensions

%pom_remove_plugin :maven-assembly-plugin compiler
# Build problem during javadoc (openjdk 1.8.0.60-15.b28) task
# [ERROR] Failed to execute goal org.apache.maven.plugins:maven-javadoc-plugin:2.10.3:aggregate (default-cli)
#         on project mustache.java: An error has occurred in JavaDocs report generation:
# [ERROR] Exit code: 1 - javadoc: error - com.sun.tools.doclets.internal.toolkit.util.DocletAbortException:
#         com.sun.tools.javac.code.Symbol$CompletionFailure: class file for junit.framework.TestCase not found
#%% pom_disable_module benchmarks
%pom_add_dep junit:junit:4.12:provided
%pom_remove_plugin :maven-shade-plugin benchmarks
%pom_remove_plugin :maven-source-plugin benchmarks

%pom_remove_plugin :maven-assembly-plugin handlebar
# Fix manifest entries
%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin handlebar "
<configuration>
  <archive>
    <manifest>
      <addClasspath>false</addClasspath>
      <mainClass>com.sampullara.mustache.Handlebar</mainClass>
    </manifest>
  </archive>
</configuration>"

%mvn_package com.github.spullara.mustache.java:mustache-maven-plugin maven-plugin
%mvn_package com.github.spullara.mustache.java:benchmarks benchmarks
%mvn_package com.github.spullara.mustache.java:compiler::tests:

%build

# Test fails @ randon on ARM builder
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8 -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE

%files benchmarks -f .mfiles-benchmarks
%doc LICENSE

%files maven-plugin -f .mfiles-maven-plugin
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_2jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_2jpp8
- new version

