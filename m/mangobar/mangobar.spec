%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: mangobar
Version: 0.2.0
Release: alt1

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
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(alsa)

%description
A Wayland status bar for mangowm, built on wlr-layer-shell.
The system tray (StatusNotifierItem / DBusMenu) is inspired
by swaybar and waybar.

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
* Mon Aug 17 2026 Nikolay Strelkov <snk@altlinux.org> 0.2.0-alt1
- New version 0.2.0.

* Sun Aug 16 2026 Nikolay Strelkov <snk@altlinux.org> 0.1.1-alt1
- new version 0.1.1 (with rpmrb script)

* Thu May 28 2026 Nikolay Strelkov <snk@altlinux.org> 0.0.0-alt1_20260528git.ab2c193
- Initial build for Sisyphus
