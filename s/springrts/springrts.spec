%define _unpackaged_files_terminate_build 1
%def_disable debug

Name: springrts
Version: 0.81.2.1
Release: alt1.4

Summary: Real time strategy game engine with many mods
License: GPL2+ or Artistic
Group: Games/Strategy 
Url: http://springrts.com/

Packager: Maxim Ivanov <redbaron@altlinux.org>

BuildRequires(pre): rpm-build-xdg rpm-macros-cmake
#BuildRequires: boost-program_options-devel cmake gcc-c++ libSDL-devel 

BuildRequires: cmake cmake-modules java-devel /proc libGL-devel libGLU-devel gcc-c++
BuildRequires: boost-devel boost-program_options-devel boost-asio-devel boost-signals-devel
BuildRequires: libICE-devel libSM-devel libX11-devel libXdamage-devel libXfixes-devel libXrender-devel 
BuildRequires: libXt-devel libfreetype-devel libogg-devel libstdc++-devel 
BuildRequires: xorg-inputproto-devel xorg-kbproto-devel xorg-xextproto-devel xorg-xf86miscproto-devel 
BuildRequires: xorg-xineramaproto-devel xorg-xproto-devel zlib-devel p7zip libXcursor-devel
BuildRequires: libdevil-devel libfreeglut-devel libglew-devel libopenal1-devel 
BuildRequires: libvorbis-devel  python-devel libSDL-devel

#BuildRequires: boost-asio-devel boost-program_options-devel boost-signals-devel ccmake gcc-c++ java-devel  libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdmcp-devel libXext-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libdevil-devel libfreeglut-devel libglew-devel libopenal1-devel libvorbis-devel libxkbfile-devel tzdata xorg-xf86vidmodeproto-devel zip


Requires: %name-data = %version-%release
Source0: %name-%version.tar
Patch0: %name-0.81.2.1-alt-glibc.patch

%description
Spring is an open source RTS (Real time Strategy) engine originally
designed to recreate the experience of Total Annihilation.  Spring now
supports many different games ("mods"), including both remakes of the
original Total Annihilation and completely new games.

This package contains the game engine and default AI, but no maps, mods,
or user interface.

%package data
Summary: data files for Spring RTS engine
Group: Games/Strategy
BuildArch: noarch

%description data
data files for Spring RTS engine

%package dedicated
Summary: springrts dedicated server
Group: Games/Strategy
Requires: %name-data = %version-%release

%description dedicated
springrts dedicated server

%prep
%setup 
%patch0 -p1

%build
%cmake \
%if_enabled debug
        -DCMAKE_BUILD_TYPE=Debug \
%else
        -DCMAKE_BUILD_TYPE=Release \
%endif
        -DLIBDIR=%_libdir \
        -DBINDIR=%_gamesbindir \
        -DAI_LIBS_DIR=%_libdir/spring \
        -DAI_DATA_DIR=%_gamesdatadir/spring
cd BUILD
%make_build VERBOSE=1

%install
cd BUILD
%make install DESTDIR=%buildroot
mkdir %buildroot%_gamesdatadir/spring/{mods,maps}

%if_enabled debug
%add_strip_skiplist %_bindir/*
%add_strip_skiplist %_libdir/*
%endif

%files 
%_gamesbindir/spring
%_libdir/spring

%files data
%_gamesdatadir/*
%_pixmapsdir/*
%_xdgmimedir/packages/*
%_desktopdir/*

%files dedicated
%_gamesbindir/spring-dedicated
%_libdir/*.so

%post data
  [ -f %_gamesdatadir/spring/base/otacontent.sdz ] && \
  [ -f %_gamesdatadir/spring/base/tacontent_v2.sdz ] && \
  [ -f %_gamesdatadir/spring/base/tatextures_v062.sdz ] && exit 0

  echo " ================= Non-free content not included  ==================="
  echo "  Please download and install additional non-free content which      "
  echo "  could not be included in this package.                             "
  echo ""
  echo "   1. download http://files.simhost.org/Spring/base-ota-content.zip  "
  echo "   2. extract it to %_gamesdatadir/spring/base                       "
  echo " ===================================================================="

%changelog
* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.81.2.1-alt1.4
- Rebuilt with Boost 1.49.0

* Mon Aug 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.81.2.1-alt1.3
- Rebuilt with Boost 1.47.0

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.81.2.1-alt1.2
- Rebuilt with Boost 1.46.1

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.81.2.1-alt1.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Thu Apr 15 2010 Maxim Ivanov <redbaron at altlinux.org> 0.81.2.1-alt1
- Bump to 0.81.2.1
- NTAI removed as it is broken
- Fix AI load crash

* Thu Apr 15 2010 Maxim Ivanov <redbaron at altlinux.org> 0.81.1.3-alt2
- Fix build with current Boost
- Fix AI libs search by unitsync library

* Mon Feb 01 2010 Maxim Ivanov <redbaron at altlinux.org> 0.81.1.3-alt1
- Bump to 0.81.1.3

* Sun Jan 24 2010 Maxim Ivanov <redbaron at altlinux.org> 0.81.0-alt1
- Bump to 0.81.0

* Sat Jan 09 2010 Maxim Ivanov <redbaron at altlinux.org> 0.80.5.2-alt1
- Updated to 0.80.5.2
- Corrected buildreq
- Better arch vs noarch files destribution

* Sat Oct 31 2009 Maxim Ivanov <redbaron at altlinux.org> 0.80.5.1-alt1
- Updated to 0.80.5.1
- Dedicated server packed separately

* Sat Sep 05 2009 Maxim Ivanov <redbaron at altlinux.org> 0.80.4.1-alt1
- Update to 0.80.4.1

* Sat Aug 29 2009 Maxim Ivanov <redbaron at altlinux.org> 0.80.2-alt1
- Update to 0.80.2

* Sun Jun 07 2009 Maxim Ivanov <redbaron at altlinux.org> 0.79.1-alt1
- Initial build for ALTLinux
