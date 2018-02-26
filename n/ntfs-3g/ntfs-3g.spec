Name: ntfs-3g
Version: 2012.1.15
Release: alt1
Epoch: 2
Summary: third generation Linux NTFS driver
URL: http://www.ntfs-3g.org/
Group: System/Kernel and hardware
License: GPL2
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: lib%name = %epoch:%version-%release
Provides: ntfsprogs = %epoch:%version-%release fuse-ntfs = %epoch:%version-%release
Obsoletes: ntfsprogs fuse-ntfs

Source0: %{name}_ntfsprogs-%version.tgz

BuildRequires: libattr-devel libfuse-devel libgcrypt-devel libgnutls-devel libuuid-devel

%description
The ntfs-3g driver is an open source, freely available read/write NTFS
driver, which provides safe and fast handling of the Windows XP, Windows
Server 2003, Windows 2000 and Windows Vista filesystems. Almost the full
POSIX filesystem functionality is supported, the major exceptions are
changing the file ownerships and the access rights.

This package contains utils for %name

%package -n lib%name
Summary: Shared libraries for %name
Group: System/Libraries
Provides: libntfs = %epoch:%version-%release

%description -n lib%name
The ntfs-3g driver is an open source, freely available read/write NTFS
driver, which provides safe and fast handling of the Windows XP, Windows
Server 2003, Windows 2000 and Windows Vista filesystems. Almost the full
POSIX filesystem functionality is supported, the major exceptions are
changing the file ownerships and the access rights.

This package contains shared libraries for %name

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %epoch:%version-%release
Provides: libntfs-devel = %epoch:%version-%release
Obsoletes: libntfs-devel

%description -n lib%name-devel
The ntfs-3g driver is an open source, freely available read/write NTFS
driver, which provides safe and fast handling of the Windows XP, Windows
Server 2003, Windows 2000 and Windows Vista filesystems. Almost the full
POSIX filesystem functionality is supported, the major exceptions are
changing the file ownerships and the access rights.

This package contains header files for %name

%prep
%setup -q -n %{name}_ntfsprogs-%version

%build
%autoreconf
%configure \
	--sbindir=/sbin \
	--bindir=/bin \
	--with-fuse=external \
	--enable-posix-acls \
	--enable-crypto \
	--disable-ldconfig \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

ln -sf ../bin/ntfs-3g %buildroot/sbin/mount.ntfs

mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/lib*.so; do
	t=$(readlink "$f")
	ln -sf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/lib*.so.* %buildroot/%_lib/

