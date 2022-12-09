%define oname	projectM

%ifarch %arm riscv64
%def_disable qt
%else
%def_disable qt
%endif

Name: lib%oname
Version: 2.1.0
Release: alt15.1

Summary: Awesome music visualizer
License: LGPLv2.1
Group: System/Libraries

Url: http://projectm.sourceforge.net/
#Source: http://freefr.dl.sourceforge.net/project/projectm/2.0.1/%oname-complete-%version-Source.tar.gz
Source: %oname-complete-%version-Source.tar

Patch1: %name-complete-2.1.0-doxy.patch
Patch2: %name-complete-2.1.0-link.patch
Patch3: %name-%version-alt-gcc6.patch
Patch4: %name-2.1.0-paths.patch
Patch5: %name-qt-2.1.0-paths.patch
Patch6: %name-g++8.patch

Requires: fonts-ttf-dejavu

BuildPreReq: doxygen

BuildRequires: cmake gcc-c++ libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXft-devel libXinerama-devel
BuildRequires: libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libftgl-devel libglew-devel
BuildRequires: libgomp-devel libxkbfile-devel xorg-xf86vidmodeproto-devel libvisual0.4-devel libpulseaudio-devel >= 0.9.8
BuildRequires: libSDL-devel

%if_enabled qt
BuildRequires: libqt4-devel
%endif

%description
projectM is a reimplementation of Milkdrop under OpenGL. It is an
awesome music visualizer. There is nothing better in the world of
Unix.

%package qt
Summary: The Qt frontend to the projectM visualization plugin
Group: System/Libraries
Requires: %name = %version-%release

%description qt
projectM-qt is a GUI designed to enhance the projectM user and preset writer
experience. It provides a way to browse, search, rate presets and setup
preset playlists for projectM-jack and projectM-pulseaudio.

%package -n %oname-pulseaudio
Summary: The projectM visualization plugin for pulseaudio
Group: Sound
Requires: %name-qt = %version-%release

%description -n %oname-pulseaudio
This package allows the use of the projectM visualization plugin through any
pulseaudio compatible applications.

%package -n %oname-test
Summary: Test utils for projectM
Group: Other
License: GPLv2
Requires: %name = %version-%release

%description -n %oname-test
Test utils for projectM

%package -n %oname-libvisual
Summary: The projectM visualization plugin for libvisual
Group: Sound
License: GPLv2
Requires: %name = %version-%release

%description -n %oname-libvisual
This package allows the use of the projectM visualization plugin through any
libvisual compatible applications.

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
%setup -n %oname-complete-%version-Source
%patch1 -p1
%patch2 -p1
%patch3 -p2
%patch4 -p1
%patch5 -p1
%patch6 -p2
%ifarch %e2k
# This line from "libvisual.h" is poisonous to some system headers:
# "#define inline  inline __attribute__ ((always_inline))"
sed -i '/<libvisual\/libvisual\.h>/i #include <sstream>' \
	src/projectM-libvisual/actor_projectM.cpp
%endif

%build
%add_optflags -std=gnu++11
%cmake \
	-DUSE_FBO:STRING=FALSE \
%if_disabled qt
	-DINCLUDE-PROJECTM-QT:BOOL=FALSE \
	-DINCLUDE-PROJECTM-PULSEAUDIO:BOOL=FALSE \
	-DINCLUDE-PROJECTM-JACK:BOOL=FALSE \
%endif
	#
%cmake_build

cd docs && doxygen %oname.dox

%install
%cmakeinstall_std

rm -f %buildroot/%_libdir/libprojectM.a
rm -f %buildroot/%_datadir/%oname/fonts/*.ttf
ln -s /usr/share/fonts/ttf/dejavu/DejaVuSans.ttf %buildroot/%_datadir/%oname/fonts/Vera.ttf
ln -s /usr/share/fonts/ttf/dejavu/DejaVuSansMono.ttf %buildroot/%_datadir/%oname/fonts/VeraMono.ttf

%files
%doc AUTHORS.txt FAQ.txt docs/doxygen/html
%_libdir/libprojectM.so.*
%dir %_datadir/%oname/
%_datadir/%oname/config.inp
%dir %_datadir/%oname/fonts/
%_datadir/%oname/fonts/*.ttf
%dir %_datadir/%oname/presets/
%_datadir/%oname/presets/*
%dir %_datadir/%oname/shaders/
%_datadir/%oname/shaders/*

%if_enabled qt
%files qt
%_libdir/libprojectM-qt.so.*

%files -n %oname-pulseaudio
%_bindir/*-pulseaudio
%_desktopdir/*-pulseaudio.desktop
%_pixmapsdir/prjm16-transparent.svg
%endif

%files -n %oname-test
%_bindir/*-test*

%files -n %oname-libvisual
%doc src/projectM-libvisual/AUTHORS src/projectM-libvisual/ChangeLog
%_libdir/libvisual*/actor/libprojectM_libvisual.so

%files devel
%_includedir/%name/
%_libdir/libprojectM.so
%_pkgconfigdir/libprojectM.pc
%if_enabled qt
%_includedir/%name-qt/
%_libdir/libprojectM-qt.so
%_pkgconfigdir/libprojectM-qt.pc
%endif

# TODO:
# - consider https://src.fedoraproject.org/rpms/libprojectM/raw/master/f/libprojectM-c++14.patch

%changelog
* Fri Dec 09 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.1.0-alt15.1
- Fixed build for Elbrus.

* Fri Nov 12 2021 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt15
- build wihtout Qt4

* Mon Mar 02 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.1.0-alt14
- Disabled qt frontend on riscv64.

* Thu Feb 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.1.0-alt13
- no return statement in the non-void function fixed (according g++8)

* Fri Jul 06 2018 Michael Shigorin <mike@altlinux.org> 2.1.0-alt12
- replaced x86_64/aarch64 specific kludge with proper fedora patches
- minor spec cleanup

* Wed Apr 11 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.0-alt11
- fixed packaging on 64bit arches other than x86_64

* Fri Jul 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt10
- Fixed build with gcc-6

* Fri Apr 08 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 2.1.0-alt9.qa1
- Rebuilt for gcc5 C++11 ABI.

* Tue Jul 30 2013 Motsyo Gennadi <drool@altlinux.ru> 2.1.0-alt9
- fix build for x86_64 (thanx to lnkvisitor@ for remote hasher64)

* Tue Jul 30 2013 Motsyo Gennadi <drool@altlinux.ru> 2.1.0-alt8
- fix test utils for linked with libGL

* Tue Jul 30 2013 Motsyo Gennadi <drool@altlinux.ru> 2.1.0-alt7
- build with default components

* Tue Jul 30 2013 Motsyo Gennadi <drool@altlinux.ru> 2.1.0-alt6
- fix

* Tue Jul 30 2013 Motsyo Gennadi <drool@altlinux.ru> 2.1.0-alt5
- fix

* Tue Jul 30 2013 Motsyo Gennadi <drool@altlinux.ru> 2.1.0-alt4
- build without visual plugin (temporary)

* Tue Jul 30 2013 Motsyo Gennadi <drool@altlinux.ru> 2.1.0-alt3
- build without pulseaudio plugin (temporary)

* Tue Jul 30 2013 Motsyo Gennadi <drool@altlinux.ru> 2.1.0-alt2
- disable test from build
- change fonts from Vera to DejaVu

* Mon Jul 29 2013 Motsyo Gennadi <drool@altlinux.ru> 2.1.0-alt1
- 2.1.0

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

