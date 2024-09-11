%define repo dde-fcitx5configtool-plugin

%def_enable clang

Name: deepin-fcitx5configtool-plugin
Version: 5.0.23
Release: alt1

Summary: The input method management plug-in of DDE control center

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-fcitx5configtool-plugin

Provides: %repo = %EVR

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires: cmake extra-cmake-modules dqt5-base-devel dqt5-tools-devel dqt5-x11extras-devel dqt5-svg-devel fcitx5-devel fcitx5-qt-devel xkeyboard-config-devel iso-codes-devel appstream libxkbcommon-devel libdtkwidget-devel deepin-control-center-devel deepin-qt-dbus-factory-devel kf5-kitemviews-devel kf5-kitemviews-devel kf5-kwidgetsaddons-devel
BuildRequires(pre): rpm-build-ninja rpm-macros-dqt5
%if_enabled clang
BuildRequires(pre): clang-devel lld-devel
%else
BuildRequires(pre): gcc-c++
%endif

%description
%summary.

%prep
%setup -n %repo-%version
%patch -p1

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PATH=%_dqt5_bindir:$PATH
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
    -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%find_lang --with-qt --output=%name.lang dde-control-center fcitx5-configtool

%files -f %name.lang
%doc README*.md
%_bindir/kbd-layout-viewer5
%_desktopdir/kbd-layout-viewer5.desktop
%dir %_libdir/dde-control-center/
%dir %_libdir/dde-control-center/modules/
%_libdir/dde-control-center/modules/libdcc-fcitx5configtool-plugin.so
# translations
%dir %_datadir/dde-control-center/
%dir %_datadir/dde-control-center/translations/
%_datadir/dde-control-center/translations/deepin-fcitx5configtool-plugin.qm
%_datadir/dde-control-center/translations/deepin-fcitx5configtool-plugin_ky@Arab.qm

%changelog
* Wed Sep 11 2024 Leontiy Volodin <lvol@altlinux.org> 5.0.23-alt1
- New version 5.0.23.
- Built via separate qt5 instead system (ALT #48138).

* Thu Dec 14 2023 Leontiy Volodin <lvol@altlinux.org> 5.0.17.0.4.7355-alt1
- Initial build for ALT Sisyphus.
