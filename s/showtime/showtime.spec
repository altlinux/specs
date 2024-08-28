%def_enable snapshot

%define _name Showtime
%define ver_major 46
%define rdn_name org.gnome.%_name

%def_enable check

Name: showtime
Version: %ver_major.3
Release: alt2

Summary: Movie player for GNOME
License: GPL-3.0-or-later
Group: Video
Url: https://gitlab.gnome.org/GNOME/Incubator/showtime

Vcs: https://gitlab.gnome.org/GNOME/Incubator/showtime.git

%if_disabled snapshot
Source: %url/-/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

BuildArch: noarch

%define gst_api_ver 1.0
%define gst_ver 1.24
%define adw_ver 1.5

Requires: typelib(Adw) = 1
Requires: gst-plugin-gtk4 >= 0.13
Requires: gstreamer%gst_api_ver >= %gst_ver
Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
Requires: gst-plugins-ugly%gst_api_ver
Requires: gst-libav
Requires: dconf

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver gir(Adw)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Play your favorite movies and video files without hassle. Showtime
features simple playback controls that fade out of your way when you're
watching, fullscreen, adjustable playback speed, multiple language and
subtitle tracks, and screenshots -- everything you need for a
straightforward viewing experience.

%prep
%setup -n %name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%attr(0755,root,root) %_bindir/%name
%python3_sitelibdir_noarch/%name/
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Wed Aug 28 2024 Yuri N. Sedunov <aris@altlinux.org> 46.3-alt2
- updated to 46.3-6-gd8d8f82 (fixed i18n)
- added gst-plugin-gtk4 to runtime dependencies (ALT #51303)

* Sat Jul 13 2024 Yuri N. Sedunov <aris@altlinux.org> 46.3-alt1
- first build for Sisyphus


