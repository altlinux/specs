# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libblake3
Version: 1.5.3
Release: alt1
Summary: The official C implementations of the BLAKE3 cryptographic hash function
License: CC0-1.0 or Apache-2.0 or Apache-2.0 with LLVM-exception
Group: System/Libraries
Url: https://blake3.io/
Vcs: https://github.com/BLAKE3-team/BLAKE3
# Docs: https://github.com/BLAKE3-team/BLAKE3-specs

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: banner
BuildRequires: cmake
%{?!_without_check:%{?!_disable_check:BuildRequires: python3 /proc}}

%description
BLAKE3 is a cryptographic hash function that is:
- Much faster than MD5, SHA-1, SHA-2, SHA-3, and BLAKE2.
- Secure, unlike MD5 and SHA-1. And secure against length extension,
  unlike SHA-2.
- Highly parallelizable across any number of threads and SIMD lanes, because
  it's a Merkle tree on the inside.
- Capable of verified streaming and incremental updates, again because it's
  a Merkle tree.
- A PRF, MAC, KDF, and XOF, as well as a regular hash.
- One algorithm with no variants, which is fast on x86-64 and also on smaller
  architectures.

%package devel
Summary: %summary
Group: Development/C
Requires: %name = %EVR

%description devel
%summary

%package checkinstall
Summary: CI for %name-devel
Group: Development/Other
BuildArch: noarch
Requires(pre): %name-devel = %EVR
Requires(pre): gcc

%description checkinstall
%summary.

%prep
%setup
sed -i 's/"blake3.h"/<blake3.h>/' c/example.c
# Now it's used only for testing.
ln -s Makefile.altlinux c/GNUmakefile
# aarch64 does not support `-mfpu=neon` flag, armh should not have it.
sed -i '/blake3_neon.c.*BLAKE3_CFLAGS_NEON/d' c/CMakeLists.txt

%build
cd c
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
cd c
%cmake_install

%check
cd c
banner check
set -o pipefail
%ifarch aarch64
  # Leak sanitizer is so slow there.
  export ASAN_OPTIONS=leak_check_at_exit=0
%endif
make check 2>&1 | tail

%pre checkinstall
set -exo pipefail
cd /tmp
gcc `pkg-config --cflags libblake3` -o example %_defaultdocdir/%name-devel-%version/example.c `pkg-config --libs libblake3`
./example < /dev/null | grep af1349b9f5f9a1a6a0404dea36dcc9499bcb25c9adc112b7cc9a93cae41f3262
rm example

%files
%doc LICENSE* README.md
%_libdir/libblake3.so.*

%files devel
%doc c/README.md c/example.c CONTRIBUTING.md blake3.pdf
%_includedir/blake3.h
%_libdir/libblake3.so
%_libdir/cmake/blake3
%_pkgconfigdir/%name.pc

%files checkinstall

%changelog
* Tue Jul 30 2024 Vitaly Chikunov <vt@altlinux.org> 1.5.3-alt1
- Update to 1.5.3 (2024-07-14).

* Wed Mar 13 2024 Vitaly Chikunov <vt@altlinux.org> 1.5.1-alt1
- Update to 1.5.1 (2024-03-12).

* Thu Sep 21 2023 Vitaly Chikunov <vt@altlinux.org> 1.5.0-alt1
- Update to 1.5.0 (2023-09-20).

* Sun Jun 11 2023 Vitaly Chikunov <vt@altlinux.org> 1.4.0-alt1
- Update to 1.4.0 (2023-06-08).
- spec: Switch to CMake when building.

* Mon Feb 14 2022 Vitaly Chikunov <vt@altlinux.org> 1.3.1-alt1
- Updated to 1.3.1 (2022-02-14).

* Sat Jan 08 2022 Vitaly Chikunov <vt@altlinux.org> 1.3.0-alt1
- Updated to 1.3.0 (2022-01-07).

* Thu Nov 11 2021 Vitaly Chikunov <vt@altlinux.org> 1.2.0-alt1
- Update to 1.2.0 (2021-11-05).
- Build with SIMD optimizations (on x86_64 and aarch64).
- Clean up libblake3 exported symbols.
- spec: Improve testing.

* Wed Aug 04 2021 Vitaly Chikunov <vt@altlinux.org> 1.0-alt1
- First import of version 1.0.0 (2021-05-18).
