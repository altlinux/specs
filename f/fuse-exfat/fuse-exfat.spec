Name: fuse-exfat
Summary: Free exFAT file system implementation
Version: 0.9.7
Release: alt1
License: GPLv3+
Group: System/Kernel and hardware
URL: http://code.google.com/p/exfat/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source0: http://exfat.googlecode.com/files/%name-%version.tar.gz
Patch0: fuse-exfat-0.9.4-alt-getopt.patch

BuildRequires: libfuse-devel python-modules-email scons

%description
This driver is the first free exFAT file system implementation with write
support. exFAT is a simple file system created by Microsoft. It is intended
to replace FAT32 removing some of it's limitations. exFAT is a standard FS
for SDXC memory cards.

%prep
%setup -q
%patch0 -p1

%build
scons

%install
install -pD -m755 fuse/mount.exfat-fuse %buildroot/sbin/mount.exfat-fuse
ln -s mount.exfat-fuse %buildroot/sbin/mount.exfat
install -pD -m644 fuse/mount.exfat-fuse.8 %buildroot%_man8dir/mount.exfat-fuse.8

%files
%attr(755,root,root) /sbin/mount.exfat-fuse
/sbin/mount.exfat
%_man8dir/*.8*

%changelog
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
