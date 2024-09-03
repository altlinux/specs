%def_without clang

%define _cmake__builddir BUILD

Name: deepin-kwin2
Version: 5.25.18
Release: alt2
%K5init no_altplace

Summary: New KWin configuration for Deepin Desktop Environment

License: GPL-2.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-kwin

Source: %url/archive/%version/deepin-kwin-%version.tar.gz
Patch: %name-%version-%release.patch

Provides: deepin-kwin = %version-%release
Obsoletes: deepin-kwin < %version-%release

BuildRequires(pre): rpm-build-kf5 rpm-build-ninja rpm-build-python3 rpm-macros-qt5
# qt5-base-devel-static for libQt5XkbCommonSupport.a
# Automatically added by buildreq on Thu Oct 26 2023
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl fontconfig-devel gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gst-libav gst-plugins-bad1.0 gst-plugins-base1.0 gst-plugins-good1.0 gst-plugins-ugly1.0 gstreamer1.0 gtk4-update-icon-cache hwdata kf5-attica-devel kf5-kauth-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-common kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdoctools kf5-kglobalaccel-devel kf5-ki18n-devel kf5-kjobwidgets-common kf5-kservice-devel kf5-kwidgetsaddons-common kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-plasma-framework-common kf5-plasma-framework-devel kf5-sonnet-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libcap-utils libdbusmenu-qt52 libdouble-conversion3 libepoxy-devel libfreetype-devel libglvnd-devel libgpg-error libgst-plugins1.0 libp11-kit libqaccessibilityclient-qt5 libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-printsupport libqt5-qml libqt5-qmlmodels libqt5-qmlworkerscript libqt5-quick libqt5-quickwidgets libqt5-sql libqt5-svg libqt5-test libqt5-texttospeech libqt5-waylandclient libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libudev-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-egl libwayland-server libxcb-devel libxcb-render-util libxcbutil-cursor libxcbutil-icccm libxcbutil-image libxcbutil-keysyms libxcbutil-keysyms-devel libxkbcommon-devel libxkbfile-devel pipewire-libs pkg-config python3 python3-base python3-dev python3-module-setuptools qt5-base-common qt5-base-devel qt5-declarative-devel qt5-svg-devel qt5-tools sh5 shared-mime-info wayland-devel xml-common xml-utils xorg-proto-devel xorg-xf86miscproto-devel zlib-devel
BuildRequires: dwayland-devel extra-cmake-modules kf5-kactivities-devel kf5-kcmutils-devel kf5-kdeclarative-devel kf5-kdoctools-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kirigami-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kpackage-devel kf5-krunner-devel kf5-ktextwidgets-devel libcap-devel libdrm-devel libgbm-devel libinput-devel liblcms2-devel libqaccessibilityclient-qt5-devel libqtxdg libwayland-cursor-devel libwayland-egl-devel libwayland-server-devel libxcbutil-cursor-devel libxcbutil-devel libxcbutil-icccm-devel libxcbutil-image-devel pipewire-libs-devel plasma5-kdecoration-devel plasma5-kscreenlocker-devel qt5-base-devel-static qt5-tools-devel qt5-x11extras-devel xorg-xwayland-devel
BuildRequires: qt5-quickcontrols xorg-xwayland
%if_with clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif

Requires: kf5-kglobalaccel libqt5-core = %_qt5_version libqt5-gui = %_qt5_version

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
Requires: libqt5-gui = %_qt5_version

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
BuildArch: noarch

%description doc
The package provides documentation for deepin-kwin.

%prep
%setup -n deepin-kwin-%version
%patch -p1

%build
export PATH=%_qt5_bindir:$PATH
%if_with clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif

%K5cmake \
    -GNinja \
    -DCMAKE_PREFIX_PATH=%_qt5_prefix \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
%nil
cmake --build BUILD -j%__nprocs

%install
%cmake_install
# Fix library links.
ln -sf %_libdir/libdeepin-kcmkwincommon.so.5 \
      %buildroot%_libdir/libdeepin-kcmkwincommon.so
ln -sf %_libdir/libdeepin-kwin.so.5 %buildroot%_libdir/libdeepin-kwin.so
# FindLang Policy.
%find_lang --with-qt popupmenu
%find_lang --with-kde dcontrol

%files -f popupmenu.lang
%doc README.md
# binaries and scripts
%_bindir/deepin-kwin_x11
%_bindir/deepin-kwin_wayland*
%_prefix/libexec/deepin-kwin*
# icons
%_iconsdir/hicolor/*/apps/deepin-kwin*
# desktop files
%_datadir/kservicetypes5/deepin-kwin*.desktop
%_datadir/kservices5/deepin*.desktop
%_datadir/krunner/dbusplugins/deepin-kwin-runner-windows.desktop
%dir %_datadir/kservices5/deepin-kwin/
%_datadir/kservices5/deepin-kwin/kwin4_decoration_qml_plastik.desktop
%_desktopdir/org.kde.deepin-kwin_rules_dialog.desktop
# other data files
%_datadir/kconf_update/deepin-kwin*
%_datadir/qlogging-categories5/org_kde_deepin-kwin.categories
%_datadir/knsrcfiles/deepin*.knsrc
%_datadir/knotifications5/deepin-kwin.notifyrc
%dir %_datadir/deepin-kwin/
%_datadir/deepin-kwin/*
%_datadir/kpackage/kcms/deepin-kcm*
%_K5cfg/deepin*.kcfg
%_datadir/dbus-1/interfaces/org.deepin.kwin*.xml
%_datadir/dbus-1/interfaces/org.deepin.KWin*.xml
%_sysconfdir/skel/.config/kglobalshortcutsrc
# do not look by %%find_lang
%dir %_datadir/translations/popupmenu/
%_datadir/translations/popupmenu/popupmenu.qm
%_datadir/locale/*/LC_MESSAGES/deepin-k*.mo
# old deepin-kwin
%_sysconfdir/xdg/*
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.kwin/
%_datadir/dsg/configs/org.deepin.kwin/org.deepin.kwin.splitmenu.display.json
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

%files doc -f dcontrol.lang

%changelog
* Tue Sep 03 2024 Leontiy Volodin <lvol@altlinux.org> 5.25.18-alt2
- NMU: fixed FTBFS.

* Mon Mar 25 2024 Leontiy Volodin <lvol@altlinux.org> 5.25.18-alt1
- New version 5.25.18.
- Set require to current qt5 version.
- Applied FindLang Policy.

* Mon Nov 27 2023 Leontiy Volodin <lvol@altlinux.org> 5.25.11-alt1
- New version 5.25.11.
- Obsoleted deepin-kwin (by upstream).
- Applied fixes from upstream branch.
- Cleanup spec and BRs.

* Thu Mar 09 2023 Leontiy Volodin <lvol@altlinux.org> 5.24.3.1.9-alt2
- Fixed build with plasma 5.27.
- Fixed noarch warnings.

* Sun Jan 22 2023 Leontiy Volodin <lvol@altlinux.org> 5.24.3.1.9-alt1
- Initial build for ALT Sisyphus (Closes: #41379, #41154).
