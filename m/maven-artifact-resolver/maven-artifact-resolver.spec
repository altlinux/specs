Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-artifact-resolver
Version:        1.0
Release:        alt1_9jpp7
# Epoch is added because the original package's version in maven-shared is 1.1-SNAPSHOT
Epoch:          1
Summary:        Maven Artifact Resolution API
License:        ASL 2.0
URL:            http://maven.apache.org/shared/%{name}
Source0:        http://central.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Replaced plexus-maven-plugin with plexus-component-metadata
Patch0:         %{name}-plexus.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-artifact-manager)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.easymock:easymock)

Obsoletes:      maven-shared-artifact-resolver < %{epoch}:%{version}-%{release}
Provides:       maven-shared-artifact-resolver = %{epoch}:%{version}-%{release}
Source44: import.info

%description
Provides a component for plugins to easily resolve project dependencies.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q
%patch0 -p1

%pom_xpath_inject pom:project/pom:dependencies "
<dependency>
  <groupId>org.apache.maven</groupId>
  <artifactId>maven-compat</artifactId>
  <version>1.0</version>
</dependency>" pom.xml

# Incompatible method invocation
rm src/test/java/org/apache/maven/shared/artifact/resolver/DefaultProjectDependenciesResolverIT.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc DEPENDENCIES LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_7jpp7
- new release

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_4jpp7
- update

