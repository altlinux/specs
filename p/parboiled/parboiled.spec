Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global scala_short_version 2.10
Name:          parboiled
Version:       1.1.6
Release:       alt1_10jpp8
Summary:       Java/Scala library providing parsing of input text based on PEGs
License:       ASL 2.0
URL:           http://parboiled.org/
Source0:       https://github.com/sirthias/parboiled/archive/%{version}.tar.gz
# for build see https://github.com/sirthias/parboiled/wiki/Building-parboiled
Source1:       http://repo1.maven.org/maven2/org/parboiled/%{name}-core/%{version}/%{name}-core-%{version}.pom
Source2:       http://repo1.maven.org/maven2/org/parboiled/%{name}-java/%{version}/%{name}-java-%{version}.pom
# customized aggregator pom
Source3:       %{name}-pom.xml
Source4:       http://repo1.maven.org/maven2/org/parboiled/%{name}-scala_%{scala_short_version}/%{version}/%{name}-scala_%{scala_short_version}-%{version}.pom
Patch0:        %{name}-1.1.6-scala-use-antrun-plugin.patch
Patch1:        parboiled-port-to-objectweb-asm-5.0.1.patch

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-analysis)
BuildRequires: mvn(org.ow2.asm:asm-tree)
BuildRequires: mvn(org.ow2.asm:asm-util)
BuildRequires: mvn(org.scala-lang:scala-compiler)
BuildRequires: mvn(org.scala-lang:scala-library)

%if 0
# test deps
BuildRequires: mvn(org.scalatest:scalatest_2.9.3)
BuildRequires: mvn(org.testng:testng)
%endif

BuildArch:     noarch
Source44: import.info

%description
parboiled is a mixed Java/Scala library providing for lightweight and
easy-to-use, yet powerful and elegant parsing of arbitrary input text
based on Parsing expression grammars (PEGs). PEGs are an alternative to
context free grammars (CFGs) for formally specifying syntax, they
make a good replacement for regular expressions and generally have quite
a few advantages over the "traditional" way of building parser via CFGs.

%package scala
Group: Development/Java
Summary:       Parboiled for Scala

%description scala
An internal Scala DSL for efficiently defining your parser rules.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

find . -name "*.class" -delete
find . -name "*.jar" -delete

cp -p %{SOURCE1} %{name}-core/pom.xml
cp -p %{SOURCE2} %{name}-java/pom.xml
cp -p %{SOURCE4} %{name}-scala/pom.xml

for m in core java; do
%pom_xpath_inject "pom:project" "
<build>
  <plugins>

  </plugins>
</build>" %{name}-${m}

%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin %{name}-${m} "
<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
  </archive>
</configuration>"
done

%pom_add_plugin org.apache.felix:maven-bundle-plugin %{name}-core "
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>org.parboiled.core</Bundle-SymbolicName>
    <Bundle-Name>org.parboiled.core</Bundle-Name>
    <Bundle-Version>\${project.version}</Bundle-Version>
    <Private-Package>org.parboiled.core.*</Private-Package>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>"

%pom_add_plugin org.apache.felix:maven-bundle-plugin %{name}-java "
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>org.parboiled.java</Bundle-SymbolicName>
    <Bundle-Name>org.parboiled.java</Bundle-Name>
    <Bundle-Version>\${project.version}</Bundle-Version>
    <Fragment-Host>org.parboiled.core</Fragment-Host>
    <Private-Package>org.parboiled.java.*</Private-Package>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>"

%patch0 -p0
%patch1 -p1

cp -p %{SOURCE3} pom.xml
sed -i "s|@VERSION@|%{version}|" pom.xml

%mvn_file :%{name}-core %{name}/core
%mvn_file :%{name}-java %{name}/java
%mvn_package :%{name}-project __noinstall
%pom_xpath_inject "pom:modules" "<module>%{name}-scala</module>"
%mvn_file :%{name}-scala_%{scala_short_version} %{name}/scala
%mvn_package :%{name}-scala_%{scala_short_version} scala

%build

# test skipped unavailable dep org.scalatest scalatest_2.9.0 1.6.1
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8
 
%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG README.markdown
%doc LICENSE

%files scala -f .mfiles-scala
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt1_10jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt1_9jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt1_8jpp8
- new version

* Mon Jan 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_6jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_3jpp7
- rebuild with maven-local

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp7
- new version

