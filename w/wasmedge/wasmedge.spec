# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

# LLVM-based ahead-of-time compilation runtime.
# - Fedora builds AOT version by default (wasmedge package) and non-AOT version
#   as a Conflicting wasmedge-rt package (using RemovePathPostfixes:, which we
#   don't have).
# - SUSE does not build AOT at all, wasmedge cannot compile.
# - Debian always builds with AOT in wasmedge.
# Also, none of them build extensions.
%def_enable aot

%define sover 0
Name: wasmedge
Version: 0.15.0
Release: alt1
Summary: A lightweight, high-performance, and extensible WebAssembly runtime
License: Apache-2.0
Group: Development/Other
Url: https://WasmEdge.org
Vcs: https://github.com/WasmEdge/WasmEdge
ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libfmt-devel
BuildRequires: libspdlog-devel
BuildRequires: ninja-build
BuildRequires: zlib-devel
%if_enabled aot
BuildRequires: lld-devel
BuildRequires: llvm-devel
%endif
%{?!_without_check:%{?!_disable_check:
BuildRequires: clang
BuildRequires: wabt
}}

%description
WasmEdge is a lightweight, high-performance, and extensible WebAssembly
runtime. It is the fastest Wasm VM.

%package -n libwasmedge%sover
Summary: WasmEdge shared library
Group: System/Libraries

%description -n libwasmedge%sover
%summary.

%package devel
Summary: Development files for WasmEdge
Group: Development/C
Requires: libwasmedge%sover = %EVR

%description devel
%summary.

%prep
%setup
echo -n "%version-%release" > VERSION

%build
%define _wasmedgedir %_libdir/%name
%add_optflags -Wno-deprecated-declarations
%cmake \
	-DBUILD_SHARED_LIBS=OFF \
%if_disabled aot
	-DWASMEDGE_USE_LLVM=OFF \
%endif
	%nil
%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_wasmedgedir

%check
PATH=%buildroot%_bindir:$PATH
export LD_LIBRARY_PATH=%buildroot%_libdir
wasmedge -v
wat2wasm -o factorial.wasm examples/wasm/factorial.wat
wasmedge factorial.wasm fac 10 | grep 3628800
%if_enabled aot
wasmedgec factorial.wasm fac.wasm
wasmedge fac.wasm fac 10 | grep 3628800
wasmedge --enable-all-statistics fac.wasm fac 10 | grep -x '.* Executed wasm instructions count: 0'
%endif
clang --target=wasm32 -nostdlib -o hello.wasm .gear/hello.c
wasmedge hello.wasm | grep 'hello world'
ls -la *.wasm

%files
%doc *.md
%_bindir/wasmedge
%if_enabled aot
%_bindir/wasmedgec
%endif

%files -n libwasmedge%sover
%doc LICENSE*
%_libdir/libwasmedge.so.%sover
%_libdir/libwasmedge.so.%sover.*
# WasmEdge plug-in dir (which we don't build yet):
%dir %_wasmedgedir

%files devel
%doc docs examples
%_includedir/wasmedge
%_libdir/libwasmedge.so

%changelog
* Mon Aug 04 2025 Vitaly Chikunov <vt@altlinux.org> 0.15.0-alt1
- Update to 0.15.0 (2025-08-04).

* Mon May 19 2025 Vitaly Chikunov <vt@altlinux.org> 0.14.1-alt1
- Experimental import 0.14.1 (2024-09-18).
