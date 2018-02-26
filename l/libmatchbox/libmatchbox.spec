Name: libmatchbox
Version: 1.9
Release: alt2.2
Summary: Libraries for the Matchbox Desktop
License: LGPLv2+
Group: System/Libraries
Url: http://projects.o-hand.com/matchbox/
Packager: Sugar Development Team <sugar@packages.altlinux.org>

%def_disable static

Source: http://matchbox-project.org/sources/%name/%version/%name-%version.tar.bz2
Patch: libmatchbox-1.9-alt-DSO.patch

BuildPreReq: pkg-config
BuildPreReq: libXext-devel
BuildPreReq: libpango-devel
BuildPreReq: libpng-devel
BuildPreReq: libjpeg-devel

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

%package devel
Summary: Header files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.
%endif

%prep
%setup -v
%patch -p2

%build
%configure \
	--enable-pango \
	--enable-jpeg \
	--enable-png \
	%{subst_enable static}
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt2.2
- Fixed build

* Tue Dec 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt2.1
- Rebuilt for soname set-versions

* Sat Dec 13 2008 Aleksey Lim <alsroot@altlinux.org> 1.9-alt2
- move .so to devel package

* Sun Nov 16 2008 Aleksey Lim <alsroot@altlinux.org> 1.9-alt1
- first build for ALT Linux Sisyphus
