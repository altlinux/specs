%define _unpackaged_files_terminate_build 1

Name: spdx-v3jsonld-store
Version: 1.0.6
Release: alt1

Summary: SPDX v3 JSON-LD document store
License: Apache-2.0
Group: Development/Java
URL: https://github.com/spdx/spdx-java-v3jsonld-store
VCS: https://github.com/spdx/spdx-java-v3jsonld-store.git
Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.spdx:java-spdx-library)
BuildRequires: mvn(commons-validator:commons-validator)
BuildRequires: mvn(org.metaeffekt.bundle.jsonschemafriend:ae-jsonschemafriend-core)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires: mvn(org.json:json)
BuildRequires: mvn(junit:junit)

%description
SPDX v3 JSON-LD Store reads and writes SPDX documents using JSON-LD.

%prep
%setup -q
%pom_change_dep \
    com.fasterxml.jackson.core:jackson-core:2.22.2 \
    com.fasterxml.jackson.core:jackson-core:2.22.1
%pom_change_dep \
    com.fasterxml.jackson.core:jackson-databind:2.22.2 \
    com.fasterxml.jackson.core:jackson-databind:2.22.1
%pom_change_dep \
    com.fasterxml.jackson.dataformat:jackson-dataformat-xml:2.22.2 \
    com.fasterxml.jackson.dataformat:jackson-dataformat-xml:2.22.1
%pom_change_dep \
    com.fasterxml.jackson.dataformat:jackson-dataformat-yaml:2.22.2 \
    com.fasterxml.jackson.dataformat:jackson-dataformat-yaml:2.22.4
%pom_remove_dep com.github.java-json-tools:json-schema-validator
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin org.spdx:spdx-maven-plugin

%build
%mvn_build -s -j

%install
%mvn_install

%files -f .mfiles-%name
%doc LICENSE README.md

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 1.0.6-alt1
- Initial build for ALT.
