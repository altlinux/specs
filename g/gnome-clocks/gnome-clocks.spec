%define ver_major 3.10

Name: gnome-clocks
Version: %ver_major.1
Release: alt1

Summary: Clock application designed for GNOME 3
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://wiki.gnome.org/Apps/Clocks

Source: http://download.gnome.org/sources/%name/%ver_major/%name-%version.tar.xz

%define gweather_ver 3.9.3
%define geocode_ver 0.99.3

Requires: geoclue2

BuildRequires: intltool yelp-tools
BuildRequires: libgio-devel libgtk+3-devel >= 3.9.11 libnotify-devel
BuildRequires: libcanberra-gtk3-devel libgnome-desktop3-devel
BuildRequires: vala-tools gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libgweather-devel >= %gweather_ver libgeocode-glib-devel >= %geocode_ver
BuildRequires: geoclue2-devel

%description
Clock application designed for GNOME 3

%prep
%setup

%build
%autoreconf
%configure \
	--disable-schemas-compile
%make_build

%install
%makeinstall_std
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_datadir/applications/%name.desktop
%_datadir/icons/*/*/apps/%name.png
%_datadir/glib-2.0/schemas/org.gnome.clocks.gschema.xml
%_datadir/appdata/%name.appdata.xml
%doc README NEWS

%changelog
* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Sun Feb 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.90-alt1
- first build for Sisyphus

