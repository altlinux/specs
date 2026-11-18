%define _unpackaged_files_terminate_build 1

Name: jackson3-module-kotlin
Version: 3.3.0
Release: alt1

Summary: Jackson module for Kotlin data classes
License: Apache-2.0
Group: Development/Java
URL: https://github.com/FasterXML/jackson-module-kotlin
VCS: https://github.com/FasterXML/jackson-module-kotlin.git

Source: %name-%version.tar
Patch0: 0001-Use-standard-Kotlin-exception-assertions.patch
Patch1: 0002-Preserve-upstream-Kotlin-annotation-targets.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: kotlin-maven
BuildRequires: kotlin-reflect
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(tools.jackson:jackson-base:pom:)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(tools.jackson.core:jackson-core)
BuildRequires: mvn(tools.jackson.core:jackson-databind)
BuildRequires: mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit5)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(tools.jackson.dataformat:jackson-dataformat-csv)
BuildRequires: mvn(tools.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires: mvn(tools.jackson.dataformat:jackson-dataformat-xml)

BuildArch: noarch

%description
Jackson extension for Kotlin constructor parameters, data classes,
default arguments, nullability and Kotlin reflection.

%javadoc_package

%prep
%setup
%autopatch -p1
%pom_remove_plugin :gradle-module-metadata-maven-plugin
%pom_remove_plugin :cyclonedx-maven-plugin
# The offline target has no previous release for the binary ABI comparison.
%pom_remove_plugin :japicmp-maven-plugin
%mvn_file : %name

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-jackson-module-kotlin
%doc LICENSE

%changelog
* Sat Nov 14 2026 Ivan Khanas <xeno@altlinux.org> 3.3.0-alt1
- Initial build for ALT.
