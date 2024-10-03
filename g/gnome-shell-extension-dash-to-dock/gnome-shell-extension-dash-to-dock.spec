%def_disable snapshot

%define _name dash-to-dock
%define ver_major 98
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
%setup -n %_name%{?_disable_snapshot:-extensions.gnome.org}-%{?_disable_snapshot:v}%version%beta

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
* Thu Oct 03 2024 Yuri N. Sedunov <aris@altlinux.org> 98-alt1
- 98

* Wed Oct 02 2024 Yuri N. Sedunov <aris@altlinux.org> 97-alt1
- 97

* Fri Sep 06 2024 Yuri N. Sedunov <aris@altlinux.org> 96-alt1
- 96

* Wed Aug 28 2024 Yuri N. Sedunov <aris@altlinux.org> 95-alt1
- 95

* Sat Aug 24 2024 Yuri N. Sedunov <aris@altlinux.org> 94-alt1
- 94

* Sun Aug 11 2024 Yuri N. Sedunov <aris@altlinux.org> 93-alt1
- 93

* Thu Apr 25 2024 Yuri N. Sedunov <aris@altlinux.org> 92-alt1
- 92

* Sat Apr 20 2024 Yuri N. Sedunov <aris@altlinux.org> 91-alt1
- 91

* Thu Apr 18 2024 Yuri N. Sedunov <aris@altlinux.org> 90-alt1
- 90

* Fri Mar 22 2024 Yuri N. Sedunov <aris@altlinux.org> 89-alt1.1
- updated to v89-31-g554f7c5 (gnome-46 support)

* Tue Oct 10 2023 Yuri N. Sedunov <aris@altlinux.org> 89-alt1
- 89

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

