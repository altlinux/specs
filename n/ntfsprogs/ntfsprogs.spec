%define _unpackaged_files_terminate_build 1
%define soversion 10

Name: ntfsprogs
Version: 2.0.0
Release: alt8.1

Summary: NTFS filesystem utilities
License: GPLv2+
Group: System/Kernel and hardware

Url: http://linux-ntfs.org/
Source0: %name-%version.tar
Patch1: %name-2.0.0-alt-libgnutls-pkg-config.patch
Patch2: %name-1.13.1-pld-stdarg_h-required.patch

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

BuildPreReq: gcc-c++ libfuse-devel >= 2.6.1 libuuid-devel pkgconfig
# crypto
BuildPreReq: libgnutls-devel >= 1.4.4 libgcrypt-devel >= 1.2.2 libconfig-devel >= 1.0.1

%description
The goals of the Linux-NTFS project are to develop reliable and full
feature access to NTFS by the Linux kernel driver, and by a user space
filesystem (ntfsmount), and to provide a wide collection of NTFS
utilities (ntfsprogs) and a developer's library (libntfs) for other
GPLed programs.

This package contains the following utilities:

   mkntfs : create an NTFS file system
   ntfscat : print NTFS files and streams on the standard output
   ntfsclone : efficiently clone, image, restore or rescue an NTFS
   ntfscluster : identify files in a specified region of an NTFS volume
   ntfscmp : compare two NTFS filesystems and tell the differences
   ntfscp : copy file to an NTFS volume
   ntfsfix : fix common errors and force Windows to check NTFS
   ntfsinfo : dump a file's attributes
   ntfslabel : display/change the label on an ntfs file system
   ntfsls : list directory contents on an NTFS filesystem
   ntfsresize : resize an NTFS filesystem without data loss
   ntfsundelete : recover a deleted file from an NTFS volume

%package -n fuse-ntfs
Summary: NTFS FUSE mount module
Group: System/Kernel and hardware
Conflicts: ntfsprogs = 1.11.0-alt1
%description -n fuse-ntfs
The goals of the Linux-NTFS project are to develop reliable and full
feature access to NTFS by the Linux kernel driver, and by a user space
filesystem (ntfsmount), and to provide a wide collection of NTFS
utilities (ntfsprogs) and a developer's library (libntfs) for other
GPLed programs.

This package contains NTFS FUSE mount module and ntfsmount helper.

%package -n libntfs%soversion
Summary: NTFS filesystem libraries
Group: System/Libraries
Provides: libntfs = %version-%release
%description -n libntfs%soversion
The goals of the Linux-NTFS project are to develop reliable and full
feature access to NTFS by the Linux kernel driver, and by a user space
filesystem (ntfsmount), and to provide a wide collection of NTFS
utilities (ntfsprogs) and a developer's library (libntfs) for other
GPLed programs.

This package contains NTFS filesystem libraries.

%package -n libntfs-devel
Summary: NTFS filesystem header files
Group: Development/C
Requires: libntfs%soversion = %version-%release
%description -n libntfs-devel
The goals of the Linux-NTFS project are to develop reliable and full
feature access to NTFS by the Linux kernel driver, and by a user space
filesystem (ntfsmount), and to provide a wide collection of NTFS
utilities (ntfsprogs) and a developer's library (libntfs) for other
GPLed programs.

This package contains NTFS filesystem header files.

%prep
%setup
%patch1 -p2
%patch2 -p1
%autoreconf

%build
%configure \
	--disable-static \
	--disable-gnome-vfs

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std
rm -f doc/Makefile*
rm -f %buildroot%_includedir/ntfs/gnome-vfs*.h
rm -f %buildroot%_man8dir/libntfs-gnomevfs.*

%files
%_bindir/ntfscat
%_bindir/ntfscluster
%_bindir/ntfscmp
%_bindir/ntfsfix
%_bindir/ntfsinfo
%_bindir/ntfsls
%_sbindir/mkntfs
%_sbindir/ntfsclone
%_sbindir/ntfscp
%_sbindir/ntfslabel
%_sbindir/ntfsresize
%_sbindir/ntfsundelete
/sbin/mkfs.ntfs
%_man8dir/libntfs.*
%_man8dir/mkfs.ntfs.*
%_man8dir/mkntfs.*
%_man8dir/ntfscat.*
%_man8dir/ntfscmp.*
%_man8dir/ntfsclone.*
%_man8dir/ntfscluster.*
%_man8dir/ntfscp.*
%_man8dir/ntfsfix.*
%_man8dir/ntfsinfo.*
%_man8dir/ntfslabel.*
%_man8dir/ntfsls.*
%_man8dir/ntfsprogs.*
%_man8dir/ntfsresize.*
%_man8dir/ntfsundelete.*
%doc AUTHORS CREDITS ChangeLog NEWS README TODO.* doc/

