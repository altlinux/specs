Name: libisofs
Version: 1.4.9
Release: alt0.1

Summary: ISO9660 filesystem creation library
License: %gpl2plus
Group: System/Libraries
#Url: http://libburnia-project.org
Url: https://dev.lovelyhq.com/libburnia/web/wikis/Libisofs
Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>

# VCS: https://dev.lovelyhq.com/libburnia/libisofs.git
Source: %name-%version.tar
#Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: zlib-devel libacl-devel libattr-devel
BuildRequires: libburn-devel >= %version

%description
libisofs is the library to pack up hard disk files and directories
into an ISO 9660 disk image. This may then be brought to CD via libburn.
libisofs is to be the foundation of our upcoming mkisofs emulation.

%package devel
Summary: Development files for libisofs
Group: System/Libraries
Requires: %name = %version

%description devel
libisofs is the library to pack up hard disk files and directories
into an ISO 9660 disk image. This may then be brought to CD via libburn.
libisofs is to be the foundation of our upcoming mkisofs emulation.

%prep
%setup
#%%patch -p1

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
%doc README ChangeLog

%changelog
* Fri Feb 09 2018 Yuri N. Sedunov <aris@altlinux.org> 1.4.9-alt0.1
- updated to 1.4.8-12-ga936409

* Fri Dec 20 2013 Michael Shigorin <mike@altlinux.org> 1.3.4-alt1
- 1.3.4
- updated Url:

* Sun Feb 24 2013 Michael Shigorin <mike@altlinux.org> 1.2.6-alt1
- 1.2.6

* Wed Nov 07 2012 Michael Shigorin <mike@altlinux.org> 1.2.4-alt2
- added temporary patch off upstream revision 1044 (MBR tweak)
- clarified libburn-devel build dependency as versioned
- minor description readability fixup

* Wed Nov 07 2012 Michael Shigorin <mike@altlinux.org> 1.2.4-alt1
- 1.2.4

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

