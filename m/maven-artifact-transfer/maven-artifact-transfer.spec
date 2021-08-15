Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           maven-artifact-transfer
Version:        0.13.1
Release:        alt1_3jpp11
Epoch:          1
Summary:        Apache Maven Artifact Transfer
License:        ASL 2.0
URL:            https://maven.apache.org/shared/maven-artifact-transfer
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch0:         0001-Compatibility-with-Maven-3.0.3-and-later.patch
Patch1:         0002-Remove-support-for-maven-3.0.X.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-impl)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
%endif
Source44: import.info

%description
An API to either install or deploy artifacts with Maven 3.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -q
find -name '*.java' -exec sed -i 's/\r//' {} +
%patch0 -p1
%patch1 -p1

%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin

# We don't want to support legacy Maven versions (older than 3.1)
%pom_remove_dep org.sonatype.aether:
find -name Maven30\*.java -delete

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 1:0.13.1-alt1_3jpp11
- new version

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 1:0.11.0-alt1_2jpp11
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1:0.9.0-alt1_6jpp8
- new version

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.9.0-alt1_3jpp8
- upstream version 0.9

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_0.3.20160118svn1722498jpp8
- new version

