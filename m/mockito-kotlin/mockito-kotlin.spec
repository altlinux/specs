%define _unpackaged_files_terminate_build 1

Name: mockito-kotlin
Version: 6.4.0
Release: alt1

Summary: Kotlin helpers for Mockito
License: MIT
Group: Development/Java
URL: https://github.com/mockito/mockito-kotlin
VCS: https://github.com/mockito/mockito-kotlin.git

Source: %name-%version.tar
Patch: %name-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlinx-coroutines
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-reflect)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-coroutines-core-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-coroutines-test-jvm)
BuildRequires: mockito
BuildRequires: mvn(com.nhaarman:expect.kt)
BuildRequires: mvn(junit:junit)

%description
Mockito-Kotlin provides Kotlin helpers and extensions for Mockito,
including type-safe matchers, stubbing and verification of suspending calls.

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register --artifacts=mockito-kotlin
%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc LICENSE

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 6.4.0-alt1
- Initial build for ALT.
