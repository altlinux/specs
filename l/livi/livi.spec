%def_enable snapshot

%define ver_major 0.2
%define rdn_name org.sigxcpu.Livi

%def_enable check

Name: livi
Version: %ver_major.0
Release: alt1

Summary: Livi is a Light Video player
License: GPL-3.0-or-later
Group: Video
Url: https://gitlab.gnome.org/guidog/livi

%if_disabled snapshot
Source: %url/-/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/guidog/livi.git
Source: %name-%version.tar
%endif

%define glib_ver 2.76
%define gst_ver 1.22
%define adw_ver 1.4

Requires: gst-plugins-base1.0 >= %gst_ver
Requires: gst-libav
# since 0.2.0 "Allow to use gtk4paintablesink instead of in-tree sink"
Requires: gst-plugin-gtk4
Requires: dconf

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(gstreamer-1.0) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-play-1.0)
BuildRequires: pkgconfig(gstreamer-gl-1.0)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Minimalistic video player using GTK4 and GStreamer. The main purpose is
to make playing hw accelerated videos with hantro and OpenGL simple.

%prep
%setup -n %name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %rdn_name

%check
%__meson_test

%files -f %rdn_name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* NEWS

%changelog
* Thu Jun 13 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Mon Mar 18 2024 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- updated to v0.1.0-2-g7c00761

* Sat Jan 20 2024 Yuri N. Sedunov <aris@altlinux.org> 0.0.6-alt1
- updated to v0.0.6-10-gd2ec9b2

* Tue Jan 02 2024 Yuri N. Sedunov <aris@altlinux.org> 0.0.5-alt1
- first build for Sisyphus (v0.0.5-48-g2205cc6)


