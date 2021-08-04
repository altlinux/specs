# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: libblake3
Version: 1.0
Release: alt1
Summary: The official C implementations of the BLAKE3 cryptographic hash function
License: Apache-2.0 or CC0-1.0
Group: System/Libraries
Url: https://blake3.io/
Vcs: https://github.com/blake3-team/blake3
# Docs: https://github.com/BLAKE3-team/BLAKE3-specs

Source: %name-%version.tar

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

%prep
%setup
sed -i 's/"blake3.h"/<blake3.h>/' c/example.c

%build
cd c
%define _optlevel 3
FLAGS="%optflags -shared -fPIC -Wl,-soname,libblake3.so.0"
%ifarch x86_64
# Build Asm implementation.
# There is also intrinsic implementation that maybe useful for someone.
gcc $FLAGS -o libblake3.so.0 \
	blake3.c blake3_dispatch.c blake3_portable.c \
	blake3_sse2_x86-64_unix.S \
	blake3_sse41_x86-64_unix.S \
	blake3_avx2_x86-64_unix.S \
	blake3_avx512_x86-64_unix.S
%endif
%ifarch aarch64
# Aarch64 should always have NEON, armv7 not always.
gcc $FLAGS -o libblake3.so.0 \
	-DBLAKE3_USE_NEON \
	blake3.c blake3_dispatch.c blake3_portable.c \
	blake3_neon.c
%endif
# If nothing else, build portable implementation.
[ -e libblake3.so ] ||
gcc $FLAGS -o libblake3.so.0 \
	-DBLAKE3_NO_SSE2 \
	-DBLAKE3_NO_SSE41 \
	-DBLAKE3_NO_AVX2 \
	-DBLAKE3_NO_AVX512 \
	blake3.c blake3_dispatch.c blake3_portable.c

%install
cd c
mkdir -p %buildroot%_includedir
install -Dp blake3.h %buildroot%_includedir/
mkdir -p %buildroot%_libdir
install -Dp libblake3.so.0 %buildroot%_libdir/libblake3.so.0.0.0
ln -s libblake3.so.0.0.0   %buildroot%_libdir/libblake3.so.0
ln -s libblake3.so.0.0.0   %buildroot%_libdir/libblake3.so

%check
cd c
export LD_LIBRARY_PATH=$PWD
ln -s libblake3.so.0 libblake3.so
gcc -o example %optflags -I. example.c -L. -lblake3
./example < /dev/null | grep af1349b9f5f9a1a6a0404dea36dcc9499bcb25c9adc112b7cc9a93cae41f3262

%files
%doc LICENSE README.md
%_libdir/libblake3.so.*

%files devel
%doc c/README.md c/example.c
%_includedir/blake3.h
%_libdir/libblake3.so

%changelog
* Wed Aug 04 2021 Vitaly Chikunov <vt@altlinux.org> 1.0-alt1
- First import of version 1.0.0 (2021-05-18).
