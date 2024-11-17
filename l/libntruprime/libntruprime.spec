# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libntruprime
Version: 20241021
Release: alt1
Summary: A microlibrary for the Streamlined NTRU Prime cryptosystem
License: LicenseRef-PD-hp OR CC0-1.0 OR 0BSD OR MIT-0 OR MIT
Group: System/Libraries
Url: https://libntruprime.cr.yp.to/

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-valgrind
BuildRequires: libcpucycles-devel
BuildRequires: librandombytes-devel
BuildRequires: python3
BuildRequires: python3-module-capstone
BuildRequires: rpm-build-python3
%ifarch %valgrind_arches
BuildRequires: valgrind-devel
%endif

%description
libntruprime is a microlibrary for the Streamlined NTRU Prime cryptosystem.
Streamlined NTRU Prime (sntrup) is a lattice-based cryptosystem.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
libntruprime is a microlibrary for the Streamlined NTRU Prime cryptosystem.
Streamlined NTRU Prime (sntrup) is a lattice-based cryptosystem.

libntruprime has a very simple stateless API based on the SUPERCOP API.

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
# "A compiled version of libntruprime that does not pass the full test suite is
#  not supported."
# "One run of ntruprime-fulltest was observed to take 529 core-minutes on a
#  2.245GHz EPYC 7742 with overclocking disabled. This test finished in 35
#  minutes of real time [with automatic parallelization.]"
time ntruprime-fulltest
%else
time ntruprime-test
%endif

%files
%_bindir/sntrup*
%_libdir/libntruprime.so.*
%_man1dir/sntrup*.1*

%files devel
%_bindir/ntruprime-*
%_includedir/ntruprime.h
%_libdir/libntruprime.so
%_man1dir/ntruprime-*.1*
%_man3dir/sntrup*.3*

%ifarch x86_64 aarch64
# x86_64:  29750.81user 170.27system 37:08.04elapsed 1342%CPU (0avgtext+0avgdata 55624maxresident)k
# aarch64: 29073.84user 111.78system 31:03.86elapsed 1565%CPU (0avgtext+0avgdata 50228maxresident)k
# other:
#   hasher-privd: parent: work_limits_ok: time elapsed limit (2400 seconds) exceeded
#   hsh-install: Packages installation failed.
%files checkinstall
%endif

%changelog
* Sun Nov 17 2024 Vitaly Chikunov <vt@altlinux.org> 20241021-alt1
- First import libntruprime-20241021.
