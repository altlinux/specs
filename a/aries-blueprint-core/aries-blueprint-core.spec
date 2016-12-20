Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global bundle org.apache.aries.blueprint.core

Name:          aries-blueprint-core
Version:       1.6.2
Release:       alt1_1jpp8
Summary:       Apache Aries Blueprint Core
License:       ASL 2.0
URL:           http://aries.apache.org/
#Source0:       http://www.apache.org/dist/aries/%%{bundle}-%%{version}-source-release.zip
Source0:       http://central.maven.org/maven2/org/apache/aries/blueprint/%{bundle}/%{version}/%{bundle}-%{version}-source-release.zip

BuildRequires: maven-local
BuildRequires: mvn(org.apache.aries:org.apache.aries.util)
BuildRequires: mvn(org.apache.aries.blueprint:blueprint-parser) >= 1.4.0
BuildRequires: mvn(org.apache.aries.blueprint:org.apache.aries.blueprint.annotation.api) >= 1.0.1
BuildRequires: mvn(org.apache.aries.blueprint:org.apache.aries.blueprint.api) >= 1.0.1
BuildRequires: mvn(org.apache.aries.proxy:org.apache.aries.proxy.api) >= 1.0.1
BuildRequires: mvn(org.apache.aries.proxy:org.apache.aries.proxy.impl) >= 1.0.5
BuildRequires: mvn(org.apache.aries.quiesce:org.apache.aries.quiesce.api) >= 1.0.0
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi.services)
BuildRequires: mvn(org.ow2.asm:asm-debug-all)
BuildRequires: mvn(org.slf4j:slf4j-api)

BuildArch:     noarch
Source44: import.info

%description
This bundle contains the core implementation of Blueprint
along with the "ext" namespace handler.

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
# Disable blueprint-parser copy
%pom_remove_plugin :maven-dependency-plugin
# Unwanted task
%pom_remove_plugin :maven-release-plugin

# Fix bundle plugin configuration
%pom_remove_plugin :maven-bundle-plugin
%pom_add_plugin org.apache.felix:maven-bundle-plugin . '
<extensions>true</extensions>
<configuration>
  <excludeDependencies>true</excludeDependencies>
  <instructions>
    <Bundle-Activator>${aries.osgi.activator}</Bundle-Activator>
    <Bundle-Name>${project.name}</Bundle-Name>
    <Bundle-SymbolicName>${project.artifactId}</Bundle-SymbolicName>
    <Bundle-Vendor>The Apache Software Foundation</Bundle-Vendor>
    <Export-Package>${aries.osgi.export.pkg}</Export-Package>
    <Export-Service>${aries.osgi.export.service}</Export-Service>
    <Import-Package>${aries.osgi.import.pkg}</Import-Package>
    <Import-Service>org.apache.aries.proxy.ProxyManager</Import-Service>
    <Implementation-Title>Apache Aries</Implementation-Title>
    <Implementation-Version>${project.version}</Implementation-Version>
    <!--Include-Resource>${aries.osgi.include.resource}</Include-Resource-->
    <Provide-Capability>
        osgi.extender;
        osgi.extender="osgi.blueprint";uses:=
        "org.osgi.service.blueprint.container,
        org.osgi.service.blueprint.reflect"; version:Version="1.0"
    </Provide-Capability>
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

%pom_xpath_remove "pom:dependency[pom:artifactId= 'blueprint-parser']/pom:scope"

%pom_change_dep org.osgi:org.osgi.core org.eclipse.osgi:org.eclipse.osgi:3.11.0.v20160714-1000
%pom_change_dep org.osgi:org.osgi.compendium org.eclipse.osgi:org.eclipse.osgi.services:3.5.100.v20160714-1000

%build

# tests disabled because of
# missing dependency on org.apache.aries.testsupport.unit
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_1jpp8
- new version

