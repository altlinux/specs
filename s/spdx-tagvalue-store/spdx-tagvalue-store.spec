%define _unpackaged_files_terminate_build 1

Name: spdx-tagvalue-store
Version: 2.0.5
Release: alt1

Summary: SPDX tag/value serialization and deserialization library
License: Apache-2.0
Group: Development/Java
URL: https://github.com/spdx/spdx-java-tagvalue-store
VCS: https://github.com/spdx/spdx-java-tagvalue-store
Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.spdx:java-spdx-library)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)

%description
An SPDX library for serializing and deserializing tag/value files.

%prep
%setup -q
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-release-plugin
%pom_remove_plugin org.sonarsource.scanner.maven:sonar-maven-plugin
%pom_remove_plugin org.spdx:spdx-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_add_plugin org.apache.maven.plugins:maven-surefire-plugin:3.5.6

%build
%mvn_build -s -j

%install
%mvn_install

%files -f .mfiles-spdx-tagvalue-store
%doc README.md LICENSE

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 2.0.5-alt1
- Initial build for ALT.
