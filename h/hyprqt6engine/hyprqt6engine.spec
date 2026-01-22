Name: hyprqt6engine
Version: 0.1.0
Release: alt2
License: BSD-3-Clause

Summary: QT6 Theme Provider for Hyprland

Group: Graphical desktop/Other

Url: https://github.com/hyprwm/hyprqt6engine
Vcs: https://github.com/hyprwm/hyprqt6engine.git

ExcludeArch: %ix86
Source: %name-%version.tar
Patch1: alt-qt-6.10.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: clang libstdc++-devel

BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(hyprutils)

BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kf6-kiconthemes-devel

%description
%summary.

%prep
%setup
%patch1 -p1

%build
%cmake -DCMAKE_CXX_COMPILER=clang++
%cmake_build 

%install
%cmake_install

%files
%_libdir/libhyprqt6engine-common.so
%_qt6_plugindir/platformthemes/libhyprqt6engine.so
%_qt6_plugindir/styles/libhypr-style.so

%changelog
* Thu Jan 22 2026 Sergey V Turchin <zerg@altlinux.org> 0.1.0-alt2
- fix to build with Qt-6.10

* Wed Oct 29 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.0-alt1
- Initial build
