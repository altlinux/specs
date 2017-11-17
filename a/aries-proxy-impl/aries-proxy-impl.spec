Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat felix-osgi-compendium
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global bundle org.apache.aries.proxy.impl
Name:          aries-proxy-impl
Version:       1.0.5
Release:       alt2_2jpp8
Summary:       Apache Aries Proxy Service
License:       ASL 2.0
URL:           http://aries.apache.org/
#Source0:       http://www.apache.org/dist/aries/%%{bundle}-%%{version}-source-release.zip
Source0:       http://central.maven.org/maven2/org/apache/aries/proxy/%{bundle}/%{version}/%{bundle}-%{version}-source-release.zip

BuildRequires: maven-local
BuildRequires: mvn(org.apache.aries.proxy:org.apache.aries.proxy.api) >= 1.0.1
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi)
BuildRequires: mvn(org.ow2.asm:asm-debug-all)
BuildRequires: mvn(org.slf4j:slf4j-api)

Obsoletes:     aries-proxy < %{version}
Provides:      aries-proxy = %{version}-%{release}

BuildArch:     noarch
Source44: import.info

%description
This bundle contains the proxy service implementation for Apache Aries.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%pom_remove_parent

%pom_add_plugin org.apache.felix:maven-bundle-plugin . '
<extensions>true</extensions>
<configuration>
  <excludeDependencies>true</excludeDependencies>
  <instructions>
    <Bundle-Activator>${aries.osgi.activator}</Bundle-Activator>
    <Bundle-Name>${project.name}</Bundle-Name>
    <Bundle-SymbolicName>${project.artifactId}</Bundle-SymbolicName>
    <Bundle-Vendor>The Apache Software Foundation</Bundle-Vendor>
    <!--Export-Package>${aries.osgi.export.pkg}</Export-Package-->
    <Export-Service>${aries.osgi.export.service}</Export-Service>
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

# Cannot load implementation hint 'org.codehaus.mojo.animal_sniffer.enforcer.CheckSignatureRule'
%pom_remove_plugin :maven-enforcer-plugin

%pom_remove_plugin org.apache.aries.versioning:org.apache.aries.versioning.plugin

# Use eclipse apis
%pom_change_dep org.osgi:org.osgi.core org.eclipse.osgi:org.eclipse.osgi:3.10.102.v20160416-2200

# antrun plugin fails to process classes
sed -i '/delete dir/d' pom.xml

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
* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt2_2jpp8
- fixed build with new felix-utils

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_2jpp8
- new jpp release

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_1jpp8
- new version

