Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global bundle org.apache.aries.quiesce.manager
Name:          aries-quiesce-manager
Version:       1.0.0
Release:       alt1_3jpp8
Summary:       Apache Aries Quiesce Manager
License:       ASL 2.0
URL:           http://aries.apache.org/
Source0:       http://www.apache.org/dist/aries/%{bundle}-%{version}-source-release.zip

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.aries:org.apache.aries.util) >= 1.0.0
BuildRequires: mvn(org.apache.aries:org.apache.aries.util-r42) >= 1.0.0
BuildRequires: mvn(org.apache.aries.quiesce:org.apache.aries.quiesce.api) >= 1.0.0
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-simple)

Obsoletes:     aries-quiesce < 0.4
Provides:      aries-quiesce = %{version}-%{release}

BuildArch:     noarch
Source44: import.info

%description
Aries Quiesce Manager. A quiesce manager provides the
functionality to stop bundles in such a manner that
currently running work can be safely finished.

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
    <Export-Service>${aries.osgi.export.service}</Export-Service>
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

# Use eclipse apis
%pom_change_dep org.osgi:org.osgi.core org.eclipse.osgi:org.eclipse.osgi:3.10.102.v20160416-2200

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3jpp8
- new version

