%define _unpackaged_files_terminate_build 1

Name: okio
Version: 3.18.2
Release: alt1

Summary: Modern I/O library for Java and Kotlin
License: Apache-2.0
Group: Development/Java
Url: https://square.github.io/okio
VCS: https://github.com/square/okio.git

Source0: %name-%version.tar
Source1: jvm-build.gradle.kts
Source2: jvm-settings.gradle.kts

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin
BuildRequires: xgradle

%description
Okio complements java.io and java.nio with convenient, efficient buffering,
byte strings, compression and file systems. This package supplies JVM core
and multiplatform publication metadata forwarding to the JVM implementation.
Upstream tests are disabled. Additional modules, including fakefilesystem,
are preserved in the source archive but are not built by this package.

%package jvm
Summary: Okio JVM implementation
Group: Development/Java

%description jvm
Full Okio JVM core, including buffers, sources, sinks, compression, archives,
resources and the system file system.

%prep
%setup
cp %SOURCE1 build.gradle.kts
cp %SOURCE2 settings.gradle.kts

%build
# JDK21 avoids Gradle/Groovy's unsupported host JDK27 bytecode.
%gradle_publish -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk --no-daemon

%install
%mvn_package :okio-jvm jvm
%gradle_register --artifacts=okio-
%gradle_install

# Upstream tests are disabled by the selected JVM packaging policy.

%files -f .mfiles
%doc LICENSE.txt README.md

%files jvm -f .mfiles-jvm
%doc LICENSE.txt

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 3.18.2-alt1
- Initial build for ALT.
