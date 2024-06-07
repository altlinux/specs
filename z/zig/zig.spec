# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method rpath=relaxed

Name: zig
Version: 0.12.1
Release: alt1
Summary: General-purpose programming language and toolchain for maintaining robust, optimal, and reusable software
# TODO: Zig lib is bundled with a lot of third party with other licenses.
License: MIT
Group: Development/C
Url: https://ziglang.org/
Vcs: https://github.com/ziglang/zig/
Requires: /proc

# https://ziglang.org/download/0.10.0/release-notes.html#Support-Table
# aarch64: OK  1:03:53
#    armh: -
#    i586: LLVM ERROR: out of memory
# ppc64le: zig2: Segmentation fault
#  x86-64: OK    31:37
ExclusiveArch: %zig_arches

Source: %name-%version.tar

%define llvm_ver 17
%define llvm_pkgver %llvm_ver.0
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-zig
# /proc is required or zig will output FileNotFound
BuildRequires: chrpath
BuildRequires: clang%llvm_pkgver-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel
BuildRequires: libtinfo-devel
BuildRequires: libxml2-devel
BuildRequires: lld%llvm_pkgver-devel
BuildRequires: llvm%llvm_pkgver-devel
BuildRequires: /proc
BuildRequires: zlib-devel

%description
%summary.

%prep
%setup

%package checkinstall
Summary: CI test for zig
Group: Development/Other
Requires(pre): zig

%description checkinstall
%summary.

%build
%define optflags_lto %nil
export CC=clang-%llvm_ver CXX=clang++-%llvm_ver LDFLAGS="-fuse-ld=lld $LDFLAGS"
# https://github.com/ziglang/zig/issues/16800
#   i586: UnknownArchitecture
#     -DZIG_HOST_TARGET_TRIPLE=native: LibCRuntimeNotFound
#     -DZIG_HOST_TARGET_TRIPLE=x86-linux-gnu: error: cast increases pointer alignment
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DZIG_PREFER_CLANG_CPP_DYLIB=true \
	-DZIG_SHARED_LLVM=ON \
	-DZIG_TARGET_MCPU=baseline \
	-DZIG_USE_LLVM_CONFIG=ON \
	-DZIG_VERSION="%version"
grep ZIG %_cmake__builddir/CMakeCache.txt
%cmake_build

%install
export ZIG_VERBOSE_LINK=y ZIG_VERBOSE_CC=y
%cmake_install
chrpath -d %buildroot%_bindir/zig

%check
PATH=%buildroot%_bindir:$PATH
zig version
zig env
zig run test/standalone/simple/hello_world/hello.zig
zig run test/standalone/simple/hello_world/hello_libc.zig -lc
# Run upstream tests from ci/x86_64-linux-debug.sh
cd %_cmake__builddir
zig test ../test/behavior.zig -I../test

%pre checkinstall
set -exo pipefail
zig version
zig run %_defaultdocdir/%name/hello.zig
t=$(mktemp -d)
cd "$t"
%__zig init
%zig_build run
%zig_test
rm -rf -- "$t" "$HOME/.cache/zig"

%files
%define _customdocdir %_docdir/%name
%doc LICENSE README.md test/standalone/simple/hello_world/*.zig doc/langref.html.in
%_bindir/zig
%_prefix/lib/zig

%files checkinstall

%changelog
* Fri Jun 07 2024 Vitaly Chikunov <vt@altlinux.org> 0.12.1-alt1
- Update to 0.12.1 (2024-06-06).

* Sat Apr 20 2024 Vitaly Chikunov <vt@altlinux.org> 0.12.0-alt1
- Update to 0.12.0 (2024-04-19).
- Switch to LLVM 17.

* Sat Aug 12 2023 Vitaly Chikunov <vt@altlinux.org> 0.11.0-alt1
- Update to 0.11.0 (2023-08-03).
- spec: Add simplest checkinstall package with a test.

* Sat Jun 03 2023 Vitaly Chikunov <vt@altlinux.org> 0.10.1-alt2
- Add simple %%check section.
- Fix crash on Intel x86-64 CPUs (ALT#46366).

* Fri Jan 20 2023 Vitaly Chikunov <vt@altlinux.org> 0.10.1-alt1
- Update to 0.10.1 (2023-01-17).

* Wed Nov 02 2022 Vitaly Chikunov <vt@altlinux.org> 0.10.0-alt1
- Update to 0.10.0 (2022-10-31).

* Sat Apr 16 2022 Vitaly Chikunov <vt@altlinux.org> 0.9.1-alt1
- Updated to 0.9.1 (2022-02-14).

* Fri Sep 10 2021 Vitaly Chikunov <vt@altlinux.org> 0.8.1-alt1
- First import of 0.8.1 (2021-09-06).
