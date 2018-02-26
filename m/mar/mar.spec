Name: mar
Version: 20070301
Release: alt1

Summary: mar - Mandrake Archiver
License: GPL
Group: Development/C

Source: %name-%version.tar

BuildRequires: bzlib-devel
Provides: /usr/bin/mkmar

%description
An archiver that supports compression (through bzlib).

%prep
%setup -c

%build
make

%install
%makeinstall

%files
%_bindir/mar
%_bindir/mkmar
%_libdir/libmar.a
%_includedir/mar-extract-only.h

%changelog
* Fri Mar  2 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 20070301-alt1
- rebuilt against glibc

* Sun Dec  3 2006 L.A. Kostis <lakostis@altlinux.ru> 20050707-alt2
- mkmar:
  + Remove use of hasher internals (drop in-chroot and workdir switches).
  + Rework pcimap functions (derive some idea from mkinitrd).
  + Remove unwanted root checks.

* Thu Jul 07 2005 Anton D. Kachalov <mouse@altlinux.org> 20050707-alt1
- multilib support
- mkmar now may partially run in chroot env

* Tue Dec 14 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 20041025-alt0.4
- mkmar modified to generate pci-ids via libhw also

* Wed Nov 10 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 20041025-alt0.3
- mkmar script added

* Tue Nov  2 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 20041025-alt0.2
- added 'extract to memory' feature

* Wed Oct 27 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 20041025-alt0.1
- packaged for %distribution
