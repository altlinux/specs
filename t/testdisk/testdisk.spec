Name: testdisk
Version: 6.13
Release: alt1.1

Summary: Tool to check and undelete partition
License: GPLv2+
Group: System/Configuration/Hardware

Url: http://www.cgsecurity.org/wiki/TestDisk
Source: http://www.cgsecurity.org/%name-%version.tar.bz2

# Automatically added by buildreq on Thu May 12 2011
# optimized out: libcom_err-devel libncurses-devel libntfs-3g libtinfo-devel pkg-config
BuildRequires: gcc-c++ glibc-devel libe2fs-devel libewf-devel libjpeg-devel libncursesw-devel libntfs-3g-devel libprogsreiserfs-devel libssl-devel libuuid-devel zlib-devel

%description
Tool to check and undelete partition. Works with the following
partitions:
 - BeFS ( BeOS )
 - BSD disklabel ( FreeBSD/OpenBSD/NetBSD )
 - CramFS (Compressed File System)
 - DOS/Windows FAT12, FAT16 and FAT32
 - HFS, Hierarchical File System
 - JFS, IBM's Journaled File System
 - Linux Ext2 and Ext3
 - Linux Raid
 - Linux Swap (versions 1 and 2)
 - LVM and LVM2, Linux Logical Volume Manager
 - Netware NSS
 - NTFS ( Windows NT/2K/XP/2003 )
 - ReiserFS 3.5 and 3.6
 - UFS (Sun/BSD/...)
 - XFS, SGI's Journaled File System

%package -n photorec
Summary: Data recovery software
Group: File tools

%description -n photorec
PhotoRec is file data recovery software designed to recover lost files
including video, documents and archives from Hard Disks and CDRom and lost
pictures (thus, its 'Photo Recovery' name) from digital camera memory.

PhotoRec ignores the filesystem and goes after the underlying data, so it
will still work even if your media's filesystem has been severely damaged
or re-formatted.

%package doc
Summary: TestDisk & PhotoRec documentation
Group: Documentation
Requires: testdisk = %version-%release

BuildArch: noarch

%description doc
Tool to check and undelete partition. Works with FAT12, FAT16, FAT32,
NTFS, EXT2, EXT3, BeFS, CramFS, HFS, JFS, Linux Raid, Linux Swap,
LVM, LVM2, NSS, ReiserFS, UFS, XFS

This package contains testdisk & photorec documentation.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/testdisk
%_bindir/fidentify
%_man8dir/testdisk*
%_man8dir/fidentify*
%exclude %_docdir/testdisk-%version

%files -n photorec
%_bindir/photorec
%_man8dir/photorec*

%files doc
%doc doc/*

%changelog
* Mon Jan 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 6.13-alt1.1
- rebuild with libntfs-3g.so.83

* Sun Nov 27 2011 Victor Forsiuk <force@altlinux.org> 6.13-alt1
- 6.13

* Thu May 12 2011 Vitaly Lipatov <lav@altlinux.ru> 6.12-alt1
- new version 6.12 (with rpmrb script)
- update buildreqs
- upstream moved binaries to /usr/bin

* Thu Mar 04 2010 Victor Forsiuk <force@altlinux.org> 6.11.3-alt1
- 6.11.3
- Build with ncursesw, libewf, libprogsreiserfs.
- Split big documentation to own subpackage.
- Package photorec separately (should be easier to find it in repo now :).

* Fri Feb 15 2008 Vitaly Lipatov <lav@altlinux.ru> 6.9-alt2
- release

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 6.9-alt1beta
- beta version 6.9

* Tue Nov 13 2007 Vitaly Lipatov <lav@altlinux.ru> 6.8-alt1
- new version 6.8 (with rpmrb script)

* Thu Jun 28 2007 Vitaly Lipatov <lav@altlinux.ru> 6.7-alt1
- new version 6.7 (with rpmrb script)

* Tue Feb 20 2007 Vitaly Lipatov <lav@altlinux.ru> 6.6-alt1
- new version 6.6 (with rpmrb script)

* Sun Oct 22 2006 Vitaly Lipatov <lav@altlinux.ru> 6.5-alt1
- new version 6.5, fix Url
- remove the patch

* Fri Jun 23 2006 Vitaly Lipatov <lav@altlinux.ru> 6.4-alt0.2
- add patch from the author

* Thu Jun 22 2006 Vitaly Lipatov <lav@altlinux.ru> 6.4-alt0.1
- new version 6.4 (with rpmrb script)

* Thu Mar 09 2006 Vitaly Lipatov <lav@altlinux.ru> 6.3-alt0.1
- new version (6.3)
- remove generic INSTALL

* Thu Dec 22 2005 Vitaly Lipatov <lav@altlinux.ru> 6.2-alt0.1
- new version

* Fri Nov 04 2005 Vitaly Lipatov <lav@altlinux.ru> 6.1-alt0.1
- new version

* Fri Aug 26 2005 Vitaly Lipatov <lav@altlinux.ru> 5.9-alt0.1
- rebuild with new libntfs
- new version 

* Fri Apr 08 2005 Vitaly Lipatov <lav@altlinux.ru> 5.7-alt0.1beta
- new version (beta)

* Sat Nov 27 2004 Vitaly Lipatov <lav@altlinux.ru> 5.5-alt1
- new version (with new version of libntfs support)

* Mon Nov 08 2004 Vitaly Lipatov <lav@altlinux.ru> 5.4-alt1
- new version

* Sun Jun 06 2004 Vitaly Lipatov <lav@altlinux.ru> 5.3-alt1
- all featured new version

* Sun Feb 22 2004 Vitaly Lipatov <lav@altlinux.ru> 5.1-alt0.1
- first build for Sisyphus (without reiserfs and ntfs detalizing)
