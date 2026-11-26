%define _unpackaged_files_terminate_build 1

Name: bazel-java-tools-native
Version: 22.0
Release: alt1

Summary: Source-built Java toolchain tools for Bazel
License: Apache-2.0
Group: Development/Java
Url: https://github.com/bazelbuild/java_tools
VCS: https://github.com/bazelbuild/bazel.git

# Upstream SingleJar requires 64-bit Unix. Match the Sisyphus Bazel targets.
ExclusiveArch: x86_64 aarch64

Source0: %name-%version.tar
Source1: java-tools-packaging-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: pkg-config
BuildRequires: zlib-devel
BuildRequires: libabseil-cpp-devel
BuildRequires: libre2-devel
BuildRequires: libgtest-devel
BuildRequires: bazel-rules-cc
BuildRequires: bazel-rules-shell
BuildRequires: libprotobuf-devel
BuildRequires: zip
BuildRequires: unzip
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(com.github.ben-manes.caffeine:caffeine)
BuildRequires: mvn(com.google.auto:auto-common)
BuildRequires: mvn(com.google.auto.value:auto-value)
BuildRequires: mvn(com.google.auto.value:auto-value-annotations)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(com.google.errorprone:error_prone_core)
BuildRequires: mvn(com.google.escapevelocity:escapevelocity)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.protobuf:protobuf-java)
BuildRequires: mvn(com.google.protobuf:protobuf-java-util)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(com.squareup:javapoet)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.ltgt.gradle.incap:incap)
BuildRequires: mvn(org.jacoco:org.jacoco.agent)
BuildRequires: mvn(org.jacoco:org.jacoco.core)
BuildRequires: mvn(org.jacoco:org.jacoco.report)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-commons)
BuildRequires: mvn(org.ow2.asm:asm-tree)

%description
Native ijar, singlejar and one_version from the java_tools v22.0 source
revision, using system zlib, Abseil and RE2. JavaBuilder, the bootstrap
compiler, test and coverage tools are built from the same source revision
and supplied as architecture-independent subpackages.

%package -n bazel-java-builder
Summary: JavaBuilder compiler driver for Bazel
Group: Development/Java
BuildArch: noarch
Requires: java-21-openjdk-devel
Requires: javapackages-tools

%description -n bazel-java-builder
JavaBuilder compiler driver with strict dependency checking, annotation
processing, Error Prone, JaCoCo instrumentation and persistent workers.
Uses the system Caffeine and Error Prone providers, with the Java 21
compiler process and classfile target.

%package -n bazel-java-tools-bootstrap
Summary: Source bootstrap GenClass and VanillaJavaBuilder for Bazel
Group: Development/Java
BuildArch: noarch
Requires: java-21-openjdk-devel
# The selected worker protobuf gencode requires this runtime ABI or newer.
Requires: protobuf-java >= 1:4.33.4
Requires: guava

%description -n bazel-java-tools-bootstrap
Stage-zero GenClass and VanillaJavaBuilder compiled directly with javac,
including ordinary compilation and persistent workers without Error Prone,
strict dependency checking or Android desugaring.

%package -n bazel-java-test-runner
Summary: JUnit test runner for Bazel Java toolchains
Group: Development/Java
BuildArch: noarch
Requires: java-headless >= 21
Requires: javapackages-tools

%description -n bazel-java-test-runner
JUnit runner with XML test reports, filtering, sharding and premature exit
detection. Runtime Java dependencies are supplied by system packages.

%package -n bazel-java-tools-coverage
Summary: JaCoCo coverage runner for Bazel
Group: Development/Java
BuildArch: noarch
Requires: java-headless >= 21

%description -n bazel-java-tools-coverage
Bazel JaCoCo coverage runner and LCOV formatter, with system dependency
paths recorded in its manifest for Bazel's single-JAR entry point.

%ifarch x86_64
%package -n bazel-java-tools-repository
Summary: System Java toolchain repository for local Bazel builds
Group: Development/Java
Requires: %name = %version-%release
Requires: bazel-java-tools-bootstrap = %version-%release
Requires: bazel-java-builder = %version-%release
Requires: bazel-java-test-runner = %version-%release
Requires: bazel-java-tools-coverage = %version-%release
Requires: turbine >= 1.17.0
Requires: java-21-openjdk-devel

%description -n bazel-java-tools-repository
Local Java 21 target toolchain definitions backed by system RPM tools.
The source-built archive, JUnit and JaCoCo tools retain their stable paths.
%endif

%prep
%setup -b1
%patch0 -p1
sh .gear/prepare-java.sh
sed 's|@JAVADIR@|%_javadir|g' .gear/coverage/MANIFEST.MF.in \
    > .gear/coverage/MANIFEST.MF
%mvn_package :java-tools-build __noinstall
%mvn_file :bazel-java-builder bazel-java-builder/java-builder
%mvn_file :bazel-java-test-runner bazel-java-test-runner/test-runner
%mvn_file :bazel-java-tools-coverage bazel-java-tools/coverage

