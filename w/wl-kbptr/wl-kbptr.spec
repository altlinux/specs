%define _unpackaged_files_terminate_build 1

Name: wl-kbptr
Version: 0.4.0
Release: alt1

Summary: Control the mouse pointer with the keyboard on Wayland.
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/moverest/wl-kbptr

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: pkgconfig(opencv4)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(cairo)

%description
%summary

%prep
%setup
%autopatch -p1

%build
%meson \
       -Dopencv=enabled
%meson_build

%install
%meson_install
install -Dm755 helpers/wl-kbptr-sway-active-win -t %buildroot%_bindir

%files
%doc LICENSE README.md config.example
%_bindir/*
%_desktopdir/*

%changelog
* Sat Jul 12 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.0-alt1
- New version 0.4.0.

* Sat Jun 28 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
