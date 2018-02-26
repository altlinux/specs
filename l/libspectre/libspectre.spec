Name: libspectre
Version: 0.2.6
Release: alt2.1
Group: System/Libraries
Summary: A PostScript rendering library
License: GPLv2+
Url: http://www.freedesktop.org/wiki/Software/libspectre
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libcairo-devel libgs-devel

%description
libspectre is a small library for rendering PostScript documents.
It provides a convenient easy to use API for handling and rendering
PostScript documents.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development library and header files for
developing applications that use %name.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
    --disable-static
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS NEWS README TODO
%_libdir/%name.so.*

%files devel
%_includedir/*
%_libdir/%name.so
%_pkgconfigdir/*.pc

%changelog
* Wed Sep 28 2011 Dmitry V. Levin <ldv@altlinux.org> 0.2.6-alt2.1
- Rebuilt for debuginfo.

* Wed Oct 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.2.6-alt2
- rebuild with libgs.so.9

* Fri Jun 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.2.6-alt1
- 0.2.6

* Sun Apr 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.2.5-alt1
- 0.2.5

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Sun Oct 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.2.3-alt1
- 0.2.3

* Sun Oct 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.2.2-alt3
- fixed build with libgs-8.70

* Mon Jun 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.2.2-alt2
- fixed build with libgs-8.64

* Tue Jan 13 2009 Sergey V Turchin <zerg at altlinux dot org> 0.2.2-alt1
- new version
- remove deprecated macroses from specfile

* Mon Sep 15 2008 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt1
- new version

* Mon May 12 2008 Sergey V Turchin <zerg at altlinux dot org> 0.2.0-alt1
- initial specfile

