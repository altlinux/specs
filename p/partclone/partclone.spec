%def_enable xfs

Name: partclone
Version: 0.2.84
Release: alt2

Summary: File System Clone Utilities
License: GPLv2+
Group: System/Configuration/Hardware

Url: http://partclone.org
Source: http://download.sourceforge.net/partclone/partclone-%version.tar

# Automatically added by buildreq on Fri Dec 04 2015
# optimized out: libaal-devel libcom_err-devel libncurses-devel libntfs-3g libtinfo-devel pkg-config xz
BuildRequires: libblkid-devel libe2fs-devel libncursesw-devel libntfs-3g-devel libprogsreiserfs-devel libreiser4-devel libuuid-devel libvmfs-devel

BuildRequires: libvmfs-devel > 0.2.1-alt1
%if_enabled xfs
BuildRequires: libxfs-devel
%endif

# TODO: build with ufs (need libufs2), jfs (need fixed build of jfsutils)

%description
A set of file system clone utilities, including ext2/3/4,%{?_enable_xfs: xfs,}
reiserfs, reiser4, btrfs, ntfs, fat, vmfs, hfs+ file system.

%prep
%setup
echo '#define git_version "%version"' > src/version.h

subst 's/ -static//g' configure.ac configure
# Exclude fail-mbr from build process
subst 's/ fail-mbr//g' Makefile.in Makefile.am


%build
%autoreconf
# NB: Due to buggy configure checks --disable-somefeature options does not
# switch off configure requirement for correspondent devel packages and
# configure will fail as if --enable-somefeature was in effect.
%configure \
	--enable-btrfs \
	--enable-extfs \
	--enable-reiser4 \
	--enable-reiserfs \
	--enable-hfsp \
	--enable-fat \
	--enable-ntfs \
	--enable-vmfs \
%if_enabled xfs
	--enable-xfs \
%endif
	--enable-ncursesw
%make_build CC="gcc -I/usr/include/vmfs"

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_sbindir/*
%_man8dir/*

%changelog
* Sun Apr 24 2016 Denis Medvedev <nbr@altlinux.org> 0.2.84-alt2
- Rebuild for new ntfs-3g.

* Fri Dec 04 2015 Michael Shigorin <mike@altlinux.org> 0.2.84-alt1
- 0.2.84
- use ntfs-3g instead of libntfs
- reenabled XFS support by default
- added debian watch file
- buildreq

* Fri Dec 04 2015 Michael Shigorin <mike@altlinux.org> 0.2.58-alt3.1
- disabled XFS support by default (FTBFS against libxfs-3.1.11-alt1)

* Sat Aug 31 2013 Led <led@altlinux.ru> 0.2.58-alt3
- rebuild with libreiser4 1.0.8 (libreiser4-1.0.so.8)

* Fri Apr 12 2013 Andrey Cherepanov <cas@altlinux.org> 0.2.58-alt2
- Enable XFS support

* Thu Apr 11 2013 Andrey Cherepanov <cas@altlinux.org> 0.2.58-alt1
- 0.2.58

* Fri Mar 16 2012 Victor Forsiuk <force@altlinux.org> 0.2.45-alt1
- 0.2.45

* Fri Jan 06 2012 Victor Forsiuk <force@altlinux.org> 0.2.43-alt1
- 0.2.43

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 0.2.24-alt1
- 0.2.24

* Sat Apr 23 2011 Victor Forsiuk <force@altlinux.org> 0.2.23-alt1
- 0.2.23

* Fri Apr 22 2011 Victor Forsiuk <force@altlinux.org> 0.2.22-alt1
- 0.2.22
- Fixed build due to e2fsprogs-v1.41.12-107-gefe0b40 API change.
  Thanks to ldv@ for patch.

* Wed Jan 26 2011 Victor Forsiuk <force@altlinux.org> 0.2.17-alt1
- 0.2.17

* Fri Dec 17 2010 Victor Forsiuk <force@altlinux.org> 0.2.16-alt1
- 0.2.16

* Fri Jun 19 2009 Grigory Batalov <bga@altlinux.ru> 0.1.1-alt2
- Built without xfs due to API change.

* Thu Jun 18 2009 Grigory Batalov <bga@altlinux.ru> 0.1.1-alt1
- Built for ALT Linux.
