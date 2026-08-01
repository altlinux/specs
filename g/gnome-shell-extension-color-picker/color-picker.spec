%define _unpackaged_files_terminate_build 1

%define _name color-picker
%define uuid %_name@tuberry
%define xdg_name org.gnome.shell.extensions.%_name

Name: gnome-shell-extension-%_name
Version: 50.2
Release: alt1
Summary: Simple color picker for GNOME Shell
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
URL: https://github.com/tuberry/color-picker
VCS: https://github.com/tuberry/color-picker
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

Requires: gnome-shell >= 48
BuildRequires(pre): rpm-macros-meson
BuildRequires: sassc
BuildRequires: meson
BuildRequires: %_bindir/glib-compile-schemas

%description
Simple color picker extension for GNOME Shell.

%prep
%setup
%autopatch -p1
sed -i 's/47.beta/%version.beta/g' meson.build

%build
%meson -Dtarget=system -Dversion=true
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/dbus-1/interfaces/org.gnome.Shell.Extensions.ColorPicker.xml
%doc README.md

%changelog
* Sat Aug 01 2026 Anton Midyukov <antohami@altlinux.org> 50.2-alt1
- New version 50.2.

* Tue Mar 25 2025 Alexander Davydzik <paladindev@altlinux.org> 48-alt1
- initial build
