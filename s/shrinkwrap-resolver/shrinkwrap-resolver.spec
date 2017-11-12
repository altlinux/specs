Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          shrinkwrap-resolver
Version:       2.2.2
Release:       alt1_4jpp8
Summary:       Java API to obtain Maven artifacts
# Some file are without license headers
# reported @ https://issues.jboss.org/projects/SHRINKRES/issues/SHRINKRES-242
License:       ASL 2.0
URL:           http://arquillian.org/modules/resolver-shrinkwrap/
Source0:       https://github.com/shrinkwrap/resolver/archive/%{version}.tar.gz

Patch0:        shrinkwrap-resolver-2.2.2-maven-model3.4.patch
Patch1:        shrinkwrap-resolver-2.2.2-override.patch

BuildRequires: maven-local
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.maven:maven-aether-provider)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-model-builder)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-repository-metadata)
BuildRequires: mvn(org.apache.maven:maven-settings)
BuildRequires: mvn(org.apache.maven:maven-settings-builder)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.apache.maven.wagon:wagon-file)
BuildRequires: mvn(org.apache.maven.wagon:wagon-http-lightweight)
BuildRequires: mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires: mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires: mvn(org.codehaus.plexus:plexus-compiler-javac)
BuildRequires: mvn(org.codehaus.plexus:plexus-component-api)
BuildRequires: mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.eclipse.aether:aether:pom:)
BuildRequires: mvn(org.eclipse.aether:aether-api)
BuildRequires: mvn(org.eclipse.aether:aether-impl)
BuildRequires: mvn(org.eclipse.aether:aether-spi)
BuildRequires: mvn(org.eclipse.aether:aether-util)
BuildRequires: mvn(org.eclipse.aether:aether-connector-basic)
BuildRequires: mvn(org.eclipse.aether:aether-transport-wagon)
BuildRequires: mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires: mvn(org.gradle:gradle-tooling-api)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.shrinkwrap:shrinkwrap-api)
BuildRequires: mvn(org.jboss.shrinkwrap:shrinkwrap-bom:pom:)
BuildRequires: mvn(org.jboss.shrinkwrap:shrinkwrap-impl-base)
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(org.sonatype.plexus:plexus-sec-dispatcher)
BuildRequires: xmvn

BuildArch:     noarch
Source44: import.info

%description
The ShrinkWrap Resolvers project provides a Java API to obtain artifacts
from a repository system. This is handy to include third party libraries
available in any Maven repository in your test archive. ShrinkWrap Resolvers
additionally allows you to reuse all the configuration you've already specified
in Maven build file, making packaging of an application archive much easier job.

%package api
Group: Development/Java
Summary:          ShrinkWrap Resolver API

%description api
API to Resolve Dependencies from a Generic Backend.

%package api-gradle-embedded-archive
Group: Development/Java
Summary:          ShrinkWrap Resolver Embedded Gradle Archive API

%description api-gradle-embedded-archive
API for Resolving Dependencies from a Gradle Backend to
a ShrinkWrap Archive and Gradle Importer.

%package api-maven
Group: Development/Java
Summary:          ShrinkWrap Resolver Maven API

%description api-maven
API to Resolve Dependencies from a Maven Backend.

%package api-maven-archive
Group: Development/Java
Summary:          ShrinkWrap Resolver Maven Archive API

%description api-maven-archive
API for Resolving Dependencies from a Maven Backend to
a ShrinkWrap Archive and Maven Importer.

%package bom
Group: Development/Java
Summary:          ShrinkWrap Resolver Bill of Materials

%description bom
Centralized dependencyManagement for the
ShrinkWrap Resolver Project.

%package build-resources
Group: Development/Java
Summary:          Shrinkwrap Resolver Build Resources

%description build-resources
Shrinkwrap Resolver Build Resources.

%package depchain
Group: Development/Java
Summary:          ShrinkWrap Resolver Dependency Chain

%description depchain
Single-POM Definition to export the
ShrinkWrap Resolver artifacts
in proper scope.

%package gradle-depchain
Group: Development/Java
Summary:          ShrinkWrap Resolver Gradle Dependency Chain

%description gradle-depchain
Single-POM Definition to export the
ShrinkWrap Resolver Gradle artifacts
in proper scope.

%package impl-gradle-embedded-archive
Group: Development/Java
Summary:          ShrinkWrap Resolver Embedded Gradle Archive Implementation

%description impl-gradle-embedded-archive
Implementation for Resolving Dependencies
from a Gradle Backend to a ShrinkWrap Archive.

