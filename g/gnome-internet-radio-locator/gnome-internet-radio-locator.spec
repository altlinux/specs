%define ver_major 1.0
%define gst_api_ver 1.0
%def_with recording

Name: gnome-internet-radio-locator
Version: %ver_major.3
Release: alt1

Summary: GNOME Internet Radio Locator
License: GPLv2+
Group: Sound
Url: https://wiki.gnome.org/Apps/Girl

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
Requires: gst-plugins-ugly%gst_api_ver
Requires: dconf

%define gtk_ver 3.0

BuildRequires: gnome-common intltool yelp-tools gtk-doc
BuildRequires: libgtk+3-devel >= %gtk_ver libxml2-devel libchamplain-gtk3-devel
BuildRequires: libgeocode-glib-devel gst-plugins%gst_api_ver-devel gst-plugins-bad1.0-devel
BuildRequires: libsoup-devel gsettings-desktop-schemas-devel

%description
GNOME Internet Radio Locator is a Free Software program that allows
you to easily locate radio programs by broadcasters on the Internet
with the help of a map.

%prep
%setup

%build
%autoreconf
%configure \
	%{subst_with recording}
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/org.gnome.gnome-internet-radio-locator.enums.xml
%_datadir/glib-2.0/schemas/org.gnome.gnome-internet-radio-locator.gschema.xml
%_iconsdir/hicolor/*x*/apps/%name.png
%_datadir/appdata/%name.appdata.xml
%_man1dir/%name.1.*
%doc AUTHORS NEWS README TODO HACKING


%changelog
* Sat Feb 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Sat Nov 25 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Tue Oct 24 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sat Sep 16 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Aug 14 2017 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed Jul 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Tue Jul 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- 0.5.3

* Mon Jul 17 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Tue Jun 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Fri Jun 16 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus

