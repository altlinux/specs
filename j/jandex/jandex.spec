%define _unpackaged_files_terminate_build 1

Name: jandex
Version: 3.6.0
Release: alt1

Summary: Java annotation indexer
License: Apache-2.0
Group: Development/Java
URL: https://smallrye.io/jandex/
VCS: https://github.com/smallrye/jandex.git

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: rpm-build-java
BuildRequires: java-17-openjdk-devel
BuildRequires: kotlin
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.moditect:moditect-maven-plugin)
BuildRequires: mvn(org.jboss.bridger:bridger)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)

%description
Jandex is a Java annotation indexer and offline reflection library. It builds
an index of class files for fast runtime annotation lookup.

%prep
%setup -q
%pom_remove_parent
# Compile the Kotlin fixture directly: the system Maven extension has
# unresolved kotlin-build-tools-api/impl dependencies. Keep Kotlin tests.
%pom_remove_plugin org.jetbrains.kotlin:kotlin-maven-plugin test-data-kotlin
# Nested integration builds use their own repositories and Groovy hooks.
%pom_remove_plugin org.apache.maven.plugins:maven-invoker-plugin maven-plugin

%mvn_file :jandex jandex
%mvn_file :jandex-maven-plugin jandex-maven-plugin
%mvn_package :jandex-test-data __noinstall
%mvn_package :jandex-test-data-kotlin __noinstall

%build
mkdir -p test-data-kotlin/target/classes
kotlinc -jvm-target 1.8 \
    test-data-kotlin/src/main/kotlin/kotest/KoClass.kt \
    -d test-data-kotlin/target/classes
# Aggregate Javadoc mixes Java 17 fixtures with the Java 8 production API.
%mvn_build -j -- -pl core,maven-plugin -am

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 3.6.0-alt1
- Initial build for ALT.
