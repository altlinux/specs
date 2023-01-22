%def_disable clang

%define _cmake__builddir BUILD

Name: deepin-kwin2
Version: 5.24.3.1.9
Release: alt1

Summary: New KWin configuration for Deepin Desktop Environment

License: GPL-2.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-kwin

Source: %url/archive/%version/deepin-kwin-%version.tar.gz

Requires: kf5-kglobalaccel

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-kf5 rpm-build-ninja rpm-build-python3
BuildRequires: cmake extra-cmake-modules plasma5-kdecoration-devel qt5-x11extras-devel qt5-declarative-devel qt5-tools-devel kf5-kwindowsystem-devel kf5-kcoreaddons-devel dtk5-gui-devel kf5-kconfig-devel kf5-kglobalaccel-devel kf5-ki18n-devel gsettings-qt-devel plasma5-kwin-devel plasma5-kwayland-server-devel kf5-kwayland-devel qt5-sensors-devel qt5-script-devel libqaccessibilityclient-qt5-devel
BuildRequires: zlib-devel bzlib-devel libpng-devel libpcre-devel libbrotli-devel libuuid-devel libexpat-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcrash-devel kf5-kinit-devel kf5-knotifications-devel kf5-kpackage-devel kf5-kwidgetsaddons-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kservice-devel kf5-plasma-framework-devel kf5-kcompletion-devel kf5-kdeclarative-devel kf5-kcmutils-devel kf5-kio-devel kf5-ktextwidgets-devel kf5-knewstuff-devel kf5-kxmlgui-devel plasma5-kscreenlocker-devel kf5-kactivities-devel kf5-kdoctools-devel plasma5-breeze-devel kf5-kirigami-devel kf5-krunner-devel
BuildRequires: libwayland-client-devel libwayland-cursor-devel libwayland-egl-devel wayland-devel libwayland-server-devel pipewire-libs-devel libwayland-server dwayland-devel
BuildRequires: libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-cursor-devel libxcbutil-devel
BuildRequires: qt5-multimedia-devel xorg-xwayland qt5-virtualkeyboard xorg-xwayland-devel wayland-protocols
BuildRequires: libdrm-devel libgbm-devel libcap-devel libxkbcommon-devel libinput-devel libudev-devel liblcms2-devel
# libQt5XkbCommonSupport.a
BuildRequires: qt5-base-devel-static

%description
The package provides a kwin configuration that used as the new WM for Deepin
Desktop Environment.

%package -n libdeepin-kwinxrenderutils5
Summary: Library for deepin-kwin
Group: System/Libraries

%description -n libdeepin-kwinxrenderutils5
The package provides libdeepin-kwinxrenderutils library for deepin-kwin.

%package -n libdeepin-kwineffects5
Summary: Library for deepin-kwin
Group: System/Libraries

%description -n libdeepin-kwineffects5
The package provides libdeepin-kwineffects library for deepin-kwin.

%package -n libdeepin-kwinglutils5
Summary: Library for deepin-kwin
Group: System/Libraries

%description -n libdeepin-kwinglutils5
The package provides libdeepin-kwinglutils library for deepin-kwin.

%package -n libdeepin-kcmkwincommon5
Summary: Library for deepin-kwin
Group: System/Libraries

%description -n libdeepin-kcmkwincommon5
The package provides libdeepin-kcmkwincommon library for deepin-kwin.

%package -n libdeepin-kwin5
Summary: Library for deepin-kwin
Group: System/Libraries

%description -n libdeepin-kwin5
The package provides libdeepin-kwin library for deepin-kwin.

%package devel
Summary: Development package for deepin-kwin
Group: Graphical desktop/Other

%description devel
The package provides development files for deepin-kwin.

%package doc
Summary: Docs for deepin-kwin
Group: Documentation

%description doc
The package provides documentation for deepin-kwin.

%prep
%setup -n deepin-kwin-%version
sed -i 's|Wayland::Server|wayland-server|' \
  src/CMakeLists.txt

%build
export PATH=%_qt5_bindir:$PATH
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif

%K5cmake \
    -GNinja \
    -DCMAKE_PREFIX_PATH=%_qt5_prefix \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DKWIN_VERSION=%get_version plasma5-kwin-devel \
%nil
cmake --build BUILD -j%__nprocs

%install
%cmake_install
# Fix library links.
ln -sf %_libdir/libdeepin-kcmkwincommon.so.5 \
      %buildroot%_libdir/libdeepin-kcmkwincommon.so
ln -sf %_libdir/libdeepin-kwin.so.5 %buildroot%_libdir/libdeepin-kwin.so

