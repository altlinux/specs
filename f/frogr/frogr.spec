%define ver_major 1.6
%def_enable video
%define xdg_name org.gnome.frogr

Name: frogr
Version: %ver_major
Release: alt1

Summary: A Flickr Remote Organizer for GNOME
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Frogr

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%{?_enable_video:Requires: gst-plugins-base1.0 gst-plugins-good1.0 gst-plugins-bad1.0 gst-libav}

%define gtk_ver 3.16.0
%define json_glib_ver 1.2

BuildRequires(pre): meson
BuildRequires: yelp-tools libappstream-glib-devel
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libjson-glib-devel >= %json_glib_ver
BuildRequires: libsoup-devel libexif-devel libxml2-devel libgcrypt-devel
%{?_enable_video:BuildRequires: gstreamer1.0-devel}

%description
Frogr intends to be a complete GNOME application to remotely manage
a flickr account from the desktop.

%prep
%setup

%build
%meson %{?_enable_video:-Denable-video=true}
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*x*/apps/%xdg_name.png
%_iconsdir/hicolor/scalable/apps/%xdg_name.svg
%_iconsdir/hicolor/scalable/apps/%xdg_name-symbolic.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%_man1dir/%name.1.*
%doc AUTHORS NEWS README


%changelog
* Sat Jan 11 2020 Yuri N. Sedunov <aris@altlinux.org> 1.6-alt1
- 1.6

* Sun Nov 25 2018 Yuri N. Sedunov <aris@altlinux.org> 1.5-alt1
- 1.5

* Thu Dec 28 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4-alt1
- 1.4

* Mon May 22 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt1
- 1.3

* Wed Oct 05 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2-alt1
- 1.2

* Wed Oct 05 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- 1.1

* Wed Dec 30 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0

* Fri Jan 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.11-alt1
- first build for Sisyphus

