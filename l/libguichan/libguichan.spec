%define oname guichan
Name: libguichan
Version: 0.8.2
Release: alt3

Summary: Guichan - small, efficient C++ GUI library designed for games

License: BSD
Group: System/Libraries

Source: http://guichan.googlecode.com/files/%oname-%version.tar.gz

Patch: %name-0.8.2.patch

Url: http://guichan.googlecode.com

# manually removed: gcc-g77 libg2c-devel 
# Automatically added by buildreq on Tue May 11 2010
BuildRequires: gcc-c++ libGL-devel libSDL-devel libSDL_image-devel liballegro-devel

%description
Guichan is a small, efficient C++ GUI library designed for games. It
comes with a standard set of widgets and can use several different
objects for displaying graphics and grabbing user input.

%package devel
Summary: Header files for Guichan library
Group: Development/C
Requires: %name = %version-%release
Requires: libstdc++-devel

%description devel
Header files for Guichan library.

%prep
%setup -q -n %oname-%version
%patch -p1
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

%files
%doc AUTHORS ChangeLog NEWS README TODO
%_libdir/libguichan*.so.*

%files devel
%_libdir/libguichan*.so
%_includedir/guichan*
%_pkgconfigdir/*.pc

%changelog
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

