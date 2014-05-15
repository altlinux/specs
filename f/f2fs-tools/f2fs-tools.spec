%def_enable shared
%def_disable static

%define fsname f2fs
Name: %fsname-tools
Version: 1.3.0
Release: alt8
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

BuildRequires: libuuid-devel

%description
Tools for Flash-Friendly File System (F2FS).
Currently, the tools include mkfs.%fsname, fsck.%fsname and dump.%fsname.


%prep
%setup -q
%patch -p1


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


%files
%doc AUTHORS
%_sbindir/*
%_man8dir/*
%if_enabled shared
%_libdir/*.so.*
%exclude %_libdir/*.so
%else
%exclude %_libdir
%endif


%changelog
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
