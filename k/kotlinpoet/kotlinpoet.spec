%define _unpackaged_files_terminate_build 1

Name: kotlinpoet
Version: 2.4.0
Release: alt1

Summary: Kotlin source generation API and metadata and KSP extensions
License: Apache-2.0
Group: Development/Java
Url: https://square.github.io/kotlinpoet
VCS: https://github.com/square/kotlinpoet.git

Source: %name-%version.tar
Patch: system-build.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-17-openjdk-devel
BuildRequires: kotlin-compiler
BuildRequires: kotlin-gradle-plugin
BuildRequires: xgradle
BuildRequires: mvn(com.google.auto:auto-common)
BuildRequires: mvn(com.google.devtools.ksp:symbol-processing-api)
BuildRequires: mvn(com.google.jimfs:jimfs)
BuildRequires: mvn(com.google.testing.compile:compile-testing)
BuildRequires: mvn(com.willowtreeapps.assertk:assertk-jvm)
BuildRequires: mvn(org.eclipse.jdt:ecj)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-reflect)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test)

%description
KotlinPoet is a Kotlin and Java API for generating Kotlin source files.
This package includes the JVM library, Kotlin metadata extensions and
Kotlin Symbol Processing interoperability extensions.

%prep
%setup
%patch -p1
mv settings.gradle.kts settings.gradle.kts.upstream
cp alt-settings.gradle settings.gradle

%build
# Gradle 9.7 does not support the default JDK 27 launcher.
%gradle_publish --no-daemon --max-workers=2 \
    -Pkotlin.compiler.execution.strategy=in-process

%install
%gradle_register --artifacts=kotlinpoet-jvm-,kotlinpoet-metadata-,kotlinpoet-ksp-
%mvn_artifact %_mavenrepolocal/repository/com/squareup/kotlinpoet/%version/kotlinpoet-%version.pom
%gradle_install

%check
%gradle_check --no-daemon --max-workers=2 \
    -Pkotlin.compiler.execution.strategy=in-process

%files -f .mfiles
%doc LICENSE.txt README.md

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 2.4.0-alt1
- Initial build for ALT.
