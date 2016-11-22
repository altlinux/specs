Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          hawtdispatch
Version:       1.22
Release:       alt1_2jpp8
Summary:       The libdispatch style API for Java
License:       ASL 2.0
URL:           http://hawtdispatch.fusesource.org/
Source0:       https://github.com/fusesource/hawtdispatch/archive/%{name}-project-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(asm:asm-tree)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.fusesource:fusesource-pom:pom:)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.fusesource.hawtbuf:hawtbuf)
BuildRequires: mvn(org.osgi:org.osgi.compendium)
BuildRequires: mvn(org.osgi:org.osgi.core)
BuildRequires: mvn(org.scala-lang:scala-compiler)
BuildRequires: mvn(org.scala-lang:scala-library)

BuildArch:     noarch
Source44: import.info

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
%pom_xpath_remove "pom:resourcesArtifacts"
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:dependencies"

%pom_xpath_remove "pom:Private-Package"
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration" \
 "<excludeDependencies>true</excludeDependencies>" %{name}-transport
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration/pom:instructions"  \
'<Export-Package>
 org.fusesource.hawtdispatch.transport;version=${project.version},
 org.fusesource.hawtdispatch.util;version=${project.version},
</Export-Package>' %{name}-transport

%pom_xpath_remove "pom:Export-Package" %{name}-scala
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration" \
 "<excludeDependencies>true</excludeDependencies>" %{name}-scala
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration/pom:instructions" \
'<Export-Package>
 org.fusesource.hawtdispatch;version=${project.version},
</Export-Package>' %{name}-scala

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

%pom_xpath_set "pom:properties/pom:asm-version" 3 %{name}
%pom_xpath_set "pom:properties/pom:asm-version" 3 %{name}-transport
%pom_xpath_set "pom:properties/pom:log4j-version" 1.2.17
%pom_xpath_set "pom:properties/pom:log4j-version" 1.2.17 %{name}
%pom_xpath_set "pom:properties/pom:log4j-version" 1.2.17 %{name}-transport

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
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1_2jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1_1jpp8
- new version

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1_4jpp8
- new version

