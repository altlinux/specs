%define _unpackaged_files_terminate_build 1

%def_without legacy_tests

Name: kotlinx-serialization
Version: 1.12.0
Release: alt1

Summary: Kotlin serialization libraries for JVM
License: Apache-2.0
Group: Development/Java
URL: https://github.com/Kotlin/kotlinx.serialization
VCS: https://github.com/Kotlin/kotlinx.serialization.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: system-gradle.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: java-17-openjdk-devel
BuildRequires: kotlin-compiler
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-gradle-plugin)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-serialization)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-reflect)
BuildRequires: kotlinx-coroutines
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-io-core-jvm)
BuildRequires: mvn(com.squareup.okio:okio-jvm)
BuildRequires: mvn(com.typesafe:config)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(com.google.guava:guava)

%if_with legacy_tests
BuildRequires: mvn(io.kotlintest:kotlintest)
BuildRequires: mvn(com.upokecenter:cbor)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-cbor)
BuildRequires: mvn(com.fasterxml.jackson.module:jackson-module-kotlin)
BuildRequires: protobuf-compiler
BuildRequires: protobuf-java
%endif

%description
Kotlin serialization core, JSON, CBOR, Protocol Buffers, properties and Hocon
libraries, including JSON integrations with kotlinx-io and Okio. This package
contains JVM implementations and multiplatform metadata with their BOM.
The complete upstream source archive retains other platform sources.

%prep
%setup
%autopatch -p1
# A 32-bit JVM cannot reserve the upstream 4 GiB heap.
if [ "$(getconf LONG_BIT)" = 32 ]; then
    sed -i 's/-Xmx4g/-Xmx1g/' gradle.properties
fi

%build
%gradle_publish --no-configuration-cache

%install
%gradle_register --artifacts=kotlinx-serialization-
%gradle_register_bom --artifacts=kotlinx-serialization-bom
%gradle_install

%check
%if_with legacy_tests
%gradle_check --no-configuration-cache
%else
# These two suites require unavailable legacy comparison/property test tools.
%gradle_check --no-configuration-cache \
    -x :kotlinx-serialization-cbor:jvmTest \
    -x :kotlinx-serialization-protobuf:jvmTest \
    -x :kotlinx-serialization-proto-test-model:check
%endif

%files -f .mfiles
%doc LICENSE.txt

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 1.12.0-alt1
- Initial build for ALT.
