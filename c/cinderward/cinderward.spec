%define _unpackaged_files_terminate_build 1

Name: cinderward
Version: 0.0.4
Release: alt1

Summary: A simple, no-nonsense, init-agnostic, Wayland-friendly GUI for firewalld
License: BSD-3-clause
Group: System/Configuration/Networking
Url: https://github.com/Nitrux/cinderward

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: libmauikit-devel

Requires: libmauikit
Requires: libqt6-quickcontrols2basic
Requires: libqt6-quicklayouts
Requires: libqt6-qmlcore
Requires: libqt6-quickeffects
Requires: libqt6-quickshapes

Requires: firewalld

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%_bindir/cinderward
%_desktopdir/org.nitrux.cinderward.desktop

%changelog
* Tue May 19 2026 Nikolay Strelkov <snk@altlinux.org> 0.0.4-alt1
- New version 0.0.4.

* Sat Jan 10 2026 Nikolay Strelkov <snk@altlinux.org> 0.0.3-alt1
- Initial build for Sisyphus
