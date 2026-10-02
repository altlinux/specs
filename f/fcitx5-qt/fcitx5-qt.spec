%define _unpackaged_files_terminate_build 1
%define _libexecdir %prefix/libexec
%global __provides_exclude_from ^%_libdir/(fcitx5|qt5)/.*\\.so$
%global build_qt6 1

Name: fcitx5-qt
Version: 5.1.16
Release: alt1

Summary: Qt library and IM module for fcitx5
License: LGPLv2+ and BSD
Group: Graphical desktop/Other

Url: https://github.com/fcitx/fcitx5-qt
Vcs: https://github.com/fcitx/fcitx5-qt

Source: %name-%version.tar.zst

Requires: %name-module = %EVR
Requires: %name-libfcitx5qtdbus = %EVR
Requires: %name-libfcitx5qt5widgets = %EVR
#Requires:       ((fcitx5-qt6%{?_isa} = %EVR) if qt6-qtbase)

BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: libX11-devel
BuildRequires: libxcb-devel
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: gnupg2
BuildRequires: ctest
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: python3-module-ninja_syntax
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(Fcitx5Utils)
BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: gettext-tools
BuildRequires: qt5-base-devel
%if %build_qt6
BuildRequires: pkgconfig(Qt6)
BuildRequires: qt6-base-devel
BuildRequires: qt6-wayland-devel
%endif

%description
Qt library and IM module for fcitx5.

%package module
Group: Graphical desktop/Other
Summary: Provides seperately modules for fcitx5-qt

%description module
This package provides im-modules that can be installed seperately
from fcitx5-qt.

%package libfcitx5qtdbus
Group: Graphical desktop/Other
Summary: Provides libFcitx5Qt5DBusAddons for fcitx5

%description libfcitx5qtdbus
This package provides libFcitx5Qt5DBusAddons for fcitx5.

%package libfcitx5qt5widgets
Group: Graphical desktop/Other
Summary: Provide libFcitx5Qt5WidgetsAddons for fcitx5

%description libfcitx5qt5widgets
This package provides libFcitx5Qt5WidgetsAddons for fcitx5.

%if %build_qt6
%package -n fcitx5-qt6-libfcitx5qt6widgets
Group: Graphical desktop/Other
Summary: Provide libFcitx5Qt6WidgetsAddons for fcitx5

%description -n fcitx5-qt6-libfcitx5qt6widgets
This package provides libFcitx5Qt6WidgetsAddons for fcitx5.

%package -n fcitx5-qt6
Group: Graphical desktop/Other
Summary: Qt 6 support for fcitx5
# This needs to be rebuilt on every minor Qt6 version bump

%description -n fcitx5-qt6
Qt6 library and IM module for fcitx5.
%endif

%package devel
Group: Graphical desktop/Other
Summary: Development files for %name
Requires: %name = %version-%release
# fedora autoprovides, not implemented in ALT
Provides: cmake(Fcitx5Qt5WidgetsAddons)

%description devel
Development files for %name

%prep
%setup

%build
%fedora_v2_cmake -GNinja -DENABLE_QT4=False \
%if %build_qt6
    -DENABLE_QT6=True
%else
    -DENABLE_QT6=False
%endif
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install

%find_lang %name

%files -f %name.lang
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt
%doc README.md
%_libexecdir/fcitx5-qt5-gui-wrapper
#%%_libdir/fcitx5/qt5/
%_datadir/applications/org.fcitx.fcitx5-qt5-gui-wrapper.desktop

%if %build_qt6
%files -n fcitx5-qt6
%_libexecdir/fcitx5-qt6-gui-wrapper
%_libdir/fcitx5/qt6/
%_datadir/applications/org.fcitx.fcitx5-qt6-gui-wrapper.desktop
%_qt6_plugindir/platforminputcontexts/libfcitx5platforminputcontextplugin.so
%_bindir/fcitx5-qt6-immodule-probing
%_libdir/libFcitx5Qt6DBusAddons.so.1
%_libdir/libFcitx5Qt6DBusAddons.so.*.*
%endif

%files devel
%_includedir/Fcitx5Qt5/
%_libdir/cmake/Fcitx5Qt5*
%_libdir/libFcitx5Qt5DBusAddons.so
%_libdir/libFcitx5Qt5WidgetsAddons.so
%if %build_qt6
%_libdir/libFcitx5Qt6DBusAddons.so
%_libdir/libFcitx5Qt6WidgetsAddons.so
%_libdir/cmake/Fcitx5Qt6*
%_includedir/Fcitx5Qt6/
%endif

%files module
%_qt5_plugindir/platforminputcontexts/libfcitx5platforminputcontextplugin.so
%_bindir/fcitx5-qt5-immodule-probing

%files libfcitx5qt5widgets
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt
%_libdir/libFcitx5Qt5WidgetsAddons.so.2
%_libdir/libFcitx5Qt5WidgetsAddons.so.*.*

%files libfcitx5qtdbus
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt
%_libdir/libFcitx5Qt5DBusAddons.so.1
%_libdir/libFcitx5Qt5DBusAddons.so.*.*

%if %build_qt6
%files -n fcitx5-qt6-libfcitx5qt6widgets
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt
%_libdir/libFcitx5Qt6WidgetsAddons.so.2
%_libdir/libFcitx5Qt6WidgetsAddons.so.*.*
%endif

%changelog
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

