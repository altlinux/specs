Name: libisofs
Version: 1.2.0
Release: alt1

Summary: ISO9660 filesystem creation library
Url: http://libburnia.pykix.org/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
License: %gpl2plus

Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>
Group: System/Libraries

BuildRequires(pre): rpm-build-licenses

BuildRequires: zlib-devel libacl-devel libattr-devel
BuildRequires: libburn-devel

%description
libisofs is the library to pack up hard disk files and directories into a
ISO 9660 disk image. This may then be brought to CD via libburn.
libisofs is to be the foundation of our upcoming mkisofs emulation.

%package devel
Summary: Development files for libisofs
Group: System/Libraries
Requires: %name = %version

%description devel
libisofs is the library to pack up hard disk files and directories into a
ISO 9660 disk image. This may then be brought to CD via libburn.
libisofs is to be the foundation of our upcoming mkisofs emulation.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--disable-static

%make_build

%install
%makeinstall_std

%files
%_libdir/%name.so.*

%files devel
%dir %_includedir/%name
%_includedir/%name/%name.h
%_libdir/%name.so
%_pkgconfigdir/*.pc

%changelog
* Tue Mar 20 2012 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Mon Oct 31 2011 Mikhail Efremov <sem@altlinux.org> 1.1.6-alt1
- Add zlib-devel, libacl-devel, libattr-devel to BR.
- 1.1.6.

* Wed Jun 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Fri Dec 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6.40-alt1
- 0.6.40

* Thu Sep 23 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6.36-alt1
- 0.6.36

* Thu May 06 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6.32-alt1
- 0.6.32

* Mon Nov 09 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6.24-alt1
- 0.6.24

* Tue Jul 14 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6.20-alt1
- 0.6.20 

* Tue Apr 14 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6.16-alt1
- 0.6.16 

* Thu Oct 02 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6.8-alt1
- new version 

* Thu May 01 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.6.4-alt1
- new version

* Thu Mar 06 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6.2.1-alt1
- new version from upstream

* Wed Sep 19 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2.8-alt1
- new vesion
- added requires from devel to lib

* Thu Feb 08 2007  Eugene Ostapets <eostapets@altlinux.org> 0.2.4-alt0.1
- Initial build

