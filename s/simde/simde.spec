# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: simde
Summary: SIMD Everywhere: Portable implementations of SIMD intrinsics
Version: 0.7.2
Release: alt2
License: MIT
Group: Development/C
Url: https://simd-everywhere.github.io/blog/
Vcs: https://github.com/simd-everywhere/simde

Source: %name-%version.tar

BuildRequires: meson
BuildRequires: gcc-c++

%description
%summary.

%package devel
Summary: SIMD Everywhere: Portable implementations of SIMD intrinsics
Group: Development/C
Provides: libsimde-devel

%description devel
The SIMDe header-only library provides fast, portable implementations
of SIMD intrinsics on hardware which doesn't natively support them,
such as calling SSE functions on ARM. There is no performance penalty
if the hardware supports the native implementation (e.g., SSE/AVX runs
at full speed on x86, NEON on ARM, etc.).

%prep
%setup

%build
# Only tests need compiling.
%meson
%meson_build

%install
mkdir -p %buildroot%_includedir
cp -a simde %buildroot%_includedir

%check
%meson_test

%files devel
%doc COPYING README.md
%_includedir/simde

%changelog
* Sat Oct 02 2021 Vitaly Chikunov <vt@altlinux.org> 0.7.2-alt2
- sse2: ignore broken _mm_loadu_si{16,32} on GCC(11).

* Sun Aug 15 2021 Vitaly Chikunov <vt@altlinux.org> 0.7.2-alt1
- First import of v0.7.2 (2021-01-24).
