%define ver_major 1.0
%def_enable video

Name: frogr
Version: %ver_major
Release: alt1

Summary: A Flickr Remote Organizer for GNOME
License: GPLv3
Group: Graphical desktop/GNOME

URL: https://wiki.gnome.org/Apps/Frogr
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%{?_enable_video:Requires: gst-plugins-base1.0 gst-plugins-good1.0 gst-plugins-bad1.0 gst-libav}

%define gtk_ver 3.14.0

BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: gnome-common intltool yelp-tools libappstream-glib-devel
BuildRequires: libjson-glib-devel libsoup-devel libexif-devel libxml2-devel libgcrypt-devel
%{?_enable_video:BuildRequires: gstreamer1.0-devel}

%description
Frogr intends to be a complete GNOME application to remotely manage
a flickr account from the desktop.

%prep
%setup

%build
%autoreconf
%configure %{subst_enable video}
%make_build V=1

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*x*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/scalable/apps/%name-symbolic.svg
%_datadir/appdata/%name.appdata.xml
%_man1dir/%name.1.*
%doc AUTHORS NEWS README

%exclude %_datadir/pixmaps/%name.xpm

%changelog
* Wed Dec 30 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0

* Fri Jan 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.11-alt1
- first build for Sisyphus

