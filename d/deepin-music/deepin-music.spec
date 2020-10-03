Name: deepin-music
Version: 6.0.1.20
Release: alt1
Summary: Awesome music player with brilliant and tweakful UI Deepin-UI based
License: GPL-3.0+ and LGPL-2.1+
Group: Sound
Url: https://github.com/linuxdeepin/deepin-music
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-music_6.0.1.8_archlinux_qt5.15.patch

BuildRequires(pre): rpm-build-kf5 clang10.0-devel
BuildRequires: gcc-c++ git-core qt5-base-devel qt5-tools libicu-devel libtag-devel libavutil-devel libavformat-devel libcue-devel dtk5-core-devel dtk5-widget-devel kf5-kcodecs-devel libXext-devel qt5-svg-devel qt5-multimedia-devel qt5-x11extras-devel libvlc-devel

%description
%summary.

%package devel
Summary: Development files for %name
Group: Development/Other

%description devel
This package provides development files for %name.

%prep
%setup
%patch -p1
# Fix library path.
sed -i 's|$${PREFIX}/lib|%_libdir|' src/libdmusic/libdmusic.pro src/plugin/netease-meta-search/netease-meta-search.pro src/vendor/dbusextended-qt/src/src.pro src/vendor/mpris-qt/src/src.pro
# Remove snap files.
# rm -rf snap/

%build
%qmake_qt5 \
    PREFIX=%_prefix \
    QT.KCodecs.libs=%_K5link \
    QMAKE_STRIP= -spec linux-clang
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
%find_lang %name

%files -f %name.lang
%doc CHANGELOG.md COPYING LICENSE README.md
%_bindir/%name
%_libdir/*.so.*
%_desktopdir/%name.desktop
%_datadir/%name/
%dir %_datadir/dman/
%_datadir/dman/%name/
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/translations/*.qm

%files devel
%_libdir/*.so
%dir %_includedir/DBusExtended/
%_includedir/DBusExtended/*
%dir %_includedir/MprisQt/
%_includedir/MprisQt/*
%_libdir/qt5/mkspecs/features/mpris-qt5.prf
%_pkgconfigdir/*.pc

%changelog
* Sat Oct 03 2020 Leontiy Volodin <lvol@altlinux.org> 6.0.1.20-alt1
- New version (6.0.1.20) with rpmgs script.

* Thu Sep 10 2020 Leontiy Volodin <lvol@altlinux.org> 6.0.1.8-alt1
- Initial build for ALT Sisyphus (thanks archlinux for this spec).
