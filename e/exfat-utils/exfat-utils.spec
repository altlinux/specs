Name: exfat-utils
Summary: Utilities for exFAT file system
Version: 1.0.1
Release: alt1
License: GPLv3+
Group: System/Kernel and hardware
URL: http://code.google.com/p/exfat/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source0: http://exfat.googlecode.com/files/%name-%version.tar.gz

Conflicts: fuse-exfat <= 1.0.1-alt1

BuildRequires: scons

%description
Utilities to manage extended file allocation table filesystem. This package
provides tools to create, check and label the filesystem.
It contains dumpexfat to dump properties of the filesystem, exfatfsck to report
errors found on a exFAT filesystem, exfatlabel to label a exFAT filesystem and
mkexfatfs to create a exFAT filesystem.

%prep
%setup -q

%build
scons

%install
scons DESTDIR=%buildroot/sbin/ install
mkdir -p %buildroot%_man8dir
find -name \*.8 -exec install -m644 {} %buildroot%_man8dir/ \;
ln -s mkexfatfs.8 %buildroot%_man8dir/mkfs.exfat.8
ln -s exfatfsck.8 %buildroot%_man8dir/fsck.exfat.8

%files
%attr(755,root,root) /sbin/*
%_man8dir/*.8*

%changelog
* Sun Sep 01 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

