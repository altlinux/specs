%define _unpackaged_files_terminate_build 1

Name: cash-burst
Version: 2.14.0
Release: alt1

Summary: Parameterized Kotlin tests with a compiler and Gradle plugin
License: Apache-2.0
Group: Development/Java
URL: https://github.com/cashapp/burst
VCS: https://github.com/cashapp/burst.git
BuildArch: noarch

Source: %name-%version.tar
Patch: system-gradle.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-gradle-plugin
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: kotlin-compiler
BuildRequires: kotlin-stdlib
BuildRequires: kotlin-test
BuildRequires: kotlin-reflect
BuildRequires: kotlin-tooling-core
BuildRequires: kotlin-build-statistics
BuildRequires: kotlinx-coroutines
BuildRequires: assertk
BuildRequires: junit
BuildRequires: junit5
BuildRequires: kotlin-compile-testing

%description
Burst generates parameterized Kotlin tests. This package provides its JVM
runtime, coroutines support, Kotlin IR compiler plugin and Gradle plugin,
including common Kotlin metadata. Native, JavaScript and Wasm targets are
not built in this RPM.

%prep
%setup
%autopatch -p1

%build
%gradle_publish --no-daemon --max-workers=2 \
    -Pkotlin.compiler.execution.strategy=in-process

%install
%gradle_register --artifacts=burst- --exclude-artifacts=burst-gradle-plugin-
%gradle_install
install -d %buildroot%_javadir %buildroot%_mavenpomdir
%gradle_install_plugin \
    --artifacts=burst-gradle-plugin-,app.cash.burst.gradle.plugin-

%check
# TestKit requires downloaded Gradle/Android/native/JS toolchains.
# Verify the installed JVM plugin separately with system Gradle.
%gradle_check --no-daemon --max-workers=2 \
    -x :burst-gradle-plugin:test \
    -Pkotlin.compiler.execution.strategy=in-process

%files -f .mfiles
%doc LICENSE
%_javadir/%name/burst-gradle-plugin.jar
%_mavenpomdir/%name/burst-gradle-plugin.pom
%_mavenpomdir/%name/app.cash.burst.gradle.plugin.pom

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 2.14.0-alt1
- Initial build for ALT.
