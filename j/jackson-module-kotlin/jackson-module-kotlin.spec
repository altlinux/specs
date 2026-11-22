%define _unpackaged_files_terminate_build 1

Name: jackson-module-kotlin
Version: 2.22.4
Release: alt1

Summary: Jackson module for Kotlin data classes
License: Apache-2.0
Group: Development/Java
URL: https://github.com/FasterXML/jackson-module-kotlin
VCS: https://github.com/FasterXML/jackson-module-kotlin.git
BuildArch: noarch

Source: %name-%version.tar
Patch0: system-tests.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: rpm-build-java
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-maven-plugin)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-reflect)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(com.fasterxml.jackson:jackson-base:pom:)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-csv)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml)
BuildRequires: mvn(com.fasterxml.jackson.datatype:jackson-datatype-jsr310)
BuildRequires: mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires: mvn(org.moditect:moditect-maven-plugin)

%description
Jackson extension for Kotlin constructor parameters, data classes,
default arguments, nullability and Kotlin reflection.

%javadoc_package

%prep
%setup -q
%autopatch -p1

%pom_xpath_set pom:properties/pom:version.kotlin 2.4.21
# Kotlin 2.4 removed the upstream 1.9 language mode; keep Java 8 bytecode.
%pom_xpath_set //pom:apiVersion 2.0
%pom_xpath_set //pom:languageVersion 2.0
%pom_remove_plugin :gradle-module-metadata-maven-plugin
%pom_remove_plugin :cyclonedx-maven-plugin
# The offline target has no previous release for the binary ABI comparison.
%pom_remove_plugin :japicmp-maven-plugin

%mvn_file : jackson-module-kotlin

%build
# Kotlin's system Maven plugin pins plugin-tools annotations 3.7.0; use the
# current Sisyphus provider (3.9.0) for its binary-compatible plugin API.
%mvn_build -s -- -Dmaven-plugin-annotations.version=3.9.0

%install
%mvn_install

%files -f .mfiles-jackson-module-kotlin
%doc LICENSE

%changelog
* Fri Nov 20 2026 Ivan Khanas <xeno@altlinux.org> 2.22.4-alt1
- Initial build for ALT.
