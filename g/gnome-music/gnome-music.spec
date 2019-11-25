%def_disable snapshot

%define ver_major 3.34
%define xdg_name org.gnome.Music
%define gst_api_ver 1.0

Name: gnome-music
Version: %ver_major.2
Release: alt1

Summary: Music playing application for GNOME3
Group: Sound
License: GPLv2+
Url: http://wiki.gnome.org/Apps/Music

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

# use python3
AutoReqProv: nopython
%define __python %nil
%add_typelib_req_skiplist typelib(Gd) typelib(Gfm)

%define tracker_ver 2.0
%define gtk_ver 3.20.0
%define grilo_ver 0.3.6
%define python_ver 3.3
%define mediaart_ver 1.9
%define pygobject_ver 3.29.1
%define pycairo_ver 1.14.0

Requires: tracker >= %tracker_ver
Requires: grilo-plugins

# gir-python.req doesn't recognize multiline expressions (see gnomemusic/albumartcache.py)
Requires: typelib(MediaArt) = 2.0 typelib(GstTag)

# gnomemusic/widgets/songwidget.py:from gi.repository.Dazzle import BoldingLabel  # noqa: F401
Requires: typelib(Dazzle)

%add_python3_req_skip gi.repository.Dazzle gi.repository.Gd

Requires: gst-plugins-base%gst_api_ver grilo-tools >= %grilo_ver tracker >= %tracker_ver

BuildRequires(pre): meson rpm-build-gir rpm-build-python3
BuildRequires: %_bindir/git
BuildRequires: yelp-tools libappstream-glib-devel desktop-file-utils
BuildRequires: libgtk+3-devel >= %gtk_ver libdazzle-devel libsoup-devel
BuildRequires: libgrilo-devel >= %grilo_ver grilo-plugins-devel
BuildRequires: libmediaart2.0-devel >= %mediaart_ver
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: python3-devel >= %python_ver
BuildRequires: pkgconfig(tracker-sparql-2.0)
BuildRequires: python3-module-pygobject3-devel >= %pygobject_ver python3-module-pycairo-devel >= %pycairo_ver
BuildRequires: libgnome-online-accounts-devel

%description
Music playing application for GNOME3.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name %xdg_name

%files -f %name.lang
%_bindir/%name
%_datadir/%xdg_name/
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/org.gnome.Music.gschema.xml
%_iconsdir/hicolor/*/*/*.svg
%_libdir/%xdg_name/
%python3_sitelibdir_noarch/gnomemusic/
%_datadir/metainfo/%xdg_name.appdata.xml
#%_man1dir/%name.1.*
%doc README* NEWS*

%changelog
* Mon Nov 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Fri Oct 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Mon May 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Thu Feb 14 2019 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt2
- updated to 3.30.2-6-g611d313b
- fixed https://gitlab.gnome.org/GNOME/gnome-music/issues/244

* Tue Oct 23 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Mon Sep 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2.1-alt1
- 3.28.2.1

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Sat Mar 17 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0.1-alt1
- 3.28.0.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Tue Feb 06 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Tue Oct 03 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Fri Jun 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt2
- fixed reqs (ALT #32594)

* Tue May 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Tue Apr 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Nov 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Tue Sep 13 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.92-alt1
- 3.21.92

* Tue May 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Thu Nov 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue Aug 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Jan 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.3.1-alt1
- 3.14.3.1

* Mon Jan 19 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt1
- 3.14.3

* Thu Nov 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2.1-alt1
- 3.12.2.1

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Sun Feb 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.3-alt1
- 3.10.3

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon Sep 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.92-alt1
- 3.9.92

* Thu Aug 29 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.90-alt1
- first build for people/gnome

