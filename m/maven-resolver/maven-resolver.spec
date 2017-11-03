Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-resolver
Epoch:          1
Version:        1.0.3
Release:        alt1_7jpp8
License:        ASL 2.0
Summary:        Apache Maven Artifact Resolver library
URL:            http://maven.apache.org/resolver/
Source0:        http://archive.apache.org/dist/maven/resolver/%{name}-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-library)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.sonatype.sisu:sisu-guice::no_aop:)

Obsoletes:      aether < 1:1.0.3
Source44: import.info

%description
Apache Maven Artifact Resolver is a library for working with artifact
repositories and dependency resolution. Maven Artifact Resolver deals with the
specification of local repository, remote repository, developer workspaces,
artifact transports and artifact resolution.

%package api
Group: Development/Java
Summary:   Maven Artifact Resolver API
Obsoletes: aether-api < 1:1.0.3
Provides:  aether-api = %{epoch}:%{version}-%{release}

%description api
The application programming interface for the repository system.

%package spi
Group: Development/Java
Summary:   Maven Artifact Resolver SPI
Obsoletes: aether-spi < 1:1.0.3
Provides:  aether-spi = %{epoch}:%{version}-%{release}

%description spi
The service provider interface for repository system implementations and
repository connectors.

%package util
Group: Development/Java
Summary:   Maven Artifact Resolver Utilities
Obsoletes: aether-util < 1:1.0.3
Provides:  aether-util = %{epoch}:%{version}-%{release}

%description util
A collection of utility classes to ease usage of the repository system.

%package impl
Group: Development/Java
Summary:   Maven Artifact Resolver Implementation
Obsoletes: aether-impl < 1:1.0.3
Provides:  aether-impl = %{epoch}:%{version}-%{release}

%description impl
An implementation of the repository system.

%package test-util
Group: Development/Java
Summary:   Maven Artifact Resolver Test Utilities
Obsoletes: aether-test-util < 1:1.0.3
Provides:  aether-test-util = %{epoch}:%{version}-%{release}

%description test-util
A collection of utility classes to ease testing of the repository system.

%package connector-basic
Group: Development/Java
Summary:   Maven Artifact Resolver Connector Basic
Obsoletes: aether-connector-basic < 1:1.0.3
Provides:  aether-connector-basic = %{epoch}:%{version}-%{release}

%description connector-basic
A repository connector implementation for repositories using URI-based layouts.

%package transport-classpath
Group: Development/Java
Summary:   Maven Artifact Resolver Transport Classpath
Obsoletes: aether-transport-classpath < 1:1.0.3
Provides:  aether-transport-classpath = %{epoch}:%{version}-%{release}

%description transport-classpath
A transport implementation for repositories using classpath:// URLs.

%package transport-file
Group: Development/Java
Summary:   Maven Artifact Resolver Transport File
Obsoletes: aether-transport-file < 1:1.0.3
Provides:  aether-transport-file = %{epoch}:%{version}-%{release}

%description transport-file
A transport implementation for repositories using file:// URLs.

%package transport-http
Group: Development/Java
Summary:   Maven Artifact Resolver Transport HTTP
Obsoletes: aether-transport-http < 1:1.0.3
Provides:  aether-transport-http = %{epoch}:%{version}-%{release}

%description transport-http
A transport implementation for repositories using http:// and https:// URLs.

%package transport-wagon
Group: Development/Java
Summary:   Maven Artifact Resolver Transport Wagon
Obsoletes: aether-transport-wagon < 1:1.0.3
Provides:  aether-transport-wagon = %{epoch}:%{version}-%{release}

%description transport-wagon
A transport implementation based on Maven Wagon.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package provides %{summary}.


%prep
%setup -q

# tests require jetty 7
%pom_remove_dep :::test maven-resolver-transport-http
rm -r maven-resolver-transport-http/src/test

# generate OSGi manifests
for pom in $(find -mindepth 2 -name pom.xml) ; do
  %pom_add_plugin "org.apache.felix:maven-bundle-plugin" $pom \
  "<configuration>
    <instructions>
      <Bundle-SymbolicName>\${project.groupId}$(sed 's:./maven-resolver::;s:/pom.xml::;s:-:.:g' <<< $pom)</Bundle-SymbolicName>
      <Export-Package>!org.eclipse.aether.internal*,org.eclipse.aether*</Export-Package>
      <_nouses>true</_nouses>
    </instructions>
  </configuration>
  <executions>
    <execution>
      <id>create-manifest</id>
      <phase>process-classes</phase>
      <goals><goal>manifest</goal></goals>
    </execution>
  </executions>"
done
%pom_add_plugin "org.apache.maven.plugins:maven-jar-plugin" pom.xml \
"<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
  </archive>
</configuration>"

%mvn_package :maven-resolver
%mvn_alias 'org.apache.maven.resolver:maven-resolver{*}' 'org.eclipse.aether:aether@1'
%mvn_file ':maven-resolver{*}' %{name}/maven-resolver@1 aether/aether@1

%build
%mvn_build -s

%install
%mvn_install


%files -f .mfiles
%doc LICENSE NOTICE

%files api -f .mfiles-%{name}-api
%doc LICENSE NOTICE
%files spi -f .mfiles-%{name}-spi
%files util -f .mfiles-%{name}-util
%files impl -f .mfiles-%{name}-impl
%files test-util -f .mfiles-%{name}-test-util
%files connector-basic -f .mfiles-%{name}-connector-basic
%files transport-classpath -f .mfiles-%{name}-transport-classpath
%files transport-file -f .mfiles-%{name}-transport-file
%files transport-http -f .mfiles-%{name}-transport-http
%files transport-wagon -f .mfiles-%{name}-transport-wagon

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sun Nov 19 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0.3-alt1_7jpp8
- new version

