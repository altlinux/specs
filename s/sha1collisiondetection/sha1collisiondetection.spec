# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: sha1collisiondetection
Version: 1.0.3
Release: alt1
Summary: Command line tool to detect SHA-1 collision in a file
Group: Other
License: MIT
Vcs: https://github.com/cr-marcstevens/sha1collisiondetection
Url: https://marc-stevens.nl/research/papers/C13-S.pdf
Source: %name-%version.tar
Requires: libsha1detectcoll1 = %EVR

%description
This library and command line tool were designed as near drop-in
replacements for common SHA-1 libraries and sha1sum. They will compute the
SHA-1 hash of any given file and additionally will detect cryptanalytic
collision attacks against SHA-1 present in each file. It is very fast
and takes less than twice the amount of time as regular SHA-1.

%package -n libsha1detectcoll1
Summary: Library to detect SHA-1 collision in a file
Group: System/Libraries

%description -n libsha1detectcoll1
%summary.

%package -n libsha1detectcoll-devel
Summary: Depelopment files to detect SHA-1 collision in a file
Group: Development/C
Requires: libsha1detectcoll1 = %EVR

%description -n libsha1detectcoll-devel
%summary.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%make_build TARGETCFLAGS="%optflags" PREFIX=%_prefix LIBDIR=%_libdir

%install
%make_install PREFIX=%buildroot%_prefix LIBDIR=%buildroot%_libdir install
find %buildroot -name '*.a' -delete
rmdir %buildroot%_includedir/sha1dc/{%_lib,bin}

%check
make test

%files
%doc README.md
%_bindir/sha1dcsum
%_bindir/sha1dcsum_partialcoll

%files -n libsha1detectcoll1
%_libdir/libsha1detectcoll.so.*

%files -n libsha1detectcoll-devel
%doc LICENSE.txt
%_includedir/sha1dc
%_libdir/libsha1detectcoll.so

%changelog
* Tue Aug 31 2021 Vitaly Chikunov <vt@altlinux.org> 1.0.3-alt1
- First import of stable-v1.0.3-37-gb4a7b0b (2020-12-09).
