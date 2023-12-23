%def_enable snapshot
%define _name g4music
%define ver_major 3.4
%define rdn_name com.github.neithern.%_name

%def_disable check

Name: %_name
Version: %ver_major.1
Release: alt1

Summary: Play your music elegantly
License: GPL-3.0-or-later
Group: Sound
Url: https://gitlab.gnome.org/neithern/g4music

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/neithern/g4music.git
Source: %_name-%version.tar
%endif

%define gtk_ver 4.10
%define adwaita_ver 1.2
%define gst_ver 1.20

Requires: gst-plugins-base1.0 >= %gst_ver
Requires: gst-plugins-bad1.0 >= %gst_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-tag-1.0)

%description
G4Music is a fast fluent lightweight music player written in GTK4, with
a beautiful and adaptive user interface, focuses on high performance for
large music collection.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %_name

%check
%__meson_test

%files -f %_name.lang
%_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.service
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.appdata.xml
%doc README*


%changelog
* Sat Dec 23 2023 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- first build for Sisyphus (v3.4-1-3-g777a0d9)


