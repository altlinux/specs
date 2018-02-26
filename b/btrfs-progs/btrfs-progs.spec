Name: btrfs-progs
Version: 0.19
Release: alt3

Summary: Utilities for managing the Btrfs filesystem
License: GPLv2
Group: System/Kernel and hardware
Url: btrfs.wiki.kernel.org/
Packager: Kiriil A. Shutemov <kas@altlinux.org>

Source: %name-%version-%release.tar

BuildRequires: libacl-devel libe2fs-devel libuuid-devel zlib-devel

%description
Btrfs (B-tree FS or usually pronounced "Butter FS") is a copy-on-write
file system for Linux. It was created as a response to the ZFS filesystem,
in order to replace the ext3 file system while removing a number of its
limitations, particularly with respect to file size, total file system size
and filesystem check duration; it is also expected to implement modern
filesystem features not supported by ext3, like writable snapshots,
snapshots of snapshots, builtin RAID support, and subvolumes. In addition,
Btrfs claims a "focus on fault tolerance, repair and easy administration.

This package contains utilities for managing the Btrfs filesystem

%prep
%setup -q -n %name-%version-%release

%build
%make_build all convert

%install
%makeinstall bindir=%buildroot/sbin

%files
/sbin/*
%_man8dir/*

%changelog
* Sun Feb 20 2011 Kirill A. Shutemov <kas@altlinux.org> 0.19-alt3
- v0.19-35-g1b444cd
- Relocate binaries to /sbin

* Tue Nov 24 2009 Kirill A. Shutemov <kas@altlinux.org> 0.19-alt2
- v0.19-4-gab8fb4c
- Fix BuildRequires

* Sun Sep 06 2009 Kirill A. Shutemov <kas@altlinux.org> 0.19-alt1
- v0.19-1-g4f89b6e

* Thu Jan 29 2009 Kirill A. Shutemov <kas@altlinux.ru> 0.18-alt1
- 0.18

* Wed Jan 21 2009 Kirill A. Shutemov <kas@altlinux.ru> 0.17-alt2
- Fixed typo in package name
- Fixed URL

* Tue Jan 13 2009 Kirill A. Shutemov <kas@altlinux.ru> 0.17-alt1
- Initial build for ALT Linux
