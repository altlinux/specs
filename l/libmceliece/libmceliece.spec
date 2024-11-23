# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libmceliece
Version: 20241009
Release: alt1
Summary: Classic McEliece microlibrary
License: LicenseRef-PD-hp OR CC0-1.0 OR 0BSD OR MIT-0 OR MIT
Group: System/Libraries
Url: https://lib.mceliece.org/

Source: %name-%version.tar
BuildRequires(pre): rpm-macros-valgrind
BuildRequires: libcpucycles-devel
BuildRequires: librandombytes-devel
BuildRequires: python3
BuildRequires: rpm-build-python3
%ifarch %valgrind_arches
BuildRequires: valgrind-devel
%endif

%description
libmceliece is a Classic McEliece microlibrary. libmceliece has a very
simple stateless API based on the SUPERCOP API, with wire-format inputs
and outputs, providing functions that directly match the KEM operations
provided by Classic McEliece, such as functions

    mceliece6960119_keypair
    mceliece6960119_enc
    mceliece6960119_dec

for the mceliece6960119 KEM.

Internally, libmceliece is based on the official Classic McEliece
software, specifically the vec implementation (designed to work portably
across CPUs) and the avx implementation (designed for higher performance
on Intel/AMD CPUs with AVX2 instructions). libmceliece includes automatic
run-time selection of implementations.

libmceliece is intended to be called by larger multi-function libraries
(such as traditional cryptographic libraries), including libraries in
other languages via FFI. The idea is that libmceliece takes responsibility
for the details of Classic McEliece computation, including optimization,
timing-attack protection, and (in ongoing work) verification, freeing up
the calling libraries to concentrate on application-specific needs such
as protocol integration. Applications can also call libmceliece directly.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
%summary.

%package checkinstall
Summary: CI tests for %name
Group: Development/Other
Requires(pre): %name-devel = %EVR
Requires(pre): valgrind

%description checkinstall
%summary.

%prep
%setup

%build
%define optflags_lto %nil
%add_optflags %(getconf LFS_CFLAGS)
# -Wl,-z,noexecstack
cat -n compilers/default
echo "gcc %optflags -fPIC -fwrapv" > compilers/default
./configure \
	--prefix=%buildroot/usr \
%ifnarch %valgrind_arches
	--no-valgrind \
%endif
	%nil
gcc() ( set -x && command gcc "$@" ); export -f gcc
%make_build

%install
%makeinstall_std
# No static libs.
rm %buildroot%_libexecdir/*.a
# Fix incorrect libdir location on 64-bit systems.
[ -d %buildroot%_libdir ] || mv %buildroot%_libexecdir %buildroot%_libdir
# Fix incorrect mandir location.
mkdir -p %buildroot%_datadir
mv %buildroot/%_prefix/man %buildroot%_datadir

%pre checkinstall
set -exo pipefail
%ifarch %valgrind_arches
# "A compiled version of libmceliece that does not pass the full test suite is
#  not supported."
# "One run of mceliece-fulltest was observed to take 752 core-minutes on a
#  2.245GHz EPYC 7742 without Turbo Boost. This test finished in around 39
#  minutes of real time; mceliece-fulltest includes some automatic
#  parallelization."
time mceliece-fulltest
%else
time mceliece-test
%endif

%check
export LD_LIBRARY_PATH=%buildroot%_libdir PATH=%buildroot%_bindir:$PATH
for i in %buildroot%_bindir/mceliece*[0-9]-keypair; do
	b=$(basename -s-keypair $i)
	$b-keypair 5>$b.publickey 9>$b.secretkey
	$b-enc >$b.ciphertext 7>$b.sessionkeyA 4<$b.publickey
	$b-dec <$b.ciphertext 7>$b.sessionkeyB 8<$b.secretkey
	diff -sq $b.sessionkey?
done
ls -lad mceliece*.*
sha256sum mceliece*.sessionkey*

%files
%_bindir/mceliece[0-9]*
%_libdir/libmceliece.so.*
%_man1dir/mceliece.1*
%_man1dir/mceliece[0-9]*.1*

%files devel
%_bindir/mceliece-*
%_includedir/mceliece.h
%_libdir/libmceliece.so
%_man1dir/mceliece-*.1*
%_man3dir/*.3*

%ifarch x86_64 aarch64
# aarch64: 41006.93user 151.47system 36:42.86elapsed 1868%CPU (0avgtext+0avgdata 58840maxresident)k
# i586: hasher-privd: parent: work_limits_ok: time elapsed limit (2400 seconds) exceeded
# ppc64le: hasher-privd: parent: work_limits_ok: time elapsed limit (2400 seconds) exceeded
# x86_64: 39815.55user 599.86system 30:11.43elapsed 2231%CPU (0avgtext+0avgdata 61440maxresident)k
%files checkinstall
%endif

%changelog
* Sat Nov 23 2024 Vitaly Chikunov <vt@altlinux.org> 20241009-alt1
- Correct version to 20241009 (2024-10-09).
- Previous release is incorrectly versioned as 20230612, in real it
  is 20241009.

* Fri Jun 23 2023 Vitaly Chikunov <vt@altlinux.org> 20230612-alt1
- First import 20230612 (2023-06-23).
