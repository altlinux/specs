%define _unpackaged_files_terminate_build 1

Name: kotlinx-datetime
Version: 0.8.0
Release: alt1

Summary: Kotlin date and time library for the JVM
License: Apache-2.0 AND BSD-3-Clause
Group: Development/Java
URL: https://github.com/Kotlin/kotlinx-datetime
VCS: https://github.com/Kotlin/kotlinx-datetime.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: system-gradle.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-gradle-plugin)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-serialization)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-core)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-core-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-json)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-json-jvm)

%description
Date and time library for Kotlin JVM applications with calendar arithmetic,
time zones, parsing and formatting. Includes JVM implementation and genuine
multiplatform metadata. The complete upstream source tree is retained.

%prep
%setup
%autopatch -p1

%build
%gradle_publish --no-configuration-cache

%install
%gradle_register --artifacts=kotlinx-datetime
%gradle_install

%check
%gradle_check --no-configuration-cache

%files -f .mfiles
%doc LICENSE.txt license/thirdparty/threetenbp_license.txt

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 0.8.0-alt1
- Initial build for ALT.
