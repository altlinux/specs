Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Optionally build with a reduced dependency set
%bcond_with jp_minimal

%global oname mustache.java

Name:          mustache-java
Version:       0.9.6
Release:       alt1_1jpp8
Summary:       Implementation of mustache.js for Java
License:       ASL 2.0
URL:           https://github.com/spullara/mustache.java/
Source0:       https://github.com/spullara/mustache.java/archive/%{oname}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.google.guava:guava:20.0)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
%if %{without jp_minimal}
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires:  mvn(com.github.spullara.cli-parser:cli-parser)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server)
%endif

BuildArch: noarch

# Obsoletes added in F30
# Benchmarks are not really useful for users, so don't bother shipping them
Obsoletes: %{name}-benchmarks < %{version}-%{release}
Source44: import.info

%description
Implementation of the Mustache language in Java.
Mustache.java is a derivative of mustache.js.

%package maven-plugin
Group: Development/Java
Summary: Mustache Maven Mojo

%description maven-plugin
A maven plugin to process mustache templates in a maven build.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{oname}-%{oname}-%{version}

%pom_disable_module scala-extensions
%pom_disable_module benchmarks

# Not needed for RPM builds
%pom_remove_plugin :maven-assembly-plugin handlebar
%pom_remove_plugin :maven-assembly-plugin compiler

%if %{with jp_minimal}
# Build without cli/webserver support
%pom_remove_dep "org.eclipse.jetty:" handlebar
%pom_remove_dep "com.github.spullara.cli-parser:" handlebar
rm handlebar/src/main/java/com/sampullara/mustache/Handlebar.java
# Build without yaml tests
%pom_remove_dep ":jackson-dataformat-yaml" compiler
rm compiler/src/test/java/com/github/mustachejava/{SpecTest.java,simple/SimpleSpecTest.java}
%else
# Fix manifest entries for cli/webserver support
%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin handlebar "
<configuration>
  <archive>
    <manifest>
      <addClasspath>false</addClasspath>
      <mainClass>com.sampullara.mustache.Handlebar</mainClass>
    </manifest>
  </archive>
</configuration>"
%endif

%mvn_package com.github.spullara.mustache.java:mustache-maven-plugin maven-plugin
%mvn_package com.github.spullara.mustache.java:compiler::tests:

%build
# Test fails at random on ARM builder
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8 -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%files maven-plugin -f .mfiles-maven-plugin
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt1_1jpp8
- new version

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

