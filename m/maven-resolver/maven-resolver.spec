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
Version:        1.1.1
Release:        alt1_2jpp8
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
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.sonatype.sisu:sisu-guice::no_aop:)

# XXX Remove after F26 EOL
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
# XXX Remove after F26 EOL
Obsoletes: aether-api < 1:1.0.3
Obsoletes: aether-ant-tasks < 1:1.0.1-9

%description api
The application programming interface for the repository system.

%package spi
Group: Development/Java
Summary:   Maven Artifact Resolver SPI
# XXX Remove after F26 EOL
Obsoletes: aether-spi < 1:1.0.3

%description spi
The service provider interface for repository system implementations and
repository connectors.

%package util
Group: Development/Java
Summary:   Maven Artifact Resolver Utilities
# XXX Remove after F26 EOL
Obsoletes: aether-util < 1:1.0.3

%description util
A collection of utility classes to ease usage of the repository system.

%package impl
Group: Development/Java
Summary:   Maven Artifact Resolver Implementation
# XXX Remove after F26 EOL
Obsoletes: aether-impl < 1:1.0.3

%description impl
An implementation of the repository system.

%package test-util
Group: Development/Java
Summary:   Maven Artifact Resolver Test Utilities
# XXX Remove after F26 EOL
Obsoletes: aether-test-util < 1:1.0.3

%description test-util
A collection of utility classes to ease testing of the repository system.

%package connector-basic
Group: Development/Java
Summary:   Maven Artifact Resolver Connector Basic
# XXX Remove after F26 EOL
Obsoletes: aether-connector-basic < 1:1.0.3

%description connector-basic
A repository connector implementation for repositories using URI-based layouts.

%package transport-classpath
Group: Development/Java
Summary:   Maven Artifact Resolver Transport Classpath
# XXX Remove after F26 EOL
Obsoletes: aether-transport-classpath < 1:1.0.3

%description transport-classpath
A transport implementation for repositories using classpath:// URLs.

%package transport-file
Group: Development/Java
Summary:   Maven Artifact Resolver Transport File
# XXX Remove after F26 EOL
Obsoletes: aether-transport-file < 1:1.0.3

%description transport-file
A transport implementation for repositories using file:// URLs.

%package transport-http
Group: Development/Java
Summary:   Maven Artifact Resolver Transport HTTP
# XXX Remove after F26 EOL
Obsoletes: aether-transport-http < 1:1.0.3

%description transport-http
A transport implementation for repositories using http:// and https:// URLs.

%package transport-wagon
Group: Development/Java
Summary:   Maven Artifact Resolver Transport Wagon
# XXX Remove after F26 EOL
Obsoletes: aether-transport-wagon < 1:1.0.3

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

%pom_disable_module maven-resolver-demos

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
%doc --no-dereference LICENSE NOTICE

%files api -f .mfiles-%{name}-api
%doc --no-dereference LICENSE NOTICE
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
%doc --no-dereference LICENSE NOTICE

%changelog
* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.1.1-alt1_2jpp8
- java update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.1.0-alt1_2jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.1.0-alt1_1jpp8
- new version

* Sun Nov 19 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0.3-alt1_7jpp8
- new version

