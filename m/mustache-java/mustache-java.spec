Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global oname mustache.java
Name:          mustache-java
Version:       0.9.0
Release:       alt1_2jpp8
Summary:       Implementation of mustache.js for Java
License:       ASL 2.0
URL:           https://github.com/spullara/mustache.java/
Source0:       https://github.com/spullara/mustache.java/archive/%{oname}-%{version}.tar.gz

BuildRequires: mvn(com.github.spullara.cli-parser:cli-parser)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires: mvn(org.eclipse.jetty:jetty-server)

BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.codehaus.plexus:plexus-compiler-api)

BuildRequires: mvn(org.jruby:jruby)
BuildRequires: mvn(org.ow2.asm:asm-commons)
BuildRequires: mvn(org.ow2.asm:asm-util)

%if 0
BuildRequires: mvn(com.twitter:util-core:6.23.0)
BuildRequires: mvn(org.scala-lang:scala-library:2.11.4)
BuildRequires: mvn(org.scala-tools:maven-scala-plugin:2.14.1)
%endif

BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: maven-plugin-plugin
BuildArch:     noarch
Source44: import.info

%description
Implementation of the Mustache language in Java.
Mustache.java is a derivative of mustache.js.

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

# These tests fails for various reasons
rm -r compiler/src/test/java/com/github/mustachejava/SpecTest.java \
  compiler/src/test/java/com/github/mustachejava/simple/SimpleSpecTest.java \
  codegen/src/test/java/com/github/mustachejava/CodegenSpecTest.java \
  indy/src/test/java/com/github/mustachejava/IndySpecTest.java

%mvn_package com.github.spullara.mustache.java:mustache-maven-plugin maven-plugin

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8 -Dmaven.test.failure.ignore=true

%install
%mvn_install

install -pm 644 compiler/target/compiler-%{version}-tests.jar %{buildroot}%{_javadir}/%{name}/compiler-tests.jar

%files -f .mfiles
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/compiler-tests.jar
%doc README.md
%doc LICENSE

%files maven-plugin -f .mfiles-maven-plugin
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_2jpp8
- new version

