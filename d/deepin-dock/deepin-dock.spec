%global repo dde-dock

%def_disable clang

Name: deepin-dock
Version: 5.3.0.49
Release: alt1
Summary: Deepin desktop-environment - Dock module
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-dock
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang11.0-devel
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake libdbusmenu-qt5-devel deepin-network-utils-devel dtk5-widget-devel deepin-qt-dbus-factory-devel >= 2.0 gsettings-qt-devel libgtk+2-devel qt5-base-devel qt5-x11extras-devel qt5-svg-devel libX11-devel libXtst-devel libXext-devel libxcb-devel libxcbutil-icccm-devel libxcbutil-image-devel qt5-linguist
Requires: libdbusmenu-qt52 libddenetworkutils libdframeworkdbus2 libxcb libxcbutil-icccm libxcbutil-image

%description
Deepin desktop-environment - Dock module.

%package devel
Summary: Development package for %name
Group: Graphical desktop/Other

%description devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version

sed -i '/TARGETS/s|lib|%_lib|' plugins/*/CMakeLists.txt
sed -E '35d;/dpkg-architecture|EXIT/d' CMakeLists.txt
sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
sed -i 's|/usr/lib/deepin-daemon|/usr/libexec/deepin-daemon|' unittest/dock_unit_test.cpp \
                                                              plugins/show-desktop/showdesktopplugin.cpp \
                                                              frame/panel/mainpanelcontrol.cpp
sed -i 's|/lib|/%_lib|' frame/controller/dockpluginscontroller.cpp \
                        plugins/tray/system-trays/systemtrayscontroller.cpp \
                        plugins/plugin-guide/plugins-developer-guide.md

sed -i 's|/usr/lib/dde-dock/plugins|%{_libdir}/dde-dock/plugins|' plugins/plugin-guide/plugins-developer-guide.md
sed -i 's|local/lib/dde-dock/plugins|local/%{_lib}/dde-dock/plugins|' plugins/plugin-guide/plugins-developer-guide.md

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif

%cmake \
    -GNinja \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DARCHITECTURE=%_arch
%ninja_build -C BUILD

%install
%ninja_install -C BUILD

%files
%doc LICENSE
%_sysconfdir/%repo/
%_bindir/%repo
%_libdir/%repo/
%_datadir/%repo/
%_datadir/polkit-1/actions/com.deepin.dde.dock.overlay.policy
%_datadir/glib-2.0/schemas/com.deepin.dde.dock.module.gschema.xml

%files devel
%_includedir/%repo/
%_pkgconfigdir/%repo.pc
%_libdir/cmake/DdeDock/DdeDockConfig.cmake

%changelog
* Mon Nov 09 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.49-alt1
- New version (5.3.0.49) with rpmgs script.
- Fixed panel plugins.
- Added requires.
- Removed patches.

* Wed Oct 14 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.27-alt1
- New version (5.3.0.27) with rpmgs script.

* Mon Oct 12 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.14-alt1
- New version (5.2.0.14) with rpmgs script.

* Wed Jul 29 2020 Leontiy Volodin <lvol@altlinux.org> 5.1.0.11-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
