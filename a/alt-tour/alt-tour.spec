%define _unpackaged_files_terminate_build 1
%define app_id org.altlinux.Tour

Name: alt-tour
Version: 1.0
Release: alt1

Summary: ALT Tour and Greeter
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://gitlab.gnome.org/Armatik/alt-tour
Vcs: https://gitlab.gnome.org/Armatik/alt-tour
Source: %name-%version.tar

Requires: alt-panelmoded

Conflicts: gnome-tour

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1)

%description
A guided tour and greeter for Alt with GNOME DE.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%app_id.desktop
%_desktopdir/org.gnome.Tour.desktop
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%doc README.md

%changelog
* Tue Mar 04 2025 Alexander Davydzik <paladindev@altlinux.org> 1.0-alt1
- initial build
