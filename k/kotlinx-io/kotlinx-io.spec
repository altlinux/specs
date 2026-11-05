%define _unpackaged_files_terminate_build 1

Name: kotlinx-io
Version: 0.9.2
Release: alt1

Summary: Kotlin IO and immutable byte strings for the JVM
License: Apache-2.0
Group: Development/Java
URL: https://github.com/Kotlin/kotlinx-io
VCS: https://github.com/Kotlin/kotlinx-io.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-jvm.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: glibc-utils
BuildRequires: rpm-build-java-osgi
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlin-maven
BuildRequires: kotlin-build-statistics
BuildRequires: kotlin-tooling-core
BuildRequires: kotlin-stdlib
BuildRequires: kotlin-test
BuildRequires: junit5
BuildRequires: mvn(com.squareup.okio:okio)
BuildRequires: mvn(com.squareup.okio:okio-jvm)

%description
Kotlin multiplatform IO primitives and immutable byte strings. This package
provides the core, byte strings and Okio integration for JVM consumers.

%prep
%setup -q
%autopatch -p1
# Reduce the Gradle heap on 32-bit build hosts.
if [ "$(getconf LONG_BIT)" = 32 ]; then
    sed -i \
        's/^org\.gradle\.jvmargs=-Xmx4G$/org.gradle.jvmargs=-Xmx1g/' \
    gradle.properties
fi
# Use system Gradle; remove the archived upstream wrapper binary.
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete

%build
%gradle_publish \
    -PDeployVersion=%version \
    -x :kotlinx-io-core:publishKotlinMultiplatformPublicationToMavenLocal \
    -x \
    :kotlinx-io-bytestring:publishKotlinMultiplatformPublicationToMavenLocal \
    -x :kotlinx-io-okio:publishKotlinMultiplatformPublicationToMavenLocal

%install
artifacts=kotlinx-io-core-jvm-
artifacts="$artifacts,kotlinx-io-bytestring-jvm-,kotlinx-io-okio-jvm-"
%gradle_register --artifacts="$artifacts"
%gradle_install

%check
# Run common and JVM tests.
%gradle_check -PDeployVersion=%version

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Tue Nov 03 2026 Ivan Khanas <xeno@altlinux.org> 0.9.2-alt1
- Initial build for ALT.
