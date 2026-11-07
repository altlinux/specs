%define _unpackaged_files_terminate_build 1
%def_with check
%define plugin_marker org.jetbrains.kotlinx.benchmark.gradle.plugin

Name: kotlinx-benchmark
Version: 0.5.0
Release: alt1

Summary: Kotlin benchmarking runtime and Gradle plugin
License: Apache-2.0
Group: Development/Java
URL: https://github.com/Kotlin/kotlinx-benchmark
VCS: https://github.com/Kotlin/kotlinx-benchmark.git

Source0: %name-%version.tar
Patch0: system-jvm.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-17-openjdk-devel
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-gradle-plugin)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-reflect)
BuildRequires: mvn(org.openjdk.jmh:jmh-core)
BuildRequires: mvn(org.openjdk.jmh:jmh-generator-bytecode)
BuildRequires: mvn(com.squareup:kotlinpoet-jvm)
BuildRequires: mvn(com.google.devtools.ksp:symbol-processing-aa-embeddable)
BuildRequires: mvn(com.google.devtools.ksp:symbol-processing-api)
BuildRequires: mvn(com.google.devtools.ksp:symbol-processing-common-deps)
%if_with check
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit5)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-json-jvm)
%endif
BuildArch: noarch

%description
Kotlin benchmarking toolkit with the complete upstream source tree. This
package contains the common metadata and complete JVM runtime, including the
JMH runner. Other platform runtime sources remain available in the source.

%package plugin
Summary: Kotlin benchmarking Gradle plugin
Group: Development/Java

%description plugin
The upstream benchmark Gradle plugin with its code generators and genuine
plugin marker, built from the same source release.

%prep
%setup
%autopatch -p1
# A 32-bit JVM cannot reserve the upstream 4 GiB heap.
if [ "$(getconf LONG_BIT)" = 32 ]; then
    sed -i 's/-Xmx4g/-Xmx1g/' gradle.properties
fi

%build
%gradle_publish -p alt-jvm -PaltVersion=%version

%install
%gradle_register --artifacts=kotlinx-benchmark-runtime-,%name-plugin-
plugin_repo=%_mavenrepolocal/repository/org/jetbrains/kotlinx/benchmark
marker_pom="$plugin_repo/%plugin_marker/%version"
%mvn_artifact "$marker_pom/%plugin_marker-%version.pom"
%mvn_package org.jetbrains.kotlinx:%name-plugin plugin
%mvn_package org.jetbrains.kotlinx.benchmark:%plugin_marker plugin
%gradle_install

%check
%if_with check
# Integration tests download Gradle distributions; compile them offline.
%gradle_check -p alt-jvm -PaltVersion=%version \
    :integration:testClasses -x :integration:test
%endif

%files -f .mfiles
%doc LICENSE

%files plugin -f .mfiles-plugin

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 0.5.0-alt1
- Initial build for ALT.
