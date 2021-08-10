# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libblake2
Summary: BLAKE2 official implementations
Version: 20190724
Release: alt2
License: Apache-2.0 or CC0-1.0 or OpenSSL
Group: System/Libraries
Url: https://www.blake2.net/
Vcs: https://github.com/blake2/blake2

Source: %name-%version.tar

%description
BLAKE2 is a cryptographic hash function faster than MD5, SHA-1, SHA-2, and
SHA-3, yet is at least as secure as the latest standard SHA-3. BLAKE2 has been
adopted by many projects due to its high speed, security, and simplicity.

%package devel
Summary: %summary
Group: Development/C
Conflicts: libb2-devel
Requires: %name = %EVR

%description devel
%summary.

%prep
%setup
# Unused source files that will clobber glob.
rm neon/blake2b-neon.c
rm neon/blake2s-neon.c
# Delete invalid default options.
sed -i 's/-march=armv7-a//;s/-mfpu=neon-vfpv4//;s/-mfloat-abi=hard//;s/-fopenmp//' neon/makefile
# Select optimized implementation.
SRC=ref
%ifarch x86_64
SRC=sse
%endif
%ifarch aarch64
SRC=neon
%endif
%ifarch ppc64le
SRC=power8
%endif
ln -s $SRC src

%build
cd src
%define _optlevel 3
FLAGS="%optflags -shared -fPIC -Wl,-soname,libblake2.so.0"
# Build and run self-test binaries.
make
# Finally make the lib.
gcc $FLAGS -o libblake2.so.0 blake2*.c blake2*.h

%install
cd src
mkdir -p %buildroot%_includedir
install -Dp blake2.h %buildroot%_includedir/
install -Dp libblake2.so.0 %buildroot%_libdir/libblake2.so.0.0.0
ln -s libblake2.so.0.0.0   %buildroot%_libdir/libblake2.so.0
ln -s libblake2.so.0.0.0   %buildroot%_libdir/libblake2.so

%check
# 1. 'make' above did full testing for all KATs.
# 2. Build and run sample b2sum.
cd b2sum
export LD_LIBRARY_PATH=%buildroot%_libdir
FLAGS="%optflags -I%buildroot%_includedir -L%buildroot%_libdir -lblake2"
gcc -o b2sum b2sum.c $FLAGS
./b2sum -a blake2b  < /dev/null \
  | grep 786a02f742015903c6c6fd852552d272912f4740e15847618a86e217f71f5419d25e1031afee585313896444934eb04b903a685b1448b755d56f701afe9be2ce
./b2sum -a blake2s  < /dev/null | grep 69217a3079908094e11121d042354a7c1f55b6482ca1a51e1b250dfd1ed0eef9
%ifarch %ix86 x86_64
# 3. Benchmark.
# Shows cpucycles per byte. Test is only on x86, because it requires
# reading cpucycles which is not enabled on other kernels, nor
# implemented in the bench.
cd ../bench
gcc -o bench-blake2b bench.c ../src/blake2b[^p]*c -DSUPERCOP
./bench-blake2b
%endif

%files
%_libdir/libblake2.so.*

%files devel
%doc COPYING README.md
%_includedir/blake2.h
%_libdir/libblake2.so

%changelog
* Thu Aug 05 2021 Vitaly Chikunov <vt@altlinux.org> 20190724-alt2
- Small spec improvements.

* Wed Aug 04 2021 Vitaly Chikunov <vt@altlinux.org> 20190724-alt1
- First import of 20190724-10-g54f4faa (2021-05-28).
