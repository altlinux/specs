Name: libdvdcss
Version: 1.2.10
Release: alt2

Summary: A portable abstraction library for DVD decryption
License: GPL
Group: System/Libraries
Url: http://www.videolan.org/libdvdcss

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar.bz2

Patch0: %name-1.2.6-alt-more_headrs_makefile.patch
Patch1: libdvdcss-1.2.10-alt-tmpdir.patch
Patch2: libdvdcss-1.2.10-alt-version-script.patch

BuildRequires: doxygen

%description
This is a portable abstraction library for DVD decryption.

libdvdcss is part of the VideoLAN project, a full MPEG2 client/server
solution. The VideoLAN Client can also be used as a standalone program
to play MPEG2 streams from a hard disk or a DVD.

%package devel
Summary: Development environment for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files required for building
%name-based software.

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure \
    --disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS NEWS README
%_libdir/*.so.*

%files devel
%doc doc/html
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Fri Nov 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.10-alt2
- rebuild

* Sun Dec 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.10-alt1
- 1.2.10

* Mon May 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.2.9-alt1
- 1.2.9
- updated build dependencies

* Thu Nov 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2.8-alt1
- new version.
- don't package .la files.

* Thu Apr 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2.6-alt2
- More headers for MPlayer build.

* Wed Mar 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Tue Feb 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Sat Nov 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Fri Nov 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Mon Sep 16 2002 Rider <rider@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Mon Jun 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt1
- 1.2.1 

* Sun May 26 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.0-alt1
- 1.2.0  

* Wed Sep 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.0.3-alt2
- Specfile major cleanup (policy enforcement).

* Tue Sep 17 2001 Rider <rider@altlinux.ru> 0.0.3-alt1
- 0.0.3
- devel, devel-static package

* Thu Sep 6 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- initial version
