%define _unpackaged_files_terminate_build 1
Name: jazzer
Version: 0.30.0
Release: alt1

Summary: Coverage-guided JVM fuzzing engine and JUnit integration
License: Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND BSD-3-Clause AND EPL-2.0
Group: Development/Java
Url: https://github.com/CodeIntelligenceTesting/jazzer
VCS: https://github.com/CodeIntelligenceTesting/jazzer.git

# The upstream README.md lists Linux support for x86_64 and aarch64.
ExclusiveArch: x86_64 aarch64

Source0: %name-%version.tar
Source1: jazzer-bzlmod-offline.tar.gz
Source2: jazzer-libfuzzer-2023-04-25.tar.gz
Source3: jazzer-jacoco-core-0.8.14.tar.gz
Source4: jazzer-system-jarjar.patch
Source5: jazzer-jacoco.patch
Source6: jazzer-rules-jvm-external.patch
Source8: jazzer-bazel-inputs.tar
Source10: 0001-Import-system-Kotlin-libraries-without-source-jars.patch
Source11: jazzer-find-requires.py
Source12: jazzer-rules-jvm-java-info.patch
Patch0: jazzer-offline-build-definitions.patch
Patch1: 0002-Use-the-public-Kotlin-toolchain-API.patch

%define __find_requires /usr/bin/python3 %{SOURCE11}
BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: bazel
BuildRequires: mvn(org.altlinux:bazel-java-builder)
BuildRequires: bazel-rules-jvm-external
BuildRequires: bazel-toml
BuildRequires: bazel-rules-kotlin-workers
BuildRequires: java-21-openjdk-devel
BuildRequires: protobuf-bazel
BuildRequires: clang21.1
BuildRequires: gcc-c++
BuildRequires: mvn(org.pantsbuild:jarjar)
BuildRequires: mvn(codes.rafael.asmjdkbridge:asm-jdk-bridge)
BuildRequires: bazel-java-tools-native
BuildRequires: mvn(org.checkerframework:dataflow-errorprone)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(org.altlinux.bootstrap:bazel-java-tools-coverage)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-compiler)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-build-tools-api)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-reflect)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(com.google.devtools.ksp:symbol-processing-aa)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-coroutines-core)
BuildRequires: mvn(org.jetbrains.intellij.deps.kotlinx:kotlinx-coroutines-core-jvm)
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-json-jvm)
BuildRequires: mvn(com.github.jsqlparser:jsqlparser)
BuildRequires: mvn(com.google.errorprone:error_prone_annotations)
BuildRequires: mvn(io.github.classgraph:classgraph)
BuildRequires: mvn(net.bytebuddy:byte-buddy-agent)
BuildRequires: mvn(net.jodah:typetools)
BuildRequires: mvn(org.apiguardian:apiguardian-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.junit.platform:junit-platform-commons)
BuildRequires: mvn(org.junit.platform:junit-platform-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(org.opentest4j:opentest4j)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-commons)
BuildRequires: mvn(org.ow2.asm:asm-tree)

Requires: java-headless >= 17

%description
Jazzer provides coverage-guided Java and JVM fuzzing, native libFuzzer
integration, instrumentation, and a JUnit test engine extension.

%package api
Summary: Public API and mutation annotations for Jazzer
License: Apache-2.0
Group: Development/Java
BuildArch: noarch

%description api
Public Java APIs and mutation annotations for writing Jazzer fuzz targets.

%package junit
Summary: JUnit integration for Jazzer
License: Apache-2.0
Group: Development/Java

%description junit
JUnit Jupiter integration for running Jazzer fuzz targets as JUnit tests.

%prep
%setup -q
%autopatch -p1
cp %{SOURCE4} jazzer-system-jarjar.patch
mkdir .rpm-sources
tar -xzf %{SOURCE2} -C .rpm-sources
tar -xzf %{SOURCE3} -C .rpm-sources
patch -d .rpm-sources/jacoco-core -p1 -i %SOURCE5
cp .rpm-sources/libfuzzer/LICENSE LICENSE.libFuzzer
cp .rpm-sources/jacoco-core/LICENSE.md LICENSE.JaCoCo
mkdir -p .offline-bcr
tar -xzf %{SOURCE1} -C .offline-bcr

# Apply the offline module patches during prep, before passing the local module
# to Bazel. Its repository patcher fails on the compatibility patch.
rules_jvm_archive=.offline-bcr/distdir/rules_jvm-v0.27.0.tar.gz
rules_jvm=.rpm-sources/contrib_rules_jvm
mkdir "$rules_jvm"
tar -xzf "$rules_jvm_archive" -C "$rules_jvm" --strip-components=1
patch -d "$rules_jvm" -p1 --fuzz=0 < \
    .offline-bcr/registry/modules/contrib_rules_jvm/0.27.0/patches/module_dot_bazel_version.patch
