%define _unpackaged_files_terminate_build 1

Name: spdx-java-jackson-store
Version: 2.0.7
Release: alt1

Summary: Jackson store implementation for SPDX Java
License: Apache-2.0
Group: Development/Java
URL: https://github.com/spdx/spdx-java-jackson-store
VCS: https://github.com/spdx/spdx-java-jackson-store
Source0: %name-%version.tar
Patch0: unavailable-json-schema-test.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.spdx:java-spdx-library)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires: mvn(org.json:json)
BuildRequires: mvn(junit:junit)

%description
Jackson-based Java store for reading and writing SPDX documents.

%prep
%setup -q
%patch0 -p1
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-release-plugin
%pom_remove_plugin org.spdx:spdx-maven-plugin
%pom_remove_dep com.github.java-json-tools:json-schema-validator

%build
%mvn_build -s -j

%install
%mvn_install

%files -f .mfiles-spdx-jackson-store
%doc README.md LICENSE

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 2.0.7-alt1
- Initial build for ALT.
