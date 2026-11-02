%define _unpackaged_files_terminate_build 1

Name: kotlinx-collections-immutable
Version: 0.5.2
Release: alt1

Summary: Persistent immutable collections for Kotlin on the JVM
License: Apache-2.0
Group: Development/Java
Url: https://github.com/Kotlin/kotlinx.collections.immutable
VCS: https://github.com/Kotlin/kotlinx.collections.immutable.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-jvm.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: rpm-build-java-osgi
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlin-tooling-core
BuildRequires: kotlin-build-statistics
BuildRequires: kotlin-stdlib
BuildRequires: kotlin-test
BuildRequires: guava-testlib
BuildRequires: junit

%description
Persistent immutable lists, maps and sets for Kotlin. This package provides
org.jetbrains.kotlinx:kotlinx-collections-immutable-jvm for JVM consumers.

%prep
%setup -q
%patch0 -p1
# Upstream includes a wrapper binary; use the system Gradle exclusively.
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete

%build
%gradle_publish \
    -x :kotlinx-collections-immutable:publishKotlinMultiplatformPublicationToMavenLocal

%install
%gradle_register --artifacts=kotlinx-collections-immutable-jvm-
%gradle_install

%check
# Run common and JVM tests.
%gradle_check

%files -f .mfiles
%doc LICENSE.txt CHANGELOG.md

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 0.5.2-alt1
- Initial build for ALT.
