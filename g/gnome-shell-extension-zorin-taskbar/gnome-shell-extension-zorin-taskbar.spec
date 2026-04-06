%def_disable snapshot

%define _name zorin-taskbar
%define ver_major 73
%define beta %nil
%define uuid %_name@zorinos.com
%define xdg_name org.gnome.shell.extensions.%_name
%define gettext_domain %_name

%def_enable check

Name: gnome-shell-extension-%_name
Version: %ver_major.2.2
Release: alt1

Summary: The official taskbar for Zorin OS
Group: Graphical desktop/GNOME
License: GPL-2.0-or-later
Url: https://github.com/ZorinOS/zorin-taskbar

Vcs: https://github.com/ZorinOS/zorin-taskbar.git

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/%version%beta/%_name-%version%beta.tar.gz
%else
Source: %_name-%version%beta.tar
%endif

Requires: gnome-shell >= 46
Requires: typelib(Adw) = 1

BuildRequires: /usr/bin/glib-compile-schemas

%description
The official taskbar for Zorin OS.

%prep
%setup -n %_name-%version%beta

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
* Mon Apr 06 2026 Yuri N. Sedunov <aris@altlinux.org> 73.2.2-alt1
- 73.2.2 (GNOME-50 supported)

* Thu Dec 25 2025 Yuri N. Sedunov <aris@altlinux.org> 70.1.1-alt1
- first build for Sisyphus

