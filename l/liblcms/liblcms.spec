%define rname lcms
%define major 1
%define minor 19
%define beta %nil

Name: lib%rname
Version: %major.%minor
Release: alt4

Summary: Little cms color engine
License: LGPL
Group: System/Libraries
Url: http://www.littlecms.com

Provides: %rname = %version
Obsoletes: %rname < %version


Source: %rname-%version.tar.gz
Source1: %rname-compat.map
Source2: %rname-compat.lds
Patch1: liblcms-1.19-alt-fix-linking.patch

# Automatically added by buildreq on Tue Feb 15 2011
BuildRequires: libjpeg-devel libtiff-devel zlib-devel


%package devel
Summary: LCMS development environment
Group: Development/C
Requires: %name = %version-%release
Provides: lcms-devel = %version
Obsoletes: lcms-devel < %version

%package devel-static
Summary: Static LCMS library
Group: Development/C
Requires: %name-devel = %version-%release

%package -n lcms-utils
Summary: Various %name-based utilities
Group: Graphics
Requires: %name = %version-%release

%description
This is a CMM engine to deal with color management stuff.

This package contains the library needed to run programs dynamically
linked with %name.

%description devel
This is a CMM engine to deal with color management stuff.

This package is only needed if you plan to develop or compile
applications which requires the LCMS library.

%description devel-static
This is a CMM engine to deal with color management stuff.

This package is only needed if you plan to develop or compile
statically linked applications which requires the LCMS library.

%description -n lcms-utils
This is a CMM engine to deal with color management stuff.

This package contains various %name-based utilities

%prep
%setup -q -n %rname-%version
%patch1 -p1
sed -i "s|^LIBRARY_CURRENT=.*$|LIBRARY_CURRENT=%major|" configure.ac
sed -i "s|^LIBRARY_REVISION=.*$|LIBRARY_REVISION=%minor|" configure.ac
find . -type f -exec chmod -x {} ';'
chmod a+x ./configure
r=$(echo -e \\r)
sed -i "s/$r//g;s/^AC_PROG_CXX//;s,python/Makefile,," configure.ac
sed -i "s/ python / /" Makefile.am
autoreconf -fisv

%build
%configure --without-python --includedir=%_includedir/lcms

# SMP-incompatible
%make -C src LDFLAGS='-Wl,--version-script=%_sourcedir/%rname-compat.map -Wl,%_sourcedir/%rname-compat.lds'
%make

%install
#makeinstall includedir=%buildroot/%_includedir/lcms
%make install DESTDIR=%buildroot

pushd %buildroot/%_includedir/lcms
for f in *
do
    ln -s lcms/$f ../$f
done
popd


%files
%doc AUTHORS NEWS README*
%_libdir/*.so.*


%files -n lcms-utils
%_bindir/*
%_man1dir/*

%files devel
%_libdir/*.so
%_libdir/pkgconfig/*
%_includedir/*

%files devel-static
%_libdir/*.a

%changelog
* Thu Jun 14 2012 Sergey V Turchin <zerg@altlinux.org> 1.19-alt4
- fix to build with gcc-4.6

* Tue Feb 15 2011 Alexey Tourbin <at@altlinux.ru> 1.19-alt3
- rebuilt for debuginfo
- disabled symbol versioning

* Thu Oct 21 2010 Sergey V Turchin <zerg@altlinux.org> 1.19-alt2
- rebuilt

* Thu Dec 24 2009 Sergey V Turchin <zerg@altlinux.org> 1.19-alt0.M51.1
- built for M51

* Mon Dec 21 2009 Sergey V Turchin <zerg@altlinux.org> 1.19-alt1
- new version
- remove ldconfig from %%post

* Wed May 13 2009 Sergey V Turchin <zerg@altlinux.org> 1.18-alt0.M40.1
- built for M40

* Wed May 13 2009 Sergey V Turchin <zerg@altlinux.org> 1.18-alt0.M41.1
- built for M41

* Wed May 13 2009 Sergey V Turchin <zerg@altlinux.org> 1.18-alt0.M50.1
- built for M50

* Tue May 12 2009 Sergey V Turchin <zerg@altlinux.org> 1.18-alt1
- 1.18a
- fixes CVE-2009-0793

* Fri Mar 20 2009 Sergey V Turchin <zerg@altlinux.org> 1.18-alt0.1
- 1.18 beta1
- fixes CVE-2009-0581, CVE-2009-0723, CVE-2009-0733

* Sat Aug 02 2008 Sergey V Turchin <zerg at altlinux dot org> 1.17-alt4
- add patch for bigendian define

* Tue Jan 22 2008 Sergey V Turchin <zerg at altlinux dot org> 1.17-alt3
- add symlinks for .h files to /usr/include/

* Wed Dec 19 2007 Sergey V Turchin <zerg at altlinux dot org> 1.17-alt2
- add version script to library

* Thu Nov 22 2007 Sergey V Turchin <zerg at altlinux dot org> 1.17-alt1
- new version

* Wed Jun 27 2007 Sergey V Turchin <zerg at altlinux dot org> 1.16-alt2
- remove -momit-leaf-frame-pointer compilation flag

* Tue Mar 13 2007 Sergey V Turchin <zerg at altlinux dot org> 1.16-alt1
- new version

* Wed Oct 18 2006 Sergey V Turchin <zerg at altlinux dot org> 1.15-alt1
- 1.15

* Wed Dec 29 2004 Stanislav Ievlev <inger@altlinux.org> 1.14-alt1
- 1.14

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.11-alt2.1.1
- Rebuilt with libtiff.so.4.

* Tue Jan 06 2004 Stanislav Ievlev <inger@altlinux.org> 1.11-alt2.1
- rebuild again

* Mon Jan 05 2004 Stanislav Ievlev <inger@altlinux.org> 1.11-alt2
- fix building with gcc3.3

* Fri Dec 19 2003 Stanislav Ievlev <inger@altlinux.org> 1.11-alt1
- 1.11
- new utils package

* Wed Sep 04 2002 Stanislav Ievlev <inger@altlinux.ru> 1.09-alt1
- 1.09
- build with gcc3

* Thu Feb 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.08-alt1
- 1.08

* Mon Sep 24 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.07-alt1
- 1.07
- Moved static library to devel-static subpackage.

* Tue Feb 06 2001 Dmitry V. Levin <ldv@fandra.org> 1.06-ipl2mdk
- RE adaptions.

* Sun Jan 14 2001 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.06-2mdk
- reverted %%make to make.

* Tue Dec 26 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.06-1mdk
- initial release.
