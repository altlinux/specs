%def_enable snapshot
%define _name g4music
%define ver_major 4.0
%define rdn_name com.github.neithern.%_name

%def_disable check

Name: %_name
Version: %ver_major
Release: alt1

Summary: Play your music elegantly
License: GPL-3.0-or-later
Group: Sound
Url: https://gitlab.gnome.org/neithern/g4music

Vcs: https://gitlab.gnome.org/neithern/g4music.git

%if_disabled snapshot
Source: %url/-/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

%define gtk_ver 4.16
%define adwaita_ver 1.6
%define gst_ver 1.24

Requires: gst-plugins-base1.0 >= %gst_ver
Requires: gst-plugins-bad1.0 >= %gst_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools
BuildRequires: desktop-file-utils /usr/bin/appstreamcli
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-tag-1.0)

%description
Gapless (AKA: G4Music) is a fast fluent lightweight music player written
in GTK4, with a beautiful and adaptive user interface, focuses on high
performance for large music collection.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %_name

appstreamcli metainfo-to-news --format text data/app.metainfo.xml.in NEWS

%check
%__meson_test

%files -f %_name.lang
%_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.service
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* NEWS


%changelog
* Sun Oct 13 2024 Yuri N. Sedunov <aris@altlinux.org> 4.0-alt1
- 4.0

* Mon Sep 16 2024 Yuri N. Sedunov <aris@altlinux.org> 3.9.2-alt1
- updated to v3.9.2-3-g21c26ed

* Wed Sep 04 2024 Yuri N. Sedunov <aris@altlinux.org> 3.9.1-alt1
- 3.9.1

* Mon Aug 26 2024 Yuri N. Sedunov <aris@altlinux.org> 3.9-alt1
- 3.9

* Sat Aug 17 2024 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Jul 29 2024 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Sun Jul 21 2024 Yuri N. Sedunov <aris@altlinux.org> 3.8-alt1
- updated to v3.8-2-gb1b9282 (renamed to Gapless)

* Sun Jun 30 2024 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- 3.7.2

* Sat Jun 29 2024 Yuri N. Sedunov <aris@altlinux.org> 3.7.1-alt1
- 3.7.1

* Mon Jun 03 2024 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Sun May 26 2024 Yuri N. Sedunov <aris@altlinux.org> 3.6-alt1
- updated to v3.6-1-gf0469bd

* Fri Apr 26 2024 Yuri N. Sedunov <aris@altlinux.org> 3.5.2-alt1
- 3.5.2

* Sun Jan 14 2024 Yuri N. Sedunov <aris@altlinux.org> 3.5.1-alt1
- 3.5.1

* Sat Dec 23 2023 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- first build for Sisyphus (v3.4-1-3-g777a0d9)


