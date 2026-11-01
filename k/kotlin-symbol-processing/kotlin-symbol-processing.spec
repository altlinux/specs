%define _unpackaged_files_terminate_build 1

Name: kotlin-symbol-processing
Version: 2.3.12
Release: alt1

Summary: Kotlin Symbol Processing libraries and Analysis API implementation
License: Apache-2.0
Group: Development/Java
Url: https://github.com/google/ksp
VCS: https://github.com/google/ksp.git

Source: %name-%version.tar
Patch: system-build.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-17-openjdk-devel
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-bootstrap-libs
BuildRequires: kotlin-compiler
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlin-ide
BuildRequires: xgradle
BuildRequires: mvn(com.github.ben-manes.caffeine:caffeine)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-core-jvm)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-reflect)

%description
Kotlin Symbol Processing provides an API for developing lightweight compiler
plugins. This package contains the symbol API, common utilities, command-line
configuration and the Kotlin Analysis API implementation. The implementation
uses the system Kotlin compiler and Analysis API libraries.

%prep
%setup
%patch -p1
mv buildSrc buildSrc.upstream
mv build.gradle.kts build.gradle.kts.upstream
mv settings.gradle.kts settings.gradle.kts.upstream
cp alt-build.gradle build.gradle
cp alt-settings.gradle settings.gradle
mkdir config-bootstrap parser-bootstrap

%build
%gradle_publish --no-daemon --max-workers=2 -PkspVersion=%version \
    -Pkotlin.compiler.execution.strategy=in-process

%install
%gradle_register --artifacts=symbol-processing-,cmdline-parser-gen-,test-utils-
%gradle_install

%check
%gradle_check --no-daemon --max-workers=2 -PkspVersion=%version \
    -Pkotlin.compiler.execution.strategy=in-process

%files -f .mfiles
%doc LICENSE README.md

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 2.3.12-alt1
- Initial build for ALT.
