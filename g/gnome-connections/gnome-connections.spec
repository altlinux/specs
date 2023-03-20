%def_disable snapshot
%define _name connections
%define xdg_name org.gnome.Connections
%define ver_major 44
%define beta %nil

Name: gnome-%_name
Version: %ver_major.0
Release: alt1%beta

Summary: GNOME Connections
Group: Graphical desktop/GNOME
License: GPL-3.0
Url: https://wiki.gnome.org/Apps/Connections

%if_disabled snapshot
Source: https://download.gnome.org/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Vcs: https://gitlab.gnome.org/GNOME/connections.git
Source: %name-%version.tar
%endif

%define glib_ver 2.58
%define gtk_ver 3.22.0
%define handy_ver 1.6

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools 
BuildRequires: yelp-tools libappstream-glib-devel desktop-file-utils
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(gtk-vnc-2.0)
# for gtk-frdp
BuildRequires: pkgconfig(freerdp2)
BuildRequires: pkgconfig(winpr2)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: gobject-introspection-devel gir(Gtk) = 3.0
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver

%description
%summary

%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_libdir/%name/
%_datadir/applications/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/dbus-1/services/%xdg_name.service
%_iconsdir/hicolor/*/*/%{xdg_name}*.*
%_datadir/mime/packages/%xdg_name.xml
%_datadir/metainfo/%xdg_name.appdata.xml
%doc README* NEWS*

# gtk-frdp usless stuff
%exclude %_includedir/%name/
%exclude %_datadir/%name/
%exclude %_libdir/%name/girepository-1.0/
%exclude %_libdir/%name/pkgconfig/

%changelog
* Sat Mar 18 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Wed Apr 13 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1.2-alt1
- 42.1.2

* Thu Apr 07 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1.1-alt1
- 42.1.1

* Tue Apr 05 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Mon Mar 21 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Fri Dec 03 2021 Yuri N. Sedunov <aris@altlinux.org> 41.2-alt1
- 41.2

* Wed Oct 27 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Fri Sep 17 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Thu Apr 15 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0.1-alt1
- 40.0.1

* Fri Mar 19 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Tue Oct 27 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Mon Sep 14 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- first build for Sisyphus


