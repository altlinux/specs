%define repo dde-dock

%def_without clang

Name: deepin-dock
Version: 6.0.37
Release: alt1
Epoch: 1

Summary: Deepin desktop-environment - Dock module

License: LGPL-3.0-or-later and GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-dock

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch
Patch1: deepin-dock-6.0.37-upstream-link-Xcursor-for-shutdown-plugin.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt5
%if_with clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif
# Qt5::XkbCommonSupport references the file /usr/lib64/libQt5XkbCommonSupport.a
# Automatically added by buildreq on Mon Oct 23 2023
# optimized out: alt-os-release bash5 bashrc cmake cmake-modules gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libXcursor-devel libXext-devel libXi-devel libXtst-devel libdbusmenu-qt52 libdouble-conversion3 libdtkcore-devel libdtkgui-devel libglvnd-devel libgpg-error libgsettings-qt libp11-kit libdqt5-concurrent libdqt5-core libdqt5-dbus libdqt5-gui libdqt5-network libdqt5-printsupport libdqt5-svg libdqt5-waylandclient libdqt5-widgets libdqt5-x11extras libdqt5-xml libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-egl libwayland-server-devel libxcb-devel libxcbutil-icccm libxcbutil-image libxkbcommon-devel pkg-config python3 python3-base dqt5-base-common dqt5-base-devel sh5 wayland-devel xorg-proto-devel
BuildRequires: dtk6-common-devel dwayland-devel extra-cmake-modules gsettings-qt-devel libXres-devel libdbusmenu-qt5-devel libdtkwidget-devel libgio-devel libwayland-cursor-devel libwayland-egl-devel libxcbutil-icccm-devel libxcbutil-image-devel dqt5-base-devel-static dqt5-svg-devel dqt5-tools dqt5-wayland-devel dqt5-x11extras-devel libxkbcommon-devel

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
sed -i 's|/usr/lib|%_libdir|' \
    plugins/pluginmanager/pluginmanager.cpp \
    frame/controller/quicksettingcontroller.cpp \
    tests/controller/ut_dockplugincontroller.cpp

%build
export PATH=%_dqt5_bindir:$PATH
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
%endif

%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=NO \
    -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
    -DARCHITECTURE=%_arch \
    -DCMAKE_INSTALL_LIBDIR=%_lib \
    -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
    -DDOCK_TRAY_USE_NATIVE_POPUP=YES \
    -DCMAKE_INSTALL_FULL_LIBDIR=%_libdir \
    -DCMAKE_INSTALL_FULL_INCLUDEDIR=%_includedir
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%find_lang --with-qt %repo

%files -f %repo.lang
%doc LICENSE README.md
%_bindir/%repo
%_libdir/%repo/
%dir %_datadir/%repo/
%_datadir/%repo/window_patterns.json
%dir %_datadir/%repo/translations/
%_datadir/%repo/translations/dde-dock.qm
%_datadir/%repo/translations/dde-dock_es_419.qm
%_datadir/%repo/translations/dde-dock_ky@Arab.qm
%_datadir/polkit-1/actions/org.deepin.dde.dock.overlay.policy
%_datadir/glib-2.0/schemas/com.deepin.dde.dock.module.gschema.xml
%dir %_sysconfdir/%repo/
%dir %_sysconfdir/%repo/indicator/
%_sysconfdir/%repo/indicator/keybord_layout.json
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/dde-dock/
%_datadir/dsg/configs/dde-dock/com.deepin.dde.dock.json
%_datadir/dsg/configs/dde-dock/org.deepin.dde.dock.power.json

%files devel
%doc plugins/plugin-guide
%_includedir/%repo/
%_pkgconfigdir/%repo.pc
%_libdir/cmake/DdeDock/DdeDockConfig.cmake

%changelog
* Thu May 16 2024 Leontiy Volodin <lvol@altlinux.org> 1:6.0.37-alt1
- New version 6.0.37.
- Built via separate qt5 instead system (ALT #48138).

* Thu Mar 21 2024 Leontiy Volodin <lvol@altlinux.org> 1:6.0.36-alt1
- New version 6.0.36.

* Tue Mar 05 2024 Leontiy Volodin <lvol@altlinux.org> 1:6.0.35.0.3.3eb9-alt1
- New version 6.0.35-3-g3eb95284.
- No more needed libqt5-core = %%_qt5_version.

* Fri Jan 19 2024 Leontiy Volodin <lvol@altlinux.org> 1:6.0.27-alt2
- Requires: libqt5-core = %%_qt5_version.

* Tue Jan 16 2024 Leontiy Volodin <lvol@altlinux.org> 1:6.0.27-alt1
- New version 6.0.27.
- Updated license tag.

* Mon Dec 04 2023 Leontiy Volodin <lvol@altlinux.org> 1:6.0.24-alt1
- New version 6.0.24.
- Removed obsolete patch.
- Cleanup spec and BRs.

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
