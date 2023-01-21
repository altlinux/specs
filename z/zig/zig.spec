# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method rpath=relaxed

Name: zig
Version: 0.10.1
Release: alt1
Summary: General-purpose programming language and toolchain for maintaining robust, optimal, and reusable software
# TODO: Zig lib is bundled with a lot of third party with other licenses.
License: MIT
Group: Development/C
Url: https://ziglang.org/
Vcs: https://github.com/ziglang/zig/

# https://ziglang.org/download/0.10.0/release-notes.html#Support-Table
# aarch64: OK   53:00
#    armh: allocation failed
#    i586: allocation failed
# ppc64le: OK 1:02:52
#  x86-64: OK   24:26
ExcludeArch: %ix86 armh

Source: %name-%version.tar

%define llvm_ver 15
BuildRequires(pre): rpm-macros-cmake
# /proc is required or zig will output FileNotFound
BuildRequires: /proc
BuildRequires: chrpath
BuildRequires: clang%llvm_ver.0-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel
BuildRequires: libtinfo-devel
BuildRequires: libxml2-devel
BuildRequires: lld%llvm_ver.0-devel
BuildRequires: llvm%llvm_ver.0-devel
BuildRequires: zlib-devel

%description
%summary.

%prep
%setup

%build
%define optflags_lto %nil
export CC=clang-%llvm_ver CXX=clang++-%llvm_ver LDFLAGS="-fuse-ld=lld $LDFLAGS"
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DZIG_USE_LLVM_CONFIG=ON \
	-DZIG_PREFER_CLANG_CPP_DYLIB=true \
	-DZIG_VERSION="%version"
%cmake_build

%install
export ZIG_VERBOSE_LINK=y ZIG_VERBOSE_CC=y
%cmake_install
chrpath -d %buildroot%_bindir/zig

%files
%doc LICENSE README.md
%_bindir/zig
%_prefix/lib/zig

%changelog
* Fri Jan 20 2023 Vitaly Chikunov <vt@altlinux.org> 0.10.1-alt1
- Update to 0.10.1 (2023-01-17).

* Wed Nov 02 2022 Vitaly Chikunov <vt@altlinux.org> 0.10.0-alt1
- Update to 0.10.0 (2022-10-31).

* Sat Apr 16 2022 Vitaly Chikunov <vt@altlinux.org> 0.9.1-alt1
- Updated to 0.9.1 (2022-02-14).

* Fri Sep 10 2021 Vitaly Chikunov <vt@altlinux.org> 0.8.1-alt1
- First import of 0.8.1 (2021-09-06).
