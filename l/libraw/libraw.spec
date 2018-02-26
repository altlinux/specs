Name: libraw
Version: 0.14.6
Release: alt1

Summary: library for reading RAW files obtained from digital photo cameras 
Group: System/Libraries
License: CDDL LGPL LibRaw

Url: http://www.libraw.org
Source: %name-%version.tar

BuildRequires: gcc-c++ libjasper-devel liblcms2-devel

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
%setup -q

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

