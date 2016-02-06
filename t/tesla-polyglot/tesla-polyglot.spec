Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%global githash 1cba6bd2480590e44daf8d21ded87dd5e8e5d3af

# Re-enable when https://bugzilla.redhat.com/show_bug.cgi?id=1234368 is fixed
#def_with ruby
%bcond_with ruby

Name:          tesla-polyglot
Version:       0.1.8
Release:       alt1_4jpp8
Summary:       Modules to enable Maven usage in other JVM languages
License:       EPL
URL:           https://github.com/takari/maven-polyglot
Source0:       https://github.com/takari/maven-polyglot/archive/%{githash}/maven-polyglot-%{githash}.tar.gz
Source1:       eclipse-1.0.txt

BuildRequires: maven-local
BuildRequires: mvn(antlr:antlr)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(commons-logging:commons-logging)
# BuildRequires: mvn(io.takari:takari:pom:)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-junit)
BuildRequires: mvn(org.apache.ant:ant-launcher)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-model-builder)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.codehaus.groovy:groovy-all)
BuildRequires: mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires: mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires: mvn(org.ow2.asm:asm-all)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-nop)

%if %{with ruby}
# Ruby module
BuildRequires: mvn(de.saumya.mojo:gem-maven-plugin)
BuildRequires: mvn(org.jruby:jruby-core)
%endif

%if 0

# clojure-maven-plugin dont work with clojure 1.5.1
# BuildRequires: mvn(org.clojure:clojure)
# Disable clojure module
# https://bugzilla.redhat.com/show_bug.cgi?id=1106061
BuildRequires: clojure-compat
BuildRequires: mvn(com.theoryinpractise:clojure-maven-plugin)

# Scala module
BuildRequires: mvn(com.twitter:util-core_2.10:6.3.8)
BuildRequires: mvn(com.twitter:util-eval_2.10:6.3.8)
BuildRequires: mvn(com.googlecode.kiama:kiama_2.10:1.5.1)
BuildRequires: mvn(net.alchim31.maven:scala-maven-plugin:3.1.5)
BuildRequires: mvn(org.scala-lang:scala-library)
BuildRequires: mvn(org.specs2:specs2_2.10:2.1.1)

# YAML module
BuildRequires: mvn(org.yaml:snakeyaml:1.4)

# test deps
# No more available retired
BuildRequires: mvn(org.easytesting:fest-assert)
%endif

Obsoletes:     %{name}-cli
Obsoletes:     %{name}-clojure
BuildArch:     noarch
Source44: import.info

%description
Polyglot for Maven is an experimental distribution of Maven
that allows the expression of a POM in something other than
XML. A couple of the dialects also have the capability to
write plugins inline: the Groovy, Ruby and Scala dialects
allow this.

%package atom
Group: Development/Java
Summary:       Polyglot Tesla :: Atom

%description atom
Polyglot Tesla :: Atom.

%package common
Group: Development/Java
Summary:       Polyglot Tesla :: Common

%description common
Polyglot Tesla :: Common.

%package groovy
Group: Development/Java
Summary:       Polyglot Tesla :: Groovy

%description groovy
Polyglot Tesla :: Groovy.

%package maven-plugin
Group: Development/Java
Summary:       Polyglot Tesla :: Maven Plugin

%description maven-plugin
This package contains Polyglot Tesla Maven Plugin.

%if %{with ruby}
%package ruby
Group: Development/Java
Summary:       Polyglot Tesla :: Ruby

%description ruby
Polyglot Tesla :: Ruby.
%endif

%package translate-plugin
Group: Development/Java
Summary:       Polyglot :: Translate Plugin

%description translate-plugin
This package contains Polyglot Translate Plugin.

%if 0
%package clojure
Group: Development/Java
Summary:       Polyglot Tesla :: Clojure
# Require clojure 1.2.x
Requires:      clojure-compat

%description clojure
Polyglot Tesla :: Clojure.

%package scala
Group: Development/Java
Summary:       Polyglot Tesla :: Scala

%description scala
Polyglot Tesla :: Scala.

%package yaml
Group: Development/Java
Summary:       Polyglot Tesla :: YAML

%description yaml
Polyglot Tesla :: YAML.
%endif

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n maven-polyglot-%{githash}
find -name "*.class" -delete
find -name "*.jar" -delete

%pom_remove_parent

