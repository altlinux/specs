%define ver_major 3.12
%define _name org.gnome.Polari

Name: polari
Version: %ver_major.2
Release: alt1

Summary: Internet Relay Chat client for GNOME
License: GPLv2+
Group: Networking/Chat
Url: https://wiki.gnome.org/Apps/Polari

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: telepathy-logger
Requires: telepathy-mission-control
Requires: telepathy-idle

%set_typelibdir %_libdir/%name/girepository-1.0
%define gtk_ver 3.12.0

BuildRequires: gtk-doc gnome-common intltool desktop-file-utils
BuildRequires: libgtk+3-devel >= %gtk_ver libtelepathy-glib-devel
BuildRequires: libgjs gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libtelepathy-glib-gir-devel

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

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_libdir/%name/
%_desktopdir/%_name.desktop
%_iconsdir/hicolor/*x*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name/
%_datadir/dbus-1/services/%_name.service
%_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%_datadir/appdata/%_name.appdata.xml
%doc AUTHORS NEWS

%exclude %_libdir/%name/*.la

%changelog
* Wed May 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Wed Apr 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- first build for Sisyphus

