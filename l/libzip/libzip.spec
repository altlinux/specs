
%define sover 2
%define libname libzip%sover
%define utilsname libzip-utils
Name: libzip
Version: 0.10.1
Release: alt1
Summary: C library for reading, creating, and modifying zip archives

Group: System/Libraries
License: BSD
Url: http://www.nih.at/libzip/

Source0: http://www.nih.at/libzip/%name-%version.tar.bz2

BuildRequires: gcc-c++ zlib-devel

%description
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.

%package -n %utilsname
Group: System/Libraries
Summary: Zip-file processing utilities
Requires: %libname = %version-%release
Conflicts: libzip <= libzip-0.9.3-alt2
%description -n %utilsname
Zip-file processing utilities

%package -n %libname
Group: System/Libraries
Summary: C library for reading, creating, and modifying zip archives
%description -n %libname
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %libname = %version-%release
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup -q

%autoreconf


%build
%configure \
    --disable-static \
    --enable-shared \
    --includedir=%_includedir/%name

%make_build


%install
%make DESTDIR=%buildroot install


%files -n %utilsname
%doc AUTHORS NEWS README THANKS TODO
%_bindir/*
%_man1dir/*zip*

%files -n %libname
%doc AUTHORS NEWS README THANKS TODO
%_libdir/*.so.%sover
%_libdir/*.so.%sover.*

%files devel
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_libdir/%name/include
%_includedir/%name/
%_man3dir/*zip*

%changelog
* Wed Mar 21 2012 Sergey V Turchin <zerg@altlinux.org> 0.10.1-alt1
- new version
- Fixed CVE-2012-1162, CVE-2012-1163

* Mon Mar 21 2011 Sergey V Turchin <zerg@altlinux.org> 0.10-alt1
- new version

* Mon Oct 25 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt2
- rebuilt

* Thu Aug 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.3-alt1
- new version

* Mon Dec 21 2009 Sergey V Turchin <zerg@altlinux.org> 0.9-alt3
- remove ldconfig from %%post

* Mon Sep 15 2008 Sergey V Turchin <zerg at altlinux dot org> 0.9-alt2
- add versioning

* Mon Sep 15 2008 Sergey V Turchin <zerg at altlinux dot org> 0.9-alt1
- new version

* Mon Mar 24 2008 Sergey V Turchin <zerg at altlinux dot org> 0.8-alt1
- initial specfile
