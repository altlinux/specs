Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
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
%global githash d426fc0a676eca0432c46be758414226ea07fd17

# Re-enable when https://bugzilla.redhat.com/show_bug.cgi?id=1234368 is fixed
#def_with ruby
%bcond_with ruby

Name:          tesla-polyglot
Version:       0.1.14
Release:       alt1_2jpp8
Summary:       Modules to enable Maven usage in other JVM languages
License:       EPL
URL:           https://github.com/takari/maven-polyglot
Source0:       https://github.com/takari/maven-polyglot/archive/%{githash}/maven-polyglot-%{githash}.tar.gz
Source1:       eclipse-1.0.txt

BuildRequires: maven-local
BuildRequires: mvn(antlr:antlr)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(commons-logging:commons-logging)
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
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.codehaus.groovy:groovy-all)
BuildRequires: mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires: mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires: mvn(org.ow2.asm:asm-all)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-nop)
BuildRequires: mvn(org.yaml:snakeyaml)

%if %{with ruby}
# Ruby module
BuildRequires: mvn(de.saumya.mojo:gem-maven-plugin)
BuildRequires: mvn(org.jruby:jruby-core)
%endif

%if 0
# clojure-maven-plugin dont work with clojure 1.5.1
# Clojure module
BuildRequires: mvn(com.theoryinpractise:clojure-maven-plugin:1.3.1)
BuildRequires: mvn(org.clojure:clojure:1.1.0)

# Scala module
BuildRequires: mvn(com.twitter:util-eval_2.10:6.23.0)
BuildRequires: mvn(com.googlecode.kiama:kiama_2.10:1.8.0)
BuildRequires: mvn(net.alchim31.maven:scala-maven-plugin:3.2.0)
BuildRequires: mvn(org.scala-lang:scala-library:2.10.5)
BuildRequires: mvn(org.specs2:specs2_2.10:2.4.17)

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

%description clojure
Polyglot Tesla :: Clojure.

%package scala
Group: Development/Java
Summary:       Polyglot Tesla :: Scala

%description scala
Polyglot Tesla :: Scala.
%endif

%package yaml
Group: Development/Java
Summary:       Polyglot Tesla :: YAML

%description yaml
Polyglot Tesla :: YAML.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n polyglot-maven-%{githash}
find -name "*.class" -delete
find -name "*.jar" -delete

%pom_remove_parent

# Unavailable build deps/tools
%pom_disable_module polyglot-clojure
%pom_disable_module polyglot-scala
%pom_remove_dep :polyglot-scala polyglot-translate-plugin

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

# Unavailable plugin
%pom_remove_plugin org.codehaus.groovy:groovy-eclipse-compiler polyglot-groovy
# Use as deps: org.codehaus.groovy:groovy-eclipse-compiler:2.9.2-01 org.codehaus.groovy:groovy-eclipse-batch:2.4.3-01
%pom_remove_plugin :maven-compiler-plugin polyglot-groovy
%pom_add_plugin org.apache.maven.plugins:maven-antrun-plugin:1.7 polyglot-groovy '
<dependencies>
  <dependency>
    <groupId>org.codehaus.groovy</groupId>
    <artifactId>groovy-all</artifactId>
    <version>2.4.4</version>
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
          srcdir="src/main" listfiles="true">
          <classpath refid="maven.compile.classpath"/>
        </groovyc>
      </tasks>
    </configuration>
    <goals>
      <goal>run</goal>
    </goals>
  </execution>
</executions>'

for p in maven-plugin translate-plugin; do
  %pom_add_plugin "org.apache.maven.plugins:maven-plugin-plugin:3.4" polyglot-${p} "
  <configuration>
    <skipErrorNoDescriptorsFound>true</skipErrorNoDescriptorsFound>
  </configuration>"
%pom_xpath_inject "pom:dependency[pom:groupId = 'org.apache.maven']" "<version>3.3.1</version>" polyglot-${p}
done

%pom_xpath_inject "pom:project/pom:dependencies/pom:dependency[pom:groupId = 'org.apache.maven']" '<version>${mavenVersion}</version>'

# atom common groovy maven-plugin translate-plugin
# diamond operator
for m in yaml
do
%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin:3.0 polyglot-${m} '
<configuration>
 <source>1.7</source>
 <target>1.7</target>
 <encoding>UTF-8</encoding>
</configuration>'
done

# Use web access
sed -i '/pyyaml/d' polyglot-yaml/src/test/java/org/sonatype/maven/polyglot/yaml/CompactFormatTest.java

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
%endif

%files maven-plugin -f .mfiles-polyglot-maven-plugin
%files translate-plugin -f .mfiles-polyglot-translate-plugin

%files yaml -f .mfiles-polyglot-yaml

%files javadoc -f .mfiles-javadoc
%doc eclipse-1.0.txt license-header.txt

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.14-alt1_2jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.8-alt1_4jpp8
- unbootsrap build

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.8-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

