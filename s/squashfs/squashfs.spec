Name: squashfs
Version: 4.2
Release: alt1

Summary: squashfs support
License: GPL
Group: System/Kernel and hardware
Url: http://squashfs.sourceforge.net

Source0: %name%version.tar

BuildRequires: zlib-devel liblzma-devel liblzo2-devel

%description
Squashfs is a compressed read-only filesystem for Linux. Squashfs is
intended for general read-only filesystem use, for archival use
(i.e. in cases where a .tar.gz file may be used), and in constrained
block device/memory systems (e.g. embedded systems) where low overhead
is needed. The filesystem is currently stable, and has been tested on
PowerPC, i586, Sparc and ARM architectures.

%package -n squashfsprogs
Summary: Utilities to operate w/ squashfs
Group: System/Kernel and hardware
%description -n squashfsprogs
Squashfs is a compressed read-only filesystem for Linux. Squashfs is
intended for general read-only filesystem use, for archival use
(i.e. in cases where a .tar.gz file may be used), and in constrained
block device/memory systems (e.g. embedded systems) where low overhead
is needed. The filesystem is currently stable, and has been tested on
PowerPC, i586, Sparc and ARM architectures.

This package includes utilities to operate w/ squashfs.
Currently it includes mksquashfs and unsquashfs tools

%prep
%setup -q -n %name%version

%build
pushd squashfs-tools
%make_build XZ_SUPPORT=1 LZO_SUPPORT=1 COMP_DEFAULT=xz
popd


%install
%__mkdir_p %buildroot/sbin %buildroot/%_bindir
%__install -m 0755 squashfs-tools/mksquashfs %buildroot/sbin/
%__install -m 0755 squashfs-tools/unsquashfs %buildroot/%_bindir
ln -sf mksquashfs %buildroot/sbin/mkfs.squashfs
ln -sf ../../sbin/mksquashfs %buildroot%_bindir/mksquashfs

%files -n squashfsprogs
%doc ACKNOWLEDGEMENTS README CHANGES
/sbin/*
%_bindir/*

%changelog
* Fri Apr 01 2011 Anton Farygin <rider@altlinux.ru> 4.2-alt1
- new version
- patch0 removed (included to mainstream)

* Thu May 28 2009 Anton Farygin <rider@altlinux.ru> 4.0-alt1
- new version

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
