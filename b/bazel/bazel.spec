%define _unpackaged_files_terminate_build 1

# disable stripping, it breaks package
%brp_strip_none %_bindir/*
%global __find_debuginfo_files %nil
%set_verify_elf_method skip
%add_debuginfo_skiplist %_bindir

# Don't build for 32-bit systems
ExcludeArch: %ix86

Name: bazel
Version: 0.23.2
Release: alt1
Summary: Correct, reproducible, and fast builds for everyone.
License: Apache-2.0
Group: Development/Java
URL: https://bazel.build

# https://github.com/bazelbuild/bazel/releases/download/%version/bazel-%version-dist.zip
Source: %name-%version.tar

BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: gcc-c++
BuildRequires: unzip zip
BuildRequires: python2.7(runpy)

%description
Bazel is a build tool that builds code quickly and reliably.
It is used to build the majority of Google's software,
and thus it has been designed to handle build problems
present in Google's development environment.

%prep
%setup

%build
[ -n "$NPROCS" ] || NPROCS=%__nprocs;
export EXTRA_BAZEL_ARGS="--jobs=$NPROCS --host_javabase=@local_jdk//:jdk"

VERBOSE=yes ./compile.sh

./scripts/generate_bash_completion.sh \
	--bazel=output/bazel \
	--output=bazel-complete.bash \
	--prepend=scripts/bazel-complete-header.bash \
	--prepend=scripts/bazel-complete-template.bash

%install
install -D -m755 output/bazel %buildroot%_bindir/bazel-real
install -D -m755 scripts/packages/bazel.sh %buildroot%_bindir/bazel
install -D -m644 bazel-complete.bash %buildroot%_datadir/bash-completion/completions/bazel

%files
%doc tools
%doc examples
%_bindir/bazel
%_bindir/bazel-real
%_datadir/bash-completion/completions/bazel

%changelog
* Wed Mar 20 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.23.2-alt1
- Initial build for ALT.
