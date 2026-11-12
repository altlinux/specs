%define _unpackaged_files_terminate_build 1

%def_without upstream_tests
%define kaml_upstream_tests false
%if_with upstream_tests
%define kaml_upstream_tests true
%endif

Name: kaml
Version: 0.104.0
Release: alt1

Summary: YAML support for Kotlin serialization
License: Apache-2.0
Group: Development/Java
URL: https://github.com/charleskorn/kaml
VCS: https://github.com/charleskorn/kaml.git
BuildArch: noarch

Source: %name-%version.tar
Patch: system-jvm.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlin-stdlib
BuildRequires: kotlinx-serialization
BuildRequires: snakeyaml-engine-kmp
BuildRequires: okio
BuildRequires: kotlin-test
BuildRequires: junit5
%if_with upstream_tests
BuildRequires: mvn(io.kotest:kotest-assertions-core-jvm)
BuildRequires: mvn(io.kotest:kotest-framework-engine-jvm)
BuildRequires: mvn(io.kotest:kotest-runner-junit5-jvm)
BuildRequires: kotlinx-coroutines
%endif

%description
Kaml implements YAML serialization and deserialization for Kotlin
serialization, with polymorphism, anchors, custom tags and configurable
formatting. This package contains the JVM library and genuine common
publication metadata. Complete multiplatform upstream sources are retained.

%prep
%setup
%autopatch -p1

%build
%gradle_publish -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk -p alt-jvm --no-daemon \
    -Pkotlin.compiler.execution.strategy=in-process \
    -PupstreamTests=%kaml_upstream_tests

%install
%gradle_register --artifacts=kaml
%gradle_install

%check
%gradle_check -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk -p alt-jvm --no-daemon \
    -Pkotlin.compiler.execution.strategy=in-process \
    -PupstreamTests=%kaml_upstream_tests

%files -f .mfiles
%doc LICENSE

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 0.104.0-alt1
- Initial build for ALT.
