Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 23
Name:          hawtdispatch
Version:       1.21
Release:       alt1_4jpp8
Summary:       The libdispatch style API for Java
License:       ASL 2.0
URL:           http://hawtdispatch.fusesource.org/
Source0:       https://github.com/fusesource/hawtdispatch/archive/%{name}-project-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(asm:asm-tree)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
%if (0%{?rhel} > 0) || (0%{?fedora} < 21)
BuildRequires: mvn(org.fusesource:fusesource-pom)
BuildRequires: mvn(log4j:log4j)
%else
BuildRequires: mvn(org.fusesource:fusesource-pom:pom:)
BuildRequires: mvn(log4j:log4j:1.2.17)
%endif
BuildRequires: mvn(org.fusesource.hawtbuf:hawtbuf)
BuildRequires: mvn(org.osgi:org.osgi.compendium)
BuildRequires: mvn(org.osgi:org.osgi.core)
BuildRequires: mvn(org.scala-lang:scala-compiler)
BuildRequires: mvn(org.scala-lang:scala-library)

%if 0
# unavailable sub module deps
# scala test deps
BuildRequires: mvn(org.scalatest:scalatest_2.10.0)
# scala-2.11
BuildRequires: mvn(org.scalatest:scalatest_2.11)

# website
BuildRequires: mvn(org.fusesource.mvnplugins:maven-linkchecker-plugin)
BuildRequires: mvn(org.fusesource.scalamd:scalamd)
BuildRequires: mvn(org.fusesource.scalate:scalate-page)
BuildRequires: mvn(org.fusesource.scalate:scalate-wikitext)
BuildRequires: mvn(org.fusesource.scalate:maven-scalate-plugin)
BuildRequires: mvn(org.mortbay.jetty:jetty-maven-plugin)
BuildRequires: mvn(org.scala-lang:scala-compiler)
BuildRequires: mvn(org.scala-tools:maven-scala-plugin)

BuildRequires: mvn(org.slf4j:slf4j-nop)
%endif

BuildArch:     noarch
Source44: import.info

# Linux C port @ http://nickhutchinson.me/libdispatch

%description
HawtDispatch is a small (less than 100k) thread pooling and
NIO event notification framework API modeled after the
libdispatch API that Apple created to power the Grand Central
Dispatch (GCD) technology in OS X. It allows you to easily develop
multi-threaded applications without having to deal with the
problems that traditionally plague multi-threaded application
development.

This package provides the libdispatch style API for Java.

%package scala
Group: Development/Java
Summary:       The libdispatch style API for Scala

%description scala
HawtDispatch: The libdispatch style API for Scala.

%package transport
Group: Development/Java
Summary:       Transport abstractions for HawtDispatch

%description transport
HawtDispatch Transport: Transport abstractions for HawtDispatch.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-project-%{version}

# remove unavailable org.fusesource.mvnplugins:fuse-javadoc-skin
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-site-plugin']/pom:configuration/pom:reportPlugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:resourcesArtifacts"
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:dependencies"
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:resourcesArtifacts"

%pom_disable_module %{name}-example
%pom_disable_module %{name}-website
%pom_disable_module %{name}-scala-2.11

%pom_remove_plugin net.alchim31.maven:scala-maven-plugin %{name}-scala
%pom_add_plugin org.apache.maven.plugins:maven-antrun-plugin:1.7 %{name}-scala '
<executions>
  <execution>
    <id>compile</id>
    <phase>process-sources</phase>
    <configuration>
      <tasks>
        <property name="build.compiler" value="extJavac"/>
        <taskdef resource="scala/tools/ant/antlib.xml" classpathref="maven.plugin.classpath"/>
        <mkdir dir="target/classes"/>
        <scalac srcdir="src/main" destdir="target/classes" classpathref="maven.compile.classpath" encoding="UTF-8">
          <include name="**/*.*"/>
        </scalac>
      </tasks>
    </configuration>
      <goals>
        <goal>run</goal>
      </goals>
  </execution>
</executions>
<dependencies>
  <dependency>
      <groupId>org.scala-lang</groupId>
      <artifactId>scala-compiler</artifactId>
      <version>${scala-version}</version>
  </dependency>
</dependencies>'
%pom_remove_dep org.scalatest: %{name}-scala

%if (0%{?rhel} > 0) || (0%{?fedora} >= 21)
%pom_xpath_set "pom:properties/pom:asm-version" 3 %{name}
%pom_xpath_set "pom:properties/pom:asm-version" 3 %{name}-transport
%pom_xpath_set "pom:properties/pom:log4j-version" 1.2.17
%pom_xpath_set "pom:properties/pom:log4j-version" 1.2.17 %{name}
%pom_xpath_set "pom:properties/pom:log4j-version" 1.2.17 %{name}-transport
%endif

%mvn_file :%{name} %{name}
%mvn_file :%{name}-transport %{name}-transport
%mvn_file :%{name}-scala %{name}-scala
%mvn_alias :%{name}-scala :%{name}-scala-2.11
%mvn_package ":%{name}-project" %{name}

# This test @ random fails on koji AssertionFailedError: null
rm -r hawtdispatch/src/test/java/org/fusesource/hawtdispatch/DispatchSourceTest.java

%build

%mvn_build -s

%install
%mvn_install 

%files -f .mfiles-%{name}
%doc changelog.md readme.md
%doc license.txt notice.md

%files scala -f .mfiles-%{name}-scala
%doc license.txt notice.md

%files transport -f .mfiles-%{name}-transport
%doc license.txt notice.md

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.md

%changelog
* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_4jpp8
- new version

