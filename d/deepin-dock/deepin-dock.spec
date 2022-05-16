%global repo dde-dock

%def_disable clang

Name: deepin-dock
Version: 5.5.9.1
Release: alt1
Epoch: 1
Summary: Deepin desktop-environment - Dock module
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-dock
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: deepin-dock-5.5.9.1-upstream-fix-undefined-elfs.patch

%if_enabled clang
BuildRequires(pre): clang-devel
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake
BuildRequires: deepin-network-utils-devel
BuildRequires: deepin-control-center
BuildRequires: deepin-control-center-devel
BuildRequires: dtk5-widget-devel
BuildRequires: deepin-qt-dbus-factory-devel
BuildRequires: gsettings-qt-devel
BuildRequires: libgtk+2-devel
BuildRequires: libdbusmenu-qt5-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-tools-devel
BuildRequires: libX11-devel
BuildRequires: libXtst-devel
BuildRequires: libXext-devel
BuildRequires: libxcb-devel
BuildRequires: libxcbutil-icccm-devel
BuildRequires: libxcbutil-image-devel
BuildRequires: libgtest-devel
BuildRequires: libgmock-devel
BuildRequires: dtk5-common
# Requires: libdbusmenu-qt52 libddenetworkutils libdframeworkdbus2 libxcb libxcbutil-icccm libxcbutil-image

%description
Deepin desktop-environment - Dock module.

%package devel
Summary: Development package for %name
Group: Graphical desktop/Other

%description devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version
%patch -p1

sed -i '/TARGETS/s|lib/|%_lib/|' plugins/*/CMakeLists.txt
sed -i 's|${prefix}/lib/@HOST_MULTIARCH@|%_libdir|' dde-dock.pc.in
sed -i 's|/usr/lib|%_libdir|' \
    frame/controller/dockpluginscontroller.cpp \
    plugins/tray/system-trays/systemtrayscontroller.cpp

%build
export PATH=%_qt5_bindir:$PATH
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%define optflags_lto %nil
%endif

%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DARCHITECTURE=%_arch
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/%repo
%_libdir/%repo/
%_datadir/%repo/
%_datadir/dcc-dock-plugin/
%_datadir/polkit-1/actions/com.deepin.dde.dock.overlay.policy
%_datadir/glib-2.0/schemas/com.deepin.dde.dock.module.gschema.xml
%dir %_sysconfdir/%repo/
%dir %_sysconfdir/%repo/indicator/
%_sysconfdir/%repo/indicator/keybord_layout.json
%dir %_datadir/dsg/
%dir %_datadir/dsg/apps/
%dir %_datadir/dsg/apps/dde-control-center/
%dir %_datadir/dsg/apps/dde-control-center/configs/
%_datadir/dsg/apps/dde-control-center/configs/dde.dock.plugin.dconfig.json
%dir %_datadir/dsg/apps/dde-dock/
%dir %_datadir/dsg/apps/dde-dock/configs/
%_datadir/dsg/apps/dde-dock/configs/com.deepin.dde.dock.dconfig.json
%_libdir/dde-control-center/modules/libdcc-dock-plugin.so

%files devel
%doc plugins/plugin-guide
%_includedir/%repo/
%_pkgconfigdir/%repo.pc
%_libdir/cmake/DdeDock/DdeDockConfig.cmake

%changelog
* Mon May 16 2022 Leontiy Volodin <lvol@altlinux.org> 1:5.5.9.1-alt1
- 5.5.9.1.
- Upstream:
  + Fixed window preview.
  + Fixed undefined elfs.

* Thu May 12 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.27-alt1
- New version (5.5.27).

* Thu Apr 21 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.12-alt1
- New version (5.5.12).

* Mon Feb 14 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.9-alt1
- New version (5.5.9).
- Changed licence tag.

* Mon Feb 07 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.69.1-alt1
- New version (5.4.69.1).

* Fri Aug 20 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.39-alt1
- New version (5.4.39).

* Wed Jul 14 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.28-alt1
- New version (5.4.28).

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.10-alt1
- New version (5.4.10) with rpmgs script.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.7-alt1
- New version (5.4.7) with rpmgs script.

* Wed Mar 24 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.4-alt1
- New version (5.4.4) with rpmgs script.

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