%package impl-maven
Group: Development/Java
Summary:          ShrinkWrap Resolver Maven Implementation

%description impl-maven
Implementation for Resolving Dependencies from a Maven Backend.

%package impl-maven-archive
Group: Development/Java
Summary:          ShrinkWrap Resolver Maven Archive Implementation

%description impl-maven-archive
Implementation for Resolving Dependencies
from a Maven Backend to a ShrinkWrap Archive.

%package maven-plugin
Group: Development/Java
Summary:          ShrinkWrap Resolver Maven Plugin

%description maven-plugin
ShrinkWrap Resolver Maven Plugin.

%package parent
Group: Development/Java
Summary:          ShrinkWrap Resolver Aggregator

%description parent
ShrinkWrap Resolver Aggregator.

%package spi
Group: Development/Java
Summary:          ShrinkWrap Resolver SPI

%description spi
Service Provider Interface to Resolve Dependencies from a Generic Backend.

%package spi-maven
Group: Development/Java
Summary:          ShrinkWrap Resolver Maven SPI

%description spi-maven
Service Provider Interface to Resolve Dependencies from a Maven Backend.

%package spi-maven-archive
Group: Development/Java
Summary:          ShrinkWrap Resolver Maven Archive SPI

%description spi-maven-archive
Service Provider Interface for Resolving Dependencies
from a Maven Backend to a ShrinkWrap Archive and
Importing Maven Project.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n resolver-%{version}
# Cleanup
find -name '*.jar' -print -delete
rm -rf */target

%patch0 -p1
%patch1 -p1

# Build problems, use old configurations
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin ":maven-enforcer-plugin"
%pom_remove_plugin :maven-invoker-plugin maven-plugin

# No test deps org.mortbay.jetty:jetty:6.1.16, org.easytesting:fest-assert:1.4
%pom_remove_dep -r org.easytesting:fest-assert
%pom_xpath_remove "pom:dependency[pom:scope = 'test']" impl-maven
rm -r impl-maven/src/test/java impl-gradle-embedded-archive/src/test/java

# Could not transfer artifact org.slf4j:slf4j-api:pom:1.6.1,
# org.jboss.spec:jboss-javaee-web-6.0:pom:3.0.2.Final from/to central (https://repo.maven.apache.org/maven2)
rm -r impl-maven-archive/src/test/java/org/jboss/shrinkwrap/resolver/impl/maven/archive/importer/ConfiguredMavenImporterTestCase.java \
 impl-maven-archive/src/test/java/org/jboss/shrinkwrap/resolver/impl/maven/archive/importer/JarMavenImporterTestCase.java \
 impl-maven-archive/src/test/java/org/jboss/shrinkwrap/resolver/impl/maven/archive/importer/ManifestTestCase.java \
 impl-maven-archive/src/test/java/org/jboss/shrinkwrap/resolver/impl/maven/archive/importer/WarMavenImporterTestCase.java \
 impl-maven-archive/src/test/java/org/jboss/shrinkwrap/resolver/impl/maven/archive/usecases/ShrinkWrapMavenTestCase.java

%build

%mvn_build -s

%install
%mvn_install

%files api -f .mfiles-%{name}-api
%doc README.asciidoc
%doc LICENSE

%files api-gradle-embedded-archive -f .mfiles-%{name}-api-gradle-embedded-archive
%files api-maven -f .mfiles-%{name}-api-maven
%files api-maven-archive -f .mfiles-%{name}-api-maven-archive

%files bom -f .mfiles-%{name}-bom
%doc LICENSE

%files build-resources -f .mfiles-%{name}-build-resources
%doc LICENSE

%files depchain -f .mfiles-%{name}-depchain
%doc LICENSE

%files gradle-depchain -f .mfiles-%{name}-gradle-depchain
%doc LICENSE

%files impl-gradle-embedded-archive -f .mfiles-%{name}-impl-gradle-embedded-archive
%files impl-maven -f .mfiles-%{name}-impl-maven
%files impl-maven-archive -f .mfiles-%{name}-impl-maven-archive
%files maven-plugin -f .mfiles-%{name}-maven-plugin

%files parent -f .mfiles-%{name}-parent
%doc LICENSE

%files spi -f .mfiles-%{name}-spi
%files spi-maven -f .mfiles-%{name}-spi-maven
%files spi-maven-archive -f .mfiles-%{name}-spi-maven-archive

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt1_3jpp8
- new jpp release

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt1_1jpp8
- new version

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.2.beta7jpp7
- full build

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