%files -n libntfs%soversion
%_libdir/libntfs.so.*

%files -n fuse-ntfs
%_bindir/ntfsmount
/sbin/mount.fuse.ntfs
/sbin/mount.ntfs-fuse
%_man8dir/ntfsmount.*
%_man8dir/mount.fuse.ntfs.*
%_man8dir/mount.ntfs-fuse.*

%files -n libntfs-devel
%_libdir/libntfs.so
%dir %_includedir/ntfs
%_includedir/ntfs/*.h


%changelog
* Fri Feb 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt8.1
- Removed bad RPATH

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt8
- Rebuilt for soname set-versions

* Tue Nov 24 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.0-alt7
- rebuild with libconfig.so.9
- disable gnome-vfs support and remove all related parts of the specfile

* Wed Aug 26 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.0-alt6
- rebuild with libconfig.so.8

* Mon Jun 29 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.0-alt5
- use pkg-config instead of libgnutls-config
- restore G_LOCK_DEFINE(libntfs) (suggested by crux@, approved by upstream)

* Fri Jan 16 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt4.1
- rebuild with libconfig.so.6

* Wed Dec 03 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.0-alt4
- rebuild with new gnutls

* Thu Nov 20 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.0-alt3
- remove update_*/clean_* invocations

* Sat Mar 01 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.0-alt2
- remove patch for compatibility with old fuse

* Tue Oct 30 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.0-alt1.1
- rebuild with libconfig.so.2

* Mon Oct 15 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.0-alt1
- Sisyphus build
- include soname number in the library package name

* Sat Sep 29 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.0-alt0.1
- 2.0.0
- Daedalus build
- update descriptions
- add patch for fuse < 2.7 support

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.13.1-alt2.0
- Automated rebuild.

* Tue Jul 04 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.13.1-alt2
- add minor patches from PLD
- fix building without crypto enabled and without libgcrypt-devel 
  (from PLD)

* Sun Jul 02 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.13.1-alt1
- 1.13.1
- enable _unpackaged_files_terminate_build
- fix linking of libntfs-gnomevfs.so

* Thu Mar 02 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.13.0-alt1
- 1.13.0

* Wed Oct 19 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.12.1-alt2
- move /sbin/mount.ntfs-fuse symlink and ntfsmount related manpages
  to ntfsmount package

* Wed Oct 12 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.12.1-alt1
- 1.12.1

* Tue Aug 09 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.11.2-alt1
- 1.11.2
- do not ever build static libs

* Tue Aug 02 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.11.0-alt2.1
- fixed BuildRequires

* Wed Jul 27 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.11.0-alt2
- ntfsmount packaged separately (#7455)

* Wed Jul 20 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Fri Jun 24 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Sat May 21 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.9.4-alt2
- don't package doc/Makefile*

* Sat Nov 13 2004 Andrey Rahmatullin <wrar@altlinux.ru> 1.9.4-alt1
- 1.9.4
- do not package static libs
- update description
- add post(un)?_ldconfig
- change Packager:

* Fri Feb 06 2004 Michael Shigorin <mike@altlinux.ru> 1.8.4-alt1.1
- fixed gcc3.2 build request
- fixed GNOME package groups

* Thu Feb  5 2004 Alexey Morozov <morozov@altlinux.org> 1.8.4-alt1
- 1.8.4
- libntfs.a is conditionally built
  (--enable/--disable static, default is enabled)
- added libntfs-gnomevfs package
  (--enable/--disable gnome-vfs, default is enabled)
  static module library is under another condition
  (--enable/--disable static-gnome-vfs, default is disabled)

* Tue Jun 24 2003 Albert R. Valiev <darkstar@altlinux.ru> 1.7.1-alt2
- deps correction

* Fri Jun 20 2003 Albert R. Valiev <darkstar@altlinux.ru> 1.7.1-alt1
- Initial build
