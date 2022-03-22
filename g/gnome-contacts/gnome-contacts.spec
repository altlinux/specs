%def_disable snapshot

%define ver_major 42
%define beta %nil
%define _libexecdir %_prefix/libexec
%define gst_api_ver 1.0
%define _name org.gnome.Contacts
%def_without cheese

Name: gnome-contacts
Version: %ver_major.0
Release: alt1%beta

Summary: Contacts manager for GNOME
License: GPL-2.0-or-later
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Contacts

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.58
%define gtk4_ver 4.6.0
%define vala_ver 0.40.10
%define tp_glib_ver 0.22.0
%define folks_ver 0.14
%define eds_ver 3.34
%define cheese_ver 3.5.90
%define geocode_ver 3.15.3
%define handy_ver 1.1.0
%define portal_ver 0.5

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools
BuildRequires: yelp-tools xsltproc docbook-dtds docbook-style-xsl libappstream-glib-devel valadoc
BuildRequires: libgio-devel >= %glib_ver libgtk4-devel >= %gtk4_ver pkgconfig(libadwaita-1)
BuildRequires:  libtelepathy-glib-devel >= %tp_glib_ver
BuildRequires: libfolks-devel >= %folks_ver libvala-devel >= %vala_ver libgnome-desktop3-devel
BuildRequires: libgnome-online-accounts-devel libgee0.8-devel evolution-data-server-devel >= %eds_ver
%{?_with_cheese:BuildRequires: gstreamer%gst_api_ver-devel libcheese-devel >= %cheese_ver}
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver
BuildRequires: libportal-devel >= %portal_ver

# for build from git
BuildRequires: libfolks-vala

%description
%name is a standalone contacts manager for GNOME desktop.

%prep
%setup -n %name-%version%beta

%build
%meson
# %{?_without_cheese:-Dcheese=false}
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_libexecdir/gnome-contacts-search-provider
%_datadir/applications/%_name.desktop
%_datadir/glib-2.0/schemas/%_name.gschema.xml
%_datadir/dbus-1/services/%_name.service
%_datadir/dbus-1/services/%_name.SearchProvider.service
%_datadir/gnome-shell/search-providers/%_name.search-provider.ini
%_iconsdir/hicolor/*/*/*
%_man1dir/%name.1.*
%_datadir/metainfo/%_name.appdata.xml
%doc NEWS README*

%changelog
* Tue Mar 22 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Mon Mar 14 2022 Yuri N. Sedunov <aris@altlinux.org> 42-alt0.5.beta
- 42.beta (ported to GTK4)

* Wed Sep 29 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Tue Mar 23 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Sat Nov 07 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Sat Sep 19 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38-alt1
- 3.38

* Fri Jun 19 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Fri Apr 17 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Wed Mar 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36-alt1
- 3.36

* Mon Jan 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34-alt1
- 3.34

* Thu Jun 20 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt2
- fixed build against libhandy-0.0.10

* Wed Apr 24 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32-alt1
- 3.32

* Wed Dec 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Tue Sep 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30-alt1
- 3.30

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Fri Apr 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Wed Jan 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26-alt1
- 3.26

* Wed Sep 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt2
- rebuilt against libedataserver-1.2.so.22

* Tue May 17 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Apr 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.19.91-alt2
- updated to 3.19.91-25-gf3dafae

* Thu Feb 25 2016 Yuri N. Sedunov <aris@altlinux.org> 3.19.91-alt1
- 3.19.91

* Thu Nov 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Wed Sep 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed Apr 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Thu Apr 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10-alt1
- 3.10.0

* Tue Jul 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Fri May 31 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Nov 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Mon Oct 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue May 08 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Thu Oct 20 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Wed Oct 19 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0.1-alt1
- 3.2.0.1

* Fri Sep 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.4.1-alt1
- first build for Sisyphus

