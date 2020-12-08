%define repo dde-kwin

%def_disable clang

Name: deepin-kwin
Version: 5.2.0.2
Release: alt4

Summary: KWin configuration for Deepin Desktop Environment
License: GPL-3.0+ and MIT
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-kwin
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

# archlinux patches
Patch1: %name-added-functions-from-their-forked-kwin.patch
Patch2: %name-tabbox-chameleon-rename.patch
Patch3: %name-build-fix.patch
Patch4: %name-unload-blur.patch
Patch5: deepin-kwin-qt5.15.patch
Patch6: kwin-5.19.patch
# ALT patches
Patch11: deepin-kwin_5.2.0.2_ALT_cmake_bad-elfs.patch
Patch12: deepin-kwin_5.2.0.2_ALT_bad-elfs_multitasking.patch
%if_enabled clang
BuildRequires(pre): clang11.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-kf5 rpm-build-ninja
BuildRequires: cmake extra-cmake-modules qt5-tools qt5-tools-devel qt5-base-devel plasma5-kdecoration-devel qt5-x11extras-devel qt5-declarative-devel kf5-kwindowsystem-devel kf5-kcoreaddons-devel dtk5-gui-devel kf5-kconfig-devel kf5-kglobalaccel-devel kf5-ki18n-devel gsettings-qt-devel plasma5-kwin-devel plasma5-kwayland-server-devel kf5-kwayland-devel
BuildRequires: zlib-devel bzlib-devel libpng-devel libpcre-devel libbrotli-devel libuuid-devel libexpat-devel
BuildRequires: libxcb-devel libglvnd-devel libX11-devel
BuildRequires: libkwin5
Requires: plasma5-kwin libkwineffects12 libkwinglutils12 libxcb libGL libX11

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
%patch1 -R -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch11 -p2
%patch12 -p2

sed -i 's|lrelease|lrelease-qt5|' plugins/platforms/plugin/translate_generation.sh
sed -i 's|${CMAKE_INSTALL_PREFIX}/share/kwin/scripts|%_K5data/kwin/scripts/|' scripts/CMakeLists.txt
sed -i 's|${CMAKE_INSTALL_PREFIX}/share/kwin/tabbox|%_K5data/kwin/tabbox|' tabbox/CMakeLists.txt
sed -i 's|/usr/share/backgrounds/default_background.jpg|/usr/share/backgrounds/deepin/desktop.jpg|' \
    plugins/kwineffects/multitasking/background.cpp \
    deepin-wm-dbus/deepinwmfaker.cpp
sed -i 's|/usr/lib/deepin-daemon|/usr/libexec/deepin-daemon|' deepin-wm-dbus/deepinwmfaker.cpp
sed -i 's|/lib|/%_lib|' plugins/platforms/plugin/main_wayland.cpp \
                        plugins/platforms/plugin/main.cpp \
                        plugins/platforms/lib/CMakeLists.txt
# Fix wm error
sed -i 's|kwin_x11 -platform|%_K5bin/kwin_x11 -platform|' configures/kwin_no_scale.in
# Fix build future version with kwin 5.20
# sed -i '/m_blurManager->create();/d' plugins/kwineffects/blur/blur.cpp

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif
# Workaround for missing libkwin.so
mkdir libs
ln -s %_libdir/libkwin.so.5 libs/libkwin.so
%K5cmake \
    -GNinja \
    -DCMAKE_INSTALL_LIBDIR=%_K5lib \
    -DKWIN_LIBRARY_PATH=`pwd`/libs
%ninja_build -C BUILD

%install
%ninja_install -C BUILD
chmod +x %buildroot%_bindir/kwin_no_scale

%files
%doc CHANGELOG.md LICENSE
%_sysconfdir/xdg/*
%_bindir/deepin-wm-dbus
%_bindir/kwin_no_scale
%_K5lib/libkwin-xcb.so.*
%_datadir/dbus-1/services/*.service
%_datadir/dbus-1/interfaces/*.xml
%_K5data/kwin/scripts/*
%_K5data/kwin/tabbox/*
%dir %_datadir/dde-kwin-xcb/
%dir %_datadir/dde-kwin-xcb/translations/
%_datadir/dde-kwin-xcb/translations/%repo-xcb*.qm
%dir %_K5plug/platforms/
%_K5plug/platforms/lib%repo-xcb.so
%_K5plug/platforms/lib%repo-wayland.so
%dir %_K5plug/kwin/
%dir %_K5plug/kwin/effects/
%dir %_K5plug/kwin/effects/plugins/
%_K5plug/kwin/effects/plugins/libblur.so
%_K5plug/kwin/effects/plugins/libmultitasking.so
%_K5plug/kwin/effects/plugins/libscissor-window.so
%_K5plug/org.kde.kdecoration2/libdeepin-chameleon.so

%files devel
%_includedir/%repo/
%_pkgconfigdir/%repo.pc
%_K5lib/libkwin-xcb.so

%changelog
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
