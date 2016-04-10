%define _name org.gnome.Characters
%define ver_major 3.20
%define _libexecdir %_prefix/libexec
%def_with included_libunistring

Name: gnome-characters
Version: %ver_major.1
Release: alt1

Summary: Character map application for GNOME
Group: Text tools
License: BSD and GPLv2+
Url: https://wiki.gnome.org/Design/Apps/CharacterMap

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
#Source: %name-%version.tar

%set_typelibdir %_libdir/%_name/girepository-1.0

%define gjs_ver 1.44.0
%define unistring_ver 0.9.5

Requires: libgjs >= %gjs_ver
# find ./ -name "*.js" |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
Requires: typelib(Gc)
Requires: typelib(Gdk)
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GnomeDesktop)
Requires: typelib(GObject)
Requires: typelib(Gtk)
Requires: typelib(IBus)
Requires: typelib(Pango)
Requires: typelib(PangoCairo)

BuildRequires: intltool libappstream-glib-devel
BuildRequires: libgtk+3-devel libgjs-devel >= %gjs_ver
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
%{?_without_included_libunistring:BuildRequires: libunistring-devel >= %unistring_ver}
BuildRequires: gperf

%description
Characters is a simple utility application to find and insert unusual
characters.

%prep
%setup

%build
%autoreconf
%configure --disable-static \
	%{?_with_included_libunistring:--with-included-libunistring}
%make_build

%install
%makeinstall_std

%find_lang %_name

%files -f %_name.lang
%_bindir/%name
%_libdir/%_name/
%_datadir/%_name/
%_desktopdir/%_name.desktop
%_datadir/dbus-1/services/%_name.service
%_datadir/glib-2.0/schemas/%_name.gschema.xml
%_datadir/dbus-1/services/%_name.BackgroundService.service
%_datadir/gnome-shell/search-providers/%_name.search-provider.ini
%_iconsdir/*/*/*/*.svg
%_iconsdir/*/*/*/*.png
%_datadir/appdata/%_name.appdata.xml
%doc NEWS COPYING README

%exclude %_libdir/%_name/libgc.la

%changelog
* Sun Apr 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Sun Oct 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Fri Feb 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.2-alt1
- first build for people/gnome

