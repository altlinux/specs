%define _unpackaged_files_terminate_build 1

Name: spdx-rdf-store
Version: 2.0.4
Release: alt1
Summary: SPDX RDF document store
License: Apache-2.0
Group: Development/Java
URL: https://github.com/spdx/spdx-java-rdf-store
VCS: https://github.com/spdx/spdx-java-rdf-store.git
Source0: %{name}-%{version}.tar.gz

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.spdx:java-spdx-library) = 2.0.5
BuildRequires: mvn(org.apache.jena:jena-core) = 5.6.0
BuildRequires: mvn(org.apache.jena:jena-arq) = 5.6.0
BuildRequires: mvn(org.apache.jena:jena-base) = 5.6.0
BuildRequires: mvn(org.apache.logging.log4j:log4j-bom:pom:) = 2.25.4
BuildRequires: mvn(org.apache.logging.log4j:log4j-core) = 2.25.4
BuildRequires: mvn(org.apache.logging.log4j:log4j-slf4j-impl) = 2.25.4
BuildRequires: mvn(junit:junit) = 4.13.2

BuildArch: noarch

%description
SPDX RDF Store reads and writes SPDX documents using Apache Jena.

%prep
%setup -q
%pom_change_dep org.spdx:java-spdx-library:2.0.4 org.spdx:java-spdx-library:2.0.5
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin org.spdx:spdx-maven-plugin

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}
%doc LICENSE README.md
%{_javadocdir}/%{name}

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 2.0.4-alt1
- Package SPDX RDF Store for Sisyphus.
- Use the singleton-generated per-package files manifest.
- Package the generated API Javadoc directory.
