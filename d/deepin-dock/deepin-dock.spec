%global repo dde-dock

%def_disable clang

Name: deepin-dock
Version: 5.6.2
Release: alt2
Epoch: 1
Summary: Deepin desktop-environment - Dock module
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-dock
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: 0001-fix-blur-icon-729.patch
Patch1: 0001-fix-remove-the-permission-of-x-in-source.patch
Patch2: 0001-chore-cleanup-code.patch
Patch3: 0001-fix-bluetooth-switch-button-735.patch
Patch4: 0001-fix-magic-lamp-under-wayland.patch
Patch5: 0001-fix-DBus-can-not-be-notified.patch
Patch6: 0001-fix-inserting-flash-drive.patch
Patch7: 0001-chore-repair-the-failure-of-compilation.patch
Patch8: 0001-fix-left-key-to-pop-the-menu-and-get-stuck.patch
Patch9: deepin-dock-5.6.2-alt-fix-undefined-elfs.patch

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
BuildRequires: dtk5-common-devel
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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
sed -i '/TARGETS/s|lib/|%_lib/|' plugins/*/CMakeLists.txt
sed -i 's|/usr/lib|%_libdir|' \
    frame/controller/dockpluginscontroller.cpp \
    plugins/tray/system-trays/systemtrayscontroller.cpp \
    tests/controller/ut_dockplugincontroller.cpp
# Hide broken options.
sed -i 's| "Suspend", "Hibernate", "Lock",||' \
    configs/org.deepin.dde.dock.plugin.power.json

%build
export PATH=%_qt5_bindir:$PATH
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif

%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DARCHITECTURE=%_arch \
    -DCMAKE_INSTALL_FULL_LIBDIR=%_libdir \
    -DCMAKE_INSTALL_FULL_INCLUDEDIR=%_includedir
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

mkdir -p %buildroot%_sysconfdir/%repo/indicator/
mv -f %buildroot/usr/etc/dde-dock/indicator/keybord_layout.json %buildroot%_sysconfdir/%repo/indicator/

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
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.control-center/
%_datadir/dsg/configs/org.deepin.dde.control-center/org.deepin.dde.dock.plugin.json
%dir %_datadir/dsg/configs/org.deepin.dde.dock/
%_datadir/dsg/configs/org.deepin.dde.dock/org.deepin.dde.dock.json
%_datadir/dsg/configs/org.deepin.dde.dock/org.deepin.dde.dock.plugin.power.json
%_libdir/dde-control-center/modules/libdcc-dock-plugin.so

%files devel
%doc plugins/plugin-guide
%_includedir/%repo/
%_pkgconfigdir/%repo.pc
%_libdir/cmake/DdeDock/DdeDockConfig.cmake

%changelog
* Fri Jan 13 2023 Leontiy Volodin <lvol@altlinux.org> 1:5.6.2-alt2
- Applied patches by upstream.
- Fixed build with dtk5-common.
- Fixed undefined elfs.

* Wed Dec 14 2022 Leontiy Volodin <lvol@altlinux.org> 1:5.6.2-alt1
- 5.6.2.

* Tue Nov 15 2022 Leontiy Volodin <lvol@altlinux.org> 1:5.5.73-alt1
- 5.5.73.
- Fixed deepin-network-core.

* Fri Jun 03 2022 Leontiy Volodin <lvol@altlinux.org> 1:5.5.9.1-alt2
- Fixed build with new dtkcommon.

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
