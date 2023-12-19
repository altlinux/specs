%def_disable snapshot
%def_disable static
%{?_enable_static:%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}}

%define _name LibRaw
%define ver_major 0.21
%define sover 23
# demosaic pack version
%define dmp_ver 0.18.8

Name: libraw
Version: %ver_major.2
Release: alt1

Summary: library for reading RAW files obtained from digital photo cameras
Group: System/Libraries
License: LGPLv2.1 and CDDL-1.0
Url: http://www.libraw.org

%if_disabled snapshot
Source: %url/data/%_name-%version.tar.gz
#Source: https://github.com/LibRaw/LibRaw/archive/%version/%_name-%version.tar.gz
%else
Vcs: https://github.com/LibRaw/LibRaw.git
Source: %_name-%version.tar
%endif
# GPLv2, GPLv3
Source1: %url/data/%_name-demosaic-pack-GPL2-%dmp_ver.tar.gz
Source2: %url/data/%_name-demosaic-pack-GPL3-%dmp_ver.tar.gz

BuildRequires: gcc-c++ libjasper-devel liblcms2-devel
BuildRequires: libjpeg-devel libgomp-devel zlib-devel

%description
LibRaw is a library for reading RAW files from digital photo cameras
(CRW/CR2, NEF, RAF, DNG, MOS, KDC, DCR, etc.; virtually all RAW formats
are supported). It pays special attention to correct retrieval of data
required for subsequent RAW conversion.
This package contains shared library.

%package samples
Group: Graphics
Summary: sample tools based on the libraw
Requires: %name = %EVR

%description samples
LibRaw is a library for reading RAW files from digital photo cameras
(CRW/CR2, NEF, RAF, DNG, MOS, KDC, DCR, etc.; virtually all RAW formats
are supported). It pays special attention to correct retrieval of data
required for subsequent RAW conversion.
This package contains samples binaries.

%package devel
Group: Development/C
Summary: library for reading RAW files
Requires: %name = %EVR

%description devel
LibRaw is a library for reading RAW files from digital photo cameras
(CRW/CR2, NEF, RAF, DNG, MOS, KDC, DCR, etc.; virtually all RAW formats
are supported). It pays special attention to correct retrieval of data
required for subsequent RAW conversion.
This package contains library headers.

%package devel-static
Group: Development/C
Summary: static library for reading RAW files
Requires: %name-devel = %EVR

%description devel-static
LibRaw is a library for reading RAW files from digital photo cameras
(CRW/CR2, NEF, RAF, DNG, MOS, KDC, DCR, etc.; virtually all RAW formats
are supported). It pays special attention to correct retrieval of data
required for subsequent RAW conversion.
This package contains static library.

%prep
%setup -n %_name-%version -a1 -a2

%build
%ifarch %e2k
# lcc 1.23.20 doesn't link a shared library against -lomp
# explicitly even if -fopenmp is there
export LIBS+="-lpthread -lomp"
%endif
%autoreconf
%configure \
    %{subst_enable static} \
    --docdir=%_datadir/doc/libraw-%version \
    --enable-jasper \
    --enable-lcms \
    --enable-jpeg \
    --enable-openmp
%nil
%make_build

%install
%makeinstall_std

%check
%make check

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
%_pkgconfigdir/libraw.pc
%_pkgconfigdir/libraw_r.pc

%if_enabled static
%files devel-static
%_libdir/libraw.a
%_libdir/libraw_r.a
%endif

%changelog
* Tue Dec 19 2023 Yuri N. Sedunov <aris@altlinux.org> 0.21.2-alt1
- 0.21.2

* Thu Feb 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.21.1-alt1
- 0.21.1

* Fri Aug 27 2021 Yuri N. Sedunov <aris@altlinux.org> 0.20.2-alt1.1
- disabled build of static libraries

* Sun Nov 01 2020 Yuri N. Sedunov <aris@altlinux.org> 0.20.2-alt1
- 0.20.2

* Mon Sep 28 2020 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Mon Oct 07 2019 Michael Shigorin <mike@altlinux.org> 0.19.5-alt1.1
- E2K: work around lack of explicit linking against libomp

* Wed Aug 21 2019 Yuri N. Sedunov <aris@altlinux.org> 0.19.5-alt1
- 0.19.5

* Tue Aug 06 2019 Yuri N. Sedunov <aris@altlinux.org> 0.19.4-alt1
- 0.19.4

* Wed Jul 03 2019 Yuri N. Sedunov <aris@altlinux.org> 0.19.3-alt1
- 0.19.3

* Mon Dec 24 2018 Yuri N. Sedunov <aris@altlinux.org> 0.19.2-alt1
- 0.19.2 (fixed CVE-2018-20363, CVE-2018-20364, CVE-2018-20365)

* Fri Nov 23 2018 Yuri N. Sedunov <aris@altlinux.org> 0.19.1-alt1
- 0.19.1

* Sat Aug 04 2018 Yuri N. Sedunov <aris@altlinux.org> 0.19.0-alt1
- 0.19.0

* Sat Jun 30 2018 Yuri N. Sedunov <aris@altlinux.org> 0.18.13-alt1
- 0.18.13

* Mon Jun 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.18.12-alt2
- rebuilt against libjasper.so.4

* Tue Jun 12 2018 Yuri N. Sedunov <aris@altlinux.org> 0.18.12-alt1
- 0.18.12 (fixed SA83507)

* Thu May 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.18.11-alt1
- 0.18.11

* Mon Feb 26 2018 Yuri N. Sedunov <aris@altlinux.org> 0.18.8-alt1
- 0.18.8

* Thu Feb 01 2018 Yuri N. Sedunov <aris@altlinux.org> 0.18.7-alt1.1
- fix for for ambiguous function call

* Sat Jan 20 2018 Yuri N. Sedunov <aris@altlinux.org> 0.18.7-alt1
- 0.18.7

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

