%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: mangobar
Version: 0.0.0
Release: alt1_20260528git.ab2c193

Summary: Simple bar for Mango
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/mangowm/mangobar

Source: %name-%version.tar

BuildRequires(pre): meson

BuildRequires: cmake
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(fcft)
BuildRequires: libcjson-devel
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-cursor)

%description
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%_bindir/mangobar

%changelog
* Thu May 28 2026 Nikolay Strelkov <snk@altlinux.org> 0.0.0-alt1_20260528git.ab2c193
- Initial build for Sisyphus
