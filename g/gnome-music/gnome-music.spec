%define ver_major 3.14

Name: gnome-music
Version: %ver_major.3.1
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

Requires: tracker

%define gtk_ver 3.12.0
%define grilo_ver 0.2.6
%define python_ver 3.3

BuildRequires: intltool yelp-tools libgtk+3-devel >= %gtk_ver
BuildRequires: libgrilo-devel >= %grilo_ver libmediaart-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: rpm-build-python3 python3-devel >= %python_ver

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

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_datadir/applications/%name.desktop
%_datadir/glib-2.0/schemas/org.gnome.Music.gschema.xml
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/icons/HighContrast/*/apps/%name.png
%_libdir/%name/
%python3_sitelibdir_noarch/gnomemusic/
%_datadir/appdata/%name.appdata.xml
#%_man1dir/%name.1.*
%doc AUTHORS README

%exclude %_libdir/%name/libgd.la

%changelog
* Mon Jan 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.3.1-alt1
- 3.14.3.1

* Mon Jan 19 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt1
- 3.14.3

* Thu Nov 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2.1-alt1
- 3.12.2.1

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Sun Feb 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.3-alt1
- 3.10.3

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon Sep 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.92-alt1
- 3.9.92

* Thu Aug 29 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.90-alt1
- first build for people/gnome

