%define _unpackaged_files_terminate_build 1

%define _libexecdir %_prefix/libexec

%def_with check

Name: rojo
Version: 0.1.0
Release: alt1

Summary: MATE Color Management Daemon
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/KeremSoke/rojo

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: vala-tools
BuildRequires: cmake
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(wayland-client)

Requires: geoclue2

%description
Rojo is MATE's color management daemon, or at least will be one day.

Today it does Night Light and gamma, and it works the same on the X
session and the Wayland (hopefully) session.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%check
%meson_test

%files -f %{name}.lang
%doc LICENSE README.md
%config(noreplace) %_sysconfdir/geoclue/conf.d/rojo.conf
%_sysconfdir/xdg/autostart/rojo.desktop
%_libexecdir/rojo
%_datadir/dbus-1/interfaces/org.mate.rojo.NightLight.xml
%_datadir/dbus-1/services/org.mate.rojo.service
%_datadir/glib-2.0/schemas/org.mate.rojo.nightlight.gschema.xml

%changelog
* Sat Nov 14 2026 Nikolay Strelkov <snk@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
