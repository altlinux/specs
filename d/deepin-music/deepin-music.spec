%def_disable clang
%def_enable cmake

%define repo dmusic

Name: deepin-music
Version: 6.0.1.91
Release: alt2
Summary: Awesome music player with brilliant and tweakful UI Deepin-UI based
License: GPL-3.0+ and LGPL-2.1+
Group: Sound
Url: https://github.com/linuxdeepin/deepin-music
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-music_6.0.1.75_alt_qt5.15.patch

%if_enabled clang
BuildRequires(pre): clang11.0-devel
%else
BuildRequires(pre): gcc-c++
BuildRequires(pre): libgomp10-devel
%endif

%if_enabled cmake
BuildRequires(pre): cmake rpm-build-ninja
%endif

BuildRequires(pre): rpm-build-kf5
BuildRequires: git-core
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: libicu-devel
BuildRequires: libtag-devel
BuildRequires: libavutil-devel
BuildRequires: libavformat-devel
BuildRequires: libcue-devel
BuildRequires: dtk5-core-devel
BuildRequires: dtk5-widget-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: libXext-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: libvlc-devel
BuildRequires: gsettings-qt-devel
Requires: libvlc ffmpeg
%if_enabled cmake
Requires: lib%repo-static = %version
%else
Requires: lib%repo = %version
%endif

%description
%summary.

%if_enabled cmake
%package -n lib%repo-static
Summary: Static libraries for %name
Group: Development/Other
Provides: lib%name = %version
Obsoletes: lib%name < %version
Provides: lib%name-static = %version
Obsoletes: lib%name-static < %version
Provides: %name-devel = %version
Obsoletes: %name-devel < %version

%description -n lib%repo-static
This package provides static libraries for %name.

%else

%package -n lib%repo
Summary: Libraries for %name
Group: System/Libraries
Provides: %name-static = %version
Obsoletes: %name-static < %version

%description -n lib%repo
This package provides libraries for %name.

%package devel
Summary: Development files for %name
Group: Development/Other
Provides: %name-static = %version
Obsoletes: %name-static < %version

%description devel
This package provides development files for %name.
%endif

%prep
%setup
%patch -p2
#sed -i 's|#include <libcue/libcue.h>|#include <libcue-1.4/libcue/libcue.h>|' music/libdmusic/util/cueparser.cpp
sed -i 's|/usr/lib|%_libdir|' music/music-player/core/pluginmanager.cpp
sed -i 's|#include "widget/soundpixmapbutton.h"|#include "view/widget/soundpixmapbutton.h"|' music/music-player/view/widget/soundvolume.cpp
sed -i 's|#include <QGSettings>|#include <QGSettings/QGSettings>|' music/music-player/view/footerwidget.cpp
sed -i 's|#include "databaseservice.h"|#include "../../presenter/databaseservice.h"|' music/music-player/view/widget/*.cpp
sed -i 's|#include "global.h"|#include "../../core/util/global.h"|' music/music-player/view/widget/playlistview.cpp

%if_enabled cmake
sed -i 's|${CMAKE_BINARY_DIR}/lib|%_libdir|' tests/googletest/googletest/cmake/internal_utils.cmake
%else
sed -i '/libdmusic/d; s/vendor/vendor \\/' music/src.pro
sed -i 's|$${PREFIX}/lib|%_libdir|' \
    music/plugin/netease-meta-search/netease-meta-search.pro \
    music/vendor/mpris-qt/src/src.pro \
    music/vendor/dbusextended-qt/src/src.pro
%endif

%build
%if_enabled cmake

%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%else
export CC="gcc"
export CXX="g++"
export AR="ar"
export NM="nm"
export READELF="readelf"
%endif

%cmake_insource \
    -GNinja \
    -DCMAKE_INSTALL_LIBDIR=%_libdir
%ninja_build

%else

# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 music/src.pro \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
    PREFIX=%_prefix \
    QT.KCodecs.libs=%_K5link \
    QT+=multimedia \
    unix:LIBS+="-L../music/dist/lib/ -ldmusic"
%make_build
%endif

%install
%if_enabled cmake
%ninja_install
%else
%makeinstall INSTALL_ROOT=%buildroot
%endif
%find_lang %name

%files -f %name.lang
%doc CHANGELOG.md COPYING LICENSE README.md
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%if_disabled cmake
%dir %_datadir/dman/
%_datadir/dman/%name/
%_datadir/translations/*.qm

%files -n lib%repo
%_libdir/*.so.*
%endif

%if_enabled cmake
%files -n lib%repo-static
%_libdir/*.a

%else
%files devel
%_libdir/*.so
%dir %_includedir/DBusExtended/
%_includedir/DBusExtended/*
%dir %_includedir/MprisQt/
%_includedir/MprisQt/*
%_libdir/qt5/mkspecs/features/mpris-qt5.prf
%_pkgconfigdir/*.pc
%endif

%changelog
* Fri Mar 05 2021 Leontiy Volodin <lvol@altlinux.org> 6.0.1.91-alt2
- Fixed paths.
- Built with gcc10.
- Renamed libdeepin-music to libdmusic.

* Wed Dec 02 2020 Leontiy Volodin <lvol@altlinux.org> 6.0.1.91-alt1
- New version (6.0.1.91) with rpmgs script.

* Thu Oct 08 2020 Leontiy Volodin <lvol@altlinux.org> 6.0.1.75-alt1
- New version (6.0.1.75) with rpmgs script.
- Built with cmake and ninja.
- Built with gcc instead clang.

* Sat Oct 03 2020 Leontiy Volodin <lvol@altlinux.org> 6.0.1.20-alt1
- New version (6.0.1.20) with rpmgs script.

* Thu Sep 10 2020 Leontiy Volodin <lvol@altlinux.org> 6.0.1.8-alt1
- Initial build for ALT Sisyphus (thanks archlinux for this spec).
