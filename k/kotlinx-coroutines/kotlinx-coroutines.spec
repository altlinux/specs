%define _unpackaged_files_terminate_build 1

Name: kotlinx-coroutines
Version: 1.11.0
Release: alt3

Summary: Kotlin coroutines JVM runtime and integrations
License: Apache-2.0
Group: Development/Java
URL: https://github.com/Kotlin/kotlinx.coroutines
VCS: https://github.com/Kotlin/kotlinx.coroutines.git
BuildArch: noarch

Source: %name-%version.tar
Source1: kotlinx-coroutines-intellij-%version.tar
Patch: offline-jvm.patch
Patch1: intellij-jvm-tests.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: animal-sniffer
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-compiler
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlin-maven
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-commons)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-reflect)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.jetbrains.kotlinx:atomicfu-jvm)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(net.bytebuddy:byte-buddy)
BuildRequires: mvn(net.bytebuddy:byte-buddy-agent)
BuildRequires: mvn(net.java.dev.jna:jna)
BuildRequires: mvn(net.java.dev.jna:jna-platform)
BuildRequires: mvn(io.projectreactor.tools:blockhound)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-testkit)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(org.slf4j:slf4j-api:2)
BuildRequires: mvn(ch.qos.logback:logback-classic)

# Supersede bootstrap metadata to avoid duplicate XMvn SYSTEM providers.
Provides: gradle-kotlinx-coroutines = %version-%release
Obsoletes: gradle-kotlinx-coroutines

%description
Kotlin coroutines JVM runtime, virtual-time test scheduler, Swing
main dispatcher, Guava and SLF4J integrations and debug instrumentation.
Built from upstream sources using system Kotlin and AtomicFU.
The IntelliJ fork is available in a separate subpackage.

%package intellij
Summary: JetBrains patched coroutines for IntelliJ threading integration
Group: Development/Java

%description intellij
JetBrains' complete patched JVM coroutines core, test scheduler, Swing,
Guava and SLF4J integrations, and debug instrumentation. Provides the genuine
IntelliJ context introspection and parallelism compensation API. Its distinct Maven group is
org.jetbrains.intellij.deps.kotlinx; use one coroutines implementation
per application class loader.

%prep
%setup -a1
%patch -p1
pushd kotlinx-coroutines-intellij-%version
%patch1 -p1
popd
cp -a alt-jvm kotlinx-coroutines-intellij-%version/
# ConsoleAppender requires an encoder with the system Logback.
for tree in . kotlinx-coroutines-intellij-%version; do
    sed -i -e 's/<layout>/<encoder>/' -e 's@</layout>@</encoder>@' \
        "$tree/integration/kotlinx-coroutines-slf4j/test-resources/logback-test.xml"
done
# Android lint annotations are unnecessary for the desktop JVM build.
agent_dir=kotlinx-coroutines-intellij-%version
sed -i '/import android.annotation[.]/d; /@SuppressLint/d' \
    "$agent_dir/kotlinx-coroutines-core/jvm/src/debug/internal/AgentPremain.kt"

%build
%gradle_publish -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk -p alt-jvm --no-daemon \
    -PreleaseVersion=%version \
    -Pkotlin.compiler.execution.strategy=in-process
%gradle_publish -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk -p kotlinx-coroutines-intellij-%version/alt-jvm \
    --no-daemon \
    -Pkotlin.compiler.execution.strategy=in-process

%install
%mvn_alias org.jetbrains.kotlinx:kotlinx-coroutines-core-jvm \
    org.jetbrains.kotlinx:kotlinx-coroutines-core
%mvn_alias org.jetbrains.kotlinx:kotlinx-coroutines-test-jvm \
    org.jetbrains.kotlinx:kotlinx-coroutines-test
%mvn_alias org.jetbrains.kotlinx:kotlinx-coroutines-debug-jvm \
    org.jetbrains.kotlinx:kotlinx-coroutines-debug
%mvn_alias org.jetbrains.kotlinx:kotlinx-coroutines-guava-jvm \
    org.jetbrains.kotlinx:kotlinx-coroutines-guava
%mvn_alias org.jetbrains.kotlinx:kotlinx-coroutines-slf4j-jvm \
    org.jetbrains.kotlinx:kotlinx-coroutines-slf4j
%mvn_file org.jetbrains.kotlinx:kotlinx-coroutines-debug-jvm \
    %name/kotlinx-coroutines-debug
%mvn_file org.jetbrains.kotlinx:kotlinx-coroutines-guava-jvm \
    %name/kotlinx-coroutines-guava
%mvn_file org.jetbrains.kotlinx:kotlinx-coroutines-slf4j-jvm \
    %name/kotlinx-coroutines-slf4j
%mvn_package org.jetbrains.intellij.deps.kotlinx:* intellij
%mvn_file org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-core-jvm \
    %name/intellij/kotlinx-coroutines-core-jvm
%mvn_file org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-test-jvm \
    %name/intellij/kotlinx-coroutines-test-jvm
%mvn_file org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-swing \
    %name/intellij/kotlinx-coroutines-swing
%mvn_file org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-debug-jvm \
    %name/intellij/kotlinx-coroutines-debug-jvm
%mvn_file org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-guava-jvm \
    %name/intellij/kotlinx-coroutines-guava-jvm
%mvn_file org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-slf4j-jvm \
    %name/intellij/kotlinx-coroutines-slf4j-jvm
%mvn_alias org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-core-jvm \
    org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-core
%mvn_alias org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-test-jvm \
    org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-test
%mvn_alias org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-debug-jvm \
    org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-debug
%mvn_alias org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-guava-jvm \
    org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-guava
%mvn_alias org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-slf4j-jvm \
    org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-slf4j
artifacts=kotlinx-coroutines-core-jvm-
artifacts="$artifacts,kotlinx-coroutines-test-jvm-"
artifacts="$artifacts,kotlinx-coroutines-swing-"
artifacts="$artifacts,kotlinx-coroutines-slf4j-,kotlinx-coroutines-debug-,kotlinx-coroutines-guava-"
%gradle_register --artifacts="$artifacts"
%gradle_install

%check
%gradle_check -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk \
    -p alt-jvm --no-daemon -PreleaseVersion=%version \
    -Pkotlin.compiler.execution.strategy=in-process
%gradle_check -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk \
    -p kotlinx-coroutines-intellij-%version/alt-jvm --no-daemon \
    -Pkotlin.compiler.execution.strategy=in-process

%files -f .mfiles
%doc LICENSE.txt

%files intellij -f .mfiles-intellij
%doc kotlinx-coroutines-intellij-%version/IntelliJ-patches.md

%changelog
* Thu Nov 19 2026 Ivan Khanas <xeno@altlinux.org> 1.11.0-alt3
- Fix FTBFS: Use a compatible SLF4J binding for the MDC tests.

* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 1.11.0-alt2
- Build SLF4J context integration and debug instrumentation.

* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 1.11.0-alt1
- Initial build for ALT.
