# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: lib25519
Version: 20241004
Release: alt1
Summary: A microlibrary for the X25519 encryption system and the Ed25519 signature system
License: LicenseRef-PD-hp OR CC0-1.0 OR 0BSD OR MIT-0 OR MIT
Group: System/Libraries
Url: https://lib25519.cr.yp.to/

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
lib25519 is a microlibrary for the X25519 encryption system and the Ed25519
signature system, both of which use the Curve25519 elliptic curve.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
lib25519 is a microlibrary for the X25519 encryption system and the Ed25519
signature system, both of which use the Curve25519 elliptic curve.

lib25519 has a very simple stateless API based on the SUPERCOP API.

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
cat -n compilers/default
echo "gcc %optflags -fPIC -fwrapv" > compilers/default
./configure \
	--prefix=%buildroot/usr \
%ifnarch %valgrind_arches
	--no-valgrind \
%endif
	%nil
%make_build

%install
%makeinstall_std
# We don't install static libraries unless really required.
rm %buildroot/usr/lib/%{name}*.a
# Fix incorrect installs.
[ -d %buildroot%_libdir ] || mv %buildroot/usr/lib %buildroot%_libdir
mkdir -p %buildroot%_mandir
mv %buildroot/usr/man/man3 %buildroot%_man3dir
mv %buildroot/usr/man/man1 %buildroot%_man1dir

%pre checkinstall
set -exo pipefail
%ifarch %valgrind_arches
# "A compiled version of lib25519 that does not pass the full test suite is not supported."
time lib25519-fulltest
%else
time lib25519-test
%endif

%files
%_bindir/ed25519-keypair
%_bindir/ed25519-open
%_bindir/ed25519-sign
%_bindir/x25519-dh
%_bindir/x25519-keypair
%_libdir/lib25519.so.1
%_man1dir/ed*.1*
%_man1dir/x*.1*

%files devel
%_bindir/lib25519-fulltest
%_bindir/lib25519-speed
%_bindir/lib25519-test
%_includedir/lib25519.h
%_libdir/lib25519.so
%_man1dir/lib*.1*
%_man3dir/lib*.3*

%files checkinstall

%changelog
* Sat Nov 16 2024 Vitaly Chikunov <vt@altlinux.org> 20241004-alt1
- First import lib25519-20241004 (2024-10-04).
