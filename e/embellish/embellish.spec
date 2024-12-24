%define APP_ID io.github.getnf.embellish
%def_enable check

Name: embellish
Version: 0.4.5
Release: alt1

Summary: Install nerd fonts
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://github.com/getnf/embellish
Vcs: https://github.com/getnf/embellish
Source: %name-%version.tar

Requires: typelib(Gtk) >= 4.0
Requires: typelib(Adw) >= 1
Requires: typelib(GnomeAutoar)

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gjs-1.0)
BuildRequires: gtk4-update-icon-cache

%description
User-friendly application designed for managing Nerd Fonts on your system. With
a sleek GTK4 user interface enhanced by libadwaita, Embellish provides
a seamless experience for installing, uninstalling and updating of Nerd Fonts.

* List all available Nerd Fonts
* Download and install a Font
* Uninstall an installed Font
* Update an installed font
* preview fonts
* Search fonts
* Read font's licence(s)

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %APP_ID

%check
%meson_test

%files -f %APP_ID.lang
%_bindir/%APP_ID
%_desktopdir/%APP_ID.desktop
%_datadir/dbus-1/services/%APP_ID.service
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/%APP_ID
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Mon Dec 09 2024 Oleg Shchavelev <oleg@altlinux.org> 0.4.5-alt1
- Initial build
