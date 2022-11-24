%define _cmake__builddir BUILD
%define repo dde-kwin
%define kwin_ver %{get_version plasma5-kwin-devel}
%_K5if_ver_lteq %kwin_ver 5.21.5
%def_enable kwin_ext
%else
%def_disable kwin_ext
%endif

%def_disable clang

Name: deepin-kwin
Version: 5.5.11
Release: alt2.1

Summary: KWin configuration for Deepin Desktop Environment
License: GPL-3.0+ and MIT
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-kwin
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

# upstream patches
Patch: kwin-greater-than.patch
Patch2: dde-kwin.5.4.26.patch
# archlinux patches
Patch4: %name-tabbox-chameleon-rename.patch
# ALT patches
Patch11: deepin-kwin-5.3.7-ALT-cmake-bad-elfs.patch

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-kf5 rpm-build-ninja
BuildRequires(pre): plasma5-kwin-devel libkwin5
BuildRequires: cmake extra-cmake-modules qt5-tools qt5-tools-devel qt5-base-devel plasma5-kdecoration-devel qt5-x11extras-devel qt5-declarative-devel kf5-kwindowsystem-devel kf5-kcoreaddons-devel dtk5-gui-devel dtk5-common kf5-kconfig-devel kf5-kglobalaccel-devel kf5-ki18n-devel gsettings-qt-devel plasma5-kwin-devel plasma5-kwayland-server-devel kf5-kwayland-devel
BuildRequires: zlib-devel bzlib-devel libpng-devel libpcre-devel libbrotli-devel libuuid-devel libexpat-devel libdrm-devel libgbm-devel
BuildRequires: libxcb-devel libglvnd-devel libX11-devel
Requires: plasma5-kwin
# libkwineffects12 libkwinglutils12 libxcb libGL libX11

%description
This package provides a kwin configuration that used as the new WM for Deepin
Desktop Environment.

%package devel
Summary: Development package for %name
Group: Graphical desktop/Other

%description devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version
#%%patch -p1
#%%patch2 -p1
#%%patch4 -p1
#%%patch11 -p2

sed -i 's|${CMAKE_INSTALL_PREFIX}/share/kwin/scripts|%_K5data/kwin/scripts/|' \
    scripts/CMakeLists.txt
sed -i 's|${CMAKE_INSTALL_PREFIX}/share/kwin/tabbox|%_K5data/kwin/tabbox|' \
    tabbox/CMakeLists.txt
sed -i 's|/usr/include/KWaylandServer|%_K5inc/KWaylandServer|' CMakeLists.txt
sed -i 's|${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}|${CMAKE_INSTALL_LIBDIR}|' \
    plugins/platforms/lib/dde-kwin.pc.in
sed -i 's| -L/usr/X11R6/lib64| -L%_libdir|; s| -lpthread| -L%_libdir -lpthread|' \
    plugins/platforms/lib/dde-kwin.pc.in
# sed -i '1icmake_minimum_required(VERSION 3.23)' CMakeLists.txt
# sed -i 's|/usr/share/backgrounds/default_background.jpg|/usr/share/design-current/backgrounds/default.png|' \
#     plugins/kwineffects/multitasking/background.cpp \
#     deepin-wm-dbus/deepinwmfaker.cpp
sed -i 's|/usr/lib|%_libdir|' \
    plugins/platforms/plugin/main_wayland.cpp \
    plugins/platforms/plugin/main.cpp
# Fix wm error
sed -i 's|kwin_x11 -platform|%_K5bin/kwin_x11 -platform|' \
    configures/kwin_no_scale.in

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif
export PATH=%_qt5_bindir:$PATH
# Workaround for missing libkwin.so
mkdir libs
ln -s %_K5lib/libkwin.so.5 libs/libkwin.so
%K5cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_LIBDIR=%_K5lib \
    -DKWIN_LIBRARY_PATH=`pwd`/libs \
%if_enabled kwin_ext
    -DUSE_PLUGINS=ON \
    -DUSE_WINDOW_TOOL=ON \
