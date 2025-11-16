%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: crystal-dock
Version: 2.15
Release: alt1

Summary: A cool dock (desktop panel) for Linux desktop
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://github.com/dangvd/crystal-dock

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: plasma6-layer-shell-qt-devel

%if_with check
BuildRequires: ctest
BuildRequires: /usr/bin/xvfb-run
%endif

%description
Crystal Dock is a cool dock (desktop panel) for Linux desktop, with
the focus on attractive user interface, simplicity and cross-desktop
support.

The current version (version 2) supports Hyprland, KDE Plasma 6,
Labwc, LXQt, Niri and Wayfire on Wayland. Other desktop environments
and compositors will be considered when they run on Wayland and provide
sufficient APIs.

Main features:

* Smooth parabolic zooming and translucent effect
* Four visual styles: Glass 3D, Glass 2D, Flat 2D and Metal 2D with
  various appearance settings
* Supported components: Application Menu (Application Launcher),
  Launcher/Task Manager, Trash, Wi-Fi Manager, Volume Control, Version Checker, Clock and (on some environments) Pager
* Multiple docks support
* Integration with various desktop environments / compositors: specific
  default launchers, special menu entries (e.g. Log Out)
* Separate configs for separate desktop environments / compositors

%prep
%setup -q -n %{name}-%{version}/src
sed -i "s|https://github.com/dangvd/crystal-dock/raw/main/||" ../README.md
sed -i "s|Categories=.*|Categories=Qt;Utility;Accessibility;|" crystal-dock.desktop.cmake

%build
%cmake
%cmake_build

%install
%cmake_install

%check
xvfb-run -a %ctest -j1 -VV

%files
%doc ../images ../LICENSE ../README.md
%_bindir/crystal-dock
%_desktopdir/crystal-dock.desktop

%changelog
* Sun Nov 16 2025 Nikolay Strelkov <snk@altlinux.org> 2.15-alt1
- Initial build for Sisyphus
