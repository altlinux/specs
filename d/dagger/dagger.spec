%define _unpackaged_files_terminate_build 1

Name: dagger
Version: 2.60.1
Release: alt1

Summary: Compile-time dependency injection for Java and Kotlin
License: Apache-2.0
Group: Development/Java
URL: https://dagger.dev/
VCS: https://github.com/google/dagger.git

Source: %name-%version.tar
Source1: alt-build.tar
Source2: room3-compiler-processing-3.0.3-sources.jar
Source3: room3-compiler-processing-testing-3.0.3-sources.jar
Source4: dagger-2.60.1-sources.jar
Source5: dagger-spi-2.60.1-sources.jar
Source6: dagger-compiler-2.60.1-sources.jar
Patch: system-build.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-21-openjdk-devel
BuildRequires: xgradle
BuildRequires: kotlin
BuildRequires: kotlin-compiler
BuildRequires: kotlin-symbol-processing
BuildRequires: kotlinpoet
BuildRequires: kotlinpoet-javapoet
BuildRequires: javapoet
BuildRequires: guava
BuildRequires: guava-testlib
BuildRequires: auto-common
BuildRequires: auto-value
BuildRequires: auto-value-annotations
BuildRequires: auto-service
BuildRequires: incap
BuildRequires: atinject
BuildRequires: atinject-javax
BuildRequires: jspecify
BuildRequires: google-error-prone-annotations
BuildRequires: jsr-305
BuildRequires: google-java-format
BuildRequires: compile-testing
BuildRequires: jetbrains-annotations
BuildRequires: truth
BuildRequires: junit
BuildRequires: mockito-core
BuildRequires: python3

%description
Dagger generates dependency injection code at compile time for Java and Kotlin.
This package includes the runtime, producers, SPI, compiler, Android processor
and Hilt core/compiler. Room3 compiler-processing libraries are built from
sources in the same build to bootstrap the annotation processor.

%prep
%setup
%autopatch -p1
mkdir .gear
tar -xf %SOURCE1 -C .gear
mkdir .gear/source-inputs
cp -p %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 %SOURCE6 .gear/source-inputs/
python3 .gear/alt-build/prepare-sources.py

%build
cd .gear/alt-build
%gradle_publish

%install
cd .gear/alt-build
dagger_artifacts="dagger-%version.pom"
for artifact in dagger-producers dagger-spi dagger-compiler \
    dagger-android-processor hilt-core hilt-compiler; do
    dagger_artifacts="$dagger_artifacts,$artifact-%version.pom"
done
dagger_artifacts="$dagger_artifacts,room3-compiler-processing-3.0.3.pom"
dagger_artifacts="$dagger_artifacts,room3-compiler-processing-testing-3.0.3.pom"
%gradle_register --artifacts="$dagger_artifacts"
%gradle_install

%check
cd .gear/alt-build
%gradle_check

%files -f .gear/alt-build/.mfiles
%doc LICENSE.txt

%changelog
* Tue Nov 03 2026 Ivan Khanas <xeno@altlinux.org> 2.60.1-alt1
- Initial build for ALT.
