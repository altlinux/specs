# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define sover 1
Name: librandombytes
Version: 20240318
Release: alt1
Summary: A simple API for applications generating fresh randomness
License: LicenseRef-PD-hp OR CC0-1.0 OR 0BSD OR MIT-0 OR MIT
Group: System/Libraries
Url: https://randombytes.cr.yp.to/

Source: %name-%version.tar
BuildRequires: libssl-devel
BuildRequires: python3

%description
%summary.

%package -n librandombytes%sover
Summary: Library to access Linux kernel randomness
Group: System/Libraries

%description -n librandombytes%sover
%summary.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: librandombytes%sover = %EVR

%description devel
librandombytes provides a simple API for applications generating fresh
randomness: include <randombytes.h>, call randombytes(x,xbytes) whenever
desired to generate fresh random bytes x[0], x[1], ..., x[xbytes-1],
and link with -lrandombytes.

%prep
%setup

%build
%define optflags_lto %nil
%add_optflags %(getconf LFS_CFLAGS)
cat -n compilers/default
echo "gcc %optflags -fPIC -fwrapv" > compilers/default
./configure --prefix=%buildroot/usr
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
# "There are default symlinks to librandombytes-kernel, but you should allow
#  the sysadmin to change these symlinks to librandombytes-openssl by simply
#  installing a librandombytes-openssl package."
# This is IMPOSSIBLE to implement in out RPM system with Conflicts nor with Alternatives.
# Also, the SONAME of the backend libs make them NOT runtime interchangeable anyway.
# Even if we fix SONAME issue our brp ldconfig call creates symlink
# (librandombytes.so.1 -> librandombytes-openssl.so.1) making it not packageable
# again (due to inherent conflict).
# Thus, we follow the lead of Debian and do not package librandombytes-openssl at all.
rm -v %buildroot%_libdir/librandombytes-openssl.so{,.%sover}

%check
export LD_LIBRARY_PATH=%buildroot%_libdir PATH=%buildroot%_bindir:$PATH
randombytes-info

%files -n librandombytes%sover
%_libdir/librandombytes-kernel.so.%sover
%_libdir/librandombytes.so.%sover

%files devel
%doc doc/*.md
%_bindir/randombytes-info
%_includedir/randombytes.h
%_libdir/librandombytes.so
%_libdir/librandombytes-kernel.so
%_man1dir/randombytes-info.1*
%_man3dir/randombytes.3*

%changelog
* Sun Nov 17 2024 Vitaly Chikunov <vt@altlinux.org> 20240318-alt1
- First import version 20240318.
