%define _unpackaged_files_terminate_build 1

Name: kotlin-semver
Version: 3.1.0
Release: alt1

Summary: Kotlin Multiplatform library for semantic versioning
License: MIT
Group: Development/Java
URL: https://github.com/z4kn4fein/kotlin-semver
VCS: https://github.com/z4kn4fein/kotlin-semver

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-gradle-plugin)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-serialization)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-core)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-core-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-json)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-json-jvm)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit)

BuildArch: noarch

%description
Kotlin SemVer is a Kotlin Multiplatform library for parsing, comparing and
validating semantic versions and constraints. This package publishes the
common metadata and JVM artifacts from the upstream source.

%prep
%setup -q
%autopatch -p1

if [ "$(getconf LONG_BIT)" = 32 ]; then
    sed -i -e '/^org\.gradle\.jvmargs/s/-Xmx3g/-Xmx768m/' \
        gradle.properties
fi

%build
%gradle_publish

%install
%gradle_register --artifacts=semver,semver-jvm
%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc LICENSE
%doc CHANGELOG.md Module.md

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 3.1.0-alt1
- Initial build for ALT.
