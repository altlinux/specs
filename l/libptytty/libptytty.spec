Summary: OS independent and secure pty/tty and utmp/wtmp/lastlog handler
Name: libptytty
Version: 2.0
Release: alt1
License: GPL-2.0
Group: System/Libraries
Url: http://software.schmorp.de/pkg/libptytty.html

Source0: %name-%version.tar
Patch0001: 0001-Fix-LFS-on-32-bit-systems.patch

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%set_verify_elf_method strict

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

%description
Libptytty is a small library that offers pseudo-tty management in an
OS-independent way. It was created out of frustration over the many
differences of pty/tty handling in different operating systems for the
use inside "rxvt-unicode".

%package devel
Summary: OS independent and secure pty/tty and utmp/wtmp/lastlog handler
Group: Development/C
Requires: %name = %version-%release

%description devel
%name development kit

%prep
%setup -q
%autopatch -p1

%cmake
%cmake_build

%install
%cmake_install

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*
%_man3dir/*

%changelog
* Mon Oct 10 2022 Alexey Gladkov <legion@altlinux.ru> 2.0-alt1
- New version (2.0).

