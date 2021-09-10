# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: zig
Version: 0.8.1
Release: alt1
Summary: General-purpose programming language and toolchain for maintaining robust, optimal, and reusable software
# TODO: Zig lib is bundled with a lot of third party with other licenses.
License: MIT
Group: Development/C
Url: https://ziglang.org/
Vcs: https://github.com/ziglang/zig/

# https://ziglang.org/download/0.8.0/release-notes.html#Support-Table
#  armh: allocation failed
#  i586: allocation failed
#  ppc64le: error: example crashed
ExcludeArch: %ix86 armh ppc64le

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
# /proc is required or zig will output FileNotFound
BuildRequires: /proc
BuildRequires: clang-devel
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: lld-devel
BuildRequires: llvm-devel
BuildRequires: llvm-devel-static

%description
%summary.

%prep
%setup

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DLLD_INCLUDE_DIRS=$(llvm-config --includedir) \
	-DCLANG_LIBRARIES=$(llvm-config --libdir)/libclang-cpp.so \
	-DLLD_LIBDIRS=$(llvm-config --libdir) \
	-DZIG_PREFER_CLANG_CPP_DYLIB=true \
	-DZIG_VERSION="%version"
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/zig
%_prefix/lib/zig

%changelog
* Fri Sep 10 2021 Vitaly Chikunov <vt@altlinux.org> 0.8.1-alt1
- First import of 0.8.1 (2021-09-06).
