%define _unpackaged_files_terminate_build 1

# bazel requires (runtime and buildtime) JDK (version is in the docs)
%define jdk_version 21

# taken from last openjdk spec
%define jdk_archs x86_64 aarch64 loongarch64

# https://github.com/bazelbuild/bazel/issues/600
%brp_strip_none %_bindir/*
%add_debuginfo_skiplist %_bindir/*

Name: bazel
Version: 7.2.1
Release: alt1

Summary: A fast, scalable, multi-language and extensible build system
License: Apache-2.0
Group: Development/Java
Url: https://bazel.build
Vcs: https://github.com/bazelbuild/bazel

ExclusiveArch: %jdk_archs

Source: %name-%version.tar

Requires: java-%jdk_version-openjdk-devel

BuildRequires: /proc
BuildRequires: java-%jdk_version-openjdk-devel
BuildRequires: python3-module-abseil-py
BuildRequires: gcc-c++
BuildRequires: zip
BuildRequires: unzip

%description
Bazel is an open-source build and test tool similar to Make, Maven, and Gradle.
It uses a human-readable, high-level build language. Bazel supports projects in
multiple languages and builds outputs for multiple platforms. Bazel supports
large codebases across multiple repositories, and large numbers of users.

%prep
%setup

%build
export EXTRA_BAZEL_ARGS="--tool_java_runtime_version=local_jdk"
export SOURCE_DATE_EPOCH="$(date -u +%%s)"
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
install -D -m755 output/bazel %buildroot%_bindir/bazel-%version
install -D -m755 scripts/packages/bazel.sh %buildroot%_bindir/bazel
install -D -m644 scripts/packages/bazel.bazelrc %buildroot%_sysconfdir/bazel.bazelrc
install -D -m644 bazel-complete.bash %buildroot%_datadir/bash-completion/completions/bazel
install -D -m644 bazel-complete.fish %buildroot%_datadir/fish/vendor_completions.d/bazel.fish
install -D -m644 scripts/zsh_completion/_bazel %buildroot%_datadir/zsh/site-functions/_bazel

%files
%doc AUTHORS CHANGELOG.md README.md
%_bindir/bazel*
%_sysconfdir/bazel.bazelrc
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_bazel

%changelog
* Wed Jul 10 2024 Anton Zhukharev <ancieg@altlinux.org> 7.2.1-alt1
- Updated to 7.2.1.

* Wed Mar 20 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.23.2-alt1
- Initial build for ALT.
