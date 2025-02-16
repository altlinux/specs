%define _unpackaged_files_terminate_build 1

Name: wdisplays
Version: 1.1.1
Release: alt1

Summary: graphical application for configuring displays in Wayland compositors
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/artizirk/wdisplays

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gdk-3.0)
BuildRequires: pkgconfig(epoxy)
BuildRequires: /usr/bin/scour

%description
wdisplays is a graphical application for configuring displays in Wayland
compositors. It borrows some code from kanshi. It should work in any
compositor that implements the wlr-output-management-unstable-v1
protocol, including sway. The goal of this project is to allow precise
adjustment of display settings in kiosks, digital signage, and other
elaborate multi-monitor setups.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc CHANGELOG.md README.md LICENSES/GPL-3.0-or-later.txt
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*

%changelog
* Sun Feb 16 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus
