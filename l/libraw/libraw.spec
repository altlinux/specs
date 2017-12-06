%define _name LibRaw

Name: libraw
Version: 0.18.6
Release: alt1

Summary: library for reading RAW files obtained from digital photo cameras
Group: System/Libraries
License: LGPLv2.1 or CDDL-1.0; GPLv2, GPLv3 - demosaic packs

Url: http://www.libraw.org

Source: %url/data/%_name-%version.tar.gz
Source1: %url/data/%_name-demosaic-pack-GPL2-%version.tar.gz
Source2: %url/data/%_name-demosaic-pack-GPL3-%version.tar.gz

BuildRequires: gcc-c++ libjasper-devel liblcms2-devel libjpeg-devel libgomp-devel

%description
LibRaw is a library for reading RAW files from digital photo cameras
(CRW/CR2, NEF, RAF, DNG, MOS, KDC, DCR, etc.; virtually all RAW formats
are supported). It pays special attention to correct retrieval of data
required for subsequent RAW conversion.
This package contains shared library.

%package samples
Group: Graphics
Summary: sample tools based on the libraw
Requires: %name = %version-%release

%description samples
LibRaw is a library for reading RAW files from digital photo cameras
(CRW/CR2, NEF, RAF, DNG, MOS, KDC, DCR, etc.; virtually all RAW formats
are supported). It pays special attention to correct retrieval of data
required for subsequent RAW conversion.
This package contains samples binaries.

%package devel
Group: Development/C
Summary: library for reading RAW files
Requires: %name = %version-%release

%description devel
LibRaw is a library for reading RAW files from digital photo cameras
(CRW/CR2, NEF, RAF, DNG, MOS, KDC, DCR, etc.; virtually all RAW formats
are supported). It pays special attention to correct retrieval of data
required for subsequent RAW conversion.
This package contains library headers.

%package devel-static
Group: Development/C
Summary: static library for reading RAW files
Requires: %name-devel = %version-%release

%description devel-static
LibRaw is a library for reading RAW files from digital photo cameras
(CRW/CR2, NEF, RAF, DNG, MOS, KDC, DCR, etc.; virtually all RAW formats
are supported). It pays special attention to correct retrieval of data
required for subsequent RAW conversion.
This package contains static library.

%prep
%setup -n %_name-%version -a1 -a2

%build
%autoreconf
%configure --docdir=%_datadir/doc/libraw-%version --enable-jasper --enable-lcms

%install
%makeinstall_std

%files
%_libdir/libraw.so.*
%_libdir/libraw_r.so.*
%_datadir/doc/libraw-%version

%files samples
%_bindir/*

%files devel
%_includedir/libraw
%_libdir/libraw.so
%_libdir/libraw_r.so
%_libdir/pkgconfig/libraw.pc
%_libdir/pkgconfig/libraw_r.pc

%files devel-static
%_libdir/libraw.a
%_libdir/libraw_r.a

%changelog
* Wed Dec 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.18.6-alt1
- 0.18.6

* Thu Sep 28 2017 Yuri N. Sedunov <aris@altlinux.org> 0.18.5-alt1
- 0.18.5

* Mon Sep 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.18.4-alt1
- 0.18.4

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 0.18.3-alt1
- 0.18.3 (fixed CVE-2017-13735)

* Mon Mar 13 2017 Yuri N. Sedunov <aris@altlinux.org> 0.18.2-alt1
- 0.18.2

* Mon Feb 13 2017 Yuri N. Sedunov <aris@altlinux.org> 0.18.1-alt1
- 0.18.1

* Thu Dec 29 2016 Yuri N. Sedunov <aris@altlinux.org> 0.18.0-alt1
- 0.18.0

* Thu May 19 2016 Yuri N. Sedunov <aris@altlinux.org> 0.17.2-alt1
- 0.17.2

* Wed Dec 02 2015 Yuri N. Sedunov <aris@altlinux.org> 0.17.1-alt1
- 0.17.1

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 0.17.0-alt1
- 0.17.0
- built with external demosaic methods distributed in separate tarballs
- updated buildreqs

* Wed Jun 10 2015 Yuri N. Sedunov <aris@altlinux.org> 0.16.2-alt1
- 0.16.2 (ALT #29741)

* Tue Jan 21 2014 Vladimir Lettiev <crux@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Jun 04 2013 Vladimir Lettiev <crux@altlinux.ru> 0.15.2-alt1
- 0.15.2

* Tue Apr 09 2013 Vladimir Lettiev <crux@altlinux.ru> 0.14.7-alt1
- 0.14.7

* Wed Jun 13 2012 Vladimir Lettiev <crux@altlinux.ru> 0.14.6-alt1
- 0.14.6 (Closes: #27428)
- build shared library
- enable jasper JPEG2000 support
- enable lcms2 support

* Fri Feb 18 2011 Vladimir Lettiev <crux@altlinux.ru> 0.13.1-alt1
- New version 0.13.1

* Sun Feb 06 2011 Vladimir Lettiev <crux@altlinux.ru> 0.12.5-alt1
- New version 0.12.5

* Wed Jan 12 2011 Vladimir Lettiev <crux@altlinux.ru> 0.12.3-alt1
- New version 0.12.3
- Used autotools for building

* Fri Dec 03 2010 Vladimir Lettiev <crux@altlinux.ru> 0.11.3-alt1
- New version 0.11.3

* Mon Oct 18 2010 Vladimir Lettiev <crux@altlinux.ru> 0.10.0-alt1
- New version 0.10.0

* Tue Jul 27 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9.1-alt1
- initial build

