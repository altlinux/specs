# SPDX-License-Identifier: GPL-2.0-or-later
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: scrub
Version: 2.6.1
Release: alt2
Summary: Disk scrubbing program
License: GPL-2.0-or-later
Url: https://github.com/chaos/scrub/
Vcs: https://github.com/chaos/scrub.git
Group: File tools
Source: %name-%version.tar
Patch: %name-%version.patch
BuildRequires: libgcrypt-devel

%description
Scrub writes patterns on files or disk devices to make
retrieving the data more difficult.  It operates in one of three modes:
1) the special file corresponding to an entire disk is scrubbed
   and all data on it is destroyed.
2) a regular file is scrubbed and only the data in the file
   (and optionally its name in the directory entry) is destroyed.
3) a regular file is created, expanded until
   the file system is full, then scrubbed as in 2).

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%check
%make_build check

%install
%makeinstall_std
rm -rf %buildroot%_defaultdocdir/%name

%files
%doc DISCLAIMER COPYING README ChangeLog
%_bindir/scrub
%_man1dir/scrub.1*

%changelog
* Wed Jul 17 2024 Alexey Shabalin <shaba@altlinux.org> 2.6.1-alt2
- Bump release, fix update from autoimports.

* Mon Jul 15 2024 Alexey Shabalin <shaba@altlinux.org> 2.6.1-alt1
- Initial package.

