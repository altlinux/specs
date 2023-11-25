%def_enable snapshot

%define old_name jellybean
%define _name stockpile
%define ver_major 0.3
%define rdn_name garden.turtle.Jellybean

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: Manage inventories of various things
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://codeberg.org/turtle/stockpile

%if_disabled snapshot
Source: %url/-/archive/%version/%name-%version.tar.gz
%else
Vcs: https://codeberg.org/turtle/stockpile.git
Source: %_name-%version.tar
%endif

Provides: %old_name = %EVR

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools blueprint-compiler
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(libadwaita-1) typelib(Adw)

%description
Stockpile is an app that allows you to manage your inventory of various
things. It provides you with an easy way to quickly use items whose
inventories are managed by Stockpile, as well as simple use and refill
functions and a handy low-stock indicator to let you know when your
stock of an item is running low.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --output %name.lang %old_name

%files -f %name.lang
%_bindir/%old_name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Sat Nov 25 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- first build for Sisyphus