# Unavailable build deps/tools
%pom_disable_module polyglot-clojure
%pom_disable_module polyglot-scala
%pom_remove_dep :polyglot-scala polyglot-translate-plugin
%pom_disable_module polyglot-yaml
%pom_remove_dep :polyglot-yaml polyglot-translate-plugin

%if %{without ruby}
%pom_disable_module polyglot-ruby
%pom_remove_dep -r :polyglot-ruby
%endif

%pom_remove_dep org.eclipse.sisu:org.eclipse.sisu.inject.tests

%pom_change_dep org.jruby:jruby-noasm org.jruby:jruby-core polyglot-ruby
%pom_remove_dep rubygems:maven-tools polyglot-ruby
# TODO: remove following line once maven-tools gem is in Fedora
rm -Rf polyglot-ruby/src/{test,it}
%pom_remove_plugin :maven-invoker-plugin polyglot-ruby

%pom_add_plugin org.apache.maven.plugins:maven-antrun-plugin:1.7 polyglot-groovy '
<dependencies>
  <dependency>
    <groupId>org.codehaus.groovy</groupId>
    <artifactId>groovy-all</artifactId>
    <version>2.4.0</version>
  </dependency>
  <dependency>
    <groupId>antlr</groupId>
    <artifactId>antlr</artifactId>
    <version>2.7.7</version>
  </dependency>
  <dependency>
    <groupId>commons-cli</groupId>
    <artifactId>commons-cli</artifactId>
    <version>1.2</version>
  </dependency>
  <dependency>
    <groupId>org.ow2.asm</groupId>
    <artifactId>asm-all</artifactId>
    <version>4.2</version>
  </dependency>
  <dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-nop</artifactId>
    <version>1.7.5</version>
  </dependency>
</dependencies>
<executions>
  <execution>
    <id>compile</id>
    <phase>compile</phase>
    <configuration>
      <tasks>
        <taskdef name="groovyc"
          classname="org.codehaus.groovy.ant.Groovyc">
          <classpath refid="maven.plugin.classpath"/>
        </taskdef>
        <groovyc destdir="target/classes"
          srcdir="src/main/groovy/" listfiles="true">
          <classpath refid="maven.compile.classpath"/>
        </groovyc>
      </tasks>
    </configuration>
    <goals>
      <goal>run</goal>
    </goals>
  </execution>
</executions>'

%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:groupId = 'org.codehaus.groovy']/pom:version" 2.4.0 polyglot-groovy

for p in maven-plugin translate-plugin; do
  %pom_add_plugin "org.apache.maven.plugins:maven-plugin-plugin:3.4" polyglot-${p} "
  <configuration>
    <skipErrorNoDescriptorsFound>true</skipErrorNoDescriptorsFound>
  </configuration>"
%pom_xpath_inject "pom:dependencies/pom:dependency[pom:groupId = 'org.apache.maven']" "<version>3.3.1</version>" polyglot-${p}
done

%pom_xpath_inject "pom:project/pom:dependencies/pom:dependency[pom:groupId = 'org.apache.maven']" '<version>${mavenVersion}</version>'

# test skipped for unavailable dependency org.easytesting:fest-assert:1.1
rm -rf polyglot-clojure/src/test/java/*

cp -p %{SOURCE1} .
sed -i 's/\r//' eclipse-1.0.txt

%mvn_alias ':polyglot-{*}' io.tesla.polyglot:tesla-polyglot-@1
%mvn_alias ':polyglot-{*}' org.sonatype.pmaven:pmaven-@1

%build

%mvn_build -s -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles-polyglot
%dir %{_javadir}/%{name}
%doc poms
%doc eclipse-1.0.txt license-header.txt

%files atom -f .mfiles-polyglot-atom
%files common -f .mfiles-polyglot-common
%files groovy -f .mfiles-polyglot-groovy

%if %{with ruby}
%files ruby -f .mfiles-polyglot-ruby
%endif

%if 0
%files clojure -f .mfiles-polyglot-clojure
%files scala -f .mfiles-polyglot-scala
%files yaml -f .mfiles-polyglot-yaml
%endif

%files maven-plugin -f .mfiles-polyglot-maven-plugin
%files translate-plugin -f .mfiles-polyglot-translate-plugin

%files javadoc -f .mfiles-javadoc
%doc eclipse-1.0.txt license-header.txt

%changelog
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.8-alt1_4jpp8
- unbootsrap build

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.8-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

