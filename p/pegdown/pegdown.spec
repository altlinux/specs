Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          pegdown
Version:       1.4.2
Release:       alt1_9jpp8
Summary:       Java library for Markdown processing
License:       ASL 2.0
URL:           http://pegdown.org
Source0:       https://github.com/sirthias/pegdown/archive/%{version}.tar.gz
# Newer release use sbt builder
Source1:       http://repo1.maven.org/maven2/org/pegdown/pegdown/%{version}/pegdown-%{version}.pom
# Forwarded upstream: https://github.com/sirthias/pegdown/pull/130
Patch0:        %{name}-rhbz1096735.patch

BuildRequires: maven-local
BuildRequires: mvn(net.sf.jtidy:jtidy)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.parboiled:parboiled-java)
%if 0
# test deps
BuildRequires: mvn(org.specs2:specs2_2.9.3)
%endif

BuildArch:     noarch
Source44: import.info

%description
A pure-Java Markdown processor based on a parboiled PEG parser
supporting a number of extensions.

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
%patch0 -p1

cp -p %{SOURCE1} pom.xml

%pom_xpath_inject "pom:project" "
<build>
  <plugins>

  </plugins>
</build>"

%pom_xpath_inject "pom:build" "
<resources>
  <resource>
    <directory>.</directory>
    <targetPath>\${project.build.outputDirectory}/META-INF</targetPath>
    <includes>
      <include>LICENSE</include>
      <include>NOTICE</include>
    </includes>
  </resource>
</resources>"

%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin . "
<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
    <manifest>
      <addDefaultImplementationEntries>true</addDefaultImplementationEntries>
      <addDefaultSpecificationEntries>true</addDefaultSpecificationEntries>
    </manifest>
  </archive>
</configuration>"

%pom_add_plugin org.apache.felix:maven-bundle-plugin . "
<extensions>true</extensions>
<configuration>
  <instructions>
    <Built-By>\${user.name}</Built-By>
    <Bundle-SymbolicName>org.pegdown</Bundle-SymbolicName>
    <Bundle-Name>pegdown</Bundle-Name>
    <Bundle-Vendor>pegdown.org</Bundle-Vendor>
    <Bundle-Version>\${project.version}</Bundle-Version>
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

rm -r src/test/scala/*
%pom_remove_dep org.specs2:specs2_2.9.3

%mvn_file :%{name} %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG README.markdown
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1_9jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1_8jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1_7jpp8
- new version

* Mon Jan 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt3_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt3_4jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_2jpp7
- new version

