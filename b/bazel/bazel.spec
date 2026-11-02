%define _unpackaged_files_terminate_build 1

%define jdk_version 21
%define jb_version 9.3.1-jb_20261029_142

# Bazel carries its application ZIP after the native launcher (upstream issue 600).
%brp_strip_none %_bindir/*
%add_debuginfo_skiplist %_bindir/*

Name: bazel
Version: 9.3.1
Release: alt1

Summary: A fast, scalable, multi-language and extensible build system
License: Apache-2.0
Group: Development/Java
Url: https://bazel.build
Vcs: https://github.com/bazelbuild/bazel.git

ExclusiveArch: %java_arches

Source: %name-%version.tar
Source1: coverage-packaging-%version.tar
# JetBrains 9.3.1-jb_20261029_142, commit 9acd9ff1c00c46e914d1393ba3d9579e812dd9d9.
Patch0: bazel-%version-alt-jetbrains-0001.patch
Patch1: bazel-%version-alt-jetbrains-0002.patch
Patch2: bazel-%version-alt-jetbrains-0003.patch
Patch3: bazel-%version-alt-jetbrains-0004.patch
Patch4: bazel-%version-alt-jetbrains-0005.patch
Patch5: bazel-%version-alt-jetbrains-0006.patch
Patch6: bazel-%version-alt-jetbrains-0007.patch
Patch7: bazel-%version-alt.patch
Patch8: bazel-%version-alt-java-test-runner-tempdir.patch



BuildRequires(pre): rpm-macros-java
BuildRequires: java-%jdk_version-openjdk-devel
BuildRequires: python3-module-abseil-py
BuildRequires: gcc-c++
BuildRequires: zip
BuildRequires: unzip
BuildRequires: maven-local
BuildRequires: guava google-gson beust-jcommander jsr-305
BuildRequires: auto-value auto-value-annotations junit truth
BuildRequires: netty netty-tcnative-openssl-dynamic async-profiler
BuildRequires: libgtest-devel libgmock-devel
BuildRequires: mockito google-error-prone-annotations


%package coverage-output-generator
Summary: LCOV coverage report merger for Bazel
Group: Development/Java
BuildArch: noarch

%description
Bazel is an open-source build and test tool similar to Make, Maven, and Gradle.
It uses a human-readable, high-level build language. Bazel supports projects in
multiple languages and builds outputs for multiple platforms. Bazel supports
large codebases across multiple repositories, and large numbers of users.

%description coverage-output-generator
CoverageOutputGenerator from this Bazel release merges LCOV and gcov reports,
applies source filters and emits combined LCOV data.

%prep
%setup -b1
%autopatch -p1

mkdir coverage-generator-build
cp -a tools/test/CoverageOutputGenerator/java \
    tools/test/CoverageOutputGenerator/javatests coverage-generator-build/
cp .gear/coverage/pom.xml .gear/coverage/check.py coverage-generator-build/
%pom_xpath_set pom:version %version coverage-generator-build

python3 .gear/coverage/configure-system-libraries.py

for library in gtest gtest_main gmock gmock_main; do
    ln -s %_libdir/lib$library.so tools/distributions/alt/gtest/lib$library.so
done
ln -s %_includedir/gtest tools/distributions/alt/gtest/gtest
ln -s %_includedir/gmock tools/distributions/alt/gtest/gmock
mkdir -p tools/distributions/alt/gtest/googletest/include \
    tools/distributions/alt/gtest/googlemock/include
ln -s %_includedir/gtest \
    tools/distributions/alt/gtest/googletest/include/gtest
ln -s %_includedir/gmock \
    tools/distributions/alt/gtest/googlemock/include/gmock

mkdir -p runner-test-build/build-sources/com/google/testing \
    runner-test-build/build-tests/com/google/testing
cp -a src/java_tools/junitrunner/java/com/google/testing/junit \
    runner-test-build/build-sources/com/google/testing/
mv runner-test-build/build-sources/com/google/testing/junit/runner/sharding/testing \
    runner-test-build/build-tests/com/google/testing/sharding-testing
cp -a src/java_tools/junitrunner/javatests/com/google/testing/junit \
    runner-test-build/build-tests/com/google/testing/
cp .gear/coverage/runner-pom.xml runner-test-build/pom.xml
sed -i 's/@VERSION@/%version/' runner-test-build/pom.xml

%build
pushd runner-test-build
%mvn_build -s -j
popd

pushd coverage-generator-build
%mvn_package :bazel-coverage-output-generator coverage-output-generator
%mvn_file :bazel-coverage-output-generator \
    bazel-coverage-output-generator/generator
%mvn_build -s -j
popd

export EMBED_LABEL="%jb_version 9acd9ff"
export EXTRA_BAZEL_ARGS="--java_runtime_version=local_jdk \
    --tool_java_runtime_version=local_jdk --copt=-Wno-return-type"
export SOURCE_DATE_EPOCH=1793271723
export VERBOSE=yes
bash ./compile.sh

bash scripts/generate_bash_completion.sh \
    --bazel=output/bazel \
    --output=bazel-complete.bash \
    --prepend=scripts/bazel-complete-header.bash \
    --prepend=scripts/bazel-complete-template.bash

python3 scripts/generate_fish_completion.py \
    --bazel=output/bazel \
    --output=bazel-complete.fish

%install
pushd coverage-generator-build
%mvn_install
popd
install -Dpm755 output/bazel %buildroot%_bindir/bazel-%jb_version
ln -s bazel-%jb_version %buildroot%_bindir/bazel-%version
install -Dpm755 scripts/packages/bazel.sh %buildroot%_bindir/bazel
install -Dpm644 scripts/packages/bazel.bazelrc \
    %buildroot%_sysconfdir/bazel.bazelrc
install -Dpm644 bazel-complete.bash \
    %buildroot%_datadir/bash-completion/completions/bazel
install -Dpm644 bazel-complete.fish \
    %buildroot%_datadir/fish/vendor_completions.d/bazel.fish
install -Dpm644 scripts/zsh_completion/_bazel \
    %buildroot%_datadir/zsh/site-functions/_bazel
sed 's|@JAVADIR@|%_javadir|g' .gear/coverage/launcher \
    > coverage-generator-build/launcher
install -Dpm755 coverage-generator-build/launcher \
    %buildroot%_bindir/bazel-coverage-output-generator
install -d %buildroot%_datadir/bazel/rules/coverage_tools
install -pm644 .gear/coverage/bazel-repository/BUILD.bazel \
    .gear/coverage/bazel-repository/MODULE.bazel \
    .gear/coverage/bazel-repository/WORKSPACE \
    %buildroot%_datadir/bazel/rules/coverage_tools/
sed 's|@BINDIR@|%_bindir|g' \
    .gear/coverage/bazel-repository/system_tool.bzl \
    > %buildroot%_datadir/bazel/rules/coverage_tools/system_tool.bzl

%check
sed 's|@JAVADIR@|%_javadir|g' .gear/coverage/launcher \
    > coverage-generator-build/build-launcher
chmod +x coverage-generator-build/build-launcher
ALT_COVERAGE_GENERATOR_JAR="$PWD/coverage-generator-build/target/bazel-coverage-output-generator-%version.jar" \
    python3 coverage-generator-build/check.py \
    "$PWD/coverage-generator-build/build-launcher"

bash .gear/coverage/check-bazel.sh

%files
%doc AUTHORS CHANGELOG.md LICENSE
%_bindir/bazel
%_bindir/bazel-%jb_version
%_bindir/bazel-%version
%_sysconfdir/bazel.bazelrc
%_datadir/bash-completion/completions/%name
%dir %_datadir/fish
%dir %_datadir/fish/vendor_completions.d
%_datadir/fish/vendor_completions.d/%name.fish
%dir %_datadir/zsh
%dir %_datadir/zsh/site-functions
%_datadir/zsh/site-functions/_bazel

%files coverage-output-generator -f coverage-generator-build/.mfiles-coverage-output-generator
%_bindir/bazel-coverage-output-generator
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/coverage_tools/

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 9.3.1-alt1
- New version.
- Apply JetBrains 9.3.1-jb_20261029_142 patches.
- Build CoverageOutputGenerator from the parent source.

* Tue Jun 24 2025 Anton Zhukharev <ancieg@altlinux.org> 8.3.0-alt1
- Updated to 8.3.0.

* Thu May 29 2025 Anton Zhukharev <ancieg@altlinux.org> 8.2.1-alt1
- Updated to 8.2.1 (closes #54435).

* Sun Oct 13 2024 Anton Zhukharev <ancieg@altlinux.org> 7.3.2-alt1
- Updated to 7.3.2.

* Wed Jul 10 2024 Anton Zhukharev <ancieg@altlinux.org> 7.2.1-alt1
- Updated to 7.2.1.

* Wed Mar 20 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.23.2-alt1
- Initial build for ALT.
