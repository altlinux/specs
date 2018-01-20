%def_disable static
%define rname lcms2

Name: lib%rname
Version: 2.9
Release: alt1

Summary: Little cms color engine, version 2
License: %mit
Group: System/Libraries
Url: http://www.littlecms.com

# VCS: https://github.com/mm2/Little-CMS.git
#Source: http://downloads.sourceforge.net/lcms/%rname-%version.tar.gz
Source: %rname-%version.tar
Patch: %rname-2.5-alt-link.patch

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Sat Nov 06 2010
BuildRequires: gcc-c++ libjpeg-devel libtiff-devel zlib-devel

%package devel
Summary: LCMS 2 development environment
Group: Development/C
Requires: %name = %version-%release

%if_enabled static
%package devel-static
Summary: Static LCMS 2 library
Group: Development/C
Requires: %name-devel = %version-%release
%endif

%package -n lcms2-utils
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
applications which requires the LCMS 2 library.

%if_enabled static
%description devel-static
This is a CMM engine to deal with color management stuff.

This package is only needed if you plan to develop or compile
statically linked applications which requires the LCMS 2 library.
%endif

%description -n lcms2-utils
This is a CMM engine to deal with color management stuff.

This package contains various %name-based utilities

%prep
%setup -n %rname-%version
%patch

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%autoreconf
%configure \
	%{subst_enable static} \
	--program-suffix=2
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*
%doc AUTHORS README* COPYING

%files -n lcms2-utils
%_bindir/*
%_man1dir/*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Wed Nov 08 2017 Yuri N. Sedunov <aris@altlinux.org> 2.9-alt1
- 2.9

* Fri Aug 19 2016 Yuri N. Sedunov <aris@altlinux.org> 2.8-alt1
- 2.8

* Fri Apr 10 2015 Yuri N. Sedunov <aris@altlinux.org> 2.7-alt1
- 2.7

* Wed May 07 2014 Yuri N. Sedunov <aris@altlinux.org> 2.6-alt1
- 2.6

* Sun Sep 01 2013 Yuri N. Sedunov <aris@altlinux.org> 2.5-alt1
- 2.5 release

* Tue Jun 04 2013 Yuri N. Sedunov <aris@altlinux.org> 2.5rc1-alt0.1
- 2.5rc1

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.2
- Rebuilt with libtiff5

* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.1
- Fixed build

* Mon Jun 20 2011 Yuriy Shirokov <yushi@altlinux.org> 2.2-alt1
- new version 2.2

* Sun Dec 19 2010 Yuriy Shirokov <yushi@altlinux.org> 2.1-alt1
- new version 2.1

* Sat Dec 18 2010 Yuriy Shirokov <yushi@altlinux.org> 2.0a-alt4
- COPYING is packaged now due to MIT license specifics

* Sun Nov 07 2010 Yuiry Al. Shirokov <yushi@altlinux.org> 2.0a-alt3
- %if_enabled for devel-static

* Sun Nov 07 2010 Yuiry Al. Shirokov <yushi@altlinux.org> 2.0a-alt2
- spec cleanup

* Tue Nov 02 2010 Yuiry Al. Shirokov <yushi@altlinux.org> 2.0a-alt1
- new major version (and new package)
- spec simplified

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

* Sun Jan 14 2001 Giuseppe Ghib`o <ghibo@mandrakesoft.com> 1.06-2mdk
- reverted %%make to make.

* Tue Dec 26 2000 Giuseppe Ghib`o <ghibo@mandrakesoft.com> 1.06-1mdk
- initial release.
