Name: xfsdump
Version: 3.1.0
Release: alt1

Summary: Administrative utilities for the XFS filesystem
License: GPL
Group: System/Kernel and hardware

Url: http://xfs.org/
Source: %name-%version.tar

# Automatically added by buildreq on Wed Apr 01 2009
BuildRequires: libattr-devel libncurses-devel libuuid-devel libxfs-devel

# we need fsx_projid from struct fsxattr
BuildRequires: libxfs-devel >= 2.8.16

%description
The xfsdump package contains xfsdump, xfsrestore and a number of
other utilities for administering XFS filesystems.

xfsdump examines files in a filesystem, determines which need to be
backed up, and copies those files to a specified disk, tape or other
storage medium.  It uses XFS-specific directives for optimizing the
dump of an XFS filesystem, and also knows how to backup XFS extended
attributes.  Backups created with xfsdump are "endian safe" and can
thus be transfered between Linux machines of different architectures
and also between IRIX machines.

xfsrestore performs the inverse function of xfsdump; it can restore a
full backup of a filesystem.  Subsequent incremental backups can then
be layered on top of the full backup.  Single files and directory
subtrees may be restored from full or partial backups.

%prep
%setup

%build
%make configure
%configure
%make_build

%install
make DIST_ROOT=%buildroot install install-dev
rm -rf %buildroot%_datadir/doc/%name
%find_lang %name

%files -f %name.lang
%doc doc/CHANGES.gz doc/README.xfsdump doc/*.gif doc/xfsdump.html
/sbin/*
%_sbindir/*
%_mandir/*/*

%changelog
* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 3.1.0-alt1
- 3.1.0

* Mon Apr 18 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.5-alt1
- 3.0.5

* Tue Mar 31 2009 Grigory Batalov <bga@altlinux.ru> 3.0.0-alt1
- New upstream release.

* Wed Mar 12 2008 Grigory Batalov <bga@altlinux.ru> 2.2.48-alt1
- New upstream release.

* Fri Sep 21 2007 Grigory Batalov <bga@altlinux.ru> 2.2.46-alt1
- New upstream release (fixes CVE-2007-2654)

* Mon Dec 18 2006 Grigory Batalov <bga@altlinux.ru> 2.2.42-alt1
- New upstream release.
- .la removal patch updated.
- Resolve conflict with systemwide list_add declaration.
- Fix compile and link with libtool.
- Html description page included.
- Uuid-shared patch obsoleted.

* Sat May 15 2004 Alexander Bokovoy <ab@altlinux.ru> 2.2.17-alt1
- 2.2.17

* Thu Dec 11 2003 Alexander Bokovoy <ab@altlinux.ru> 2.2.14-alt1
- 2.2.14
- Build everything dynamically

* Tue May 20 2003 Alexander Bokovoy <ab@altlinux.ru> 2.2.6-alt1
- 2.2.6, changed maintainer
- Spec cleanup
- Updated buildrequires
- Removed obsolete patches

* Fri Dec 27 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.0.3-alt1
- 2.0.3
- Updated buildrequires

* Wed Apr 10 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.0.0-alt0.1cvs
- 2.0.0

* Wed Nov 21 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.1.7-alt1
- 1.1.7

* Wed Oct 31 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.1.3-alt2
- Rebuilt with libxfs 1.3.7

* Thu Sep 20 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.1.3-alt1
- First build for Sisyphus

* Fri Sep  7 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.1.3-1mdk
- 1.1.3.
- rework spec files and adjust requires.

* Wed May  2 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.5-1mdk
- Fist attempt based on the SGI spec.

# end of file


