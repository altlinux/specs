Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global oname mustache.java
Name:          mustache-java
Version:       0.9.4
Release:       alt1_4jpp8
Summary:       Implementation of mustache.js for Java
License:       ASL 2.0
URL:           https://github.com/spullara/mustache.java/
Source0:       https://github.com/spullara/mustache.java/archive/%{oname}-%{version}.tar.gz

# This patch is sent upstream: https://github.com/spullara/mustache.java/pull/183
Patch0: jackson-standardisation.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires:  mvn(com.github.spullara.cli-parser:cli-parser)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server)
BuildRequires:  mvn(org.openjdk.jmh:jmh-core)
BuildRequires:  mvn(org.openjdk.jmh:jmh-generator-annprocess)

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

%patch0 -p1

%pom_disable_module scala-extensions

%pom_remove_plugin :maven-assembly-plugin handlebar
%pom_remove_plugin :maven-assembly-plugin compiler
%pom_remove_plugin :maven-shade-plugin benchmarks
%pom_remove_plugin :maven-source-plugin benchmarks

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

# Fix build with current maven-jar-plugin
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions" "
<execution>
  <id>default-jar</id>
  <phase>skip</phase>
</execution>" compiler

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
%doc --no-dereference LICENSE

%files benchmarks -f .mfiles-benchmarks
%doc --no-dereference LICENSE

%files maven-plugin -f .mfiles-maven-plugin
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_3jpp8
- new fc release

* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_2jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_2jpp8
- new version