%build
# Compile against the Java 21 javac APIs, preserving runtime compatibility.
%cmake -S .gear/native \
    -DRULES_CC_SOURCE_ROOT=%_datadir/bazel/rules/rules_cc \
    -DRULES_SHELL_SOURCE_ROOT=%_datadir/bazel/rules/rules_shell
%cmake_build
sh .gear/bootstrap/build.sh %_javadir
%mvn_build -s -j

%install
%mvn_install
install -Dpm755 %_cmake__builddir/ijar %buildroot%_bindir/bazel-ijar
install -Dpm755 %_cmake__builddir/singlejar %buildroot%_bindir/bazel-singlejar
install -Dpm755 %_cmake__builddir/one_version \
    %buildroot%_bindir/bazel-one-version
install -Dpm644 bootstrap/java-tools-bootstrap.jar \
    %buildroot%_javadir/bazel-java-tools-bootstrap.jar
sed 's|@JAVADIR@|%_javadir|g' .gear/bootstrap/launcher > bootstrap/launcher
install -Dpm755 bootstrap/launcher %buildroot%_bindir/bazel-genclass
install -Dpm755 bootstrap/launcher %buildroot%_bindir/bazel-vanilla-javabuilder
sed -e 's|@JAVADIR@|%_javadir|g' -e 's|@JVMDIR@|%_jvmdir|g' \
    .gear/builder/launcher > java-build/builder/launcher
install -Dpm755 java-build/builder/launcher \
    %buildroot%_bindir/bazel-java-builder
sed 's|@JAVADIR@|%_javadir|g' .gear/runner/launcher \
    > java-build/runner/launcher
install -Dpm755 java-build/runner/launcher \
    %buildroot%_bindir/bazel-java-test-runner
%ifarch x86_64
install -d %buildroot%_datadir/bazel/rules/java_tools
install -pm644 .gear/system-repository/BUILD.bazel \
    .gear/system-repository/MODULE.bazel .gear/system-repository/WORKSPACE \
    %buildroot%_datadir/bazel/rules/java_tools/
sed -e 's|@BINDIR@|%_bindir|g' -e 's|@JVMDIR@|%_jvmdir|g' \
    .gear/system-repository/rpm_tool.bzl \
    > %buildroot%_datadir/bazel/rules/java_tools/rpm_tool.bzl
sed 's|@JVMDIR@|%_jvmdir|g' .gear/system-repository/BUILD.bazel \
    > %buildroot%_datadir/bazel/rules/java_tools/BUILD.bazel
ln -s %_javadir/bazel-java-test-runner/test-runner.jar \
    %buildroot%_datadir/bazel/rules/java_tools/Runner.jar
ln -s %_javadir/bazel-java-tools/coverage.jar \
    %buildroot%_datadir/bazel/rules/java_tools/JacocoCoverage.jar
%endif

%check
ctest --test-dir %_cmake__builddir --output-on-failure
python3 .gear/native/check.py %_cmake__builddir/ijar \
    %_cmake__builddir/singlejar %_cmake__builddir/one_version
sed -e 's|@JAVADIR@|%_javadir|g' -e 's|@JVMDIR@|%_jvmdir|g' \
    .gear/builder/launcher > java-build/builder/build-launcher
chmod +x java-build/builder/build-launcher
builder_dir="$PWD/java-build/builder"
ALT_BUILDER_JAR="$builder_dir/target/bazel-java-builder-%version.jar" \
ALT_CAFFEINE_JAR="%_javadir/java-caffeine/caffeine.jar" \
    python3 .gear/builder/check.py "$PWD/java-build/builder/build-launcher"

# Exercise the bootstrap and independent JVM entry points on Java 21.
sh .gear/bootstrap/check.sh bootstrap/java-tools-bootstrap.jar %_javadir
sed 's|@JAVADIR@|%_javadir|g' .gear/runner/launcher \
    > java-build/runner/build-launcher
chmod +x java-build/runner/build-launcher
runner_dir="$PWD/java-build/runner"
ALT_RUNNER_JAR="$runner_dir/target/bazel-java-test-runner-%version.jar" \
    python3 .gear/runner/check.py "$PWD/java-build/runner/build-launcher"

%files
%doc LICENSE
%_bindir/bazel-ijar
%_bindir/bazel-singlejar
%_bindir/bazel-one-version

%files -n bazel-java-builder -f .mfiles-bazel-java-builder
%_bindir/bazel-java-builder

%files -n bazel-java-tools-bootstrap
%_javadir/bazel-java-tools-bootstrap.jar
%_bindir/bazel-genclass
%_bindir/bazel-vanilla-javabuilder

%files -n bazel-java-test-runner -f .mfiles-bazel-java-test-runner
%_bindir/bazel-java-test-runner

%files -n bazel-java-tools-coverage -f .mfiles-bazel-java-tools-coverage

%ifarch x86_64
%files -n bazel-java-tools-repository
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/java_tools/
%endif

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 22.0-alt1
- Initial build for ALT.
- Fix FTBFS: align architectures with Bazel and fix repository file ownership.
- Allow installing the standalone Java tools without native binaries.
- Use the Java 21 build of Turbine.
