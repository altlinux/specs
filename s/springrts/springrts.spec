%define _unpackaged_files_terminate_build 1
%def_enable debug

Name: springrts
Version: 104.0
Release: alt1

Summary: Real time strategy game engine with many mods
License: GPL2+ or Artistic
Group: Games/Strategy
Url: https://springrts.com/

BuildRequires(pre): rpm-build-xdg rpm-macros-cmake
BuildRequires: cmake cmake-modules java-devel /proc libGL-devel libGLU-devel gcc-c++
BuildRequires: boost-devel boost-program_options-devel boost-asio-devel boost-signals-devel boost-filesystem-devel
BuildRequires: libICE-devel libSM-devel libX11-devel libXdamage-devel libXfixes-devel libXrender-devel 
BuildRequires: libXt-devel libfreetype-devel libogg-devel libstdc++-devel 
BuildRequires: xorg-inputproto-devel xorg-kbproto-devel xorg-xextproto-devel xorg-xf86miscproto-devel 
BuildRequires: xorg-xineramaproto-devel xorg-xproto-devel zlib-devel p7zip libXcursor-devel
BuildRequires: libdevil-devel libfreeglut-devel libglew-devel libopenal1-devel 
BuildRequires: libvorbis-devel  python-devel libSDL2-devel
BuildRequires: docbook5-style-xsl asciidoc libminizip-devel
BuildRequires: libXres-devel libXtst-devel libXau-devel libXcomposite-devel
BuildRequires: libXdmcp-devel libXext-devel libXft-devel libXi-devel
BuildRequires: libXinerama-devel libxkbfile-devel libXmu-devel libXpm-devel
BuildRequires: libXrandr-devel libXScrnSaver-devel libXv-devel
BuildRequires: libXxf86misc-devel libXxf86vm-devel
BuildRequires: libcurl-devel jsoncpp-devel libunwind-devel

Requires: %name-data = %EVR
Conflicts: %name-dedicated < %EVR
Provides: %name-dedicated = %EVR
Obsoletes: %name-dedicated

Source: %name-%version.tar
Patch1: %name-alt-linking.patch

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

%prep
%setup
%patch1 -p2

%build
%add_optflags -fPIC -DPIC -D_FILE_OFFSET_BITS=64
%cmake \
%if_enabled debug
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%else
        -DCMAKE_BUILD_TYPE=Release \
%endif
        -DLIBDIR=%_libdir \
        -DBINDIR=%_gamesbindir \
        -DAI_LIBS_DIR=%_libdir/spring \
        -DAI_DATA_DIR=%_gamesdatadir/spring \
        -DDOCDIR=share/doc/%name-%version \
        -DDOCBOOK_XSL=%_datadir/sgml/docbook/xsl-ns-stylesheets/manpages/docbook.xsl \
        -DAI_TYPES=NATIVE

%make_build -C BUILD VERBOSE=1

%install
%makeinstall_std -C BUILD VERBOSE=1

# Move icons into proper Freedesktop hicolor theme
mkdir -p %buildroot%_liconsdir

mv %buildroot%_pixmapsdir/spring.png \
    %buildroot%_liconsdir/

mkdir -p %buildroot%_iconsdir/hicolor/48x48/mimetypes/

mv %buildroot%_pixmapsdir/application-x-spring-demo.png \
    %buildroot%_iconsdir/hicolor/48x48/mimetypes/

# Make it visible
sed -i -e '/NoDisplay=true/d' \
    %buildroot%_desktopdir/spring.desktop

%files 
%_gamesbindir/pr-downloader
%_gamesbindir/spring
%_gamesbindir/spring-headless
%_gamesbindir/spring-dedicated
%_libdir/spring
%_libdir/*.so

%files data
%_gamesdatadir/*
%_xdgmimedir/packages/*
%_desktopdir/*
%_liconsdir/*
%_iconsdir/hicolor/48x48/mimetypes/*.png

%changelog
* Mon Apr 02 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 104.0-alt1
- Updated to upstream version 104.0.

* Thu Sep 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 103.0-alt1
- Updated to upstream release 103.0.
- Moved dedicated server back to main package.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 91.0-alt1.git20120830.qa1.1
- rebuild with boost 1.57.0
- fix build

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 91.0-alt1.git20120830.qa1
- NMU: rebuilt with libboost_*.so.1.53.0.

* Wed Dec 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 91.0-alt1.git20120830
- Version 91.0

* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.81.2.1-alt1.5
- Fixed build

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
