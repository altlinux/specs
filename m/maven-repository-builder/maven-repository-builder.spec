Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-repository-builder
Version:        1.0
Release:        alt3_4jpp8
# Maven-shared defines maven-repository-builder version as 1.0
Epoch:          1
Summary:        Maven repository builder
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-repository-builder/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/maven-repository-builder/1.0/maven-repository-builder-%{version}-source-release.zip
# ASL mandates that the licence file be included in redistributed source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-artifact-manager)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven.shared:maven-test-tools)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-file)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http-lightweight)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
Source44: import.info

%description
Maven repository builder.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch
    
%description javadoc
This package provides %{summary}.

%prep
%setup -q

# Replace plexus-maven-plugin with plexus-component-metadata
find -name 'pom.xml' -exec sed \
    -i 's/<artifactId>plexus-maven-plugin<\/artifactId>/<artifactId>plexus-component-metadata<\/artifactId>/' '{}' ';'
find -name 'pom.xml' -exec sed \
    -i 's/<goal>descriptor<\/goal>/<goal>generate-metadata<\/goal>/' '{}' ';'

# Removing JARs because of binary code contained
find -iname '*.jar' -delete

cp %{SOURCE1} LICENSE.txt

%pom_add_dep org.apache.maven:maven-compat:3.3.3

%build
# Skipping tests because they don't work without the JARs
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt3_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt3_2jpp8
- new version

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_0.3.alpha2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_0.0.alpha2jpp7
- new release

