Name: partclone
Version: 0.2.45
Release: alt1

Summary: File System Clone Utilities
License: GPLv2+
Group: System/Configuration/Hardware

Url: http://partclone.org
Source: http://download.sourceforge.net/partclone/partclone-%version.tar.gz
Patch1: partclone-0.2.22-alt-group_desc.patch

# Automatically added by buildreq on Sat Apr 23 2011
# optimized out: libaal-devel libcom_err-devel libgpg-error libncurses-devel libtinfo-devel pkg-config
BuildRequires: libe2fs-devel libncursesw-devel libntfs-devel libprogsreiserfs-devel libreiser4-devel libuuid-devel
BuildRequires: libvmfs-devel > 0.2.1-alt1

# TODO: build with ufs (need libufs2), jfs (need fixed build of jfsutils)

%description
A set of file system clone utilities, including ext2/3/4, %{?_enable_xfs:xfs, }reiserfs,
reiser4, btrfs, ntfs, fat, vmfs, hfs+ file system.

%prep
%setup
#%patch1 -p1

subst 's/ -static//g' configure.ac configure

%build
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
	--enable-ncursesw
%make_build CC="gcc -I/usr/include/vmfs"

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_sbindir/*
%_man8dir/*

%changelog
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
