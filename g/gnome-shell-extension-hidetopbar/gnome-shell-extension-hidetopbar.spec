%def_enable snapshot

%define _name hidetopbar
%define ver_major 113
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
License: GPL-3.0
Url: https://gitlab.gnome.org/tuxor1337/hidetopbar

BuildArch: noarch

%if_disabled snapshot
Source: %url/-/archive/extensions.gnome.org-%version%beta/%_name-%version%beta.tar.gz
%else
Vcs: https://gitlab.gnome.org/tuxor1337/hidetopbar.git
Source: %_name-%version%beta.tar
%endif

Requires: gnome-shell >= 44
Requires: typelib(Gtk) = 4.0

BuildRequires: zip /usr/bin/glib-compile-schemas

%description
GNOME extension to hide the top bar except in overview mode.

%prep
%setup -n %_name-%version%beta

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
* Mon Jun 26 2023 Yuri N. Sedunov <aris@altlinux.org> 113-alt1
- first build for Sisyphus