%files
%doc AUTHORS CREDITS ChangeLog NEWS
/sbin/*
/bin/*
%_man8dir/*

%files -n lib%name
/%_lib/lib*.so.*

%files -n lib%name-devel
%_includedir/ntfs-3g
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Jan 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:2012.1.15-alt1
- 2012.1.15

* Mon Apr 11 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:2011.4.12-alt1
- 2011.4.12

* Mon Jan 24 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:2011.1.15-alt1
- 2011.1.15

* Mon Oct 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2010.10.2-alt1
- 2010.10.2

* Mon Aug 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2010.8.8-alt1
- 2010.8.8

* Fri Jun 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2010.5.22-alt1
- 2010.5.22

* Mon May 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2010.5.16-alt1
- 2010.5.16

* Mon Mar 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2010.3.6-alt1
- 2010.3.6

* Sat Jan 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:2010.1.16-alt1
- 2010.1.16

* Tue Dec 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2009.11.14-alt2
- added /sbin/mount.ntfs

* Mon Nov 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2009.11.14-alt1
- 2009.11.14

* Sun Nov 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2009.10.5-alt0.rc
- 2009.10.5-RC

* Wed Sep 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:2009.4.4-alt2
- disabled static
- updated fdi (closes: #21458)

* Wed Apr 29 2009 Alexey Sidorov <alexsid@altlinux.ru> 2:2009.4.4-alt1
- New version

* Thu Feb 12 2009 Alexey Sidorov <alexsid@altlinux.ru> 2:2009.2.1-alt1
- New version
- Initial online recovery support

* Fri Jan 23 2009 Alexey Sidorov <alexsid@altlinux.ru> 2:2009.1.1-alt1
- New version
- Used internal fuse library
- New Version Numbering 
- Built-in, transparent UTF-8 conversion support. This solves all the problems
  with hidden and inaccessible filenames having national characters.
  The 'locale=' mount option is not used anymore for filename characterset
  conversion. Instead filenames are always converted to UTF-8.
- Other fixes

* Mon Sep 22 2008 Alexey Sidorov <alexsid@altlinux.ru> 2:1.2506-alt4
- Fixed locale setting

* Tue Sep 09 2008 Alexey Sidorov <alexsid@altlinux.ru> 2:1.2506-alt3
- Added fdi for mount by HAL (#17055)

* Thu Jun 19 2008 Alexey Sidorov <alexsid@altlinux.ru> 2:1.2506-alt2
- Fixed requires around fuse's min version (#15624)

* Wed May 07 2008 Alexey Sidorov <alexsid@altlinux.ru> 2:1.2506-alt1
- New version
- Some fixes (Upgrade is strongly recommended)

* Fri Mar 14 2008 Alexey Sidorov <alexsid@altlinux.ru> 2:1.2310-alt1
- New version

* Sun Feb 24 2008 Alexey Sidorov <alexsid@altlinux.ru> 2:1.2216-alt1
- Build with dynamically linked external FUSE library
- New version:
- New: added 'remove_hiberfile' mount option to be able to read/write
  mount hibernated volumes for recovery and troubleshooting purposes.
- Fix: unprivileged unmount didn't always work.
- Fix: setuid-root ntfs-3g had a local root exploit and other security
  problems.

* Sat Feb 02 2008 Alexey Sidorov <alexsid@altlinux.ru> 2:1.2129-alt3
- And again build with integrated FUSE library (problems with old
  fuse in sisyphus)

* Wed Jan 30 2008 Alexey Sidorov <alexsid@altlinux.ru> 2:1.2129-alt2
- Back to dynamically linked external FUSE library

* Tue Jan 29 2008 Alexey Sidorov <alexsid@altlinux.ru> 2:1.2129-alt1
- New version:
- added ntfs-3g.probe utility which probes a volume for read-only or
  read-write mountability.
- built-in FUSE support by using a 50%% stripped down, integrated FUSE
  library which is linked statically into libntfs-3g

* Mon Nov 26 2007 Alexey Sidorov <alexsid@altlinux.ru> 2:1.1120-alt1
- New version

* Mon Oct 29 2007 Alexey Sidorov <alexsid@altlinux.ru> 2:1.1030-alt2
- Fix BuildRequires

* Mon Oct 29 2007 Alexey Sidorov <alexsid@altlinux.ru> 2:1.1030-alt1
- New version
- fix: free space calculation may was wrong for >1 TB volumes. 
- fix: some faulty Thunderbird versions caused system log flooding. 
- fix: many other minor fixes.

* Thu Oct 04 2007 Alexey Sidorov <alexsid@altlinux.ru> 2:1.1004-alt1
- New version

* Thu Sep 13 2007 Alexey Sidorov <alexsid@altlinux.ru> 2:1.913-alt1
- new version
- fix: hibernation check was too rigid and mount was refused
  in read/write mode unnecessarily in some cases.
- change: free disk space calculation was highly CPU intensive
  during write activity.
- improved the performance of writing multi-GB size files,
  writing many files, concurrent write.

* Mon Aug 27 2007 Alexey Sidorov <alexsid@altlinux.ru> 2:1.826-alt1
- new version (small fixes)

* Wed Aug 15 2007 Alexey Sidorov <alexsid@altlinux.ru> 2:1.810-alt1
- new version (bugfixes)

* Tue Jul 10 2007 Alexey Sidorov <alexsid@altlinux.ru> 2:1.710-alt1
- new version (bugfixes)
- Summary in UTF8
- Description little changed according to upstream

* Wed May 16 2007 Alexey Sidorov <alexsid@altlinux.ru> 2:1.516-alt1
- new version (emergency, security fix release)

* Mon Apr 16 2007 Alexey Sidorov <alexsid@altlinux.ru> 2:1.417-alt1
- new version

* Wed Mar 28 2007 Alexey Sidorov <alexsid@altlinux.ru> 2:1.328-alt1
- new version
- remove ntfs-3g-0.20070102-BETA-alt-noldconfig.patch (fixed by upstream)

* Wed Feb 21 2007 Alexey Sidorov <alexsid@altlinux.ru> 2:1.0-alt1
- document and release version update to stable status

* Fri Feb 16 2007 Alexey Sidorov <alexsid@altlinux.ru> 1:20070207-alt1.RC1
- New packager
- 20070102-BETA -> 20070207-RC1
- support old FUSE kernel modules (#10831, fixed by upstream)

* Fri Jan 05 2007 Igor Zubkov <icesik@altlinux.org> 1:20070102-alt1.BETA
- 20070822-BETA -> 20070102-BETA :)
- add serial
- update Url

* Thu Aug 31 2006 Igor Zubkov <icesik@altlinux.org> 20070822-alt1.BETA
- 20070803-BETA -> 20070822-BETA
- headers move from /usr/include/ntfs/ to /usr/include/ntfs-3g/ by upstream

* Tue Aug 15 2006 Igor Zubkov <icesik@altlinux.org> 20070803-alt1.BETA
- 20070714-BETA -> 20070803-BETA
- convert spec to UTF-8
- add docs to main package

* Tue Jul 18 2006 Igor Zubkov <icesik@altlinux.ru> 20070714-alt3.BETA
- fix requires

* Tue Jul 18 2006 Igor Zubkov <icesik@altlinux.ru> 20070714-alt2.BETA
- fix postin/postun scripts (add ldconfig)

* Tue Jul 18 2006 Igor Zubkov <icesik@altlinux.ru> 20070714-alt1.BETA
- total spec clean up

* Mon Jul 17 2006 <hihin_cat_narod_dot_ru> 20070714-BETA
- 2006/07/14: ntfs-3g beta is released.
