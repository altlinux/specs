Name: libdvdread
Version: 4.1.3
Release: alt3
Summary: A library for reading DVD-Video images
License: GPL
Group: System/Libraries
Url: http://www.mplayerhq.hu/MPlayer/releases/dvdnav/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar.bz2
Patch1: libdvdread-4.1.3-DVDFileStat.patch

BuildRequires: doxygen

%description
libdvdread provides a simple foundation for reading DVD-Video images.
This allows application designers to access some of the more advanced
features of the DVD format.
libdvdread currently uses libdl to dynamically probe for libdvdcss at
runtime.  If libdvdcss is found, then it will be used to decrypt the
encrypted sections of a DVD.

%package devel
Summary: Development environment for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files you can use to develop
applications reading DVD-video images

%prep
%setup -q
%patch1 -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS TODO README
%_libdir/*.so.*

%files devel
%_includedir/*
%_bindir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/aclocal/*.m4

%changelog
* Fri Nov 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.1.3-alt3
- rebuild

* Sun Sep 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.1.3-alt2
- applied DVDFileStat patch

* Mon Jun 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.1.3-alt1
- 4.1.3

* Sat Jan 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.9.7-alt1
- 0.9.7 release.

* Fri Apr 14 2006 LAKostis <lakostis at altlinux.ru> 0.9.5-alt1
- NMU;
- new version

* Sun Oct 03 2004 Anton Farygin <rider@altlinux.ru> 0.9.4-alt1
- new version

* Fri Oct 18 2002 Rider <rider@altlinux.ru> 0.9.3-alt2
- Russian summary
- rebuild (gcc 3.2)

* Fri Jun 14 2002 Rider <rider@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Tue Nov 08 2001 Rider <rider@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Wed Sep 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.9.1-alt2
- Specfile major cleanup (policy enforcement).

* Tue Sep 18 2001 Rider <rider@altlinux.ru> - 0.9.1-alt1
- First build for ALT Linux

* Thu Sep 6 2001 Martin NorbДck <d95mback@dtek.chalmers.se>
- Updated to version 0.9.0
* Tue Jul 03 2001 Martin NorbДck <d95mback@dtek.chalmers.se>
- initial version
