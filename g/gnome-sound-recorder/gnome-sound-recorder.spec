%def_enable snapshot
%define _unpackaged_files_terminate_build 1
%define ver_major 43
%define beta .beta
%define xdg_name org.gnome.SoundRecorder
%define gst_api_ver 1.0

Name: gnome-sound-recorder
Version: %ver_major
Release: alt0.5%beta

Summary: Sound Recorder for GNOME
Group: Sound
License: GPLv2+
Url: https://wiki.gnome.org/Design/Apps/SoundRecorder

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version%beta.tar
%endif

BuildArch: noarch

Obsoletes: gnome-media-common
Obsoletes: gnome-media-grecord
Provides:  gnome-media-grecord = %version-%release

%define glib_ver 2.44
%define gtk_ver 4.4.0
%define gjs_ver 1.54
%define adwaita_ver 1.2.0

Requires: libgjs >= %gjs_ver
Requires: gst-plugins-base%gst_api_ver gst-plugins-good%gst_api_ver gst-plugins-bad%gst_api_ver
Requires: gstreamer%gst_api_ver-utils
# find ./ -name "*.js" |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
Requires: typelib(Adw) = 1
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GObject)
Requires: typelib(Gst)
Requires: typelib(GstPbutils)
Requires: typelib(GstPlayer)
Requires: typelib(Gtk) = 4.0
# explicitly required to avoid installation old version
Requires: libgst-plugins%gst_api_ver-gir

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson /usr/bin/tsc
BuildRequires: libgio-devel >= %glib_ver libgtk4-devel >= %gtk_ver
BuildRequires: libgjs-devel libgtk4-gir-devel yelp-tools
BuildRequires: pkgconfig(gstreamer-player-%gst_api_ver)
BuildRequires: gst-plugins%gst_api_ver-devel
BuildRequires: gstreamer%gst_api_ver-utils gst-plugins-base%gst_api_ver
BuildRequires: gst-plugins-good%gst_api_ver gst-plugins-bad%gst_api_ver
BuildRequires: gobject-introspection-devel pkgconfig(libadwaita-1) >= %adwaita_ver

%description
The GNOME application for record and play sound files.

%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %xdg_name

%files -f %name.lang
%_bindir/%name
%_datadir/%xdg_name
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc NEWS README*


%changelog
* Fri Oct 13 2023 Yuri N. Sedunov <aris@altlinux.org> 43-alt0.5.beta
- updated to 43.beta-51-gaffa6c5

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Sun Jan 23 2022 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt2
- updated to 40.0-33-g7c98b31 (ported to GTK4 + Adwaita)

* Tue Mar 23 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Sat Jan 30 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Fri Sep 18 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Sat Sep 21 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Tue Jun 04 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Feb 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt2
- applied upstream patch to "Fix crashes when selecting a recording"
  (ALT #36071)

* Fri Jan 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Sun Sep 16 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt2
- fixed for gjs-1.54

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Feb 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.27.90-alt1
- 3.27.90

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Sep 13 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.92-alt1
- 3.21.92

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Thu Apr 28 2016 Yuri N. Sedunov <aris@altlinux.org> 3.19.92-alt1
- 3.19.92

* Sun Feb 28 2016 Yuri N. Sedunov <aris@altlinux.org> 3.19.91-alt1
- 3.19.91

* Sun Nov 08 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Tue Oct 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.17.92-alt1
- 3.17.92

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Sat Feb 07 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt2
- explicitly required libgst-plugins1.0-gir to avoid 0.10 version

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Wed Sep 17 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0.1-alt1
- 3.14.0.1

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Mon May 05 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt2
- obsoletes/provides gnome-media-grecord

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Feb 04 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.5-alt1
- first build for Sisyphus

