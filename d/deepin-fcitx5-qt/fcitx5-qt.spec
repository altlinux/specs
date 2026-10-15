%define _unpackaged_files_terminate_build 1
%define _libexecdir %prefix/libexec

Name: deepin-fcitx5-qt
Version: 5.1.16
Release: alt0.dde.1

Summary: Qt library and IM module for fcitx5
License: LGPLv2+ and BSD
Group: Graphical desktop/Other

Url: https://github.com/fcitx/fcitx5-qt
Vcs: https://github.com/fcitx/fcitx5-qt

Source: %name-%version.tar.zst

Requires: %name-module = %EVR
#Requires:       ((fcitx5-dqt6%{?_isa} = %EVR) if dqt6-qtbase)

BuildRequires(pre): rpm-macros-cmake rpm-macros-dqt6
BuildRequires: libX11-devel
BuildRequires: libxcb-devel
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: gnupg2
BuildRequires: ctest
BuildRequires: cmake
BuildRequires: deepin-extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: python3-module-ninja_syntax
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(Fcitx5Utils)
BuildRequires: gettext-tools
BuildRequires: dqt6-base-devel
BuildRequires: dqt6-wayland-devel
BuildRequires: vulkan-headers
BuildRequires: libdqt6-widgets
BuildRequires: libdqt6-concurrent

# find libraries
%add_findprov_lib_path %_dqt6_libdir

%description
%summary.

%package -n fcitx5-dqt6-module
Group: Graphical desktop/Other
Summary: Provides seperately modules for fcitx5-qt
Requires: libdqt6-gui = %_dqt6_version
Requires: libdqt6-waylandclient = %_dqt6_version

%description -n fcitx5-dqt6-module
This package provides im-modules that can be installed seperately
from fcitx5-dqt6.

%package -n fcitx5-dqt6-libfcitx5qt6widgets
Group: Graphical desktop/Other
Summary: Provide libFcitx5Qt6WidgetsAddons for fcitx5

%description -n fcitx5-dqt6-libfcitx5qt6widgets
This package provides libFcitx5Qt6WidgetsAddons for fcitx5.

%package -n fcitx5-dqt6
Group: Graphical desktop/Other
Summary: Qt 6 support for fcitx5

%description -n fcitx5-dqt6
Qt6 library and IM module for fcitx5.

%package -n fcitx5-dqt6-devel
Group: Graphical desktop/Other
Summary: Development files for %name
Requires: fcitx5-dqt6 = %version-%release

%description -n fcitx5-dqt6-devel
Development files for %name

%prep
%setup

%build
export ECM_DIR=%_datadir/DDE-ECM
%DQ6cmake \
    -DCMAKE_INSTALL_LIBDIR=%_dqt6_libdir \
    -DCMAKE_INSTALL_INCLUDEDIR=%_dqt6_headerdir \
    -DCMAKE_INSTALL_BINDIR=%_dqt6_bindir \
    -DCMAKE_INSTALL_LIBEXECDIR=%_dqt6_libexecdir \
    -DCMAKE_INSTALL_DATADIR=%_dqt6_datadir \
    -DENABLE_QT4=False \
    -DENABLE_QT5=False \
    -DENABLE_QT6=True \
#
%DQ6make

%install
%DQ6install_qt
mkdir -p %buildroot%_dqt6_datadir/locale
mv -f %buildroot%_datadir/locale/* %buildroot%_dqt6_datadir/locale

%files -n fcitx5-dqt6
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt
%doc README.md
%_dqt6_libexecdir/fcitx5-qt6-gui-wrapper
%_dqt6_libdir/fcitx5/qt6/
%_dqt6_datadir/applications/org.fcitx.fcitx5-qt6-gui-wrapper.desktop
%dir %_dqt6_datadir/locale/
%_dqt6_datadir/locale/*
%_dqt6_libdir/libFcitx5Qt6DBusAddons.so.1
%_dqt6_libdir/libFcitx5Qt6DBusAddons.so.*.*

%files -n fcitx5-dqt6-devel
%_dqt6_libdatadir/libFcitx5Qt6DBusAddons.so
%_dqt6_libdatadir/libFcitx5Qt6WidgetsAddons.so
%_dqt6_libdir/libFcitx5Qt6DBusAddons.so
%_dqt6_libdir/libFcitx5Qt6WidgetsAddons.so
%_dqt6_libdir/cmake/Fcitx5Qt6*
%_dqt6_headerdir/Fcitx5Qt6/

%files -n fcitx5-dqt6-module
%_bindir/fcitx5-qt6-immodule-probing-dqt6
%_dqt6_plugindir/platforminputcontexts/libfcitx5platforminputcontextplugin.so
%_dqt6_bindir/fcitx5-qt6-immodule-probing

%files -n fcitx5-dqt6-libfcitx5qt6widgets
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt
%_dqt6_libdir/libFcitx5Qt6WidgetsAddons.so.2
%_dqt6_libdir/libFcitx5Qt6WidgetsAddons.so.*.*

%changelog
* Thu Oct 15 2026 Leontiy Volodin <lvol@altlinux.org> 5.1.16-alt0.dde.1
- fork for independent deepin buildings (deepin-fcitx5configtool-plugin).

* Thu Oct 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.1.16-alt1
- 5.1.9 -> 5.1.16 (ALT #60369)
- dropped old patches

* Thu Mar 05 2026 Leontiy Volodin <lvol@altlinux.org> 5.1.9-alt1_5
- NMU: fix build on qt 6.10

* Mon Apr 07 2025 Leontiy Volodin <lvol@altlinux.org> 5.1.9-alt1_4
- update (ALT #52979)

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.1-alt1_3
- update

* Tue Jun 27 2023 Anton Midyukov <antohami@altlinux.org> 5.0.15-alt1_2
- NMU: fix buildrequires

* Wed Sep 28 2022 Igor Vlasenko <viy@altlinux.org> 5.0.15-alt1_1
- new version

