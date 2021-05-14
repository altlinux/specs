%define _sbindir /sbin

Name: fuse-exfat
Summary: Free exFAT file system implementation
Version: 1.3.0
Release: alt2
License: GPL-3.0-or-later
Group: System/Kernel and hardware
Url: https://github.com/relan/exfat

Source: https://github.com/relan/exfat/releases/download/v%version/%name-%version.tar.gz

Requires: exfatprogs

BuildRequires: libfuse-devel

%description
This driver is the first free exFAT file system implementation with write
support. exFAT is a simple file system created by Microsoft. It is intended
to replace FAT32 removing some of it's limitations. exFAT is a standard FS
for SDXC memory cards.

%prep
%setup

%autoreconf
%configure
%make_build

%install
%makeinstall_std
ln -s mount.exfat-fuse.8 %buildroot%_man8dir/mount.exfat.8

%files
%attr(755,root,root) %_sbindir/*
%_man8dir/*.8*

%changelog
* Fri May 14 2021 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt2
- Requires exfatprogs instead exfat-utils

* Sat Mar 28 2020 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- 1.3.0
- Fixed License tag
- Update URL tag

* Sat Mar 28 2020 Artyom Bystrov <arbars@altlinux.org> 1.0.1-alt3
- Rising from kingdom of Sisyphus archive >:-)
- Fixed SConstruct "print ()" bug

* Sun Sep 01 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- separate packages to fuse-exfat end exfat-utils

* Tue Feb 26 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Tue Jan 22 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Fri Aug 17 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Tue Mar 20 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Tue Jan 24 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Fri May 27 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Sun Mar 06 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Fri Jan 14 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.3-alt2
- mount.exfat: fixed options parse

* Sat Jan 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.3-alt1
- initial release
