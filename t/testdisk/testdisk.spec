Name: testdisk
Version: 7.0
Release: alt2

Summary: Tool to check and undelete partition
License: GPLv2+
Group: System/Configuration/Hardware

Url: http://www.cgsecurity.org/wiki/TestDisk
Source: http://www.cgsecurity.org/%name-%version.tar.bz2

# manually removed: python3 ruby ruby-stdlibs
# Automatically added by buildreq on Wed May 06 2015
# optimized out: fontconfig gnu-config libcloog-isl4 libcom_err-devel libncurses-devel libntfs-3g libqt4-core libqt4-gui libstdc++-devel libtinfo-devel pkg-config python3-base zlib-devel
BuildRequires: gcc-c++ glibc-devel libdb4-devel libe2fs-devel libewf-devel libjpeg-devel libncursesw-devel libntfs-3g-devel libossp-uuid-devel libprogsreiserfs-devel libqt4-devel libuuid-devel

Provides: testdisk-doc = %name-%version
Obsoletes: testdisk-doc < 6.14

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

See online documentation at:
http://www.cgsecurity.org/wiki/TestDisk

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

See online documentation at:
http://www.cgsecurity.org/wiki/PhotoRec

%package -n qphotorec
Summary: GUI for PhotoRec, a data recovery software
Group: File tools

%description -n qphotorec
QPhotoRec is file data recovery GUI software designed to recover lost files
including video, documents and archives from Hard Disks and CDRom and lost
pictures (thus, its 'Photo Recovery' name) from digital camera memory.

See online documentation at:
http://www.cgsecurity.org/wiki/PhotoRec

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
rm -rf %buildroot%_mandir/zh_CN/

%files
%_bindir/testdisk
%_bindir/fidentify
%_man8dir/testdisk*
%_man8dir/fidentify*
%doc %_docdir/testdisk/

%files -n photorec
%_bindir/photorec
%_man8dir/photorec*

%files -n qphotorec
%_bindir/qphotorec
%_desktopdir/qphotorec.desktop
%_iconsdir/hicolor/48x48/apps/qphotorec.png
%_iconsdir//hicolor/scalable/apps/qphotorec.svg

%_man8dir/qphotorec*

%changelog
* Sun Apr 24 2016 Denis Medvedev <nbr@altlinux.org> 7.0-alt2
- Rebuild for sisyphus.

* Wed May 06 2015 Vitaly Lipatov <lav@altlinux.ru> 7.0-alt1
- new version 7.0 (with rpmrb script)
- add qphotorec subpackage

* Tue Nov 05 2013 Michael Shigorin <mike@altlinux.org> 6.14-alt2
- added missing P:/O: for testdisk-doc subpackage, sorry

* Fri Nov 01 2013 Michael Shigorin <mike@altlinux.org> 6.14-alt1
- 6.14
- dropped doc subpackage (it's online, links moved to %%description)

* Tue Jan 22 2013 Michael Shigorin <mike@altlinux.org> 6.13-alt1.3
- rebuilt with libntfs-3g.so.84

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.13-alt1.2
- Rebuilt with libewf 20120813

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
