%def_disable snapshot

%define _name dash-to-dock
%define ver_major 79
%define beta %nil
%define uuid %_name@micxgx.gmail.com
%define xdg_name org.gnome.shell.extensions.%_name
%define gettext_domain dashtodock

%def_enable check

Name: gnome-shell-extension-%_name
Version: %ver_major
Release: alt1

Summary: A dock for the GNOME Shell
Group: Graphical desktop/GNOME
License: GPL-2.0
Url: https://github.com/micheleg/dash-to-dock

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/extensions.gnome.org-v%version%beta/%_name-%version%beta.tar.gz
%else
Vcs: https://github.com/micheleg/dash-to-dock.git
Source: %_name-%version%beta.tar
%endif

Requires: gnome-shell >= 44
Requires: typelib(Gtk) = 4.0
Requires: typelib(Dbusmenu)

BuildRequires: /usr/bin/glib-compile-schemas sassc eslint

%description
This extension moves the dash out of the overview transforming it in
a dock for an easier launching of applications and a faster switching
between windows and desktops. Side and bottom placement options are
available.

%prep
%setup -n %_name%{?_disable_snapshot:-extensions.gnome.org-v}%version%beta

%build
%make VERSION=%version

%install
%makeinstall_std
%find_lang %gettext_domain

%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc README.md

%changelog
* Sun Mar 26 2023 Yuri N. Sedunov <aris@altlinux.org> 79-alt1
- first build for Sisyphus

