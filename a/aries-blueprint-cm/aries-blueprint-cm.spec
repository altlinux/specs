Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global bundle org.apache.aries.blueprint.cm
Name:          aries-blueprint-cm
Version:       1.0.8
Release:       alt1_4jpp8
Summary:       Apache Aries Blueprint CM
License:       ASL 2.0
URL:           http://aries.apache.org/
#Source0:       http://www.apache.org/dist/aries/%%{bundle}-%%{version}-source-release.zip
Source0:       http://central.maven.org/maven2/org/apache/aries/blueprint/%{bundle}/%{version}/%{bundle}-%{version}-source-release.zip

BuildRequires: maven-local
BuildRequires: mvn(org.apache.aries.blueprint:blueprint-parser) >= 1.4.0
BuildRequires: mvn(org.apache.aries.blueprint:org.apache.aries.blueprint.api) >= 1.0.1
BuildRequires: mvn(org.apache.aries.blueprint:org.apache.aries.blueprint.core) >= 1.6.2
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi.services)
BuildRequires: mvn(org.slf4j:slf4j-api)

Obsoletes:     aries-blueprint < 1:0.3.2
Provides:      aries-blueprint = %{version}-%{release}

BuildArch:     noarch
Source44: import.info

%description
This bundle contains the ConfigAdmin namespace for blueprint.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%pom_remove_parent
%pom_remove_plugin org.apache.aries.versioning:org.apache.aries.versioning.plugin

# Fix bundle plugin configuration
%pom_add_plugin org.apache.felix:maven-bundle-plugin . '
<extensions>true</extensions>
<configuration>
  <excludeDependencies>true</excludeDependencies>
  <instructions>
    <Bundle-Name>${project.name}</Bundle-Name>
    <Bundle-SymbolicName>${project.artifactId}</Bundle-SymbolicName>
    <Bundle-Vendor>The Apache Software Foundation</Bundle-Vendor>
    <Import-Package>${aries.osgi.import.pkg}</Import-Package>
    <Implementation-Title>Apache Aries</Implementation-Title>
    <Implementation-Version>${project.version}</Implementation-Version>
    <Private-Package>${aries.osgi.private.pkg}</Private-Package>
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
</executions>'

%pom_change_dep org.osgi:org.osgi.core org.eclipse.osgi:org.eclipse.osgi:3.11.0.v20160714-1000
%pom_change_dep org.osgi:org.osgi.compendium org.eclipse.osgi:org.eclipse.osgi.services:3.5.100.v20160714-1000

%build

# tests disabled because of
# missing dependency on pax-swissbox-tinybundles de.kalpatec.pojosr.framework
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_4jpp8
- java update

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_3jpp8
- new version

