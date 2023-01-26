# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: iotop-c
Version: 1.23
Release: alt1
Summary: A top utility for IO
License: GPL-2.0-or-later
Group: Monitoring
Url: https://github.com/Tomas-M/iotop

Source: %name-%version.tar

BuildRequires: libncursesw-devel

%description
Is your Linux server too slow or load is too high? One of the possible
causes of such symptoms may be high IO (input/output) waiting time,
which basically means that some of your processes need to read or write
to a hard drive while it is too slow and not ready yet, serving data
for some other processes.

Common practice is to use iostat -x in order to find out which
block device (hard drive) is slow, but this information is not always
helpful. It could help you much more if you knew which process reads or
writes the most data from your slow disk, so you could renice it using
ionice or even kill it.

iotop identifies processes that use high amount of input/output requests
on your machine. It is similar to the well known top utility, but instead
of showing you what consumes CPU the most, it lists processes by their
IO usage. Inspired by iotop Python script from Guillaume Chazarain,
rewritten in C by Vyacheslav Trushkin and improved by Boian Bonev so it
runs without Python at all.

%prep
%setup
sed -i '/STRIP/d' Makefile

%build
%make_build CFLAGS="%optflags %(getconf LFS_CFLAGS)" V=1

%install
%makeinstall_std
mv %buildroot%_sbindir/iotop   %buildroot%_sbindir/iotop-c
mv %buildroot%_man8dir/iotop.8 %buildroot%_mandir/man8/iotop-c.8

%files
%doc COPYING LICENSE README.md
%_sbindir/iotop-c
%_man8dir/iotop-c.*

%changelog
* Thu Jan 26 2023 Vitaly Chikunov <vt@altlinux.org> 1.23-alt1
- Update to v1.23 (2023-01-24).

* Tue Jul 12 2022 Vitaly Chikunov <vt@altlinux.org> 1.22-alt1
- Update to v1.22 (2022-07-10).

* Tue May 03 2022 Vitaly Chikunov <vt@altlinux.org> 1.21-alt1
- First import v1.21 (2022-01-27).
