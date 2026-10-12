%define oname guichan
%define abiversion 2
%define libver 0.8.1
Name: libguichan
Version: 0.8.3
Release: alt1

Summary: Guichan - small, efficient C++ GUI library designed for games

License: BSD
Group: System/Libraries

# Source-url: https://github.com/darkbitsorg/guichan/archive/v%version/%oname-%version.tar.gz
Source: %oname-%version.tar.gz

Url: https://github.com/darkbitsorg/guichan

# manually removed: gcc-g77 libg2c-devel 
# Automatically added by buildreq on Tue May 11 2010
BuildRequires: gcc-c++ libGL-devel libSDL-devel libSDL_image-devel liballegro-devel

%description
Guichan is a small, efficient C++ GUI library designed for games. It
comes with a standard set of widgets and can use several different
objects for displaying graphics and grabbing user input.

%package -n %name%abiversion
Summary: Guichan - small, efficient C++ GUI library designed for games
# the library package was renamed by soname (.so.1 -> .so.2): replace the old one
Obsoletes: %name < %EVR
Group: System/Libraries

%description -n %name%abiversion
Guichan is a small, efficient C++ GUI library designed for games. It
comes with a standard set of widgets and can use several different
objects for displaying graphics and grabbing user input.

This package contains Guichan shared libraries (core, SDL, OpenGL, Allegro).

%package devel
Summary: Header files for Guichan library
Group: Development/C
Requires: %name%abiversion = %EVR
Requires: libstdc++-devel

%description devel
Header files for Guichan library.

%prep
%setup -q -n %oname-%version
# make libguichan before extradirs
sed -i "s|SUBDIRS = widgets|SUBDIRS = widgets \.|g" src/Makefile.am

%build
%autoreconf
export LDFLAGS="-L%_x11libdir"
%configure --disable-static \
	--enable-opengl \
	--enable-allegro

%make_build

%install
%make_install install DESTDIR=%buildroot

%files -n %name%abiversion
%doc AUTHORS ChangeLog NEWS README TODO
%_libdir/libguichan-%libver.so.%abiversion
%_libdir/libguichan-%libver.so.%abiversion.*
%_libdir/libguichan_sdl-%libver.so.%abiversion
%_libdir/libguichan_sdl-%libver.so.%abiversion.*
%_libdir/libguichan_opengl-%libver.so.%abiversion
%_libdir/libguichan_opengl-%libver.so.%abiversion.*
%_libdir/libguichan_allegro-%libver.so.%abiversion
%_libdir/libguichan_allegro-%libver.so.%abiversion.*

%files devel
%_libdir/libguichan*.so
%_includedir/guichan*
%_pkgconfigdir/*.pc

%changelog
* Sun Oct 11 2026 Vitaly Lipatov <lav@altlinux.ru> 0.8.3-alt1
- new version 0.8.3
- drop libs linking patch (fixed upstream)
- SONAME changed to libguichan*-0.8.1.so.2: rename libguichan to libguichan2
  (Shared Libs Policy)
- obsolete the old libguichan package

* Wed Jun 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.2-alt3.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Mar 22 2011 Fr. Br. George <george@altlinux.ru> 0.8.2-alt3
- Rebuild with allegro-4.4

* Tue Dec 14 2010 Fr. Br. George <george@altlinux.ru> 0.8.2-alt2
- Rebuild with set-versioned

* Wed May 12 2010 Fr. Br. George <george@altlinux.ru> 0.8.2-alt1
- Version up

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.7.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libguichan
  * postun_ldconfig for libguichan
  * postclean-05-filetriggers for spec file

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt1
- new version 0.7.1 (with rpmrb script)
- update patch, update buildreqs

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt0.2
- fix linking, check on x86_64 

* Mon Sep 04 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt0.1
- new version 0.5.0 (with rpmrb script)

* Mon May 29 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt0.4
- build snapshot

* Sun Dec 04 2005 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt0.3
- use _x11libdir for X11 libs

* Sat Sep 17 2005 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt0.2
- first build for ALT Linux Sisyphus
- spec from PLD

