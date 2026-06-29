# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: wabt
Version: 1.0.41
Release: alt1
Summary: The WebAssembly Binary Toolkit
License: Apache-2.0
Group: Development/Other
Url: https://github.com/WebAssembly/wabt
Vcs: https://github.com/WebAssembly/wabt.git

Source: %name-%version.tar
Source1: gtest-0.tar
Source2: picosha2-0.tar
Source3: ply-0.tar
Source4: simde-0.tar
Source5: munit-0.tar
Source6: testsuite-0.tar
Source7: uvwasi-0.tar
Source8: wasm-c-api-0.tar
BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: openssl-devel
%{?!_without_check:%{?!_disable_check:
BuildRequires: /proc
}}

%description
WABT (we pronounce it "wabbit") is a suite of tools for WebAssembly.
These tools are intended for use in (or for development of) toolchains
or other systems that want to manipulate WebAssembly files. Unlike
the WebAssembly spec interpreter (which is written to be as simple,
declarative and "speccy" as possible), they are written in C/C++ and
designed for easier integration into other systems. Unlike Binaryen these
tools do not aim to provide an optimization platform or a higher-level
compiler target; instead they aim for full fidelity and compliance with
the spec (e.g. 1:1 round-trips with no changes to instructions).

%prep
%setup
tar xf %SOURCE1 -C third_party
tar xf %SOURCE2 -C third_party
tar xf %SOURCE3 -C third_party
tar xf %SOURCE4 -C third_party
tar xf %SOURCE5 -C third_party/simde/test
tar xf %SOURCE6 -C third_party
tar xf %SOURCE7 -C third_party
tar xf %SOURCE8 -C third_party
%ifnarch x86_64 %ix64
# SIMD is emulated on other arches and 120 sec is not enough.
sed -i 's/run-tests\.py/& --timeout=600/' CMakeLists.txt
%endif

%build
%define optflags_lto %nil
%add_optflags %(getconf LFS_CFLAGS)
%cmake \
%if_disabled check
	-DBUILD_TESTS=OFF -DBUILD_LIBWASM=OFF \
%endif
	%nil
%cmake_build

%install
%cmake_install

%check
%buildroot%_bindir/wat2wasm --version
%cmake_build --target run-unittests
# test/pipes.txt requires /proc
%ifarch x86_64
# aarch64: taking 33:15 on aarch64 due to SIMD emulation.
# i586: https://github.com/WebAssembly/wabt/issues/1044
%cmake_build --target run-tests
%endif

%files
%define _customdocdir %_docdir/%name
%doc *.md LICENSE
%_bindir/spectest-interp
%_bindir/wasm2c
%_bindir/wasm2wat
%_bindir/wasm-decompile
%_bindir/wasm-interp
%_bindir/wasm-objdump
%_bindir/wasm-stats
%_bindir/wasm-strip
%_bindir/wasm-validate
%_bindir/wast2json
%_bindir/wat2wasm
%_bindir/wat-desugar
%_libdir/libwasm-rt-impl.a
%_libdir/libwabt.a
%_man1dir/wa*.1*
%_man1dir/spectest*.1*
%_datadir/%name
%_includedir/%name
%_includedir/wasm-*.h
%_cmakedir/%name

%changelog
* Mon Jun 29 2026 Sergey Zhidkih <rx1513@altlinux.org> 1.0.41-alt1
- Update to 1.0.41 (2026-05-06).

* Sat Mar 21 2026 Vitaly Chikunov <vt@altlinux.org> 1.0.40-alt1
- Update to 1.0.40 (2026-03-10).

* Thu Nov 06 2025 Vitaly Chikunov <vt@altlinux.org> 1.0.39-alt1
- Update to 1.0.39 (2025-11-04).

* Sat Oct 11 2025 Vitaly Chikunov <vt@altlinux.org> 1.0.38-alt1
- Update to 1.0.38 (2025-09-23).

* Sun May 18 2025 Vitaly Chikunov <vt@altlinux.org> 1.0.37-alt1
- Experimentally import 1.0.37 (2025-03-01).
