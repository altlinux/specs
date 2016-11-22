Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             maven-shared-jarsigner
Version:          1.3.2
Release:          alt1_4jpp8
Summary:          Component to assist in signing Java archives
License:          ASL 2.0
URL:              http://maven.apache.org/shared/maven-jarsigner/
BuildArch:        noarch

Source0:          http://repo1.maven.org/maven2/org/apache/maven/shared/maven-jarsigner/%{version}/maven-jarsigner-%{version}-source-release.zip

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils) >= 0.6
BuildRequires:  mvn(org.apache.maven:maven-toolchain)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
Source44: import.info

%description
Apache Maven Jarsigner is a component which provides utilities to sign
and verify Java archive and other files in your Maven MOJOs.

%package javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -qn maven-jarsigner-%{version}
find -name \*.jar -delete

%build
# Tests require bundled JARs, which are removed.
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE README.TXT

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_3jpp8
- new version

