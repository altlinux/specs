#Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define sover 4
%define oname shapelib
%def_enable check

Name: libshape
Version: 1.6.3
Release: alt1
Summary: The Shapefile C Library and Utilities

License: LGPL-2.0-or-later OR MIT
Group: Development/C

URL: http://shapelib.maptools.org/
VCS: https://github.com/OSGeo/shapelib

# Source-url: http://download.osgeo.org/shapelib/%oname-%version.tar
Source: %oname-%version.tar

BuildRequires: gcc-c++

%description
The Shapefile C Library provides the ability to write
simple C programs for reading, writing and updating (to a
limited extent) ESRI Shapefiles, and the associated
attribute file (.dbf).

%package utils
Summary: The ShapeLib Utilities
Group: Other
Obsoletes: libshape < %EVR

%description utils
These utilities for demonstrate the capabilities of the Shapefile C Library.

%package -n libshp%sover
Summary: The Shapefile C Library
Group: System/Libraries
Conflicts: libshape < %EVR

%description -n libshp%sover
%summary.

%package devel
Summary: Development files for Shapefile C Library
Group: Development/C
Requires: libshp%sover = %EVR

%description devel
This package provides include files and libraries
for Shapefile C Library functions.

%prep
%setup -n %oname-%version

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%check
%make_build check

%files utils
%doc LICENSE-LGPL LICENSE-MIT README README.tree ChangeLog web/*.html
%doc contrib/doc/
%_bindir/*

%files devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n libshp%sover
%_libdir/libshp.so.%sover
%_libdir/libshp.so.%sover.*

%changelog
* Tue May 12 2026 Polina Poidenko <polipoki@altlinux.org> 1.6.3-alt1
- New version 1.6.3.
- Separate subpackage libshp4 in accordance with Shared Libs Policy.
- Separate subpackage libshape-utils.
- Rebuild without libproj.

* Mon Nov 24 2025 Alexander Danilov <admsasha@altlinux.org> 1.6.2-alt1
- New version 1.6.2 (Fixes: CVE-2022-0699).

* Wed Oct 19 2022 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1
- NMU: New version.
- Rebuilt with libproj 9.1.0.

* Fri Oct 04 2019 Vladislav Zavjalov <slazav@altlinux.org> 1.4.1-alt3
- fix build with libproj 6.2.0 (use DACCEPT_USE_OF_DEPRECATED_PROJ_API_H)

* Fri Feb 15 2019 Vladislav Zavjalov <slazav@altlinux.org> 1.4.1-alt2
- rebuild with libproj 5.2.0
- remove ubt macro

* Mon May 14 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.1-alt1
- Updated to upstream version 1.4.1.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.0b2-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Nov 13 2010 Vitaly Lipatov <lav@altlinux.ru> 1.3.0b2-alt1
- initial build for ALT Linux Sisyphus

* Wed May 19 2010 Lucian Langa <cooly@gnome.eu.org> - 1.3.0b2-6
- update to latest upstream beta

* Tue Mar 09 2010 Lucian Langa <cooly@gnome.eu.org> - 1.3.0b1-5
- update to latest upstream version

* Fri Feb 19 2010 Lucian Langa <cooly@gnome.eu.org> - 1.2.10-2.20100216cvs
- update patch0-3 fix undefined symbols

* Tue Feb 16 2010 Lucian Langa <cooly@gnome.eu.org> - 1.2.10-1.20100216cvs
- revert to latest cvs snapshot

* Thu Feb 04 2010 Lucian Langa <cooly@gnome.eu.org> - 1.3.0b1-4
- misc cleanups

* Thu Feb 04 2010 Lucian Langa <cooly@gnome.eu.org> - 1.3.0b1-3
- do not package static libfiles (#556094)

* Thu Jan 07 2010 Lucian Langa <cooly@gnome.eu.org> - 1.3.0b1-2
- fix patch2 - no not depend on gdal

* Thu Jan 07 2010 Lucian Langa <cooly@gnome.eu.org> - 1.3.0b1-1
- misc cleanups
- update BR
- fix source0
- update to latest upstream snapshot

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10-20.20060304cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10-19.20060304cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2.10-18.20060304cvs
- fix patch application

* Thu Sep  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2.10-17.20060304cvs
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.10-16.20060304cvs
- Autorebuild for GCC 4.3

* Sun Oct  21 2007 Shawn McCann <mccann0011@hotmail.com> - 1.2.10-15.20060304cvs
- Fix for bug 339931

* Sat Sep  16 2006 Shawn McCann <mccann0011@hotmail.com> - 1.2.10-12.20060304cvs
- Rebuild for FC6

* Sun Mar  5 2006 Shawn McCann <mccann0011@hotmail.com> - 1.2.10-11.20060304cvs
- Fixed a makefile bug that messed up parallel builds

* Sat Mar  4 2006 Shawn McCann <mccann0011@hotmail.com> - 1.2.10-10.20060304cvs
- Upgraded to cvs snapshot taken on March 4, 2006

* Sat Mar  4 2006 Shawn McCann <mccann0011@hotmail.com> - 1.2.10-9
- Rebuild for Fedora Extras 5

* Mon Apr 11 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.2.10-8
- Fix "invalid lvalue in assignment" for GCC4.

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Feb 13 2005 David Woodhouse <dwmw2@infradead.org> 0:1.2.10-6
- Don't hard-code endianness; just use endian.h

* Wed Dec 15 2004 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:1.2.10-5
- Patched patch and spec file according to suggestions of Michael Schwendt
- In particular, this separates the building from the installing in the rpm.

* Thu Aug 12 2004 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:1.2.10-0.fdr.4
- Moved RPM_OPT_FLAGS out of make files.
- Removed backup files from patch.
- Made sure that make was using the appropriate libdir.

* Mon Dec 22 2003 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:1.2.10-0.fdr.3
- Added url tag, changed copyright to license and changed permissions on patch file.

* Mon Dec 22 2003 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:1.2.10-0.fdr.2
- Add source URL
- Removed proj requirement as it is automatically detected.
- Added epoch to proj-devel requirement
- Fixed post and postun
- Changed group to Development/Libraries, although this appears to be only
  somewhat satisfactory.
- Removed "which make"

* Wed Nov  5 2003 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:1.2.10-0.fdr.1
- Updated to 1.2.10 release
- Major changes to spec for Fedora
- Changes to Makefile patch for Fedora
- Split off devel package
