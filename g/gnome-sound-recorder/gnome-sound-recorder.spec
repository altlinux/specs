%define _unpackaged_files_terminate_build 1
%define ver_major 3.12
%define _name org.gnome.SoundRecorder
%define gst_api_ver 1.0

Name: gnome-sound-recorder
Version: %ver_major.1
Release: alt1

Summary: Sound Recorder for GNOME
Group: Development/Tools
License: GPLv2+
Url: https://live.gnome.org/Ghex

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: gst-plugins-base%gst_api_ver gst-plugins-good%gst_api_ver gst-plugins-bad%gst_api_ver

%add_typelib_req_skiplist typelib(Gd)
%define glib_ver 2.31.10
%define gtk_ver 3.9.4

BuildRequires: gnome-common libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libgjs-devel libgtk+3-gir-devel intltool yelp-tools

%description
The GNOME application for record and play sound files.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-schemas-compile

%make_build

%install
%makeinstall_std

%find_lang --with-gnome --output=%name.lang %name

%files -f %name.lang
%_bindir/*
%_libdir/%name/
%_datadir/%name/
%_datadir/applications/%_name.desktop
%_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%_iconsdir/hicolor/*/apps/*
#%_iconsdir/HighContrast/*x*/apps/%name.png
#%_datadir/appdata/%name.appdata.xml
%doc NEWS README

%exclude %_libdir/%name/*.la

%changelog
* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Feb 04 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.5-alt1
- first build for Sisyphus

