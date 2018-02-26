%define tarname squashfs
Name: squashfs3
Version: 3.4
Release: alt2

Summary: squashfs support
License: GPL
Group: System/Kernel and hardware
Url: http://squashfs.sourceforge.net

Source0: %tarname%version.tar
Patch0: squashfs2.1-r2-permission.patch
Patch1: squashfs3.4-makefile.patch

BuildRequires: zlib-devel

%description
Squashfs is a compressed read-only filesystem for Linux. Squashfs is
intended for general read-only filesystem use, for archival use
(i.e. in cases where a .tar.gz file may be used), and in constrained
block device/memory systems (e.g. embedded systems) where low overhead
is needed. The filesystem is currently stable, and has been tested on
PowerPC, i586, Sparc and ARM architectures.

%package -n squashfsprogs3
Summary: Utilities to operate w/ squashfs
Group: System/Kernel and hardware
%description -n squashfsprogs3
Squashfs is a compressed read-only filesystem for Linux. Squashfs is
intended for general read-only filesystem use, for archival use
(i.e. in cases where a .tar.gz file may be used), and in constrained
block device/memory systems (e.g. embedded systems) where low overhead
is needed. The filesystem is currently stable, and has been tested on
PowerPC, i586, Sparc and ARM architectures.

This package includes utilities to operate w/ squashfs.
Currently it includes mksquashfs and unsquashfs tools

%prep
%setup -q -n %tarname%version
%patch0 -p1
%patch1 -p1

%build
pushd squashfs-tools
%make_build
popd


%install
%__mkdir_p %buildroot/sbin %buildroot/%_bindir
%__install -m 0755 squashfs-tools/mksquashfs %buildroot/sbin/mksquashfs3
%__install -m 0755 squashfs-tools/unsquashfs %buildroot/%_bindir/unsquashfs3
ln -sf mksquashfs3 %buildroot/sbin/mkfs.squashfs3
ln -sf ../../sbin/mksquashfs3 %buildroot%_bindir/mksquashfs3

%files -n squashfsprogs3
%doc ACKNOWLEDGEMENTS README CHANGES
/sbin/*
%_bindir/*

%changelog
* Thu May 28 2009 Anton Farygin <rider@altlinux.ru> 3.4-alt2
- build squashfs version 3 as separate package

* Tue Sep 02 2008 Anton Farygin <rider@altlinux.ru> 3.4-alt1
- new version

* Tue Aug 05 2008 Anton Farygin <rider@altlinux.ru> 3.3-alt4
- removed lzma support

* Tue Nov 06 2007 Anton Farygin <rider@altlinux.ru> 3.3-alt1
- new version

* Tue Jan 16 2007 Anton Farygin <rider@altlinux.ru> 3.2-alt2
- unsquashfs moved to %_bindir
- fixed description

* Sun Jan 14 2007 Anton Farygin <rider@altlinux.ru> 3.2-alt1
- new version
- removed kernel-feat-squashfs subpackage

* Tue Nov 07 2006 Anton Farygin <rider@altlinux.ru> 3.1-alt2.r2
- unsquashfs added to package

* Mon Oct 30 2006 Anton Farygin <rider@altlinux.ru> 3.1-alt1.r2
- updated to 3.1-r2
- removed kernel 2.4 patch
- use patch for 2.6.18 kernel

* Wed Sep 14 2005 Anton Farygin <rider@altlinux.ru> 2.2-alt1.r2
- updated to 2.2-r2
- use patch for 2.6.13 kernel

* Wed Aug 03 2005 Anton Farygin <rider@altlinux.ru> 2.2-alt1
- updated to new version

* Thu Apr 14 2005 Anton Farygin <rider@altlinux.ru> 2.1-alt2.r2
- mksquashfs: fixed target file permissions

* Wed Feb 09 2005 Anton Farygin <rider@altlinux.ru> 2.1-alt1.r2
- new version

* Thu May 20 2004 Alexey Morozov <morozov@altlinux.org> 1.3r3-alt2
- Initial build.

* Mon Mar 29 2004 Anton Farygin <rider@altlinux.ru> 1.3-alt1
- first build
