%define ver_major 3.22
%define xdg_name org.gnome.Polari

Name: polari
Version: %ver_major.2
Release: alt1

Summary: Internet Relay Chat client for GNOME
License: GPLv2+
Group: Networking/Chat
Url: https://wiki.gnome.org/Apps/Polari

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: libgjs
Requires: telepathy-logger
Requires: telepathy-mission-control
Requires: telepathy-idle

# find ./ -name "*.js" |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
Requires: typelib(Gdk)
Requires: typelib(GdkPixbuf)
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GObject)
Requires: typelib(Gtk)
Requires: typelib(Pango)
Requires: typelib(PangoCairo)
Requires: typelib(Polari)
Requires: typelib(Secret)
Requires: typelib(Soup)
Requires: typelib(TelepathyGLib)
Requires: typelib(TelepathyLogger)

%set_typelibdir %_libdir/%name/girepository-1.0
%define gtk_ver 3.21.6

BuildRequires: gtk-doc gnome-common yelp-tools
BuildRequires: desktop-file-utils libappstream-glib-devel
BuildRequires: libgtk+3-devel >= %gtk_ver libtelepathy-glib-devel
BuildRequires: libgjs gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libsecret-gir-devel libsoup-gir-devel
BuildRequires: libtelepathy-glib-gir-devel libtelepathy-logger-gir-devel

%description
Polari is a simple IRC Client that is designed to integrate seamlessly
with GNOME 3 Desktop.

%prep
%setup

%build
%configure --disable-static \
	--disable-schemas-compile
%make_build

%install
%makeinstall_std

%find_lang --with-gnome --output=%name.lang %name %xdg_name

%files -f %name.lang
%_bindir/%name
%_libdir/%name/
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*x*/apps/%xdg_name.png
%_iconsdir/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_datadir/%name/
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.Polari.service
%_datadir/telepathy/clients/Polari.client
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/appdata/%xdg_name.appdata.xml
%doc AUTHORS NEWS

%exclude %_libdir/%name/*.la

%changelog
* Thu Nov 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sat Aug 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Wed May 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Sat Apr 30 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Wed Oct 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed Apr 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Wed May 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Wed Apr 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- first build for Sisyphus

