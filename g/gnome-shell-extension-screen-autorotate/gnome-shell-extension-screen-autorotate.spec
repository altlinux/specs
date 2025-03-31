%def_disable snapshot

%define _name screen-autorotate
%define __name screen-rotate
%define ver_major 25
%define beta %nil
%define uuid %__name@shyzus.github.io
%define xdg_name org.gnome.shell.extensions.%__name
%define gettext_domain gnome-shell-extension-%__name

Name: gnome-shell-extension-%_name
Version: %ver_major
Release: alt1

Summary: Screen Rotate extension for the GNOME Shell
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://github.com/shyzus/gnome-shell-extension-screen-autorotate

Vcs: https://github.com/shyzus/gnome-shell-extension-screen-autorotate.git

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif

Provides: gnome-shell-extension-%__name = %EVR

Requires: gnome-shell >= 45
Requires: typelib(Adw) = 1
Requires: iio-sensor-proxy

BuildRequires: /usr/bin/glib-compile-schemas

%description
A GNOME extension to enable screen rotation regardless of touch mode.
This extension uses Mutter's D-Bus API, so it works on both X11 and Wayland.

%prep
%setup -n %name-%version%beta

%install
mkdir -p %buildroot%_datadir/{gnome-shell/extensions/%uuid,glib-2.0/schemas}
cp -a %uuid/*.{js,json} %buildroot%_datadir/gnome-shell/extensions/%uuid/
cp -a %uuid/schemas/%xdg_name.gschema.xml %buildroot%_datadir/glib-2.0/schemas/

%find_lang %gettext_domain

%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc README.md

%changelog
* Tue Apr 01 2025 Yuri N. Sedunov <aris@altlinux.org> 25-alt1
- first build for Sisyphus

