%def_enable shared
%def_disable static

%define fsname f2fs
Name: %fsname-tools
Version: 1.7.0
Release: alt1
Summary: Tools for Flash-Friendly File System (F2FS)
License: GPLv2
Group: System/Kernel and hardware
URL: http://sourceforge.net/projects/%name
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Provides: %fsname-utils = %version-%release
Provides: mkfs.%fsname = %version-%release
Provides: fsck.%fsname = %version-%release
Provides: dump.%fsname = %version-%release

BuildRequires: libuuid-devel libselinux-devel

%description
NAND flash memory-based storage devices, such as SSD, and SD cards,
have been widely being used for ranging from mobile to server systems.
Since they are known to have different characteristics from the
conventional rotational disks,a file system, an upper layer to
the storage device, should adapt to the changes
from the sketch.

F2FS is a new file system carefully designed for the
NAND flash memory-based storage devices.
We chose a log structure file system approach,
but we tried to adapt it to the new form of storage.
Also we remedy some known issues of the very old log
structured file system, such as snowball effect
of wandering tree and high cleaning overhead.

Because a NAND-based storage device shows different characteristics
according to its internal geometry or flash memory management
scheme aka FTL, we add various parameters not only for configuring
on-disk layout, but also for selecting allocation
and cleaning algorithms.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the libraries needed to develop applications
that use %name


%prep
%setup -q
%patch -p1
sed -i 's/AC_PROG_LIBTOOL/LT_INIT/' configure.ac


%build
%autoreconf
%configure \
%if_enabled shared
	--disable-static --enable-shared \
%else
	--enable-static --disable-shared \
%endif
	--with-gnu-ld
%make_build


%install
%makeinstall_std
mkdir -m 755 -p %buildroot%_includedir
install -m 644 include/f2fs_fs.h %buildroot%_includedir
install -m 644 mkfs/f2fs_format_utils.h %buildroot%_includedir


%files
%doc COPYING AUTHORS ChangeLog
%_sbindir/*
%_man8dir/*
%if_enabled shared
%_libdir/*.so.*
%else
%exclude %_libdir
%endif

%files devel
%_includedir/*.h
%if_enabled shared
%_libdir/*.so
%endif


%changelog
* Wed Nov 23 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1.7.0-alt1
- Update to latest release

* Sun Jun 15 2014 Led <led@altlinux.ru> 1.3.0-alt11
- upstream updates

* Thu Jun 12 2014 Led <led@altlinux.ru> 1.3.0-alt10
- fsck.f2fs: large volume support
- mkfs: support passing in the number of sectors to use

* Wed May 21 2014 Led <led@altlinux.ru> 1.3.0-alt9
- mkfs.f2fs, fsck.f2fs: large volume support

* Thu May 15 2014 Led <led@altlinux.ru> 1.3.0-alt8
- upstream fixes

* Fri May 09 2014 Led <led@altlinux.ru> 1.3.0-alt7
- upstream fixes

* Sat Apr 26 2014 Led <led@altlinux.ru> 1.3.0-alt6
- upstream updates

* Fri Apr 04 2014 Led <led@altlinux.ru> 1.3.0-alt5
- mkfs: fix wrong extension count

* Sun Mar 02 2014 Led <led@altlinux.ru> 1.3.0-alt4
- mkfs: support large directory

* Sun Feb 16 2014 Led <led@altlinux.ru> 1.3.0-alt3
- f2fstat: add nat caches and free nids

* Fri Feb 07 2014 Led <led@altlinux.ru> 1.3.0-alt2
- f2fstat: add memory information used by f2fs

* Thu Feb 06 2014 Led <led@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Sat Feb 01 2014 Led <led@altlinux.ru> 1.2.0-alt5
- mkfs: fixed the wrong nat bitmap size

* Sat Jan 25 2014 Led <led@altlinux.ru> 1.2.0-alt4
- upstream updates and fixes

* Sun Jan 12 2014 Led <led@altlinux.ru> 1.2.0-alt3
- upstream fixes

* Wed Nov 20 2013 Led <led@altlinux.ru> 1.2.0-alt2
- upstream fixes

* Fri Nov 01 2013 Led <led@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Fri Oct 18 2013 Led <led@altlinux.ru> 1.1.0-alt5
- upstream updates

* Sat Aug 31 2013 Led <led@altlinux.ru> 1.1.0-alt4
- upstream updates

* Sat Jul 13 2013 Led <led@altlinux.ru> 1.1.0-alt3
- upstream updates:
  + added fsck.f2fs and dump.f2fs
- provide f2fs-utils
- link utils with shared library

* Thu Jul 04 2013 Led <led@altlinux.ru> 1.1.0-alt2
- upstream updates

* Sun Feb 10 2013 Led <led@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Fri Oct 12 2012 Led <led@altlinux.ru> 1.0.0-alt1
- initial build
