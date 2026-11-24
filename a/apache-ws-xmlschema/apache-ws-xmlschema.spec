Name: apache-ws-xmlschema
Version: 2.3.3
Release: alt1

Summary: Java libraries for reading and writing XML Schema documents
License: Apache-2.0
Group: Development/Java
URL: https://ws.apache.org/xmlschema/
VCS: https://github.com/apache/ws-xmlschema
Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache:apache-jar-resource-bundle)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(jakarta.xml.bind:jakarta.xml.bind-api:2.3.3)
BuildRequires: mvn(com.google.guava:guava-testlib)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(xmlunit:xmlunit)

%description
Apache XMLSchema is a Java object model for loading, editing and generating
XML Schema documents.

%package walker
Summary: XML Schema traversal and document validation library
Group: Development/Java

%description walker
This module traverses XML Schema definitions and validates XML document paths
against their structure.

%prep
%setup -q
# This reactor module is an OSGi integration test, using the Pax Exam harness.
%pom_disable_module xmlschema-bundle-test
# Keep unit and W3C tests, and skip the Checkstyle and PMD profile.
%pom_xpath_remove "pom:project/pom:profiles/pom:profile[pom:id='sourcecheck']"
build='pom:project/pom:build'
plugins='pom:plugins/pom:plugin'
%pom_xpath_set \
    "$build/$plugins[pom:artifactId='maven-enforcer-plugin']/pom:version" 3.6.2

%build
%mvn_package :xmlschema %name
%mvn_package :xmlschema-core %name
%mvn_package :xmlschema-walker %name-walker
%mvn_package :w3c-testcases __noinstall
%mvn_build -s -j

%install
%mvn_install

%files -f .mfiles-%name
%doc README.txt RELEASE-NOTE.txt

%files walker -f .mfiles-%name-walker

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 2.3.3-alt1
- Initial build for ALT.
