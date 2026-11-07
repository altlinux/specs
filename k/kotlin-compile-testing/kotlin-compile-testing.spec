%define _unpackaged_files_terminate_build 1

Name: kotlin-compile-testing
Version: 0.14.0
Release: alt1

Summary: Kotlin compiler and annotation processor testing harness
License: MPL-2.0
Group: Development/Java
URL: https://github.com/ZacSweers/kotlin-compile-testing
VCS: https://github.com/ZacSweers/kotlin-compile-testing.git

Source: %name-%version.tar
Patch: system-build.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-gradle-plugin
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: kotlin-compiler
BuildRequires: kotlin-ide
BuildRequires: kotlin-test
BuildRequires: kotlin-symbol-processing
BuildRequires: kotlinpoet
BuildRequires: mockito-kotlin
BuildRequires: auto-service
BuildRequires: classgraph
BuildRequires: okio-jvm
BuildRequires: javapoet
BuildRequires: assertj-core

%description
Kotlin Compile Testing provides a test harness for Kotlin annotation
processors, compiler plugins and code generation. It includes the core
compiler harness and the Kotlin Symbol Processing integration.

%prep
%setup
%autopatch -p1
mv build.gradle.kts build.gradle.kts.upstream
mv settings.gradle.kts settings.gradle.kts.upstream
for module in core ksp test-annotations test-processor; do
    mv "$module/build.gradle.kts" "$module/build.gradle.kts.upstream"
done
cp alt-build.gradle build.gradle
cp alt-settings.gradle settings.gradle

%build
%gradle_publish --no-daemon --max-workers=2 \
    -Pkotlin.compiler.execution.strategy=in-process

%install
%gradle_register --artifacts=core-,ksp-
%gradle_install

%check
%gradle_check --no-daemon --max-workers=2 \
    -Pkotlin.compiler.execution.strategy=in-process

%files -f .mfiles
%doc LICENSE

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 0.14.0-alt1
- Initial build for ALT.