%else
    -DUSE_PLUGINS=OFF \
    -DUSE_WINDOW_TOOL=OFF \
    -DUSE_SCRIPTS=OFF \
    -DUSE_DEEPIN_WM_DBUS=ON \
    -DUSE_TABBOX=ON \
    -DUSE_DEEPIN_WAYLAND=OFF \
    -DUSE_KWIN_NO_SCALE=ON \
    -DENABLE_BUILTIN_BLUR=OFF \
    -DENABLE_KDECORATION=ON \
    -DENABLE_BUILTIN_MULTITASKING=ON \
    -DENABLE_BUILTIN_BLACK_SCREEN=OFF \
%endif
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
chmod +x %buildroot%_bindir/kwin_no_scale

%files
%doc CHANGELOG.md LICENSE
%_sysconfdir/xdg/*
%_bindir/kwin_no_scale
%_bindir/deepin-wm-dbus
%_datadir/dbus-1/services/*.service
%_datadir/dbus-1/interfaces/*.xml
%_K5data/kwin/tabbox/*
# %%_K5data/kwin/scripts/*
%if_enabled kwin_ext
%_K5plug/platforms/lib%repo-xcb.so
%_K5data/kwin/scripts/*
%dir %_datadir/dde-kwin-xcb/
%dir %_datadir/dde-kwin-xcb/translations/
%_datadir/dde-kwin-xcb/translations/%repo-xcb*.qm
%dir %_K5plug/platforms/
%_K5lib/libkwin-xcb.so.*
%_K5plug/platforms/lib%repo-wayland.so
%dir %_K5plug/kwin/
%dir %_K5plug/kwin/effects/
%dir %_K5plug/kwin/effects/plugins/
%_K5plug/kwin/effects/plugins/libblur.so
%_K5plug/kwin/effects/plugins/libmultitasking.so
%_K5plug/kwin/effects/plugins/libscissor-window.so
%_K5plug/org.kde.kdecoration2/libdeepin-chameleon.so
%endif

%files devel
%if_enabled kwin_ext
%_K5plug/platforms/lib%repo-xcb.so
%_datadir/dbus-1/interfaces/*.xml
%_includedir/%repo/
%_pkgconfigdir/%repo.pc
%_K5lib/libkwin-xcb.so
%endif

%changelog
* Thu Nov 24 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.11-alt2.1
- Removed hard mention of the cmake build version.

* Wed Nov 23 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.11-alt2
- New version (5.5.11-deepin).
- Restored blur.

* Thu Oct 06 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.11-alt1
- New version (5.5.11).

* Thu Jun 02 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.26-alt3
- Fixed multitasking using the dock panel.
- Rebuilt with gcc12.

* Tue May 31 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.26-alt2
- Fixed wallpaper error.
- Enabled blur.
- Enabled checkbox for rounding.

* Tue Apr 19 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.26-alt1
- New version (5.4.26).

* Wed Mar 09 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.19-alt1
- New version (5.4.19).

* Fri Feb 04 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.12-alt1
- New version (5.4.12).

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 5.3.14-alt3
- fix to build with new kwin

* Tue Oct 05 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.14-alt2
- Fixed library links with x11.

* Fri Aug 20 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.14-alt1
- New version (5.3.14).

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.9-alt1
- New version (5.3.9) with rpmgs script.

* Fri Apr 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.7-alt3.git4d0141c
- Fixed build with dtk 5.4.13.

* Wed Mar 31 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.7-alt2.git4d0141c
- Fixed compile with kwin 5.21.
- Built from commit 4d0141c175e770586f2e08893c8105d1022dfc29.

* Tue Mar 30 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.7-alt1
- New version (5.3.7) with rpmgs script.

* Mon Jan 04 2021 Leontiy Volodin <lvol@altlinux.org> 5.2.0.13-alt1
- New version (5.2.0.13) with rpmgs script.

* Tue Dec 15 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.11-alt2
- Changed default background.

* Fri Dec 11 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.11-alt1
- New version (5.2.0.11) with rpmgs script.

* Tue Dec 08 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.2-alt4
- Fixed critical wm error.

* Wed Nov 25 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.2-alt3
- Fixed undefined symbols in elfs.
- Fixed url.

* Wed Nov 25 2020 Andrey Cherepanov <cas@altlinux.org> 5.2.0.2-alt2.1
- Link with libkwin to prevent unresolved symbols.

* Wed Oct 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.2-alt2
- Fixed file locations.

* Wed Sep 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.2-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
