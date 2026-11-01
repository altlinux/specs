%define _unpackaged_files_terminate_build 1

Name: kotlinx-coroutines
Version: 1.11.0
Release: alt1

Summary: Kotlin coroutines JVM runtime, test scheduler and Swing dispatcher
License: Apache-2.0
Group: Development/Java
Url: https://github.com/Kotlin/kotlinx.coroutines
VCS: https://github.com/Kotlin/kotlinx.coroutines.git
BuildArch: noarch

Source: %name-%version.tar
Source1: kotlinx-coroutines-intellij-%version.tar
Patch: offline-jvm.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: animal-sniffer
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-compiler
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlin-maven
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-reflect)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.jetbrains.kotlinx:atomicfu-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-coroutines-core-jvm)
BuildRequires: mvn(org.jetbrains:annotations)

# Supersede bootstrap metadata to avoid duplicate XMvn SYSTEM providers.
Provides: gradle-kotlinx-coroutines = %version-%release
Obsoletes: gradle-kotlinx-coroutines

%description
Kotlin coroutines JVM runtime, virtual-time test scheduler and Swing
main dispatcher. Built from upstream sources using system Kotlin and
AtomicFU. The IntelliJ fork is available in a separate subpackage.

%package intellij
Summary: JetBrains patched coroutines for IntelliJ threading integration
Group: Development/Java

%description intellij
JetBrains' complete patched JVM coroutines core, test scheduler and Swing
integration. Provides the genuine IntelliJ context introspection and
parallelism compensation API. Its distinct Maven group is
org.jetbrains.intellij.deps.kotlinx; use one coroutines implementation
per application class loader.

%prep
%setup -a1
%patch -p1
cp -a alt-jvm kotlinx-coroutines-intellij-%version/
# Android lint annotations are unnecessary for the desktop JVM build.
sed -i '/import android.annotation[.]/d; /@SuppressLint/d' \
    kotlinx-coroutines-intellij-%version/kotlinx-coroutines-core/jvm/src/debug/internal/AgentPremain.kt

%build
# Rebuilds must not register stale publications from an earlier attempt.
rm -rf "$HOME/.m2/repository/org/jetbrains/kotlinx/kotlinx-coroutines-"*
rm -rf "$HOME/.m2/repository/org/jetbrains/intellij/deps/kotlinx"
%gradle_publish -p alt-jvm --no-daemon --max-workers=4 \
    -PreleaseVersion=%version \
    -Pkotlin.compiler.execution.strategy=in-process
%gradle_publish -p kotlinx-coroutines-intellij-%version/alt-jvm \
    --no-daemon --max-workers=4 \
    -Pkotlin.compiler.execution.strategy=in-process

%install
%mvn_alias org.jetbrains.kotlinx:kotlinx-coroutines-core-jvm \
    org.jetbrains.kotlinx:kotlinx-coroutines-core
%mvn_alias org.jetbrains.kotlinx:kotlinx-coroutines-test-jvm \
    org.jetbrains.kotlinx:kotlinx-coroutines-test
%mvn_package org.jetbrains.intellij.deps.kotlinx:* intellij
%mvn_file org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-core-jvm \
    %name/intellij/kotlinx-coroutines-core-jvm
%mvn_file org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-test-jvm \
    %name/intellij/kotlinx-coroutines-test-jvm
%mvn_file org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-swing \
    %name/intellij/kotlinx-coroutines-swing
%mvn_alias org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-core-jvm \
    org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-core
%mvn_alias org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-test-jvm \
    org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-test
artifacts=kotlinx-coroutines-core-jvm-
artifacts="$artifacts,kotlinx-coroutines-test-jvm-"
artifacts="$artifacts,kotlinx-coroutines-swing-"
%gradle_register --artifacts="$artifacts"
%gradle_install

%files -f .mfiles
%doc LICENSE.txt

%files intellij -f .mfiles-intellij
%doc kotlinx-coroutines-intellij-%version/LICENSE.txt
%doc kotlinx-coroutines-intellij-%version/IntelliJ-patches.md

%changelog
* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 1.11.0-alt1
- Initial build for ALT.
