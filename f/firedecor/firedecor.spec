%define _unpackaged_files_terminate_build 1

%set_verify_elf_method relaxed

Name: firedecor
Version: 20231023
Release: alt1

Summary: MNT Reform specific window decoration for Wayfire
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/mntmn/Firedecor

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(wayfire)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(libinput)
BuildRequires: boost-devel

%description
An advanced window decoration plugin for the Wayfire window manager. 
Provides pretty standard rectangular frames and title bars with an icon 
and familiar minimize/maximize/close buttons.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%_libdir/wayfire/libfiredecor.so
%dir %_datadir/firedecor/button-styles/reform
%_datadir/firedecor/button-styles/reform/*
%_datadir/firedecor/executable.svg
%_datadir/wayfire/metadata/firedecor.xml

%changelog
* Sat Feb 15 2025 Nikolay Strelkov <snk@altlinux.org> 20231023-alt1
- Initial build for Sisyphus
