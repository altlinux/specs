%global repo dde-dock

%def_disable clang

Name: deepin-dock
Version: 5.3.64
Release: alt1
Summary: Deepin desktop-environment - Dock module
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-dock
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: deepin-dock-5.3.64-alt-fix-underlinked.patch

%if_enabled clang
BuildRequires(pre): clang11.0-devel
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake
BuildRequires: deepin-network-utils-devel
BuildRequires: dtk5-widget-devel
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: gsettings-qt-devel
BuildRequires: libgtk+2-devel
BuildRequires: libdbusmenu-qt5-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-linguist
BuildRequires: libX11-devel
BuildRequires: libXtst-devel
BuildRequires: libXext-devel
BuildRequires: libxcb-devel
BuildRequires: libxcbutil-icccm-devel
BuildRequires: libxcbutil-image-devel
BuildRequires: libgtest-devel
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
%patch -p2

sed -i '/TARGETS/s|lib|%_lib|' plugins/*/CMakeLists.txt
sed -E '35d;/dpkg-architecture|EXIT/d;44d' CMakeLists.txt
sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
sed -i 's|/usr/lib/deepin-daemon|/usr/libexec/deepin-daemon|' \
    unittest/dock_unit_test.cpp \
    plugins/show-desktop/showdesktopplugin.cpp \
    frame/panel/mainpanelcontrol.cpp
sed -i 's|/lib|/%_lib|' \
    frame/controller/dockpluginscontroller.cpp \
    plugins/tray/system-trays/systemtrayscontroller.cpp \
    plugins/plugin-guide/plugins-developer-guide.md

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif

%cmake_insource \
    -GNinja \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DARCHITECTURE=%_arch
%ninja_build

%install
%ninja_install

%files
%doc LICENSE
%_sysconfdir/%repo/
%_bindir/%repo
%_libdir/%repo/
%_datadir/%repo/
%_datadir/polkit-1/actions/com.deepin.dde.dock.overlay.policy
%_datadir/glib-2.0/schemas/com.deepin.dde.dock.module.gschema.xml

%files devel
%doc plugins/plugin-guide
%_includedir/%repo/
%_pkgconfigdir/%repo.pc
%_libdir/cmake/DdeDock/DdeDockConfig.cmake

%changelog
* Mon Jan 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.64-alt1
- New version (5.3.64) with rpmgs script.

* Tue Jan 12 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.0.54-alt1
- New version (5.3.0.54) with rpmgs script.

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
