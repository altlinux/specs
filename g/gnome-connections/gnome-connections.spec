%def_disable snapshot
%define _name connections
%define xdg_name org.gnome.Connections
%define ver_major 3.38

Name: gnome-%_name
Version: %ver_major.0
Release: alt1

Summary: GNOME Connections
Group: Graphical desktop/GNOME
License: GPL-3.0
Url: https://wiki.gnome.org/Apps/Connections

%if_disabled snapshot
Source: https://download.gnome.org/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Vcs: https://gitlab.gnome.org/GNOME/connections.git
Source: %name-%version.tar
%endif

%define glib_ver 2.58
%define gtk_ver 3.22.0

BuildRequires(pre): meson
BuildRequires: vala-tools 
BuildRequires: yelp-tools libappstream-glib-devel desktop-file-utils
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(gtk-vnc-2.0)
# for gtk-frdp
BuildRequires: pkgconfig(freerdp2)
BuildRequires: pkgconfig(winpr2)
BuildRequires: gobject-introspection-devel gir(Gtk) = 3.0

%description
%summary

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %_name

%files -f %_name.lang
%_bindir/%_name
%_libdir/%_name/
%_datadir/applications/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/dbus-1/services/%xdg_name.service
%_iconsdir/hicolor/*/*/%{xdg_name}*.*
%_datadir/mime/packages/%xdg_name.xml
%_datadir/appdata/%xdg_name.appdata.xml
%doc README* NEWS*

# gtk-frdp usless stuff
%exclude %_includedir/%_name/
%exclude %_datadir/%_name/
%exclude %_libdir/%_name/girepository-1.0/
%exclude %_libdir/%_name/pkgconfig/

%changelog
* Mon Sep 14 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- first build for Sisyphus