patch -d "$rules_jvm" -p1 --fuzz=0 < %{SOURCE12}

tar -xf %SOURCE8 --strip-components=1
cp -a %_datadir/bazel/rules/rules_jvm_external .rpm-sources/
patch -d .rpm-sources/rules_jvm_external -p1 -i %SOURCE6
cp -a %_datadir/bazel/rules/rules_kotlin-workers .rpm-sources/rules_kotlin
install -pm 0644 rules-kotlin.module .rpm-sources/rules_kotlin/MODULE.bazel
patch -d .rpm-sources/rules_kotlin -p1 -i %SOURCE10
tar -xf .offline-bcr/distdir/bazel-lib-v2.19.3.tar.gz \
    -C .rpm-sources/aspect_bazel_lib --strip-components=1 --skip-old-files
tar -xf .offline-bcr/distdir/bazel-lib-v3.1.0.tar.gz \
    -C .rpm-sources/bazel_lib --strip-components=1 --skip-old-files

%build
python_repo=rules_python++python+python_3_11_$(uname -m)-unknown-linux-gnu
USE_BAZEL_VERSION=latest bazel --server_javabase=%_jvmdir/java-21-openjdk \
    test --jobs="${NPROCS:-%__nprocs}" \
    --repo_env=JAVA_HOME=%_jvmdir/java-21-openjdk \
    --registry="file://$PWD/.offline-bcr/registry" \
    --override_repository="$python_repo=.rpm-sources/local-python" \
    --//deploy:jazzer_version=%version \
    //deploy:jazzer //deploy:jazzer-api //deploy:jazzer-junit \
    //deploy:jazzer-pom //deploy:jazzer-api-pom //deploy:jazzer-junit-pom \
    //deploy:jazzer_artifact_test //deploy:jazzer-api_artifact_test \
    //deploy:jazzer-junit_artifact_test \
    //src/main/native/com/code_intelligence/jazzer/driver:fuzzed_data_provider_test \
    //src/test/java/com/code_intelligence/jazzer/driver:FuzzedDataProviderImplTest \
    //src/test/java/com/code_intelligence/jazzer/driver:FuzzTargetRunnerTest

%install
%mvn_package com.code-intelligence:jazzer
%mvn_package com.code-intelligence:jazzer-api jazzer-api
%mvn_package com.code-intelligence:jazzer-junit jazzer-junit
# Stage readable POMs and writable JARs for XMvn's manifest update.
mkdir xmvn-artifacts
for artifact in jazzer jazzer-api jazzer-junit; do
    install -m 0644 "bazel-bin/deploy/$artifact-project.jar" "xmvn-artifacts/$artifact.jar"
    install -m 0644 "bazel-bin/deploy/$artifact-pom.xml" "xmvn-artifacts/$artifact.pom"
    %mvn_artifact "xmvn-artifacts/$artifact.pom" "xmvn-artifacts/$artifact.jar"
done
%mvn_install

install -d %buildroot%_bindir
cat > %buildroot%_bindir/jazzer <<'EOF'
#!/bin/sh
classpath=%_jnidir/jazzer/jazzer.jar:%_javadir/jazzer/jazzer-api.jar
for arg do
    shift
    case "$arg" in
        --cp=*) classpath=$classpath:"${arg#--cp=}"
            ;;
        *) set -- "$@" "$arg"
            ;;
    esac
done
exec %_bindir/java -cp "$classpath" com.code_intelligence.jazzer.Jazzer "$@"
EOF
chmod 0755 %buildroot%_bindir/jazzer

asm_docs=%_docdir/objectweb-asm-$(rpm -q --qf '%%{VERSION}' objectweb-asm)
kotlin_docs=%_docdir/kotlin-stdlib-$(rpm -q --qf '%%{VERSION}' kotlin-stdlib)
install -pm 0644 "$asm_docs/LICENSE.txt" LICENSE.ASM
install -pm 0644 "$kotlin_docs/license/LICENSE.txt" LICENSE.Kotlin
install -pm 0644 "$kotlin_docs/license/NOTICE.txt" NOTICE.Kotlin

%files -f .mfiles
%_bindir/jazzer
%doc LICENSE LICENSE.libFuzzer LICENSE.JaCoCo LICENSE.ASM
%doc LICENSE.Kotlin NOTICE.Kotlin

%files api -f .mfiles-jazzer-api

%files junit -f .mfiles-jazzer-junit

%changelog
* Thu Nov 26 2026 Ivan Khanas <xeno@altlinux.org> 0.30.0-alt1
- Initial build for ALT.
- Fix FTBFS: use the packaged SingleJar on aarch64.
- Match the JUnit subpackage architectures to the native runtime.
