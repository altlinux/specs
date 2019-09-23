%define _unpackaged_files_terminate_build 1

%define ver_major 3.34
%define xdg_name org.gnome.Books

Name: gnome-books
Version: %ver_major.0
Release: alt1

Summary: An e-book manager application for GNOME
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Books

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

%set_typelibdir %_libdir/%name/girepository-1.0

%define gtk_ver 3.22.15
%define gjs_ver 1.48
%define gi_ver 1.31.6
%define soup_ver 2.41.3
%define webkit_ver 2.6.0
%define evince_ver 3.13.3
%define tracker_ver 0.17.3

Conflicts: gnome-documents < 3.31
Requires: libgjs >= %gjs_ver

# find ./ -name "*.js" |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
Requires: typelib(cairo)
Requires: typelib(EvinceDocument)
Requires: typelib(EvinceView)
Requires: typelib(Gd)
Requires: typelib(Gdk)
Requires: typelib(GdkPixbuf)
Requires: typelib(GdPrivate)
Requires: typelib(Gepub)
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GnomeDesktop)
Requires: typelib(GObject)
Requires: typelib(Gtk)
Requires: typelib(Pango)
Requires: typelib(Tracker)
Requires: typelib(TrackerControl)
Requires: typelib(WebKit2)

BuildRequires(pre): meson rpm-build-gnome rpm-build-gir
BuildRequires: yelp-tools libappstream-glib-devel desktop-file-utils
BuildRequires: docbook-style-xsl librsvg
BuildRequires: pkgconfig(gjs-1.0) >= %gjs_ver
BuildRequires: pkgconfig(evince-document-3.0) >= %evince_ver
BuildRequires: pkgconfig(evince-view-3.0)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(gobject-introspection-1.0) >= %gi_ver
BuildRequires: pkgconfig(gtk+-3.0) >= %gtk_ver
BuildRequires: pkgconfig(libsoup-2.4) >= %soup_ver
BuildRequires: pkgconfig(tracker-control-2.0) >= %tracker_ver
BuildRequires: pkgconfig(tracker-sparql-2.0)
BuildRequires: pkgconfig(webkit2gtk-4.0) >= %webkit_ver
BuildRequires: pkgconfig(libgepub-0.6)
BuildRequires: libgtk+3-gir-devel libgnome-desktop3-gir-devel libgepub-gir-devel
BuildRequires: libevince-gir-devel

%description
A simple application to access, organize and read your e-books on GNOME.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_libdir/%name/
%_datadir/%name/
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/%xdg_name.*
%_iconsdir/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_man1dir/%name.1.*
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/org.gnome.books.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name.enums.xml
%_datadir/metainfo/%xdg_name.appdata.xml
%doc README* NEWS


%changelog
* Fri Sep 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Fri Mar 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Wed Feb 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.31.90-alt1
- first build for Sisyphus

