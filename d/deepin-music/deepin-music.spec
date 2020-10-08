Name: deepin-music
Version: 6.0.1.75
Release: alt1
Summary: Awesome music player with brilliant and tweakful UI Deepin-UI based
License: GPL-3.0+ and LGPL-2.1+
Group: Sound
Url: https://github.com/linuxdeepin/deepin-music
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-music_6.0.1.75_alt_qt5.15.patch

BuildRequires(pre): rpm-build-kf5 rpm-build-ninja cmake
BuildRequires: gcc-c++ git-core qt5-base-devel qt5-tools-devel libicu-devel libtag-devel libavutil-devel libavformat-devel libcue-devel dtk5-core-devel dtk5-widget-devel kf5-kcodecs-devel libXext-devel qt5-svg-devel qt5-multimedia-devel qt5-x11extras-devel libvlc-devel

%description
%summary.

%package -n lib%name-static
Summary: Static libraries for %name
Group: Development/Other
Provides: %name-devel = %version
Obsoletes: %name-devel < %version

%description -n lib%name-static
This package provides static libraries for %name.

%prep
%setup
%patch -p2
sed -i 's|#include <libcue/libcue.h>|#include <libcue-1.4/libcue/libcue.h>|' music/libdmusic/util/cueparser.cpp

%build
%cmake_insource \
    -GNinja \
    -DCMAKE_INSTALL_LIBDIR=%_libdir
%ninja_build

%install
%ninja_install
%find_lang %name

%files -f %name.lang
%doc CHANGELOG.md COPYING LICENSE README.md
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%files -n lib%name-static
%_libdir/*.a

%changelog
* Thu Oct 08 2020 Leontiy Volodin <lvol@altlinux.org> 6.0.1.75-alt1
- New version (6.0.1.75) with rpmgs script.
- Built with cmake and ninja.
- Built with gcc instead clang.

* Sat Oct 03 2020 Leontiy Volodin <lvol@altlinux.org> 6.0.1.20-alt1
- New version (6.0.1.20) with rpmgs script.

* Thu Sep 10 2020 Leontiy Volodin <lvol@altlinux.org> 6.0.1.8-alt1
- Initial build for ALT Sisyphus (thanks archlinux for this spec).
