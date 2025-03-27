%define _unpackaged_files_terminate_build 1

%define _name color-picker
%define uuid %_name@tuberry
%define xdg_name org.gnome.shell.extensions.%_name

Name: gnome-shell-extension-%_name
Version: 48
Release: alt1
Summary: Simple color picker for GNOME Shell
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/tuberry/color-picker
Vcs: https://github.com/tuberry/color-picker
Source: %name-%version.tar

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
sed -i 's/47.beta/%version.beta/g' meson.build

%build
%meson -Dtarget=system -Dversion=%version
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc README.md

%changelog
* Tue Mar 25 2025 Alexander Davydzik <paladindev@altlinux.org> 48-alt1
- initial build
