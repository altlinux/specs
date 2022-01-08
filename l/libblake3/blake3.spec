# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libblake3
Version: 1.3.0
Release: alt1
Summary: The official C implementations of the BLAKE3 cryptographic hash function
License: Apache-2.0 or CC0-1.0
Group: System/Libraries
Url: https://blake3.io/
Vcs: https://github.com/BLAKE3-team/BLAKE3
# Docs: https://github.com/BLAKE3-team/BLAKE3-specs

Source: %name-%version.tar

BuildRequires: banner
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
Summary: Checkinstall for %name-devel
Group: Development/Other
BuildArch: noarch
Requires(pre): %name-devel = %EVR
Requires(pre): gcc

%description checkinstall
%summary.

%prep
%setup
sed -i 's/"blake3.h"/<blake3.h>/' c/example.c
ln -s Makefile.altlinux c/GNUmakefile

%build
%define _optlevel 3
%add_optflags -Wextra -Wa,--noexecstack
CFLAGS="%optflags" \
%make_build -C c

%install
%makeinstall_std -C c

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
set -ex
cd /tmp
gcc -o example %_defaultdocdir/%name-devel-%version/example.c -lblake3
./example < /dev/null | grep af1349b9f5f9a1a6a0404dea36dcc9499bcb25c9adc112b7cc9a93cae41f3262
rm example

%files
%doc LICENSE README.md
%_libdir/libblake3.so.*

%files devel
%doc c/README.md c/example.c CONTRIBUTING.md blake3.pdf
%_includedir/blake3.h
%_libdir/libblake3.so

%files checkinstall

%changelog
* Sat Jan 08 2022 Vitaly Chikunov <vt@altlinux.org> 1.3.0-alt1
- Updated to 1.3.0 (2022-01-07).

* Thu Nov 11 2021 Vitaly Chikunov <vt@altlinux.org> 1.2.0-alt1
- Update to 1.2.0 (2021-11-05).
- Build with SIMD optimizations (on x86_64 and aarch64).
- Clean up libblake3 exported symbols.
- spec: Improve testing.

* Wed Aug 04 2021 Vitaly Chikunov <vt@altlinux.org> 1.0-alt1
- First import of version 1.0.0 (2021-05-18).
