%def_disable snapshot

%define _name dash-to-dock
%define ver_major 87
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

Requires: gnome-shell >= 45
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

%check
%make -k check VERBOSE=1

%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc README.md

%changelog
* Fri Aug 25 2023 Yuri N. Sedunov <aris@altlinux.org> 87-alt1
- 87

* Fri Jun 16 2023 Yuri N. Sedunov <aris@altlinux.org> 84-alt1
- 84

* Tue Jun 13 2023 Yuri N. Sedunov <aris@altlinux.org> 83-alt1
- 83

* Fri Jun 02 2023 Yuri N. Sedunov <aris@altlinux.org> 82-alt1
- 82

* Tue May 16 2023 Yuri N. Sedunov <aris@altlinux.org> 81-alt1
- 81

* Tue Apr 18 2023 Yuri N. Sedunov <aris@altlinux.org> 80-alt1
- 80

* Sun Mar 26 2023 Yuri N. Sedunov <aris@altlinux.org> 79-alt1
- first build for Sisyphus

