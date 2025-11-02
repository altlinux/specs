Name: hyprqt6engine
Version: 0.1.0
Release: alt1
License: BSD-3-Clause

Summary: QT6 Theme Provider for Hyprland

Group: Graphical desktop/Other

Url: https://github.com/hyprwm/hyprqt6engine
Vcs: https://github.com/hyprwm/hyprqt6engine.git

ExcludeArch: %ix86
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: clang libstdc++-devel

BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(hyprutils)

BuildRequires: pkgconfig(Qt6)
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kf6-kiconthemes-devel

%description
%summary.

%prep
%setup

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
* Wed Oct 29 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.0-alt1
- Initial build
