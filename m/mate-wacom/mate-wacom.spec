%define _unpackaged_files_terminate_build 1

%def_with check

Name: mate-wacom
Version: 1.0.0
Release: alt1

Summary: Graphics Tablet Settings for MATE Control Center
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/KeremSoke/mate-wacom

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: vala-tools
BuildRequires: cmake
BuildRequires: pkgconfig(gtk+-3.0)

Requires: /usr/bin/xsetwacom
Requires: /usr/bin/xrandr

%description
A GTK 3/Vala graphics tablet settings window for MATE.
Uses the xsetwacom utility to read and apply X11 Wacom driver settings.

%prep
%setup
rm -vf po/*.po~

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
%_bindir/mate-wacom-properties
%_desktopdir/mate-wacom-properties.desktop

%changelog
* Sat Nov 14 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
