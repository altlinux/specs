%def_enable snapshot

%define ver_major 0.0
%define rdn_name org.sigxcpu.Livi

# online screenshots
%def_disable check

Name: livi
Version: %ver_major.5
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
%define gst_ver 1.20
%define adw_ver 1.4

Requires: gst-plugins-base1.0 >= %gst_ver
Requires: gst-libav
Requires: gstreamer-vaapi
Requires: dconf

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(gstreamer-1.0) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-play-1.0)
BuildRequires: pkgconfig(gstreamer-gl-1.0)
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils}

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
%doc README*

%changelog
* Tue Jan 02 2024 Yuri N. Sedunov <aris@altlinux.org> 0.0.5-alt1
- first build for Sisyphus (v0.0.5-48-g2205cc6)


