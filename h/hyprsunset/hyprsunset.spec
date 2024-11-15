Name: hyprsunset
Version: 0.1.0
Release: alt1
License: BSD-3-Clause

Summary: An application to enable a blue-light filter on Hyprland

Group: Graphical desktop/Other

Url: https://github.com/hyprwm/hyprsunset

Source: %name-%version.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-cmake

BuildRequires: gcc-c++ cmake

BuildRequires: pkgconfig(hyprutils)
BuildRequires: pkgconfig(hyprland-protocols)
BuildRequires: pkgconfig(hyprwayland-scanner)

BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-protocols)

BuildRequires: pkgconfig(libffi)

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
%_bindir/%name

%changelog
* Sun Nov 10 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.1.0-alt1
- Initial build
