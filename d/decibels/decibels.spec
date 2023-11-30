%def_enable snapshot
%define _unpackaged_files_terminate_build 1

%define ver_major 0.1
%define rdn_name com.vixalien.decibels
%define gst_api_ver 1.0

Name: decibels
Version: %ver_major.7
Release: alt1

Summary: Sound Player for GNOME
Group: Sound
License: GPL-3.0-or-later
Url: https://apps.gnome.org/Decibels

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Vcs: https://github.com/vixalien/decibels.git
Source: %name-%version.tar
%endif

BuildArch: noarch

%define gjs_ver 1.54

Requires: libgjs >= %gjs_ver
Requires: gst-plugins-base%gst_api_ver gst-plugins-good%gst_api_ver
Requires: gstreamer%gst_api_ver-utils

Requires: typelib(Gtk) = 4.0
Requires: typelib(Adw) = 1
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GObject)
Requires: typelib(Gst) = %gst_api_ver
Requires: typelib(GstPbutils)
Requires: typelib(GstPlayer)

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson /usr/bin/tsc libgjs-devel
BuildRequires: desktop-file-utils /usr/bin/appstreamcli
BuildRequires: pkgconfig(libadwaita-1)

%description
The GNOME application for play sound files.

%prep
%setup -n %name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %rdn_name

%files -f %name.lang
%_bindir/%rdn_name
%_datadir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Thu Nov 30 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt1
- 0.1.7

* Sat Nov 25 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- first build for Sisyphus (0.1.6-10-g87d200a)