%files
%doc README.md
# binaries and scripts
%_K5bin/deepin-kwin_x11
%_K5bin/deepin-kwin_wayland*
%_prefix/libexec/deepin-kwin*
# icons
%_K5icon/hicolor/*/apps/deepin-kwin*
# desktop files
%_datadir/kservicetypes5/deepin-kwin*.desktop
%_datadir/kservices5/deepin*.desktop
%_datadir/krunner/dbusplugins/deepin-kwin-runner-windows.desktop
%dir %_datadir/kservices5/deepin-kwin/
%_datadir/kservices5/deepin-kwin/kwin4_decoration_qml_plastik.desktop
%_K5xdgapp/org.kde.deepin-kwin_rules_dialog.desktop
# services
%_prefix/lib/systemd/user/deepin-kwin*.service
# other data files
%_datadir/kconf_update/deepin-kwin*
%_datadir/qlogging-categories5/org_kde_deepin-kwin.categories
%_datadir/knsrcfiles/deepin*.knsrc
%_datadir/knotifications5/deepin-kwin.notifyrc
%dir %_datadir/deepin-kwin/
%_datadir/deepin-kwin/*
%_datadir/kpackage/kcms/deepin-kcm*
%_K5cfg/deepin*.kcfg
%_K5dbus_iface/org.deepin.kwin*.xml
%_K5dbus_iface/org.deepin.KWin*.xml
%_datadir/translations/popupmenu/popupmenu*.qm
%_datadir/locale/*/LC_MESSAGES/deepin-k*.mo
# libs and plugins
%_libdir/kconf_update_bin/deepin-kwin5_update_default_rules
%dir %_libdir/qt5/plugins/deepin-kwin/
%dir %_libdir/qt5/plugins/deepin-kwin/effects/
%dir %_libdir/qt5/plugins/deepin-kwin/effects/configs/
%dir %_libdir/qt5/plugins/deepin-kwin/plugins/
%_libdir/qt5/plugins/deepin-kwin/effects/configs/*.so
%_libdir/qt5/plugins/deepin-kwin/plugins/*.so
%_libdir/qt5/plugins/deepin*.so
%_libdir/qt5/plugins/kcms/deepin-kcm*.so
%_libdir/qt5/plugins/org.kde.deepin-kwin*
%_libdir/qt5/plugins/org.kde.kdecoration2/deepin*.so
%_libdir/qt5/plugins/kpackage/packagestructure/deepin-kwin*.so
%dir %_libdir/qt5/qml/org/deepin/
%dir %_libdir/qt5/qml/org/deepin/kwin/
%dir %_libdir/qt5/qml/org/deepin/kwin/decoration/
%_libdir/qt5/qml/org/deepin/kwin/decoration/libdecorationplugin.so
%_libdir/qt5/qml/org/deepin/kwin/decoration/*.qml
%_libdir/qt5/qml/org/deepin/kwin/decoration/qmldir
%dir %_libdir/qt5/qml/org/kde/deepin-kwin/
%dir %_libdir/qt5/qml/org/kde/deepin-kwin/decorations/
%dir %_libdir/qt5/qml/org/kde/deepin-kwin/decorations/plastik/
%dir %_libdir/qt5/qml/org/kde/deepin-kwin/private/
%dir %_libdir/qt5/qml/org/kde/deepin-kwin/private/kdecoration/
%_libdir/qt5/qml/org/kde/deepin-kwin/decorations/plastik/libplastikplugin.so
%_libdir/qt5/qml/org/kde/deepin-kwin/decorations/plastik/qmldir
%_libdir/qt5/qml/org/kde/deepin-kwin/private/kdecoration/libkdecorationprivatedeclarative.so
%_libdir/qt5/qml/org/kde/deepin-kwin/private/kdecoration/qmldir

%files -n libdeepin-kwinxrenderutils5
%_libdir/libdeepin-kwinxrenderutils.so.*

%files -n libdeepin-kwineffects5
%_libdir/libdeepin-kwineffects.so.*

%files -n libdeepin-kwinglutils5
%_libdir/libdeepin-kwinglutils.so.*

%files -n libdeepin-kcmkwincommon5
%_libdir/libdeepin-kcmkwincommon.so.5*

%files -n libdeepin-kwin5
%_libdir/libdeepin-kwin.so.5*

%files devel
%doc CONTRIBUTING.md
%_libdir/libdeepin-kwinxrenderutils.so
%_libdir/libdeepin-kwineffects.so
%_libdir/libdeepin-kwinglutils.so
%_libdir/libdeepin-kcmkwincommon.so
%_libdir/libdeepin-kwin.so
%_includedir/deepin_kwin*.h
%dir %_libdir/cmake/DeepinKWinEffects/
%dir %_libdir/cmake/DeepinKWinDBusInterface/
%_libdir/cmake/DeepinKWinEffects/KWinEffects*.cmake
%_libdir/cmake/DeepinKWinDBusInterface/KWinDBusInterfaceConfig.cmake

%files doc
%dir %_K5doc/*/dcontrol/
%_K5doc/*/dcontrol/*

%changelog
* Sun Jan 22 2023 Leontiy Volodin <lvol@altlinux.org> 5.24.3.1.9-alt1
- Initial build for ALT Sisyphus (Closes: #41379, #41154).
