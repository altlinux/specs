%def_enable snapshot
%define _unpackaged_files_terminate_build 1

%define ver_major 46
%define xdg_name org.gnome.Decibels
%define gst_api_ver 1.0

%def_enable check

Name: decibels
Version: %ver_major.0
Release: alt1

Summary: Sound Player for GNOME
Group: Sound
License: GPL-3.0-or-later
Url: https://apps.gnome.org/Decibels

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Vcs: https://gitlab.gnome.org/vixalien/decibels.git
Source: %name-%version.tar
%endif

BuildArch: noarch

%define gjs_ver 1.54
%define adw_ver 1.5

Requires: libgjs >= %gjs_ver
Requires: gst-plugins-base%gst_api_ver gst-plugins-good%gst_api_ver
Requires: gstreamer%gst_api_ver-utils

Requires: typelib(Gtk) = 4.0
Requires: typelib(Adw) = 1
Requires: libadwaita-gir >= %adw_ver
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GObject)
Requires: typelib(Gst) = %gst_api_ver
Requires: typelib(GstPbutils)
Requires: typelib(GstPlayer)

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson blueprint-compiler /usr/bin/tsc libgjs-devel
BuildRequires: pkgconfig(libadwaita-1)
%{?_enable_check:BuildRequires: desktop-file-utils /usr/bin/appstreamcli}

%description
The GNOME application for play sound files.

%prep
%setup -n %name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %xdg_name

%check
%__meson_test

%files -f %name.lang
%_bindir/%xdg_name
%_datadir/%xdg_name
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc README*


%changelog
* Fri Mar 29 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0-alt1
- 46.0

* Thu Nov 30 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt1
- 0.1.7

* Sat Nov 25 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- first build for Sisyphus (0.1.6-10-g87d200a)

