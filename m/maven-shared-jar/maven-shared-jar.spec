Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-shared-jar
Version:        1.2
Release:        alt1_2jpp8
# Maven-shared defines maven-shared-jar version as 1.1
Epoch:          1
Summary:        Maven JAR Utilities
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-shared-jar
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:bcel-findbugs)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(org.apache.maven:maven-artifact:2.2.1)
BuildRequires:  mvn(org.apache.maven:maven-model:2.2.1)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-digest)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

Obsoletes:      maven-shared-jar < %{epoch}:%{version}-%{release} 
Provides:       maven-shared-jar = %{epoch}:%{version}-%{release}
Source44: import.info

%description
Utilities that help identify the contents of a JAR, including Java class
analysis and Maven metadata analysis.

This is a replacement package for maven-shared-jar

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch
    
%description javadoc
API documentation for %{name}.


%prep
%setup -q

find -type f -iname '*.jar' -delete

%build
# Tests require the jars that were removed
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.2-alt1_2jpp8
- new version

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt1_9jpp8
- new version

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt1_2jpp7
- update

* Sun Aug 24 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

