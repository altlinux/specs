# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method relaxed

Name: nocache
Version: 1.2
Release: alt1
Summary: minimize caching effects
License: BSD-2-Clause
Group: Development/Other
Url: https://github.com/Feh/nocache

Source: %name-%version.tar
%{?!_without_check:%{?!_disable_check:
BuildRequires: /proc
BuildRequires: strace
}}

%description
The nocache tool tries to minimize the effect an application has on
the Linux file system cache. This is done by intercepting the open and
close system calls and calling posix_fadvise with the POSIX_FADV_DONTNEED
parameter. Because the library remembers which pages (ie., 4K-blocks of
the file) were already in file system cache when the file was opened,
these will not be marked as "don't need", because other applications
might need that, although they are not actively used (think: hot standby).

%prep
%setup

%build
%define optflags_lto %nil
%make_build CFLAGS="%optflags"

%install
%makeinstall_std PREFIX=%_prefix LIBDIR=/..%_libdir

%check
# `make test` cannot be run on tmpfs.
strace -f -o log -y -- ./nocache cp README OUTPUT
# 3146381 fadvise64(3</usr/src/RPM/BUILD/nocache-1.2/README>, 0, 0, POSIX_FADV_NOREUSE) = 0
grep 'fadvise.*/README.*POSIX_FADV_NOREUSE' log

%files
%doc COPYING README
%_bindir/nocache
%_bindir/cachedel
%_bindir/cachestats
%_libdir/nocache.so
%_man1dir/*.1*

%changelog
* Thu Mar 09 2023 Vitaly Chikunov <vt@altlinux.org> 1.2-alt1
- First import v1.2 (2022-05-01).
