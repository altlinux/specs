# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method rpath=relaxed

%define llvm_ver 21
%define llvm_pkgver %llvm_ver.1

Name:    zig
Version: 0.16.0
Release: alt1
Summary: General-purpose programming language and toolchain for maintaining robust, optimal, and reusable software

# ./LICENSE - MIT
# ./lib/
#   libcxx/LICENSE.TXT - Apache-2.0 with LLVM-exception
#   libcxxabi/LICENSE.TXT - Apache-2.0 with LLVM-exception
#   libunwind/LICENSE.TXT - Apache-2.0 with LLVM-execption
#   libc/
#     musl/COPYRIGHT - MIT
#     include/generic-freebsd/sys/copyright.hi - BSD-2-Clause
#     freebsd/COPYRIGHT - BSD-1-Clause and BSD-2-Clause and BSD-4-Clause (guessing from SPDX-Identifiers)
#     mingw/COPYING - ZPL-2.1
#     glibc/LICENSES - LGPL-2.1+ and ISC and BSD-3-Clause and GPL-2.0-or-later (from our spec)
#     wasi/LICENSE - Apache-2.0 with LLVM-exception and Apache-2.0 and MIT and CC0 and BSD-2-Clause
License: MIT and Apache-2.0 with LLVM-exception and BSD-2-Clause and BSD-1-Clause and BSD-4-Clause and ZPL-2.1 and LGPL-2.1+ and ISC and BSD-3-Clause and GPL-2.0-or-later and Apache-2.0 and CC0
Group:   Development/C
Url:     https://ziglang.org/
Vcs:     https://codeberg.org/ziglang/zig.git

# /proc is required or zig will output FileNotFound
Requires: /proc

ExclusiveArch: %zig_arches

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-zig
BuildRequires: /proc
BuildRequires: chrpath
BuildRequires: clang%llvm_pkgver-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel
BuildRequires: libtinfo-devel
BuildRequires: libxml2-devel
BuildRequires: lld%llvm_pkgver-devel
BuildRequires: llvm%llvm_pkgver-devel
BuildRequires: zlib-devel

%description
%summary.

%package checkinstall
Summary: CI test for zig
Group: Development/Other
Requires(pre): zig

%description checkinstall
%summary.

%prep
%setup

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
zig version | grep -Fx '%version'
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
* Tue Sep 01 2026 Ilya Sorochan <k0tran@altlinux.org> 0.16.0-alt1
- Update to 0.16.0 (2026-04-13), (ALT#60236).
- Switch to LLVM 21.
- Switch to building from version tag.
- Small spec cleanup and reordering.

* Sat Oct 11 2025 Vitaly Chikunov <vt@altlinux.org> 0.15.2-alt1
- Update to 0.15.2 (2025-10-10).

* Fri Aug 22 2025 Vitaly Chikunov <vt@altlinux.org> 0.15.1-alt1
- Update to 0.15.1 (2025-08-19).

* Mon May 26 2025 Vitaly Chikunov <vt@altlinux.org> 0.14.1-alt1
- Update to 0.14.1 (2025-05-21).

* Tue Apr 22 2025 Ilya Sorochan <k0tran@altlinux.org> 0.14.0-alt1
- Update to 0.14.0 (2025-03-03).
- Switch to LLVM 19.
- Remove RSS limit for zig.

* Thu Aug 01 2024 Vitaly Chikunov <vt@altlinux.org> 0.13.0-alt1
- Update to 0.13.0 (2024-06-06), (ALT#50967).
- Switch to LLVM 18.

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
