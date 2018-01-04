%def_disable snapshot

%define ver_major 3.26
%define xdg_name org.gnome.bijiben
%define _libexecdir %_prefix/libexec
%def_enable zeitgeist

Name: bijiben
Version: %ver_major.2
Release: alt2

Summary: Note editor for GNOME
License: LGPLv3+
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Bijiben

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.28
%define gtk_ver 3.11.4
%define tracker_ver 0.18
%define eds_ver 3.19.90

BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: tracker-devel >= %tracker_ver
BuildRequires: libxml2-devel libwebkit2gtk-devel
BuildRequires: libgnome-online-accounts-devel libuuid-devel
BuildRequires: evolution-data-server-devel >= %eds_ver libical-devel libicu-devel
BuildRequires: rpm-build-xdg gnome-common intltool yelp-tools libappstream-glib-devel
%{?_enable_zeitgeist:BuildRequires: libzeitgeist2.0-devel}

%description
Bijiben is an attempt to design an intuitive note editor with strong
desktop integration.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static \
	--disable-schemas-compile \
	--disable-update-mimedb
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_libexecdir/%name-shell-search-provider
%_desktopdir/%xdg_name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*x*/*/%xdg_name.png
%_iconsdir/hicolor/scalable/*/%xdg_name-symbolic.svg
%_datadir/gnome-shell/search-providers/%xdg_name-search-provider.ini
%_datadir/dbus-1/services/%xdg_name.SearchProvider.service
%_xdgmimedir/packages/%xdg_name.xml
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/appdata/%xdg_name.appdata.xml
%_datadir/metainfo/%xdg_name.appdata.xml
%doc README AUTHORS NEWS

%changelog
* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt2
- rebuilt against libical.so.3/libicu*.so.60

* Mon Oct 30 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Tue Aug 15 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Fri Jun 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- updated to 3_24_0-9-g5ce5172

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.2-alt1
- 3.21.2

* Tue May 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt2
- rebuilt against libical.so.2

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Sun Sep 20 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue May 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Sat Mar 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Mar 02 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.91-alt1
- 3.15.91

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon Aug 19 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Sat Jun 22 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Sat May 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Thu Apr 18 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Mar 18 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.92-alt1
- first build for people/gnome

