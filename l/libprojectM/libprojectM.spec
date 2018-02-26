# FIXME: soname
%define oname	projectM

Name: lib%oname
Version: 2.0.1
Release: alt3

License: LGPL
Group: System/Libraries
Url: http://projectm.sourceforge.net/

Summary: Awesome music visualizer

Packager: Motsyo Gennadi <drool@altlinux.ru>

Source0: http://freefr.dl.sourceforge.net/project/projectm/2.0.1/%oname-%version-Source.tar.gz
Patch1: %name-1.2.0-cmake_version.patch
Patch2: %name-2.0.1-alt_link.patch

Requires: fonts-ttf-vera

# Automatically added by buildreq on Fri Apr 02 2010 (-bi)
BuildRequires: cmake gcc-c++ libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libftgl-devel libglew-devel libgomp-devel libxkbfile-devel xorg-xf86vidmodeproto-devel

%description
projectM is a reimplementation of Milkdrop under OpenGL. It is an
awesome music visualizer. There is nothing better in the world of
Unix.

%package devel
Summary: Header files for projectM library
Group: Development/C
Requires: %name = %version-%release

%description devel
Header files for projectM library.

%package static
Summary: Static projectM library
Group: Development/Libraries
Requires: %name-devel = %version-%release

%description static
Static projectM library.

%prep
%setup -n %oname-%version-Source
%patch1 -p1
%patch2 -p1
%__subst 's| m | m pthread |' CMakeLists.txt

%build
cmake \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DUSE_FBO:STRING=FALSE \
	-DLIB_INSTALL_DIR:STRING=%_libdir \
%ifarch x86_64
	-DLIB_SUFFIX=64 \
%endif

%make_build

%install
%make DESTDIR=%buildroot install
rm -f %buildroot/%_libdir/libprojectM.a
rm -f %buildroot/%_datadir/%oname/fonts/*.ttf
ln -s /usr/share/fonts/ttf/TrueType-vera/Vera.ttf %buildroot/%_datadir/%oname/fonts/Vera.ttf
ln -s /usr/share/fonts/ttf/TrueType-vera/VeraMono.ttf %buildroot/%_datadir/%oname/fonts/VeraMono.ttf

%files
%doc ChangeLog
%_libdir/libprojectM.so.*
%dir %_datadir/%oname/
%_datadir/%oname/config.inp
%dir %_datadir/%oname/fonts/
%_datadir/%oname/fonts/*.ttf
%dir %_datadir/%oname/presets/
%_datadir/%oname/presets/*
%dir %_datadir/%oname/shaders/
%_datadir/%oname/shaders/*

%files devel
%_includedir/%name/
%_libdir/libprojectM.so
%_pkgconfigdir/libprojectM.pc

#%files static
#%_libdir/libprojectM.a

%changelog
* Tue Jun 28 2011 Motsyo Gennadi <drool@altlinux.ru> 2.0.1-alt3
- fix for included fonts

* Sat Apr 02 2011 Motsyo Gennadi <drool@altlinux.ru> 2.0.1-alt2
- build without internal fonts (close #25320)

* Fri Apr 02 2010 Motsyo Gennadi <drool@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Wed Oct 21 2009 Motsyo Gennadi <drool@altlinux.ru> 1.2.0-alt3.2
- fix build without '%cmake' macros
- fix build with optflags
- fix warning for cmake version

* Wed Aug 26 2009 Motsyo Gennadi <drool@altlinux.ru> 1.2.0-alt3.1
- fix build with gcc44

* Sun Mar 01 2009 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt3
- build with US_FBO=FALSE (disable Framebuffer Objects using)

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt2.1
- NMU:
  * updated build dependencies

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt2
- fix build on x86_64

* Sat Jun 14 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Wed Nov 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.01-alt2
- fix build on x86_64

* Sat Oct 27 2007 Vitaly Lipatov <lav@altlinux.ru> 1.01-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)

