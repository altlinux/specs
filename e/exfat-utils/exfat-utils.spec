%define _sbindir /sbin

Name: exfat-utils
Summary: Utilities for exFAT file system
Version: 1.3.0
Release: alt1
License: GPL-3.0-or-later
Group: System/Kernel and hardware
URL: https://github.com/relan/exfat
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source0: https://github.com/relan/exfat/releases/download/v%version/%name-%version.tar.gz

Conflicts: fuse-exfat <= 1.0.1-alt1

%description
Utilities to manage extended file allocation table filesystem. This package
provides tools to create, check and label the filesystem.
It contains dumpexfat to dump properties of the filesystem, exfatfsck to report
errors found on a exFAT filesystem, exfatlabel to label a exFAT filesystem and
mkexfatfs to create a exFAT filesystem.

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
find -name \*.8 -exec install -m644 {} %buildroot%_man8dir/ \;
ln -s mkexfatfs.8 %buildroot%_man8dir/mkfs.exfat.8
ln -s exfatfsck.8 %buildroot%_man8dir/fsck.exfat.8

%files
%attr(755,root,root) %_sbindir/*
%_man8dir/*.8*

%changelog
* Sat Mar 28 2020 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- 1.3.0
- Fixed License tag
- Update URL tag

* Sun Sep 01 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

