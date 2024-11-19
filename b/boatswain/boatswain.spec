%define APP_ID com.feaneron.Boatswain
%def_enable check

Name: boatswain
Version: 0.4.0
Release: alt1

Summary: Control your Elgato Stream Decks
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://gitlab.gnome.org/World/boatswain
Vcs: https://gitlab.gnome.org/World/boatswain
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rpm-build-gir
BuildRequires: gobject-introspection-devel
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libpeas-2)
BuildRequires: pkgconfig(libportal-gtk4)
BuildRequires: pkgconfig(gusb)
BuildRequires: pkgconfig(hidapi-libusb)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: gir(Gtk)
BuildRequires: gir(Json)
BuildRequires: gir(Peas)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
%endif

%description
Boatswain allows you to control Elgato Stream Deck devices.

With Boatswain you will be able to:

* Organize your actions in pages and profiles
* Set custom icons to actions
* Control your music player
* Play sound effects during your streams
* Control OBS Studio using Stream Deck (requires the obs-websocket extension)
* Send network requests
* Keep track of your gaming score
* Open files and launch applications

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_libdir/girepository-1.0/Bs-0.typelib
%_datadir/appdata/%APP_ID.appdata.xml
%_desktopdir/%APP_ID.desktop
%_datadir/gir-1.0/Bs-0.gir
%_datadir/glib-2.0/schemas/%{APP_ID}*.gschema.xml
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg

%changelog
* Fri Nov 08 2024 Oleg Shchavelev <oleg@altlinux.org> 0.4.0-alt1
- Initial build
