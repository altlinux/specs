%define ver_major 3.10

Name: gnome-music
Version: %ver_major.1
Release: alt1

Summary: Music playing application for GNOME3
Group: Sound
License: GPLv2+
Url: http://wiki.gnome.org/Apps/Music

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

# use python3
AutoReqProv: nopython
%define __python %nil

%add_typelib_req_skiplist typelib(Gd)

%define gtk_ver 3.9.0
%define grilo_ver 0.2.6

BuildRequires: intltool libgtk+3-devel >= %gtk_ver libgrilo-devel >= %grilo_ver
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: rpm-build-python3 python3-devel

Requires: gst-plugins-base1.0 grilo-tools tracker

%description
Music playing application for GNOME3.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_datadir/applications/%name.desktop
%_datadir/glib-2.0/schemas/org.gnome.Music.gschema.xml
%_datadir/icons/hicolor/*/apps/%name.png
%_libdir/%name/
%python3_sitelibdir_noarch/gnomemusic/
%_datadir/appdata/%name.appdata.xml
%doc AUTHORS README

%exclude %_libdir/%name/libgd.la

%changelog
* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon Sep 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.92-alt1
- 3.9.92

* Thu Aug 29 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.90-alt1
- first build for people/gnome

