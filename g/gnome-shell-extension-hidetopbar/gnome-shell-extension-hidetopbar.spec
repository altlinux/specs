%def_disable snapshot

%define _name hidetopbar
%define ver_major 124
%define git_tag 0a44c5f88e4a4144c96186090e552e452c196862
%define beta %nil
%define uuid hidetopbar@mathieu.bidon.ca
%define xdg_name org.gnome.shell.extensions.%_name
%define gettext_domain %_name

%def_enable check

Name: gnome-shell-extension-%_name
Version: %ver_major
Release: alt1

Summary: Hide Top Bar extension for the GNOME Shell
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://gitlab.gnome.org/tuxor1337/hidetopbar

Vcs: https://gitlab.gnome.org/tuxor1337/hidetopbar.git

BuildArch: noarch

%if_disabled snapshot
Source: %url/-/archive/extensions.gnome.org-%version%beta/%_name-%version%beta.tar.gz
%else
Source: %_name-%version%beta.tar
%endif

Requires: gnome-shell >= 45
Requires: typelib(Adw) = 1

BuildRequires: zip /usr/bin/glib-compile-schemas

%description
GNOME extension to hide the top bar except in overview mode.

%prep
%setup -n %_name-%{?_disable_snapshot:extensions.gnome.org-}%version%beta%{?_disable_snapshot:-%git_tag}

%build
%make VERSION=%version

%install
mkdir -p %buildroot%_datadir/{gnome-shell/extensions/%uuid,glib-2.0/schemas}
cp -a *.js* *.ui %buildroot%_datadir/gnome-shell/extensions/%uuid/
cp -a schemas/%xdg_name.gschema.xml %buildroot%_datadir/glib-2.0/schemas/
cp -ar locale %buildroot%_datadir/ && rm -f %buildroot/%_datadir/locale/{*.pot*,*/*/*.po*}

%find_lang %gettext_domain

%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc README.md

%changelog
* Wed May 06 2026 Yuri N. Sedunov <aris@altlinux.org> 124-alt1
- 124 (GNOME 50 supported)

* Sun Sep 28 2025 Yuri N. Sedunov <aris@altlinux.org> 121-alt1
- 121 (GNOME 49 supported)

* Thu Jun 12 2025 Yuri N. Sedunov <aris@altlinux.org> 120-alt1
- 120

* Fri Feb 21 2025 Yuri N. Sedunov <aris@altlinux.org> 118-alt1
- 118 (ALT #53198)

* Mon Jun 26 2023 Yuri N. Sedunov <aris@altlinux.org> 113-alt1
- first build for Sisyphus

