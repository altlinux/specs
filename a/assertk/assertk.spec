%define _unpackaged_files_terminate_build 1

Name: assertk
Version: 0.28.1
Release: alt1

Summary: Fluent assertions for Kotlin and coroutines
License: MIT
Group: Development/Java
Url: https://github.com/willowtreeapps/assertk
VCS: https://github.com/willowtreeapps/assertk.git
BuildArch: noarch

Source: %name-%version.tar
Patch: system-gradle.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-build-statistics
BuildRequires: kotlin-compiler
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlin-tooling-core
BuildRequires: kotlinx-coroutines
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: mvn(com.willowtreeapps.opentest4k:opentest4k-jvm)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-reflect)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test)

%description
AssertK provides fluent assertions for Kotlin, inspired by AssertJ.
This package includes the JVM libraries and common Kotlin metadata for
AssertK and its coroutines assertions module.

%prep
%setup
%patch -p1

%build
%gradle_publish --no-daemon --max-workers=2 \
    -PreleaseVersion=%version \
    -Pkotlin.compiler.execution.strategy=in-process

%install
%gradle_register --artifacts=assertk-
%gradle_install

%check
%gradle_check --no-daemon --max-workers=2 \
    -PreleaseVersion=%version \
    -Pkotlin.compiler.execution.strategy=in-process

%files -f .mfiles
%doc LICENSE README.md CHANGELOG.md

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 0.28.1-alt1
- Initial build for ALT.
