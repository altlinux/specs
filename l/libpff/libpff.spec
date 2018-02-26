Name: libpff
Version: 20100510
Release: alt1
Summary: Library to to access the Personal Folder File (PFF) and the Offline Folder File (OFF) format. PFF is used in PAB (Personal Address Book), PST (Personal Storage Table) and OST (Offline Storage Table) files
Group: System/Libraries
License: LGPL
Source: %name-alpha-%version.tar.gz
Url: http://libpff.sourceforge.net

%description
libpff is a library to access the Personal Folder File (PFF) and the Offline Folder File (OFF) format. PFF is used in PAB (Personal Address Book), PST (Personal Storage Table) and OST (Offline Storage Table) files.

%package devel
Summary: Header files and libraries for developing applications for libpff
Group: Development/Libraries
Requires: libpff = %version-%release
Group: Development/C

%description devel
Header files and libraries for developing applications for libpff.

%package tools
Summary: Several tools for accessing Personal Folder Files (OST, PAB and PST)
Group: Applications/System
Requires: libpff = %version-%release
Group:	Office

%description tools
Several tools for accessing Personal Folder Files (OST, PAB and PST)

%prep
%setup -q

%build
%configure
#--prefix=/usr --libdir=%_libdir --mandir=%_mandir
%make_build

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%doc AUTHORS COPYING NEWS README
%_libdir/*.so.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README ChangeLog
%_libdir/*.a
%_libdir/*.so
%_libdir/pkgconfig/libpff.pc
%_includedir/*
%_man3dir/*

%files tools
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%_bindir/*
%_man1dir/*

%changelog
* Fri Jul 09 2010 Fr. Br. George <george@altlinux.ru> 20100510-alt1
- Initial build for ALT

* Sun Mar 28 2010 Joachim Metz <jbmetz@users.sourceforge.net> 20100328-1
- Email change

* Sat Aug 29 2009 Joachim Metz <forensics@hoffmannbv.nl> 20090829-1
- Fix for empty requires and build requires

* Thu May 21 2009 Joachim Metz <forensics@hoffmannbv.nl> 20090521-1
- Corrected typo in autoconf/make macros

* Sat Mar 21 2009 Joachim Metz <forensics@hoffmannbv.nl> 20090321-1
- Changed comment

* Sat Jan 24 2009 Joachim Metz <forensics@hoffmannbv.nl> 20090124-1
- Added support for libbfio

* Tue Dec 16 2008 Joachim Metz <forensics@hoffmannbv.nl> 20081216-1
- Changed project URL

* Sat Oct 19 2008 Joachim Metz <forensics@hoffmannbv.nl> 20081018-1
- Added pffexport and pffrecover
- Added support for libuna

* Mon Sep 1 2008 Joachim Metz <forensics@hoffmannbv.nl> 20080901-1
- Small adjustments to text
- Removed old requires and build requires

* Sun May 11 2008 Joachim Metz <forensics@hoffmannbv.nl> 20080511-1
- Initial version based on libtableau spec file

